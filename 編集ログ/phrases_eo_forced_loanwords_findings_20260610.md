# 強引な外来語エスペラント化（minibaro級）全数調査報告

作成日: 2026-06-10
対象: `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv` 全5,000文（＋2890語彙リスト）
背景: minibaro → trinkejeto / ĉambra fridujeto / ĉambra ŝranketo 置換（commit 7684656）を受け、
「同様の強引な借用語が他にも無いか」を全数調査した。
方針: 前回ログ（`phrases_eo_review_findings_20260607.md`）と同じ。**明確に確認できたものだけ**を
修正候補とし、確証なきものは却下（「角を矯めて牛を殺さない」）。判定は PIV / Reta Vortaro (ReVo) /
eo.wikipedia への実照合に基づく。

**ステータス: Codex再検証後、一部適用済み。**
2026-06-10に、学習教材としての標準性・透明性・意味保持を優先し、第1ラウンド8文＋第2ラウンド18文
＝計26文を修正した。
修正した文はRHVoice `spomenka`で音声を再生成し、root音声とスマホ用音声を同期済み。
Google Driveフォールバックは、ユーザー側で新WAVをアップロードするまで新規キーが一部未登録になる。
アプリ同梱のローカル音声は存在するため通常再生には支障ないが、Drive fallback完全同期には追加アップロードが必要。

## Codex再検証・適用結果（2026-06-10）

### 適用した修正（8文）

- PID 826: `Ni penos fari lian fotoroboton` → `Ni penos fari lian portreton laŭ priskribo`
  - `fotoroboto` は露語由来カルク色が強く、PIV標準語根だけで「説明に基づく人物像」を表せるため置換。
- PID 1301: `Fraŭlino Wane ...` → `Fraŭlino Wayne ...`
  - 日中韓露訳が Wayne 相当で一致しており、英語列も `Miss Wayne ...` に統一。
- PID 2923: `picerion` → `picejon`
  - PIVは `pic/o` の派生として `picejo` を載せ、CSV内にも `picejoj` が既出。
- PID 3232: `grilitan salmon` → `kradrostitan salmon`
- PID 3248: `grilitan karpon` → `kradrostitan karpon`
  - PIVの `gril/o` はコオロギ。料理の「グリル」は標準語根 `krad/o` + `rost/i` で表す方が教材として透明。
- PID 3526: `certifikato` → `atestilo`
  - CSV内で証明書には `atestilo` 系が既に使われており、標準語根 `atest/i` に統一。
- PID 3682: `duonduzenon da ovoj` → `ses ovojn`
  - `duzeno` は非PIVで、日韓訳も「6個」相当。学習教材として普遍的な数詞表現に置換。
- PID 4802: `mobilan reton` → `poŝtelefonan reton`
  - `mobile network` の直訳感を避け、CSV内既出の `poŝtelefono` 系に合わせた。

### 維持した候補

- PID 4223 `toaston`: PIVに `toast/o` があり、「トースト」の意味として正規。
- PID 4405 `feni`: PIVの `fen/o` には温風器具（例: harsekigilo）の意味があり、派生動詞として許容範囲。
- PID 2959 `smuzion`: PIV非掲載だが、Vikipedioでも `Fruktkirlaĵo aŭ Smuzio` として扱われ、現代借用語として理解可能。今回は過純化を避けて維持。
- PID 4073 `regato`: ユーザー判断により維持。PIVには `regatt/o = boatkonkurso` があり、以前の `regatto`→`regato` 修正の趣旨も踏まえて触らない。
- PID 870 `vendmanaĝero`: `manaĝero` はPIVに狭義で掲載され、現代的職名として理解可能。`vendestro` への置換は意味を狭める可能性があるため維持。

## Codex第2ラウンド再検証・適用結果（2026-06-10）

第2ラウンドの強候補・グレーリストから、明確に教材品質が上がる18文を追加修正した。
食品名など、固有文化名として学ぶ価値があるものや、現代語として十分通るものは維持した。

### 第2ラウンドで適用した修正（18文）

- PID 4941: `pezi` → `pesi`
  - PIVで `pez/i` は自動詞「重さがある」、`pes/i` は他動詞「重さを量る」。これは明確な1字誤り。
- PID 4014: `Estis remiso` → `La rezulto estis egala`
  - `remiso` は不安定な借用形。初心者向けには標準語根だけの透明な表現がよい。
- PID 3330: `kaperojn` → `kaporojn`
  - PIVで食用ケッパーは `kapor/o`。`kaper/i` は「私掠する」で別語根。
- PID 3226/3229: `fumitan` → `fumaĵitan`
  - PIVでは燻製にする動詞は `fumaĵi`。喫煙・煙を出す `fumi` と区別。
- PID 3999: `malsekkostumon` → `plonĝkostumon`
  - 英語 `wetsuit` の直訳を避け、同トピック内既出の `plonĝkostumo` に統一。
- PID 2271: `Kie estas la parkometro?` → `Kie mi pagu por parkumado?`
  - `parkometro` を避け、駐車料金を払う場所を標準語根で尋ねる表現へ。
- PID 2290: `Vi pasos superbazaron` → `Vi preterpasos superbazaron`
  - 「通り過ぎる」は `preterpasi` が自然。
- PID 3192: `La sekvan rondon mi pagas` → `La sekvajn trinkaĵojn mi pagas`
  - 英語 `round` の酒席イディオム直訳を避け、意味を透明化。
- PID 998: `Li estas en rilato` → `Li havas amrilaton`
  - 裸の `en rilato` を避け、恋愛関係を明示。
- PID 4385/4387: `farbigi/farbi` harojn → `tinkturigi/tinkturi` harojn
  - PIVで髪や布を染めるのは `tinkturi`。`farbi` は塗料を塗る語感。
- PID 1921: `fotografiojn` → `fotojn`
  - 可算の写真はCSV内既出の `fotoj` に統一。PIVでは `fotografio` は写真術寄り。
- PID 4403: `Malantaŭe kojne` → `Malantaŭe laŭgrade mallongigite`
  - 露語直訳風の `kojne` を避け、髪型指示として意味を明示。
- PID 2885: `adherema filmo` → `adhera plastfolio`
  - 英語 `cling film` の直訳感を抑え、PIV語根 `adher-` と `plast-` で透明化。
- PID 3347: `cerealojn` → `cerealaĵojn`
  - PIVで朝食用シリアルは `cerealaĵo`。
- PID 2870: `detergenton` → `deterganton`
  - PIV派生形 `deterganto` に統一。
- PID 2464: `10 funtojn` → `10 pundojn`
  - 通貨ポンドはCSV内の他文と同じ `pundoj` に統一。重量単位 `funtoj` は別文で維持。

### 第2ラウンドで維持した主な候補

- PID 3175 `naĉojn`: 料理名としての文化的借用。説明的言い換えは不自然で、料理名としての学習価値を落とすため維持。
- PID 3087 `kalzoneon`: 料理名として維持。`faldita pico` は説明としては分かるが、固有料理名を失う。
- PID 4021 `servas la pilkon`: スポーツ文脈で十分理解可能。`ekfrapas` はサーブの専門性を弱めるため維持。
- PID 3969 `viva muziko`: 現代語として理解可能。`ĉeesta/surloka muziko` はかえって不自然寄り。
- PID 4530/4645/4646 `analizo`: 医療・検査文脈で理解可能。検査の種類を狭める置換はしない。
- PID 2337 `rezervajn partojn`: 車の部品として自然に理解可能。`vicpecoj` への置換はやや専門的。
- PID 947 `belaruso`, PID 1382/1737 `informatiko`, PID 1752 `konstruktivan`, PID 3972 `diskĵokeo`:
  現代語・国名表記・専門語として維持。
- PID 3711/3738 `vidoj`, Wi-Fi/Facebook/Tvitero/evento/mufino/bovlingo/sprajo:
  明確な誤りではなく、表記方針や現代語許容の範囲として維持。

## 調査方法（網羅性の担保）
1. 全5,000文のエスペラント列からユニーク語 **4,813語** を全数抽出。
2. うち2890語彙リスト・基本機能語でカバーされない **2,156語** を8系統で1語ずつ全数レビュー。
   ＋ 2890教育語彙リスト自体の精査 ＋ 現代借用語パターン網（61マーカー）での直接走査。
3. 候補 **60語根** を辞書学者役エージェントが敵対的に検証（デフォルトは「却下」側に倒す）。
   PIV掲載・ReVo記事の有無・eo.wikipedia記事名を可能な限り実フェッチで確認。
4. 結果: **49語根 却下（正規語と確認）／11語根 確定（12文）**。

---

## 【修正候補】確定11語根・12文

多くは**コーパス内部の不整合**（同じコーパスの他の文では本来語を使用）という決定的証拠つき。
確度の高い順ではなく PID 順。「→」が修正案。

### 1. PID 3232 / 3248 — grilita（×2文）
- 文: "Mi ŝatus la **grilitan** salmon" (Lv4, Food/Meat & Fish)
- 文: "Li havos **grilitan** karpon" (Lv7, Food/Meat & Fish)
- → **kradrostitan**（"Mi ŝatus la kradrostitan salmon" / "Li havos kradrostitan karpon"）
- 根拠: PIVに動詞 grili は無し。PIVの grilo は「コオロギ」のみで、grilitan は誤った語根に
  解析される。PIVの焼き網調理は kradrosti。コーパス自身が他所では全て rost- を使用
  （rostitan viandon 3052, rostitan skombron 3236, rostbefon 3227, mezrostita 3051,
  そして決定的に **rostokradon**「焼き網」4131）。

### 2. PID 4223 — toasto
- 文: "Ĉu vi ŝatus **toaston**?" (Lv7, Leisure Time/Having Guests)
- → **rostpanon**（"Ĉu vi ŝatus rostpanon?"）
- 根拠: PIVの tosto は「乾杯」のみ（本コーパスも PID 210 "Ni tostu por vi!" / 216 "proponi
  toston" で正しく乾杯として使用）。パンの toasto は 'oa' という非エスペラント綴りを含む
  機械的英語借用で、乾杯の tosto と1字違いのため学習者に最大級に紛らわしい。
  PIV・Wells とも「トースト（パン）」は rostpano。語彙リストに pano と rosti があるため
  学習者に完全に透明。

### 3. PID 2923 — picerio
- 文: "Ĉu vi povas rekomendi **picerion**?" (Lv7, Restaurant & Pub/Booking a Table)
- → **picejon**（"Ĉu vi povas rekomendi picejon?"）
- 根拠: picerio はPIV非掲載のイタリア語直借用。標準形は透明な合成語 picejo（pico+ejo）で、
  **本コーパス自身が PID 553 で picejoj を使用**（内部不整合）。さらに語彙リストの
  piceo（トウヒ＝樹木）と視覚衝突する。

### 4. PID 3526 — certifikato
- 文: "Ĉu estas **certifikato** por ĝi?" (Lv7, Shopping/Accessories)
- → **atestilo**（"Ĉu estas atestilo por ĝi?"）
- 根拠: ReVo記事なし（実照合404）・PIV非掲載。標準は atestilo（Fundamento語根 atest- + -il）。
  **本コーパス自身が atestilo を2回使用**（PID 2121 "internacia vakcinatestilo",
  PID 4633 "kuracistan atestilon"）。修正で3文が統一される。語彙リストに atesti あり。

### 5. PID 4405 — feni
- 文: "Bonvolu tondi kaj **feni** miajn harojn" (Lv8, Services/At the Beauty Salon)
- → **blovsekigi**（"Bonvolu tondi kaj blovsekigi miajn harojn"）
- 根拠: PIV・ReVoとも feno は「フェーン（アルプスおろしの風）」のみで、動詞・美容の語義なし。
  露語 фен（ドライヤー）の機械カルク（本文の露訳列 "высушите феном" が出所を裏付け）。
  **本コーパス自身が PID 3586 で harsekigilon を使用**（内部不整合）。
