import uuid

from score_append_utils import (
    append_score_row_fast,
    append_score_row_safe,
    compute_user_score_totals,
    load_sheet_records,
    upsert_user_total,
)
from score_row_utils import SENTENCE_MODE, VOCAB_MODE, normalize_mode, normalize_score_row


SCORES_SHEET = "Scores"
USER_STATS_SHEET = "UserStats"
USER_STATS_SENTENCE_SHEET = "UserStatsSentence"
SCORE_WRITE_RETRIES = 3
SCORE_WRITE_RETRY_BASE_SEC = 0.4


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


def _safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _score_result(payload, *, ok, message, warning=None):
    return {
        "type": "score_save_result",
        "requestId": str(payload.get("requestId", "")),
        "saveId": str(payload.get("saveId", "")),
        "ok": bool(ok),
        "message": message,
        "warning": warning or "",
    }


def _build_record(payload):
    mode = normalize_mode(payload.get("mode"), fallback=VOCAB_MODE)
    save_id = str(payload.get("saveId") or "").strip() or f"mobile-{uuid.uuid4()}"
    user = str(payload.get("user") or "").strip()
    levels = payload.get("levels")
    if isinstance(levels, (list, tuple)):
        levels = ",".join(str(level) for level in levels)
    else:
        levels = str(levels or "")

    common = {
        "user": user,
        "mode": mode,
        "correct": _safe_int(payload.get("correct"), 0),
        "total": _safe_int(payload.get("total"), 0),
        "accuracy": _safe_float(payload.get("accuracy"), 0.0),
        "points": _safe_float(payload.get("points"), 0.0),
        "spartan_attempts": _safe_int(payload.get("spartanAttempts"), 0),
        "spartan_correct": _safe_int(payload.get("spartanCorrect"), 0),
        "spartan_accuracy": _safe_float(payload.get("spartanAccuracy"), 0.0),
        "spartan_mode": bool(payload.get("spartanMode")),
        "direction": str(payload.get("direction") or ""),
        "accuracy_bonus": _safe_float(payload.get("accuracyBonus"), 0.0),
        "accuracy_bonus_spartan": 0.0,
        "source": "mobile_app",
        "mobile_session_id": str(payload.get("sessionId") or ""),
        "mobile_app_version": str(payload.get("appVersion") or ""),
        "started_at": str(payload.get("startedAt") or ""),
        "completed_at": str(payload.get("completedAt") or ""),
        "ts": str(payload.get("ts") or ""),
        "save_id": save_id,
    }

    if mode == SENTENCE_MODE:
        return normalize_score_row(
            {
                **common,
                "topic": str(payload.get("topic") or ""),
                "subtopic": str(payload.get("subtopic") or ""),
                "levels": levels,
                "raw_points": _safe_float(payload.get("rawPointsMain"), 0.0)
                + _safe_float(payload.get("spartanScaledPoints"), 0.0),
                "points_main": _safe_float(payload.get("rawPointsMain"), 0.0),
                "points_spartan_raw": _safe_float(payload.get("rawPointsSpartan"), 0.0),
                "points_spartan_scaled": _safe_float(payload.get("spartanScaledPoints"), 0.0),
            },
            fallback_mode=SENTENCE_MODE,
        )

    return normalize_score_row(
        {
            **common,
            "group_id": str(payload.get("groupId") or ""),
            "seed": _safe_int(payload.get("seed"), 1),
            "pos": str(payload.get("pos") or ""),
            "raw_points_total": _safe_float(payload.get("rawPointsTotal"), 0.0),
            "raw_points_main": _safe_float(payload.get("rawPointsMain"), 0.0),
            "raw_points_spartan": _safe_float(payload.get("rawPointsSpartan"), 0.0),
            "accuracy_bonus_main": _safe_float(payload.get("accuracyBonus"), 0.0),
            "spartan_scaled_points": _safe_float(payload.get("spartanScaledPoints"), 0.0),
        },
        fallback_mode=VOCAB_MODE,
    )


def _append_score(record):
    fast_saved = append_score_row_fast(record, worksheet_name=SCORES_SHEET)
    if fast_saved is True:
        return True
    return append_score_row_safe(
        record,
        worksheet_name=SCORES_SHEET,
        retries=SCORE_WRITE_RETRIES,
        retry_base_sec=SCORE_WRITE_RETRY_BASE_SEC,
    )


def _update_totals(record):
    records = load_sheet_records(SCORES_SHEET, refresh=True)
    if records is None:
        return False, False

    user = str(record.get("user") or "").strip()
    totals = compute_user_score_totals(records, user)
    ts = str(record.get("ts") or "")

    overall_ok = upsert_user_total(
        USER_STATS_SHEET,
        user=user,
        total_points=totals["overall"],
        last_updated=ts,
        retries=SCORE_WRITE_RETRIES,
        retry_base_sec=SCORE_WRITE_RETRY_BASE_SEC,
    )
    sentence_ok = True
    if record.get("mode") == SENTENCE_MODE:
        sentence_ok = upsert_user_total(
            USER_STATS_SENTENCE_SHEET,
            user=user,
            total_points=totals["sentence"],
            last_updated=ts,
            retries=SCORE_WRITE_RETRIES,
            retry_base_sec=SCORE_WRITE_RETRY_BASE_SEC,
        )
    return overall_ok, sentence_ok


def save_mobile_score_request(payload):
    if not isinstance(payload, dict) or payload.get("type") != "save_score":
        return _score_result({}, ok=False, message="保存要求の形式が不正です。")

    user = str(payload.get("user") or "").strip()
    if not user:
        return _score_result(payload, ok=False, message="保存するにはユーザー名が必要です。")

    record = _build_record(payload)
    if record["total"] <= 0:
        return _score_result(payload, ok=False, message="保存できるクイズ結果がありません。")

    if not _append_score(record):
        return _score_result(
            payload,
            ok=False,
            message="Google Sheetsへの保存に失敗しました。Secrets設定とSheets共有権限を確認してください。",
        )

    overall_ok, sentence_ok = _update_totals(record)
    if not overall_ok or not sentence_ok:
        return _score_result(
            payload,
            ok=False,
            message="スコアログは保存しましたが、累積得点の更新に失敗しました。もう一度保存を押すと再試行できます。",
        )

    points = _safe_float(record.get("points"), 0.0)
    return _score_result(
        payload,
        ok=True,
        message=f"ランキングに保存しました。今回の{points:.1f}点を累積得点に加算済みです。",
    )
