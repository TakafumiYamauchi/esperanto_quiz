import json
import math
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import pandas as pd

from data_sources import VOCAB_CSV


# -------- パラメータ --------
# ランダムシードは 1〜8192 に丸める。PC版とスマホ版で同じグループ内容にするため、
# グループ分割にはPython標準乱数ではなくJS版と同じmulberry32を使う。
DEFAULT_SEED = 1
SEED_MIN = 1
SEED_MAX = 8192
UINT32_MASK = 0xFFFFFFFF
UINT32_SIZE = 4294967296


def clamp_seed(seed: int, fallback: int = DEFAULT_SEED) -> int:
    try:
        parsed = int(seed)
    except (TypeError, ValueError):
        parsed = fallback
    return max(SEED_MIN, min(SEED_MAX, parsed))


class Mulberry32:
    def __init__(self, seed: int):
        self.state = clamp_seed(seed) & UINT32_MASK

    def random(self) -> float:
        self.state = (self.state + 0x6D2B79F5) & UINT32_MASK
        t = self.state
        t = ((t ^ (t >> 15)) * (t | 1)) & UINT32_MASK
        t ^= (t + (((t ^ (t >> 7)) * (t | 61)) & UINT32_MASK)) & UINT32_MASK
        return ((t ^ (t >> 14)) & UINT32_MASK) / UINT32_SIZE

    def shuffle(self, items: List) -> None:
        for index in range(len(items) - 1, 0, -1):
            swap_index = int(self.random() * (index + 1))
            items[index], items[swap_index] = items[swap_index], items[index]


# -------- 品詞判定ロジック --------
# エスペラントの語尾規則＋例外リストで分類する。
PERSONAL_PRONOUNS = {"mi", "vi", "li", "ŝi", "ĝi", "ni", "ili", "oni", "ci"}
PRONOUNS = {"oni", "si", "mem"}
CORRELATIVE_PREFIXES = ["ki", "ti", "i", "neni", "ĉi"]
CORRELATIVE_SUFFIXES = ["u", "o", "a", "e", "al", "am", "el", "om", "es"]
CORRELATIVE_SPECIAL = {"ĉi", "ĉiuj", "ĉiu"}
PREPOSITIONS = {
    "al",
    "da",
    "de",
    "disde",
    "el",
    "ekster",
    "ĝis",
    "je",
    "inter",
    "kontraŭ",
    "kun",
    "laŭ",
    "malgraŭ",
    "per",
    "po",
    "por",
    "post",
    "pri",
    "pro",
    "sen",
    "sub",
    "super",
    "sur",
    "tra",
    "trans",
    "ĉe",
    "ĉirkaŭ",
    "antaŭ",
    "apud",
    "eksteren",
    "interne",
    "preter",
    "en",
    "anstataŭ",
    "krom",
    "malantaŭ",
}
CONJUNCTIONS = {
    "kaj",
    "aŭ",
    "sed",
    "se",
    "ĉar",
    "ke",
    "do",
    "tamen",
    "kvankam",
    "ol",
    "ĉu",
    "kvazaŭ",
    "dum",
    "nek",
    "tial",
}
BARE_ADVERBS = {
    "jes",
    "ne",
    "nun",
    "tre",
    "pli",
    "plej",
    "jen",
    "ja",
    "preskaŭ",
    "baldaŭ",
    "hieraŭ",
    "morgaŭ",
    "ĉiam",
    "neniam",
    "foje",
    "refoje",
    "ankoraŭ",
    "tuj",
    "jam",
    "eĉ",
    "apenaŭ",
    "for",
    "tie",
    "tie ĉi",
    "ĉie",
    "sekve",
    "multe",
    "iom",
    "iomete",
    "sufiĉe",
    "egale",
    "kune",
    "aparte",
    "tute",
    "parte",
    "rekte",
    "malrekte",
    "denove",
    "pli-malpli",
    "proksime",
    "malproksime",
    "bone",
    "malbone",
    "ajn",
    "ankaŭ",
    "nur",
    "des",
    "hodiaŭ",
    "almenaŭ",
    "adiaŭ",
}
NUMERALS = {
    "nul",
    "nulo",
    "unu",
    "du",
    "tri",
    "kvar",
    "kvin",
    "ses",
    "sep",
    "ok",
    "naŭ",
    "dek",
    "cent",
    "mil",
    "miliono",
    "miliardo",
    "ducent",
    "tricent",
}