- 注意: 'fen' の文字列はEO列に11件の誤検出あり（fenestro×9, ofendiĝu 268, fendiĝis 4456）。
  これらは別語根で正当。**触らないこと。**

### 6. PID 826 — fotoroboto
- 文: "Ni penos fari lian **fotoroboton**" (Lv9, Emergencies/At the Police Station)
- → **komponitan portreton**（"Ni penos fari lian komponitan portreton"）
- 根拠: PIV非掲載・ReVo記事なし（実照合404）・eo.wikipedia検索0件。露語 фоторобот
  （モンタージュ写真）の純カルクで、スラヴ語圏外のエスペランティストには不透明。
  露訳列 "составить его фоторобот" が出所を裏付け。語彙リストに portreto があるため
  修正案は既習語根のみで構成され、現状0件の portret- に例文を与える副次効果もある。

### 7. PID 4802 — mobila
- 文: "Kiun **mobilan** reton vi havas?" (Lv10, Communication Means/Phone)
- → **poŝtelefonan reton**（"Kiun poŝtelefonan reton vi havas?"）
- 根拠: PIVは mobiliz/i（＋美術のモビール mobilo）のみで形容詞 mobila は無し。ReVoにも
  記事なし（実照合: M索引に mobilizi/mobilizo のみ）。eo.wikipedia の記事名は
  「Poŝtelefono」で、'Mobila telefono' 等は存在しない。"mobile network" の機械カルク。
  本コーパスは PID 3567 で poŝtelefonon を使用済み。
- 注意: PID 2578 "aŭtomobilaj ferdekoj" は aŭtomobilo（PIV正規語）由来で正当。**触らないこと。**

### 8. PID 2959 — smuzio
- 文: "Mi ŝatus papajan **smuzion**, mi petas" (Lv6, Restaurant & Pub/Ordering Drinks)
- → **papajan kirlaĵon**（"Mi ŝatus papajan kirlaĵon, mi petas"）
- 根拠: PIV非掲載・ReVo記事なし（実照合）。決定的に、**eo.wikipedia 自身が Smuzio を
  本来語合成 Fruktkirlaĵo にリダイレクト**している。kirl- 語根は本コーパスの PID 3376
  kirlovaĵon（スクランブルエッグ）で使用済み。文中に papaja が既にあるため
  fruktokirlaĵo でなく単に kirlaĵo とするのが重複なく自然。
- ※前回ログ（20260607）の浅いスキャンでは「正当な借用語」と仮判定していたが、
  今回の辞書実照合で覆った（判定変更を明示しておく）。

### 9. PID 4073 — regato
- 文: "Kiom da boatoj partoprenas en ĉi tiu **regato**?" (Lv10, Leisure Time/Sport)
- → **velkonkurso**（"Kiom da boatoj partoprenas en ĉi tiu velkonkurso?"）
- 根拠: ReVoで regato は reg-at-o「統治される者・臣民」（regi の受動分詞名詞）のみで、
  流暢な読者はまずそう解析する。レガッタの意の regat- 借用語根はPIV・ReVo・eo.wikipedia
  いずれにも不在。ホモニムを生む機械借用。
- ⚠️ 重要な経緯: この文は dcd6ecc で regatto（綴り誤り）→ regato に修正したまさにその文。
  当時の修正は「二重子音の除去」として正しかったが、今回の深掘りで regato という語自体が
  借用として不適と判明した（二段階目の発見）。
- 代案検討: boatvetkuro だと "Kiom da boatoj ... en ĉi tiu boatvetkuro" と boato が重複する
  ため velkonkurso が読みやすい。コーパスは vetkuroj (4042, 4064) を、語彙リストは
  konkurso を既に含む。

### 10. PID 870 — vendmanaĝero
- 文: "Mi estas Hina, **vendmanaĝero**" (Lv9, Making Friends/Introductions)
- → **vendestro**（"Mi estas Hina, vendestro"）／別案 vendodirektoro
- 根拠: PIVの manaĝero は「芸能人・スポーツ選手の業務を管理する者（≒興行主）」の狭義のみ。
  ReVoに manaĝer- 記事なし（実照合404）。"sales manager" の機械カルクで、報道エスペラントは
  vendestro / vendodirektoro / vendoĉefo を使う。語彙リストは -estro（接尾辞として）と
  direktoro の両方を含む。

### 11. PID 3682 — duonduzeno
- 文: "Mi ŝatus **duonduzenon** da ovoj" (Lv10, Shopping/At the Supermarket)
- → **ses ovojn**（"Mi ŝatus ses ovojn"）が最も安全。別案 duondekduon da ovoj
- 根拠: duzeno はPIV非掲載で、ReVoにも記事なし・dekdu/ 記事内にも言及なし（実照合）。
  対訳辞書（Wells, Krause）が解読用に載せるのみで、まとまった文章では稀。
  学習コーパスとしては普遍的な数詞合成（dekduo）または単純な ses が適切。
- ※前回ログ（20260607）では【要確認・修正せず】だった項目。今回 ReVo 実照合の
  不在確認により判定を引き上げた（最終判断はユーザーに委ねる）。

---

## 【却下】正規語と確認された主な候補（49語根 — 再調査不要のための記録）

- **PIV 2020 見出し語**: ĉipso（ポテトチップス）, ŝorto（短パン）, steko, strudelo（PIV2,
  eo-wiki記事名も Strudelo）, benjeto（PIV1・文学出典あり）, stovo, hobio, jeto, starto,
  fragila（文学的新語としてPIV掲載）, tablojdo, jogurto, keĉupo（PIVは keĉapo, ReVoに keĉupo）
- **ReVo記事＋出典あり**: bovlingo（ボウリング）, mocarelo, muzikalo, suspenso, ŝorbeto,
  zorio（ビーチサンダル）, diskĵokeo, bonuso（→bonuskarto）, avio（→aviokompanio）, halala
- **正規の合成・派生**: kreditkarto, klimatizilo, retpoŝto, bankado, dislimo, karamelizi,
  rapidometro（透明な -metro 型）, fotokopiilo, taksimetro, fakso/faksi, skanilo
- **現代の定着語**: parkumi/parkumejo, hamburgero, animacio, informatiko, kebabo,
  mufino, naĉoj, kalzoneo（eo-wiki記事名 Kalzoneo と一致）
- **ブランド・固有名詞の表記（借用語ではない）**: Wi-Fi, PIN-kodo, Facebook, Tvitero,
  Skajpo（ReVo記事あり）, London Kings Cross, Divalo（eo-wiki実在）, siĥo（sikho の異綴）,
  22°C（記号）
- **konstruktiva** (PID 1752): 前回ログ同様【要確認・修正せず】を維持（PIVに
  konstruktivismo 経由で語根あり・現代誌で使用例あり。純化なら konstrua）。

2890教育語彙リスト自体には強引な借用語は**見つからなかった**（クリーン）。

---

## 【副産物】同調査で見つかったその他の修正候補

- **PID 1301 "Fraŭlino Wane"** — おそらく **Wayne** のタイポ。全訳列が ウェイン / 韦恩 /
  웨인 / Уэйн と一致。修正すると音声 1146_frauxlino_wane_... の再収録が必要。
- **表記揺れ（好みの問題・任意）**: Tvitero（PID 4902, エス化）vs Facebook（PID 4891, 生表記）。
  統一するなら Fejsbuko が対応形。なお Twitter→X 改名による内容の古さは別論点。
- **語彙CSVの重複見出し（誤りではない・整理課題）**: boto/botoj、buĝeto/budĝeto。

## 【参考】minibaro 置換3文への言語レビュー所見（適用済み分・任意の再検討）

2026-06-09 の検証時に言語レビューが付した所見（3文とも文法は正しい・適用済みのまま問題なし）:
- PID 2780 "ĉambran fridujeton" — 3案中最良。透明で自然。
- PID 2798 "trinkaĵoj el la ĉambra ŝranketo" — 正しいがやや冗長。
- PID 2618 "trinkejeto" — 唯一の弱点。「小さな飲み屋」寄りに読め、minibar の意が自明でない。
  もし揃えるなら ĉambra fridujeto への統一が候補（1概念3表現の解消にもなる）。

---

## 修正を適用する場合の手順（1文ごと）

EO文変更 → audioKey が変わるため、minibaro 修正と同一の手順が必要:
1. CSV の Esperanto 列を修正（他言語列は不変）
2. `python3 tools/reconcile_phrase_audio_rhvoice.py`（spomenka）で新WAV生成・旧WAV退避
   （当日日付を --candidate-csv/--generation-csv/--report-md/--archive-dir に指定）
3. `mobile_app/sentence-audio/` へミラー同期（perm 664）
4. `python3 tools/build_mobile_data.py`（sentences.json 再生成）
5. 新WAVを Google Drive フォルダ 1tmb4_k3zRv2JjOmHCNvv5zIbbneeKwYZ にアップロード
   （旧WAVは削除推奨 — 現在 minibaro 旧3件が削除されず残存中）
6. `python3 tools/build_drive_audio_manifest.py` で manifest 再生成
7. `python3 tools/validate_mobile_assets.py` で全検証
8. mobile-sw.js の CACHE_VERSION / app.js の APP_VERSION を更新 → commit / push

---
---

# 第2ラウンド調査（2026-06-10・Codex引き渡し用）

第1ラウンドの**構造的死角**を対象に再走査した。本ラウンドの成果物は「確定リスト」ではなく
**証拠付き候補リスト（グレーリスト込み）**であり、最終的な言語判定と修正は Codex に委ねる。
Codex が維持判断済みの5件（toaston / feni / smuzion / regato / vendmanaĝero）は対象外とし、
再フラグしていない。

## 第2ラウンドの調査範囲（第1回との差分）
1. **未レビューだった2,558語**: 第1回は2890語彙リストに語根が一致した語を機械的に除外して
   いた。偽の語根一致（例: kaperoj⇔kaperi）が隠れ蓑になるため、全数を1語ずつ再レビュー。
2. **正書法アノマリー56語**: 非エス綴り（oa/ou/th/ck/w/q/x/y・二重子音）の全数走査。
3. **EO≈EN/RU鏡像類似874語**: 各文のEO語と同じ文の英語・露語（翻字）との類似度0.8以上を
   機械抽出し、feni←фен 型の「出所言語との鏡像」を二重チェック。
4. **2890語彙リストの独立再走査**（前半・後半の2系統）。
5. **第1回却下49語根のグレーリスト再審**（Codex判断前提で、却下せず証拠付きで回収）。

判定の根拠として、ローカルの **PIV2020全文抽出（PIV2020_structured.txt・約45,000見出し）** への
grep照合と、Reta Vortaro / eo.wikipedia への実フェッチを使用した（証拠の質が第1回より高い）。

候補48語根を検証した結果: **強候補8 / グレーリスト24前後 / 誤フラグ12（破棄）**。

## 【強候補】forced-strong 8件（Codex最終判定待ち）

### R2-1. PID 4941 — pezi（他動詞誤用・1字修正）
- 文: "Bonvolu **pezi** ĉi tiun pakaĵon" (Lv6 Advanced 1, Communication Means/At the Post Office)
- → **pesi**（"Bonvolu pesi ĉi tiun pakaĵon"）
- 根拠: PIV2020 pez/i は明示的に (ntr)「重さがある」。他動詞「重さを量る」は pes/i
  （Fundamenta, sense 1 に "pesi pakaĵon" の用例そのもの）。コーパス自身が PID 2035
  "pesi la bagaĝon"・PID 3680 "pesi al mi tricent gramojn"・PID 4955 pesilon と正用。
