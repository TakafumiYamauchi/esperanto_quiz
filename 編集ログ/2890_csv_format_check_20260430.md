# 2890 CSV フォーマット点検レポート（2026-04-30）

## 対象

- `2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv`
- 照合用コピー: `編集ログ/2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv`
- 比較元: `2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv`

## 結論

CSVフォーマットとしての破損は見つからなかった。

## 確認結果

- UTF-8 BOM: あり
- 改行コード: CRLFのみ
- 物理行数: 2891行
- CSV行数: 2891行
- データ行数: 2890行
- 全行列数: 9列
- 空行: なし
- NULバイト: なし
- UTF-8デコード: 成功
- Python `csv.reader(strict=True)` による厳格パース: 成功
- 物理行ごとのCSVパース: 全行9列で成功
- 引用符数: 各物理行で偶数、未閉じ引用符なし
- 標準CSV最小引用での再シリアライズ: 元ファイルと完全一致
- 先頭・末尾に余分な空白を持つセル: なし
- セル内改行: なし
- 重複語根: なし
- 語根数: 2890件、すべて一意

## 比較元CSVとの整合

- 行数: 一致
- ヘッダー: 一致
- 語根順序: 一致
- 4列目以降のメタデータ列: 一致
- 変更は日中韓注釈列に限定されている

## 編集ログ側コピーとの整合

- ルート側CSVと `編集ログ/` 側CSVはバイト単位で完全一致。

## 保護対象記法のカウント

- `>>`: 435
- `=`: 154
- `[~`: 10
- `{Ｂ}`: 2633
- `{Ｏ}`: 278

## レベル列の形式

- `Level_JP_Num`, `Level_JP_Scaled`, `Unified_Level` は空欄を除き数値としてパース可能。
- `Level_JP`, `Level_CN` の値分布にもCSV破損を示す異常は見つからなかった。

## 備考

- 今回はフォーマット点検のみで、CSV本文の修正は行っていない。
- `=...` 形式の参照や `[~...]` 形式の派生語メモは、仕様上保持すべき既存記法として扱い、フォーマットエラーとは判定していない。
