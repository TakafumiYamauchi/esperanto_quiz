#!/usr/bin/env python3
"""Build a mobile audio manifest from public Google Drive folders."""

from __future__ import annotations

import datetime as dt
import html
import json
import re
import sys
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "mobile_app" / "data" / "audio_manifest.json"
VOCAB_DATA_PATH = ROOT / "mobile_app" / "data" / "vocab.json"
SENTENCE_DATA_PATH = ROOT / "mobile_app" / "data" / "sentences.json"

FOLDERS = {
    "sentence": {
        # Repointed 2026-06-07 to a freshly-created public folder after the
        # previous one (1Mz5wgbIEBV-...) became inaccessible (trashed).
        "folder_id": "1tmb4_k3zRv2JjOmHCNvv5zIbbneeKwYZ",
        "label": "Esperanto例文5000文_収録音声",
    },
    "vocab": {
        "folder_id": "1YBN5sNxSTHKXh_oJJSlCG-L3lnT1OpIG",
        "label": "audio",
    },
}

FILE_ENTRY_RE = re.compile(
    r'id="entry-(?P<file_id>[-_A-Za-z0-9]+)"'
    r'.{0,2500}?'
    r'class="flip-entry-title">(?P<filename>[^<]+\.wav)</div>',
    re.DOTALL,
)


def fetch_drive_folder(folder_id: str) -> str:
    url = f"https://drive.google.com/embeddedfolderview?id={folder_id}#list"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_wav_files(page: str) -> dict[str, str]:
    unescaped = html.unescape(page)
    files: dict[str, str] = {}
    for match in FILE_ENTRY_RE.finditer(unescaped):
        filename = match.group("filename").strip()
        file_id = match.group("file_id").strip()
        if not filename or not file_id:
            continue
        # str.removesuffix is 3.9+; repo's default python3 is 3.8, so do it manually.
        audio_key = filename[:-4] if filename.endswith(".wav") else filename
        files[audio_key] = file_id
    return dict(sorted(files.items()))


def load_audio_keys(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        str(entry.get("audioKey", "")).strip()
        for entry in payload.get("entries", [])
        if entry.get("hasAudio") and str(entry.get("audioKey", "")).strip()
    }


def main() -> int:
    manifest: dict[str, object] = {
        "schema": 1,
        "provider": "google_drive",
        "downloadBaseUrl": "https://drive.google.com/uc?export=download&id=",
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sources": {},
        "vocab": {},
        "sentence": {},
    }

    existing: dict = {}
    if OUT_PATH.exists():
        try:
            existing = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    for mode, config in FOLDERS.items():
        page = fetch_drive_folder(config["folder_id"])
        files = extract_wav_files(page)
        if not files:
            # Drive folder inaccessible/empty (trashed or not public): preserve the
            # previous manifest section rather than aborting the whole rebuild, so an
            # unrelated broken folder cannot block updating the one that did succeed.
            prev = existing.get(mode)
            if isinstance(prev, dict) and prev:
                print(
                    f"warning: no wav files in {config['label']}; "
                    f"preserving {len(prev)} existing '{mode}' entries",
                    file=sys.stderr,
                )
                manifest[mode] = prev
                manifest["sources"][mode] = {
                    "folderId": config["folder_id"],
                    "label": config["label"],
                    "fileCount": len(prev),
                    "preservedFromPrevious": True,
                }
                continue
            print(f"error: no wav files found in {config['label']}", file=sys.stderr)
            return 1
        manifest[mode] = files
        manifest["sources"][mode] = {
            "folderId": config["folder_id"],
            "label": config["label"],
            "fileCount": len(files),
        }
        print(f"{mode}: {len(files)} wav files")

    expected = {
        "vocab": load_audio_keys(VOCAB_DATA_PATH),
        "sentence": load_audio_keys(SENTENCE_DATA_PATH),
    }
    warnings = []
    for mode, keys in expected.items():
        available = set(manifest[mode].keys())
        missing = sorted(keys - available)
        extra = sorted(available - keys)
        manifest["sources"][mode]["matchedDataKeys"] = len(keys & available)
        manifest["sources"][mode]["missingDataKeys"] = missing
        manifest["sources"][mode]["extraDriveKeys"] = extra[:100]
        if missing:
            warnings.append(f"{mode}: {len(missing)} data audio keys missing from Drive")
        if extra:
            warnings.append(f"{mode}: {len(extra)} Drive files not referenced by mobile data")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT_PATH.relative_to(ROOT)}")
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
