import datetime
import inspect
import random
import time
import uuid
from pathlib import Path

import streamlit as st
import pandas as pd

from data_sources import VOCAB_CSV
from quiz_scoring import (
    BASE_POINTS,
    SPARTAN_SCORE_MULTIPLIER,
    STREAK_BONUS,
    VOCAB_ACCURACY_BONUS as ACCURACY_BONUS_PER_Q,
    VOCAB_STAGE_FACTORS,
    compute_result_summary,
    scale_spartan_points,
    score_for_correct,
)
from ranking_utils import rank_dict as shared_rank_dict
from ranking_utils import summarize_rankings_from_stats as shared_summarize_rankings_from_stats
from score_sync_service import append_score_record, update_overall_user_stats
from score_row_utils import normalize_score_rows
from mobile_streamlit_bridge import render_mobile_app_entry
from classic_navigation import get_classic_quiz_mode, render_classic_mode_switch
from classic_session_persistence import (
    render_classic_session_loader,
    render_classic_session_restore_prompt,
    render_classic_session_writer,
    request_classic_session_clear,
)
import vocab_grouping as vg

# パス設定
# 語彙データ（日本語を含む多言語版）
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = VOCAB_CSV
AUDIO_DIR = BASE_DIR / "audio"
SCORE_FILE = Path("scores.json")

# 殿堂入りライン
HOF_THRESHOLD = 1000000
MOBILE_UA_TOKENS = (
    "iphone",
    "ipad",
    "ipod",
    "android",
    "mobile",
)
DESKTOP_UA_TOKENS = (
    "windows nt",
    "macintosh",
    "x11",
    "cros",
)
SCORE_READ_RETRIES = 3
SCORE_READ_RETRY_BASE_SEC = 0.35
SCORES_SHEET = "Scores"
USER_STATS_SHEET = "UserStats"
DEBUG_QUERY_VALUES = {"1", "true", "yes", "on"}
RECENT_SCORES_LIMIT = 200
AUDIO_CACHE_MAX_ENTRIES = 256

POS_JP = {
    "noun": "名詞",
    "verb": "動詞",
    "adjective": "形容詞",
    "adverb": "副詞",
    "preposition": "前置詞",
    "conjunction": "接続詞",
    "prefix": "接頭辞",
    "suffix": "接尾辞",
    "correlative": "相関詞",
    "numeral": "数詞",
    "bare_adverb": "原形副詞",
    "pronoun": "代名詞",
    "other": "その他",
}

STAGE_JP = {
    "beginner": "初級",
    "intermediate": "中級",
    "advanced": "上級",
}

# 出題方向
QUIZ_DIRECTIONS = {
    "eo_to_ja": "エスペラント → 日本語",
    "ja_to_eo": "日本語 → エスペラント",
}


@st.cache_data
def load_groups(seed: int, csv_mtime_ns: int):
    """
    vocab_grouping の関数シグネチャ差分を吸収する。
    デプロイ環境で旧版が読み込まれていても TypeError を避ける。
    """
    # CSV更新時にキャッシュを自動更新するため、mtimeをキーに含める。
    del csv_mtime_ns
    kwargs = {"seed": seed}
    try:
        sig = inspect.signature(vg.build_groups)
        if "audio_key_fn" in sig.parameters:
            kwargs["audio_key_fn"] = vg._default_audio_key
        if "translation_column" in sig.parameters:
            kwargs["translation_column"] = "Japanese_Trans"
    except Exception:
        # 署名取得に失敗した場合は最小引数でフォールバック
        pass
    return vg.build_groups(CSV_PATH, **kwargs)


def safe_mtime_ns(path: Path) -> int:
    try:
        return path.stat().st_mtime_ns
    except OSError:
        return 0


def is_mobile_client() -> bool:
    """ヘッダ(Client Hints含む) + URLパラメータでモバイル判定する。"""
    try:
        headers = st.context.headers
    except Exception:
        headers = {}
    normalized = {str(k).lower(): str(v).lower() for k, v in dict(headers).items()}
    ua = normalized.get("user-agent", "")
    ch_mobile = normalized.get("sec-ch-ua-mobile", "")
    ch_platform = normalized.get("sec-ch-ua-platform", "")
    qp_mobile = str(st.query_params.get("mobile", "")).strip().lower()

    if ch_mobile in {"?1", "1", "true"}:
        return True
    if any(token in ch_platform for token in ("android", "ios", "iphone", "ipad")):
        return True
    if any(token in ua for token in MOBILE_UA_TOKENS):
        return True

    qp_is_mobile = qp_mobile in {"1", "true", "yes", "on"}
    if not qp_is_mobile:
        return False

    # クエリ強制は「UA/Platformが取れない場合」か「明確なデスクトップでない場合」だけ許可。
    has_signal = bool(ua or ch_platform or ch_mobile)
    looks_desktop = (
        any(token in ch_platform for token in ("windows", "mac", "linux", "chrome os", "cros"))
        or any(token in ua for token in DESKTOP_UA_TOKENS)
    )
    if not has_signal:
        return True
    return not looks_desktop


def is_debug_mode() -> bool:
    raw = str(st.query_params.get("debug", "")).strip().lower()
    return raw in DEBUG_QUERY_VALUES


from streamlit_gsheets import GSheetsConnection


# -------- Google Sheets 連携 --------
# ローカルのJSONではなく、Google Sheetsをデータベースとして使用する
# 事前に .streamlit/secrets.toml に認証情報を設定する必要がある

def get_connection():
    try:
        return st.connection("gsheets", type=GSheetsConnection)
    except Exception as e:
        # User-facing warnings are handled by loader state to avoid duplicate error boxes.
        print(f"Google Sheets connection init failed: {e}")
        return None


def _read_sheet_with_retry(conn, worksheet: str, force_refresh: bool):
    ttl = 0 if force_refresh else 60
    last_error = None
    for attempt in range(SCORE_READ_RETRIES):
        try:
            return conn.read(worksheet=worksheet, ttl=ttl)
        except Exception as e:
            last_error = e
            if attempt + 1 < SCORE_READ_RETRIES:
                time.sleep(SCORE_READ_RETRY_BASE_SEC * (attempt + 1))
    if last_error is not None:
        raise last_error
    return pd.DataFrame()


def load_scores(force_refresh: bool = False):
    """Google Sheetsからスコアを読み込む"""
    conn = get_connection()
    cached_scores = st.session_state.get("cached_scores", [])
    if conn is None:
        if cached_scores:
            st.session_state.score_refresh_needed = False
            if force_refresh:
                st.session_state.score_load_error = "最新ランキングの再取得に失敗したため、前回のデータを表示しています。"
            else:
                st.session_state.score_load_error = "最新ランキングを取得できなかったため、前回のデータを表示しています。"
            return normalize_score_rows(cached_scores, fallback_mode="vocab")
        st.session_state.score_load_error = "Google Sheets 接続を初期化できませんでした。"
        st.session_state.score_refresh_needed = False
        return []
    try:
        # 一時的な通信失敗に備えて短いリトライを行う
        df = _read_sheet_with_retry(conn, worksheet=SCORES_SHEET, force_refresh=force_refresh)
        st.session_state.score_load_error = None
        st.session_state.score_refresh_needed = False
        if df is None or df.empty:
            return []
        # mode 欠損データを吸収しつつ返す
        return normalize_score_rows(df.to_dict(orient="records"), fallback_mode="vocab")
    except Exception as e:
        print(f"Ranking load error: {e}")
        if cached_scores:
            st.session_state.score_refresh_needed = False
            if force_refresh:
                st.session_state.score_load_error = f"最新ランキングの取得に失敗したため、前回のデータを表示しています: {e}"
            else:
                st.session_state.score_load_error = f"最新ランキングを取得できなかったため、前回のデータを表示しています: {e}"
            return normalize_score_rows(cached_scores, fallback_mode="vocab")
        st.session_state.score_load_error = f"ランキングの取得に失敗しました: {e}"
        st.session_state.score_refresh_needed = False
        return []


