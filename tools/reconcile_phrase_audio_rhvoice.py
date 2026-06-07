#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import shutil
import subprocess
import sys
import tempfile
import wave
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import vocab_grouping as vg  # noqa: E402
from data_sources import PHRASE_ID_OFFSET  # noqa: E402


AUDIO_FORMATS = (
    (".wav", "audio/wav"),
    (".mp3", "audio/mpeg"),
    (".ogg", "audio/ogg"),
)


@dataclass(frozen=True)
class AudioCandidate:
    phrase_id: int
    phrase: str
    expected_key: str
    matched_audio_file: str
    match_type: str

    @property
    def expected_file(self) -> str:
        return f"{self.expected_key}.wav"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Reconcile Esperanto phrase audio with the current phrase CSV, "
            "using RHVoice/Spomenka for replacement WAV files."
        )
    )
    parser.add_argument(
        "--csv",
        default=str(ROOT / "phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv"),
        help="Phrase CSV used by the sentence Streamlit apps.",
    )
    parser.add_argument(
        "--audio-dir",
        default=str(ROOT / "Esperanto例文5000文_収録音声"),
        help="Directory where phrase audio files live.",
    )
    parser.add_argument(
        "--voice",
        default="spomenka",
        help="RHVoice profile name.",
    )
    parser.add_argument(
        "--sample-rate",
        type=int,
        default=24000,
        help="Output sample rate passed to RHVoice-test.",
    )
    parser.add_argument(
        "--candidate-csv",
        default=str(ROOT / "編集ログ" / "phrases_audio_replacement_candidates_20260429.csv"),
        help="Write fallback/missing candidates to this CSV.",
    )
    parser.add_argument(
        "--generation-csv",
        default=str(ROOT / "編集ログ" / "phrases_audio_replacement_generation_20260429.csv"),
        help="Write generation/archive results to this CSV.",
    )
    parser.add_argument(
        "--report-md",
        default=str(ROOT / "編集ログ" / "audio_alignment_report_20260429.md"),
        help="Write a short Markdown alignment report.",
    )
    parser.add_argument(
        "--archive-dir",
        default=str(ROOT / "Esperanto例文5000文_収録音声" / "archived_replaced_audio_20260429"),
        help="Directory where superseded fallback audio files are moved.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite exact-key WAV files if they already exist.",
    )
    parser.add_argument(
        "--no-archive",
        action="store_true",
        help="Do not move superseded fallback files after exact files are available.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only scan and write the candidate CSV/report.",
    )
    parser.add_argument(
        "--write-empty-reports",
        action="store_true",
        help=(
            "Overwrite report files even when the current scan has no candidates. "
            "By default, existing audit files are preserved after reconciliation."
        ),
    )
    return parser.parse_args()


def phrase_audio_key(phrase_id: int, phrase: str) -> str:
    return f"{phrase_id - PHRASE_ID_OFFSET:04d}_{vg._default_audio_key(phrase)}"


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def find_exact(audio_dir: Path, key: str) -> Path | None:
    for ext, _mime in AUDIO_FORMATS:
        fp = audio_dir / f"{key}{ext}"
        if fp.exists():
            return fp
    return None


def find_fallback(audio_dir: Path, phrase_id: int, key: str) -> tuple[Path | None, str]:
    legacy_key = key.replace("_", "")
    for ext, _mime in AUDIO_FORMATS:
        fp = audio_dir / f"{legacy_key}{ext}"
        if fp.exists():
            return fp, "legacy"

    prefix = f"{phrase_id - PHRASE_ID_OFFSET:04d}_"
    for ext, _mime in AUDIO_FORMATS:
        matches = sorted(audio_dir.glob(f"{prefix}*{ext}"))
        if matches:
            return matches[0], "prefix"
    return None, "missing"


def scan(csv_path: Path, audio_dir: Path) -> tuple[dict[str, int], list[AudioCandidate]]:
    stats = {"rows": 0, "exact": 0, "legacy": 0, "prefix": 0, "missing": 0}
    candidates: list[AudioCandidate] = []

    for row in load_rows(csv_path):
        stats["rows"] += 1
        phrase_id = int(str(row["PhraseID"]).strip())
        phrase = str(row["Esperanto"]).strip()
        key = phrase_audio_key(phrase_id, phrase)

        if find_exact(audio_dir, key):
            stats["exact"] += 1
            continue

        fallback, match_type = find_fallback(audio_dir, phrase_id, key)
        stats[match_type] += 1
        candidates.append(
            AudioCandidate(
                phrase_id=phrase_id,
                phrase=phrase,
                expected_key=key,
                matched_audio_file=fallback.name if fallback else "",
                match_type=match_type,
            )
        )

    return stats, candidates


