from __future__ import annotations

import datetime
import json
import uuid
from pathlib import Path
from typing import Any, Dict, Optional

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).resolve().parent
CLASSIC_STATE_BRIDGE_DIR = BASE_DIR / "classic_state_bridge"
SCHEMA_VERSION = 1
STORAGE_PREFIX = "esperanto-choice-classic"
SUPPORTED_APP_KINDS = {"vocab", "sentence"}
SUPPORTED_TARGET_LANGS = {"ja", "zh", "ko"}
CLASSIC_SESSION_TEXT = {
    "ja": {
        "restore_warning": "保存された途中クイズがあります。",
        "restore_button": "途中から再開",
        "discard_button": "保存データを破棄",
        "restore_error": "保存データを復元できませんでした。新しく開始してください。",
        "vocab_quiz": "単語クイズ",
        "sentence_quiz": "例文クイズ",
        "result": "結果画面",
        "spartan_remaining": "スパルタ復習 残り{count}問",
        "checking": "Q{current}/{total} の確認中",
        "question": "Q{current}/{total}",
        "user": "ユーザー",
        "saved": "保存",
    },
    "zh": {
        "restore_warning": "发现已保存的未完成测验。",
        "restore_button": "从中途继续",
        "discard_button": "丢弃保存数据",
        "restore_error": "无法恢复保存数据。请重新开始。",
        "vocab_quiz": "单词测验",
        "sentence_quiz": "例句测验",
        "result": "结果画面",
        "spartan_remaining": "强化复习 剩余{count}题",
        "checking": "Q{current}/{total} 确认中",
        "question": "Q{current}/{total}",
        "user": "用户",
        "saved": "保存",
    },
    "ko": {
        "restore_warning": "저장된 진행 중 퀴즈가 있습니다.",
        "restore_button": "이어서 재개",
        "discard_button": "저장 데이터 삭제",
        "restore_error": "저장 데이터를 복원하지 못했습니다. 새로 시작해 주세요.",
        "vocab_quiz": "단어 퀴즈",
        "sentence_quiz": "예문 퀴즈",
        "result": "결과 화면",
        "spartan_remaining": "스파르타 복습 남은 {count}문제",
        "checking": "Q{current}/{total} 확인 중",
        "question": "Q{current}/{total}",
        "user": "사용자",
        "saved": "저장",
    },
}

_classic_state_component = components.declare_component(
    "esperanto_classic_session_storage",
    path=str(CLASSIC_STATE_BRIDGE_DIR),
)


def classic_storage_key(app_kind: str, target_lang: str = "ja") -> str:
    app = _normalize_app_kind(app_kind)
    lang = _normalize_target_lang(target_lang)
    return f"{STORAGE_PREFIX}:{lang}:{app}:session:v{SCHEMA_VERSION}"


def render_classic_session_loader(app_kind: str, target_lang: str = "ja") -> Optional[Dict[str, Any]]:
    """Load a browser-local classic Streamlit quiz snapshot once per server session."""
    app = _normalize_app_kind(app_kind)
    if st.session_state.get("questions"):
        return None

    candidate_key = _candidate_key(app)
    candidate = st.session_state.get(candidate_key)
    if isinstance(candidate, dict):
        return candidate

    if st.session_state.get(_load_done_key(app)):
        return None

    request_id = st.session_state.setdefault(_load_request_key(app), str(uuid.uuid4()))
    value = _classic_state_component(
        command={
            "action": "load",
            "storageKey": classic_storage_key(app, target_lang),
            "requestId": request_id,
        },
        default=None,
        key=f"classic_session_loader_{app}",
        height=1,
    )
    if not (
        isinstance(value, dict)
        and value.get("type") == "loaded"
        and value.get("requestId") == request_id
    ):
        return None

    st.session_state[_load_done_key(app)] = True
    if not value.get("ok", False):
        return None

    snapshot = validate_classic_session_snapshot(
        value.get("payload"),
        expected_app_kind=app,
        expected_target_lang=target_lang,
    )
    if snapshot:
        st.session_state[candidate_key] = snapshot
        return snapshot
    return None


