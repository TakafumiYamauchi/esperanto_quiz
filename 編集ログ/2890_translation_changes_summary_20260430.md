# 2890 CSV 注釈修正内容まとめ（2026-04-30）

## 概要

- 対象: `2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv`
- 比較元: `2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv`
- 元CSVから差分がある語根数: **276件**
- 変更された注釈セル数: **453セル**（日本語 99、中国語 205、韓国語 149）
- ルート側CSVと `編集ログ/` 側CSVは同内容になるよう反映済み。

## 修正方針

- 4択クイズの選択肢として読んだとき、語義不足・誤解・不自然さが出やすい注釈を中心に修正した。
- PIV本文、日本語・中国語・韓国語の対応関係を見比べ、欠けている主要義や専門分野義だけを最小限補った。
- 「語根露出」「未解決参照（`>>...`、`=...`）」「派生語メモ（`[~o]` など）」は修正対象外として維持した。
- `{Ｂ}` などの記号は削除・変更していない。
- 中国語欄の補足が最も多く、次に韓国語欄、日本語欄は少数の調整に留めた。

## 修正内容の大まかな分類

### 1. 専門分野義の不足補足

PIVや他言語欄では示されているのに、ある言語欄だけ抜けていた分野義を補った。
例: `legi` の中国語に `（信息）读取`、`skribi` に `（信息）写入`、`masko` に `（摄影）遮片`、`fliki` に `（计算机）打补丁`、`maksimumo` に `极大值`、`radiko` に数学の `根、方根`、`reala` に数学の実数義、`karaktero` に生物学の `性状，形质`、`ideologio` に哲学の `观念学`、`projekto` に工学上の設計資料義を追加。

### 2. 日中韓の語義対応のずれを調整

日本語・韓国語にはあるが中国語にはない、またはその逆の語義を補い、三言語の選択肢としての粒度を近づけた。
例: `gento` の民族義、`mistero` の宗教一般義、`tradicio` の宗教上の聖伝、`osto` の料理上の骨、`katastrofo` の劇作上の結末、`miopa` や `eĥo` の転義、`sekso` の古い文法義、`rolo` の劇の配役義、`varbi` の軍事徴募義を補った。

### 3. 4択で誤答を誘いやすい狭すぎる訳を拡張

訳語が一部の意味に寄りすぎている場合、選択肢として必要な範囲を少し広げた。
例: `radiko` の中国語は `方根` だけだと平方根寄りに見えるため、方程式の根も含む `（数）根、方根` にした。`afiŝo` の中国語は広告に限定されすぎないよう、ポスター・掲示物を示す語に自然化した。`ludi` は遊戯義だけに見えないよう、PIV第1義の「たわむれる・自由に動く」範囲を補った。`proceso` は法廷の訴訟だけに限定されないよう、過程・プロセス義を補った。`stelo` は天体・記号だけでなく芸能上のスター義も補った。`fondi` は「創立する」だけでなく「根拠を置く」義も読めるよう中国語を補った。`fortuno` は `sorto` と重なりすぎる「運命」寄りの訳を幸運・つきへ戻し、`integra` は「不可欠」寄りではなく完全・欠けのなさを中心に調整した。`firma` と `vegeti` は中国語の表現をより自然な範囲に調整した。`tekniko` は単独語として「工学」より技術・技法・手法が中心になるよう日本語・韓国語を調整し、`kotizi` は会費だけでなく分担金を支払う義も読めるよう中国語・韓国語を広げた。

### 4. 他言語表記の混入修正

中国語欄・韓国語欄に別言語の表記が紛れ込んでいる箇所は、意味を変えずに当該言語の自然な表記へ直した。
例: `kaldrono` の中国語欄に混入していた日本語カタカナ `カルデラ` を、中国語の地理用語 `破火山口，火山口凹地` に調整。

### 5. 過補正を避けて保留したもの

単なる分野ラベル差、既存訳で自然に吸収できる意味、表記統一だけの変更は原則として見送った。
例: `treni` の情報分野ラベル付きドラッグ義は、中国語の `拖，拉，拽` でUI上のドラッグにも読めるため追加せず、`presi` の `印刷` はプリント義も含められるため未修正。

### 6. 誤解を招く専門義の修正

既存注釈がPIVの細部義を別概念として読ませてしまう箇所は、必要最小限で直した。
例: `oriento` のフリーメーソン関連義は「地方支部」ではなく、ロッジ内で長が座る東側席を指すため、日中韓の該当補足を修正した。

## 追加された巡回レビュー記録

- `編集ログ/2890_translation_review_20260430_twentyseventh_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_twentyeighth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_twentyninth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtieth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyfirst_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtysecond_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtythird_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyfourth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyfifth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtysixth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyseventh_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyeighth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_thirtyninth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortieth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortyfirst_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortysecond_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortythird_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortyfourth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortyfifth_pass_rows0001-2890.md`
- `編集ログ/2890_translation_review_20260430_fortysixth_pass_rows1201-1400.md`
- `編集ログ/2890_translation_review_20260430_fortyseventh_pass_rows1401-1500.md`
- `編集ログ/2890_translation_review_20260430_fortyeighth_pass_rows1501-1600.md`
- `編集ログ/2890_translation_review_20260430_fortyninth_pass_rows1601-1700.md`
- `編集ログ/2890_translation_review_20260430_fiftieth_pass_rows1701-1800.md`
- `編集ログ/2890_translation_review_20260430_fiftyfirst_pass_rows1801-1900.md`
- `編集ログ/2890_translation_review_20260430_fiftysecond_pass_rows1901-2000.md`
- `編集ログ/2890_translation_review_20260430_fiftythird_pass_rows2001-2100.md`
- `編集ログ/2890_translation_review_20260430_fiftyfourth_pass_rows2101-2200.md`
- `編集ログ/2890_translation_review_20260430_fiftyfifth_pass_rows2201-2300.md`
- `編集ログ/2890_translation_review_20260430_fiftysixth_pass_rows2301-2400.md`
- `編集ログ/2890_translation_review_20260430_fiftyseventh_pass_rows2401-2500.md`
- `編集ログ/2890_translation_review_20260430_fiftyeighth_pass_rows2501-2600.md`
- `編集ログ/2890_translation_review_20260430_fiftyninth_pass_rows2601-2700.md`
- `編集ログ/2890_translation_review_20260430_sixtieth_pass_rows2701-2800.md`
- `編集ログ/2890_translation_review_20260430_sixtyfirst_pass_rows2801-2890.md`
- `編集ログ/2890_translation_review_20260430_sixtysecond_pass_rows0001-0100.md`
- `編集ログ/2890_translation_review_20260430_sixtythird_pass_rows0101-0200.md`
- `編集ログ/2890_translation_review_20260430_sixtyfourth_pass_rows0201-0300.md`
- `編集ログ/2890_translation_review_20260430_sixtyfifth_pass_rows0301-0400.md`
- `編集ログ/2890_translation_review_20260430_sixtysixth_pass_rows0401-0500.md`
- `編集ログ/2890_translation_review_20260430_sixtyseventh_pass_rows0501-0600.md`
- `編集ログ/2890_translation_review_20260430_sixtyeighth_pass_rows0601-0700.md`
- `編集ログ/2890_translation_review_20260430_sixtyninth_pass_rows0701-0800.md`
- `編集ログ/2890_translation_review_20260430_seventieth_pass_rows0801-0900.md`
- `編集ログ/2890_translation_review_20260430_seventyfirst_pass_rows0901-1000.md`
- `編集ログ/2890_translation_review_20260430_seventysecond_pass_rows1001-1100.md`
- `編集ログ/2890_translation_review_20260430_seventythird_pass_rows1101-1200.md`
- `編集ログ/2890_translation_review_20260430_seventyfourth_pass_rows1201-1300.md`
- `編集ログ/2890_translation_review_20260430_seventyfifth_pass_rows1301-1400.md`
- `編集ログ/2890_translation_review_20260430_seventysixth_pass_rows1401-1500.md`
- `編集ログ/2890_translation_review_20260430_seventyseventh_pass_rows1501-1600.md`
- `編集ログ/2890_translation_review_20260430_seventyeighth_pass_rows1601-1700.md`
- `編集ログ/2890_translation_review_20260430_seventyninth_pass_rows1701-1800.md`
- `編集ログ/2890_translation_review_20260430_eightieth_pass_rows1801-1900.md`
- `編集ログ/2890_translation_review_20260430_eightyfirst_pass_rows1901-2000.md`
- `編集ログ/2890_translation_review_20260430_eightysecond_pass_rows2001-2100.md`
- `編集ログ/2890_translation_review_20260430_eightythird_pass_rows2101-2200.md`
- `編集ログ/2890_translation_review_20260430_eightyfourth_pass_rows2201-2300.md`
- `編集ログ/2890_translation_review_20260430_eightyfifth_pass_rows2301-2400.md`
- `編集ログ/2890_translation_review_20260430_eightysixth_pass_rows2401-2500.md`
- `編集ログ/2890_translation_review_20260430_eightyseventh_pass_rows2501-2600.md`
- `編集ログ/2890_translation_review_20260430_eightyeighth_pass_rows2601-2700.md`
- `編集ログ/2890_translation_review_20260430_eightyninth_pass_rows2701-2800.md`
- `編集ログ/2890_translation_review_20260430_ninetieth_pass_rows2801-2890.md`
- `編集ログ/2890_translation_review_20260430_ninetyfirst_pass_rows0001-0100.md`
- `編集ログ/2890_translation_review_20260430_ninetysecond_pass_rows0101-0200.md`
- `編集ログ/2890_translation_review_20260430_ninetythird_pass_rows0201-0300.md`
- `編集ログ/2890_translation_review_20260430_ninetyfourth_pass_rows0301-0400.md`
- `編集ログ/2890_translation_review_20260430_ninetyfifth_pass_rows0401-0500.md`
- `編集ログ/2890_translation_review_20260430_ninetysixth_pass_rows0501-0600.md`
- `編集ログ/2890_translation_review_20260430_ninetyseventh_pass_rows0601-0700.md`
- `編集ログ/2890_translation_review_20260430_ninetyeighth_pass_rows0701-0800.md`
- `編集ログ/2890_translation_review_20260430_ninetyninth_pass_rows0801-0900.md`
- `編集ログ/2890_translation_review_20260430_onehundredth_pass_rows0901-1000.md`
- `編集ログ/2890_translation_review_20260430_onehundredfirst_pass_rows1001-1100.md`
- `編集ログ/2890_translation_review_20260430_onehundredsecond_pass_rows1101-1200.md`
- `編集ログ/2890_translation_review_20260430_onehundredthird_pass_rows1201-1300.md`
- `編集ログ/2890_translation_review_20260430_onehundredfourth_pass_rows1301-1400.md`
- `編集ログ/2890_translation_review_20260430_onehundredfifth_pass_rows1401-1500.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixth_pass_rows1501-1600.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventh_pass_rows1601-1700.md`
- `編集ログ/2890_translation_review_20260430_onehundredeighth_pass_rows1701-1800.md`
- `編集ログ/2890_translation_review_20260430_onehundredninth_pass_rows1801-1900.md`
- `編集ログ/2890_translation_review_20260430_onehundredtenth_pass_rows1901-2000.md`
- `編集ログ/2890_translation_review_20260430_onehundredeleventh_pass_rows2001-2100.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwelfth_pass_rows2101-2200.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirteenth_pass_rows2201-2300.md`
- `編集ログ/2890_translation_review_20260430_onehundredfourteenth_pass_rows2301-2400.md`
- `編集ログ/2890_translation_review_20260430_onehundredfifteenth_pass_rows2401-2500.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixteenth_pass_rows2501-2600.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventeenth_pass_rows2601-2700.md`
- `編集ログ/2890_translation_review_20260430_onehundredeighteenth_pass_rows2701-2800.md`
- `編集ログ/2890_translation_review_20260430_onehundrednineteenth_pass_rows2801-2890.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentieth_pass_rows0001-2890_recheck.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyfirst_pass_rows0001-0100_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentysecond_pass_rows0101-0200_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentythird_pass_rows0201-0300_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyfourth_pass_rows0301-0400_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyfifth_pass_rows0401-0500_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentysixth_pass_rows0501-0600_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyseventh_pass_rows0601-0700_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyeighth_pass_rows0701-0800_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredtwentyninth_pass_rows0801-0900_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtieth_pass_rows0901-1000_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyfirst_pass_rows1001-1100_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtysecond_pass_rows1101-1200_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtythird_pass_rows1201-1300_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyfourth_pass_rows1301-1400_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyfifth_pass_rows1401-1500_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtysixth_pass_rows1501-1600_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyseventh_pass_rows1601-1700_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyeighth_pass_rows1701-1800_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredthirtyninth_pass_rows1801-1900_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortieth_pass_rows1901-2000_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyfirst_pass_rows2001-2100_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortysecond_pass_rows2101-2200_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortythird_pass_rows2201-2300_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyfourth_pass_rows2301-2400_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyfifth_pass_rows2401-2500_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortysixth_pass_rows2501-2600_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyseventh_pass_rows2601-2700_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyeighth_pass_rows2701-2800_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfortyninth_pass_rows2801-2890_recheck2.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftieth_pass_rows0001-0100_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyfirst_pass_rows0101-0200_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftysecond_pass_rows0201-0300_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftythird_pass_rows0301-0400_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyfourth_pass_rows0401-0500_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyfifth_pass_rows0501-0600_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftysixth_pass_rows0601-0700_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyseventh_pass_rows0701-0800_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyeighth_pass_rows0801-0900_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredfiftyninth_pass_rows0901-1000_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtieth_pass_rows1001-1100_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyfirst_pass_rows1101-1200_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtysecond_pass_rows1201-1300_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtythird_pass_rows1301-1400_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyfourth_pass_rows1401-1500_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyfifth_pass_rows1501-1600_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtysixth_pass_rows1601-1700_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyseventh_pass_rows1701-1800_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyeighth_pass_rows1801-1900_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredsixtyninth_pass_rows1901-2000_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventieth_pass_rows2001-2100_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyfirst_pass_rows2101-2200_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventysecond_pass_rows2201-2300_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventythird_pass_rows2301-2400_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyfourth_pass_rows2401-2500_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyfifth_pass_rows2501-2600_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventysixth_pass_rows2601-2700_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyseventh_pass_rows2701-2800_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyeighth_pass_rows2801-2890_recheck3.md`
- `編集ログ/2890_translation_review_20260430_onehundredseventyninth_pass_rows0001-0100_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightieth_pass_rows0101-0200_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyfirst_pass_rows0201-0300_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightysecond_pass_rows0301-0400_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightythird_pass_rows0401-0500_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyfourth_pass_rows0501-0600_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyfifth_pass_rows0601-0700_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightysixth_pass_rows0701-0800_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyseventh_pass_rows0801-0900_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyeighth_pass_rows0901-1000_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredeightyninth_pass_rows1001-1100_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetieth_pass_rows1101-1200_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyfirst_pass_rows1201-1300_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetysecond_pass_rows1301-1400_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetythird_pass_rows1401-1500_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyfourth_pass_rows1501-1600_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyfifth_pass_rows1601-1700_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetysixth_pass_rows1701-1800_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyseventh_pass_rows1801-1900_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyeighth_pass_rows1901-2000_recheck4.md`
- `編集ログ/2890_translation_review_20260430_onehundredninetyninth_pass_rows2001-2100_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredth_pass_rows2101-2200_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredfirst_pass_rows2201-2300_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredsecond_pass_rows2301-2400_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredthird_pass_rows2401-2500_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredfourth_pass_rows2501-2600_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredfifth_pass_rows2601-2700_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixth_pass_rows2701-2800_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventh_pass_rows2801-2890_recheck4.md`
- `編集ログ/2890_translation_review_20260430_twohundredeighth_pass_rows0001-0100_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredninth_pass_rows0101-0200_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtenth_pass_rows0201-0300_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredeleventh_pass_rows0301-0400_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwelfth_pass_rows0401-0500_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirteenth_pass_rows0501-0600_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredfourteenth_pass_rows0601-0700_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredfifteenth_pass_rows0701-0800_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixteenth_pass_rows0801-0900_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventeenth_pass_rows0901-1000_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredeighteenth_pass_rows1001-1100_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundrednineteenth_pass_rows1101-1200_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentieth_pass_rows1201-1300_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyfirst_pass_rows1301-1400_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentysecond_pass_rows1401-1500_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentythird_pass_rows1501-1600_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyfourth_pass_rows1601-1700_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyfifth_pass_rows1701-1800_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentysixth_pass_rows1801-1900_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyseventh_pass_rows1901-2000_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyeighth_pass_rows2001-2100_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredtwentyninth_pass_rows2101-2200_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtieth_pass_rows2201-2300_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyfirst_pass_rows2301-2400_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtysecond_pass_rows2401-2500_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtythird_pass_rows2501-2600_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyfourth_pass_rows2601-2700_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyfifth_pass_rows2701-2800_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtysixth_pass_rows2801-2890_recheck5.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyseventh_pass_rows0001-0100_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyeighth_pass_rows0101-0200_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredthirtyninth_pass_rows0201-0300_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortieth_pass_rows0301-0400_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyfirst_pass_rows0401-0500_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortysecond_pass_rows0501-0600_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortythird_pass_rows0601-0700_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyfourth_pass_rows0701-0800_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyfifth_pass_rows0801-0900_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortysixth_pass_rows0901-1000_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyseventh_pass_rows1001-1100_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyeighth_pass_rows1101-1200_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfortyninth_pass_rows1201-1300_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftieth_pass_rows1301-1400_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyfirst_pass_rows1401-1500_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftysecond_pass_rows1501-1600_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftythird_pass_rows1601-1700_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyfourth_pass_rows1701-1800_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyfifth_pass_rows1801-1900_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftysixth_pass_rows1901-2000_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyseventh_pass_rows2001-2100_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyeighth_pass_rows2101-2200_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredfiftyninth_pass_rows2201-2300_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtieth_pass_rows2301-2400_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyfirst_pass_rows2401-2500_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtysecond_pass_rows2501-2600_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtythird_pass_rows2601-2700_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyfourth_pass_rows2701-2800_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyfifth_pass_rows2801-2890_recheck6.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtysixth_pass_rows0001-0100_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyseventh_pass_rows0101-0200_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyeighth_pass_rows0201-0300_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredsixtyninth_pass_rows0301-0400_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventieth_pass_rows0401-0500_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyfirst_pass_rows0501-0600_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventysecond_pass_rows0601-0700_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventythird_pass_rows0701-0800_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyfourth_pass_rows0801-0900_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyfifth_pass_rows0901-1000_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventysixth_pass_rows1001-1100_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyseventh_pass_rows1101-1200_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyeighth_pass_rows1201-1300_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredseventyninth_pass_rows1301-1400_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightieth_pass_rows1401-1500_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyfirst_pass_rows1501-1600_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightysecond_pass_rows1601-1700_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightythird_pass_rows1701-1800_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyfourth_pass_rows1801-1900_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyfifth_pass_rows1901-2000_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightysixth_pass_rows2001-2100_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyseventh_pass_rows2101-2200_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyeighth_pass_rows2201-2300_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredeightyninth_pass_rows2301-2400_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredninetieth_pass_rows2401-2500_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredninetyfirst_pass_rows2501-2600_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredninetysecond_pass_rows2601-2700_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredninetythird_pass_rows2701-2800_recheck7.md`
- `編集ログ/2890_translation_review_20260430_twohundredninetyfourth_pass_rows2801-2890_recheck7.md`

