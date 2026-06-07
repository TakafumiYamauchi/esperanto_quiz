"""`score_row_utils.infer_mode` のモード判定の優先順位契約を固定する。

スコア行が vocab か sentence かを、明示 `mode` → sentence ヒント列 → vocab ヒント列 →
fallback の順で推論する（既知のやや脆い箇所）。とくに重要な契約:
  - 明示 `mode`（別名含む）が最優先。
  - sentence ヒントと vocab ヒントが両方ある場合は **sentence が勝つ**（sentence を先に判定）。
  - 空欄（None / NaN / 空文字）のヒントは無視する。
  - ヒントが無ければ fallback（既定 vocab）。

この推論は `Scores` 集計や累積更新の振り分けに使われるため、優先順位が静かに反転すると
スコアが誤って集計されうる。本テストでその契約をロックする。純粋追加・振る舞い不変。
"""
import unittest

from score_row_utils import SENTENCE_MODE, VOCAB_MODE, infer_mode


class InferModeContractTests(unittest.TestCase):
    def test_explicit_mode_and_aliases_win(self):
        self.assertEqual(infer_mode({"mode": "sentence"}), SENTENCE_MODE)
        self.assertEqual(infer_mode({"mode": "vocab"}), VOCAB_MODE)
        self.assertEqual(infer_mode({"mode": "phrase"}), SENTENCE_MODE)   # alias
        self.assertEqual(infer_mode({"mode": "words"}), VOCAB_MODE)       # alias

    def test_explicit_mode_overrides_conflicting_hints(self):
        # 明示 mode は、矛盾するヒントがあっても優先される。
        self.assertEqual(infer_mode({"mode": "vocab", "topic": "X", "phrase_id": 3}), VOCAB_MODE)
        self.assertEqual(infer_mode({"mode": "sentence", "group_id": "noun:g1"}), SENTENCE_MODE)

    def test_single_sided_hints(self):
        self.assertEqual(infer_mode({"phrase_id": 3}), SENTENCE_MODE)
        self.assertEqual(infer_mode({"topic": "Greetings"}), SENTENCE_MODE)
        self.assertEqual(infer_mode({"group_id": "noun:g1"}), VOCAB_MODE)
        self.assertEqual(infer_mode({"seed": 42}), VOCAB_MODE)

    def test_conflicting_hints_sentence_wins(self):
        # sentence ヒントと vocab ヒントが両立 → sentence が勝つ（先に判定するため）。
        self.assertEqual(infer_mode({"topic": "X", "group_id": "g1"}), SENTENCE_MODE)

    def test_blank_hints_are_ignored(self):
        nan = float("nan")
        self.assertEqual(infer_mode({"topic": "", "group_id": "g1"}), VOCAB_MODE)
        self.assertEqual(infer_mode({"group_id": "", "phrase_id": 5}), SENTENCE_MODE)
        self.assertEqual(infer_mode({"topic": nan, "group_id": "g1"}), VOCAB_MODE)

    def test_fallback_when_no_signal(self):
        self.assertEqual(infer_mode({}), VOCAB_MODE)                 # 既定 fallback
        self.assertEqual(infer_mode({}, fallback="sentence"), SENTENCE_MODE)


if __name__ == "__main__":
    unittest.main()
