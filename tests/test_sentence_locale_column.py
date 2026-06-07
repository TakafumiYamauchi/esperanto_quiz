"""例文版クローンが『正しいローカライズ翻訳列』を読むことを守る (i18n の根幹)。

例文アプリは翻訳を汎用キー `"japanese"` に格納し、`build_questions` はそのキーで
選択肢を表示・重複排除する。各言語版は CSV の異なる列をこのキーへ読み込む:
  - sentence_app.py (ja)         : 日本語 / Japanese
  - sentence_app_Cxina_versio.py : 中文 / Chinese
  - sentence_app_Korea_versio.py : 한국어 / Korean

`test_clone_parity` は文字列定数をマスクするため、この列名の取り違え（例: zh 版が
誤って「日本語」列を読む → 中国語ユーザーに日本語が表示される）を検知できない。
本テストがそのギャップを埋め、`col_ja = _get_col(df, [...])` の候補列が言語ごとに
正しいことを AST で検証する。純粋追加・振る舞い不変。
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ファイル -> その言語版が col_ja に読み込むべき主列。
EXPECTED_PRIMARY_COLUMN = {
    "sentence_app.py": "日本語",
    "sentence_app_Cxina_versio.py": "中文",
    "sentence_app_Korea_versio.py": "한국어",
}


def _col_ja_candidate_columns(path: Path):
    """`col_ja = _get_col(df, [<候補列...>])` の候補列名リストを返す。"""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "col_ja" for t in node.targets
        ):
            call = node.value
            if (
                isinstance(call, ast.Call)
                and getattr(call.func, "id", None) == "_get_col"
                and len(call.args) >= 2
                and isinstance(call.args[1], ast.List)
            ):
                return [
                    elt.value
                    for elt in call.args[1].elts
                    if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                ]
    return None


class SentenceLocaleColumnTests(unittest.TestCase):
    def test_each_clone_reads_its_localized_column(self):
        for filename, primary in EXPECTED_PRIMARY_COLUMN.items():
            with self.subTest(file=filename):
                candidates = _col_ja_candidate_columns(ROOT / filename)
                self.assertIsNotNone(
                    candidates, msg=f"{filename}: col_ja = _get_col(df, [...]) が見つからない"
                )
                self.assertEqual(
                    candidates[0],
                    primary,
                    msg=(
                        f"{filename} の翻訳列が誤り: 期待 先頭='{primary}' 実際={candidates}"
                        "（言語版が誤った翻訳列を表示する退行）"
                    ),
                )

    def test_clones_do_not_read_japanese_for_zh_ko(self):
        # zh/ko 版が日本語列を読んでいないこと（取り違えの明示的ガード）。
        for filename in ("sentence_app_Cxina_versio.py", "sentence_app_Korea_versio.py"):
            with self.subTest(file=filename):
                candidates = _col_ja_candidate_columns(ROOT / filename) or []
                self.assertNotIn("日本語", candidates, msg=f"{filename} が日本語列を読んでいる")


if __name__ == "__main__":
    unittest.main()