def strip_plural_accusative(word: str) -> str:
    base = word
    while base.endswith(("j", "n")):
        base = base[:-1]
    return base


def is_correlative(word: str) -> bool:
    for prefix in CORRELATIVE_PREFIXES:
        for suffix in CORRELATIVE_SUFFIXES:
            if word == f"{prefix}{suffix}":
                return True
    return False


def classify_pos(word: str) -> str:
    w = word.strip().lower()
    if not w:
        return "unknown"

    if w.startswith("-") and w.endswith("-"):
        return "suffix"
    if w.startswith("-"):
        return "suffix"
    if w.endswith("-"):
        return "prefix"

    if w in CORRELATIVE_SPECIAL or is_correlative(w):
        return "correlative"
    if w in PERSONAL_PRONOUNS:
        return "personal_pronoun"
    if w in PRONOUNS:
        return "pronoun"
    if w.isdigit() or w in NUMERALS or re.match(
        # 数詞の語根（および合成）に文法語尾が付いた形だけを数詞とみなす。
        # 旧パターン [a-zĉĝĥĵŝŭ]* は語根で始まる任意の語（okulo, trinki,
        # oktobro, centro など）を数詞へ誤分類していたため、語尾を限定して厳格化する。
        r"^(?:unu|du|tri|kvar|kvin|ses|sep|ok|naŭ|dek|cent|mil)+(?:a|o|aj|oj|an|on|ajn|ojn)?$",
        w,
    ):
        return "numeral"
    if w in PREPOSITIONS:
        return "preposition"
    if w in CONJUNCTIONS:
        return "conjunction"
    if w in BARE_ADVERBS:
        return "bare_adverb"

    base = strip_plural_accusative(w)
    if base.endswith("e"):
        return "adverb"
    if any(base.endswith(end) for end in ("as", "is", "os", "us", "u", "i")):
        return "verb"
    if base.endswith("a"):
        return "adjective"
    if base.endswith("o"):
        return "noun"

    return "other"


# -------- データ構造 --------
@dataclass
class VocabEntry:
    esperanto: str
    japanese: str
    unified_level: float
    pos: str
    source_index: int
    audio_key: Optional[str] = None  # 音声ファイル lookup 用のキー（任意）


@dataclass
class Group:
    id: str
    pos: str
    stages: List[str]
    size: int
    entries: List[VocabEntry]


# -------- 分配のユーティリティ --------
def allocate_by_ratio(total: int, weights: Sequence[int]) -> List[int]:
    """
    total 個を weights の比率に従って整数配分する。
    端数は小数部の大きい順に 1 ずつ再配分する。
    """
    if total <= 0:
        return [0 for _ in weights]

    total_weight = sum(weights)
    raw = [total * w / total_weight for w in weights]
    floors = [math.floor(x) for x in raw]
    remainder = total - sum(floors)

    order = sorted(range(len(weights)), key=lambda i: raw[i] - floors[i], reverse=True)
    for i in range(remainder):
        floors[order[i % len(order)]] += 1
    return floors


def even_chunks(items: List[VocabEntry], parts: int) -> List[List[VocabEntry]]:
    """parts 個にできるだけ均等に分割する（差は最大1）。"""
    if parts <= 0:
        return [items]
    base, extra = divmod(len(items), parts)
    chunks = []
    cursor = 0
    for i in range(parts):
        size = base + (1 if i < extra else 0)
        chunks.append(items[cursor : cursor + size])
        cursor += size
    return chunks