def render_classic_session_restore_prompt(app_kind: str, target_lang: str = "ja") -> bool:
    """Render a conservative opt-in restore prompt for a loaded snapshot."""
    app = _normalize_app_kind(app_kind)
    if st.session_state.get("questions"):
        return False

    snapshot = st.session_state.get(_candidate_key(app))
    if not isinstance(snapshot, dict):
        return False

    labels = _classic_text(target_lang)
    st.warning(labels["restore_warning"])
    st.caption(describe_classic_session_snapshot(snapshot))
    col_restore, col_discard = st.columns(2)
    if col_restore.button(labels["restore_button"], key=f"classic_restore_{app}", type="primary"):
        if apply_classic_session_snapshot(snapshot, expected_app_kind=app, expected_target_lang=target_lang):
            _forget_candidate(app)
            st.rerun()
        st.error(labels["restore_error"])
        request_classic_session_clear(app)
    if col_discard.button(labels["discard_button"], key=f"classic_discard_{app}"):
        _forget_candidate(app)
        request_classic_session_clear(app)
        st.rerun()
    return True


def render_classic_session_writer(app_kind: str, target_lang: str = "ja") -> None:
    """Persist or clear the browser-local classic quiz snapshot without reruns."""
    app = _normalize_app_kind(app_kind)
    clear_requested = bool(st.session_state.pop(_clear_requested_key(app), False))
    storage_key = classic_storage_key(app, target_lang)
    request_id = str(uuid.uuid4())

    if clear_requested or bool(st.session_state.get("score_saved", False)):
        _classic_state_component(
            command={
                "action": "clear",
                "storageKey": storage_key,
                "requestId": request_id,
            },
            default=None,
            key=f"classic_session_writer_{app}",
            height=1,
        )
        return

    snapshot = build_classic_session_snapshot(app, target_lang, st.session_state)
    if not snapshot:
        return

    _forget_candidate(app)
    _classic_state_component(
        command={
            "action": "save",
            "storageKey": storage_key,
            "requestId": request_id,
            "payload": snapshot,
        },
        default=None,
        key=f"classic_session_writer_{app}",
        height=1,
    )


def request_classic_session_clear(app_kind: str) -> None:
    app = _normalize_app_kind(app_kind)
    st.session_state[_clear_requested_key(app)] = True
    _forget_candidate(app)


def build_classic_session_snapshot(
    app_kind: str,
    target_lang: str,
    state: Any,
) -> Optional[Dict[str, Any]]:
    app = _normalize_app_kind(app_kind)
    lang = _normalize_target_lang(target_lang)
    questions = _get_state_value(state, "questions", [])
    if not isinstance(questions, list) or not questions:
        return None

    payload_state: Dict[str, Any] = {
        "questions": questions,
        "q_index": _get_state_value(state, "q_index", 0),
        "correct": _get_state_value(state, "correct", 0),
        "streak": _get_state_value(state, "streak", 0),
        "answers": _get_state_value(state, "answers", []),
        "showing_result": _get_state_value(state, "showing_result", False),
        "last_result_msg": _get_state_value(state, "last_result_msg", ""),
        "last_is_correct": _get_state_value(state, "last_is_correct", False),
        "spartan_mode": _get_state_value(state, "spartan_mode", False),
        "spartan_pending": _get_state_value(state, "spartan_pending", []),
        "in_spartan_round": _get_state_value(state, "in_spartan_round", False),
        "spartan_current_q_idx": _get_state_value(state, "spartan_current_q_idx", None),
        "spartan_attempts": _get_state_value(state, "spartan_attempts", 0),
        "spartan_correct_count": _get_state_value(state, "spartan_correct_count", 0),
        "show_option_audio": _get_state_value(state, "show_option_audio", True),
    }

    if app == "vocab":
        payload_state.update(
            {
                "user_name": _get_state_value(state, "user_name", ""),
                "seed": _get_state_value(state, "seed", 1),
                "group_id": _get_state_value(state, "group_id", None),
                "pos_select": _get_state_value(state, "pos_select", ""),
                "main_points": _get_state_value(state, "main_points", 0.0),
                "spartan_points": _get_state_value(state, "spartan_points", 0.0),
                "quiz_direction": _get_state_value(state, "quiz_direction", "eo_to_ja"),
                "last_correct_answer": _get_state_value(state, "last_correct_answer", ""),
            }
        )
    else:
        payload_state.update(
            {
                "sentence_user_name": _get_state_value(state, "sentence_user_name", ""),
                "direction": _get_state_value(state, "direction", "ja_to_eo"),
                "points_raw": _get_state_value(state, "points_raw", 0.0),
                "points_main": _get_state_value(state, "points_main", 0.0),
                "points_spartan_raw": _get_state_value(state, "points_spartan_raw", 0.0),
                "points_spartan_scaled": _get_state_value(state, "points_spartan_scaled", 0.0),
                "quiz_topic": _get_state_value(state, "quiz_topic", None),
                "quiz_subtopic": _get_state_value(state, "quiz_subtopic", None),
                "quiz_levels": _get_state_value(state, "quiz_levels", []),
            }
        )

    snapshot = {
        "version": SCHEMA_VERSION,
        "appKind": app,
        "targetLang": lang,
        "savedAt": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "state": payload_state,
    }
    try:
        plain_snapshot = json.loads(json.dumps(snapshot, ensure_ascii=False))
    except (TypeError, ValueError):
        return None
    return validate_classic_session_snapshot(
        plain_snapshot,
        expected_app_kind=app,
        expected_target_lang=lang,
    )


