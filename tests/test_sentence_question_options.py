"""例文4択の不変条件: 同一表示の選択肢を出さない（重複排除ロジックの回帰防止）。

例文データには「同じエスペラント文・同じ訳」の行が意図的に複数存在する
（validate_mobile_assets でも検出: `Pardonu min`/「申し訳ありません。」等）。
これらは出題対象として残しつつ、4択の選択肢に同一表示が並ばないよう
`sentence_app.build_questions` が表示テキストで重複排除している（direction に応じて
`japanese`/`phrase` を切り替え、`seen_options` で正解と誤答の表示を一意化）。

この重複排除は実データに重複が実在するため本番で実際に効いている load-bearing な
ロジックだが、従来テストが無かった。本テストは合成データ（既知の重複ペアを含む）で
実関数を直接呼び、両方向・複数シードで「全選択肢の表示が相異なる」ことを検証する。
振る舞いは変えない純粋追加。
"""
import random
import unittest

from sentence_app import build_questions


def _make_entries():
    """8件の合成例文。うち2組は『表示が衝突する』ペアを意図的に含む。"""
    entries = []
    # 衝突ペアA: japanese が同一（eo_to_ja の選択肢表示が衝突）だが phrase は別
    entries.append({"phrase": "Frazo A1", "japanese": "同じ日本語", "level": 1, "phrase_id": 1})
    entries.append({"phrase": "Frazo A2", "japanese": "同じ日本語", "level": 1, "phrase_id": 2})
    # 衝突ペアB: phrase が同一（ja_to_eo の選択肢表示が衝突）だが japanese は別
    entries.append({"phrase": "Sama frazo", "japanese": "日本語B1", "level": 1, "phrase_id": 3})
    entries.append({"phrase": "Sama frazo", "japanese": "日本語B2", "level": 1, "phrase_id": 4})
    # 完全重複ペア（phrase も japanese も同一＝実データの Pardonu min 相当）
    entries.append({"phrase": "Pardonu min", "japanese": "申し訳ありません。", "level": 1, "phrase_id": 5})
    entries.append({"phrase": "Pardonu min", "japanese": "申し訳ありません。", "level": 1, "phrase_id": 6})
    # 残りは全て相異なる（4択を成立させる余裕を持たせる）
    for i in range(7, 15):
        entries.append({"phrase": f"Frazo {i}", "japanese": f"文{i}", "level": 1, "phrase_id": i})
    return entries


class SentenceQuestionOptionUniquenessTests(unittest.TestCase):
    def _check_direction(self, direction: str, display_key: str) -> None:
        entries = _make_entries()
        any_question = False
        for seed in range(20):  # 複数シードでシャッフル順を変えて網羅
            questions = build_questions(entries, levels={1}, rng=random.Random(seed), direction=direction)
            for q in questions:
                any_question = True
                labels = [opt[display_key] for opt in q["options"]]
                self.assertEqual(
                    len(set(labels)),
                    len(labels),
                    msg=f"direction={direction} seed={seed} で同一表示の選択肢が発生: {labels}",
                )
                # 正解インデックスが範囲内で整合していること。
                self.assertTrue(0 <= q["answer_index"] < len(q["options"]))
        self.assertTrue(any_question, f"direction={direction}: 質問が1件も生成されず検証が空振り")

    def test_eo_to_ja_options_have_unique_japanese(self):
        # エスペラント→日本語: 選択肢は japanese 表示。重複してはならない。
        self._check_direction("eo_to_ja", "japanese")

    def test_ja_to_eo_options_have_unique_esperanto(self):
        # 日本語→エスペラント: 選択肢は phrase(エスペラント) 表示。重複してはならない。
        self._check_direction("ja_to_eo", "phrase")


if __name__ == "__main__":
    unittest.main()