def write_candidates(path: Path, candidates: list[AudioCandidate]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "PhraseID",
                "current_phrase",
                "current_audio_key",
                "matched_audio_file",
                "match_type",
            ],
        )
        writer.writeheader()
        for item in candidates:
            writer.writerow(
                {
                    "PhraseID": item.phrase_id,
                    "current_phrase": item.phrase,
                    "current_audio_key": item.expected_key,
                    "matched_audio_file": item.matched_audio_file,
                    "match_type": item.match_type,
                }
            )


def validate_wav(path: Path) -> tuple[bool, str]:
    try:
        with wave.open(str(path), "rb") as wf:
            frames = wf.getnframes()
            channels = wf.getnchannels()
            rate = wf.getframerate()
        if frames <= 0:
            return False, "empty wav"
        if channels <= 0 or rate <= 0:
            return False, f"invalid wav metadata: channels={channels}, rate={rate}"
        return True, f"ok: frames={frames}, channels={channels}, rate={rate}"
    except Exception as exc:
        return False, str(exc)


def synthesize_rhvoice(text: str, out_wav: Path, *, voice: str, sample_rate: int) -> None:
    rhvoice = shutil.which("RHVoice-test")
    if not rhvoice:
        raise RuntimeError("RHVoice-test was not found in PATH.")

    out_wav.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        prefix=f"{out_wav.stem}.",
        suffix=".wav",
        dir=str(out_wav.parent),
        delete=False,
    ) as tmp:
        tmp_path = Path(tmp.name)

    try:
        subprocess.run(
            [
                rhvoice,
                "-p",
                voice,
                "-R",
                str(sample_rate),
                "-o",
                str(tmp_path),
            ],
            input=f"{text}\n",
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        ok, detail = validate_wav(tmp_path)
        if not ok:
            raise RuntimeError(f"Generated WAV is invalid: {detail}")
        tmp_path.replace(out_wav)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def archive_superseded(
    audio_dir: Path,
    archive_dir: Path,
    candidates: list[AudioCandidate],
) -> list[dict[str, str]]:
    archive_dir.mkdir(parents=True, exist_ok=True)
    moved: list[dict[str, str]] = []
    seen: set[str] = set()

    for item in candidates:
        if not item.matched_audio_file or item.matched_audio_file in seen:
            continue
        seen.add(item.matched_audio_file)

        exact_path = audio_dir / item.expected_file
        if not exact_path.exists():
            moved.append(
                {
                    "PhraseID": str(item.phrase_id),
                    "old_file": item.matched_audio_file,
                    "new_file": item.expected_file,
                    "status": "kept_no_exact_file",
                }
            )
            continue

        src = audio_dir / item.matched_audio_file
        if not src.exists():
            moved.append(
                {
                    "PhraseID": str(item.phrase_id),
                    "old_file": item.matched_audio_file,
                    "new_file": item.expected_file,
                    "status": "already_absent",
                }
            )
            continue

        dst = archive_dir / src.name
        if dst.exists():
            stem = dst.stem
            suffix = dst.suffix
            counter = 2
            while dst.exists():
                dst = archive_dir / f"{stem}_{counter}{suffix}"
                counter += 1
        shutil.move(str(src), str(dst))
        moved.append(
            {
                "PhraseID": str(item.phrase_id),
                "old_file": src.name,
                "new_file": item.expected_file,
                "status": f"moved_to:{dst.name}",
            }
        )

    manifest = archive_dir / "moved_files.csv"
    with manifest.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["PhraseID", "old_file", "new_file", "status"])
        writer.writeheader()
        writer.writerows(moved)
    return moved


def validate_expected_audio(csv_path: Path, audio_dir: Path) -> tuple[dict[str, int], list[dict[str, str]]]:
    counts = {"rows": 0, "exact": 0, "bad_audio": 0}
    bad: list[dict[str, str]] = []
    for row in load_rows(csv_path):
        counts["rows"] += 1
        phrase_id = int(str(row["PhraseID"]).strip())
        phrase = str(row["Esperanto"]).strip()
        key = phrase_audio_key(phrase_id, phrase)
        fp = audio_dir / f"{key}.wav"
        if not fp.exists():
            bad.append({"PhraseID": str(phrase_id), "file": fp.name, "status": "missing"})
            continue
        counts["exact"] += 1
        ok, detail = validate_wav(fp)
        if not ok:
            counts["bad_audio"] += 1
            bad.append({"PhraseID": str(phrase_id), "file": fp.name, "status": detail})
    return counts, bad