def validate_classic_session_snapshot(
    payload: Any,
    *,
    expected_app_kind: str,
    expected_target_lang: str = "ja",
) -> Optional[Dict[str, Any]]:
    app = _normalize_app_kind(expected_app_kind)
    lang = _normalize_target_lang(expected_target_lang)
    if not isinstance(payload, dict):
        return None
    if payload.get("version") != SCHEMA_VERSION:
        return None
    if payload.get("appKind") != app or payload.get("targetLang") != lang:
        return None

    raw_state = payload.get("state")
    if not isinstance(raw_state, dict):
        return None
    raw_questions = raw_state.get("questions")
    if not isinstance(raw_questions, list) or not raw_questions:
        return None
    question_validator = _is_valid_vocab_question if app == "vocab" else _is_valid_sentence_question
    questions = [q for q in raw_questions if question_validator(q)]
    if len(questions) != len(raw_questions):
        return None

    total = len(questions)
    spartan_pending = _sanitize_index_list(raw_state.get("spartan_pending"), total)
    in_spartan = bool(raw_state.get("in_spartan_round")) and bool(spartan_pending)
    spartan_current = _optional_index(raw_state.get("spartan_current_q_idx"), total)
    if spartan_current not in spartan_pending:
        spartan_current = None

    clean_state: Dict[str, Any] = {
        "questions": questions,
        "q_index": _clamp_int(raw_state.get("q_index"), 0, total, 0),
        "correct": _clamp_int(raw_state.get("correct"), 0, total, 0),
        "streak": _clamp_int(raw_state.get("streak"), 0, total, 0),
        "answers": _sanitize_answers(raw_state.get("answers"), total),
        "showing_result": bool(raw_state.get("showing_result")),
        "last_result_msg": _safe_str(raw_state.get("last_result_msg"), 300),
        "last_is_correct": bool(raw_state.get("last_is_correct")),
        "spartan_mode": bool(raw_state.get("spartan_mode")),
        "spartan_pending": spartan_pending,
        "in_spartan_round": in_spartan,
        "spartan_current_q_idx": spartan_current,
        "spartan_attempts": _clamp_int(raw_state.get("spartan_attempts"), 0, 99999, 0),
        "spartan_correct_count": _clamp_int(raw_state.get("spartan_correct_count"), 0, 99999, 0),
        "show_option_audio": bool(raw_state.get("show_option_audio", True)),
    }

    if app == "vocab":
        clean_state.update(
            {
                "user_name": _safe_str(raw_state.get("user_name"), 32),
                "seed": _clamp_int(raw_state.get("seed"), 1, 8192, 1),
                "group_id": _safe_optional_str(raw_state.get("group_id"), 120),
                "pos_select": _safe_str(raw_state.get("pos_select"), 80),
                "main_points": _safe_float(raw_state.get("main_points")),
                "spartan_points": _safe_float(raw_state.get("spartan_points")),
                "quiz_direction": _choice(raw_state.get("quiz_direction"), {"eo_to_ja", "ja_to_eo"}, "eo_to_ja"),
                "last_correct_answer": _safe_str(raw_state.get("last_correct_answer"), 200),
            }
        )
    else:
        clean_state.update(
            {
                "sentence_user_name": _safe_str(raw_state.get("sentence_user_name"), 32),
                "direction": _choice(raw_state.get("direction"), {"ja_to_eo", "eo_to_ja"}, "ja_to_eo"),
                "points_raw": _safe_float(raw_state.get("points_raw")),
                "points_main": _safe_float(raw_state.get("points_main")),
                "points_spartan_raw": _safe_float(raw_state.get("points_spartan_raw")),
                "points_spartan_scaled": _safe_float(raw_state.get("points_spartan_scaled")),
                "quiz_topic": _safe_optional_str(raw_state.get("quiz_topic"), 120),
                "quiz_subtopic": _safe_optional_str(raw_state.get("quiz_subtopic"), 120),
                "quiz_levels": _sanitize_levels(raw_state.get("quiz_levels")),
            }
        )

    return {
        "version": SCHEMA_VERSION,
        "appKind": app,
        "targetLang": lang,
        "savedAt": _safe_str(payload.get("savedAt"), 40),
        "state": clean_state,
    }


