"""スコア計算の『絶対値』を固定する回帰テスト。

`tests/test_quiz_logic_parity.py` は Python(`quiz_scoring.py`) と JS(`quiz_core.mjs`) が
互いに一致することを保証するが、両方を同時に同じ値へ変えると（例: BASE_POINTS 10→12）
パリティは緑のまま得点だけが静かに変わってしまう。本テストは、仕様の定数から手計算で
独立に導いた期待値で絶対値を固定し、その種の退行を検知する。

期待値の導出（quiz_scoring.py の定数より）:
  BASE_POINTS=10, STREAK_BONUS=0.5, stage={beginner:1.0,intermediate:1.3,advanced:1.6}
  SENTENCE_SCORE_SCALE=2/1.5, SENTENCE_STREAK_SCALE=2.0, SPARTAN=0.7
  vocab正解   = 10*stage + max(0,streak-1)*0.5
  sentence正解 = (level+11.5)*(2/1.5) + max(0,streak-1)*0.5*2.0
  accuracy_bonus = accuracy * total * (vocab:5.0 / sentence:10.0)
純粋追加・振る舞い不変。
"""
import unittest

from quiz_scoring import compute_result_summary, scale_spartan_points, score_for_correct


class QuizScoringValueTests(unittest.TestCase):
    def test_vocab_correct_points(self):
        # 10*1.0 + 0
        self.assertAlmostEqual(score_for_correct(mode="vocab", streak=1, stages=["beginner"]), 10.0)
        # 10*1.3 + 1*0.5
        self.assertAlmostEqual(score_for_correct(mode="vocab", streak=2, stages=["intermediate"]), 13.5)
        # 10*1.6 + 2*0.5
        self.assertAlmostEqual(score_for_correct(mode="vocab", streak=3, stages=["advanced"]), 17.0)
        # 連続ボーナスは2問目以降（streak=1 では0）
        self.assertAlmostEqual(score_for_correct(mode="vocab", streak=1, stages=["advanced"]), 16.0)

    def test_sentence_correct_points(self):
        # (5+11.5)*(2/1.5) + 0 = 22.0
        self.assertAlmostEqual(score_for_correct(mode="sentence", streak=1, level=5), 22.0)
        # (12+11.5)*(2/1.5) + 2*0.5*2.0 = 31.3333.. + 2.0
        self.assertAlmostEqual(score_for_correct(mode="sentence", streak=3, level=12), 23.5 * (2 / 1.5) + 2.0)
        # (0+11.5)*(2/1.5)
        self.assertAlmostEqual(score_for_correct(mode="sentence", streak=1, level=0), 11.5 * (2 / 1.5))

    def test_spartan_scaling(self):
        self.assertAlmostEqual(scale_spartan_points(100), 70.0)
        self.assertAlmostEqual(scale_spartan_points(0), 0.0)

    def test_result_summary_vocab(self):
        s = compute_result_summary(mode="vocab", total=10, correct=8, main_points=100.0, spartan_scaled_points=0.0)
        self.assertAlmostEqual(s["accuracy"], 0.8)
        self.assertAlmostEqual(s["accuracyBonus"], 40.0)   # 0.8 * 10 * 5.0
        self.assertAlmostEqual(s["points"], 140.0)         # 100 + 0 + 40

    def test_result_summary_sentence_uses_higher_bonus(self):
        s = compute_result_summary(mode="sentence", total=10, correct=10, main_points=200.0, spartan_scaled_points=14.0)
        self.assertAlmostEqual(s["accuracy"], 1.0)
        self.assertAlmostEqual(s["accuracyBonus"], 100.0)  # 1.0 * 10 * 10.0
        self.assertAlmostEqual(s["points"], 314.0)         # 200 + 14 + 100

    def test_result_summary_zero_total_no_division_error(self):
        s = compute_result_summary(mode="vocab", total=0, correct=0, main_points=0.0, spartan_scaled_points=0.0)
        self.assertEqual(s["accuracy"], 0)
        self.assertAlmostEqual(s["points"], 0.0)


if __name__ == "__main__":
    unittest.main()