def choose_group_count(total: int) -> int:
    """20〜30語の範囲になるようなグループ数を選択する。"""
    if total <= 30:
        return 1
    if 31 <= total <= 39:
        return 2

    lower = math.ceil(total / 30)
    upper = max(lower, math.floor(total / 20))
    target = 25
    candidates = list(range(lower, upper + 1))
    return min(candidates, key=lambda g: abs(total / g - target))


# -------- コア処理 --------
def load_vocab(
    csv_path: Path,
    audio_key_fn: Optional[Callable[[str], str]] = None,
    translation_column: str = "Japanese_Trans",
) -> List[VocabEntry]:
    df = pd.read_csv(csv_path)
    required_columns = ["Esperanto", "Unified_Level", translation_column]
    missing_columns = [c for c in required_columns if c not in df.columns]
    if missing_columns:
        raise KeyError(
            f"Missing columns {missing_columns} in {csv_path}. "
            f"Available columns: {', '.join(map(str, df.columns))}"
        )
    entries: List[VocabEntry] = []
    for idx, row in df.iterrows():
        eo_raw = row.get("Esperanto")
        tr_raw = row.get(translation_column)
        level_raw = row.get("Unified_Level")

        if pd.isna(eo_raw) or pd.isna(tr_raw) or pd.isna(level_raw):
            continue

        eo = str(eo_raw).strip()
        ja = str(tr_raw).strip()
        if not eo or not ja:
            continue

        try:
            level = float(level_raw)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(level):
            continue

        pos = classify_pos(eo)
        audio_key = audio_key_fn(eo) if audio_key_fn else None
        entries.append(
            VocabEntry(
                esperanto=eo,
                japanese=ja,
                unified_level=level,
                pos=pos,
                source_index=idx,
                audio_key=audio_key,
            )
        )
    return entries


def split_by_level(entries: List[VocabEntry]) -> Dict[str, List[VocabEntry]]:
    """
    品詞ごとの語彙を Unified_Level 昇順に並べ、
    55:65:120 の比率で 初級/中級/上級 に分ける。
    """
    sorted_entries = sorted(entries, key=lambda e: e.unified_level)
    counts = allocate_by_ratio(len(entries), [55, 65, 120])
    beginner, intermediate, advanced = counts
    buckets: Dict[str, List[VocabEntry]] = {
        "beginner": sorted_entries[:beginner],
        "intermediate": sorted_entries[beginner : beginner + intermediate],
        "advanced": sorted_entries[beginner + intermediate :],
    }
    return buckets


def build_sublevels(
    buckets: Dict[str, List[VocabEntry]]
) -> List[Tuple[List[str], List[VocabEntry]]]:
    """
    初級/中級/上級をそれぞれ 3/3/6 の等分サブレベルに分け、
    レベル順のリストとして返す（ラベルは ["beginner_1", ...] など）。
    """
    ordered: List[Tuple[List[str], List[VocabEntry]]] = []
    for stage, parts in [("beginner", 3), ("intermediate", 3), ("advanced", 6)]:
        sub_chunks = even_chunks(buckets.get(stage, []), parts)
        for idx, chunk in enumerate(sub_chunks, start=1):
            if not chunk:
                continue
            ordered.append(([f"{stage}_{idx}"], list(chunk)))
    return ordered


def merge_small_sublevels(
    sublevels: List[Tuple[List[str], List[VocabEntry]]]
) -> List[Tuple[List[str], List[VocabEntry]]]:
    """
    語数が20未満のサブレベルは隣接サブレベルと結合。
    すべて結合しても20未満ならそのまま返す。
    """
    if not sublevels:
        return []

    merged: List[Tuple[List[str], List[VocabEntry]]] = []
    current_labels, current_words = sublevels[0]

    for labels, words in sublevels[1:]:
        if len(current_words) < 20:
            current_labels += labels
            current_words += words
            continue

        merged.append((current_labels, current_words))
        current_labels, current_words = labels, words

    if len(current_words) < 20 and merged:
        prev_labels, prev_words = merged.pop()
        prev_labels += current_labels
        prev_words += current_words
        merged.append((prev_labels, prev_words))
    else:
        merged.append((current_labels, current_words))

    return merged