def apply_classic_session_snapshot(
    payload: Any,
    *,
    expected_app_kind: str,
    expected_target_lang: str = "ja",
) -> bool:
    snapshot = validate_classic_session_snapshot(
        payload,
        expected_app_kind=expected_app_kind,
        expected_target_lang=expected_target_lang,
    )
    if not snapshot:
        return False

    state = snapshot["state"]
    for key, value in state.items():
        st.session_state[key] = value

    st.session_state.score_saved = False
    st.session_state.pending_save_id = None
    st.session_state.score_refresh_needed = False
    st.session_state.score_sync_warning = None
    if snapshot["appKind"] == "vocab":
        st.session_state.last_saved_key = None
    else:
        st.session_state.sentence_saved_total_projection = None
    return True


def describe_classic_session_snapshot(snapshot: Dict[str, Any]) -> str:
    app = snapshot.get("appKind")
    labels = _classic_text(snapshot.get("targetLang"))
    state = snapshot.get("state") if isinstance(snapshot.get("state"), dict) else {}
    questions = state.get("questions") if isinstance(state.get("questions"), list) else []
    total = len(questions)
    q_index = _clamp_int(state.get("q_index"), 0, total, 0)
    if total and q_index >= total and not state.get("in_spartan_round"):
        progress = labels["result"]
    elif state.get("in_spartan_round"):
        progress = labels["spartan_remaining"].format(count=len(state.get("spartan_pending") or []))
    elif state.get("showing_result"):
        progress = labels["checking"].format(current=min(q_index + 1, total), total=total)
    else:
        progress = labels["question"].format(current=min(q_index + 1, total), total=total)

    label = labels["vocab_quiz"] if app == "vocab" else labels["sentence_quiz"]
    saved_at = _safe_str(snapshot.get("savedAt"), 40).replace("T", " ").replace("Z", " UTC")
    user = _safe_str(
        state.get("user_name") if app == "vocab" else state.get("sentence_user_name"),
        32,
    )
    user_part = f" / {labels['user']}: {user}" if user else ""
    saved_part = f" / {labels['saved']}: {saved_at}" if saved_at else ""
    return f"{label} / {progress}{user_part}{saved_part}"


def _normalize_app_kind(app_kind: str) -> str:
    app = str(app_kind or "").strip().lower()
    if app not in SUPPORTED_APP_KINDS:
        raise ValueError(f"Unsupported classic session app kind: {app_kind}")
    return app


def _normalize_target_lang(target_lang: str) -> str:
    lang = str(target_lang or "ja").strip().lower()
    return lang if lang in SUPPORTED_TARGET_LANGS else "ja"


def _classic_text(target_lang: str) -> Dict[str, str]:
    return CLASSIC_SESSION_TEXT[_normalize_target_lang(target_lang)]


def _candidate_key(app_kind: str) -> str:
    return f"_classic_session_candidate_{app_kind}"