- 注意: PID 4942 "Ĉu ĉi tio pezas tro multe?"（自動詞）、4649 pezo、2050 superpezo は正当。

### R2-2. PID 4014 — remiso
- 文: "Estis **remiso**" (Lv1 Beginner 1, Leisure Time/Sport)
- → **egalrezulto**（"Estis egalrezulto"）／別案 "La matĉo finiĝis sendecide"
- 根拠: 波独語 remis（引き分け）の機械エス化。PIV2020抽出に remis- 見出しなし・
  ReVo art/remis.html は404（実照合）。rem-i（舟を漕ぐ）と衝突し「漕ぎ主義」と誤解析される。
- 注意: 語彙リスト1474行の remi（舟を漕ぐ）は正当・無関係。**触らないこと。**

### R2-3. PID 3330 — kaperoj（語根取り違え）
- 文: "Li ŝatas **kaperojn**" (Lv4, Food/Staple Food & Spices)
- → **kaporojn**（"Li ŝatas kaporojn"）
- 根拠: PIV2020で kaper/i はザメンホフ的「私掠（敵船を拿捕する）」の動詞。食用ケッパーは
  kapor/o（Fundamenta + Oficiala Aldono）。現状の文は字義通りには「彼は私掠行為を好む」。
- ※第1回は「Wells辞書の異形として許容」と却下したが、PIV実照合で取り違えと判明（判定変更）。

### R2-4. PIDs 3226 / 3229 — fumita（燻製の意）
- 文: "Ĉu vi ŝatas **fumitan** viandon?" / "Mi prenos la **fumitan** truton" (Food/Meat & Fish)
- → **fumaĵita**（"fumaĵitan viandon" / "fumaĵitan truton"）
- 根拠: PIV2020・ReVoとも他動詞 fumi は「（タバコ等を）吸う」のみ。燻製にするは fumaĵi
  （PIV: "fumaĵita ŝinko, haringo"）。
- 注意: fum- 文字列は計18文にヒットするが、他15文（喫煙・禁煙文脈）は正用。**触らないこと。**

### R2-5. PID 3999 — malsekkostumo
- 文: "Kiom kostas lui **malsekkostumon** por unu tago?" (Lv10, Leisure Time/At the Beach)
- → **plonĝkostumon**
- 根拠: 英 wet+suit の形態素直訳。PIV2020・ReVoとも不在。**同じ小トピックの隣接文
  PID 3994・4000 が plonĝkostumon を使用**（内部不整合）。

### R2-6. PID 2271 — parkometro
- 文: "Kie estas la **parkometro**?" (Lv7, Car/Driving & Parking)
- → 言い換え **"Kie mi pagu por la parkumado?"**／別案 "Kie estas la parkuma pagilo?"
- 根拠: PIV2020抽出45k見出しに parkometr- なし・ReVo park 記事にも機器の語義なし（実照合）。
  コーパスは parkum- 系で統一済み（2245/2248/2269/2270/2356/2360/2373/4324）。

### R2-7. PID 3175 — naĉoj
- 文: "**Naĉojn**, mi petas" (Lv5, Restaurant & Pub/At the Pub)
- → 言い換え "Frititajn maizpecojn (tortiljopecojn), mi petas"／"Terpomfritojn, mi petas"
- 根拠: PIV・ReVoとも完全不在（辞書登録ゼロ）。
- ※第1回は「文化的食品名として許容」と却下したが、グレーリスト再審で smuzio 同型の
  無登録現代借用と再判定（判定変更）。Codexの判断材料として両論を残す。

### R2-8. PID 3087 — kalzoneo
- 文: "Jes, ili ankaŭ ŝatas **kalzoneon**" (Lv8, Restaurant & Pub/During the Meal)
- → **falditan picon**（pico はPIV標準・コーパスに9回出現）
- 根拠: PIV2020・ReVoとも不在（eo.wikipedia のみ）。picerio と同族のイタリア語直借用。
- ※第1回は「eo-wiki記事名と一致」で却容としたが再審で引き上げ（判定変更）。維持も可。

## 【グレーリスト】Codex判断行き 24件（語は実在だが PIV外の語義/形・英露カルク・内部不整合）

### A. 用法カルク（語自体は正当、当該文の語義がPIV外）
| PID | 現在の文（要点） | 問題 | 修正案 |
|---|---|---|---|
| 4021 | Kiu **servas** la pilkon? | servi にスポーツの「サーブ」語義なし（英 serve calque） | "Kiu ekfrapas la pilkon?" 等 |
| 2290 | Vi **pasos** superbazaron | pasi は自動詞（他動は古語=trapasi）。英 "pass a supermarket" calque | "Vi preterpasos superbazaron" |
| 3192 | La sekvan **rondon** mi pagas | rondo に「（酒の）一巡」語義なし（英 round calque） | "La sekvajn trinkaĵojn mi pagas" |
| 998 | Li estas **en rilato** | 裸の "en rilato"（英 in a relationship calque）。PIVは補語必須 | "Li havas amrilaton" |
| 3969 | Ĉu vi havas **vivan muzikon**? | viva に「生演奏」語義なし（PIV外・ReVoは収録） | "ĉeestan/surlokan muzikon" |
| 4530/4645/4646 | fari **analizojn**（医療検査） | analizo=化学分析。英露の「検査」calque ×3文 | "(laboratoriajn) ekzamenojn / testojn" |
| 4385/4387 | **farbi** miajn harojn | farbi=ペンキ塗り。毛染めは tinkturi（PIV） | "tinkturi miajn harojn blonde" |
| 2337 | ĉu vi havas rezervajn **partojn**? | 車の交換部品は peco/vicpeco（PIV）。parto は英 parts calque | "Ĉu vi havas vicpecojn?" |
| 1921 | grandigi ĉi tiujn **fotografiojn** | fotografio=写真術（不可算）。可算の写真は foto/fotografaĵo。同小トピック5文は fotoj | "fotojn" |
| 4141 | la plej bona **aktiveco** | aktiveco=抽象的活発さ。可算の活動は aktivaĵo/agado | "aktivaĵo" |
| 4403 | Malantaŭe **kojne** | 露 "Сзади клином" の直カルク。PIVの形容派生は kojnoforma | "kojnoforme"／"laŭgrade mallongigite" |
| 2885 | rulon da **adherema filmo** | 英 cling film calque（adhero は正当語根） | "adhera plastfolio" |

### B. PIV外の語形（PIV2020に別形あり・1字〜1語の置換）
| PID | 現在 | PIV2020形 | 備考 |
|---|---|---|---|
| 947 | belaruso | **beloruso** (k4444) | 1字修正 a→o |
| 1382/1737 | informatiko ×2 | **informadiko**（または komputiko） | 第1回は許容判定→再審でグレー |
| 1752 | konstruktivan kritikon | **konstruan kritikon** | 20260607ログでも要確認だった項目 |
| 3347 | cerealojn | **cerealaĵojn**（PIV派生形）/ matengrenaĵojn | cerealo は植物学の穀物種のみ |
| 2870 | detergenton | **deterganton**（PIV deterg/i 派生）/ lavilon | |
| 3972 | diskĵokeo | **diskestro**（PIV2020収録） | ReVo に diskĵokeo もあり（維持可） |
| 2464 | aldoni 10 **funtojn**（運賃チャージ） | **pundojn** | 通貨はコーパス全体で pundoj（1722/2060/4303）。2049 の funtoj（重量）は正当 |
| 3711/3738 | poŝtkartoj kun **vidoj** | **vidaĵoj**（PIVの絵葉書用例そのもの） | 2626/2836/4338 の vido（眺望）は境界・維持可 |

### C. 方針判断（誤りではない・表記ポリシーの統一）
- **Wi-Fi 生表記 ×2**（2606/3067）: ReVo形 vifio に統一するか、現状維持か（2文間では一貫）。
- **Tvitero vs Facebook**（4902/4891）: エス化と生表記が混在。どちらかに統一を推奨。
- **evento ×2**（1897/1947）: PIV語義は狭いがReVoの催事語義あり。aranĝoj への置換は任意。
  evento は語彙リスト416行でも教えているため、維持の論拠もある。
- **mufino**（3282）/ **bovlingo**（4160）/ **sprajo**（4412）: 辞書登録が薄いが言い換えに難
  （kuketo は別物・kegloludo は9ピン寄り・harlako は限定的）。Codexの裁量範囲。

## 【破棄】第2ラウンドで誤フラグと確認（再調査不要）
preskribi（PIV Oficiala Aldono・Z用例つき「処方する」— スキャナの「PIV不在」は事実誤認）、
tekokomputilo、paracetamolo、plur-、keĉupo、ŝorbeto、siĥo、rapidometro、muzikalo、
hamburgero、kebabo、parkumi。

## 【語彙リスト2890語の再走査結果】（フレーズではなく語彙CSV側の整理課題）
強引な借用語は前半・後半とも**ゼロ**（クリーン確認・2系統の独立レビューで一致）。
ただし整理課題を発見:
- **ĥ/k 重複ペア**（PIVはĥ形を参照扱い）: teĥniko(2848)/tekniko(1714)、ĥemio(2887)/kemio(764)、
  meĥaniko(2696)/mekaniko(1058)、meĥanismo(2697)/mekanismo(1059)、既知の budĝeto(2484)/buĝeto(254)
- **間投詞の重複**: fi(2104)/fi!(2554)、ha(2134)/ha!(2595)、he(2135)/he!(2600)、
  ho(2136)/ho!(2603)、ve(2377)/ve!(2864) — どちらか一方に統合推奨
- **不正形見出し**: "dio,Dio"(2516・カンマ連結かつ dio(2067) と重複)、"de/teni (sin)"(2505・
  空白+括弧入り)
- **形式不統一**: 2403〜2891行は PIV式スラッシュ区切り（aviad/ilo等・35件超）— TTSや
  解答照合に影響しうる
- jakto(2155) は PIV主形で正当（jaĥto が参照形）。boto/botoj は既知。

## 第2ラウンドの注意事項（Codex向け）
- 偽陽性警告を必ず参照のこと: fum-（15文の喫煙文脈は正用）、fen-（fenestro×9等）、
  part-（apart-/aparten-/partopren- 等16件は別語根）、rem-（remi=漕ぐは正当）、
  film-（映画の35文は正用）、pez-（自動詞用法3文は正用）。
- 第1回→第2回で判定が変わった3語（kapero・naĉoj・kalzoneo）は、第2回がローカルPIV2020
  全文への実grepに基づくため証拠の質が高い。ただし最終判断は Codex に委ねる。
- 語彙リスト後半の再走査は当初の自動実行が技術的要因で1回失敗し、別系統で再実行・完了済み
  （結果は上記の通りクリーン＋整理課題のみ）。

---
---

# 第3ラウンド調査（2026-06-10・フレーズ単位カルク・Codex引き渡し用）

第1・2ラウンドで**単語レベル**は全数走査済みのため、第3ラウンドは同じ病気の**連語・慣用句
レベル**（英語・露語の言い回しの逐語移植）を対象に、全5,000文を10分割で精読した。
判定は3条件（①英露列と逐語一致の非自明な連語 ②PIV/ReVo慣用に不在 ③明確な自然形が存在）
を満たすもののみフラグ。候補65件 → **強候補41 / グレーリスト20 / 誤フラグ4破棄**。
証拠はローカルPIV2020全文抽出への行番号付きgrep照合に基づく。

⚠️ **Codexへの注記**: フレーズ単位の言い換えは単語置換より侵襲的（音声再収録対象が多い）。
また会話帳というレジスター上、現代口語として許容する判断もあり得る（Codexが toasto 等を
維持した前例と同様）。本リストは「PIV照合で慣用外と確認できた」という事実の提示であり、
直すかどうかの優先順位付けは Codex に委ねる。**パターン家族ごとに一括判断すると効率的。**