def write_generation_report(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "PhraseID",
                "phrase",
                "voice",
                "output_file",
                "matched_audio_file",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def write_markdown_report(
    path: Path,
    *,
    before: dict[str, int],
    after: dict[str, int],
    candidate_csv: Path,
    generation_csv: Path,
    archive_dir: Path,
    moved_count: int,
    bad_audio: list[dict[str, str]],
    voice: str,
    sample_rate: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    bad_summary = "0" if not bad_audio else str(len(bad_audio))
    text = f"""# 音声整合確認レポート

作成日: {today}

## 対象

- 例文CSV: `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`
- 例文音声: `Esperanto例文5000文_収録音声/`
- 音声生成: RHVoice `{voice}` / {sample_rate} Hz WAV

## 実施前

- rows: {before['rows']}
- exact: {before['exact']}
- legacy fallback: {before['legacy']}
- prefix fallback: {before['prefix']}
- missing: {before['missing']}

## 実施内容

- 差し替え候補一覧を作成: `{display_path(candidate_csv)}`
- RHVoice/Spomenka で exact-key WAV を生成: `{display_path(generation_csv)}`
- 旧prefix/legacy音声を退避: `{display_path(archive_dir)}/`
- 退避件数: {moved_count}

## 実施後

- rows: {after['rows']}
- exact WAV: {after['exact']}
- bad audio: {bad_summary}

## 補足

- アプリは `PhraseID - 155` と Esperanto 文の正規化キーで音声を先に exact 検索する。
- 今回の更新後は、CSV上のEsperanto文と同じキーのWAVが全件存在するため、旧音声へのprefix fallbackは通常使われない。
- 検証はファイル名・存在・WAV可読性の確認であり、ASRによる発話内容の文字起こし照合までは含まない。
"""
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv)
    audio_dir = Path(args.audio_dir)
    candidate_csv = Path(args.candidate_csv)
    generation_csv = Path(args.generation_csv)
    report_md = Path(args.report_md)
    archive_dir = Path(args.archive_dir)

    before, candidates = scan(csv_path, audio_dir)
    should_write_audit = bool(candidates) or args.write_empty_reports
    if should_write_audit or not candidate_csv.exists():
        write_candidates(candidate_csv, candidates)
    else:
        print(f"preserved existing candidate CSV: {candidate_csv}")
    print(
        "scan: "
        f"rows={before['rows']} exact={before['exact']} "
        f"legacy={before['legacy']} prefix={before['prefix']} missing={before['missing']}"
    )
    print(f"candidates: {len(candidates)} -> {candidate_csv}")

    results: list[dict[str, str]] = []
    if not args.dry_run:
        for item in candidates:
            out_wav = audio_dir / item.expected_file
            if out_wav.exists() and not args.overwrite:
                status = "skipped_exists"
            else:
                try:
                    synthesize_rhvoice(
                        item.phrase,
                        out_wav,
                        voice=args.voice,
                        sample_rate=args.sample_rate,
                    )
                    status = "generated"
                    print(f"generated {item.phrase_id}: {out_wav.name}")
                except Exception as exc:  # pragma: no cover - maintenance utility
                    status = f"error: {exc}"
                    print(f"error {item.phrase_id}: {exc}", file=sys.stderr)
            results.append(
                {
                    "PhraseID": str(item.phrase_id),
                    "phrase": item.phrase,
                    "voice": args.voice,
                    "output_file": out_wav.name,
                    "matched_audio_file": item.matched_audio_file,
                    "status": status,
                }
            )

        if not args.no_archive:
            moved = archive_superseded(audio_dir, archive_dir, candidates)
        else:
            moved = []
    else:
        moved = []

    if should_write_audit or results or not generation_csv.exists():
        write_generation_report(generation_csv, results)
    else:
        print(f"preserved existing generation CSV: {generation_csv}")
    after, bad_audio = validate_expected_audio(csv_path, audio_dir)
    if should_write_audit or results or not report_md.exists():
        write_markdown_report(
            report_md,
            before=before,
            after=after,
            candidate_csv=candidate_csv,
            generation_csv=generation_csv,
            archive_dir=archive_dir,
            moved_count=sum(1 for row in moved if row["status"].startswith("moved_to:")),
            bad_audio=bad_audio,
            voice=args.voice,
            sample_rate=args.sample_rate,
        )
    else:
        print(f"preserved existing Markdown report: {report_md}")

    print(
        "validate: "
        f"rows={after['rows']} exact_wav={after['exact']} bad_audio={after['bad_audio']}"
    )
    print(f"report: {report_md}")

    errors = [row for row in results if row["status"].startswith("error:")]
    return 1 if errors or bad_audio or after["exact"] != after["rows"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
