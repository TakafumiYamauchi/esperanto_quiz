# テストスイート

「現状ある程度動いているアプリ」を壊さずに保守するための回帰ガード集。各テストが
「何を守るか」を一覧化する。**いずれも稼働コードの振る舞いは変えない検査**である。

## 実行方法

```bash
# Python 単体テスト（CIゲート）— 69 tests。リポジトリ直下から discover で実行する。
npm run test:unit          # = python3 -m unittest discover -s tests -p 'test_*.py'

# アセット整合（CSV↔JSON↔音声キー↔manifest、WAVヘッダ）
npm run validate:mobile-assets          # 完全
npm run validate:mobile-assets:quick    # WAVヘッダ省略

# Playwright E2E（手動・ローカルのみ。CIには含まれない）
npm run test:mobile            # 静的PWAの再読込復元・結果・履歴
npm run test:streamlit-mobile  # Streamlit埋め込みモバイルの再読込復元
```

> 注: `tests/` はパッケージではない（`__init__.py` 無し）。`python3 -m unittest tests.<module>`
> は `ModuleNotFoundError` になるため、必ず `discover` で実行する。

## Python 単体テスト（69）

### スコア計算・グループ化のパリティ／正当性
| ファイル | 件 | 守る対象 |
|---|---|---|
| `test_quiz_logic_parity.py` | 2 | Python(`quiz_scoring.py`+`build_groups`) ↔ JS(`quiz_core.mjs`) がスコアもグループ化も一致（`node` を起動して比較） |
| `test_quiz_scoring_values.py` | 6 | スコアの**絶対値**（手計算の期待値）。両言語同時の定数ドリフトを検知（パリティでは見逃す） |
| `test_classify_pos.py` | 5 | 品詞分類器: 数詞/相関詞の誤分類是正が退行しないこと・本物の数詞/相関詞の維持・基本形態規則 |

### 4択ビルダー
| ファイル | 件 | 守る対象 |
|---|---|---|
| `test_vocab_question_options.py` | 3 | 単語: グループ内表示の一意性（カナリア）＋ビルダーが表示重複誤答を排除（予防） |
| `test_sentence_question_options.py` | 2 | 例文: direction対応の表示重複排除（実データに重複が存在する load-bearing ロジック） |
| `test_sentence_locale_column.py` | 2 | zh/ko 例文クローンが正しいローカライズ列(中文/한국어)を読む（i18n。`clone_parity` の盲点を補完） |

### ファイル間の整合
| ファイル | 件 | 守る対象 |
|---|---|---|
| `test_clone_parity.py` | 1 | 6エントリーアプリ(ja/zh/ko × 単語/例文)の共有ロジックが構造的に一致（クローン・ドリフト＝最大の保守リスク） |
| `test_phrase_offset_consistency.py` | 3 | 例文キーの `PhraseID` オフセットが `data_sources.PHRASE_ID_OFFSET` に一元化され、どこにも直書きが無いこと |
| `test_app_imports.py` | 1 | 6エントリーアプリが import 可能で `main()` を公開（構文/import スモーク） |

### ナビゲーション・状態・スコアバックエンド
| ファイル | 件 | 守る対象 |
|---|---|---|
| `test_classic_navigation.py` | 4 | URLクエリパラメータ → クイズモード解決 |
| `test_classic_session_persistence.py` | 6 | PCクラシック版の localStorage スナップショット 生成/検証/復元 |
| `test_infer_mode.py` | 6 | vocab/sentence モード推論の優先順位契約（明示>sentenceヒント>vocabヒント>fallback、競合時sentence勝ち） |
| `test_score_sync_service.py` | 3 | 共有スコア同期サービスの累積振り分け（overall / sentence） |
| `test_compute_score_totals.py` | 7 | スコア集計中核 `compute_user_score_totals` の契約: overall==vocab+sentence／`infer_mode`振り分け／`save_id`重複排除／userフィルタ／points頑健化（保存経路で唯一の無テスト関数だった） |
| `test_score_row_alignment.py` | 11 | 列整列レイヤ: `_row_from_headers`(レコード→実ヘッダ順の行)＋`_read_records_from_values`(生シート→records、短行パディング・全空行ドロップ・内部空ヘッダ列は左シフトせず安全) |
| `test_mobile_score_ranking.py` | 7 | モバイルのスコア保存(`save_id`冪等・recoverable)＋ランキング集計(JST・max-merge) |

## Playwright E2E（手動・ローカル）
| ファイル | 守る対象 |
|---|---|
| `mobile-pwa.spec.js` | 静的PWA: 再読込復元・結果/履歴・保存データ復旧 |
| `streamlit-mobile.spec.js` | Streamlit埋め込みモバイル: 再読込復元・結果/履歴 |