## 【強候補・家族別】calque-strong 41件

### 家族A: 依頼の "Ĉu mi pov(us) havi X?"（英 "Can/Could I have X?" の移植）— 9件＋同族2件
PIV havi は所有状態のみで授受の依頼語義なし（PIV自身が havebla を「RICEVI できる」と定義）。
**決定的な内部不整合**: 同じトピック隣接文は ricevi を使用（2717 sapon / 2720 kusenon /
2721 kovrilon / 2722 gladilon / 2951 akvon / 2984 kranakvon）。
- 対象: PID 2207（seruron）, 2208（kaskon・露列は получить=ricevi）, 2654（unulitan ĉambron）,
  2718（tukon）, 2983（lakto）, 2988（botelon da vino）, 3031（menuon kaj vinkarton）,
  3506（ŝtrumpetojn）, 4475（ŝlosilringon）
- 同族（未フラグだが同型）: 1910（gvidiston）, 4949（poŝtmarkojn）
- 修正型: **havi → ricevi**（または "X, mi petas" 形）

### 家族B: havi/havos ＝「食べる・注文する」（英 light-verb "have" の移植）— 4件＋同族2件
PIV havi に飲食の語義なし。日韓訳自身が「食べます」と訳している（havi では表せない意味）。
- 対象: PID 3013（Kion vi ŝatus havi?）, 3248（havos kradrostitan karpon）,
  3298（havos kelkajn tomatojn）, 3334（havos iom da faboj）
- 同族: 4158（Kion ni havos por tagmanĝo?）, 4167（por deserto?）
- 修正型: **havi → preni / mendi**（隣接文 3327 "Mi prenos..." が in-corpus 規範）

### 家族C: fari rezervon（英 "make a reservation"）— 1件＋同族3件
PIV rezervo の4語義に予約なし。しかも PIV 慣用 "fari rezervojn" は別意味（留保を付ける）と
衝突。動詞 rezervi 自体は正当。
- 対象: 2640 / 同族: 2684, 2704, 2918
- 修正型: **fari rezervon → rezervi**（"Mi ŝatus rezervi ĉambron"）

### 家族D: 無目的語の Daŭrigu（道案内の英 "Continue..."）— 1件＋同族4件
PIV daŭrigi は他動詞。不定詞補語用法すら (evi) 注記つきで「Z. deklaris tiun lastan uzon
ne bona」。道案内の無目的語命令形は二重に規範外。
- 対象: 1841 / 同族: 1853, 1854, 1855, 1856
- 修正型: **Daŭrigu → Iru plu**（"Iru plu rekte antaŭen..."）

### 家族E: aliĝi al 人（英 "join me/you"）— 1件＋同族3件
PIV aliĝi は組織・団体・運動への加入のみ（aliĝilo=参加申込書）。食卓の同席は kun/akompani。
- 対象: 1119（aliĝu al mi por tagmanĝo）/ 同族: 1124, 1199, 1209
- 修正型: **"Venu tagmanĝi kun mi" / "Ĉu mi rajtas sidiĝi ĉe vi?"** 型

### 家族F: sur aviadilo / sur flugo（英 "on the plane/flight"）— 2件＋同族1件
PIVのRim.は三次元空間に en を指定（sur la ŝipo は歩ける甲板ゆえ例外）。flugo は出来事で
場所ですらない。
- 対象: 1968, 1987 / 同族: 2158
- 修正型: **sur → en**（aviadilo）／ **por**（flugo: "liberaj lokoj por ĉi tiu flugo"）

### 家族G: televido ＝ 受像機（機器は televidilo）— 1件＋同族2件
PIV: televido=遠隔視・放送、機器は televidilo。ReVoは機器語義を収録するが malofta 注記。
コーパス自身 2819 "La televidilo ne funkcias" / 4482 televidilojn と正用が混在（内部不整合）。
- 対象: 4455（ripari la televidon）/ 同族: 2620, 4171
- 修正型: **televido → televidilo**（機器文脈のみ。1068/1082 "spekti televidon"=放送 は正当）

### 単発の強候補（21件）
| PID | 現行（要点） | 問題（PIV照合） | 修正案 |
|---|---|---|---|
| 374 | Ĉu mi povus **havi vian atenton**? | atento の慣用は doni/turni/dediĉi のみ | "Vian atenton, mi petas!" |
| 190 | Delonge **ni ne vidiĝis** | vidiĝi=「見える」のみ。露 виделись の -ся 移植 | "ni ne intervidiĝis"（Z型: "ni nin ne vidis"） |
| 753 | Ĉu mi **povas havi vian nomon**? | havi nomon=「名を持つ」。字義は相手の名を持つ許可 | "Ĉu vi bonvolus diri al mi vian nomon...?" |
| 769 | **Ĉio estos bone kun vi** | 露 "С вами всё будет хорошо" の二重移植 | "Vi fartos bone." |
| 1559 | Per kio vi **gajnas vian vivon**? | **PIVが明示的に (evitinda) と烙印**（=perlabori 参照） | "Per kio vi vivtenas vin?" |
| 1208 | Ĉu vi **renkontiĝas kun iu**?（交際） | renkontiĝi に恋愛語義なし（PIV/ReVo） | "Ĉu vi havas koramik(in)on?" |
| 1201 | Ni **manĝu ekstere**（外食） | ekstere は屋外のみ。字義は「屋外で食べよう」(+同族2925) | "Ni manĝu en restoracio" |
| 1703 | Ĉu vi estas **komputile klera**? | klera=教養。英 "computer literate" の移植 | "sperta pri komputiloj" |
| 1734 | Ĉu mi **ricevos vojaĝkostojn**? | kosto=支払う額。受け取るのは repago | "Ĉu oni repagos al mi la vojaĝkostojn?" |
| 1764 | Ŝi estos **bonega aldono** al via teamo | aldono=行為・付録。人には不可 | "Ŝi bonege riĉigos vian teamon" |
| 3053 | Ĉu ĝi **venas kun** legomoj? | veni は移動のみ。英 "come with" 句動詞の移植 | "Ĉu ĝi estas servata kun legomoj?" |
| 3568 | Ĉu ĝi **venas kun** instrukcioj? | 同上（店頭の箱入り商品は「来」ない） | "Ĉu instrukcioj estas inkluzivitaj?" |
| 4100 | mi dezirus **havi unu** | 英 prop-word "one" の移植（PIV unu の準代名詞用法外） | "...havi pianon / havi tian" |
| 3788 | mi iros **ien alian** | 副詞 ien に形容詞対格 alian — **非文法** | "mi iros aliloken" |
| 4284 | Mi ŝatus **fari retiron** | 英 "make a withdrawal"。retiro に出金語義なし (+同族4296/4303のretiri) | "Mi ŝatus elpreni monon" |
| 4650 | redukti vian **trinkadon**（飲酒） | trinkado=飲むこと一般。飲酒は drinki（Fundamenta） | "redukti vian drinkadon" |
| 4341 | **deponaĵo**（敷金） | deponaĵo=預けた物。敷金は kaŭcio（Oficiala） | "kaŭcio egala al unu-monata lupago" |
| 4419 | Mi ŝatus **havi traktadon** de la vizaĝo | havi+treatment ＆ traktado=取り扱い・交渉 | "Mi ŝatus vizaĝan haŭtflegadon" |
| 4561 | Mi **sentas min kapturna** | kapturna=めまいを**起こさせる**側 | "Mi havas kapturnon" |
| 4411 | Ĉu vi ŝatus **ion sur ĝi**?（美容室） | 英の省略表現の移植（ĝi の指示も不明） | "...ke mi surmetu ion sur la harojn?" |
| 4708 | Li **havas grandajn dioptriojn** | dioptrio=光学単位。人は所有できない | "Liaj okulvitroj estas tre fortaj" |
| 4871 | Je kioma horo li **estas atendata reveni**? | 英の subject-raising 受動の移植 | "...oni atendas, ke li revenos?" |

## 【グレーリスト】20件（判断材料つき・Codex裁量）
| PID | 連語 | 備考 | 修正案 |
|---|---|---|---|
| 169 | Tiel-tiel | 汎欧州的表現・口語で現用。辞書には不在 | Mezbone |
| 645 | dufoje pripensus | 露列にも дважды あり・組成的に透明 | bone pripensus |
| 1366 | iri al universitato（通学） | Z自身が iradi en lernejon を使用 (+同族1339/1340/1357) | En kiu universitato vi studas? |
| 1739 | vidi ... kiel（みなす） | rigardi kiel がPIV慣用 | rigardas ... kiel |
| 1763 | produkti altkvalitan laboron | 英ビジネス語法 | Ŝia laboro estas konstante altkvalita |
| 2520 | trajno finiĝas ĉi tie | 路線でなく列車が「終わる」 | ĉi tie estas la fina haltejo |
| 2292 | stari en trafikblokiĝo | 露 стоять в пробке の移植 | resti blokita en trafikŝtopiĝo |
| 2966 | doma vino | 英 house wine。3043 は別表現で不整合 | la vino de la domo |
| 2699 | helpon kun via bagaĝo | 英 help with の前置詞移植 | helpon pri via bagaĝo |
| 3439 | estas tro malvaste（服） | 服のきつさは malvasta/premi (+3502/4427は形容詞で正用) | Ĝi estas tro malvasta ĉi tie |
| 3239 | supo finiĝis（品切れ） | 露 закончился の移植 | elĉerpiĝis / ne plu restas |
| 4029 | membro de gimnastikejo | 場所の「会員」 | Mi membras en sportklubo |
| 4010 | Ĉu vi povas naĝi?（技能） | 技能は scipovi が明確 | Ĉu vi scipovas naĝi? |
| 4649 | perdi iom da pezo | 英 lose weight。組成的には可読 | iom maldikiĝi |
| 4399/4688/4689/4731 | **fari rendevuon** ×4 | 英 make an appointment。家族として一括判断可 | **aranĝi rendevuon** |
| 4930 | havi abonon al | 英 have a subscription | Mi abonas ĉi tiun revuon |
| 4986 | pro via tempo kaj konsidero | 英ビジネス定型 (+同族244 "dankas pro via tempo") | Dankon, ke vi dediĉis al mi tempon |

（誤フラグ4件は破棄: kunhavi vidpunkton 492=PIVにZ用例 "kunhavi opinion"・surmeti bandaĝon
767=PIVの第1用例そのもの "surmeti pansaĵon sur vundon" 等）

## 【網羅性批評の結論】（独立エージェントによる監査の監査）
- **全レンズでの被覆は実質完了**: 全ユニーク語は2回人間レビュー済み（R1未カバー語+R2カバー語）、
  全フレーズ精読1回（R3）、正書法・マーカー・鏡像・グレー再審・x-system/ĥ-k 網も完了。
- 批評自身が2つの機械的プローブを実行し追加検証:
  ① 全4,813語の機械的PIV語根照合 → 既知発見を再導出（=R1〜R3の再現率を裏付け）、未報告の
  残渣は2件のみ: **Skajpon**（4874・生ブランド表記の方針問題）、**kmeran**（4537・PIV見出しは
  ĥmero — kmera は形揺れ）
  ② 英露グロス→EO訳語の不整合マイニング → グレー級5件: **deklaracio**（2088/2106/4953・税関
  申告は PIV では deklaro が基本）、**inkludita**（2648・他4文は inkluzivita で不整合）、
  **fragila**（2062 vs 3610 facilrompaj の不整合）、**poŝtejo**（1803 vs poŝtoficejo×3 の不整合）、
  **doktoro**（4504・医師は kuracisto が規範、doktoro は学位）
- **どちらのプローブも minibaro級（forced級）の新発見はゼロ** → 監査は漸近線に到達。
  残りの収穫はグレー級のみと判断。
