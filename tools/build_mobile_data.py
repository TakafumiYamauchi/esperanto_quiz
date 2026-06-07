#!/usr/bin/env python3
"""Build compact JSON payloads for the mobile-first static quiz app."""

from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from vocab_grouping import _default_audio_key, classify_pos  # noqa: E402
from data_sources import PHRASE_ID_OFFSET  # noqa: E402


VOCAB_CSV = ROOT / "2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv"
PHRASE_CSV = ROOT / "phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv"
OUT_DIR = ROOT / "mobile_app" / "data"
VOCAB_AUDIO_DIR = ROOT / "audio"
PHRASE_AUDIO_DIR = ROOT / "Esperanto例文5000文_収録音声"


def _clean(value: object) -> str:
    return str(value or "").strip()


def _safe_float(value: str) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(parsed):
        return None
    return parsed


def _safe_int(value: str) -> int | None:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def _translations(row: dict[str, str], mapping: dict[str, str], fallback: str) -> dict[str, str]:
    values = {lang: _clean(row.get(column)) for lang, column in mapping.items()}
    fallback_text = _clean(fallback)
    return {
        "ja": values.get("ja") or fallback_text,
        "zh": values.get("zh") or values.get("ja") or fallback_text,
        "ko": values.get("ko") or values.get("ja") or fallback_text,
    }


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    path.write_text(data + "\n", encoding="utf-8")


def _phrase_audio_key(phrase_id: int, phrase: str) -> str:
    return f"{phrase_id - PHRASE_ID_OFFSET:04d}_{_default_audio_key(phrase)}"


def build_vocab_payload() -> dict[str, object]:
    entries: list[dict[str, object]] = []
    for index, row in enumerate(_read_csv(VOCAB_CSV)):
        esperanto = _clean(row.get("Esperanto"))
        japanese = _clean(row.get("Japanese_Trans"))
        translations = _translations(
            row,
            {
                "ja": "Japanese_Trans",
                "zh": "Chinese_Trans",
                "ko": "Korean_Trans",
            },
            japanese,
        )
        level = _safe_float(_clean(row.get("Unified_Level")))
        if not esperanto or not japanese or level is None:
            continue
        audio_key = _default_audio_key(esperanto)
        entries.append(
            {
                "id": index,
                "eo": esperanto,
                "ja": japanese,
                "translations": translations,
                "level": level,
                "pos": classify_pos(esperanto),
                "audioKey": audio_key,
                "hasAudio": (VOCAB_AUDIO_DIR / f"{audio_key}.wav").exists(),
            }
        )

    return {
        "schema": 1,
        "source": VOCAB_CSV.name,
        "count": len(entries),
        "entries": entries,
    }


def build_sentence_payload() -> dict[str, object]:
    entries: list[dict[str, object]] = []
    for row in _read_csv(PHRASE_CSV):
        phrase_id = _safe_int(_clean(row.get("PhraseID")))
        level = _safe_int(_clean(row.get("LevelID")))
        topic = _clean(row.get("TopicName_EN"))
        subtopic = _clean(row.get("SubtopicName_EN"))
        phrase = _clean(row.get("Esperanto"))
        japanese = _clean(row.get("日本語"))
        translations = _translations(
            row,
            {
                "ja": "日本語",
                "zh": "中文",
                "ko": "한국어",
            },
            japanese,
        )
        if phrase_id is None or level is None:
            continue
        if not topic or not subtopic or not phrase or not japanese:
            continue
        audio_key = _phrase_audio_key(phrase_id, phrase)
        entries.append(
            {
                "id": phrase_id,
                "level": level,
                "levelName": _clean(row.get("LevelName_EN")),
                "topic": topic,
                "subtopic": subtopic,
                "eo": phrase,
                "ja": japanese,
                "translations": translations,
                "audioKey": audio_key,
                "hasAudio": (PHRASE_AUDIO_DIR / f"{audio_key}.wav").exists(),
            }
        )

    return {
        "schema": 1,
        "source": PHRASE_CSV.name,
        "count": len(entries),
        "entries": entries,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    vocab_payload = build_vocab_payload()
    sentence_payload = build_sentence_payload()
    _write_json(OUT_DIR / "vocab.json", vocab_payload)
    _write_json(OUT_DIR / "sentences.json", sentence_payload)
    print(f"wrote vocab.json ({vocab_payload['count']} entries)")
    print(f"wrote sentences.json ({sentence_payload['count']} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
