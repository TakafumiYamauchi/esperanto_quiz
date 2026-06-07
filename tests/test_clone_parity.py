"""言語版クローンのロジック同期を守るガード（最大の保守リスク=clone driftの検知）。

ZH/KO 版（`*_Cxina_versio.py` / `*_Korea_versio.py`）はベース（`app.py` /
`sentence_app.py`）の手動コピーで、設計上の差分は「翻訳・UI文言・URL などの
文字列」と「`main()` 内の言語別ルーティング2か所」だけのはず:
  1. 兄弟モジュールの取り込み名（`from sentence_app import main` 等）
  2. `render_mobile_app_entry(...)` の言語別引数（source / target_lang / default_mode）

本テストは、それ以外のコード構造（制御フロー・数値定数・演算子・関数の有無）が
ベースと各変種で完全一致することを AST レベルで検証する。文字列定数・上記2か所は
正規化して無視するので、翻訳や言語ルーティングの正当な差分では失敗しない。

ベースに入れた修正を言語版へ反映し忘れる（= 実ドリフト）と、このテストが失敗して
即座に検知できる。振る舞いは一切変えない純粋追加。Python 3.8 互換。
"""
import ast
import copy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAIRS = [
    ("app.py", "app_Cxina_versio.py"),
    ("app.py", "app_Korea_versio.py"),
    ("sentence_app.py", "sentence_app_Cxina_versio.py"),
    ("sentence_app.py", "sentence_app_Korea_versio.py"),
]

# 言語別に意図的に引数が変わるルーティング関数（呼び出し引数を正規化対象にする）
ROUTING_CALLS = {"render_mobile_app_entry"}


class _Normalizer(ast.NodeTransformer):
    """言語版で正当に変わる箇所（文字列・兄弟import名・ルーティング呼び出し引数）を
    プレースホルダ化し、それ以外の構造差だけを残す。"""

    def visit_Constant(self, node):
        if isinstance(node.value, (str, bytes)):
            return ast.copy_location(ast.Constant(value="<STR>"), node)
        return node

    def visit_ImportFrom(self, node):
        self.generic_visit(node)
        node.module = "<MODULE>"
        return node

    def visit_Call(self, node):
        self.generic_visit(node)
        func_name = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
        if func_name in ROUTING_CALLS:
            node.args = []
            node.keywords = []
        return node


def _normalized_functions(path: Path) -> dict:
    """トップレベル関数名 -> 正規化AST(ダンプ) の辞書。"""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    funcs = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs[node.name] = ast.dump(_Normalizer().visit(copy.deepcopy(node)))
    return funcs


class CloneParityTests(unittest.TestCase):
    def test_language_clones_share_identical_logic(self):
        for base_name, variant_name in PAIRS:
            with self.subTest(pair=f"{base_name} vs {variant_name}"):
                base = _normalized_functions(ROOT / base_name)
                variant = _normalized_functions(ROOT / variant_name)

                self.assertEqual(
                    set(base),
                    set(variant),
                    msg=(
                        f"{base_name} と {variant_name} でトップレベル関数の集合が不一致: "
                        f"base only={sorted(set(base) - set(variant))} "
                        f"variant only={sorted(set(variant) - set(base))}"
                    ),
                )

                for name in sorted(set(base) & set(variant)):
                    with self.subTest(function=name):
                        self.assertEqual(
                            base[name],
                            variant[name],
                            msg=(
                                f"{name}() のロジック構造が {base_name} と {variant_name} で"
                                f"乖離（clone drift）。ベースの修正を言語版へ反映してください。"
                            ),
                        )


if __name__ == "__main__":
    unittest.main()