- 推奨クローズアウト: 上記残渣7件を本書で Codex に引き渡し（済）、以後は打ち止めで良い。

## 追加の小発見（インライン検査・第3ラウンド時）
- **jaĥto / jaĥtklubo**（フレーズ側）vs **jakto**（語彙リスト2155行・PIV主形）— 教材内の形分裂。
  どちらかに統一推奨（PIV主形は jakto、jaĥto は参照形）。
- x-system漏れ 0件・表示用EO列に異常文字なし（クリーン確認）。

---

## Codex第3ラウンド再検証・適用結果（2026-06-10）

ユーザー方針として「エスペラント学習用教材では、正しい範囲内なら表現は多様な方がよい」ことを
優先した。そのため、Claude Code の強候補でも、現代会話として成立しうるものや、辞書上の異形・
口語的表現として許容できるものは一括置換しなかった。採用は、非文法・意味ズレ・PIVで明確に
避けるべき用法・教材内でより標準的な形が強く確立している箇所に限定した。

### 適用した修正（41文）

- PID 190: `Delonge ni ne vidiĝis` → `Delonge ni ne intervidiĝis`
- PID 374: `Ĉu mi povus havi vian atenton?` → `Vian atenton, mi petas!`
- PID 753: `Ĉu mi povas havi vian nomon kaj adreson?` → `Ĉu vi bonvolus diri al mi vian nomon kaj adreson?`
- PID 769: `Ĉio estos bone kun vi` → `Vi fartos bone`
- PID 1201 / 2925: `manĝi ekstere`（外食の意）→ `manĝi eksterhejme`
- PID 1208: `Ĉu vi renkontiĝas kun iu?` → `Ĉu vi havas amrilaton kun iu?`
- PID 1559: `Per kio vi gajnas vian vivon?` → `Per kio vi vivtenas vin?`
- PID 1703: `Ĉu vi estas komputile klera?` → `Ĉu vi estas lerta pri komputiloj?`
- PID 1734: `Ĉu mi ricevos vojaĝkostojn?` → `Ĉu oni repagos al mi la vojaĝkostojn?`
- PID 1764: `Ŝi estos bonega aldono al via programo` → `Ŝi estos tre valora por via programo`
- PID 1841 / 1853 / 1854 / 1855 / 1856: 道案内の無目的語 `Daŭrigu...` → `Iru plu...`
- PID 1968 / 1987 / 2158: `sur aviadilo / sur flugo` → `en aviadilo / por flugo`
- PID 2620 / 4171 / 4455: 機器の `televido` → `televidilo`
- PID 2640 / 2684 / 2704 / 2918: `fari rezervon` 系 → `rezervi` 系
- PID 3013 / 3248 / 3298 / 3334: 飲食・注文の light-verb `havi/havos` → `mendi/preni/manĝi`
- PID 3053 / 3568: `veni kun` → `esti servata kun` / `esti inkluzivita`
- PID 3788: 非文法的な `ien alian` → `aliloken`
- PID 4284: `fari retiron` → `elpreni monon`
- PID 4341: 敷金の `deponaĵo` → `kaŭcio`
- PID 4411: 指示対象不明の `ion sur ĝi` → `Ĉu mi metu ion sur la harojn?`
- PID 4419: `havi traktadon de la vizaĝo` → `haŭtflegadon de la vizaĝo`
- PID 4561: `Mi sentas min kapturna` → `Mi havas kapturnon`
- PID 4650: 飲酒量の `trinkado` → `alkoholtrinkado`
- PID 4708: `havi grandajn dioptriojn` → `bezoni fortajn okulvitrojn`
- PID 4871: `estas atendata reveni` → `oni atendas, ke li revenos`

音声は `RHVoice-test` / `spomenka` で再生成し、旧音声は
`Esperanto例文5000文_収録音声/archived_replaced_audio_20260610_forced_loanwords_round3/`
へ退避した。候補・生成ログ:

- `編集ログ/phrases_audio_replacement_candidates_20260610_forced_loanwords_round3.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round3.csv`
- `編集ログ/audio_alignment_report_20260610_forced_loanwords_round3.md`

### あえて維持した主な候補

- `Ĉu mi povas/povus havi X?` の依頼表現は一括修正しない。`ricevi` の方が標準的な箇所もあるが、
  現代会話として意味が通り、教材内の表現多様性として残せるものは残した。
- `aliĝi al ni/vi` は、組織加入だけでなく「加わる」方向の解釈が可能なため、今回の修正対象外。
- `Kion ni havos por tagmanĝo/deserto?` は家庭内の「何が出るか」の表現として成立しうるため維持。
- `Tiel-tiel`, `dufoje pripensus`, `iri al universitato`, `vidi ... kiel`,
  `produkti altkvalitan laboron`, `doma vino`, `perdi pezon`, `havi abonon` などは、
  教材上の許容範囲または表現多様性として維持。
- `fari rendevuon` は `aranĝi rendevuon` がより辞書的だが、今回は明確な誤りとは扱わず維持。
- 残渣7件のうち `deklaracio`, `inkludita`, `fragila`, `poŝtejo`, `doktoro`, `kmera`, `Skajpon` は、
  いずれも minibaro 級の強制外来語とは判断せず維持。
- `jaĥto / jaĥtklubo` は PIV で `jakto` 参照形として確認できるため、教材内の異形として維持。

### Drive状態メモ

`python3 tools/build_drive_audio_manifest.py` 実行時点では、Drive共有フォルダに新41音声が未アップロードで、
旧41音声が残っている状態だった。そのため `audio_manifest.json` には
`missingDataKeys` 41件と `extraDriveKeys` 41件が記録されている。新41 WAVのDriveアップロード後に、
manifestを再生成する必要がある。

---
---

# 最終検品（2026-06-10・Codex大規模適用後の事後監査）

Codex 適用後のコーパス（変更66文対・未コミット時点）と、未走査だった最後の表面（アプリUI内の
EO表示文字列）を検品した。

## 結果サマリ
- **変更66文対: すべて文法的に健全・PIV準拠・内部整合**。要注意としていた新29トークン
  （kradrostita, fumaĵita, kaporo, vivteni, intervidiĝis, eksterhejme, kaŭcio, tinkturi/tinkturigi
  の使い分け, pesi/pezi, pundo/funto 等）も全て正しい。grilita・fumita・farbi・fari rezervon・
  Daŭrigu は完全に一掃済み。
- **アプリUI: 学習者向けEO表示文字列はゼロ**（6つのStreamlit UI・mobile PWA・manifest を全走査。
  唯一の EO はブランド名 "Esperanto 4択" の言語名で問題なし）→ UI面はクリーン確定。

## 残った指摘 2件（いずれも軽微・Codex向け）

### 1.【中】銀行セクションの retiri カルク取り残し（4284修正の家族未展開）
- ID 4284 は "elpreni monon" に修正済みだが、**同じ At the Bank セクションの3文が旧カルクのまま**:
  - ID 4291: "Mi bezonas formularon por **monretiro**" → "por **monelpreno**"
  - ID 4296: "Ĉu mi povas **retiri** monon de mia kreditkarto ĉi tie?" → "**elpreni** monon"
  - ID 4303: "Mi ŝatus **retiri** 100 pundojn, mi petas" → "**elpreni** 100 pundojn"
- 根拠: PIV2020 の retiri は「引き戻す・撤回する」のみ（110204-110206行）で出金語義なし。
  elpreni は Z 用例で金銭と共起（"li elprenis du denarojn..." 35012行）。現状は同一セクション内で
  2動詞が競合し、**多数派が旧カルク**という中途状態。コーパス全体でこの3行が money-sense retir-
  の全数（emerit- 語根の2件は無関係・触らない）。
- 修正時は3文の音声再収録が必要。4284 は戻さないこと。

### 2.【低】ID 2271 の軽い意味ドリフト（任意）
- 旧 "Kie estas la parkometro?" → 新 "Kie mi pagu por parkumado?" は、訳列（パーキングメーター
  はどこ？）に対し「どこで払えばいい？」へ問いの焦点が移動。実用上は同じ場面で機能するため
  許容範囲だが、厳密に揃えるなら訳列側の調整も選択肢。

## 監査打ち止め宣言
語彙（全4,813トークン×2回）→ 連語（全5,000文）→ 機械プローブ（PIV語根照合・英露グロス
不整合マイニング）→ 修正後検品（66文対）→ UI文字列、の全表面を走査完了。
**minibaro級の未発見残存はない**と判断する。以後の品質向上は、本書のグレーリストと上記2件の
Codex 裁定、および通常の運用レビューに委ねる。

---

## Codex最終検品への裁定・適用結果（2026-06-10）

ユーザー方針として、エスペラント学習用教材では「正しい範囲内なら表現は多様な方がよい」ことを
再確認した。そのため、Claude Code の指摘をそのまま純化方向に寄せるのではなく、次の基準で採否を
分けた。

- 単に PIV に見出しがない・外来語風であるだけなら原則として維持。
- ただし、既に同じ意味領域をより標準的な語へ直したことで、同一セクション内に明確な内部不整合が
  残る場合は修正。
- 訳列との対応を崩す言い換えは避ける。外来語を避ける場合も、場面の焦点を保つ透明表現にする。

### 追加で適用した修正（4文）

- PID 2271: `Kie mi pagu por parkumado?` → `Kie estas la pagmaŝino por parkumado?`
  - 旧 `parkometro` を機械的に戻すのではなく、訳列の「パーキングメーター／駐車料金支払い機」の
    焦点を保つ透明表現へ調整した。`parkuma pagilo` は `pagilo` が主に「支払い手段」に寄るため避けた。
- PID 4291: `Mi bezonas formularon por monretiro` → `Mi bezonas formularon por elpreno de mono`
- PID 4296: `Ĉu mi povas retiri monon de mia kreditkarto ĉi tie?` → `Ĉu mi povas elpreni monon per mia kreditkarto ĉi tie?`
- PID 4303: `Mi ŝatus retiri 100 pundojn, mi petas` → `Mi ŝatus elpreni 100 pundojn, mi petas`
  - `retiri` は「退く・引き下がる・撤回する」側の語義で、出金の語義は手元の PIV/ReVo では確認できない。
    4284 を `elpreni monon` に直した以上、同じ銀行セクションの出金表現は `elpreni/elpreno de mono` に
    揃える方が教材として一貫する。

音声は `RHVoice-test` / `spomenka` で再生成し、root音声とスマホ用音声を同期済み。旧音声は
`Esperanto例文5000文_収録音声/archived_replaced_audio_20260610_forced_loanwords_final_audit/`
へ退避した。候補・生成ログ:

- `編集ログ/phrases_audio_replacement_candidates_20260610_forced_loanwords_final_audit.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_final_audit.csv`
- `編集ログ/audio_alignment_report_20260610_forced_loanwords_final_audit.md`

### 最終Drive状態メモ

`python3 tools/build_drive_audio_manifest.py` を再実行した時点で、Drive fallback は新45音声が未アップロード、
旧45音声が未削除の状態。`npm run validate:mobile-assets` はローカル同梱音声の整合性を確認して
passed だが、Drive fallback については `missingDataKeys` 45件・`extraDriveKeys` 45件の警告が
残る。Driveアップロード後に manifest を再生成すれば解消する。

### Drive最終同期確認（2026-06-10 22:54 JST）

ユーザー側で新45音声のアップロードと旧45音声の削除を完了後、`python3 tools/build_drive_audio_manifest.py`
を再実行した。結果:

- Drive上の例文WAV: 5000件
- mobile data と一致する例文音声: 5000件
- `missingDataKeys`: 0件
- `extraDriveKeys`: 0件
- `npm run validate:mobile-assets`: passed

これにより、ローカル同梱音声だけでなく、Google Drive fallback も整合状態になった。

---
---

