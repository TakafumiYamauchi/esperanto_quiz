import datetime

from score_append_utils import load_sheet_records
from score_row_utils import iter_unique_score_rows


SCORES_SHEET = "Scores"
USER_STATS_SHEET = "UserStats"
HOF_THRESHOLD = 1_000_000
RANKING_TOP_N = 20


def _safe_float(value, default=0.0):
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


def _parse_jst_date(value):
    raw = str(value or "").strip()
    if not raw:
        return None
    normalized = raw.replace("Z", "+00:00")
    try:
        parsed = datetime.datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=datetime.timezone.utc)
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return parsed.astimezone(jst).date()


def _score_log_totals(score_rows):
    jst = datetime.timezone(datetime.timedelta(hours=9))
    today = datetime.datetime.now(jst).date()
    month_start = today.replace(day=1)
    overall = {}
    today_totals = {}
    month_totals = {}

    for row in iter_unique_score_rows(score_rows or []):
        user = str(row.get("user") or "").strip()
        if not user:
            continue
        points = _safe_float(row.get("points"), 0.0)
        overall[user] = overall.get(user, 0.0) + points

        score_date = _parse_jst_date(row.get("ts") or row.get("completed_at"))
        if not score_date:
            continue
        if score_date == today:
            today_totals[user] = today_totals.get(user, 0.0) + points
        if score_date >= month_start:
            month_totals[user] = month_totals.get(user, 0.0) + points

    return overall, today_totals, month_totals


def _stats_totals(stats_rows):
    totals = {}
    for row in stats_rows or []:
        user = str(row.get("user") or "").strip()
        if not user:
            continue
        total = row.get("total_points")
        if total is None:
            for key, value in row.items():
                if "total_points" in str(key):
                    total = value
                    break
        totals[user] = max(totals.get(user, 0.0), _safe_float(total, 0.0))
    return totals


def _merge_max(primary, secondary):
    merged = dict(primary or {})
    for user, points in (secondary or {}).items():
        merged[user] = max(_safe_float(merged.get(user), 0.0), _safe_float(points, 0.0))
    return merged


def _rank_rows(totals, *, current_user="", top_n=RANKING_TOP_N):
    ranked = sorted(
        ((user, _safe_float(points, 0.0)) for user, points in (totals or {}).items() if str(user).strip()),
        key=lambda item: (-item[1], item[0].lower()),
    )
    rows = []
    current = None
    normalized_current = str(current_user or "").strip()
    for index, (user, points) in enumerate(ranked, start=1):
        row = {
            "rank": index,
            "user": user,
            "points": round(points, 1),
            "isCurrentUser": bool(normalized_current and user == normalized_current),
        }
        if index <= top_n:
            rows.append(row)
        if row["isCurrentUser"]:
            current = row
    if current and not any(row["user"] == current["user"] for row in rows):
        rows.append(current)
    return rows, current


def _ranking_result(payload, *, ok, message, rankings=None, own=None, source="unavailable"):
    return {
        "type": "rankings_result",
        "requestId": str(payload.get("requestId", "")),
        "ok": bool(ok),
        "message": message,
        "source": source,
        "rankings": rankings or {"overall": [], "today": [], "month": [], "hof": []},
        "own": own or {},
        "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


def load_mobile_rankings_request(payload):
    if not isinstance(payload, dict) or payload.get("type") != "load_rankings":
        return _ranking_result({}, ok=False, message="ランキング取得要求の形式が不正です。")

    user = str(payload.get("user") or "").strip()
    stats_rows = load_sheet_records(USER_STATS_SHEET, refresh=True)
    score_rows = load_sheet_records(SCORES_SHEET, refresh=True)

    if stats_rows is None and score_rows is None:
        return _ranking_result(
            payload,
            ok=False,
            message="ランキングを取得できませんでした。Secrets設定とSheets共有権限を確認してください。",
        )

    score_overall, today_totals, month_totals = _score_log_totals(score_rows or [])
    overall_totals = _merge_max(_stats_totals(stats_rows or []), score_overall)
    hof_totals = {name: points for name, points in overall_totals.items() if points >= HOF_THRESHOLD}

    overall_rows, own_overall = _rank_rows(overall_totals, current_user=user)
    today_rows, own_today = _rank_rows(today_totals, current_user=user)
    month_rows, own_month = _rank_rows(month_totals, current_user=user)
    hof_rows, own_hof = _rank_rows(hof_totals, current_user=user)

    source = "live"
    warning = ""
    if stats_rows is None:
        source = "scores_only"
        warning = "累積ランキングはScoresログ集計から表示しています。"
    elif score_rows is None:
        source = "stats_only"
        warning = "本日・今月ランキングはScoresログを取得できないため空表示です。"

    return _ranking_result(
        payload,
        ok=True,
        message=warning or "ランキングを更新しました。",
        source=source,
        rankings={
            "overall": overall_rows,
            "today": today_rows,
            "month": month_rows,
            "hof": hof_rows,
        },
        own={
            "overall": own_overall,
            "today": own_today,
            "month": own_month,
            "hof": own_hof,
        },
    )