def _load_done_key(app_kind: str) -> str:
    return f"_classic_session_load_done_{app_kind}"


def _load_request_key(app_kind: str) -> str:
    return f"_classic_session_load_request_{app_kind}"


def _clear_requested_key(app_kind: str) -> str:
    return f"_classic_session_clear_requested_{app_kind}"


def _forget_candidate(app_kind: str) -> None:
    st.session_state.pop(_candidate_key(app_kind), None)


def _get_state_value(state: Any, key: str, default: Any) -> Any:
    try:
        return state.get(key, default)
    except AttributeError:
        return default


def _is_valid_vocab_question(question: Any) -> bool:
    if not isinstance(question, dict):
        return False
    options = question.get("options")
    answer_index = question.get("answer_index")
    stages = question.get("stages")
    return (
        isinstance(question.get("prompt"), str)
        and isinstance(options, list)
        and 2 <= len(options) <= 4
        and isinstance(answer_index, int)
        and 0 <= answer_index < len(options)
        and isinstance(stages, list)
        and all(isinstance(stage, str) for stage in stages)
        and all(_is_valid_vocab_option(option) for option in options)
    )


def _is_valid_vocab_option(option: Any) -> bool:
    return (
        isinstance(option, dict)
        and isinstance(option.get("japanese"), str)
        and isinstance(option.get("esperanto"), str)
    )


def _is_valid_sentence_question(question: Any) -> bool:
    if not isinstance(question, dict):
        return False
    options = question.get("options")
    answer_index = question.get("answer_index")
    return (
        isinstance(question.get("prompt_eo"), str)
        and isinstance(question.get("prompt_ja"), str)
        and isinstance(options, list)
        and len(options) >= 4
        and isinstance(answer_index, int)
        and 0 <= answer_index < len(options)
        and all(_is_valid_sentence_option(option) for option in options)
    )


def _is_valid_sentence_option(option: Any) -> bool:
    return (
        isinstance(option, dict)
        and isinstance(option.get("phrase"), str)
        and isinstance(option.get("japanese"), str)
        and isinstance(option.get("phrase_id"), (int, str))
        and isinstance(option.get("level"), (int, float))
    )


def _sanitize_answers(value: Any, question_count: int) -> list:
    if not isinstance(value, list):
        return []
    answers = []
    for answer in value:
        if not isinstance(answer, dict):
            continue
        q_idx = _optional_index(answer.get("q_idx"), question_count)
        selected = answer.get("selected")
        correct = answer.get("correct")
        if q_idx is None or not isinstance(selected, int) or not isinstance(correct, int):
            continue
        clean = {
            "q_idx": q_idx,
            "selected": selected,
            "correct": correct,
        }
        if isinstance(answer.get("phase"), str):
            clean["phase"] = answer["phase"]
        if isinstance(answer.get("q"), str):
            clean["q"] = answer["q"]
        answers.append(clean)
    return answers


def _sanitize_index_list(value: Any, question_count: int) -> list:
    if not isinstance(value, list):
        return []
    seen = set()
    indexes = []
    for item in value:
        idx = _optional_index(item, question_count)
        if idx is not None and idx not in seen:
            seen.add(idx)
            indexes.append(idx)
    return indexes


def _sanitize_levels(value: Any) -> list:
    if not isinstance(value, list):
        return []
    levels = []
    seen = set()
    for item in value:
        level = _clamp_int(item, 1, 10, 0)
        if level and level not in seen:
            seen.add(level)
            levels.append(level)
    return levels


def _optional_index(value: Any, question_count: int) -> Optional[int]:
    try:
        idx = int(value)
    except (TypeError, ValueError):
        return None
    if idx < 0 or idx >= question_count:
        return None
    return idx


def _clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return min(max(number, minimum), maximum)


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if number != number or number in (float("inf"), float("-inf")):
        return default
    return number


def _safe_str(value: Any, max_length: int) -> str:
    return str(value or "").strip()[:max_length]


def _safe_optional_str(value: Any, max_length: int) -> Optional[str]:
    text = _safe_str(value, max_length)
    return text or None


def _choice(value: Any, choices: set, default: str) -> str:
    text = str(value or "")
    return text if text in choices else default