# 第5ラウンド（クローズアウト精密プローブ・2026-06-11未明・Codex引き渡し用）

網羅性批評が完了宣言の条件として勧告した2プローブ（偽りの友スイープ・概念訳語一貫性マイニング）
を正式実行し、固有名詞ポリシー監査と最終ミニバッチ検品を併走させた。
結果: **新規 forced級 3件＋graylist 約12件**。批評の勧告どおり、この層にはまだ実りがあった。

## 【強候補】forced級 3件（いずれも一語〜一句の修正・音声再収録各1本）

### R5-1. PID 2184 — "En **kazo** de fajro uzu la ŝtuparon"（Plane/Airport Signs）
- → **"En okazo de fajro..."**（標識用に簡潔なら "Okaze de fajro..."）
- 根拠: PIV2020 kaz/o（51965行）は文法・法律・医学の3語義のみで、一般の「〜の場合」語義なし。
  Z慣用は "en okazo de"（"en okazo de bezono" ^Z, bezon/o 11987行）。falsa amiko 型の語義借用。
  コーパスの okaz- 正用（1311-1313）との内部不整合。

### R5-2. PID 2172 — "**Kriza elirejo**"（Plane/Airport Signs）
- → **"Savelirejo"**
- 根拠: PIVの派生見出し savelirejo（ir/i 配下 45834行）の用例が "savelirejo en teatro,
  **EN AVIADILO**" と、まさにこの空港標識の文脈。**コーパス自身が PID 2744 で Savelirejo を
  正用**（内部不整合）。

### R5-3. PID 3410 — "**Kia grandeco ĝi estas?**"（Shopping）
- → **"Kiun grandecon ĝi havas?"**（または "Kia estas ĝia grandeco?"）
- 根拠: kia-копula構文は主語が述語名詞の実例である必要（"Kia homo li estas?"）。服=grandeco
  というカテゴリエラーで、英 "What size is it?" の語順移植。**同小トピック PID 3449 が正規形**。

## 【graylist medium】1件
- **PID 4934 "fotokabino"** → fotobudo / fotoaŭtomato（eo-wiki記事名）。露 фотокабина の
  鏡像（feni型シグネチャ）。kabin/o はPIV見出しに無し（kabineto のみ）。PIVの公衆ボックスは
  bud/o（telefonbudo）。ReVo確認を Codex に依頼。

## 【graylist low】11件（要点のみ・全て維持も可）
| PID | 項目 | 論点 |
|---|---|---|
| 2483 | Urĝa bremso | 緊急なのは状況であってブレーキではない（英 calque）。sav-/kriz- 系統一なら Krizbremso |
| 2765/2794/2795 | elregistriĝi ×3 | PIVに el- 形なし（チェックアウト）。現代用法としては可。代替 elloĝiĝi。3文一括判断 |
| 2649 | plenan pensionon | PIVのRim.が宿泊費語義を明示的に非推奨。ただし旅行語彙として定着 → KEEP寄り |
| 1701 | pensia programo | programo に制度語義なし。pensia sistemo が和訳（年金制度）に密着。優先度極低 |
| 4058 | tribuno（観客席） | PIVの語義は要人席・演壇のみ。露 трибуна 鏡像。ReVo次第 → KEEP寄り |
| 2551 | Oxford-strato 等ハイブリッド | 同カテゴリの Bond Street / Charing Cross（生表記）と不統一 |
| 2512 | Kings Cross | 正式名は King's（アポストロフィ）— EN列の表記のみの問題 |
| 2593 | Bankoko | PIVは Bangkoko、eo-wikiは Bankoko — **基準同士が矛盾する唯一の都市名**。裁定を Codex に |
| 2443 | Abu-Dabio | PIV・eo-wiki 主形とも Abudabio（ハイフン形はリダイレクトのみ） |
| 860/584 | Emilin / Laŭran | PIV形は Emilio/Laŭro だが現代の女性名 -i/-a 形は学習者に自然 → KEEP推奨・方針記録のみ |
| 2271 | pagmaŝino | PIV・コーパス慣行（bankaŭtomato×3等）とも -aŭtomato。統一なら pagaŭtomato。KEEPも可 |

## 【クリーン確認】（再調査不要の記録）
- **falsaj amikoj 約80語根**: 上記以外すべてPIV語義どおり（akurateco=時間厳守、novelo=短編、
  rezigni=断念、magazeno=PIV語義2、recepto 両語義、poliso、miliardo、konkurso 等すべて正用）。
- **概念訳語の一貫性 36概念**: rezervi 完全統一・elpreni 完全転換（retir- 残存ゼロ）・
  kaŭcio/antaŭpago/garantiaĵo の使い分け正確・kvitanco/monpuno/asekuro/horaro/kajo 等すべて整合。
- **露語ミラー 25語根＋110語幹**: remont/anketo/vokzal/kupe 等の典型露語借用は全て不在または正規。
- **固有名詞 169語**: 方針は驚くほど一貫（国名100%エス化・ランドマーク生表記=eo-wiki記事名準拠・
  **人名は対格が必要な位置でのみエス化するという隠れた文法則**まで観察され、格エラーはゼロ）。
- **最終ミニバッチ4文**: 全てクリーン（elpreno de mono はPIV散文の型・per は意味論的に正しい・
  La rezulto estis egala 自然）。※訂正: "La rezulto estis egala" は PID 4014（3859ではない）。

## 正式クローズアウト
網羅性批評が課した条件（精密ダブレットマイナー実行＋falsaj amikoj スイープ）を満たした。
単語2周・連語1周・機械プローブ2種・語義1周・固有名詞1周・修正後検品2周を完了し、
**残るのは本書のグレーリストの Codex 裁定のみ**。Claude Code 側の発掘ミッションはここで完了。

## Codex第5ラウンド最終裁定・適用結果（2026-06-10）

Claude Code の第5ラウンド提案を、学習教材としての標準性・透明性・意味保持・多様性維持の観点で再判定した。
単にPIV見出しがない、または外来語風であるだけでは修正せず、次のどちらかに当たるものだけを採用した。

- PIV/既存コーパスに、より明確で同じ意味を保つ形がある。
- 現行表現が英露語の構文・語義を強く移しており、初学者に誤った語感を与えやすい。

### 追加で適用した修正（5文）

- PID 2172: `Kriza elirejo` → `Savelirejo`
  - PIVに `savelirejo en teatro, en aviadilo` の用例があり、空港・機内標識として最も透明。PID 2744 既出表現とも一致。
- PID 2184: `En kazo de fajro uzu la ŝtuparon` → `Okaze de fajro uzu la ŝtuparon`
  - 一般の「〜の場合」は `kazo` より `okazo/okaze` が教材として安全。標識文として簡潔な副詞形を採用。
- PID 2483: `Urĝa bremso` → `Krizbremso`
  - `urĝa` 自体は正規語だが、固定設備名としては「緊急時用ブレーキ」を表す `kriz-` 合成の方が誤解が少ない。
- PID 3410: `Kia grandeco ĝi estas?` → `Kiun grandecon ĝi havas?`
  - 服そのものを `grandeco` とする英語式構文を避け、同小トピックの `Kian grandecon havas...` 型に合わせた。
- PID 4934: `Ĉu vi havas fotokabinon?` → `Ĉu vi havas fotobudon?`
  - `kabin/o` は手元PIVで確認できず、露語 `фотокабина` の鏡像に見える。PIV掲載語根 `bud/o` による `fotobudo` は意味が透明。

### 維持した候補

- PID 2765/2794/2795 `elregistriĝi`
  - PIV見出し外でも、`registriĝi` からの規則的派生としてチェックアウト文脈で理解しやすい。`elloĝiĝi` はかえって不自然寄り。
- PID 2649 `plena pensiono`
  - 旅行・宿泊語彙として定着しており、訳列の full board / パンシオン系とも対応するため維持。
- PID 1701 `pensia programo`
  - `pensia sistemo` も可能だが、福利厚生の「制度・プログラム」として意味は保てる。明確な誤りではないため維持。
- PID 4058 `centra tribuno`
  - スポーツ施設の観客席として実例があり、`spektantejo` 等への置換はニュアンスを変えうるため維持。
- PID 2551/2512/2593/2443 の地名・通り名表記
  - 固有名詞は教材内で「国名はエス化、ランドマーク・通り名は実用表記を許容」という方針が概ね通っている。表記統一だけを目的に音声再収録まではしない。
- PID 584/860 `Laŭran` / `Emilin`
  - 対格が必要な位置で人名をエスペラント化しており、文法上問題なし。
- PID 2271 `pagmaŝino por parkumado`
  - `pagaŭtomato` も可能だが、現在形は意味が透明で、駐車料金支払い機として教材上十分に安全。

### 音声・データ反映

追加5文は RHVoice `spomenka` で音声を再生成し、root音声とスマホ用音声を同期した。

- 候補ログ: `編集ログ/phrases_audio_replacement_candidates_20260610_forced_loanwords_round5.csv`
- 生成ログ: `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round5.csv`
- 音声照合レポート: `編集ログ/audio_alignment_report_20260610_forced_loanwords_round5.md`
- 旧root音声退避先: `Esperanto例文5000文_収録音声/archived_replaced_audio_20260610_forced_loanwords_round5/`

`mobile_app/data/sentences.json` は再生成済み。Google Drive fallback は、この時点では新5音声が未アップロード、
旧5音声がDrive側に残るため、`mobile_app/data/audio_manifest.json` では `missingDataKeys=5` / `extraDriveKeys=5`
として記録される。ローカル同梱音声は root / mobile とも5000件で揃っている。

---
---

# 第6ラウンド（文法・自然さレンズ・2026-06-11・Codex引き渡し用）

第5ラウンドまでの「語彙・連語・語義」と相補的な最後の層＝**文法レベルの不自然さ**を全数走査した
（対格・再帰所有詞・時制/アスペクト・冠詞・前置詞・一致・語順・接続詞の8観点 × 全5,000文、
＋esti+分詞110文の専用精査）。検証はPMEG級文法家役スケプティクが過剰フラグを棄却済み。

## 🎯 最大の発見:「, bonvolu」英語pleaseタグ家族（全26文・系統的）

文末に裸の bonvolu/bonvole を英語の ", please" として付加するパターン。PIVの bonvoli は
「Esti tiel bona, ke oni afable konsentas」で全用例が**不定詞補語付き**（聞き手の好意への言及）。
- 宣言文＋bonvolu（"Mi ŝatus koktelon, **bonvolu**"）は、意味上「私はカクテルが欲しい —
  ご親切であれ!」となり破綻。"Ĉu ni povus pagi, **bonvole**?" は副詞が話者側の行為に係り
  「我々が親切にも払う」と逆転。
- **コーパス自身の規範**: ", mi petas" ×134文、"Bonvolu+不定詞" ×128文（隣接文に正用例多数:
  2967 "La samon denove, mi petas" / 3017 "Ni ŝatus mendi antaŭmanĝaĵojn, mi petas"）。
- 修正型: **", bonvolu" → ", mi petas"**（一括置換可能・各文音声再収録）。

全26文の内訳（タイプ別）:
- **A型: 宣言文+bonvolu（明確な欠陥・9文）**: 2978, 2980, 3040, 3091, 3243, 3249, 3311, 4691,
  4768, 4918※ ※Mi ŝatus系
- **B型: 命令文+bonvolu（PMEGが明示的に却下する二重命令・4文）**: 2909 (Sekvu min), 4880
  (Plilaŭtigu), 4881 (Mallaŭtigu), ＋2312（Por 25 frankoj）
- **C型: bonvole疑問文（副詞の係り先逆転・2文）**: 2986, 3105
- **D型: 省略名詞句+bonvolu（弁護可能だが mi petas 規範と不統一・11文）**: 2073 (La sekva,
  bonvolu!), 2106, 2750, 2910, 3030, 3202, 3366, 3553, 4384, 4682