def _load_status(source: str = "unavailable", *, exact: bool = False, error: str = None):
    return {"source": source, "exact": exact, "error": error}


def _ranking_status_notice(status):
    if not status:
        return None, None
    source = status.get("source")
    if source == "cache":
        return "info", "全体ランキングの補助集計は前回取得したデータを暫定表示しています。"
    if source == "unavailable":
        return "warning", "全体ランキングの補助集計を取得できなかったため、Scores ログ集計ベースで表示しています。"
    return None, None


def save_score(record: dict):
    """Google Sheetsにスコアを追記する"""
    return append_score_record(record, fallback_mode="vocab")


def update_user_stats(user: str, points: float, ts: str):
    """UserStatsシート（累積スコア）を更新する"""
    del points
    ok = update_overall_user_stats(
        user=user,
        last_updated=ts,
    )
    if not ok:
        print("UserStats update error: row upsert failed.")
    return ok


def load_rankings(force_refresh: bool = False, *, include_status: bool = False):
    """ランキング用データをUserStatsから読み込む"""
    conn = get_connection()
    cached_rankings = st.session_state.get("cached_rankings", [])

    def finish(rows, *, source: str, exact: bool, error: str = None):
        status = _load_status(source, exact=exact, error=error)
        if include_status:
            return rows, status
        return rows

    if conn is None:
        if cached_rankings:
            return finish(
                cached_rankings,
                source="cache",
                exact=False,
                error="Google Sheets 接続を初期化できませんでした。",
            )
        return finish([], source="unavailable", exact=False, error="Google Sheets 接続を初期化できませんでした。")
    try:
        df = _read_sheet_with_retry(conn, worksheet=USER_STATS_SHEET, force_refresh=force_refresh)
        if df is None or df.empty:
            return finish([], source="live", exact=True)
        return finish(df.to_dict(orient="records"), source="live", exact=True)
    except Exception as e:
        if cached_rankings:
            return finish(cached_rankings, source="cache", exact=False, error=str(e))
        return finish([], source="unavailable", exact=False, error=str(e))


