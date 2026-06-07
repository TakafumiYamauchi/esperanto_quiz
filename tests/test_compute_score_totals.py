"""スコア集計の中核 `score_append_utils.compute_user_score_totals` の契約を固定する。

`compute_user_score_totals` は PC/モバイル統一保存経路(`score_sync_service`)が
ユーザ別の overall / vocab / sentence 累計を算出するために呼ぶ load-bearing 関数。
にもかかわらず既存テストは `score_sync_service` 側でこの関数を **モックに差し替えて**
おり(`test_score_sync_service.py`)、内部ロジック自体は一度も直接検証されていない。

本テストはネットワーク非依存の純粋ロジック部分だけを対象に、現行の正しい振る舞いを
特性化(characterization)して回帰ガードにする。**稼働コードは変更しない**(純粋追加)。

守る不変条件:
  - overall == vocab + sentence（全行で常に成立）
  - mode 振り分けは `infer_mode`（明示 mode > sentence ヒント > vocab ヒント > fallback=vocab）
  - 同一 save_id は一度だけ計上（`iter_unique_score_rows`）／空 save_id は重複排除しない
  - user は前後空白を無視して厳密一致でフィルタ／空ユーザは全ゼロ
  - points は `_safe_float` で頑健に数値化（None/空/非数値/欠落は 0.0、クラッシュしない）
"""
import math
import unittest

from score_append_utils import compute_user_score_totals


class ComputeUserScoreTotalsContractTests(unittest.TestCase):
    def test_empty_user_returns_zeros(self):
        records = [{"user": "alice", "points": "100", "mode": "vocab"}]
        for user in ("", "   ", None):
            totals = compute_user_score_totals(records, user)
            self.assertEqual(totals, {"overall": 0.0, "vocab": 0.0, "sentence": 0.0})

    def test_empty_or_nondict_records_safe(self):
        self.assertEqual(
            compute_user_score_totals([], "alice"),
            {"overall": 0.0, "vocab": 0.0, "sentence": 0.0},
        )
        # 非 dict 要素は iter_unique_score_rows が読み飛ばす（クラッシュしない）。
        messy = [None, "not-a-row", 42, {"user": "alice", "points": "5", "mode": "vocab"}]
        totals = compute_user_score_totals(messy, "alice")
        self.assertEqual(totals["vocab"], 5.0)
        self.assertEqual(totals["overall"], 5.0)

    def test_overall_equals_vocab_plus_sentence_with_mode_inference(self):
        records = [
            {"user": "alice", "points": "100", "mode": "vocab"},      # 明示 vocab
            {"user": "alice", "points": "50", "mode": "sentence"},    # 明示 sentence
            {"user": "alice", "points": "30", "phrase_id": "200"},    # sentence ヒント
            {"user": "alice", "points": "20", "group_id": "g1"},      # vocab ヒント
            {"user": "bob", "points": "999", "mode": "vocab"},        # 別ユーザ→除外
        ]
        totals = compute_user_score_totals(records, "alice")
        self.assertEqual(totals["vocab"], 120.0)     # 100 + 20
        self.assertEqual(totals["sentence"], 80.0)   # 50 + 30
        self.assertEqual(totals["overall"], 200.0)
        # 不変条件: overall は常に vocab + sentence の和。
        self.assertAlmostEqual(totals["overall"], totals["vocab"] + totals["sentence"])

    def test_conflicting_hints_resolve_to_sentence(self):
        # sentence ヒントと vocab ヒントが同居する行は sentence に計上される
        # （infer_mode が sentence ヒントを先に判定する＝集計ルーティングの確定仕様）。
        records = [{"user": "alice", "points": "40", "phrase_id": "1", "group_id": "g1"}]
        totals = compute_user_score_totals(records, "alice")
        self.assertEqual(totals["sentence"], 40.0)
        self.assertEqual(totals["vocab"], 0.0)

    def test_save_id_dedup_counts_once_blank_not_deduped(self):
        records = [
            {"user": "alice", "points": "100", "mode": "vocab", "save_id": "s1"},
            {"user": "alice", "points": "100", "mode": "vocab", "save_id": "s1"},  # 重複→除外
            {"user": "alice", "points": "10", "mode": "vocab", "save_id": ""},     # 空→計上
            {"user": "alice", "points": "10", "mode": "vocab", "save_id": ""},     # 空→計上
        ]
        totals = compute_user_score_totals(records, "alice")
        self.assertEqual(totals["vocab"], 120.0)   # 100(一度) + 10 + 10
        self.assertEqual(totals["overall"], 120.0)
        self.assertEqual(totals["sentence"], 0.0)

    def test_user_filter_trims_whitespace_on_both_sides(self):
        records = [
            {"user": "  alice  ", "points": "7", "mode": "vocab"},
            {"user": "alice", "points": "3", "mode": "vocab"},
        ]
        # 引数側・行側の双方を strip して一致させる。
        totals = compute_user_score_totals(records, "  alice  ")
        self.assertEqual(totals["vocab"], 10.0)

    def test_points_coercion_is_robust(self):
        records = [
            {"user": "alice", "mode": "vocab"},                     # points 欠落 → 0.0
            {"user": "alice", "points": None, "mode": "vocab"},     # None → 0.0
            {"user": "alice", "points": "", "mode": "vocab"},       # 空文字 → 0.0
            {"user": "alice", "points": "abc", "mode": "vocab"},    # 非数値 → 0.0
            {"user": "alice", "points": "nan", "mode": "vocab"},    # NaN → 0.0
            {"user": "alice", "points": "12.5", "mode": "vocab"},   # 正常
            {"user": "alice", "points": 100, "mode": "vocab"},      # int も可
        ]
        totals = compute_user_score_totals(records, "alice")
        self.assertEqual(totals["vocab"], 112.5)
        self.assertTrue(math.isfinite(totals["overall"]))


if __name__ == "__main__":
    unittest.main()