- Codex への提案: A〜C型は修正推奨、D型は「省略不定詞の bonvolu」と読めるため裁量
  （ただし統一の観点では全26文を mi petas に揃えるのが最も簡明）。

## 【defect級】その他の文法欠陥 10件

| PID | 現在 | 問題 | 修正案 |
|---|---|---|---|
| 240 | la plej malmulto, **kion** mi povis fari | 名詞先行詞の後は kiu系（PIV自身のZ用例 "el tiu malmulto, **kiun** mi scias"）＋ "la plej malmulto" 自体が変則 | "la plej malgranda afero, **kiun**..." |
| 3582 | io speciala, **kiun** vi ŝatus vidi | 逆方向の同種エラー: io 先行詞の後は **kio**（PIV ki/o 語義4a明文） | "io speciala, **kion**..." |
| 992 | Li estas **divorciĝinta** | PIVの divorci は (ntr)＝eksedz(in)iĝi で変化動詞。-iĝ 二重付加 | "Li estas **eksedziĝinta**"（または divorcinta） |
| 1528 | Du mil **foje** kvin estas dek mil | 乗算演算子は Fundamento/PIV 全例で **-oble**（"kvinoble sep estas tridek kvin" ^Z） | "**Kvinoble du mil** estas dek mil" 型 |
| 1809 | por **atingi tien** | atingi は (tr) 専用（PIV全用例が直接目的語）。tien と非両立 | "por **alveni** tien" |
| 1726 | Ĉu mi povus ricevi **aliĝilon**?（就職面接） | PIVの aliĝilo は団体・大会への加入申込書のみ。求職応募書類ではない | "**kandidatiĝan formularon**" |
| 2295 | Vi lasis viajn lumojn **ŝaltitajn** | 目的語述語に -n は不可（PIV: "lasu ŝin trankvil**a**" ^Z, "lasu min sol**a**" ^Z） | "...lumojn **ŝaltitaj**" |
| 2377 | **Ne trinku kaj veturu** | 三重カルク: ① ne の作用域は第1動詞のみ（合成的には「飲むな、そして運転せよ」）② 飲酒は drinki ③ 英語慣用の直訳 | "**Ne stiru ebria**"（または "Ne veturu, se vi drinkis"） |
| 4481 | kie mi povas **lasi ripari** mian fotoaparaton | PIV Rim.4 の igi/lasi 区別（lasi=黙認、igi=使役）。英 "have it repaired"/独 lassen の移植 | "kie mi povas **riparigi**..." |
| 4762 | **pakaĵon** da aspirino | PIVの pakaĵo は旅行荷物・発送小包専用 | "**paketon** da aspirino" |

## 【graylist】12件（判断材料つき・Codex裁量）
| PID | 項目 | 論点 |
|---|---|---|
| 286 | resti **plu longe** | plu 自体が「より長く」（PIV語釈 "(pli longatempe)"）— 重複。pli longe / plu resti |
| 936 | **Kia** estas via nacieco? | 同定質問は kio（"Kia estas via nomo?" 型エラー・露語列が出所） |
| 990 | Ĉu vi **edziniĝis**? | -is は「結婚した（出来事）」。EN/JA は状態質問 → "Ĉu vi estas edziniĝinta?"（984 と不統一） |
| 1479 | **Kvarfoje** tri estas dek du | PIV の同一例文は "kvar**oble** tri estas dekdu"（1528より軽度） |
| 4006 | asekurita **por** urĝaj situacioj | PIVの asekuri はリスク補語に全例 **kontraŭ** |
| 4962 | Ĉu kiu giĉeto estas **poŝtrestante**? | poŝtrestante は郵便物に書く副詞表記であり述語にならない（Z） |
| 1718 | labori **laŭvice**（交代勤務） | PIVは skipo（シフト）。laŭvice=順番に |
| 2000 | **Suriru**（無目的語） | suriri は (tr)。"Eniru" / "Suriru la ŝipon" |
| 2249等 | **Turnu** maldekstren ×6文 | turni は (tr)。2243 は正しく turniĝu — 内部不統一（6文家族: 2242/2249/2250/2267/2282/2284） |
| 2466 | **kontraŭi** + 不定詞 | PIVの kontraŭi は名詞/al 補語のみ。"Ĉu vi kontraŭus, se mi..." 型へ |
| 1557 | laboras **sur farmo** | PIVの土地・施設は en farmoj（ただし Z "sur sian bienon" もあり証拠は混在） |
| 922 | la 欠落: **Unuiĝintaj Arabaj Emirlandoj** | 複数形国名は la 付きが規範 |

## 【クリーン確認】（基礎文法の健全性証明・再調査不要）
- **sia/lia 再帰所有詞**: 全文で誤りゼロ（機械＋人間の二重確認）
- **間接話法の時制バックシフト**: ゼロ（ke節は正しく未来形を保持: 1762, 2068, 2560 等）
- **複合時制カルク**: 110文精査で "estis -inta"（過去完了引き写し）・"estas -anta"（進行形
  引き写し）は**ゼロ** — esti+分詞は全て正常な述語形容詞・受動分詞
- 方向対格（sur la gazonon 309 / en la universitaton 396 / en la aviadilon 2011）、
  数量 da、義務の volitivo、se節の未来形、目的語述語の無 -n（551, 594, 2800）等、
  難所はおおむね正確 — **基礎文法の土台は堅牢**。

## 第6ラウンド総括
「不自然なエスペラント表現」の最終層として、**defect級 36文**（bonvolu家族26＋単発10）と
graylist 12件を Codex に引き渡す。これらは外来語ではなく**構文・語法の英語写し**であり、
minibaro 監査の自然な完結編にあたる。修正時はいずれも音声再収録を要する。

## Codex第6ラウンド最終裁定・適用結果（2026-06-11）

Claude Code の第6ラウンド提案を、PIVの語法、PMEG的な文法整理、既存コーパス内の使い分け、
および「正しい範囲内の多様性は残す」という教材方針で再判定した。

結論として、**51文を追加修正**した。内訳は次の通り。

- 文末 `bonvolu/bonvole` pleaseタグ: 26文を `mi petas` に統一。
  - ただし、単独の `Bonvolu`（PID 334）と `Bonvolu + 不定詞` の正用例は維持した。
  - ここは「`bonvolu` という語が誤り」という判断ではなく、文末タグとして量産されている型を教材向けに整理したもの。
- defect級: 10文を修正。
  - `divorciĝinta` → `eksedziĝinta`
  - `atingi tien` → `alveni tien`
  - `aliĝilo` → `kandidatiĝa formularo`
  - 目的語述語の `ŝaltitajn` → `ŝaltitaj`
  - `Ne trinku kaj veturu` → `Ne stiru ebria`
  - `lasi ripari` → `riparigi`
  - `pakaĵo da aspirino` → `paketo da aspirino`
  - `io speciala, kiun` → `io speciala, kion`
  - 乗算表現は `-oble` に統一
  - `la plej malmulto` は `la plej malgranda afero` に自然化
- graylistから採用: 15文を修正。
  - `resti plu longe` → `resti pli longe`
  - `Kia estas via nacieco?` → `Kio estas via nacieco?`
  - 婚姻状態質問を `Ĉu vi estas edziniĝinta?` に修正
  - `labori laŭvice` → `labori laŭ deĵoroj`
  - `suriru` は目的語 `la aviadilon` を補足
  - `Turnu ...` 6文を、既存PID 2243に合わせて `Turniĝu ...` に統一
  - `kontraŭi + 不定詞` を `Ne ĝenas min ...` に自然化
  - `poŝtrestante` を `poŝtrestantaj sendaĵoj` として整理

維持したもの:

- PID 334 `Bonvolu`
  - 短い応答・見出し的な「お願いします」として、教材内の多様性として維持。
- 既存の `Bonvolu + 不定詞` 系
  - PMEG/PIV的にも丁寧な依頼として成立し、既存コーパスでも多数の正用例がある。
- PID 1557 `Li laboras sur farmo`
  - `en farmo` も可能だが、`sur farmo` は農場という場所・敷地で働く表現として許容範囲と判断。
- PID 4006 `Ĉu la jaĥto estas asekurita por urĝaj situacioj?`
  - `asekurita kontraŭ ...` 型も考えられるが、現行文は「緊急時に備えて保険があるか」という意味を保っており、修正で意味が狭まりやすい。

### 音声・データ反映

追加51文は RHVoice `spomenka` で音声を再生成し、root音声とスマホ用音声を同期した。

- 候補ログ: `編集ログ/phrases_audio_replacement_candidates_20260611_grammar_round6.csv`
- 生成ログ: `編集ログ/phrases_audio_replacement_generation_20260611_grammar_round6.csv`
- 音声照合レポート: `編集ログ/audio_alignment_report_20260611_grammar_round6.md`
- 旧root音声退避先: `Esperanto例文5000文_収録音声/archived_replaced_audio_20260611_grammar_round6/`

`mobile_app/data/sentences.json` と `mobile_app/data/audio_manifest.json` は再生成済み。
Drive fallback は、第6ラウンド新51音声のアップロード前で `matchedDataKeys=4949` / `missingDataKeys=51`。
Drive側には第6ラウンド旧51音声と第5ラウンド以前の旧5音声、計56件が `extraDriveKeys` として残る。

---

# 第7ラウンド（定型句・疑問詞・造語法・-um レンズ・2026-06-11）

最後の未走査レンズ4本: 社交定型句の慣用性（185文）・kia/kio/kiom 疑問文census（全44文）・
長複合語の造語法（58種）・-um 派生語の正統性（真の派生 約20種）。

## Claude第7ラウンド調査結果: ほぼ完全クリーン — 確定グレー1件のみ

### 【graylist 中】PID 2074 — "Mi feriumas"
- → **"Mi ferias"** を推奨。PIV2020 の ferio 項（29687行）は **ferii**（"Ĝui ferion"）のみを
  派生し、feriumi は PIV・ReVo とも不在（-um は正規派生で表せない時のための接尾辞であり、
  ferii が既に同義のため -um 形は冗長）。ただし口語では一定の通用があるため、Codex が
  Tekstaro/Monato で実例を確認できれば維持も可。修正時は音声1本。

## Codex第7ラウンド最終裁定・適用結果（2026-06-11）

PID 2074 `Mi feriumas` は**維持**する。

PIV2020 では標準的な見出しとして `ferio` から `ferii`（休暇を楽しむ）が派生しており、
`feriumi` は掲載されていない。この点だけを見れば `Mi ferias` がより辞書的・標準的な言い方である。
ただし、`feriumi` は `ferio` + `-um-` + `-i` による透明な派生で、実際の使用例も確認できる。
「休暇を過ごす／休暇中である」という意味も文脈上明確であり、誤解を招く造語や意味ズレとは言いにくい。

この教材では「正しい範囲内の多様性を残す」方針を優先するため、ここは `Mi ferias` に正規化しない。
標準形だけを教えるなら `Mi ferias` もよいが、現行文は入国審査での簡潔な応答として十分成立する。
したがってCSV・音声・モバイルデータの変更は行わない。

### スケプティク検証で棄却された候補（記録のみ・対応不要）
- 定型句: 228 "Tio estas tre afabla de vi"・2072 "Ĝuu vian restadon!" — 変異の範囲内
- kia 疑問文: 1690 salajro / 4266・4300 kurzo / 1709 kariera celo — **PIV自身の編集例
  "kia estas la ĉimatena temperaturo?" / Z "kia estas via aĝo?" が kia+計測名詞を是認**
- 複合語: 2882 skatolmalfermilo（PIVは elladigilo だが合成として可読）・4172 telekomandilo
  （PIV telekomandi から派生可能）・4711 kontaktlensoj（連結母音無し形も通用）

