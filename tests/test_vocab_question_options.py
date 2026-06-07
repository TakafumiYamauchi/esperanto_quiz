"""4択クイズの不変条件: 同一グループ内の選択肢表示は一意であること。

PC版 (`vocab_grouping.build_questions_for_group`) は誤答候補をエントリ単位で
サンプリングし、表示テキストの重複排除をしない。したがって、もし同一グループ
（同一 POS × 同一レベル帯）に同じ訳語を持つ語が同居すると、`eo_to_ja` 出題で
「見た目が同一の選択肢」が複数並び、4択の答えが一意に定まらなくなる。

現行 CSV では同居が発生しないため実害はない（2026-06-07 実測: 全20,230質問で0件）。
本テストはその不変条件をデータ品質カナリアとして固定し、将来の語彙追加や分類器
変更で曖昧な4択が混入したら即座に検知できるようにする。

加えて 2026-06-07、`build_questions_for_group` 自体が誤答候補を表示テキスト(日本語・
エスペラント)で重複排除するようにした（例文版・モバイル JS 版と同方針、README の
「対象言語で同一表示の選択肢を避ける」に整合）。現データでは何も除外されず挙動は
バイト不変（173,400問で実証）。`test_builder_dedups_*` がその予防動作を合成データで
検証する。＝「検知（データ品質カナリア）」＋「予防（ビルダー）」の二重防御。
"""
import random
import unittest
from collections import Counter

from data_sources import VOCAB_CSV
from vocab_grouping import Group, VocabEntry, build_groups, build_questions_for_group

# 端点 + パリティテストと同じ代表シード。全8192シードは網羅できないためカナリア。
SEEDS = (1, 17, 8192)


class VocabQuestionOptionUniquenessTests(unittest.TestCase):
    def _assert_group_displays_unique(self, field: str) -> None:
        for seed in SEEDS:
            groups = build_groups(VOCAB_CSV, seed=seed)
            for group in groups:
                values = [getattr(entry, field) for entry in group.entries]
                dups = [value for value, count in Counter(values).items() if count >= 2]
                self.assertEqual(
                    dups,
                    [],
                    msg=(
                        f"seed={seed} group={group.id} (pos={group.pos}) に "
                        f"{field} の重複表示 {dups} があり、曖昧な4択が生成されうる"
                    ),
                )

    def test_japanese_displays_unique_per_group(self):
        # eo_to_ja 出題で選択肢に使われる日本語訳が、グループ内で一意であること。
        self._assert_group_displays_unique("japanese")

    def test_esperanto_displays_unique_per_group(self):
        # ja_to_eo 出題で選択肢に使われるエスペラント語が、グループ内で一意であること。
        self._assert_group_displays_unique("esperanto")

    def test_builder_dedups_duplicate_display_options(self):
        # グループに同一表示の語が混在しても、4択に同一表示が並ばない（ビルダーの予防動作）。
        entries = [
            VocabEntry(esperanto="hundo", japanese="犬", unified_level=1.0, pos="noun", source_index=0, audio_key="hundo"),
            VocabEntry(esperanto="kato", japanese="猫", unified_level=1.0, pos="noun", source_index=1, audio_key="kato"),
            VocabEntry(esperanto="ĉevalo", japanese="馬", unified_level=1.0, pos="noun", source_index=2, audio_key="cxevalo"),
            VocabEntry(esperanto="hundeto", japanese="犬", unified_level=1.0, pos="noun", source_index=3, audio_key="hundeto"),  # 「犬」重複
            VocabEntry(esperanto="birdo", japanese="鳥", unified_level=1.0, pos="noun", source_index=4, audio_key="birdo"),
            VocabEntry(esperanto="fiŝo", japanese="魚", unified_level=1.0, pos="noun", source_index=5, audio_key="fixo"),
        ]
        group = Group(id="synthetic", pos="noun", stages=["beginner_1"], size=len(entries), entries=entries)
        generated = False
        for seed in range(50):
            for question in build_questions_for_group(group, rng=random.Random(seed)):
                generated = True
                for field in ("japanese", "esperanto"):
                    labels = [opt[field] for opt in question["options"]]
                    self.assertEqual(
                        len(set(labels)),
                        len(labels),
                        msg=f"seed={seed} で {field} の表示重複: {labels}",
                    )
        self.assertTrue(generated, "合成グループから質問が生成されなかった（検証が空振り）")


if __name__ == "__main__":
    unittest.main()
