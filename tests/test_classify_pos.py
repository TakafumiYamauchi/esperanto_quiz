"""`vocab_grouping.classify_pos` の品詞分類を具体例で固定する回帰テスト。

2026-06-07 の分類器修正（数詞regex の厳格化＋`CORRELATIVE_PREFIXES` からの `"ĉ"` 除去）
を、誤分類されていた実単語を使って明示的にロックする。将来 regex や接頭辞リストを
触って退行（例: `okulo` が再び numeral に戻る）したら即CI失敗する。純粋追加・振る舞い不変。

各期待値は実装の現出力を実機確認済み（言語的にも妥当）。
"""
import unittest

from vocab_grouping import classify_pos


class ClassifyPosRegressionTests(unittest.TestCase):
    # 旧 regex `[a-zĉĝĥĵŝŭ]*` が数詞語根で始まる普通の語を numeral に誤分類していた。
    # 厳格化後は本来の品詞へ。
    FIXED_FALSE_NUMERALS = {
        # 名詞 (-o 系)
        "okulo": "noun", "oktobro": "noun", "septembro": "noun", "centro": "noun",
        "centralo": "noun", "kvartalo": "noun", "duŝo": "noun", "tribunalo": "noun",
        "centimetro": "noun", "milimetro": "noun",
        # 動詞 (-i 系)
        "trinki": "verb", "deklari": "verb", "dubi": "verb", "dungi": "verb",
        "militi": "verb", "okazi": "verb", "okupi": "verb", "triki": "verb",
        # 形容詞 (-a)
        "dekstra": "adjective", "milda": "adjective",
        # 接続詞
        "dum": "conjunction",
    }

    # 厳格化後も本物の数詞は numeral のまま。
    REAL_NUMERALS = [
        "unu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "naŭ", "dek",
        "cent", "mil", "nul", "nulo", "miliono", "miliardo",
    ]

    # `"ĉ"` 接頭辞の除去で `ĉe`/`ĉu` が相関詞誤分類から本来の品詞へ。
    FIXED_FALSE_CORRELATIVES = {"ĉe": "preposition", "ĉu": "conjunction"}

    # `"ĉi"` 接頭辞は残したので、本物の `ĉi`系・他の相関詞は維持。
    REAL_CORRELATIVES = ["ĉio", "ĉiu", "ĉiam", "ĉie", "kiu", "tio", "neniam", "ie"]

    # 一般的な形態規則（語尾ベース）。
    MORPHOLOGY = {
        "-a": "suffix", "hundo": "noun", "sukceso": "noun",
        "kuri": "verb", "manĝi": "verb", "bela": "adjective", "rapide": "adverb",
    }

    def test_fixed_false_numerals_are_no_longer_numeral(self):
        for word, expected in self.FIXED_FALSE_NUMERALS.items():
            with self.subTest(word=word):
                self.assertEqual(classify_pos(word), expected)
                self.assertNotEqual(classify_pos(word), "numeral")

    def test_real_numerals_remain_numeral(self):
        for word in self.REAL_NUMERALS:
            with self.subTest(word=word):
                self.assertEqual(classify_pos(word), "numeral")

    def test_fixed_false_correlatives_are_no_longer_correlative(self):
        for word, expected in self.FIXED_FALSE_CORRELATIVES.items():
            with self.subTest(word=word):
                self.assertEqual(classify_pos(word), expected)

    def test_real_correlatives_remain_correlative(self):
        for word in self.REAL_CORRELATIVES:
            with self.subTest(word=word):
                self.assertEqual(classify_pos(word), "correlative")

    def test_basic_morphology_rules(self):
        for word, expected in self.MORPHOLOGY.items():
            with self.subTest(word=word):
                self.assertEqual(classify_pos(word), expected)


if __name__ == "__main__":
    unittest.main()
