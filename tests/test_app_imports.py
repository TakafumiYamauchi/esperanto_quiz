"""6つのエントリーアプリが import 可能（構文/import 健全）であることを守るスモークテスト。

既存のユニットテストは `app.py` および各言語版 app を一度も import しない
（`test_clone_parity` は AST テキスト解析のみ）。そのため、これらエントリーアプリに
構文エラーや import エラー（例: 削除した名前の参照、壊れた相対 import）が混入しても
従来テストでは検知できなかった。本テストはその空白を埋め、全エントリーが読み込め、
`main()` を公開していることを確認する。

各アプリは `if __name__ == "__main__": main()` ガード済みで、import だけでは Streamlit を
起動しない（モジュール定義のみ実行）。純粋追加・振る舞い不変。
"""
import importlib
import unittest

ENTRY_APPS = [
    "app",
    "app_Cxina_versio",
    "app_Korea_versio",
    "sentence_app",
    "sentence_app_Cxina_versio",
    "sentence_app_Korea_versio",
]


class EntryAppImportSmokeTests(unittest.TestCase):
    def test_entry_apps_import_and_expose_main(self):
        for name in ENTRY_APPS:
            with self.subTest(app=name):
                try:
                    module = importlib.import_module(name)
                except Exception as exc:  # noqa: BLE001 - 失敗時に原因を明示する
                    self.fail(f"{name} の import に失敗: {type(exc).__name__}: {exc}")
                self.assertTrue(
                    callable(getattr(module, "main", None)),
                    msg=f"{name} が呼び出し可能な main() を公開していない",
                )


if __name__ == "__main__":
    unittest.main()