def split_into_groups(labels: List[str], words: List[VocabEntry], pos: str, rng) -> List[Group]:
    rng.shuffle(words)
    total = len(words)
    groups: List[Group] = []

    if total < 20:
        group_sizes = [total]
    elif total <= 30:
        group_sizes = [total]
    elif 31 <= total <= 39:
        half = total // 2
        group_sizes = [half, total - half]
    else:
        count = choose_group_count(total)
        base, extra = divmod(total, count)
        group_sizes = [base + (1 if i < extra else 0) for i in range(count)]

    cursor = 0
    for idx, size in enumerate(group_sizes, start=1):
        slice_words = words[cursor : cursor + size]
        cursor += size
        group_id = f"{pos}:{'+'.join(labels)}:g{idx}"
        groups.append(
            Group(
                id=group_id,
                pos=pos,
                stages=labels,
                size=len(slice_words),
                entries=slice_words,
            )
        )
    return groups


def build_groups(
    csv_path: Path,
    seed: int = DEFAULT_SEED,
    audio_key_fn: Optional[Callable[[str], str]] = None,
    translation_column: str = "Japanese_Trans",
) -> List[Group]:
    # personal_pronoun と pronoun は統合して 1 品詞として扱う
    COMBINED_POS = {"personal_pronoun": "pronoun", "pronoun": "pronoun"}

    rng = Mulberry32(seed)
    entries = load_vocab(
        csv_path,
        audio_key_fn=audio_key_fn,
        translation_column=translation_column,
    )

    groups: List[Group] = []
    by_pos: Dict[str, List[VocabEntry]] = {}
    for entry in entries:
        pos_key = COMBINED_POS.get(entry.pos, entry.pos)
        by_pos.setdefault(pos_key, []).append(entry)

    for pos, items in by_pos.items():
        level_buckets = split_by_level(items)
        sublevels = build_sublevels(level_buckets)
        merged = merge_small_sublevels(sublevels)
        for labels, words in merged:
            groups.extend(split_into_groups(labels, words, pos, rng))

    return groups


# -------- 出題ロジック --------
def build_question(
    groups: Sequence[Group],
    rng: Optional[random.Random] = None,
    min_options: int = 2,
    max_options: int = 4,
) -> Dict:
    """
    4択問題を1件生成する。
    - 正答・誤答ともに同じグループ内から選ぶ
    - グループの語数が min_options 未満ならスキップ
    - options 数はグループ語数と max_options の小さい方
    """
    rng = rng or random.Random()
    eligible = [g for g in groups if len(g.entries) >= min_options]
    if not eligible:
        raise ValueError("No group has enough entries.")

    group = rng.choice(eligible)
    correct = rng.choice(group.entries)
    pool = [e for e in group.entries if e is not correct]
    option_size = min(max_options - 1, len(pool))
    wrong = rng.sample(pool, option_size)
    options = wrong + [correct]
    rng.shuffle(options)

    answer_index = options.index(correct)
    return {
        "group_id": group.id,
        "pos": group.pos,
        "stages": group.stages,
        "prompt": correct.esperanto,
        "answer_index": answer_index,
        "options": [
            {
                "japanese": opt.japanese,
                "esperanto": opt.esperanto,
                "audio_key": opt.audio_key,
            }
            for opt in options
        ],
    }


