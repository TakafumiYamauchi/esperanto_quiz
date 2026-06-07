#!/usr/bin/env python3
"""Validate mobile quiz data, audio keys, manifests, and WAV assets."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import wave
from collections import Counter
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from vocab_grouping import _default_audio_key  # noqa: E402
from data_sources import PHRASE_ID_OFFSET  # noqa: E402


VOCAB_CSV = ROOT / "2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv"
PHRASE_CSV = ROOT / "phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv"
VOCAB_JSON = ROOT / "mobile_app" / "data" / "vocab.json"
SENTENCE_JSON = ROOT / "mobile_app" / "data" / "sentences.json"
AUDIO_MANIFEST_JSON = ROOT / "mobile_app" / "data" / "audio_manifest.json"
VOCAB_AUDIO_DIR = ROOT / "audio"
MOBILE_VOCAB_AUDIO_DIR = ROOT / "mobile_app" / "audio"
SENTENCE_AUDIO_DIR = ROOT / "Esperanto例文5000文_収録音声"
MOBILE_SENTENCE_AUDIO_DIR = ROOT / "mobile_app" / "sentence-audio"

FILE_ID_RE = re.compile(r"^[-_A-Za-z0-9]+$")


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


def clean(value: object) -> str:
    return str(value or "").strip()


def safe_float(value: object) -> float | None:
    try:
        return float(clean(value))
    except (TypeError, ValueError):
        return None


def safe_int(value: object) -> int | None:
    try:
        return int(float(clean(value)))
    except (TypeError, ValueError):
        return None


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json_object(path: Path, report: ValidationReport) -> dict[str, Any]:
    if not path.exists():
        report.error(f"missing JSON file: {path.relative_to(ROOT)}")
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        report.error(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(payload, dict):
        report.error(f"{path.relative_to(ROOT)} must be a JSON object")
        return {}
    return payload


def phrase_audio_key(phrase_id: int, phrase: str) -> str:
    return f"{phrase_id - PHRASE_ID_OFFSET:04d}_{_default_audio_key(phrase)}"


def expected_translations(row: dict[str, str], mapping: dict[str, str], fallback: str) -> dict[str, str]:
    values = {lang: clean(row.get(column)) for lang, column in mapping.items()}
    fallback_text = clean(fallback)
    return {
        "ja": values.get("ja") or fallback_text,
        "zh": values.get("zh") or values.get("ja") or fallback_text,
        "ko": values.get("ko") or values.get("ja") or fallback_text,
    }


def expected_vocab_rows(report: ValidationReport) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, row in enumerate(read_csv(VOCAB_CSV)):
        esperanto = clean(row.get("Esperanto"))
        japanese = clean(row.get("Japanese_Trans"))
        level = safe_float(row.get("Unified_Level"))
        if not esperanto or not japanese or level is None:
            continue
        rows.append(
            {
                "id": index,
                "eo": esperanto,
                "ja": japanese,
                "translations": expected_translations(
                    row,
                    {
                        "ja": "Japanese_Trans",
                        "zh": "Chinese_Trans",
                        "ko": "Korean_Trans",
                    },
                    japanese,
                ),
                "level": level,
                "audioKey": _default_audio_key(esperanto),
            }
        )
    if not rows:
        report.error("vocab CSV produced no valid rows")
    return rows


def expected_sentence_rows(report: ValidationReport) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in read_csv(PHRASE_CSV):
        phrase_id = safe_int(row.get("PhraseID"))
        level = safe_int(row.get("LevelID"))
        topic = clean(row.get("TopicName_EN"))
        subtopic = clean(row.get("SubtopicName_EN"))
        phrase = clean(row.get("Esperanto"))
        japanese = clean(row.get("日本語"))
        if phrase_id is None or level is None:
            continue
        if not topic or not subtopic or not phrase or not japanese:
            continue
        rows.append(
            {
                "id": phrase_id,
                "eo": phrase,
                "ja": japanese,
                "translations": expected_translations(
                    row,
                    {
                        "ja": "日本語",
                        "zh": "中文",
                        "ko": "한국어",
                    },
                    japanese,
                ),
                "level": level,
                "topic": topic,
                "subtopic": subtopic,
                "audioKey": phrase_audio_key(phrase_id, phrase),
            }
        )
    if not rows:
        report.error("sentence CSV produced no valid rows")
    return rows


def entries_from_payload(path: Path, payload: dict[str, Any], report: ValidationReport) -> list[dict[str, Any]]:
    entries = payload.get("entries")
    if not isinstance(entries, list):
        report.error(f"{path.relative_to(ROOT)}: entries must be a list")
        return []
    count = payload.get("count")
    if count != len(entries):
        report.error(f"{path.relative_to(ROOT)}: count={count!r} does not match entries={len(entries)}")
    return [entry for entry in entries if isinstance(entry, dict)]


def validate_entries(
    label: str,
    entries: list[dict[str, Any]],
    expected_rows: list[dict[str, Any]],
    audio_dir: Path,
    mobile_audio_dir: Path,
    report: ValidationReport,
) -> set[str]:
    expected_by_id = {row["id"]: row for row in expected_rows}
    entries_by_id = {entry.get("id"): entry for entry in entries}
    if len(entries_by_id) != len(entries):
        report.error(f"{label}: duplicate ids in mobile data")
    missing_ids = sorted(set(expected_by_id) - set(entries_by_id))
    extra_ids = sorted(set(entries_by_id) - set(expected_by_id))
    if missing_ids:
        report.error(f"{label}: {len(missing_ids)} CSV ids missing from mobile JSON: {sample(missing_ids)}")
    if extra_ids:
        report.error(f"{label}: {len(extra_ids)} mobile JSON ids not found in CSV: {sample(extra_ids)}")

    audio_keys: set[str] = set()
    for entry in entries:
        entry_id = entry.get("id")
        expected = expected_by_id.get(entry_id)
        prefix = f"{label} id={entry_id!r}"
        for field in ("eo", "ja", "audioKey"):
            if not clean(entry.get(field)):
                report.error(f"{prefix}: missing {field}")
        if not isinstance(entry.get("hasAudio"), bool):
            report.error(f"{prefix}: hasAudio must be boolean")
        if expected:
            for field in ("eo", "ja", "audioKey"):
                if clean(entry.get(field)) != clean(expected.get(field)):
                    report.error(
                        f"{prefix}: {field} mismatch: data={clean(entry.get(field))!r}, "
                        f"expected={clean(expected.get(field))!r}"
                    )
            translations = entry.get("translations")
            expected_trans = expected.get("translations") or {}
            if not isinstance(translations, dict):
                report.error(f"{prefix}: translations must be an object with ja/zh/ko")
            else:
                for lang in ("ja", "zh", "ko"):
                    if clean(translations.get(lang)) != clean(expected_trans.get(lang)):
                        report.error(
                            f"{prefix}: translations.{lang} mismatch: "
                            f"data={clean(translations.get(lang))!r}, "
                            f"expected={clean(expected_trans.get(lang))!r}"
                        )
        audio_key = clean(entry.get("audioKey"))
        if not audio_key:
            continue
        audio_keys.add(audio_key)
        root_exists = (audio_dir / f"{audio_key}.wav").exists()
        mobile_exists = (mobile_audio_dir / f"{audio_key}.wav").exists()
        if entry.get("hasAudio") != root_exists:
            report.error(f"{prefix}: hasAudio={entry.get('hasAudio')!r} but root audio exists={root_exists}")
        if root_exists and not mobile_exists:
            report.error(f"{prefix}: root audio exists but mobile audio is missing for {audio_key}.wav")
        if entry.get("hasAudio") and not root_exists:
            report.error(f"{prefix}: marked hasAudio but missing {audio_dir.relative_to(ROOT)}/{audio_key}.wav")

    duplicate_keys = {
        key: count for key, count in Counter(clean(entry.get("audioKey")) for entry in entries).items() if key and count > 1
    }
    if duplicate_keys:
        report.note(f"{label}: {len(duplicate_keys)} duplicate audio keys share existing audio files")
    return audio_keys


def validate_audio_dirs(
    label: str,
    data_audio_keys: set[str],
    audio_dir: Path,
    mobile_audio_dir: Path,
    report: ValidationReport,
) -> None:
    root_files = wav_stems(audio_dir)
    mobile_files = wav_stems(mobile_audio_dir)
    missing_root = sorted(data_audio_keys - root_files)
    missing_mobile = sorted(data_audio_keys - mobile_files)
    extra_root = sorted(root_files - data_audio_keys)
    extra_mobile = sorted(mobile_files - data_audio_keys)
    root_minus_mobile = sorted(root_files - mobile_files)
    mobile_minus_root = sorted(mobile_files - root_files)

    if missing_root:
        report.error(f"{label}: {len(missing_root)} referenced audio files missing from {audio_dir.relative_to(ROOT)}")
    if missing_mobile:
        report.error(
            f"{label}: {len(missing_mobile)} referenced audio files missing from {mobile_audio_dir.relative_to(ROOT)}"
        )
    if extra_root:
        report.warn(f"{label}: {len(extra_root)} extra root audio files not referenced by data: {sample(extra_root)}")
    if extra_mobile:
        report.warn(f"{label}: {len(extra_mobile)} extra mobile audio files not referenced by data: {sample(extra_mobile)}")
    if root_minus_mobile or mobile_minus_root:
        report.error(
            f"{label}: root/mobile audio directory mismatch "
            f"root-only={len(root_minus_mobile)} mobile-only={len(mobile_minus_root)}"
        )
    report.note(
        f"{label}: data_keys={len(data_audio_keys)} root_wav={len(root_files)} mobile_wav={len(mobile_files)}"
    )


def validate_manifest(
    label: str,
    data_audio_keys: set[str],
    manifest_entries: Any,
    report: ValidationReport,
) -> None:
    if not isinstance(manifest_entries, dict):
        report.error(f"manifest {label}: must be an object")
        return
    cleaned = {clean(key): clean(file_id) for key, file_id in manifest_entries.items() if clean(key)}
    invalid_ids = [key for key, file_id in cleaned.items() if not FILE_ID_RE.match(file_id)]
    missing = sorted(data_audio_keys - set(cleaned))
    extra = sorted(set(cleaned) - data_audio_keys)
    if invalid_ids:
        report.error(f"manifest {label}: invalid Google Drive file ids for keys: {sample(invalid_ids)}")
    if missing:
        report.error(f"manifest {label}: {len(missing)} data audio keys missing from manifest: {sample(missing)}")
    if extra:
        report.warn(f"manifest {label}: {len(extra)} extra manifest keys not referenced by data: {sample(extra)}")
    report.note(f"manifest {label}: keys={len(cleaned)}")


def validate_duplicate_display_choices(entries: list[dict[str, Any]], report: ValidationReport) -> None:
    notes: list[str] = []
    for lang in ("ja", "zh", "ko"):
        duplicates = {
            key: count
            for key, count in Counter(
                (
                    clean(entry.get("topic")),
                    clean(entry.get("subtopic")),
                    clean(entry.get("eo")),
                    clean((entry.get("translations") or {}).get(lang) if isinstance(entry.get("translations"), dict) else entry.get("ja")),
                )
                for entry in entries
            ).items()
            if count > 1
        }
        if duplicates:
            rendered = "; ".join(f"{count}x {key[2]!r} / {key[3]!r}" for key, count in list(duplicates.items())[:3])
            notes.append(f"{lang}: {rendered}")
    if notes:
        report.note(
            "sentence: duplicate display rows are kept as quiz targets; "
            "wrong-choice generation must avoid identical labels "
            f"({' | '.join(notes)})"
        )


def validate_wav_headers(paths: list[Path], report: ValidationReport) -> None:
    bad: list[str] = []
    zero_duration: list[str] = []
    total_seconds = 0.0
    for path in paths:
        try:
            with wave.open(str(path), "rb") as wav:
                frames = wav.getnframes()
                rate = wav.getframerate()
                seconds = frames / rate if rate else 0.0
        except Exception as exc:
            bad.append(f"{path.relative_to(ROOT)} ({type(exc).__name__}: {exc})")
            continue
        total_seconds += seconds
        if seconds <= 0:
            zero_duration.append(str(path.relative_to(ROOT)))
    if bad:
        report.error(f"WAV header failures: {len(bad)} files: {sample(bad)}")
    if zero_duration:
        report.error(f"WAV zero-duration files: {len(zero_duration)} files: {sample(zero_duration)}")
    report.note(f"WAV headers checked: files={len(paths)} total_seconds={total_seconds:.2f}")


def wav_stems(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {candidate.stem for candidate in path.glob("*.wav") if candidate.is_file()}


def sample(items: list[Any], limit: int = 8) -> str:
    shown = ", ".join(repr(item) for item in items[:limit])
    if len(items) > limit:
        return f"{shown}, ..."
    return shown


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Skip WAV header/duration checks and validate only paths, keys, and JSON/manifest consistency.",
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Treat warnings such as extra unreferenced audio files as failures.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = ValidationReport()

    expected_vocab = expected_vocab_rows(report)
    expected_sentences = expected_sentence_rows(report)
    vocab_payload = read_json_object(VOCAB_JSON, report)
    sentence_payload = read_json_object(SENTENCE_JSON, report)
    manifest = read_json_object(AUDIO_MANIFEST_JSON, report)

    vocab_entries = entries_from_payload(VOCAB_JSON, vocab_payload, report)
    sentence_entries = entries_from_payload(SENTENCE_JSON, sentence_payload, report)

    if len(vocab_entries) != len(expected_vocab):
        report.error(f"vocab: entries={len(vocab_entries)} expected_from_csv={len(expected_vocab)}")
    if len(sentence_entries) != len(expected_sentences):
        report.error(f"sentence: entries={len(sentence_entries)} expected_from_csv={len(expected_sentences)}")
    report.note(f"vocab: entries={len(vocab_entries)} expected_from_csv={len(expected_vocab)}")
    report.note(f"sentence: entries={len(sentence_entries)} expected_from_csv={len(expected_sentences)}")

    vocab_keys = validate_entries(
        "vocab", vocab_entries, expected_vocab, VOCAB_AUDIO_DIR, MOBILE_VOCAB_AUDIO_DIR, report
    )
    sentence_keys = validate_entries(
        "sentence", sentence_entries, expected_sentences, SENTENCE_AUDIO_DIR, MOBILE_SENTENCE_AUDIO_DIR, report
    )
    validate_audio_dirs("vocab", vocab_keys, VOCAB_AUDIO_DIR, MOBILE_VOCAB_AUDIO_DIR, report)
    validate_audio_dirs("sentence", sentence_keys, SENTENCE_AUDIO_DIR, MOBILE_SENTENCE_AUDIO_DIR, report)
    validate_manifest("vocab", vocab_keys, manifest.get("vocab"), report)
    validate_manifest("sentence", sentence_keys, manifest.get("sentence"), report)
    validate_duplicate_display_choices(sentence_entries, report)

    if not args.quick:
        wav_paths = (
            sorted(MOBILE_VOCAB_AUDIO_DIR.glob("*.wav"))
            + sorted(MOBILE_SENTENCE_AUDIO_DIR.glob("*.wav"))
            + sorted(VOCAB_AUDIO_DIR.glob("*.wav"))
            + sorted(SENTENCE_AUDIO_DIR.glob("*.wav"))
        )
        validate_wav_headers(wav_paths, report)
    else:
        report.note("WAV header checks skipped by --quick")

    print("Mobile asset validation")
    for note in report.notes:
        print(f"  OK: {note}")
    for warning in report.warnings:
        print(f"  WARNING: {warning}")
    for error in report.errors:
        print(f"  ERROR: {error}")

    if report.errors or (args.strict_warnings and report.warnings):
        print("Validation failed.")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