## クリーン証明（再調査不要）
- **定型句185文**: 全主要定型が正典どおり — "Bonan tagon!"（*Havu bonan tagon を正しく回避）、
  Sanon!（くしゃみ）、Je via sano!（乾杯）、Bonan apetiton!、Gratulon!/Feliĉan X-on! 系列、
  Dankon/Nedankinde、Pardonu 系 — **即席逐語訳による定型置換はゼロ**
- **kia 疑問文44文**: 明確な誤りゼロ（936 は修正済み）
- **長複合語58種**: 不正な分節・語順・不透明な造語ゼロ。連結母音 -o- の挿入/省略は
  PIV流儀と一致（butikoŝtelistoj / telerlavmaŝino / interezprocento 等すべて正格）
- **-um 派生語**: feriumi 以外すべて PIV2020 確立語（akvumi・brakumi・butikumi・foliumi・
  gustumi・literumi・malvarmumo・mezumo・ondumado・panumi・plandumo・tendumi・ventumilo）

## 収量曲線と最終判断
R5: forced 3 + gray 12 → R6: defect 36 + gray 12 → **R7: gray 1**。
収量は明確に枯渇した。語彙(×2)・連語・語義・固有名詞・文法(8観点)・定型句・疑問詞・
造語法・-um の**全レンズを走査完了**。本書をもって発掘フェーズを終了し、
以後は Codex 裁定（特に第6ラウンドの bonvolu 家族26文と defect 10件）に移行すべきである。

---
---

# 第8ラウンド（多様性校正レンズ・2026-06-11）

ユーザー指示「**学習教材として表現の多様性は歓迎**」を校正値として組み込み、(1) 軽動詞構文
331件・(2) 焦点詞 ankaŭ/nur 42文・(3) 比較/配分構文33文の census と、(4) **既存グレーリスト
25項目の多様性再裁定**を実施した。

## 【Codex裁定】エスペラント本文は維持、訳調整2件

### R8-1. PID 1588 — "Mi faras **praktikon**"（Jobs・職業体験）【KEEP】
- Codex裁定: **修正しない**。
- 根拠: `staĝo` / `staĝi` はこの文脈で非常に自然な候補だが、PIVの `praktiko` は
  「理論に対する実践」だけでなく、`komencis mian medicinan praktikon` や `praktiki ... profesion`
  のような実務・職業実践の用法を含む。`Mi faras praktikon` はやや広い表現ではあるが、
  RU `Я прохожу практику`、JA「職業体験」、ZH/KRの実習文脈から大きく外れない。
- 教材方針: 正しい範囲内の表現多様性として維持する。`staĝo` に統一すると自然ではあるが、
  明確な誤り訂正ではなく過度な標準化になりうる。

### R8-2/3. ankaŭ の焦点と訳のズレ（訳調整を採用）
- PID 3241 "Provu **ankaŭ vi** la stekon!" — EOは「あなたも」。PIVの `ankaŭ` 項でも、
  原則として強調語の直前に置くとされるため、EOは維持し、訳側を「あなたも」焦点へ調整した。
- PID 3679 — "Mi ankaŭ bezonas..." 自体は **PIV の ankaŭ 項 Rim. がZ用法として明文是認**
  する自然な形。EOは維持し、日訳だけを「小麦粉も500グラム...」へ調整した。
- ※「Mi ankaŭ ŝatas X」型10文の初期フラグは、上記Z用法是認により**全て棄却**（誤りではない）。

## 【クリーン確認】
- **軽動詞331件**: fari mendon/plendon/servon/paŭzon/interkonsenton、preni lecionojn/
  medikamenton 等、疑った組み合わせはことごとく**PIV本文にコロケーションごと掲載**。
  fari foton・fari halton 等は現代の良質な使用で多様性として維持。
- **nur 20文**: 19/20 で焦点直前配置が正確（残1も許容範囲）。
- **比較・配分33文**: 完全クリーン — pli...ol の格処理（"malamas pli ol mensogulon"）、
  kiel eble plej、la 無し ambaŭ（Zの勧告どおり）、po の配分用法、unu la alian、すべて教科書的。

## 【多様性再裁定】グレーリスト25項目の最終区分け（Codex への正式勧告）

### 多様性保護 → KEEP 確定（22項目・修正不要・再フラグ禁止）
pagmaŝino(2271)・informatiko(1382,1737)・Wi-Fi生表記(2606,3067)・Tvitero/Facebook(4902,4891)・
doma vino(2966)・Bankoko(2593)・Abu-Dabio(2443)・Emilin/Laŭran(860,584)・Oxford-strato(2551)・
jaĥto/jakto・evento(1897,1947)・fari rendevuon(4399,4688,4689,4731)・kia+計測名詞(1690,4266,
4300,1709)・elregistriĝi(2765,2794,2795)・plena pensiono(2649)・tribuno(4058)・mufino(3282)・
bovlingo(4160)・sprajo(4412)・pensia programo(1701)・deklaracio(2088,2106,4953)・
inkludita(2648)・fragila(2062)・poŝtejo(1803)

決定的な再照合の成果（裁定の質を上げた新証拠）:
- **funtoj(2464)**: PIV funt/o Sense 2 が明文で「^Z = pundo」— 通貨 funto はザメンホフ用法。
  既適用の pundoj 修正は「統一」であって誤り訂正ではなかった（差し戻し不要・記録のみ）。
- **jaĥto/jakto**: PIVは**両方を見出し語**に持つ（jaĥt/o「^Z = jakto」+ jakt/o）— 同義形併存。
- **deklaracio**: PIV公式追加語で定義そのものが「Deklaro 1」— 公認同義語。
- **inkludi/inkluzivi**: PIVが相互参照する**公認同義語ペア**。
- **plena pensiono**: PIVのRim.が禁じるのは「宿泊料金」語義のみで、全食付き形態は適法。

### フラグ存続（文法・意味の欠陥 — 多様性では保護されない）
- **turnu 家族×6**（無目的語他動詞 — 2243 turniĝu が規範）→ R6修正適用済み・正当
- **bonvolu A型**（宣言文+bonvolu: 意味破綻）**B型**（二重命令: PMEG明示却下)**C型**（bonvole
  係り先逆転）→ R6修正適用済み・正当
- **bonvolu D型**（省略名詞句型11文）: 本来は多様性保護→KEEPが正裁定だったが、既に mi petas
  へ修正・再収録済みで適用後も完全に自然なため**差し戻し不要**。今後この型を再フラグしないこと。

## 第8ラウンド総括
Claude案をCodex側で再裁定した結果、エスペラント本文の追加修正は0件。
`Mi faras praktikon` は教材上の多様性として維持し、`ankaŭ` の焦点が訳とずれていた2件だけを
訳側で調整した。音声再生成は不要。

---
---

# 第9ラウンド（統語規約 census・2026-06-11）

機械検査可能な統語規約5種の全数走査: 意志の ke節 -u 一致／従属節の時制保持／従属接続詞の形
（antaŭ ol・post kiam 等）／従属節前のコンマ規約／ĉi- 複合語のハイフン。

## 結果: 4規約は完全クリーン・コンマ規約のみ3件

- **意志動詞 + ke + 直説法（-u であるべき所）: 0件** — voli/peti/rekomendi 系の ke節は全て正しく -u
- **従属節の英語式時制落ち（kiam/se節の現在形+主節未来形）: 0件**
- **誤形接続詞（*antaŭ ke / *post ke / *ĝis ke）: 0件**
- **ĉi+副詞のハイフン欠落: 0件**（ĉi-vespere 等すべて正格）
- **コンマ規約**: 候補45件中42件は前置詞+疑問詞の直接疑問文（コンマ不要・正格）。
  真の欠落は3件のみ:

### 【cosmetic】従属 kiam 節のコンマ欠落（コーパス規範は 12:3 でコンマあり）
| PID | 現在 | 修正 |
|---|---|---|
| 2061 | Mi ne ricevis la bagaĝetikedon kiam mi registriĝis | ...bagaĝetikedon**,** kiam... |
| 4544 | Ĉu doloras kiam vi glutas? | Ĉu doloras**,** kiam vi glutas? |
| 4678 | Doloras kiam mi maĉas | Doloras**,** kiam mi maĉas |

**重要: この3件は音声再収録不要**。audioKey のスラグ正規化は句読点を除去するため
（実測: 'Doloras kiam mi maĉas' と 'Doloras, kiam mi maĉas' は同一スラグ）、
CSV修正 + build_mobile_data.py 再実行のみで完結する、本監査で唯一のゼロコスト修正候補。

## 全9ラウンド最終総括
語彙(×2)・連語・語義・固有名詞・文法(8観点)・定型句・疑問詞・造語法・-um・軽動詞・焦点詞・
比較構文・統語規約(5種) — **検査可能な全レイヤーの走査が完了**。第9Rの収量はコンマ3件のみで、
収量曲線は完全にゼロへ漸近した。本書（dossier）をもって発掘活動を最終終了とする。
残作業: Codex 裁定（1588 praktiko→staĝo・3241/3679 訳調整・コンマ3件）と、
多様性保護22項目の「再フラグ禁止」運用のみ。

---
---

# 第10ラウンド（適用後の実現形監査・2026-06-11）

Codex が第5〜第8ラウンドの修正を4コミット（39fbd76 / 6c83b47 / 355cd9e / 01e5a11）で適用・
push 完了したため、**実際にコーパスへ入った「実現形」62文＋訳調整3行**を事後監査した。

## 結果: 実現形は全て健全 — 新たな不自然表現の混入ゼロ

- 62文の実現形は、dossier の提案どおり（bonvolu→mi petas 全26文・turniĝu×6・Savelirejo・
  Okaze de fajro・kaporojn・Kiun grandecon・kion/kiun 対・eksedziĝinta・ŝaltitaj・
  Ne stiru ebria・riparigi・paketon 等）か、**Codex 独自の洗練形**。
- Codex 洗練形の個別検証（spot check 済み・全て正格）:
  - 1528 **"Dumiloble kvin"** — PIV の dekoble・miloble（Z用例 "multigu vin miloble"）と
    同型の正規融合形。2000×5 の語順も原文保持で適切
  - 1718 **"labori laŭ deĵoroj"** — PIV deĵoro（勤務時間帯）による私案 skipo より適切な選択
  - 2466 **"Ne ĝenas min vojaĝi..."** — 私案より自然
  - 4708 **"Li bezonas fortajn okulvitrojn"** — dioptrioj 単位誤用を文ごと再構成（EN "His
    prescription is strong" とは微差あるが眼鏡店文脈で等価・許容）
  - 4934 **fotobudon** — 提案どおり（訳列も フォトブース に同期）
- 訳調整3行は完全に整合: 1301 EN Wayne、3241 は **EN/JA/ZH/KO 全てを「あなたも」焦点に統一**
  （EO維持の最小介入案を採用）、3679 JA「小麦粉も」。
- **Drive 同期完了**: manifest sentence keys = 5000/5000（45キー欠落解消・チェックリスト消化）。
  資産検証パス・テスト69件green・origin/main と完全同期。

## 残オープン項目（Codex 裁定待ち・3グループのみ）
1. PID 1588 "Mi faras praktikon" → staĝon（R8 defect・音声1本）
2. PID 2074 "Mi feriumas" → ferias（R7 graylist・音声1本）
3. コンマ3件 2061/4544/4678（R9・**音声再収録不要のゼロコスト修正**）

## 全10ラウンド・最終クローズ
発掘9ラウンド＋適用後監査1ラウンドをもって、本監査プロジェクトの全工程を終了する。
コーパスは「外来語・カルク・語義・文法・定型句・統語規約」の全層で監査済みとなり、
多様性保護22項目の境界も確定した。以後の品質管理は通常運用に移行する。