# -------- CLI 便利コマンド --------
def save_groups_json(groups: List[Group], path: Path) -> None:
    payload = [
        {
            "id": g.id,
            "pos": g.pos,
            "stages": g.stages,
            "size": g.size,
            "entries": [
                {
                    "esperanto": e.esperanto,
                    "japanese": e.japanese,
                    "unified_level": e.unified_level,
                    "pos": e.pos,
                    "audio_key": e.audio_key,
                }
                for e in g.entries
            ],
        }
        for g in groups
    ]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _default_audio_key(word: str) -> str:
    eo_to_ascii = str.maketrans(
        {
            "ĉ": "cx",
            "ĝ": "gx",
            "ĥ": "hx",
            "ĵ": "jx",
            "ŝ": "sx",
            "ŭ": "ux",
            "Ĉ": "Cx",
            "Ĝ": "Gx",
            "Ĥ": "Hx",
            "Ĵ": "Jx",
            "Ŝ": "Sx",
            "Ŭ": "Ux",
        }
    )
    ascii_word = word.translate(eo_to_ascii)
    safe = re.sub(r"[^0-9A-Za-z_]+", "_", ascii_word.strip()) or "untitled"
    return safe.lower().strip("_")


def build_questions_for_group(
    group: Group,
    rng: Optional[random.Random] = None,
    min_options: int = 2,
    max_options: int = 4,
) -> List[Dict]:
    """
    1グループ内の全単語を1回ずつ出題するための質問リストを作成する。
    小規模グループ（例: 2語）でも min_options を満たせば生成。
    """
    rng = rng or random.Random()
    if len(group.entries) < min_options:
        return []

    questions = []
    entries = list(group.entries)
    rng.shuffle(entries)
    for correct in entries:
        # 誤答候補を表示テキスト(日本語・エスペラント)で一意化し、同一表示の選択肢が
        # 4択に並ばないようにする（例文版 build_questions・モバイル quiz_core.mjs と同方針、
        # README「対象言語で同一表示の選択肢を避ける」に整合）。
        # 各グループの表示が全て一意な現データでは何も除外されず、pool は従来と同一順序・
        # 同一要素になり誤答抽選も結果も完全に不変（173,400問でバイト一致を実測）。
        seen_ja = {correct.japanese}
        seen_eo = {correct.esperanto}
        pool = []
        for entry in group.entries:
            if entry is correct:
                continue
            if entry.japanese in seen_ja or entry.esperanto in seen_eo:
                continue
            seen_ja.add(entry.japanese)
            seen_eo.add(entry.esperanto)
            pool.append(entry)
        option_size = min(max_options - 1, len(pool))
        wrong = rng.sample(pool, option_size)
        options = wrong + [correct]
        rng.shuffle(options)
        answer_index = options.index(correct)
        questions.append(
            {
                "group_id": group.id,
                "pos": group.pos,
                "stages": group.stages,
                "prompt": correct.esperanto,
                "answer_index": answer_index,
                "options": [
                    {
                        "japanese": opt.japanese,
                        "esperanto": opt.esperanto,
                        "audio_key": opt.audio_key,
                    }
                    for opt in options
                ],
            }
        )
    return questions


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Build groupings and demo a quiz item."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=VOCAB_CSV,
        help="Path to the vocabulary CSV.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Random seed (1-8192 recommended).",
    )
    parser.add_argument(
        "--dump",
        type=Path,
        help="Optional path to write grouped JSON.",
    )
    args = parser.parse_args()

    groups = build_groups(args.csv, seed=args.seed, audio_key_fn=_default_audio_key)
    print(f"Generated {len(groups)} groups with seed={args.seed}.")
    for g in sorted(groups, key=lambda x: x.id)[:5]:
        print(f" - {g.id}: {g.size} items")

    question = build_question(groups, rng=random.Random(args.seed + 1))
    print("\nSample question:")
    print(json.dumps(question, ensure_ascii=False, indent=2))

    if args.dump:
        save_groups_json(groups, args.dump)
        print(f"Saved groups to {args.dump}")


if __name__ == "__main__":
    main()