def safe_float(value, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        if isinstance(value, str) and not value.strip():
            return default
        parsed = float(value)
        if parsed != parsed or parsed in (float("inf"), float("-inf")):
            return default
        return parsed
    except (TypeError, ValueError):
        return default


def _get_user_total_from_rows(rows, user: str, field: str = "total_points"):
    normalized_user = str(user).strip()
    if not normalized_user or not rows:
        return None
    matched_total = None
    for row in rows:
        if str(row.get("user", "")).strip() != normalized_user:
            continue
        candidate = safe_float(row.get(field, 0), 0.0)
        if matched_total is None or candidate > matched_total:
            matched_total = candidate
    return matched_total


def _resolve_overall_points(user: str, score_rows, ranked_rows=None):
    normalized_user = str(user).strip()
    if not normalized_user:
        return 0.0, 0.0, 0.0, False

    vocab_total = sum(
        safe_float(r.get("points", 0), 0.0)
        for r in (score_rows or [])
        if str(r.get("user", "")).strip() == normalized_user and r.get("mode") != "sentence"
    )
    sentence_total = sum(
        safe_float(r.get("points", 0), 0.0)
        for r in (score_rows or [])
        if str(r.get("user", "")).strip() == normalized_user and r.get("mode") == "sentence"
    )
    log_total = vocab_total + sentence_total
    ranked_total = _get_user_total_from_rows(ranked_rows, normalized_user)
    candidates = [vocab_total, sentence_total, log_total]
    if ranked_total is not None:
        candidates.append(ranked_total)
    overall_total = max(candidates) if candidates else 0.0
    warning_needed = abs(log_total - overall_total) > 0.5
    return overall_total, vocab_total, sentence_total, warning_needed


def summarize_scores(scores):
    # JSTタイムゾーン設定 (UTC+9)
    jst = datetime.timezone(datetime.timedelta(hours=9))
    now_jst = datetime.datetime.now(jst)
    today_jst = now_jst.date()
    month_start_jst = today_jst.replace(day=1)

    totals = {}
    totals_today = {}
    totals_month = {}
    hof = {}
    for r in scores:
        user = str(r.get("user", "")).strip()
        if not user:
            continue
        pts = safe_float(r.get("points", 0), 0.0)
        ts = str(r.get("ts", "")).strip()
        date_obj = None
        if ts:
            # 旧データのゆるい日時表記も許容し、UTC基準でJST日付へ正規化する
            parsed_ts = pd.to_datetime(ts, errors="coerce", utc=True)
            if pd.notna(parsed_ts):
                date_obj = parsed_ts.tz_convert(jst).date()

        totals[user] = totals.get(user, 0) + pts
        if date_obj:
            if date_obj == today_jst:
                totals_today[user] = totals_today.get(user, 0) + pts
            if date_obj >= month_start_jst:
                totals_month[user] = totals_month.get(user, 0) + pts

        if totals[user] >= HOF_THRESHOLD:
            hof[user] = totals[user]
    return totals, totals_today, totals_month, hof


def summarize_rankings_from_stats(stats_data, score_rows=None):
    """UserStatsデータからランキングを作成"""
    scores = score_rows if score_rows is not None else load_scores()
    return shared_summarize_rankings_from_stats(
        stats_data,
        score_rows=scores,
        hof_threshold=HOF_THRESHOLD,
    )


def rank_dict(d, top_n=None):
    return shared_rank_dict(d, top_n=top_n)


def show_rankings(stats_data, score_rows=None, status=None):
    if is_debug_mode():
        with st.expander("Debug: Raw UserStats Data"):
            st.write("Raw Data:", stats_data)
            if st.button("Clear Cache & Rerun", key="clear_cache_vocab_debug"):
                st.cache_data.clear()
                st.rerun()

    notice_level, notice_text = _ranking_status_notice(status)
    if notice_text:
        getattr(st, notice_level)(notice_text)

    totals, totals_today, totals_month, hof = summarize_rankings_from_stats(stats_data, score_rows=score_rows)
    tabs = st.tabs(["累積", "本日", "今月", f"殿堂（{HOF_THRESHOLD}点以上）"])
    import pandas as pd

    def to_df(d):
        if not d:
            return pd.DataFrame(columns=["順位", "ユーザー", "得点"])
        # 得点順にソート
        items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        # データフレーム化 (順位をつける)
        data = []
        for i, (u, p) in enumerate(items, 1):
            data.append({"順位": i, "ユーザー": u, "得点": f"{p:.1f}"})
        return pd.DataFrame(data)

    with tabs[0]:
        st.dataframe(to_df(totals), use_container_width=True, hide_index=True)
    with tabs[1]:
        st.dataframe(to_df(totals_today), use_container_width=True, hide_index=True)
    with tabs[2]:
        st.dataframe(to_df(totals_month), use_container_width=True, hide_index=True)
    with tabs[3]:
        st.dataframe(to_df(hof), use_container_width=True, hide_index=True)


def render_cross_language_footer(current_key: str):
    links = [
        ("vocab_zh", "語彙版（中文）", "https://esperanto-quiz-zh.streamlit.app/?quiz=vocab&classic=1"),
        ("sentence_zh", "文章版（中文）", "https://esperanto-quiz-zh.streamlit.app/?quiz=sentence&classic=1"),
        ("vocab_ko", "단어 버전(한국어)", "https://esperanto-quiz-ko.streamlit.app/?quiz=vocab&classic=1"),
        ("sentence_ko", "예문 버전(한국어)", "https://esperanto-quiz-ko.streamlit.app/?quiz=sentence&classic=1"),
        ("vocab_ja", "語彙版（日本語）", "https://esperanto-quiz.streamlit.app/?quiz=vocab&classic=1"),
        ("sentence_ja", "文章版（日本語）", "https://esperanto-quiz.streamlit.app/?quiz=sentence&classic=1"),
    ]
    foreign_links = [item for item in links if item[0] != current_key]
    link_html = " ・ ".join(
        f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{label}</a>" for _, label, url in foreign_links
    )
    st.markdown(
        f"""
        <div style="margin-top: 1.4rem; padding-top: 0.55rem; border-top: 1px solid #e5e7eb; font-size: 0.80rem; color: #6b7280;">
            他言語版: {link_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def format_stage_label(stages):
    def map_stage(s):
        if s.startswith("beginner"):
            n = s.split("_")[1] if "_" in s else ""
            return f"{STAGE_JP['beginner']}{n}"
        if s.startswith("intermediate"):
            n = s.split("_")[1] if "_" in s else ""
            return f"{STAGE_JP['intermediate']}{n}"
        if s.startswith("advanced"):
            n = s.split("_")[1] if "_" in s else ""
            return f"{STAGE_JP['advanced']}{n}"
        return s

    return "+".join(map_stage(s) for s in stages)


def format_group_label(group):
    stage_label = format_stage_label(group.stages)
    gid = group.id.split(":")[-1]  # g1
    gid_num = gid[1:] if gid.startswith("g") else gid
    return f"{POS_JP.get(group.pos, group.pos)} / {stage_label} / グループ{gid_num} ({group.size}語)"


@st.cache_data(show_spinner=False, max_entries=AUDIO_CACHE_MAX_ENTRIES)
def find_audio(akey: str):
    """
    音声ファイルの読み込みをキャッシュして重複I/Oを防ぐ。
    キャッシュはヒット/ミス両方を保持する。
    """
    for ext, mime in [(".wav", "audio/wav"), (".mp3", "audio/mpeg"), (".ogg", "audio/ogg")]:
        fp = AUDIO_DIR / f"{akey}{ext}"
        if fp.exists():
            return fp.read_bytes(), mime
    return None, None


def simple_audio_player(akey: str, question_index: int = 0, instance: str = "default"):
    """
    シンプルな st.audio() ベースのプレイヤー
    - Streamlitがコンポーネントライフサイクルを管理するため、ゴーストiframe問題が発生しない
    - ブラウザ標準の再生速度調整機能を使用可能（Safari/Firefox等）
    """
    data, mime = find_audio(akey)
    if not data:
        st.info("音声ファイルなし")
        return

    format_map = {
        "audio/wav": "audio/wav",
        "audio/mpeg": "audio/mp3",
        "audio/ogg": "audio/ogg",
    }
    audio_format = format_map.get(mime, "audio/wav")
    # start_timeにランダムな微小オフセットを付与してID衝突を防ぐ（key引数は使えないため）
    offset = random.random() / 1000.0 + 1e-6
    with st.container():
        st.audio(data, format=audio_format, autoplay=True, start_time=offset)


def init_state():
    st.session_state.setdefault("user_name", "")
    st.session_state.setdefault("seed", 1)
    st.session_state.setdefault("group_id", None)
    st.session_state.setdefault("questions", [])
    st.session_state.setdefault("q_index", 0)
    st.session_state.setdefault("correct", 0)
    st.session_state.setdefault("main_points", 0.0)
    st.session_state.setdefault("spartan_points", 0.0)
    st.session_state.setdefault("streak", 0)
    st.session_state.setdefault("answers", [])
    st.session_state.setdefault("score_saved", False)
    st.session_state.setdefault("pending_save_id", None)
    st.session_state.setdefault("score_refresh_needed", False)
    st.session_state.setdefault("last_saved_key", None)
    st.session_state.setdefault("score_load_error", None)
    st.session_state.setdefault("score_sync_warning", None)
    st.session_state.setdefault("spartan_mode", False)
    st.session_state.setdefault("spartan_pending", [])
    st.session_state.setdefault("in_spartan_round", False)
    st.session_state.setdefault("spartan_current_q_idx", None)
    st.session_state.setdefault("spartan_attempts", 0)
    st.session_state.setdefault("spartan_correct_count", 0)
    st.session_state.setdefault("quiz_direction", "eo_to_ja")
    # UI State
    st.session_state.setdefault("showing_result", False)
    st.session_state.setdefault("last_result_msg", "")
    st.session_state.setdefault("last_is_correct", False)
    st.session_state.setdefault("last_correct_answer", "")
    st.session_state.setdefault("cached_scores", [])
    st.session_state.setdefault("cached_rankings", [])
    st.session_state.setdefault("cached_rankings_status", _load_status())
    st.session_state.setdefault("show_option_audio", True)


def start_quiz(group, rng):
    questions = vg.build_questions_for_group(group, rng=rng, min_options=2, max_options=4)
    st.session_state.questions = questions
    st.session_state.q_index = 0
    st.session_state.correct = 0
    st.session_state.main_points = 0.0
    st.session_state.spartan_points = 0.0
    st.session_state.streak = 0
    st.session_state.answers = []
    st.session_state.score_saved = False
    st.session_state.pending_save_id = None
    st.session_state.score_refresh_needed = False
    st.session_state.last_saved_key = None
    st.session_state.score_sync_warning = None
    st.session_state.showing_result = False
    st.session_state.spartan_pending = []
    st.session_state.in_spartan_round = False
    st.session_state.spartan_current_q_idx = None
    st.session_state.spartan_attempts = 0
    st.session_state.spartan_correct_count = 0


def main(*, set_page_config_once: bool = True):
    if set_page_config_once:
        st.set_page_config(
            page_title="エスペラントクイズ",
            page_icon="💚",
            layout="centered",
            initial_sidebar_state="expanded",
        )
    if get_classic_quiz_mode(default="vocab") == "sentence":
        from sentence_app import main as sentence_main

        sentence_main(set_page_config_once=False)
        return
    init_state()

    is_mobile = is_mobile_client()
    if render_mobile_app_entry(is_mobile, source="vocab_ja"):
        return
    if "mobile_compact_ui" not in st.session_state:
        st.session_state.mobile_compact_ui = is_mobile
    if "compact_hide_option_audio" not in st.session_state:
        st.session_state.compact_hide_option_audio = True
    if "compact_hide_prompt_audio" not in st.session_state:
        st.session_state.compact_hide_prompt_audio = True
    if "mobile_ultra_compact" not in st.session_state:
        st.session_state.mobile_ultra_compact = is_mobile
    if "mobile_hide_streamlit_chrome" not in st.session_state:
        st.session_state.mobile_hide_streamlit_chrome = False

    requested_compact_ui = bool(st.session_state.mobile_compact_ui)
    compact_ui = is_mobile and requested_compact_ui
    ultra_compact_ui = compact_ui and bool(st.session_state.mobile_ultra_compact)
    direction_for_style = st.session_state.get("quiz_direction", "eo_to_ja")
    base_font = "18px" if direction_for_style == "eo_to_ja" else "24px"
    mobile_font = (
        "34px"
        if (ultra_compact_ui and direction_for_style == "eo_to_ja")
        else (
            "38px"
            if ultra_compact_ui
            else (
                "32px"
                if (compact_ui and direction_for_style == "eo_to_ja")
                else ("36px" if compact_ui else ("24px" if direction_for_style == "eo_to_ja" else "30px"))
            )
        )
    )
    mobile_button_height = "148px" if ultra_compact_ui else ("168px" if compact_ui else "188px")
    mobile_button_padding = "8px" if ultra_compact_ui else ("10px" if compact_ui else "12px")
    mobile_main_title_font = "18px" if ultra_compact_ui else ("20px" if compact_ui else "24px")
    mobile_question_font = (
        "38px"
        if ultra_compact_ui
        else ("44px" if compact_ui else ("50px" if direction_for_style == "ja_to_eo" else "54px"))
    )
    mobile_option_font = (
        "51px"
        if (ultra_compact_ui and direction_for_style == "eo_to_ja")
        else (
            "57px"
            if ultra_compact_ui
            else (
                "48px"
                if (compact_ui and direction_for_style == "eo_to_ja")
                else ("54px" if compact_ui else ("36px" if direction_for_style == "eo_to_ja" else "45px"))
            )
        )
    )
    mobile_page_top_padding = "0.15rem" if ultra_compact_ui else ("0.35rem" if compact_ui else "0.9rem")
    mobile_page_bottom_padding = "0.2rem" if ultra_compact_ui else ("0.4rem" if compact_ui else "0.7rem")
    show_main_title = not (compact_ui and bool(st.session_state.get("questions")))
    main_title_html = "<div class='main-title'>エスペラント単語４択クイズ</div>" if show_main_title else ""
    mobile_chrome_css = (
        """
            div[data-testid="stToolbar"] {display: none !important;}
            #MainMenu {visibility: hidden !important;}
            footer {display: none !important;}
        """
        if st.session_state.mobile_hide_streamlit_chrome
        else ""
    )

    # エスペラント・グリーン (#009900) を基調としたテーマ設定
    st.markdown(
        f"""
        <style>
        @media (max-width: 768px) {{
            {mobile_chrome_css}
            .block-container {{
                padding-top: {mobile_page_top_padding} !important;
                padding-bottom: {mobile_page_bottom_padding} !important;
            }}
        }}
        div.stButton > button[kind="primary"] {{
            background-color: #009900 !important;
            border-color: #009900 !important;
            color: white !important;
            font-size: {base_font} !important;
            font-weight: 700 !important;
            line-height: 1.35 !important;
        }}
        div.stButton > button[kind="primary"]:hover {{
            background-color: #007700 !important;
            border-color: #007700 !important;
        }}
        div.stButton > button[kind="primary"]:active {{
            background-color: #005500 !important;
            border-color: #005500 !important;
        }}
        div.stButton > button[kind="secondary"] {{
            border-color: #009900 !important;
        }}
        [data-testid="stMain"] .stButton button {{
            height: 120px;
            min-height: 120px;
            max-height: 120px;
            width: 100% !important;
            white-space: normal;
            overflow: hidden;
            text-overflow: ellipsis;
            font-size: {base_font} !important;
            font-weight: 700 !important;
            line-height: 1.35 !important;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 12px;
        }}
        [data-testid="stMain"] .stButton button p, [data-testid="stMain"] .stButton button div, [data-testid="stMain"] .stButton button span {{
            font-size: {base_font} !important;
            font-weight: 700 !important;
            line-height: 1.35 !important;
        }}
        @media (max-width: 768px) {{
            [data-testid="stMain"] .stButton button {{
                height: auto;
                min-height: {mobile_button_height};
                max-height: none;
                overflow: visible;
                text-overflow: clip;
                white-space: normal;
                overflow-wrap: anywhere;
                word-break: break-word;
                font-size: {mobile_option_font} !important;
                font-weight: 700 !important;
                line-height: 1.35 !important;
                padding: {mobile_button_padding};
            }}
            [data-testid="stMain"] .stButton button p, [data-testid="stMain"] .stButton button div, [data-testid="stMain"] .stButton button span {{
                font-size: {mobile_option_font} !important;
                font-weight: 700 !important;
                line-height: 1.35 !important;
            }}
            [data-testid="stMain"] .stButton {{
                margin-bottom: 0.2rem !important;
            }}
            p {{
                margin-block-start: 0.2rem;
                margin-block-end: 0.2rem;
            }}
        }}
        .main-title {{
            font-size: 24px;
            font-weight: bold;
            color: #009900;
            margin-bottom: 10px;
            white-space: nowrap;
        }}
        .question-title {{
            font-size: {"20px" if direction_for_style == "ja_to_eo" else "22px"} !important;
            line-height: 1.3 !important;
            margin-top: 0.5rem;
            margin-bottom: 0.75rem;
        }}
        @media (max-width: 768px) {{
            .main-title {{
                font-size: {mobile_main_title_font} !important;
                margin-bottom: 0.3rem !important;
            }}
            .question-title {{
                font-size: {mobile_question_font} !important;
                line-height: 1.25 !important;
                margin-top: 0.2rem !important;
                margin-bottom: 0.45rem !important;
            }}
            .question-box.tight {{
                max-height: none;
                overflow: visible;
                margin-bottom: 0.35rem;
                padding-top: 0.35rem;
                padding-right: 0;
            }}
            .question-box.tight .question-title {{
                margin-top: 0.25rem !important;
                margin-bottom: 0.2rem !important;
            }}
            .compact-progress {{
                font-size: 24px;
                color: #0b6623;
                margin: 0.1rem 0 0.3rem 0;
            }}
            .compact-progress strong {{
                color: #0e8a2c;
            }}
            .question-audio-hint {{
                font-size: 22px;
                color: #0b6623;
                margin-bottom: 0.15rem;
            }}
        }}
        @media (max-width: 420px) {{
            .question-box.tight {{
                max-height: none;
            }}
            [data-testid="stMain"] .stButton button {{
                height: auto !important;
                min-height: 124px !important;
                max-height: none !important;
                overflow: visible !important;
                text-overflow: clip !important;
                white-space: normal !important;
                overflow-wrap: anywhere !important;
                word-break: break-word !important;
                padding: 8px !important;
                font-size: 45px !important;
            }}
            [data-testid="stMain"] .stButton button p, [data-testid="stMain"] .stButton button div, [data-testid="stMain"] .stButton button span, [data-testid="stMain"] .stButton button * {{
                font-size: 45px !important;
                line-height: 1.3 !important;
            }}
        }}
        </style>
        {main_title_html}
        """,
        unsafe_allow_html=True,
    )

    # モバイル用: 音声自動再生のアンロックスクリプト（グローバルに1回だけ挿入）
    # ユーザーが画面のどこかをタップしたら、サイレント音声を再生して
    # 以降の自動再生を可能にする
    st.markdown(
        """
        <script>
        (function() {
            try {
                const isNarrow = window.innerWidth <= 768;
                const looksMobileUA = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
                const params = new URLSearchParams(window.location.search);
                const hasMobileParam = params.get("mobile") === "1";
                if (isNarrow && looksMobileUA && !hasMobileParam) {
                    params.set("mobile", "1");
                    const target = window.location.pathname + "?" + params.toString() + window.location.hash;
                    window.location.replace(target);
                    return;
                }
                if ((!isNarrow || !looksMobileUA) && hasMobileParam) {
                    params.delete("mobile");
                    const query = params.toString();
                    const target = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
                    window.location.replace(target);
                    return;
                }
            } catch (_) {}
        })();

        (function() {
            // 既にアンロック済みならスキップ
            if (window._esperantoAudioUnlocked) return;

            const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
            if (!isMobile) {
                window._esperantoAudioUnlocked = true;
                return;
            }

            // sessionStorageでページ間のアンロック状態を維持
            if (sessionStorage.getItem('esperanto_audio_unlocked') === 'true') {
                window._esperantoAudioUnlocked = true;
                return;
            }

            function unlockAudio() {
                // サイレントな短いオーディオを再生してブラウザの制限を解除
                const silentAudio = new Audio('data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA=');
                silentAudio.volume = 0.01;
                silentAudio.play().then(() => {
                    console.log('Audio unlocked for mobile');
                    window._esperantoAudioUnlocked = true;
                    sessionStorage.setItem('esperanto_audio_unlocked', 'true');
                }).catch((e) => {
                    console.log('Silent audio play failed:', e);
                });
            }

            // 最初のユーザー操作でアンロック
            document.addEventListener('touchstart', unlockAudio, { once: true });
            document.addEventListener('click', unlockAudio, { once: true });
        })();

        (function() {
            if (window.__esperantoOptionAutoFitInstalled) {
                if (typeof window.__esperantoOptionAutoFitSchedule === "function") {
                    window.__esperantoOptionAutoFitSchedule();
                }
                return;
            }
            window.__esperantoOptionAutoFitInstalled = true;

            const MOBILE_BP = 768;
            const MIN_FONT_PX = 16;
            const MIN_RATIO = 0.62;
            const HEIGHT_TOLERANCE = 6;
            const MAX_STEPS = 22;

            function applySize(btn, nodes, px) {
                const size = `${px}px`;
                btn.style.fontSize = size;
                nodes.forEach((n) => {
                    n.style.fontSize = size;
                });
            }

            function fitOne(btn) {
                if (window.innerWidth > MOBILE_BP) return;
                const base = parseFloat(btn.dataset.baseFontPx || getComputedStyle(btn).fontSize || "0");
                if (!base || Number.isNaN(base)) return;
                if (!btn.dataset.baseFontPx) {
                    btn.dataset.baseFontPx = String(base);
                }

                const minHeight = parseFloat(getComputedStyle(btn).minHeight || "0");
                const targetHeight = (Number.isFinite(minHeight) && minHeight > 0) ? (minHeight + HEIGHT_TOLERANCE) : 180;
                const minFont = Math.max(MIN_FONT_PX, base * MIN_RATIO);
                const nodes = btn.querySelectorAll("p, div, span");

                applySize(btn, nodes, base);
                if (btn.offsetHeight <= targetHeight) return;

                let size = base;
                let step = 0;
                while (btn.offsetHeight > targetHeight && size > minFont && step < MAX_STEPS) {
                    size -= 1;
                    applySize(btn, nodes, size);
                    step += 1;
                }
            }

            function fitOptionButtons() {
                if (window.innerWidth > MOBILE_BP) return;
                const buttons = document.querySelectorAll('div.stButton > button[kind="primary"]');
                buttons.forEach(fitOne);
            }

            let rafId = null;
            function scheduleFit() {
                if (rafId !== null) return;
                rafId = window.requestAnimationFrame(() => {
                    rafId = null;
                    fitOptionButtons();
                });
            }

            window.__esperantoOptionAutoFitSchedule = scheduleFit;

            const observer = new MutationObserver(scheduleFit);
            observer.observe(document.body, { childList: true, subtree: true });
            window.addEventListener("resize", scheduleFit, { passive: true });
            scheduleFit();
        })();
        </script>
        """,
        unsafe_allow_html=True
    )

    render_classic_session_loader("vocab", target_lang="ja")
    render_classic_session_restore_prompt("vocab", target_lang="ja")

    def persist_classic_session():
        render_classic_session_writer("vocab", target_lang="ja")

    show_intro_block = not (compact_ui and bool(st.session_state.get("questions")))
    if show_intro_block:
        render_classic_mode_switch("vocab", "ja")
        st.write("品詞×レベルでグルーピングした単語から出題します。シードを変えるとグループ分けと順番が変わります。")
        with st.expander("スコア計算ルール"):
            st.markdown(
                "\n".join(
                    [
                        f"- 基礎点: {BASE_POINTS} × レベル倍率 "
                        f"(初級{VOCAB_STAGE_FACTORS['beginner']:.1f} / "
                        f"中級{VOCAB_STAGE_FACTORS['intermediate']:.1f} / "
                        f"上級{VOCAB_STAGE_FACTORS['advanced']:.1f})",
                        f"- 連続正解ボーナス: 2問目以降の連続正解1回につき +{STREAK_BONUS}",
                        f"- 精度ボーナス: 最終正答率 × 問題数 × {ACCURACY_BONUS_PER_Q}",
                        f"- スパルタ精度ボーナス: なし（復習分は基礎+難易度のみを{SPARTAN_SCORE_MULTIPLIER:.1f}倍で加算）",
                        "- グループを出し切ると結果画面でボーナス込みの合計を表示します。",
                    ]
                )
            )

    with st.sidebar:
        st.header("設定")
        # keyを指定することでステート管理をStreamlitに任せる
        user_name = st.text_input("ユーザー名 (スコア保存用)", key="user_name")
        if user_name and not str(user_name).strip():
            st.warning("空白だけのユーザー名ではスコアを保存できません。")
        seed = st.number_input("ランダムシード (1-8192)", min_value=1, max_value=8192, step=1, key="seed")
        # st.session_state.seed = seed # key="seed"にしたので不要
        # st.session_state.shuffle_every_time = st.checkbox("毎回ランダムに並べる（シード無視）", value=st.session_state.shuffle_every_time)
        try:
            groups = load_groups(seed, safe_mtime_ns(CSV_PATH))
        except Exception as e:
            st.error(f"問題データの読み込みに失敗しました: {e}")
            st.stop()
        if not groups:
            st.error("問題データが空です。CSV内容を確認してください。")
            st.stop()
        pos_list = sorted({g.pos for g in groups})
        pos_label_map = {p: POS_JP.get(p, p) for p in pos_list}
        pos_choice = st.selectbox("品詞を選択", pos_list, format_func=lambda p: pos_label_map.get(p, p), key="pos_select")
        group_options = [g for g in groups if g.pos == pos_choice]
        group_labels = [format_group_label(g) for g in group_options]
        choice = st.selectbox("グループを選択", group_labels)
        selected_group = group_options[group_labels.index(choice)] if group_options else None
        st.checkbox(
            f"スパルタモード（全問後に間違えた問題だけ正解するまでランダム出題・得点{SPARTAN_SCORE_MULTIPLIER:.1f}倍）",
            key="spartan_mode",
            disabled=bool(st.session_state.questions),
        )
        st.selectbox(
            "出題方向",
            options=list(QUIZ_DIRECTIONS.keys()),
            format_func=lambda k: QUIZ_DIRECTIONS[k],
            key="quiz_direction",
            disabled=bool(st.session_state.questions),
        )
        st.checkbox(
            "選択肢の音声を表示",
            value=st.session_state.show_option_audio,
            key="show_option_audio",
            help="オフにすると選択肢ごとの音声プレイヤーを非表示にして軽量化します。",
        )
        if is_mobile:
            st.checkbox(
                "従来版スマホ表示を圧縮",
                key="mobile_compact_ui",
                help="スマホ専用UIに問題がある場合の保険です。従来Streamlit版をスマホで開いた時だけ使います。",
            )
            if compact_ui:
                st.checkbox(
                    "スマホ最適化時は選択肢の音声を自動で隠す",
                    key="compact_hide_option_audio",
                    help="問題文の音声は維持しつつ、選択肢ごとの音声表示だけ抑制して縦スクロールを減らします。",
                )
                st.checkbox(
                    "スマホ最適化時は問題文音声プレイヤーを隠す",
                    key="compact_hide_prompt_audio",
                    help="設問+4択を1画面に収めやすくします。必要時のみOFFにして表示してください。",
                )
                st.checkbox(
                    "超圧縮モード（小画面向け）",
                    key="mobile_ultra_compact",
                    help="設問エリア・ボタンをさらに圧縮します。",
                )
                st.checkbox(
                    "スマホ時に上部メニュー類を隠す",
                    key="mobile_hide_streamlit_chrome",
                    help="縦領域を増やします。通常操作に戻したい場合はOFFにしてください。",
                )
            st.caption(f"端末判定: モバイル / 従来版圧縮: {'ON' if compact_ui else 'OFF'}")
        if st.button("クイズ開始", disabled=not selected_group, use_container_width=True):
            # 出題順は常にランダム（シードはグループ分けのみに使用）
            rng = random.Random()
            start_quiz(selected_group, rng=rng)
            st.session_state.group_id = selected_group.id

        st.markdown("---")
        # ホームに戻るボタンをクイズ開始ボタンと同様に横幅可変にし、見た目を揃える
        if st.button("🏠 ホームに戻る", use_container_width=True, type="primary", key="home-btn"):
            request_classic_session_clear("vocab")
            st.session_state.questions = []
            st.session_state.group_id = None
            st.session_state.q_index = 0
            st.session_state.correct = 0
            st.session_state.main_points = 0.0
            st.session_state.spartan_points = 0.0
            st.session_state.streak = 0
            st.session_state.answers = []
            st.session_state.showing_result = False
            st.session_state.score_saved = False
            st.session_state.pending_save_id = None
            st.session_state.score_refresh_needed = False
            st.session_state.last_saved_key = None
            st.session_state.score_sync_warning = None
            st.session_state.spartan_pending = []
            st.session_state.in_spartan_round = False
            st.session_state.spartan_current_q_idx = None
            st.session_state.spartan_attempts = 0
            st.session_state.spartan_correct_count = 0
            # ホームに戻る時はスコアを再読み込み
            st.session_state.cached_scores = load_scores(force_refresh=True)
            st.session_state.score_load_error = None
            st.rerun()

        st.markdown("---")
        st.markdown(
            "[📘 例文クイズはこちら](https://esperanto-quiz.streamlit.app/?quiz=sentence&classic=1)"
        )

    normalized_user_name = str(st.session_state.get("user_name", "")).strip()

    # スコア読み込み戦略:
    # 1. クイズ中（questionsがあり、結果画面でない）はAPIを呼ばない（キャッシュ使用）
    # 2. ホーム画面、結果画面、スコア保存直後はAPIを呼ぶ
    finished_quiz = (
        bool(st.session_state.questions)
        and st.session_state.q_index >= len(st.session_state.questions)
        and not st.session_state.in_spartan_round
    )
    should_load = (
        not st.session_state.questions
        or finished_quiz
        or st.session_state.score_saved
        or not st.session_state.cached_scores
    )

    force_refresh_scores = st.session_state.get("score_refresh_needed", False)
    if should_load:
        scores = load_scores(force_refresh=force_refresh_scores)
        st.session_state.cached_scores = scores
    else:
        scores = st.session_state.cached_scores

    rankings = st.session_state.get("cached_rankings", [])
    rankings_status = st.session_state.get("cached_rankings_status", _load_status())
    rankings_loaded = False

    def get_overall_rankings():
        nonlocal rankings, rankings_status, rankings_loaded
        if not rankings_loaded:
            rankings, rankings_status = load_rankings(
                force_refresh=force_refresh_scores,
                include_status=True,
            )
            st.session_state.cached_rankings = rankings
            st.session_state.cached_rankings_status = rankings_status
            rankings_loaded = True
        return rankings, rankings_status

    if st.session_state.get("score_load_error"):
        col_warn, col_btn = st.columns([4, 1])
        col_warn.warning(st.session_state.score_load_error)
        col_warn.caption("認証・通信エラー時のみ再試行してください。")
        if col_btn.button("再読み込み", key="retry_scores_vocab"):
            st.session_state.cached_scores = load_scores(force_refresh=True)
            st.session_state.score_load_error = None
            st.rerun()
    # サイドバーでユーザー名が入力されていれば累積を案内（scores読み込み後）
    user_total_vocab = None
    user_total_overall = None
    user_total_sentence = None
    if normalized_user_name and scores:
        with st.sidebar:
            st.markdown("---")
            # クイズ中はネットアクセスを避け、ログ合計を優先
            in_quiz = bool(st.session_state.questions) and not st.session_state.showing_result
            overall_stats = None
            overall_stats_status = _load_status(source="live", exact=True)
            if not in_quiz:
                overall_stats, overall_stats_status = get_overall_rankings()
            user_total_overall, user_total_vocab, user_total_sentence, warning_needed = _resolve_overall_points(
                normalized_user_name,
                score_rows=scores,
                ranked_rows=overall_stats,
            )
            st.info(f"現在の累積（単語）: {user_total_vocab:.1f}")
            st.info(f"現在の累積（全体）: {user_total_overall:.1f}")
            notice_level, notice_text = _ranking_status_notice(overall_stats_status)
            if notice_text:
                st.caption(notice_text)
            if warning_needed:
                if abs((user_total_vocab + user_total_sentence) - user_total_overall) > 0.5:
                    st.warning("累積（単語＋文章）と全体の合計に差分があります。少し時間をおいて再読み込みしてください。")

    # 古いセッション（フィールド欠落）を検出してリセット
    if st.session_state.questions:
        q0 = st.session_state.questions[0]
        if "prompt" not in q0 or "options" not in q0 or "answer_index" not in q0:
            request_classic_session_clear("vocab")
            st.session_state.questions = []
            st.session_state.q_index = 0
            st.session_state.correct = 0
            st.session_state.main_points = 0.0
            st.session_state.spartan_points = 0.0
            st.session_state.streak = 0
            st.session_state.answers = []
            st.session_state.showing_result = False
            st.warning("問題データを再生成します。サイドバーで再度『クイズ開始』を押してください。")

    if not st.session_state.questions:
        st.info("左のサイドバーからグループを選び、クイズを開始してください。")
        if scores:
            st.subheader("ランキング（単語のみ・ログ集計）")
            vocab_scores = [r for r in scores if r.get("mode") != "sentence"]
            _, vocab_today, vocab_month, vocab_hof = summarize_scores(vocab_scores)
            totals_vocab = {}
            for r in vocab_scores:
                u = str(r.get("user", "")).strip()
                if not u:
                    continue
                totals_vocab[u] = totals_vocab.get(u, 0) + safe_float(r.get("points", 0), 0.0)

            import pandas as pd
            def to_df_log(d):
                if not d:
                    return pd.DataFrame(columns=["順位", "ユーザー", "得点"])
                items = sorted(d.items(), key=lambda x: x[1], reverse=True)
                data = [{"順位": i, "ユーザー": u, "得点": f"{p:.1f}"} for i, (u, p) in enumerate(items, 1)]
                return pd.DataFrame(data)

            tabs_log = st.tabs(["累積", "本日", "今月", f"殿堂（{HOF_THRESHOLD}点以上）"])
            tabs_log[0].dataframe(to_df_log(totals_vocab), use_container_width=True, hide_index=True)
            tabs_log[1].dataframe(to_df_log(vocab_today), use_container_width=True, hide_index=True)
            tabs_log[2].dataframe(to_df_log(vocab_month), use_container_width=True, hide_index=True)
            tabs_log[3].dataframe(to_df_log(vocab_hof), use_container_width=True, hide_index=True)

            st.subheader("ランキング（全体: 単語+文章）")
            ranking_rows, ranking_rows_status = get_overall_rankings()
            show_rankings(ranking_rows, score_rows=scores, status=ranking_rows_status)
        persist_classic_session()
        render_cross_language_footer("vocab_ja")
        return

    q_index = st.session_state.q_index
    questions = st.session_state.questions
    # スパルタモードへの遷移判定
    if (
        q_index >= len(questions)
        and st.session_state.spartan_mode
        and st.session_state.spartan_pending
    ):
        st.session_state.in_spartan_round = True
    if (
        st.session_state.in_spartan_round
        and not st.session_state.spartan_pending
    ):
        st.session_state.in_spartan_round = False

    # 結果画面（通常モード or スパルタ未発動）
    if q_index >= len(questions) and not st.session_state.in_spartan_round:
        correct = st.session_state.correct
        total = len(questions)
        # スパルタ部の精度
        sp_attempts = st.session_state.spartan_attempts
        sp_correct = st.session_state.spartan_correct_count
        sp_accuracy = sp_correct / sp_attempts if sp_attempts else 0

        raw_points_main = st.session_state.main_points
        raw_points_spartan = st.session_state.spartan_points
        raw_points_total = raw_points_main + raw_points_spartan
        spartan_scaled = scale_spartan_points(raw_points_spartan)
        summary = compute_result_summary(
            mode="vocab",
            total=total,
            correct=correct,
            main_points=raw_points_main,
            spartan_scaled_points=spartan_scaled,
        )
        accuracy = summary["accuracy"]
        accuracy_bonus = summary["accuracyBonus"]
        points = summary["points"]
        st.subheader("結果")
        st.metric("正答率", f"{accuracy*100:.1f}%")
        st.metric("得点", f"{points:.1f}")
        if st.session_state.spartan_mode and sp_attempts:
            st.caption(f"スパルタモード: 復習分を通常の{SPARTAN_SCORE_MULTIPLIER*100:.0f}%で加算（精度ボーナスなし）")
            st.caption(f"スパルタ精度: {sp_accuracy*100:.1f}% ({sp_correct}/{sp_attempts})")
        st.write(f"正解 {correct} / {total}")
        st.write(
            f"内訳: 本編 基礎+難易度 {raw_points_main:.1f} / 精度ボーナス {accuracy_bonus:.1f}"
            f" / スパルタ 基礎+難易度 {raw_points_spartan:.1f}（精度ボーナスなし）"
            f" → 加算 {spartan_scaled:.1f}（{SPARTAN_SCORE_MULTIPLIER*100:.0f}%）"
        )
        st.caption("音声で再確認できます。")
        if normalized_user_name:
            existing_users = {str(r.get("user", "")).strip() for r in scores} if scores else set()
            if normalized_user_name in existing_users:
                st.info("このユーザー名は既にスコアがあります。累積に加算します。")
            if st.session_state.score_saved:
                st.success("スコアを保存しました！")
                if st.session_state.get("score_sync_warning"):
                    st.warning(st.session_state.score_sync_warning)
            else:
                if st.session_state.get("score_sync_warning"):
                    st.warning(st.session_state.score_sync_warning)
                st.caption("保存するとランキングにも反映されます。失敗したらもう一度お試しください。")
                if st.button("スコアを保存", key="save_score_btn", use_container_width=True):
                    now = datetime.datetime.utcnow().isoformat()
                    save_id = st.session_state.get("pending_save_id")
                    if not save_id:
                        save_id = str(uuid.uuid4())
                        st.session_state.pending_save_id = save_id
                    record = {
                        "user": normalized_user_name,
                        "group_id": st.session_state.group_id,
                        "seed": st.session_state.seed,
                        "correct": correct,
                        "total": total,
                        "accuracy": accuracy,
                        "points": points,
                        "raw_points_total": raw_points_total,
                        "raw_points_main": raw_points_main,
                        "raw_points_spartan": raw_points_spartan,
                        "accuracy_bonus_main": accuracy_bonus,
                        "accuracy_bonus_spartan": 0.0,
                        "spartan_scaled_points": spartan_scaled,
                        "spartan_attempts": sp_attempts,
                        "spartan_correct": sp_correct,
                        "spartan_accuracy": sp_accuracy,
                        "accuracy_bonus": accuracy_bonus,
                        "spartan_mode": st.session_state.spartan_mode,
                        "direction": st.session_state.quiz_direction,
                        "ts": now,
                        "save_id": save_id,
                    }
                    # Scores更新（ログ）を正本として先に保存する
                    if save_score(record):
                        # UserStats更新（累積）はベストエフォート
                        stats_ok = update_user_stats(normalized_user_name, points, now)
                        st.session_state.score_refresh_needed = True
                        if stats_ok:
                            st.session_state.score_saved = True
                            st.session_state.pending_save_id = None
                            st.session_state.score_sync_warning = None
                        else:
                            st.session_state.score_saved = False
                            st.session_state.score_sync_warning = (
                                "スコアログは保存済みです。累積スコア反映だけ失敗したため、"
                                "もう一度押すと同じ保存IDで安全に再更新します。"
                            )
                        st.rerun()
                    else:
                        st.error("保存に失敗しました。秘密情報（secrets）の設定を確認してください。")

        if scores:
            with st.expander(f"最近のスコア（最新{RECENT_SCORES_LIMIT}件）", expanded=False):
                # 列順を軽く整える（存在する列のみ）
                import pandas as pd
                preferred_cols = [
                    "ts",
                    "user",
                    "points",
                    "accuracy",
                    "correct",
                    "total",
                    "group_id",
                    "seed",
                    "direction",
                    "spartan_mode",
                    "raw_points_main",
                    "raw_points_spartan",
                    "spartan_scaled_points",
                    "spartan_attempts",
                    "spartan_correct",
                    "spartan_accuracy",
                    "accuracy_bonus_main",
                ]
                recent_rows = list(reversed(scores[-RECENT_SCORES_LIMIT:]))
                df_recent = pd.DataFrame(recent_rows)
                cols = [c for c in preferred_cols if c in df_recent.columns] if not df_recent.empty else []
                if cols:
                    df_recent = df_recent[cols + [c for c in df_recent.columns if c not in cols]]
                st.dataframe(df_recent, hide_index=True, use_container_width=True)
            st.subheader("ランキング（単語のみ・ログ集計）")
            vocab_scores = [r for r in scores if r.get("mode") != "sentence"]
            totals_vocab = {}
            for r in vocab_scores:
                u = str(r.get("user", "")).strip()
                if not u:
                    continue
                totals_vocab[u] = totals_vocab.get(u, 0) + safe_float(r.get("points", 0), 0.0)
            import pandas as pd
            def to_df_log(d):
                if not d:
                    return pd.DataFrame(columns=["順位", "ユーザー", "得点"])
                items = sorted(d.items(), key=lambda x: x[1], reverse=True)
                data = [{"順位": i, "ユーザー": u, "得点": f"{p:.1f}"} for i, (u, p) in enumerate(items, 1)]
                return pd.DataFrame(data)
            st.dataframe(to_df_log(totals_vocab), use_container_width=True, hide_index=True)
            st.subheader("ランキング（全体: 単語+文章）")
            ranking_rows, ranking_rows_status = get_overall_rankings()
            show_rankings(ranking_rows, score_rows=scores, status=ranking_rows_status)

        # 復習セクション
        st.subheader("復習")
        wrong = []
        correct_list = []
        direction_review = st.session_state.quiz_direction
        for ans in st.session_state.answers:
            idx = ans.get("q_idx", -1)
            if idx < 0 or idx >= len(st.session_state.questions):
                continue
            q = st.session_state.questions[idx]
            options = q.get("options") or []
            correct_idx = ans.get("correct", -1)
            if correct_idx < 0 or correct_idx >= len(options):
                continue
            selected = ans.get("selected")
            selected_text = ""
            if isinstance(selected, int) and 0 <= selected < len(options):
                selected_text = options[selected]["japanese"] if direction_review == "eo_to_ja" else options[selected]["esperanto"]
            answer_text = options[correct_idx]["japanese"]
            answer_eo = options[correct_idx]["esperanto"]
            entry = {
                "prompt": q["prompt"],
                "selected": selected_text,
                "answer": answer_text,
                "answer_eo": answer_eo,
                "phase": ans.get("phase", "main"),
                "audio_key": options[correct_idx].get("audio_key"),
            }
            if selected == correct_idx:
                correct_list.append(entry)
            else:
                wrong.append(entry)

        if wrong:
            st.markdown("### 間違えた問題")
            st.caption("音声で再確認できます。")
            for w in wrong:
                st.write(f"- {w['prompt']}: 正解「{w['answer']} / {w['answer_eo']}」、あなたの回答「{w['selected']}」 ({w['phase']})")
                if w.get("audio_key"):
                    data, mime = find_audio(w["audio_key"])
                    if data:
                        st.audio(data, format=mime, start_time=0)
        if correct_list:
            st.markdown("### 正解した問題（確認用）")
            st.caption("音声で確認だけできます。")
            for c in correct_list:
                st.write(f"- {c['prompt']}: {c['answer']} / {c['answer_eo']} ({c['phase']})")
                if c.get("audio_key"):
                    data, mime = find_audio(c["audio_key"])
                    if data:
                        st.audio(data, format=mime, start_time=0)
        if st.button("もう一度同じグループで再挑戦", key="retry_btn"):
            group = next(
                (
                    g
                    for g in load_groups(st.session_state.seed, safe_mtime_ns(CSV_PATH))
                    if g.id == st.session_state.group_id
                ),
                None,
            )
            if group:
                rng = random.Random()
                start_quiz(group, rng=rng)
                st.rerun()
        persist_classic_session()
        render_cross_language_footer("vocab_ja")
        return

    # 出題対象の選択（通常/スパルタ）
    in_spartan = st.session_state.in_spartan_round
    if in_spartan:
        pending = st.session_state.spartan_pending
        if not pending:
            st.session_state.in_spartan_round = False
            st.rerun()
        if (
            st.session_state.spartan_current_q_idx is None
            or st.session_state.spartan_current_q_idx not in pending
        ):
            st.session_state.spartan_current_q_idx = random.choice(pending)
        current_q_idx = st.session_state.spartan_current_q_idx
    else:
        current_q_idx = q_index

    question = questions[current_q_idx]
    audio_key = question["options"][question["answer_index"]].get("audio_key")
    direction = st.session_state.quiz_direction
    compact_question_ui = compact_ui

    # 出題単語（一番上に大きく表示）
    if direction == "ja_to_eo":
        prompt_display = question["options"][question["answer_index"]]["japanese"]
        option_labels = [opt["esperanto"] for opt in question["options"]]
    else:
        prompt_display = question["prompt"]
        option_labels = [opt["japanese"] for opt in question["options"]]
        # エス→日では問題文の音声を出題時に自動再生（下部には重複表示しない）
        if audio_key and not st.session_state.showing_result:
            hide_prompt_audio = compact_question_ui and st.session_state.get("compact_hide_prompt_audio", True)
            if not hide_prompt_audio:
                if not compact_question_ui:
                    st.caption(f"🔊 発音を聞く（問題文・自動再生）【{audio_key}】")
                simple_audio_player(audio_key, question_index=q_index, instance="prompt")
            else:
                st.markdown("<div class='question-audio-hint'>🔇 問題文音声はスマホ最適化で非表示</div>", unsafe_allow_html=True)

    if in_spartan:
        if not compact_question_ui:
            st.subheader(f"スパルタ復習 残り{len(st.session_state.spartan_pending)}問 / 全{len(questions)}問")
            st.caption("間違えた問題のみをランダムに出題しています。正解でリストから消えます。")
        title_prefix = "復習"
    else:
        title_prefix = f"Q{q_index+1}/{len(questions)}"
    question_box_cls = "question-box tight" if ultra_compact_ui else "question-box"
    st.markdown(
        f"<div class='{question_box_cls}'><h3 class='question-title'>{title_prefix}: {prompt_display}</h3></div>",
        unsafe_allow_html=True,
    )
    # 進捗インジケータ（モバイルで邪魔にならないよう小さめ）
    total_questions = len(questions)
    correct_so_far = st.session_state.correct
    remaining = len(st.session_state.spartan_pending) if in_spartan else max(total_questions - st.session_state.q_index, 0)
    if compact_question_ui:
        st.markdown(
            f"<div class='compact-progress'>"
            f"正解 <strong>{correct_so_far}/{total_questions}</strong> ・ "
            f"連続 <strong>{st.session_state.streak}回</strong> ・ "
            f"残り <strong>{remaining}問</strong>"
            f"</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .mini-metrics {font-size: 14px; line-height: 1.2; margin-top: 0; color: #0b6623;}
            .mini-metrics strong {font-size: 16px; color: #0e8a2c;}
            </style>
            """,
            unsafe_allow_html=True,
        )
        col_left, _ = st.columns([2, 5], gap="small")
        with col_left:
            cols_prog = st.columns([1, 1, 1], gap="small")
            cols_prog[0].markdown(f"<div class='mini-metrics'>正解数<br><strong>{correct_so_far}/{total_questions}</strong></div>", unsafe_allow_html=True)
            cols_prog[1].markdown(f"<div class='mini-metrics'>連続正解 <strong>{st.session_state.streak}回</strong></div>", unsafe_allow_html=True)
            cols_prog[2].markdown(f"<div class='mini-metrics'>残り<br><strong>{remaining}問</strong></div>", unsafe_allow_html=True)

    # 結果表示モードの場合
    showing_result = st.session_state.showing_result
    if showing_result:
        # 結果を表示
        if st.session_state.last_is_correct:
            st.success(st.session_state.last_result_msg)
        else:
            st.error(st.session_state.last_result_msg)

        # 問題文の音声（結果画面でのみ再生）
        if audio_key:
            st.markdown("---")
            st.caption(f"🔊 発音を確認（自動再生）【{audio_key}】")
            simple_audio_player(audio_key, question_index=q_index, instance="result")

        # 「次へ」ボタン
        if st.button("次へ進む", type="primary", use_container_width=True, key=f"next_btn_{st.session_state.q_index}_{'sp' if in_spartan else 'main'}"):
            if in_spartan:
                st.session_state.showing_result = False
                st.session_state.spartan_current_q_idx = None
            else:
                st.session_state.q_index += 1
                st.session_state.showing_result = False
            st.rerun()
        persist_classic_session()
        render_cross_language_footer("vocab_ja")
        return

    # 回答待ちモード: 4択ボタンを出題直下に配置（出題方向でラベル切り替え）
    clicked_index = None
    # 4択の各選択肢の音声は常に表示（方向に関わらず）
    show_audio = st.session_state.get("show_option_audio", True)
    if compact_question_ui and st.session_state.get("compact_hide_option_audio", True):
        show_audio = False

    for row_start in range(0, len(option_labels), 2):
        cols = st.columns([1, 1], gap="small" if compact_question_ui else "medium")
        for j in range(2):
            idx = row_start + j
            if idx >= len(option_labels):
                continue
            with cols[j]:
                button_key = f"opt-{current_q_idx}-{idx}-{'sp' if in_spartan else 'main'}"
                if st.button(option_labels[idx], key=button_key, use_container_width=True, type="primary"):
                    clicked_index = idx
                if show_audio:
                    opt_audio = question["options"][idx].get("audio_key")
                    if opt_audio:
                        data, mime = find_audio(opt_audio)
                        if data:
                            st.audio(data, format=mime, start_time=0)


    if clicked_index is not None:
        is_correct = clicked_index == question["answer_index"]
        if in_spartan:
            st.session_state.spartan_attempts += 1
        st.session_state.answers.append(
            {
                "q_idx": current_q_idx,
                "q": question["prompt"],
                "selected": clicked_index,
                "correct": question["answer_index"],
                "phase": "spartan" if in_spartan else "main",
            }
        )

        if is_correct:
            # 正解時は即座に次へ（ユーザー要望）
            st.session_state.streak += 1
            earned = score_for_correct(
                mode="vocab",
                streak=st.session_state.streak,
                stages=question["stages"],
            )

            if not in_spartan:
                st.session_state.main_points += earned
                st.session_state.correct += 1
                st.session_state.q_index += 1
                st.session_state.showing_result = False
            else:
                st.session_state.spartan_points += earned
                st.session_state.spartan_correct_count += 1
                # 復習リストから除外して次のランダムへ
                st.session_state.spartan_pending = [
                    idx for idx in st.session_state.spartan_pending if idx != current_q_idx
                ]
                st.session_state.spartan_current_q_idx = None
                st.session_state.showing_result = False
                if not st.session_state.spartan_pending:
                    st.session_state.in_spartan_round = False
            st.rerun()
        else:
            # 不正解時は正解を表示して一時停止
            msg = f"不正解。正解: {option_labels[question['answer_index']]}"
            st.session_state.streak = 0
            # 初回フェーズでの誤答はスパルタ対象に追加
            if st.session_state.spartan_mode and not in_spartan:
                if current_q_idx not in st.session_state.spartan_pending:
                    st.session_state.spartan_pending.append(current_q_idx)

            # 結果表示モードへ移行
            st.session_state.showing_result = True
            st.session_state.last_result_msg = msg
            st.session_state.last_is_correct = False
            st.session_state.last_correct_answer = option_labels[question['answer_index']]
            st.rerun()

    persist_classic_session()
    render_cross_language_footer("vocab_ja")


if __name__ == "__main__":
    main()