## 全変更一覧

行番号はCSVファイル上の行番号。変更前後は、実際に変わった言語欄だけを掲載する。

| 行 | 語根 | 欄 | 変更前 | 変更後 |
|---:|---|---|---|---|
| 9 | `-end-` | 中国語 | [后缀] 表示应当被…、必须被…；也可表值得被… | [后缀] 表示应当被…、必须被… |
| 17 | `-j` | 韓国語 | 복수어미 | 복수 어미 |
| 24 | `-ot-` | 日本語 | {Ｂ}［分詞接尾辞］受動・将然 | {Ｂ}［分詞接尾辞］（受動・将然） |
| 39 | `aboni` | 韓国語 | 예약하다, 구독하다 | 정기 예약하다, 구독하다 |
| 41 | `absurda` | 中国語 | 荒谬，不合逻辑 | 荒谬，不合逻辑；（哲）荒诞的 |
| 54 | `advokato` | 中国語 | 律师，辩护人 | 律师，辩护人；（转）代言人，拥护者 |
| 58 | `afiŝo` | 中国語 | 广告，招贴；（网络）帖子 | 海报，招贴，告示；（网络）帖子 |
| 73 | `akra` | 日本語 | {Ｂ}鋭い | {Ｂ}鋭い; （味・音などが）刺激の強い; 厳しい |
| 73 | `akra` | 中国語 | 锋利，尖锐 | 锋利，尖锐；刺激性强；严厉 |
| 73 | `akra` | 韓国語 | 예리한, 날카로운 | 예리한, 날카로운; 자극적인; 엄한 |
| 75 | `akto` | 日本語 | {Ｂ}【劇】幕; 【法】証書 | {Ｂ}【劇】幕; 公式行為・決定; 【法】証書 |
| 75 | `akto` | 中国語 | （戏剧）幕；（法）证书，文书 | （戏剧）幕；正式行为、决定；（法）证书，文书 |
| 75 | `akto` | 韓国語 | 연극의 막; (법) 증서, 문서 | 연극의 막; 공식 행위·결정; (법) 증서, 문서 |
| 87 | `almozo` | 日本語 | {Ｂ}施し物 | {Ｂ}施し, 施し物 |
| 99 | `amplekso` | 日本語 | {Ｂ}大きさ, 広がり; 【哲】外延; 【統】分布範囲 | {Ｂ}大きさ, 広がり; 【哲】外延; 【統】分布範囲; 【楽】音域 |
| 99 | `amplekso` | 中国語 | 大小，广度；（哲）外延；（统）分布范围 | 大小，广度；（哲）外延；（统）分布范围；（音）音域 |
| 99 | `amplekso` | 韓国語 | 크기, 넓이; (철학) 외연; (통계) 분포 범위 | 크기, 넓이; (철학) 외연; (통계) 분포 범위; (음악) 음역 |
| 112 | `aparato` | 日本語 | {Ｂ}装置, 機械一式; 【解】器官系; 【政】機関; 【情】装置, デバイス | {Ｂ}装置, 機械一式; 【解】器官系; 【政】機関; 【文献】校勘資料; 【情】装置, デバイス |
| 112 | `aparato` | 中国語 | 一套装置，仪器；（解）器官系统；（政）机关；（信息）装置，设备 | 一套装置，仪器；（解）器官系统；（政）机关；（文献）校勘资料；（信息）装置，设备 |
| 112 | `aparato` | 韓国語 | 장치, 기계; (해부) 기관계; (정치) 기구; (정보) 장치, 디바이스 | 장치, 기계; (해부) 기관계; (정치) 기구; (문헌) 교감 자료; (정보) 장치, 디바이스 |
| 130 | `arko` | 中国語 | 弧，拱形物；弓；[物] 电弧 | 弧，拱形物；弓；[物] 电弧；（解）弓状结构 |
| 132 | `armi` | 日本語 | {Ｂ}［他］武装させる; 装甲する | {Ｂ}［他］武装させる; 装甲・補強する; 《転》強化する |
| 132 | `armi` | 中国語 | 武装，加固 | 武装；披甲；加固，装甲 |
| 132 | `armi` | 韓国語 | 무장시키다; 무기를 갖추게 하다; 장갑을 두르다 | 무장시키다; 무기를 갖추게 하다; 장갑을 입히다, 보강하다; (비유) 강화하다 |
| 133 | `artikolo` | 日本語 | {Ｂ}記事; 条項; 【法】（法令の）条, >>paragrafo; 【Ｇ】冠詞 | {Ｂ}記事; 辞書項目; 条項; 【法】（法令の）条, >>paragrafo; 【Ｇ】冠詞 |
| 133 | `artikolo` | 中国語 | 文章，条目，条款；（法）条文；（语）冠词 | 文章，词典条目，条款；（法）条文；（语）冠词 |
| 133 | `artikolo` | 韓国語 | 기사; 조항, 조문; (문법) 관사 | 기사; 사전 항목; 조항, 조문; (문법) 관사 |
| 134 | `arto` | 中国語 | 技艺；艺术 | 技艺；艺术；人工 |
| 134 | `arto` | 韓国語 | 기술, 예술 | 기술, 예술; 인공 |
| 135 | `arĝento` | 韓国語 | 은(금속) | 은(금속); (쇼기) 은장 |
| 138 | `asocio` | 中国語 | 协会，联合会，社团 | 协会，联合会，社团；联想，结合 |
| 138 | `asocio` | 日本語 | {Ｂ}協会, 結社; 結合, 連合 | {Ｂ}協会, 結社; 結合, 連合; 連想 |
| 138 | `asocio` | 韓国語 | 협회, 결사체; 결합, 연합 | 협회, 결사체; 결합, 연합; 연상 |
| 180 | `banko` | 日本語 | {Ｂ}銀行; 【遊】（賭博で）親元にある賭け金, 場銭（ばせん） | {Ｂ}銀行; （血液・情報などの）バンク; 【遊】（賭博で）親元にある賭け金, 場銭（ばせん） |
| 180 | `banko` | 中国語 | 银行；（赌）庄家的赌金 | 银行；（血液、信息等的）库；（赌）庄家的赌金 |
| 180 | `banko` | 韓国語 | 은행; (도박) 판돈, 자금 | 은행; 혈액·정보 등의 저장소; (도박) 판돈, 자금 |
| 181 | `barakti` | 韓国語 | 몸부림치다, 발버둥치다 | 몸부림치다, 발버둥치다; (비유) 고투하다 |
| 183 | `barelo` | 日本語 | {Ｂ}樽（たる） | {Ｂ}樽（たる）; バレル（容量単位） |
| 183 | `barelo` | 中国語 | 桶，酒桶 | 桶，酒桶；桶（容量单位） |
| 183 | `barelo` | 韓国語 | 통, 술통, 배럴 | 통, 술통; 배럴(용량 단위) |
| 189 | `bazo` | 中国語 | 基础，根基；（化）碱；（数）基数，底边；基地 | 底座，基础，根基；（生）基部；（化）碱；（数）基数，基底，底边；基地 |
| 192 | `beko` | 日本語 | {Ｂ}くちばし | {Ｂ}くちばし; くちばし状の突起・先端 |
| 206 | `bileto` | 日本語 | {Ｂ}切符, 券 | {Ｂ}切符, 券; 紙幣; 簡単な手紙 |
| 206 | `bileto` | 中国語 | 票，券 | 票，券；钞票；便条，短笺 |
| 206 | `bileto` | 韓国語 | 표, 티켓 | 표, 티켓; 지폐; 짧은 편지, 쪽지 |
| 209 | `blanka` | 日本語 | {Ｂ}白い | {Ｂ}白い; 空白の, 白紙の |
| 209 | `blanka` | 韓国語 | 하얀, 흰 | 하얀, 흰; 빈, 공백의 |
| 214 | `blovi` | 中国語 | 风吹，吹 | 风吹，吹气；吹动，吹奏 |
| 227 | `brako` | 日本語 | {Ｂ}腕 | {Ｂ}腕; 腕状の部分 |
| 227 | `brako` | 中国語 | 胳膊 | 胳膊；臂状部分 |
| 227 | `brako` | 韓国語 | 팔 | 팔; 팔처럼 뻗은 부분 |
| 228 | `branĉo` | 中国語 | 枝，分支 | 枝；分支，支线，部门 |
| 236 | `bronzo` | 韓国語 | 청동, 구리합금 | 청동, 구리-주석 합금 |
| 237 | `broso` | 日本語 | {Ｂ}ブラシ | {Ｂ}ブラシ; 【電】ブラシ（電刷） |
| 253 | `butono` | 韓国語 | 단추; (기계·전자기기의) 버튼; 단추 모양의 것; 꽃봉오리; 피부의 작은 돋음 | 단추; (기계·전자기기의) 버튼; 단추 모양의 것; 꽃봉오리; 작은 뾰루지 |
| 254 | `buĝeto` | 韓国語 | 예산 | 예산; 예산안 |
| 255 | `buŝo` | 日本語 | {Ｂ}口; 【解】口腔 | {Ｂ}口; 【解】口腔; 開口部 |
| 255 | `buŝo` | 中国語 | 嘴；口；口腔 | 嘴；口；口腔；开口，口部 |
| 255 | `buŝo` | 韓国語 | 입; (해부) 구강 | 입; (해부) 구강; 입구, 개구부 |
| 270 | `ciklo` | 中国語 | 周期；循环；（文）组诗；（化）环 | 周期；循环；（文）组诗；（化）环；（环境）物质循环；（物）周（频率单位） |
| 282 | `danci` | 中国語 | 跳舞；（他）跳（某种）舞 | 跳舞；雀跃，跳动；（他）跳（某种）舞 |
| 282 | `danci` | 韓国語 | 춤추다; (…을) 추다 | 춤추다; 흥겹게 뛰다, 뛰놀다; (…을) 추다 |
| 290 | `dediĉi` | 中国語 | 献；题献；献身，致力于 | 献；题献；献身，致力于；（宗）奉献 |
| 302 | `densa` | 中国語 | 浓的，浓密的；稠密的，密集的；（植）茂密的 | 浓的，浓密的；稠密的，密集的；（植）茂密的；（摄影）密度高的，不透明的 |
| 302 | `densa` | 韓国語 | 짙은, 농밀한; 빽빽한, 밀도가 높은 | 짙은, 농밀한; 빽빽한, 밀도가 높은; (사진) 농도가 짙은, 불투명한 |
| 315 | `dialogo` | 韓国語 | 대화, 문답 | 대화, 문답; (문학) 대화체 작품 |
| 318 | `difini` | 韓国語 | 정의하다, 뜻을 분명히 하다 | 정의하다, 뜻을 분명히 하다; 정하다 |
| 320 | `dika` | 日本語 | {Ｂ}厚い; 太い; 太った | {Ｂ}厚い; 太い; 太った; 粘性のある |
| 320 | `dika` | 中国語 | 厚，粗，胖 | 厚，粗，胖；粘稠的 |
| 320 | `dika` | 韓国語 | 두꺼운, 굵은, 뚱뚱한 | 두꺼운, 굵은, 뚱뚱한; 점성이 있는, 걸쭉한 |
| 323 | `dimensio` | 中国語 | 大小，尺寸；维数；量纲 | 大小，尺寸；维数；量纲；（转）规模，范围 |
| 333 | `distingi` | 日本語 | {Ｂ}［他］見分ける, 識別する, 判別する | {Ｂ}［他］見分ける, 識別する, 判別する; はっきり認める; 特別に扱う |
| 333 | `distingi` | 中国語 | 区别，辨别；分清；看清 | 区别，辨别；分清；看清；区别对待，优待 |
| 333 | `distingi` | 韓国語 | 구별하다 | 구별하다, 식별하다; 분명히 알아보다; 특별히 대우하다 |
| 339 | `do` | 日本語 | {Ｂ}［接］だから, すると, それでは, そこで, >>sekve, >>〜; ［副］（疑問文を強めて）いったい全体; （命令文を強めて）さあ, ほら / {Ｏ}［文字名］ドー（文字D，dの名称） | {Ｂ}［接］だから, すると, それでは, そこで, >>sekve, >>〜; ［副］（疑問文を強めて）いったい全体; （命令文を強めて）さあ, ほら / {Ｏ}［音名］C音; ［文字名］ドー（文字D，dの名称） |
| 339 | `do` | 中国語 | （接）所以，那么；（副）究竟、到底；（字母名）D 的名称 | （接）所以，那么；（副）究竟、到底；（音名）C音；（字母名）D 的名称 |
| 339 | `do` | 韓国語 | 그래서, 그러면; (부) 도대체; (문자명) D의 이름 | 그래서, 그러면; (부) 도대체; (음악) C음; (문자명) D의 이름 |
| 344 | `dolĉa` | 日本語 | {Ｂ}甘い; 心地好い; やさしい | {Ｂ}甘い; 心地好い; やさしい; （水が）淡水の, 塩気のない |
| 344 | `dolĉa` | 中国語 | 甜，甜美；温柔 | 甜，甜美；温柔；（水）淡的，非咸的 |
| 344 | `dolĉa` | 韓国語 | 달콤한; 기분 좋은; 상냥한 | 달콤한; 기분 좋은; 상냥한; (물) 민물의, 짜지 않은 |
| 383 | `ekzameni` | 中国語 | 考核，检查，审查，考试 | 检查，审查，考核，考试；讯问 |
| 398 | `enigmo` | 韓国語 | 수수께끼 | 수수께끼; (비유) 난해한 것, 불가사의한 것 |
| 405 | `esenco` | 中国語 | 本质，核心；（化）香精，精油 | 本质，核心；（化）香精，精油；（哲）实在，本体 |
| 421 | `eĥo` | 中国語 | 回声，反响；回波 | 回声，反响；回波；（转）言论、意见的重复、附和 |
| 427 | `fajfi` | 中国語 | 吹口哨，吹哨 | 吹口哨；鸣哨，鸣笛；（鸟）啭鸣 |
| 455 | `ferio` | 中国語 | 假日，休息日；停业日 | 假日，休息日；假期；停业日 |
| 455 | `ferio` | 韓国語 | 휴일, 쉬는 날; 휴업일 | 휴일, 쉬는 날; 휴가, 방학; 휴업일 |
| 459 | `festeni` | 中国語 | 欢宴，赴宴 | 欢宴，赴宴；设宴 |
| 473 | `firma` | 中国語 | 坚实，牢固；坚决 | 坚实，牢固；坚定，稳定 |
| 476 | `flago` | 日本語 | {Ｂ}旗, >>〜 | {Ｂ}旗, >>〜; 【情】フラグ（状態標識） |
| 476 | `flago` | 中国語 | 旗帜 | 旗帜；（计）标志位，标志 |
| 476 | `flago` | 韓国語 | 깃발, 기 | 깃발, 기; (컴퓨터) 플래그, 상태 표시 |
| 483 | `fliki` | 中国語 | 缝补，修补；弥补 | 缝补，修补；弥补；（计算机）打补丁 |
| 488 | `flui` | 中国語 | 流，流动 | 流，流动；（转）顺畅地进行 |
| 493 | `fondi` | 中国語 | 建立；创建，创办 | 建立；创建，创办；以…为根据 |
| 493 | `fondi` | 韓国語 | 조직 등을 창설하다 | 조직 등을 창설하다; 근거를 두다 |
| 497 | `forko` | 日本語 | {Ｂ}フォーク状の道具; 【料】フォーク, =manĝo〜 | {Ｂ}フォーク状の道具; 【料】フォーク, =manĝo〜; 分岐点 |
| 497 | `forko` | 中国語 | 叉子，叉形物 | 叉子，叉形物；岔口，分叉处 |
| 497 | `forko` | 韓国語 | 갈래진 도구; 식탁용 포크 | 갈래진 도구; 식탁용 포크; 갈림길, 분기점 |
| 520 | `fronto` | 中国語 | 前线；阵线；前面，正面 | 前线；阵线；前面，正面；（气象）锋面 |
| 531 | `funkcio` | 日本語 | {Ｂ}職務, 役目; 機能, 作用; 【数】関数; 【情】関数 | {Ｂ}職務, 役目; 機能, 作用; 【数・情】関数; 【化】官能, 官能基 |
| 531 | `funkcio` | 中国語 | 职能，职务；作用，功能；函数 | 职能，职务；作用，功能；函数；（化）官能，官能团 |
| 531 | `funkcio` | 韓国語 | 직무, 기능, 역할; (수학·정보) 함수 | 직무, 기능, 역할; (수학·정보) 함수; (화학) 작용기 |
| 534 | `fuŝi` | 韓国語 | 망치다 | 서투르게 처리하다, 망치다 |
| 537 | `ganto` | 中国語 | （分指的）手套 | （分指的）手套；（运动）手套、球类手套 |
| 546 | `gento` | 中国語 | 种族，氏族，部族 | 种族，氏族，部族；民族 |
| 571 | `greno` | 日本語 | {Ｂ}穀物 | {Ｂ}穀物; 穀粒 |
| 580 | `guto` | 韓国語 | 물방울, 한 방울 | 물방울, 한 방울; (비유) 아주 적은 양 |
| 625 | `ial` | 韓国語 | 어떤 이유로, 그 때문에 | 어떤 이유로, 왠지 |
| 627 | `idealo` | 日本語 | {Ｂ}理想 | {Ｂ}理想; 【数】イデアル |
| 627 | `idealo` | 中国語 | 理想，崇高目标 | 理想，崇高目标；（数）理想 |
| 627 | `idealo` | 韓国語 | 이상, 이상향 | 이상, 이상향; (수학) 아이디얼 |
| 682 | `inviti` | 中国語 | 邀请 | 邀请；请…做；（转）吸引，诱人 |
| 689 | `izoli` | 中国語 | 隔离，使孤立；使绝缘；隔绝 | 隔离，使孤立；使绝缘；（化）分离，单离 |
| 712 | `kafo` | 中国語 | 咖啡 | 咖啡；咖啡豆 |
| 714 | `kajero` | 中国語 | 笔记本，练习本 | 笔记本，练习本；（书籍的）分册 |
| 716 | `kaldrono` | 中国語 | 大锅；（地理）火山口凹地（カルデ拉） | 大锅；（地理）破火山口，火山口凹地 |
| 725 | `kampo` | 中国語 | 田地，场地；领域，范围；（理）场 | 田地，场地；领域，范围；（理）场；（信息）字段 |
| 726 | `kanalo` | 中国語 | 运河，沟渠，水道；海峡；（通信）频道；（解）管道 | 运河，沟渠，水道；海峡；（通信）频道；（解）管道；（转）渠道，途径 |
| 733 | `kapo` | 日本語 | {Ｂ}頭, 首, 頭部; 頭脳; 一人, 一頭; 《転》頂上部, 先端, 先頭; 指導者 | {Ｂ}頭, 頭部; 頭脳; 一人, 一頭; 《転》頂上部, 先端, 先頭; 指導者 |
| 737 | `karaktero` | 中国語 | 性格，个性；性质，特征；风格 | 性格，个性；性质，特征；风格；（生）性状，形质 |
| 765 | `kerno` | 日本語 | {Ｂ}核, 種（たね）, 芯（しん）; 《転》核心; 【理】核, =〜 | {Ｂ}核, 種（たね）, 芯（しん）; 《転》核心; 【理】核, =〜; 【数】核 |
| 765 | `kerno` | 中国語 | 仁，核，芯；中心，核心；（理）原子核 | 仁，核，芯；中心，核心；（理）原子核；（数）核 |
| 765 | `kerno` | 韓国語 | 핵, 씨, 심; 핵심; (물리) 원자핵 | 핵, 씨, 심; 핵심; (물리) 원자핵; (수학) 핵 |
| 776 | `kirurgio` | 日本語 | {Ｂ}【医】外科学, 外科 | {Ｂ}【医】外科学, 外科; 外科手術 |
| 783 | `kliento` | 中国語 | 顾客，委托人，患者 | 顾客，委托人，患者；（史）古罗马被保护平民 |
| 783 | `kliento` | 韓国語 | 고객, 의뢰인, 환자 | 고객, 의뢰인, 환자; (역사) 고대 로마의 피보호 평민 |
| 798 | `kolono` | 中国語 | 圆柱，支柱；（排版）栏；（军）纵队 | 圆柱，支柱；纪念柱；柱状物；（转）支柱人物；（排版）栏；（军）纵队 |
| 814 | `kompari` | 中国語 | 比较，对比 | 比较，对比；比作，比拟 |
| 822 | `komuniki` | 中国語 | 传达，通知 | 传达，通知；传递，传播 |
| 841 | `konkurso` | 中国語 | 竞赛，比赛 | 竞赛，比赛；选拔考试 |
| 854 | `konstrui` | 中国語 | 建筑；构成 | 建造，建筑；组装，构成 |
| 861 | `konvena` | 中国語 | 适当，适合 | 适当，适合；合乎礼仪，得体 |
| 875 | `kosti` | 韓国語 | 값이 나가다, 비용이 들다; (비유) 대가를 치르게 하다 | 값이 나가다, 비용이 들다; (비유) 대가가 들다 |
| 901 | `krokodilo` | 中国語 | 鳄属动物；[~i]在讲世界语的环境中说民族语 | 鳄鱼（鳄属动物）；[~i]在讲世界语的环境中说民族语 |
| 903 | `krono` | 韓国語 | 왕관, 화관; 왕권, 왕위; (화폐) 크로네 | 왕관, 화관, 영예의 관; 왕권, 왕위; 관 모양의 것; (화폐) 크로네 |
| 908 | `kruro` | 中国語 | 腿，脚；（解）小腿（膝至踝） | 腿，脚；（解）小腿（膝至踝）；（转）支脚，腿状部位 |
| 955 | `lama` | 日本語 | {Ｂ}足（脚）の不自由な, びっこの; 《転》釣り合いの取れていない | {Ｂ}足（脚）の不自由な, 足を引きずる; 《転》釣り合いの取れていない |
| 959 | `lano` | 中国語 | 羊毛；（织）毛线，毛织物 | 羊毛；（织）毛线，毛织物；羊毛状物 |
| 960 | `lardo` | 韓国語 | 돼지 비계, 라드 | 돼지 비계, 라드; (옛말) 베이컨 |
| 971 | `legi` | 中国語 | 读；朗读；读懂，解读 | 读；朗读；读懂，解读；（信息）读取 |
| 987 | `ligi` | 中国語 | 绑，连，联 | 绑，系，连接；束缚；关联，联合 |
| 1007 | `ludi` | 中国語 | 玩，游戏；演奏；扮演（角色） | 嬉戏，自由活动；玩，游戏；演奏；扮演（角色） |
| 1010 | `lukti` | 中国語 | 搏斗，角斗；奋斗 | 搏斗，摔跤；奋斗 |
| 1020 | `maksimumo` | 中国語 | 最大限度，最大量，最高程度；（数）最大值 | 最大限度，最大量，最高程度；（数）最大值、极大值 |
| 1027 | `maniero` | 日本語 | {Ｂ}やり方, 仕方, 様式, 流儀 | {Ｂ}やり方, 仕方, 様式, 流儀; 礼儀作法, 風習 |
| 1033 | `manĝi` | 中国語 | 吃；（虫）蛀食；（转）腐蚀，侵蚀 | 吃；以…为食；（虫）蛀食；（转）腐蚀，侵蚀；贪婪地吞食 |
| 1042 | `maso` | 中国語 | 团块，集合体，总体；（物理）质量 | 团块，集合体，总体；（美术）块面；（物理）质量 |
| 1046 | `mateno` | 中国語 | 早晨 | 早晨，上午 |
| 1046 | `mateno` | 韓国語 | 아침 | 아침, 오전 |
| 1083 | `miksi` | 韓国語 | 섞다, 혼합하다 | 섞다, 혼합하다; (비유) 혼동하다 |
| 1099 | `mistero` | 中国語 | 神秘，不可思议；奥秘；谜，秘密 | 神秘，不可思议；谜，秘密；（宗）秘仪，奥义；（基督教）玄义 |
| 1099 | `mistero` | 韓国語 | 신비, 불가사의; 수수께끼, 비밀; (기독교) 신비 교의 | 신비, 불가사의; 수수께끼, 비밀; (종교) 비의, 신비 의식; (기독교) 신비 교의 |
| 1108 | `mola` | 韓国語 | 부드럽고 무른; 온화한; 유약한 | 부드럽고 무른; 온화한; 유약한; (음성) 구개음화된 |
| 1111 | `mondo` | 中国語 | 世界；宇宙，万物；世间，社会；（转）界，领域 | 世界；宇宙，万物；世间，社会；世人；（转）界，领域 |
| 1115 | `montri` | 中国語 | 显示，展示；指出；表明 | 显示，展示；指出；表明；说明，使明白 |
| 1117 | `moralo` | 韓国語 | 도덕, 윤리 | 도덕, 윤리; 도덕론 |
| 1118 | `mordi` | 日本語 | {Ｂ}［他］かむ, かみつく, かじる; 削り取る, 腐食する | {Ｂ}［他］かむ, かみつく, かじる; 削り取る, 腐食する; （錨・歯車などが）食い込む, かみ合う |
| 1118 | `mordi` | 中国語 | 咬，咬住，啃；腐蚀，侵蚀 | 咬，咬住，啃；腐蚀，侵蚀；（锚、齿轮等）咬住，啮合 |
| 1118 | `mordi` | 韓国語 | 이로 물다, 깨물다; (비유) 부식하다, 잠식하다 | 이로 물다, 깨물다; (비유) 부식하다, 잠식하다; (닻·톱니바퀴 등이) 걸리다, 맞물리다 |
| 1121 | `morti` | 中国語 | 死亡；（植物）枯死；（转）消失，灭绝 | 死亡；（植物）枯死；（肢体）麻木，失去知觉；（转）消失，灭绝 |
| 1121 | `morti` | 韓国語 | 죽다; (식물 등이) 시들어 죽다; (비유) 사라지다, 멸하다 | 죽다; (식물 등이) 시들어 죽다; (신체 부위가) 감각이 없어지다; (비유) 사라지다, 멸하다 |
| 1123 | `motoro` | 中国語 | 发动机，马达，引擎；原动力 | 发动机，马达，引擎；原动力，推动者 |
| 1125 | `mueli` | 中国語 | 磨，碾 | 磨，碾；粉碎，压榨 |
| 1128 | `murmuri` | 韓国語 | 작게 중얼거리거나 투덜대다 | 낮고 작은 소리를 내다; 중얼거리다, 투덜거리다 |
| 1135 | `muziko` | 中国語 | 音乐 | 音乐；乐曲 |
| 1136 | `muŝo` | 日本語 | {Ｂ}【虫】ハエ（蝿）; （下唇の下の）ちょびひげ | {Ｂ}【虫】ハエ（蝿）; （下唇の下の）ちょびひげ; （昔の）つけぼくろ |
| 1136 | `muŝo` | 中国語 | 苍蝇，蝇类；（转）唇下小胡子 | 苍蝇，蝇类；唇下小胡子；（旧）贴在脸上的黑色美人痣 |
| 1136 | `muŝo` | 韓国語 | 파리; 턱 아래의 작은 수염 | 파리; 턱 아래의 작은 수염; (옛날) 얼굴에 붙이던 검은 장식점 |
| 1138 | `nadlo` | 中国語 | 针；指针；磁针；击针；唱针；注射针 | 针；指针；磁针；击针；唱针；注射针；尖峰状岩峰 |
| 1138 | `nadlo` | 韓国語 | 바늘; (계기) 지침·자침; (총기) 격침; (주사·축음기 등) 바늘 | 바늘; (계기) 지침·자침; (총기) 격침; (주사·축음기 등) 바늘; 뾰족한 암봉 |
| 1140 | `najbaro` | 中国語 | 邻居 | 邻居；近旁的人 |
| 1143 | `naturo` | 韓国語 | 자연, 자연계, 본성 | 자연, 자연계; 본성, 성질 |
| 1147 | `naŭzi` | 韓国語 | 구역질 나게 하다, 싫증나게 하다 | 구역질 나게 하다; 혐오감이나 진저리를 일으키다 |
| 1164 | `nesto` | 日本語 | {Ｂ}巣; 《転》すみか, ねぐら | {Ｂ}巣; 《転》すみか, ねぐら, 巣窟 |
| 1164 | `nesto` | 韓国語 | 새 둥지, 보금자리 | 둥지; (비유) 보금자리, 소굴 |
| 1172 | `nodo` | 中国語 | 结，结点，交点；要点；（动植物）节、瘤；（物理/光学）波节、节点；（航海）节；（计）节点 | 结，结点，交点；要点；（动植物）节、瘤；（解）结节；（物理/光学）波节、节点；（航海）节；（计）节点 |
| 1175 | `nomo` | 日本語 | {Ｂ}名前; 名称 | {Ｂ}名前; 名称; 名声 |
| 1175 | `nomo` | 中国語 | 名字，名称 | 名字，名称；名声 |
| 1175 | `nomo` | 韓国語 | 이름, 명칭 | 이름, 명칭; 명성 |
| 1188 | `nutri` | 中国語 | 喂养，哺育；赡养，抚养 | 喂养，哺育；赡养，抚养；供给养料；（转）滋养，滋长 |
| 1190 | `objekto` | 日本語 | {Ｂ}物体, もの, 品物, >>aĵo; 対象, 主題, 題材; 【Ｇ】目的語; 【哲】客体, 対象 | {Ｂ}物体, もの, 品物, >>aĵo; 対象, 主題, 題材; 科目; 【Ｇ】目的語; 【哲】客体, 対象 |
| 1190 | `objekto` | 中国語 | 物体；对象，主题，题材；【语法】宾语；【哲】客体 | 物体；对象，主题，题材；科目；【语法】宾语；【哲】客体 |
| 1190 | `objekto` | 韓国語 | 물체, 사물; 대상, 주제, 제재; (문법) 목적어; (철학) 객체 | 물체, 사물; 대상, 주제, 제재; 과목; (문법) 목적어; (철학) 객체 |
| 1195 | `oceano` | 日本語 | {Ｂ}【地理】大洋, 大海, 海洋 | {Ｂ}【地理】大洋, 大海, 海洋; 《転》広大なもの |
| 1199 | `oferti` | 韓国語 | 제공하다, 조건을 제시하다 | 제공하다, 조건을 제시하다, 견적을 내다 |
| 1206 | `okulo` | 日本語 | {Ｂ}【解】目; 目つき, まなざし, 視線 | {Ｂ}【解】目; 目つき, まなざし, 視線; 【農】芽, 芽眼 |
| 1206 | `okulo` | 中国語 | 眼睛；目光，眼神，视线 | 眼睛；目光，眼神，视线；（农）芽眼 |
| 1206 | `okulo` | 韓国語 | 눈, 안구; 눈빛, 시선 | 눈, 안구; 눈빛, 시선; (농업) 눈, 싹눈 |
| 1212 | `ondo` | 中国語 | 波，波浪；波状起伏；（物）波 | 波，波浪；波状起伏；（转）浪潮，波动；（物）波 |
| 1212 | `ondo` | 韓国語 | 물결, 파도; 물결 모양의 것; (물리) 파동 | 물결, 파도; 물결 모양의 것; (비유) 일시적 고조, 흐름; (물리) 파동 |
| 1223 | `organo` | 日本語 | {Ｂ}【解】器官, 臓器; 【機】装置; 機関紙, 機関誌; （国家・政党などの）機関, 機構 | {Ｂ}【解】器官, 臓器; 【機】装置; 機関紙, 機関誌; （国家・政党などの）機関, 機構; 声, 声量 |
| 1223 | `organo` | 中国語 | 器官，脏器；装置；机构；机关报（刊） | 器官，脏器；装置；机构；机关报（刊）；嗓音，声量 |
| 1223 | `organo` | 韓国語 | 기관, 장기; 장치; 기관지; (국가·정당 등의) 기관, 기구 | 기관, 장기; 장치; 기관지; (국가·정당 등의) 기관, 기구; 목소리, 성량 |
| 1224 | `oriento` | 日本語 | {Ｂ}東, 東方, 東部, ><〜; （フリーメーソンの）地方支部 | {Ｂ}東, 東方, 東部, ><〜; （フリーメーソンのロッジで長が座る）東側席 |
| 1224 | `oriento` | 中国語 | 东，东方 | 东，东方，东部；（共济会会所中会长所在的）东侧席 |
| 1224 | `oriento` | 韓国語 | 동쪽, 동방, 동부; (프리메이슨) 지방 지부 | 동쪽, 동방, 동부; (프리메이슨 롯지에서 의장이 앉는) 동쪽 자리 |
| 1232 | `osto` | 中国語 | 骨，骨头；遗骨 | 骨，骨头；遗骨；（食）带肉骨头 |
| 1239 | `pala` | 中国語 | 苍白，灰白，暗淡；乏味 | 苍白，灰白，暗淡；缺乏生气，苍白无力 |
| 1239 | `pala` | 韓国語 | 창백한; (색·빛이) 엷은, 희미한 | 창백한; (색·빛이) 엷은, 희미한; (비유) 생기 없고 힘없는 |
| 1249 | `papero` | 日本語 | {Ｂ}紙, 用紙 | {Ｂ}紙, 用紙; 書類, 文書 |
| 1249 | `papero` | 中国語 | 纸，纸张，用纸 | 纸，纸张，用纸；文件，文书 |
| 1249 | `papero` | 韓国語 | 종이, 용지 | 종이, 용지; 서류, 문서 |
| 1280 | `pendi` | 中国語 | 挂，垂 | 悬挂，下垂；悬空 |
| 1295 | `permesi` | 中国語 | 允许，准许 | 允许，准许；（情况）容许，使可能 |
| 1296 | `persekuti` | 韓国語 | 집요하게 괴롭히다, 박해하다; (법) 기소하다 | 추적하다, 뒤쫓다; 집요하게 괴롭히다, 박해하다; (법) 기소하다 |
| 1299 | `persono` | 日本語 | {Ｂ}人（個人）, 人物; 【劇】登場人物; 【Ｇ】人称 | {Ｂ}人（個人）, 人物; 【法】人（自然人・法人）; 【劇】登場人物; 【Ｇ】人称 |
| 1299 | `persono` | 中国語 | 人，个人；（剧）人物；（语）人称 | 人，个人；（法）人（自然人、法人）；（剧）人物；（语）人称 |
| 1299 | `persono` | 韓国語 | 사람, 개인; (연극) 등장인물; (문법) 인칭 | 사람, 개인; (법) 사람·법인; (연극) 등장인물; (문법) 인칭 |
| 1302 | `petoli` | 中国語 | 嬉闹，顽皮玩耍；打闹，胡闹 | 嬉闹，顽皮玩耍；打闹，胡闹；调情，亲昵嬉戏 |
| 1302 | `petoli` | 韓国語 | 까불며 장난치다, 즐겁게 떠들며 놀다 | 까불며 장난치다, 즐겁게 떠들며 놀다; 이성과 시시덕거리다 |
| 1303 | `petrolo` | 中国語 | 石油 | 石油及其制品（原油、煤油等） |
| 1304 | `peza` | 日本語 | {Ｂ}重い; 重さがある; 《転》重苦しい; 重々しい | {Ｂ}重い; 重さがある; （食物が）胃にもたれる; 《転》重苦しい; 重々しい |
| 1304 | `peza` | 中国語 | 重的；沉重的；（转）压抑的，庄重的 | 重的；沉重的；（食物）难消化的；（转）压抑的，庄重的 |
| 1304 | `peza` | 韓国語 | 무거운; (비유) 무겁고 답답한; 중후한, 묵직한 | 무거운; (음식이) 소화가 잘 안 되는; (비유) 무겁고 답답한; 중후한, 묵직한 |
| 1309 | `pilko` | 中国語 | 球 | 球；（滴管等的）橡胶球囊 |
| 1309 | `pilko` | 韓国語 | 공, 둥근 공 모양 물건 | 공; (스포이트 등의) 고무 벌브 |
| 1320 | `plado` | 日本語 | {Ｂ}大皿, 皿, >>〜; （皿に盛った）料理 | {Ｂ}大皿, 皿, >>〜; （皿に盛った）料理; 【微】ペトリ皿 |
| 1320 | `plado` | 中国語 | 盘子，大盘；一盘菜（一道菜） | 盘子，大盘；一盘菜（一道菜）；（微生物）培养皿 |
| 1320 | `plado` | 韓国語 | 큰 접시, 접시; (접시에 담긴) 요리 | 큰 접시, 접시; (접시에 담긴) 요리; (미생물) 페트리 접시 |
| 1325 | `planti` | 中国語 | 栽种，种植 | 栽种，种植；竖立，插立 |
| 1327 | `plata` | 中国語 | 扁；平，平坦 | 扁；平，平坦；（转）平板，单调 |
| 1337 | `plugi` | 中国語 | 犁地，耕地 | 犁地，耕地；开出沟痕 |
| 1377 | `premio` | 日本語 | {Ｂ}賞, 賞品; 景品 | {Ｂ}賞, 賞品, 賞金; 景品 |
| 1392 | `princo` | 中国語 | 君主，诸侯；王子，亲王，王侯 | 君主，诸侯；王子，亲王，王侯；（转）首屈一指的人物 |
| 1400 | `proceso` | 日本語 | {Ｂ}【法】訴訟 | {Ｂ}【法】訴訟; 過程, プロセス |
| 1400 | `proceso` | 中国語 | 诉讼 | 诉讼；过程，进程 |
| 1400 | `proceso` | 韓国語 | 소송, 재판 | 소송, 재판; 과정, 프로세스 |
| 1405 | `programo` | 中国語 | 节目单，程序表；日程，议程；纲要，计划；程序 | 节目单，程序表；日程，议程；纲要，计划；（计算机）程序 |
| 1407 | `projekto` | 中国語 | 打算，设想，计划；方案，草案 | 打算，设想，计划；方案，草案；（工程）设计资料、设计图 |
| 1409 | `proksima` | 日本語 | {Ｂ}（空間的・時間的に）近い, 近接した | {Ｂ}（空間的・時間的に）近い, 近接した; （関係・意味などが）近い |
| 1409 | `proksima` | 中国語 | 近的，邻近的，接近的（空间/时间） | 近的，邻近的，接近的（空间/时间）；（关系、意义等）接近的 |
| 1409 | `proksima` | 韓国語 | 가까운, 근접한; (시간적으로) 가까운 | 가까운, 근접한; (시간적으로) 가까운; (관계·의미상) 가까운 |
| 1417 | `protekti` | 中国語 | 保护，庇护 | 保护，庇护；扶持，支持 |
| 1435 | `pura` | 韓国語 | 순수한, 깨끗한; (도덕적으로) 순결한 | 순수한, 깨끗한; (도덕적으로) 순결한; (종교) 정결한 |
| 1440 | `rabi` | 韓国語 | 폭력이나 협박으로 남의 것을 빼앗다 | 폭력이나 협박으로 남의 것을 빼앗다; (비유) 소중한 것을 빼앗다 |
| 1441 | `radiko` | 中国語 | 根；词根；方根 | 根，根本；词根；（数）根、方根 |
| 1442 | `radio` | 中国語 | 光线，射线，放射线；（数）半径；（机）辐条；（通）无线电广播，广播电台；收音机 | 光线，射线，放射线；放射状物；（数）半径；（机）辐条；（转）光明，光辉；（通）无线电广播，广播电台；收音机 |
| 1443 | `rado` | 中国語 | 轮子，车轮；齿轮 | 轮子，车轮；齿轮；轮状物 |
| 1446 | `rajto` | 韓国語 | 권리 | 권리, 권한, 권익 |
| 1448 | `rampi` | 中国語 | 爬，蠕动，爬行，匍匐而行 | 爬，蠕动，爬行，匍匐而行；缓慢前进；（转）卑躬屈膝 |
| 1448 | `rampi` | 韓国語 | 기어가다, 포복하다 | 기어가다, 포복하다; 느릿느릿 나아가다; (비유) 비굴하게 굽실거리다 |
| 1458 | `reala` | 日本語 | {Ｂ}現実の, 実在の; 本当の, 本物の | {Ｂ}現実の, 実在の; 本当の, 本物の; 【数】実数の |
| 1458 | `reala` | 中国語 | 真实，真，真正；现实，实际 | 真实，真，真正；现实，实际；（数）实数的 |
| 1458 | `reala` | 韓国語 | 현실의, 실제의, 진짜의 | 현실의, 실제의, 진짜의; (수학) 실수의 |
| 1463 | `redukti` | 中国語 | 减少，减小，缩小，降低；使陷入（某状态）；（化）还原；（医）复位 | 减少，减小，缩小，降低；使陷入（某状态）；（摄影）减薄；（化）还原；（医）复位 |
| 1476 | `renkonti` | 中国語 | 遇见，碰到；遭遇；（问题等）面对 | 遇见，碰到；遭遇；（反应）对待，应对；（问题等）面对 |
| 1487 | `revizii` | 中国語 | 复查，重新审查；修订，校订；（法）再审 | 复查，重新审查；修订，校订；（法）再审；（机械）检修 |
| 1499 | `rigardi` | 中国語 | 看，注视；看待，认为；面向 | 看，注视；察看，留意；看待，认为；面向 |
| 1504 | `rimedo` | 日本語 | {Ｂ}手段, 方法, 方策; （救済・回復のための）対策, 措置 | {Ｂ}手段, 方法, 方策; （救済・回復のための）対策, 措置; 資力, 財源 |
| 1504 | `rimedo` | 中国語 | 手段，方法；对策，补救办法 | 手段，方法；对策，补救办法；财力，资金 |
| 1504 | `rimedo` | 韓国語 | 수단, 방법, 대책 | 수단, 방법, 대책; 재력, 자금 |
| 1507 | `ringo` | 中国語 | 环，圈；戒指 | 环，圈；戒指；环状物 |
| 1510 | `ripo` | 中国語 | 肋骨；【植】叶脉；【机】肋板，加强筋 | 肋骨；【植】叶脉；（纺）罗纹；【机】肋板，加强筋；（海）肋材 |
| 1515 | `rivero` | 中国語 | 河 | 河流；（转）洪流，奔流 |
| 1515 | `rivero` | 韓国語 | 강, 하천 | 강, 하천; (비유) 흐름, 물결 |
| 1519 | `roko` | 日本語 | {Ｂ}岩, 岩石; 岩山, 岩礁 | {Ｂ}岩, 岩石; 岩山, 岩礁; 【音】ロック音楽 |
| 1519 | `roko` | 中国語 | 岩石；岩体，岩山；岩礁 | 岩石；岩体，岩山；岩礁；（音）摇滚乐 |
| 1519 | `roko` | 韓国語 | 바위, 암석 | 바위, 암석; (음악) 록 음악 |
| 1520 | `rolo` | 韓国語 | 역할, 임무 | 배역, 역할; 임무 |
| 1524 | `ronki` | 中国語 | 打鼾，发呼噜声 | 打鼾，发呼噜声；发出类似鼾声的低沉声 |
| 1524 | `ronki` | 韓国語 | 코를 곤다; 큰 코고는 소리가 나다 | 코를 골다; 코고는 듯한 낮은 소리를 내다 |
| 1525 | `rosti` | 中国語 | 烤，烘烤；烘焙，焙烧；（转）受强热 | 烤，烘烤；烘焙，焙烧；（转）使…受强热 |
| 1526 | `rozo` | 中国語 | 蔷薇，玫瑰；（建）玫瑰窗；（罗盘）方位盘 | 蔷薇，玫瑰；玫瑰形物；（建）玫瑰窗；（罗盘）方位盘；喷壶喷头 |
| 1536 | `sako` | 中国語 | 袋，口袋；袋包 | 袋子，口袋；包，提包 |
| 1536 | `sako` | 韓国語 | 주머니, 가방 | 자루, 포대; 주머니, 가방 |
| 1543 | `saluti` | 中国語 | 问候，致意，打招呼；敬礼 | 问候，致意，打招呼；敬礼；欢迎，公开致敬 |
| 1543 | `saluti` | 韓国語 | 상대에게 인사하거나 예의를 표하다 | 상대에게 인사하거나 예의를 표하다; 환영하다, 공개적으로 경의를 표하다 |
| 1548 | `sankta` | 中国語 | 圣的，神圣 | 圣的，神圣；（转）应受尊重的，不可侵犯的 |
| 1551 | `savi` | 中国語 | 救，挽救；保护，保全 | 救，挽救；保护，保全；（宗）拯救 |
| 1551 | `savi` | 韓国語 | 위험에서 구해내다, 목숨을 구하다; 파괴에서 지켜 보전하다 | 위험에서 구해내다, 목숨을 구하다; 파괴에서 지켜 보전하다; (종교) 구원하다 |
| 1564 | `sekso` | 中国語 | 性，性别；男女（总称）；性相关事物 | 性，性别；男女（总称）；性相关事物；（古）语法性 |
| 1564 | `sekso` | 韓国語 | 성, 성별; 남성, 여성(총칭); 성에 관한 일 | 성, 성별; 남성, 여성(총칭); 성에 관한 일; (고어) 문법적 성 |
| 1578 | `serio` | 中国語 | 系列；（理）串联；（数）级数 | 系列；（化）系列；（理）串联；（数）级数；（地质）统 |
| 1580 | `serpento` | 韓国語 | 뱀; (비유) 음흉한 사람 | 뱀; (비유) 음흉한 사람; (음악) 세르팡(옛 목관악기) |
| 1589 | `sidi` | 中国語 | 坐着；位于；坐落；（衣服）合身 | 坐着；停留不动；处于某种状态；位于，坐落；（衣服）合身 |
| 1591 | `signifi` | 韓国語 | 의미하다, 나타내다; 징후가 되다; 의미가 있다 | 의미하다, 나타내다; …와 동등하다; 징후가 되다; 의미가 있다 |
| 1592 | `signo` | 中国語 | 标记，记号；征兆；信号，手势；符号 | 标记，记号；征兆；信号，手势；符号；（信息）字符 |
| 1595 | `simila` | 中国語 | 相似的，类似的 | 相似的，类似的；（数）相似的 |
| 1595 | `simila` | 韓国語 | 서로 닮은, 비슷한 | 서로 닮은, 비슷한; (수학) 닮음인 |
| 1609 | `skribi` | 中国語 | 写，书写；记述；（信）写信 | 写，书写；记述；（信）写信；（信息）写入 |
| 1641 | `spiri` | 中国語 | 呼吸；（转）散发，表现 | 呼吸；喘口气，稍作休息；（转）散发，表现 |
| 1647 | `stadio` | 韓国語 | 발전 과정의 한 단계, 시기 | 발전 과정의 한 단계, 시기; (고대 그리스) 스타디온(약 180m) |
| 1649 | `standardo` | 韓国語 | 국가·군대를 상징하는 깃발, 국기, 군기 | 국가·군대를 상징하는 깃발, 국기, 군기; (비유) 기치, 표지 |
| 1656 | `stelo` | 日本語 | {Ｂ}【天】星; 星印, 星形; 【Ｅ】ステーロ（仮想の通貨単位） | {Ｂ}【天】星; 星印, 星形; スター, 花形俳優; 【Ｅ】ステーロ（仮想の通貨単位） |
| 1656 | `stelo` | 中国語 | 星；星号，星形；【E】一种虚拟货币单位 | 星；星号，星形；明星，明星演员；【E】一种虚拟货币单位 |
| 1656 | `stelo` | 韓国語 | 별, 별표, 별 모양; 에스페란토의 가상 화폐 단위 | 별, 별표, 별 모양; 스타, 인기 배우; 에스페란토의 가상 화폐 단위 |
| 1658 | `stilo` | 日本語 | {Ｂ}文体; 【建】【服】様式; 流儀, スタイル | {Ｂ}文体; 【建】【服】様式; 流儀, スタイル; 暦法 |
| 1658 | `stilo` | 中国語 | 文体；样式，风格；流派，格调 | 文体；样式，风格；流派，格调；历法 |
| 1658 | `stilo` | 韓国語 | 문체; 양식, 스타일 | 문체; 양식, 스타일; 역법 |
| 1659 | `stomako` | 韓国語 | 위, 위장 | 위, 위장; (비유) 배, 식욕 |
| 1670 | `subjekto` | 日本語 | {Ｂ}主題, 題目, 論題; 【Ｇ】主語; 【哲】主体 | {Ｂ}【Ｇ】主語; 【哲】主体; 【医・心】被験者, 対象者 |
| 1670 | `subjekto` | 中国語 | 主题，论题；（语）主语；（哲）主体 | （语）主语；（哲）主体；（医/心）受试者，对象 |
| 1670 | `subjekto` | 韓国語 | 주제, 논제; (문법) 주어; (철학) 주체 | (문법) 주어; (철학) 주체; (의학·심리) 피험자, 대상자 |
| 1680 | `sulko` | 日本語 | {Ｂ}【農】うねま（畝間）; 溝; わだち（轍）; （波の）うね | {Ｂ}【農】うねま（畝間）; 溝; わだち（轍）; しわ, ひだ; 【解】溝; （波の）うね |
| 1680 | `sulko` | 中国語 | 犁沟，垄沟；沟槽，车辙；（波）波状起伏 | 犁沟，垄沟；沟槽，车辙；皱纹，褶皱；（解）沟；（波）波状起伏 |
| 1680 | `sulko` | 韓国語 | 밭고랑; 홈, 도랑; 바큇자국; 물결의 이랑 | 밭고랑; 홈, 도랑; 바큇자국; 주름, 깊은 고랑; (해부) 고랑; 물결의 이랑 |
| 1688 | `surfaco` | 中国語 | 面，表面 | 面，表面；（数）曲面，面 |
| 1694 | `svingi` | 中国語 | 挥动，挥舞，甩动，抡 | 挥动，挥舞，甩动，抡；（转）推动，激励 |
| 1695 | `tabako` | 韓国語 | 담배, 담배잎이나 그 가공품 | 담배, 담뱃잎이나 그 가공품; (식물) 담배속 식물 |
| 1696 | `tabelo` | 日本語 | {Ｂ}表, 一覧表, 目録, 数表; 【史】=tabuleto（書字板） | {Ｂ}表, 一覧表, 目録, 数表; 【史】=tabuleto（書字板）; 【情】配列 |
| 1696 | `tabelo` | 中国語 | 表，一览表，数表；图表；（史）书写板、泥板、蜡板 | 表，一览表，数表；图表；（史）书写板、泥板、蜡板；（计）数组 |
| 1696 | `tabelo` | 韓国語 | 표, 일람표, 목록, 수표(數表); (역사) 서판 | 표, 일람표, 목록, 수표(數表); (역사) 서판; (컴퓨터) 배열 |
| 1709 | `taso` | 日本語 | {Ｂ}茶碗, カップ, 湯のみ | {Ｂ}茶碗, カップ, 湯のみ; （分量）一杯 |
| 1714 | `tekniko` | 日本語 | {Ｂ}技術, 工学; 技巧, 技法, 手法 | {Ｂ}技術, 技法, 手法; 技巧 |
| 1714 | `tekniko` | 韓国語 | 기술, 공학; 기교, 기법, 수법 | 기술, 기법, 수법; 기교 |
| 1722 | `tempo` | 中国語 | 时间；时代，时期；（语法）时制 | 时间；时代，时期；（科学）标准时；（语法）时制 |
| 1728 | `teorio` | 中国語 | 理论，学说 | 理论，学说；空论 |
| 1728 | `teorio` | 韓国語 | 이론; 학설, …론 | 이론; 학설, …론; 탁상론 |
| 1732 | `tero` | 中国語 | 地球；陆地，地面；土地；土壤 | 地球；陆地，地面；土地；土壤；现世；世人 |
| 1758 | `tordi` | 韓国語 | 비틀다, 꼬다 | 비틀다, 꼬다; 왜곡하다 |
| 1759 | `tra` | 中国語 | 通过，经过，透过，穿过 | 通过，经过，透过，穿过；在…整个期间 |
| 1760 | `tradicio` | 中国語 | 传统，惯例；口传，传说 | 传统，惯例；口传，传说；（宗）圣传，口传教义 |
| 1775 | `treni` | 中国語 | 拖，拉，拽，牵引 | 拖，拉，拽，牵引；（转）勉强拖着度过 |
| 1780 | `trinki` | 日本語 | {Ｂ}［他］飲む（水・茶など） | {Ｂ}［他］飲む（水・茶など）; 祝杯をあげる |
| 1780 | `trinki` | 韓国語 | 마시다 | 마시다; 축배를 들다 |
| 1787 | `trunko` | 中国語 | 树干，躯干；（数）截头体；（建）柱身 | 树干，躯干；（解）主干；（数）截头体；（建）柱身；（海）锚杆 |
| 1800 | `turmenti` | 中国語 | 折磨，使痛苦 | 折磨，使痛苦；拷问 |
| 1800 | `turmenti` | 韓国語 | 괴롭히다, 고통을 주다 | 괴롭히다, 고통을 주다; 고문하다 |
| 1801 | `turni` | 中国語 | 转动；转向；翻转 | 转动；转向；翻转；改变 |
| 1801 | `turni` | 韓国語 | 돌리다, 회전시키다; 방향을 바꾸다; 뒤집다 | 돌리다, 회전시키다; 방향을 바꾸다; 뒤집다; 바꾸다 |
| 1820 | `valida` | 中国語 | 有效，生效 | 有效，生效；妥当的，有根据的 |
| 1827 | `varii` | 中国語 | 变化，变动；各不相同 | 变化，变动；各不相同；（材料）胀缩变形 |
| 1851 | `vermo` | 日本語 | {Ｂ}（ミミズ・寄生虫などの）虫; （毛虫・いも虫など）幼虫; うじ虫 | {Ｂ}（ミミズ・寄生虫などの）虫; （毛虫・いも虫など）幼虫; うじ虫; 《転》卑しい人; 【情】ワーム |
| 1851 | `vermo` | 中国語 | 蠕虫；幼虫；蛆虫 | 蠕虫；幼虫；蛆虫；（转）卑微无价值的人；（计）蠕虫 |
| 1851 | `vermo` | 韓国語 | 벌레, 유충, 구더기 | 벌레, 유충, 구더기; (비유) 하찮은 사람; (컴퓨터) 웜 |
| 1853 | `verŝi` | 韓国語 | 액체를 붓거나 쏟다 | 액체나 빛 등을 붓거나 쏟다; 흘리다 |
| 1887 | `volvi` | 中国語 | 缠，绕 | 卷，卷起；缠绕 |
| 1901 | `ĉambro` | 日本語 | {Ｂ}部屋, 室 | {Ｂ}部屋, 室; （議会などの）院, 会議所; 【技】室, チャンバー |
| 1901 | `ĉambro` | 中国語 | 房间 | 房间，室；议院、商会等机构；（技术）腔室，室 |
| 1901 | `ĉambro` | 韓国語 | 방, 실 | 방, 실; (의회 등의) 원, 회의소; (기술) 실, 챔버 |
| 1917 | `ĉevalo` | 日本語 | {Ｂ}【動】ウマ（馬）; 【遊】（チェスの）ナイト, （将棋の）桂馬 | {Ｂ}【動】ウマ（馬）; 【遊】（チェスの）ナイト, （将棋の）桂馬; 【機】馬力 |
| 1917 | `ĉevalo` | 中国語 | 马；（棋）马（国际象棋），桂马（将棋） | 马；（棋）马（国际象棋），桂马（将棋）；（技术）马力 |
| 1917 | `ĉevalo` | 韓国語 | 말[馬]; (체스) 나이트; (쇼기) 계마 | 말[馬]; (체스) 나이트; (쇼기) 계마; (기술) 마력 |
| 1943 | `ĝui` | 韓国語 | 즐기다 | 즐기다, 누리다 |
| 1948 | `ĵeti` | 中国語 | 扔，投，抛；甩出，抛散 | 扔，投，抛；甩出，抛散；猛推，猛地伸出 |
| 1965 | `ŝiri` | 中国語 | 撕，扯裂，撕开；扯下，摘下；强行分开 | 撕，扯裂，撕开；扯下，摘下；强行分开；（转）使剧痛，使心痛如裂 |
| 1973 | `ŝpari` | 日本語 | {Ｂ}［他］たくわえる, ためる, 貯蓄する; 節約する, 倹約する; =〜gi | {Ｂ}［他］たくわえる, ためる, 貯蓄する; 節約する, 倹約する; （人に苦労などを）免れさせる; =〜gi |
| 1973 | `ŝpari` | 中国語 | 储蓄，积攒；节省，节约 | 储蓄，积攒；节省，节约；使免受（辛劳、麻烦等） |
| 1973 | `ŝpari` | 韓国語 | 저축하다, 모아 두다, 비축하다; 아껴 쓰다, 절약하다 | 저축하다, 모아 두다, 비축하다; 아껴 쓰다, 절약하다; (수고·곤란 등을) 면하게 하다 |
| 1985 | `ŝuldi` | 中国語 | 欠（钱/债）；负有义务；受…恩惠 | 欠（钱/债）；负有义务；受…恩惠；归功于，归因于 |
| 1986 | `ŝultro` | 中国語 | 肩 | 肩；肩状部位 |
| 2096 | `fakturo` | 韓国語 | 상품·서비스 대금 청구서 | 거래 명세서, 송장, 청구서 |
| 2115 | `fortuno` | 日本語 | {Ｂ}運（幸運）, 運命, 幸運（財産の意味ではまれ） | {Ｂ}幸運, つき（財産の意味ではまれ） |
| 2115 | `fortuno` | 中国語 | 运气，幸运；命运 | 运气，幸运；好运 |
| 2115 | `fortuno` | 韓国語 | 행운, 운명 | 행운, 운 |
| 2140 | `ideologio` | 中国語 | 意识形态；思想体系；观念形态 | 意识形态；思想体系；观念形态；（哲）观念学；（转）空论 |
| 2146 | `indico` | 日本語 | {Ｂ}手がかり, =indikaĵo（徴候）; 【学】指数, 率; 【学】添え字（変数の右下につける） | {Ｂ}手がかり, =indikaĵo（徴候）; 【学】指数, 率; 【学】添え字（変数の右下につける）; 【情】インデックス（位置番号） |
| 2146 | `indico` | 中国語 | 征候，迹象，线索；指数，比率；（数）下标 | 征候，迹象，线索；指数，比率；（数）下标；（计）索引号，位置编号 |
| 2146 | `indico` | 韓国語 | 징후, 단서; 지수, 비율; (수학) 아래첨자 | 징후, 단서; 지수, 비율; (수학) 아래첨자; (컴퓨터) 인덱스, 위치 번호 |
| 2149 | `integra` | 日本語 | {Ｂ}全部の（完全な）, 欠けたところのない; 不可分の, 不可欠の | {Ｂ}全部の（完全な）, 欠けたところのない; （穀物・粉などが）全粒の; 【植】全縁の |
| 2149 | `integra` | 中国語 | 完整的，完备无缺的；不可分的；不可缺少的 | 完整的，完备无缺的；全谷物的；（植）全缘的 |
| 2149 | `integra` | 韓国語 | 완전한, 빠진 데 없는; 불가분의, 불가결한 | 완전한, 빠진 데 없는; 통곡물의; (식물) 가장자리가 갈라지지 않은 |
| 2170 | `katastrofo` | 中国語 | 大灾害，大惨事；破局 | 大灾害，大惨事；破局；（剧）结局，收场 |
| 2178 | `kodo` | 日本語 | {Ｏ}【法】法典; （電信などの）符号, 暗号; 【情】符号, コード | {Ｏ}【法】法典; （電信などの）符号, 暗号; 【情】コード; 【生】遺伝暗号 |
| 2178 | `kodo` | 中国語 | 法典；符号、密码；[计] 代码 | 法典；符号、密码；[计] 代码；（生）遗传密码 |
| 2178 | `kodo` | 韓国語 | 법전; 부호, 암호; (정보) 코드 | 법전; 부호, 암호; (정보) 코드; (생물) 유전 암호 |
| 2208 | `kotizi` | 中国語 | 缴纳会费 | 缴纳会费或分担金 |
| 2208 | `kotizi` | 韓国語 | 회비를 내다 | 회비나 분담금을 내다 |
| 2213 | `kvitanci` | 中国語 | 开收据 | 开收据；出具收讫或收货凭证 |
| 2213 | `kvitanci` | 韓国語 | 영수증을 발급하다 | 영수증·수령증을 발급하다 |
| 2216 | `latino` | 日本語 | {Ｂ}【史】ラテン人（古代イタリアの一種族） | {Ｂ}ラテン語; 【史】ラテン人（古代イタリアの一種族） |
| 2216 | `latino` | 中国語 | 古代拉丁人 | 拉丁语；古代拉丁人 |
| 2216 | `latino` | 韓国語 | 고대 이탈리아의 라틴인 | 라틴어; 고대 라틴인 |
| 2231 | `masko` | 日本語 | {Ｏ}仮面, 面（めん）, 覆面, マスク; 【写】（覆い焼きの）マスク; 《転》（いつわりの）仮面 | {Ｏ}仮面, 面（めん）, 覆面, マスク; 【写】（覆い焼きの）マスク; 【情】ビットマスク; 《転》（いつわりの）仮面 |
| 2231 | `masko` | 中国語 | 面具，假面；口罩；（转）伪装 | 面具，假面；口罩；（摄影）遮片；（计）位掩码；（转）伪装 |
| 2231 | `masko` | 韓国語 | 가면, 복면, 마스크; (사진) 마스크; (비유) 거짓된 겉모습 | 가면, 복면, 마스크; (사진) 마스크; (컴퓨터) 비트 마스크; (비유) 거짓된 겉모습 |
| 2242 | `miopa` | 日本語 | {Ｏ}【医】近視の, 近眼の, >>hipermetropa, >>presbiopa | {Ｏ}【医】近視の, 近眼の, >>hipermetropa, >>presbiopa; 《転》視野の狭い, 近視眼的な |
| 2242 | `miopa` | 中国語 | 近视的 | 近视的；（转）目光短浅的 |
| 2242 | `miopa` | 韓国語 | 근시의, 근시안의 | 근시의, 근시안의; (비유) 시야가 좁은 |
| 2243 | `miraklo` | 中国語 | 奇迹 | 奇迹；令人惊异的事 |
| 2250 | `negativa` | 日本語 | {Ｏ}消極的な; 否定的な; 【電】陰の; 【理】負の, Ｓ極の; 【数】負の; >>〜, ><〜 | {Ｏ}消極的な; 否定的な; （検査で）陰性の; 【電】陰の; 【理】負の, Ｓ極の; 【数】負の; 【写】陰画の; >>〜, ><〜 |
| 2250 | `negativa` | 中国語 | 消极的；否定的；（电/数）负的 | 消极的；否定的；（检测）阴性的；（电/物/数）负的，S极的；（摄影）负片的 |
| 2250 | `negativa` | 韓国語 | 소극적인; 부정적인; (전기) 음의, 음극의; (물리·수학) 음의, S극의 | 소극적인; 부정적인; (검사) 음성의; (전기) 음의, 음극의; (물리·수학) 음의, S극의; (사진) 음화의 |
| 2272 | `parentezo` | 韓国語 | 괄호; 문장 중간의 삽입구 | 괄호; 문장 중간의 삽입어구 |
| 2280 | `pledi` | 中国語 | 辩护；辩解；陈词（庭辩） | 辩护；辩解；陈词（庭辩）；（转）支持，为…辩护 |
| 2285 | `pozitiva` | 日本語 | {Ｏ}積極的な, 建設的な, 実際的な, 現実的な, 確実な; 肯定的な; 実証的な; 【電】陽の; 【理】正の, Ｎ極の; 【数】正の; 【写】ポジの; >>〜, ><〜 | {Ｏ}積極的な, 建設的な, 実際的な, 現実的な, 確実な; 肯定的な; 実証的な; （検査で）陽性の; 【電】陽の; 【理】正の, Ｎ極の; 【数】正の; 【写】ポジの; >>〜, ><〜 |
| 2285 | `pozitiva` | 中国語 | 积极的，肯定的；实际的，确实的；实证的；（检测）阳性的；（电/数）正的；（摄影）正片的 | 积极的，肯定的；实际的，确实的；实证的；（检测）阳性的；（电/物/数）正的，N极的；（摄影）正片的 |
| 2285 | `pozitiva` | 韓国語 | 적극적이고 건설적인; 실제적이고 현실적이며 확실한; 긍정적인; 실증적인; (전기·물리·수학) 양의, N극의; (사진) 포지의 | 적극적이고 건설적인; 실제적이고 현실적이며 확실한; 긍정적인; 실증적인; (검사) 양성의; (전기·물리·수학) 양의, N극의; (사진) 포지의 |
| 2314 | `rubo` | 中国語 | 瓦砾，垃圾，废料；（转）无价值之物 | 瓦砾，垃圾，废料；（地质）岩屑；（环境）废弃物；（转）无价值之物 |
| 2317 | `satelito` | 日本語 | {Ｏ}【天】衛星; 人工衛星; 《転》衛星国, 衛星都市; 《転》（追従する）手下, 取り巻き | {Ｏ}【天】衛星; 人工衛星; 【機】遊星歯車; 《転》衛星国, 衛星都市; 《転》（追従する）手下, 取り巻き |
| 2317 | `satelito` | 中国語 | 卫星；人造卫星；（转）卫星国、卫星城市；追随者 | 卫星；人造卫星；（机）行星齿轮；（转）卫星国、卫星城市；追随者 |
| 2317 | `satelito` | 韓国語 | 위성, 인공위성; (비유) 위성국·위성도시; 추종자 | 위성, 인공위성; (기계) 유성 기어; (비유) 위성국·위성도시; 추종자 |
| 2326 | `skizi` | 中国語 | 草拟，素描 | 草拟，素描；概述 |
| 2345 | `supre` | 韓国語 | 위에, 꼭대기에 | 위에, 위쪽으로; 높은 곳에, 꼭대기에 |
| 2351 | `talento` | 韓国語 | 재능, 타고난 능력 | 재능, 타고난 능력; 탈란트(고대 무게·화폐 단위) |
| 2362 | `testamento` | 中国語 | 遗嘱；[宗] 约书 | 遗嘱；（基督教）圣约（旧约/新约） |
| 2366 | `tropiko` | 日本語 | {Ｏ}【地理】回帰線 | {Ｏ}【地理】回帰線; （複数で）熱帯地方 |
| 2376 | `varbi` | 日本語 | {Ｏ}［他］（会員などを）募集する; 【軍】徴募する | {Ｏ}［他］（会員・顧客などを）勧誘する, 募集する; 【軍】徴募する |
| 2376 | `varbi` | 中国語 | 招募 | 招募，劝募；招揽客户 |
| 2376 | `varbi` | 韓国語 | 사람을 모집하다 | 회원 등을 모집하다, 가입을 권유하다; 고객을 끌어들이다; (군사) 모병하다 |
| 2378 | `vegeti` | 中国語 | 生长；混日子 | 生长；（转）无生气地生活，无所作为地度日 |
| 2399 | `ŝoki` | 日本語 | {Ｏ}［他］精神的な衝撃を与える, ショックを与える, ぎょっとさせる | {Ｏ}［他］精神的な衝撃を与える, ショックを与える, ぎょっとさせる; 【医】ショック状態にする |
| 2399 | `ŝoki` | 中国語 | 震惊，冲击 | 震惊，冲击；（医）使休克 |
| 2399 | `ŝoki` | 韓国語 | 정신적 충격을 주다 | 정신적 충격을 주다; (의학) 쇼크 상태에 빠뜨리다 |
| 2446 | `ampolo` | 日本語 | {Ｂ}電球; 【医】アンプル | {Ｂ}電球; 【医】アンプル; 【解】膨大部 |
| 2446 | `ampolo` | 中国語 | 电灯泡；【医】安瓿 | 电灯泡；【医】安瓿；（解）壶腹，膨大部 |
| 2446 | `ampolo` | 韓国語 | 전구; (의학) 앰풀 | 전구; (의학) 앰풀; (해부) 팽대부 |
| 2466 | `bapti` | 中国語 | 洗礼；命名 | 施洗礼；命名 |
| 2498 | `cirkvito` | 日本語 | {Ｂ}【電】回路 | {Ｂ}【電】回路; 【機】流体回路 |
| 2498 | `cirkvito` | 中国語 | 电路 | 电路；（机）流体回路 |
| 2498 | `cirkvito` | 韓国語 | 전기 회로 | 전기 회로; (기계) 유체 회로 |
| 2573 | `funto` | 日本語 | {Ｂ}【単】ポンド（重量単位） | {Ｂ}【単】ポンド（重量単位）; 【貨】ポンド |
| 2573 | `funto` | 中国語 | 磅（重量单位） | 磅（重量单位）；英镑等货币单位 |
| 2573 | `funto` | 韓国語 | 파운드(무게 단위) | 파운드(무게 단위); 파운드화(통화 단위) |
| 2575 | `galo` | 日本語 | {Ｂ}【解】胆汁; 《転》苦々しさ, 癇癪 | {Ｂ}【解】胆汁; 【測】ガル（重力加速度の単位）; 《転》苦々しさ, 癇癪 |
| 2575 | `galo` | 中国語 | 胆汁；恼怒，脾气 | 胆汁；（测）伽（重力加速度单位）；恼怒，脾气；（转）苦涩 |
| 2575 | `galo` | 韓国語 | 담즙; (비유) 분노, 씁쓸함 | 담즙; (측지) 갈(중력가속도 단위); (비유) 분노, 씁쓸함 |
| 2579 | `garni` | 日本語 | {Ｂ}［他］飾る（付け合わせる）, 装飾する; 付け合わせる | {Ｂ}［他］補強する, 備え付ける; 飾る, 装飾する; 付け合わせる |
| 2579 | `garni` | 中国語 | 装饰，点缀；配菜 | 加固，装配；装饰，点缀；配菜 |
| 2579 | `garni` | 韓国語 | 장식하다, 꾸미다; 곁들이다 | 보강하다, 갖추다; 장식하다, 꾸미다; 곁들이다 |
| 2594 | `gvardio` | 日本語 | {Ｂ}【軍】近衛兵 | {Ｂ}【軍】近衛隊, 近衛兵 |
| 2604 | `horizontalo` | 日本語 | {Ｂ}水平線 | {Ｂ}水平な線, 横線 |
| 2604 | `horizontalo` | 韓国語 | 수평선; 수평의 선 | 수평선, 가로줄 |
| 2620 | `kakao` | 日本語 | {Ｂ}カカオ | {Ｂ}カカオ; ココア（粉・飲料） |
| 2620 | `kakao` | 韓国語 | 카카오콩 | 카카오콩; 코코아(분말·음료) |
| 2659 | `kresto` | 日本語 | {Ｂ}とさか; 頂上 | {Ｂ}とさか, 冠羽; （山・波などの）峰, 稜線 |
| 2673 | `laŭbo` | 日本語 | {Ｂ}あずまや | {Ｂ}緑廊, 藤棚, あずまや |
| 2766 | `prunto` | 日本語 | {Ｂ}借入, 借金; 借りたもの | {Ｂ}借入, 借金; 借りたもの; 【情】借り（減算の繰り下がり）; 【言】借用, 借用語 |
| 2766 | `prunto` | 中国語 | 借款；借入款；借来的款项或物品 | 借款；借入款；借来的款项或物品；（计）借位；（语言）借用、借词 |
| 2766 | `prunto` | 韓国語 | 차입, 빌린 돈이나 물건 | 차입, 빌린 돈이나 물건; (컴퓨터) 빌림수; (언어) 차용, 차용어 |
| 2779 | `registro` | 日本語 | {Ｂ}記録, 登録簿; 【音】音域 | {Ｂ}記録, 登録簿; 【音】音域; 【情】レジスタ（記憶装置） |
| 2779 | `registro` | 中国語 | 登记簿，登记表；记录；（音）音域 | 登记簿，登记表；记录；（音）音域；（计）寄存器 |
| 2779 | `registro` | 韓国語 | 기록, 등록부; (음악) 음역 | 기록, 등록부; (음악) 음역; (컴퓨터) 레지스터 |
| 2796 | `rusto` | 日本語 | {Ｂ}錆（さび） | {Ｂ}錆（さび）; 【植病】さび病 |
| 2818 | `spiti` | 日本語 | {Ｂ}［他］逆らう, 無視する | {Ｂ}［他］逆らう, 挑む; ものともしない |
| 2818 | `spiti` | 韓国語 | 무시하다, 거역하다 | 무시하고 맞서다, 거역하다 |
| 2819 | `splito` | 日本語 | {Ｂ}破片, 裂片 | {Ｂ}破片, 裂片; 【電】半導体チップ |
| 2819 | `splito` | 中国語 | 裂片，碎片 | 裂片，碎片；（电）半导体芯片 |
| 2819 | `splito` | 韓国語 | 조각, 파편 | 조각, 파편; (전자) 반도체 칩 |
| 2823 | `stampo` | 日本語 | {Ｂ}刻印; 特徴 | {Ｂ}刻印, スタンプ印; 特徴 |
| 2833 | `suplemento` | 日本語 | {Ｂ}補足, 増補 | {Ｂ}補足, 増補; 【数】補角 |
| 2833 | `suplemento` | 中国語 | 增补；补篇，补遗 | 增补；补篇，补遗；（数）补角 |
| 2833 | `suplemento` | 韓国語 | 보충, 증보; 부록 | 보충, 증보; 부록; (수학) 보각 |
| 2834 | `supro` | 韓国語 | 꼭대기 | 꼭대기, 윗부분 |
| 2837 | `takto` | 日本語 | {Ｂ}拍子; 機転 | {Ｂ}拍子, リズム; （対人上の）機転・気配り; 【電】クロック信号 |
| 2837 | `takto` | 中国語 | 拍子，节拍；机敏，分寸感 | 拍子，节拍；机敏，分寸感；（电）时钟信号 |
| 2837 | `takto` | 韓国語 | 박자, 리듬; 재치, 눈치 | 박자, 리듬; 재치, 배려 있는 눈치; (전자) 클록 신호 |
| 2838 | `tapeto` | 日本語 | {Ｂ}壁紙; じゅうたん | {Ｂ}壁紙; タペストリー（壁掛け織物） |
| 2838 | `tapeto` | 中国語 | 墙纸；地毯 | 墙纸，壁纸；壁毯 |
| 2838 | `tapeto` | 韓国語 | 벽지; 양탄자 | 벽지; 태피스트리(벽걸이 직물) |
| 2846 | `teraso` | 中国語 | 平台，台地，平顶屋 | 露台，平台；台地，阶地；屋顶平台 |
| 2848 | `teĥniko` | 日本語 | {Ｂ}技術（テクノロジー）, =〜 | {Ｂ}技法・技術, =〜 |
| 2860 | `tufo` | 韓国語 | 한 다발, 한 숱 | 한 다발, 한 뭉치 |
| 2861 | `vadi` | 日本語 | {Ｂ}［自］（浅瀬を）歩いて渡る | {Ｂ}［自］水・泥・雪などを歩いて進む; 浅瀬を渡る |
| 2861 | `vadi` | 中国語 | 淌水，涉水；跋涉 | 淌水，涉水；在泥、雪、沙等中跋涉 |
| 2861 | `vadi` | 韓国語 | 얕은 물을 걸어 건너다 | 물·진흙·눈 등을 헤치고 걷다; 얕은 물을 걸어 건너다 |
| 2866 | `veluro` | 日本語 | {Ｂ}ビロード, ベルベット | {Ｂ}ビロード, ベルベット; ビロード状の柔らかな毛・表面 |
| 2866 | `veluro` | 韓国語 | 벨벳, 비로드 직물 | 벨벳, 비로드 직물; 벨벳 같은 부드러운 털·표면 |
| 2867 | `vergo` | 日本語 | {Ｂ}むち, 小枝 | {Ｂ}むち, 小枝; 細い棒・ロッド |
| 2867 | `vergo` | 中国語 | 鞭子；细枝，小枝 | 鞭子；细枝，小枝；细杆 |
| 2867 | `vergo` | 韓国語 | 채찍; 잔가지 | 채찍; 잔가지; 가는 막대 |
| 2875 | `vindo` | 日本語 | {Ｂ}巻き布, 包帯; 産着 | {Ｂ}巻き布, おくるみ; 包帯 |

## 検証メモ

- BOMあり、CRLF維持。
- データ行数2890件、全行9列を維持。
- `編集ログ/` 側CSVとルート側CSVの内容一致を確認済み。
- 元CSVと比べて、`>>`、`=`、`[~` の出現数は不変。
