# `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv` エスペラント点検ログ

開始日: 2026-06-07
対象: 5,000 件（PhraseID 156〜）／列 = Esperanto, English, 日本語, 中文, 한국어, Русский язык
方針: ロシア語＝最も信頼できる原文。エス⇄日中韓 が主対応。**意味ズレが明確な箇所のみ**修正。
表現の多様性は許容。怪しいエス表現は **PIV2020 / Glosbe / Reta Vortaro** で確認し、
**明確に確認できたものだけ**修正。確証なきものは「要確認」に留める。「角を矯めて牛を殺さない」。

分類:
- **【修正】** 確認済みの明確な誤り。CSV に適用。
- **【要確認】** 非標準・気になるが、意味は通じ明確な誤りではない（＝原則そのまま）。
- **【許容】** 多様性の範囲内（記録のみ）。

---

## 全体スキャン①: 捏造語（PIV非掲載語根）検出

`/tmp/eo_scan.py` で全5,000文のエス単語形 4,814種を抽出し、PIV2020 の語根
（語根49,550／派生語48,781）と形態解析で照合。**未掲載は 55 語のみ**（＝語根の
捏造はほぼ無いと判断できる良好な状態）。内訳:
- 固有名詞・地名・人名: budapeŝto, sydney, rio, ĵanejro(Janeiro), curie, rockefeller,
  william, smith, garcia, lucy, mumbajo, oxford, tottenham, cannes, charing, court,
  kings, street, cross, emirates, lufthansa, rambla, seasons, paracetamolo …（正当）
- ブランド/URL断片: facebook, com, example, name, excel, big, abu, wi, hm, skajpon(Skype),
  tvitero(Twitter) …（正当）
- 正当な複合語・借用語: retpoŝtadreso, plonĝkostumo(n), luoperiodo, deksesjaraĝe,
  bonuskarton, naĉojn(nachos), smuzion(smoothie), kalzoneon(calzone), kmeran(Khmer) …（正当）
- 誤検出（PIV掲載済をスキャナが取り逃し）: kontribuon←kontribu^3i は PIV掲載・正当。

→ 検査が必要な実候補は3件のみ（下記）。

### 候補の精査結果
- **[4355] `kafeoj` → `kafejoj`** 【修正】
  - 文: "Ĉu estas iuj butikoj aŭ kafeoj proksime de la domo?"（家の近くに店やカフェは？）
  - `kafejo`=カフェ は PIV標準（"Butiko, kie oni trinkas kafon"）。`kafeo` は語として存在しない。
  - EN cafes / JA カフェ / RU кафе と完全一致。明確な綴り誤り → `kafejoj` に修正。意味不変。
- **[3682] `duonduzenon`（"duzeno"=ダース）** 【要確認・修正せず】
  - 文: "Mi ŝatus duonduzenon da ovoj"（卵を半ダース＝6個）。
  - `duzeno`/`dozeno` は NPIV非掲載。エスには公式の「ダース」語が無く `dekduo`(=12) が native。
    ただし `duzeno` は露 дюжина / 独 Dutzend に通じる理解可能な借用で、意味は明確。
  - 意味ズレではないため**そのまま**。標準化したい場合の選択肢のみ付記:「ses ovoj」(6個) 等。
- **[1752] `konstruktivan`（"konstruktiva"=建設的な）** 【要確認・修正せず】
  - 文: "Li akceptas konstruktivan kritikon"（建設的な批判を受け入れる）。
  - PIV標準は `konstrua kritiko`。`konstruktiva` は露 конструктивный 由来の理解可能な
    国際語形で、意味は正確。明確な誤りではないため**そのまま**（改善案: `konstruan`）。

---

## バッチ別 意味・文法点検

（100件ずつ。各バッチ: 行範囲・確認件数・所見を記録）

### バッチ1: 行1–100（PhraseID 156–255 / Basic Sentences: 挨拶・好意・感謝）
- 確認: 100件。**誤りなし（0件）**。すべて自然で正しいエス。
- 良好確認: `semajnfino`(週末), `hejmen`(方向対格), `plenumiĝu`/`realiĝos`(願望・自動詞), 
  `gastamo`, `malavara`, 分裂文 `estas mi, kiu devus danki vin`。

### バッチ2: 行101–200（PhraseID 256–355 / Basic Sentences: 謝罪・指示・短問答）
- 確認: 100件。**誤りなし（0件）**。
- 良好確認: `sur la gazonon`(方向対格), `viciĝi`(並ぶ), `kien`, `lasi vin foriri`, 
  他動詞 `atentu la hundon`, `nome de`, `pardonpeti`。

## 全体スキャン②: 機械的整合チェック（全5,000件）
- x-system 残存（cx/gx等の未変換）: **0**。全ダイアクリティックは正しいUnicode。
- 空白異常（前後空白・二重空白）: **0**。
- エス文中の外来文字 q/w/x/y を含む小文字トークン: **1**（URL内 "example" のみ）。
- 重複EOで日本語訳が異なる: 13組（誤りではない＝同一エス文を別文脈で再利用、訳は同義の範囲）。
  例: "Kiel vi fartas?"→お元気ですか/ご気分はいかが、"Kun plezuro"→喜んで/ぜひそうしたい 等。
  → エス的に問題なし。クイズ上の表示重複は別件（本タスク対象外）。参考記録のみ。

### バッチ3: 行201–300（PhraseID 356–455 / Basic短問答・祝い・言語/意思疎通）
- 確認: 100件。**明確な誤りなし（0件）**。要確認 1件。
- **[420]【要確認・修正せず】** "Mi povas komuniki itale"（伊語でなんとか話せる）。
  `komuniki` は他動詞「伝達する」。自動詞「意思疎通する」は `komunikiĝi` がより標準。
  意味は通じ明確な誤りではないため**そのまま**（改善案: `komunikiĝi itale`）。
- 良好確認: `datreveno`,`diplomiĝo`,`novnaskito`,`stirekzameno`,`literumi`,`Ĥanukon`,
  `regi lingvon`,`ju pli…des pli`,`nenian ideon`, 言語形容詞の省略(`la bengalan`)。

### バッチ4: 行301–400（PhraseID 456–555 / 意思疎通・賛否・情報のやりとり）
- 確認: 100件。**誤りなし（0件）**。
- 良好確認: 述語形容詞 `Kion vi trovas pli interesa`(trovi後は主格＝PMEG準拠), 
  手段副詞 `aviadile/trajne`, `kontraŭdiri`,`vidpunkto`,`junulargastejo`,`duŝiĝi`,`survoje`,
  `sensencaĵo`,`picejo`。
- 参考: [491] "Mi vidas nenian malhelpon"(障害なし)＝RU препятствий と一致。EN objection/JA異論
  とは微差だが エス的に正しく意味ズレではない。

### バッチ5: 行401–500（PhraseID 556–655 / 感情・助けと助言・意見）
- 確認: 100件。**明確な誤りなし（0件）**。
- 観察（修正せず）: [630] "teni la pordon malfermitan"。teni 後の述語は主格 `malfermita` が
  PMEG推奨だが、対格も広く許容され明確な誤りではない → そのまま。
- 良好確認: `cirkaj spektakloj`,`kapturno`,`elĉerpita`,`tekkomputilo`,`flugpersonaro`,
  `malkonsili`,`fieri pri`, 仮定法 `se mi estus vi…`, `proponi ke …iru`(願望)。

### バッチ6: 行501–600（PhraseID 656–755 / 意見・緊急・事故）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `butikumado`,`fajrobrigado`,`haltigu la ŝteliston`,`flari ion brulantan`(分詞対格),
  `traŭmatizita`,`kolizii kun`,`stirpermesilo`,`prioritato`,`asekuri`,`interpretisto`,
  `blovi en …tubon`(方向対格),`informi iun pri`,`konsideri …la plej bona`(述語主格)。
- 参考(修正せず): [732] "ŝildon"=標識。trafiksigno/vojsigno がより精確だが ŝildo(看板/標識板)も
  許容範囲・意味明確。

### バッチ7: 行601–700（PhraseID 756–855 / 応急手当・警察署・自己紹介）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `elartikigis`,`manĝaĵveneniĝo`,`tordis al mi la maleolon`(所有の与格),`poliso`,
  `denunci ŝtelon`,`enrompi en …aŭton`,`suspektindan`,`monpuno`,`kiel atestanton`(同格対格),
  `senkulpa`,`ambasadejo/ambasadoro`,`familinomo`。
- 参考(修正せず): [826] "fotoroboto"(似顔絵/モンタージュ)＝露 фоторобот のカルク。PIV非掲載だが
  foto+roboto で理解可能・原文RUと整合 → そのまま。

### バッチ8: 行701–800（PhraseID 856–955 / 紹介・居住地・年齢国籍宗教）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `vendmanaĝero`,`fianĉo`,`kutimis …fiŝkapti`(過去の習慣),`kunloĝas`,
  `Unuiĝintaj Arabaj Emirlandoj`, 国籍/宗教派生(`usonano`,`aŭstrianino`,`judino`,
  `islamanino`,`hinduistino`),`nacieco`,`aparteni al`, 日付 `la 14-a de junio`。

### バッチ9: 行801–900（PhraseID 956–1055 / 宗教・家族関係・人物描写）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: 分詞形容詞 `fianĉiĝinta/edziniĝinta/divorciĝinta`, `solinfano`,`geavoj/genepoj/nepinoj`,
  `okulvitroj`,`bonŝanculo`,`svelta`,`bukla rufa`,`scivolema`,`ol li`(ol後は主格),
  性一致 `edziniĝis`↔RU замужем。

### バッチ10: 行901–1000（PhraseID 1056–1155 / 好き嫌い・待ち合わせ）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `tempioj`,`bonkondutaj`,`fotografado/ĝardenado/piedirado`,`patkukojn`,`troti`,
  `elteni`,`dombestojn`,`testudon`,`verki novelojn`,`abomeni`,`modprezentado`,
  `sciencfikciaj`,`mensogulon`,`geedziĝon`,`vestiblo`,`kafpaŭzon`。

---

## 中間まとめ（1,000/5,000 = 20% 完了, 2026-06-07）
- **意味点検バッチ1–10（行1–1000, PhraseID 156–1155）: 明確な誤り 0件。**
- 確定修正は全体スキャン由来の **1件のみ**: [4355] `kafeoj→kafejoj`（適用済・git差分1行）。
- 要確認（修正せず）: [3682]duzeno, [1752]konstruktiva, [420]komuniki, [826]fotoroboto, [732]ŝildo。
  いずれも露語カルク/語法の微差で、意味は明確・許容範囲。
- 機械チェック（全5000）: x-system残存0／空白異常0／外来文字混入0。
- 所見: 会話系セクションは極めて高品質。捏造語ほぼ無し。以降の専門トピック
  （食事・旅行・健康・ビジネス等）の希少語に注意して継続。

### バッチ11: 行1001–1100（PhraseID 1156–1255 / 承諾辞退・デート）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `partion de golfo`,`regali per`,`lokon kien iri`,`elpensi`,`vi mankas al mi`(会いたい),
  `enamiĝis al`,`brakumi`,`freneziĝas pro`,`veturigi`,`forveturu`,`lasu min trankvila`,`krom se`。

### バッチ12: 行1101–1200（PhraseID 1256–1355 / 賛辞・結婚・学校）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `ravega`,`hararanĝo`,`nupto/novgeedzoj`, 婚式形容詞(`porcelana/arĝenta/perla/
  korala/rubena/diamanta`),`ŝranketojn`,`gimnastikejon`,`liniilon`,`viŝgumon`,`parkere`,
  `mezumo`,`sonorilo…sonoros`。
- 相互確認: [1341] `deksesjaraĝe`（スキャンで希少語フラグ）＝有効な複合副詞と確認。
- 参考: [1294] "edziniĝos kun mi"。`edziniĝi al` が古典的だが `kun` も広く許容、RU(выйдешь замуж＝
  女性側)と性も整合 → そのまま。

### バッチ13: 行1201–1300（PhraseID 1356–1455 / 大学・学生生活）
- 確認: 100件。**明確な誤りなし（0件）**。学術語彙も的確。
- 良好確認: `klasĉambron`,`kandidatiĝu`,`informatikon`,`magistriĝo/doktoriĝas`,`prelegas`,
  `distancan lernadon`,`stipendiojn`,`specialiĝanta`,`akceptkondiĉoj`,`rektoro`,
  `studentloĝejon`,`estrino de la fako`,`lektoro`,`mezlernejo`,`disertacio`,`oratoro`,`templimo`。

### バッチ14: 行1301–1400（PhraseID 1456–1555 / 数字・色・職業）
- 確認: 100件。**明確な誤りなし（0件）**。
- 数字(0〜miliardo)・四則演算(`egalas/kvarfoje/dividite per/multiplikite per`)・色混合
  (`rozkoloron/helverdan/viola/ĉielarko`) すべて正しい。
- 職業: `juristo`,`veterinaro`,`staĝanta kontisto`,`komercistino`,`vokcentro`,`handikapitaj infanoj`。

### バッチ15: 行1401–1500（PhraseID 1556–1655 / 職業・雇用形態・職場・ビジネス）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `merkatika administranto`,`flegistino`,`superbazaro`,`ekonomikisto`,`memstara laboristo`,
  `senlabora`,`emerita/emeritiĝi`,`dommastrino`,`promociita`,`patrina/patra forpermeso`,
  `maldungita pro redukto de laborfortoj`,`demisiis`,`fakturo`,`altigos salajron`,`ferien`,`limtempo`。
- 参考(修正せず): [1620]`presi` と [1621]`printilo` の併用＝古典形と新語の混在だが双方許容・意味明確。

### バッチ16: 行1501–1600（PhraseID 1656–1755 / 商談・面接・推薦状）
- 確認: 100件。**新規の明確な誤りなし（0件）**（[1752]konstruktiva は既出の要確認）。
- 良好確認: `vizitkarto`,`afervojaĝojn`,`ekspedo`,`negoci`,`vivresumo`(履歴書),`komputile klera`,
  `kvalifikojn`,`provperiodo`,`laŭvice`(シフト),`aliĝilon`,`vojaĝkostojn`,`defion`,`intervjuo`,
  `fortaĵoj kaj malfortaĵoj`,`lojaleco/akurateco`,`laborema`,`ĝustatempe`。

### バッチ17: 行1601–1700（PhraseID 1756–1855 / 推薦状・道を尋ねる/教える）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `rekomendleteron`,`elstaran kontribuon`(スキャン誤検出の確認),`humursento`,`kiudirekte`,
  `apoteko`,`ŝparvojon`,`vidindaĵoj`,`marbordon`,`orientiĝas`, 方向副詞`maldekstren/antaŭen`,
  `kruciĝo`,`Nordo/Sudo/Oriento/Okcidento`,`semaforo`,`aŭtobushaltejo`,`je du paŝoj`(慣用),
  測定対格`kilometron/ducent metrojn/duonkilometron`。

### バッチ18: 行1701–1800（PhraseID 1856–1955 / 観光案内所・遠足）
- 確認: 100件。**明確な誤りなし（0件）**。要確認 1件。
- **[1856]【要確認・修正せず】** "Daŭrigu rekten preter kelkaj semaforoj"。`rekten`(様態副詞rekteへの
  方向対格)は非標準。同ファイル他所(1777/1821/1839/1841)は `rekte`。意味は明確("まっすぐ")のため
  そのまま（一貫させるなら `rekte`）。
- 良好確認: `subpasejon`,`indikilojn`,`eksterlandano`,`flughaveno`,`tendumejojn`,`navedan buson`,
  `gvidatan ekskurson`,`rondvojaĝojn`,`Parlamentejon`,`kartvelan`,`subeksponitaj`,`memorkarto`。

### バッチ19: 行1801–1900（PhraseID 1956–2055 / 航空便予約・搭乗手続き・荷物）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `halto dumvoje`,`kvitancon`,`celloko`,`elirejo/pordego`,`suriru`(搭乗),`enlanda`,
  `senimposta butiko`,`malplenigi`,`demetu`,`likvaĵojn`,`giĉeto`,`rezervonumeron`,`pleton`,
  `elpreni …el ĝia ujo`,`pesi`,`portiston`,`bagaĝetikedo`,`ĉareton`,`manbagaĝojn`,`superpezo`,`taksihaltejo`。
- 参考: `flugkompanio`↔`aviokompanio` の併用＝同義で双方標準。

### バッチ20: 行1901–2000（PhraseID 2056–2155 / 入国審査・税関・機内）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `bagaĝ-ricevejo`,`difektita`,`loĝpermesilo`,`azilon`,`deklaracio`,`transitvizo`,
  `rifuĝinto`,`vojaĝĉekoj`,`enmigradan formularon`,`konsulejon`,`vakcinatestilo`,`reklini`,
  `sekurzonon`,`aŭskultiloj`,`sako por vomado`,`stevardino`,`alteriĝos`,`malŝalti`,`bagaĝujon`,`alteco`。

## 中間まとめ（2,000/5,000 = 40% 完了）
- 意味点検バッチ1–20（PhraseID 156–2155）: **明確な誤り 0件**。
- 確定修正: 1件（[4355]kafeoj→kafejoj, 適用済）。
- 要確認（修正せず・全て理解可能で意味ズレ無し）: duzeno[3682], konstruktiva[1752], komuniki[420],
  fotoroboto[826], ŝildo[732], rekten[1856]。

### バッチ21: 行2001–2100（PhraseID 2156–2255 / 空港標識・レンタカー・運転駐車）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `Forflugoj`,`Necesejo`,`deklarendaj`,`transmision`,`antaŭlumojn`,`benzinujo`,
  `senlima kilometraĵo`,`kasko/ŝoforo`,`centran ŝlosadon`,`kofrujon`,`direktomontrilojn`,
  `klimatizilon`,`viŝilojn`,`kaŭcion`,`rapidlimo/aŭtovojoj`,`parkumi`,`turnu/turniĝu`,
  `trans la ponton`(移動対格) vs `sub la ponto`(位置格) を正しく区別。
- 相互確認: [2225]`luoperiodo`（スキャン希少語フラグ）＝有効な複合語と確認。

### バッチ22: 行2101–2200（PhraseID 2256–2355 / 運転駐車・給油・故障）
- 確認: 100件。**明確な誤りなし（0件）**。※自動車整備の専門語彙＝捏造リスク最高域だが全て的確。
- 良好確認: `stiradan ekzamenon`,`glacikovritaj`,`aŭtoriparejo`,`trafikrondo`,`trafikblokiĝo`,
  `paneis`,`akumulatoro…malŝargiĝis`,`pneŭmatiko krevis`,`mekanikiston`,`hupo`,`radiatoro likas`,
  `kapoton`,`bremslumoj`,`brulaĵindikilo`,`rapidometro`,`stirmekanismo`,`oleopremo`,`bremslikvaĵon`,
  `kontraŭfrostan`,`startokablojn`, `lasis …lumojn ŝaltitajn`(lasi後の述語対格)。
- 参考: `pneŭo`↔`pneŭmatiko` 併用＝双方標準（短縮形）。

### バッチ23: 行2201–2300（PhraseID 2356–2455 / 道路標識・バス/鉄道駅）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `Parkumejo`,`Malrapidiĝu`,`Vojlaboroj`,`Buskoridoro`,`Cedu vojon`,`Nivelkruciĝo`,
  `Piedira transirejo`,`Revenbileto`,`monatan abonon`,`horaron`,`biletaŭtomatoj`,`unuaklasa`,
  `rabatita tarifo`,`pensiulan`,`kajo`,`biletejo`,`ekspresa trajno`,`troplena`,`interspacon`,`atendejo`。

### バッチ24: 行2301–2400（PhraseID 2456–2555 / 鉄道車内・タクシー）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `eksprestrajno`,`vojaĝkarton`,`renovigi …abonbileton`,`skemon de la metroo`,`Urĝa bremso`,
  `vagono/restoracia vagono`,`Laŭpeta haltejo`,`Ejfelturo`,`pakaĵujon`,`apogiĝu`,`alproksimiĝas`,
  `kupeo`,`preterveturis`,`taksimetro`,`restmonon`,`trinkmono`,`ellasu`,`krompago`,`tribunalo`。

### バッチ25: 行2401–2500（PhraseID 2556–2655 / タクシー・船・ホテル設備/予約）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `bankaŭtomato`,`Savringo/Savboato`,`marmalsanon`,`kajuto`,`enŝipiĝos`,`ferdekoj`,`pramo`,
  `savvestojn`,`krozado`,`monŝanĝejo`,`ferdekseĝon`,`radiogramon`,`monŝrankon`,`adaptilon`,
  `lavservo`,`rulseĝan aliron`,`frizejo`,`duŝkabinoj`,`ŝtopilingo/razilo`,`handikapuloj`,`plenan pensionon`。
- 参考: `dombesto`↔`hejmbesto` 併用＝双方標準。

## 中間まとめ（2,500/5,000 = 50% 折り返し）
- 意味点検バッチ1–25（PhraseID 156–2655）: **明確な誤り 0件**。
- 確定修正 1件（[4355]kafeoj→kafejoj）。要確認 6件（全て理解可能・意味ズレ無し）。
- 専門領域（自動車整備・航空・船舶）も含め捏造語ほぼ皆無。プロ品質のデータと評価。

### バッチ26: 行2501–2600（PhraseID 2656–2755 / ホテル予約・チェックイン・滞在中）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `atendoliston`,`longdaŭra restado`,`nefumantoj`,`duoblan ĉambron`,`etaĝo`,`valoraĵojn`,
  `infanliton`,`kusenon`,`gladilon/gladigi`,`ŝargilon`,`makulon`,`savelirejo`,`alergia al polvo`,
  `plilongigi`,`plusendi`。

### バッチ27: 行2601–2700（PhraseID 2756–2855 / ホテル支払/苦情/アパート賃貸）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `lavejo`,`bluzoj`,`elregistriĝi`(⇔registriĝi),`kalkulon`,`servokotizo`,
  `detaligitan fakturon`,`ventumilon`,`televidilo`,`lavujo…ŝtopita`,`brakhorloĝon`,`bolilo`,
  `hejtado`,`ratoj`,`littukojn`,`neakceptebla`,`apartamenton`。

### バッチ28: 行2701–2800（PhraseID 2856–2955 / アパート備品・レストラン予約/飲物注文）
- 確認: 100件。**明確な誤りなし（0件）**。※家庭/台所用品＝捏造リスク高域だが全て透明な複合語/PIV語。
- 良好確認: `vazaro`,`alumetoj`,`balailon`,`tondilon`,`ŝvabrilon`,`rubsakojn`,`detergenton`,`ampolon`,
  `fridujo`,`kuirilo/hejtilo`,`korktirilon`,`skatolmalfermilon/botelmalfermilon`,`suĉkloŝon`(ラバーカップ),
  `adherema filmo`(ラップ),`polvosuĉilon`,`mikroondilo`,`telerlavmaŝino`,`elektromezurilo`,`ĉambristino`,
  `kvarope`,`fumejo`,`cinamo`,`vinkarton`。

### バッチ29: 行2801–2900（PhraseID 2956–3055 / 飲物注文・料理注文）
- 確認: 100件。**明確な誤りなし（0件）**。
- スキャン候補 [2959]`smuzion`(スムージー) = 近年の借用語として許容（露смузи/日スムージー）→ そのまま。
- 良好確認: `Doma vino`,`ĉampano`,`karafon`,`koktelon`,`sojan lakton`,`kranakvo`,`brando/konjakon`,
  `vegetaranino/vegano`,`koŝeran`,`pastaĵojn`,`bifstekon kun fritoj`,`ŝinkan`,`omarojn`,
  `antaŭmanĝaĵojn`,`cepo`,`farĉitajn fungojn`,`ĉefpladon`,`mezrostita`。

### バッチ30: 行2901–3000（PhraseID 3056–3155 / 食事中・支払い・苦情）
- 確認: 100件。**明確な誤りなし（0件）**。
- スキャン候補 [3087]`kalzoneon`(カルツォーネ) = 料理借用語として許容（露кальцоне）→ そのまま。
- 良好確認: `vinagro`,`manĝobastonetojn`,`tritiko`,`legoman kareaĵon`,`kokido`,`rapidmanĝaĵon`,
  `laktaĵoj`,`nuksoj`,`teleron/forko`,`monujon`,`ĉefkuiristo`,`malĝuste sumigita`,`spica/sala`,
  `rostitan meleagron`,`trokuirita`,`odoras je korko`。

## 中間まとめ（3,000/5,000 = 60%）
- 意味点検バッチ1–30（PhraseID 156–3155）: **明確な誤り 0件**。
- 確定修正 1件（[4355]）。要確認 6件（duzeno/konstruktiva/komuniki/fotoroboto/ŝildo/rekten）。
- スキャン候補のうち smuzio/kalzono を文脈で確認＝許容借用語。
- 希少語の多い食事・家庭・交通領域も健全。

### バッチ31: 行3001–3100（PhraseID 3156–3255 / パブ・肉と魚）
- 確認: 100件。**明確な誤りなし（0件）**。※魚介/肉の専門語が密集する捏造リスク最高域だが全て正確なPIV語。
- スキャン候補 [3175]`naĉojn`(ナチョス) = 許容借用語 → そのまま。
- 検証: [3227]`rostbefo` は **PIV見出し語そのもの**（`### rostbef/o`）＝正規形と確認（誤りではない）。
- 良好確認: `soleo`,`kalmaro`,`truto`,`skombro`,`moruo`,`tinuso`,`koturno`,`polpo`,`karpo`,`ŝarko`,
  `haringo`,`kankro`(ザリガニ)⇔`krabo`(カニ),`ansero`,`fazano`,`kuniklo`,`salikoko`,`lumbaĵo`,
  `postebrion`,`laktoskuaĵon`,`marfruktan`。

### バッチ32: 行3101–3200（PhraseID 3256–3355 / 果物・野菜・香辛料・朝食）
- 確認: 100件。**明確な誤りなし（0件）**。※植物/料理語彙が最密集＝捏造リスク最高域。全て正確なPIV語/透明な複合語。
- 良好確認（希少な植物名も的確）: `eruko`(ルッコラ),`mirtelo`(ブルーベリー),`oksikoko`(クランベリー),
  `kapsiko`(唐辛子),`melongeno`(ナス),`kikero`(ひよこ豆),`rafano`(ラディッシュ),`juglando`(クルミ),
  `migdalo`,`safrano`,`koriandro`,`zingibro`,`florbrasiko`,`panumitan`(衣付き),`preferi X al Y`。
- 所見: 捏造語の懸念は本データでは実質的に当たらないことを強く裏付け。

### バッチ33: 行3201–3300（PhraseID 3356–3455 / 朝食・デパート・衣料）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `kolbasojn`,`avenajn biskvitojn`,`ŝorbeton`,`krespojn`,`benjetojn`,`acera siropo`,
  `kazeo`,`kirlovaĵon`(スクランブルエッグ),`senkafeina`,`artefarita dolĉigilo`,`rabatvendo`,`magazeno`,
  `teretaĝo`,`butikoŝtelistoj…juĝe persekutataj`,`surprovi/provejo`,`Ne blankigu`,`kemia purigado`,
  `Lavu inversigite`,`piĵamon`。

### バッチ34: 行3301–3400（PhraseID 3456–3555 / 衣料・靴・装身具・パーソナルケア）
- 確認: 100件。**明確な誤りなし（0件）**。※語彙密集域、全て的確/透明。
- 良好確認: `sablokoloran`(ベージュ),`nuanco`,`kalkanumoj`(ヒール),`pantofloj`,`gumaj botoj`,`koltukon`,
  `felĉapon`,`ŝtrumpetojn`,`ŝelkojn`(サスペンダー),`manumbutonoj`(カフス),`horloĝrimenon`,`juvelaĵon`,
  `fermilo de…kolĉeno`(留め具),`Lipruĝon`,`dentobrosojn`,`paletron da ŝminko por la palpebroj`(アイシャドウ),
  `ungofajlilon`(爪やすり),`akvorezistan ŝminkon por okulharoj`(マスカラ),`vizaĝpudro`。
- 参考: `dentopasto`↔`dentpasto` 併用＝軽微な複合差、双方可。

### バッチ35: 行3401–3500（PhraseID 3556–3655 / パーソナルケア・電子機器・雑貨・スーパー）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `pinĉilon`,`lensokovrilon`,`skanilon`,`pilojn/baterioj`,`laŭtparoliloj`,`muson`,
  `harsekigilon`,`linajn tablotukojn`,`ceramikaĵojn`,`facilrompaj`,`sitelon kaj ŝovelilon`,`bierkruĉojn`,
  `arĝentan manĝilaron`,`vinkarafojn`,`kudrilojn kaj kudran fadenon`,`konstrubriketojn`,
  `mane teksitan tapiŝon`,`taksi`(査定),`bokalon da mustardo`,`limdato`,`bakejo`。
- 参考: `konfitaĵo`↔`marmelado`, `pilo`↔`baterio` 併用＝双方標準。

## 中間まとめ（3,500/5,000 = 70%）
- 意味点検バッチ1–35（PhraseID 156–3655）: **明確な誤り 0件**。確定修正 1件。

### バッチ36: 行3501–3600（PhraseID 3656–3755 / スーパー・書店/花屋・支払/返品）
- 確認: 100件。**明確な誤りなし（0件）**。
- 花・書籍語彙も正確なPIV語: `narcisoj`,`lekantojn`(デイジー),`magnolioj`,`lilioj`,`krizantemojn`,
  `diantoj`(カーネーション),`tulipoj`,`orkideojn`,`bukedo`/`krono`(花冠), `kafgrajnojn`,`konservaĵojn`,
  `frostigitaj nutraĵoj`,`sunflora oleo`,`bastonpanon`(バゲット),`foliumi`,`gvidlibron`,`poemarojn`,
  `koloriglibrojn`,`brokanta librovendejo`(古本),`PIN-kodon`。
- [3682]`duonduzenon`(既出の要確認 duzeno)が本バッチに再出（記録済）。

### バッチ37: 行3601–3700（PhraseID 3756–3855 / 支払/返品・映画・劇場）
- 確認: 100件。**明確な誤りなし（0件）**。
- スキャン候補 [3777]`bonuskarton`(ポイントカード) = 許容複合語 → そのまま。
- 良好確認: `donacskatolon`,`enojn`(円),`donacpaki/envolvi`,`transakcio`,`repagon`(返金),
  `filmo de suspenso`(スリラー),`pufmaizo`(ポップコーン),`intrigo`,`reĝisoro`(監督),`scenaristo`,
  `subtekstojn`,`animaciaĵon`,`nigrablankan`,`opereto`,`dekoraciojn`,`solisto`,`aktorino`。

### バッチ38: 行3701–3800（PhraseID 3856–3955 / 劇場・美術館/博物館・ナイトクラブ）
- 確認: 100件。**明確な誤りなし（0件）**。
- 芸術語彙も的確: `baleton`,`teatran binoklon`(オペラグラス),`vestejo`(クローク),`interakto`(休憩),
  `loĝio`(ボックス席),`operejo`,`scenejo`,`ĝenro`,`fulmilon`(フラッシュ),`vaksaj figuroj`,
  `impresionismajn`,`mozaiko`,`skulptaĵo`,`etnografia`,`plenkreskulan bileton`,`pentraĵgalerion`,
  `vestkodo`,`bilardo`。

### バッチ39: 行3801–3900（PhraseID 3956–4055 / ナイトクラブ・ビーチ・スポーツ）
- 確認: 100件。**明確な誤りなし（0件）**。
- 良好確認: `gastlisto`,`diskĵokeo`,`strando`/`plaĝo`,`sunseĝon`,`akvoskiojn`,`kanuon`,`surfotabulon`,
  `jaĥtklubo`,`aerbotelo`,`ĉevalfortoj`(馬力),`savjakon`,`remiso`(引分),`ludu duope`,`golon/golis`,
  `poentaro`,`kriketon`,`rugbeo`,`vetkuroj`,`flugpilka/manpilka matĉo`,`subtenanto`。スキャン候補
  `plonĝkostumo` も妥当と確認。
- 参考: [4022]`arbitracianto`＝審判。`arbitro` がより慣用だが理解可能・誤りではない。

### バッチ40: 行3901–4000（PhraseID 4056–4155 / スポーツ・音楽・キャンプ）
- 確認: 100件。**明確な誤りなし（0件）**。要確認 1件。
- **[4073]【要確認・修正せず】** "regatto"(レガッタ)。PIV見出しは `### regatt/o`(t重複)だが、PIV本文の
  用例は一貫して `regato`(t単一, 5回以上)＝現代標準形。PIV内部で不一致のため確証なし → そのまま。
- 良好確認: `dirigento`(指揮者),`simfonian orkestron`,`ruldomon`(キャンピングカー),`kukolo`,`pego`(キツツキ),
  `najtingaloj`,`telfero`(ロープウェイ),`femurajn muskolojn`,`golfbastonojn/golfĉaron`,`vetŝancoj`,`ĥoro`。

## 中間まとめ（4,000/5,000 = 80%）
- 意味点検バッチ1–40（PhraseID 156–4155）: **明確な誤り 0件**。確定修正 1件。
- 要確認 累計: duzeno, konstruktiva, komuniki, fotoroboto, ŝildo, rekten, regatto（全て修正せず・意味明確）。

### バッチ41: 行4001–4100（PhraseID 4156–4255 / 家族時間・園芸・来客・銀行）
- 確認: 100件。**明確な誤りなし（0件）**。※農業語彙＝捏造リスク高域だが全て正確なPIV語。
- 良好確認: `erpis`(まぐわ掛け),`plugos`(耕す),`falĉas`(草刈り),`hordeon`(大麦),`sekalon`(ライ麦),
  `rastis…en amason`,`rikolto`,`fruktarbejo`,`kulturplantojn`,`sojfabojn`,`telekomandilon`,
  `sagetojn`(ダーツ),`buŝtukojn`(ナプキン),`manĝoĉambron`,`ĝinon kun toniko`,`satiĝis`。

### バッチ42: 行4101–4200（PhraseID 4256–4355 / 銀行・不動産仲介）
- 確認: 100件。**明確な誤りなし（0件）**。金融語彙も正確なPIV専門語。
- 良好確認: `kurzo`(為替),`provizio`(手数料),`saldon`(残高),`ĝiri`(振込),`hipoteko`(住宅ローン),
  `konteltiron`(明細),`ĉekaron`,`kontantigi`,`interezprocento`,`fremdan valuton`, 不動産:`bangalon`,
  `vicdomon`,`deponaĵo je unu-monata lupago`,`meblitan/nemeblitan`,`novkonstruitan/duamanan`,`prezintervalon`。
- 確認: [4355]は `kafejoj` と表示＝先の確定修正(kafeoj→kafejoj)が正しく反映済。

### バッチ43: 行4201–4300（PhraseID 4356–4455 / 不動産・美容室・仕立て屋・修理）
- 確認: 100件。**明確な誤りなし（0件）**。※美容/仕立ての専門語も全て的確/透明。
- 良好確認: `franĝon`(前髪),`konstantan ondumadon`(パーマ),`kalve`,`farbi…blonde`,`frizaĵon`,
  `bukli la pintojn internen`,`senharigon…per vakso`,`manikuron/pedikuron`,`kojne`(刈り上げ),
  `feni`(ブロー),`ŝampui`,`nuko`(うなじ),`lipharojn/barbon`,`kranihaŭto`(頭皮),`elpluki`,`laki…ungojn`,
  `zipon`,`alkudri`,`fliki…truon`,`laŭmezuran`(オーダーメイド),`maniklongon`(袖丈),`mallarĝigi/plilarĝigi`。

### バッチ44: 行4301–4400（PhraseID 4456–4555 / 修理・医者）
- 確認: 100件。**明確な誤りなし（0件）**。※医療語彙＝捏造リスク高域だが全て正確なPIV語。
- 良好確認: `kapturnon`,`Tusu`,`poleno`(花粉),`antibiotikoj`,`rentgenan ekzamenon`,`analizojn`(検査),
  `sangogrupo`,`sangopremon`(血圧),`insulino`,`ulcero`,`trankviligaĵo`,`recepton`,`desinfekti`,
  `glutas`,`suprenfaldi…manikon`,`vundo`,`fendiĝis`,`plandumojn`(靴底),`krono`(リューズ),`fabrikanto`。

### バッチ45: 行4401–4500（PhraseID 4556–4655 / 病気・治療）
- 確認: 100件。**明確な誤りなし（0件）**。※医療＝捏造リスク最高域だが全て正確なPIV医学語。
- 良好確認: `malvarmumon`,`tuberon`(しこり),`haŭterupcion`(発疹),`furunkon`(おでき),`gripon`,`astmon`,
  `diareon`,`konstipita`,`nazkataron`,`mikozon de la piedoj`(水虫),`limfonodoj`,`suturerojn`(縫合),
  `anestezon`,`urinan specimenon`,`injekton`,`kontaĝa`,`fojnofebro`(花粉症),`sendormeco`,`deprimita`,
  `perturbon`,`diabetulo`,`ellitiĝi`。

## 中間まとめ（4,500/5,000 = 90%）
- 意味点検バッチ1–45（PhraseID 156–4655）: **明確な誤り 0件**。確定修正 1件。

### バッチ46: 行4501–4600（PhraseID 4656–4755 / 治療・歯科・眼科・薬局）
- 確認: 100件。**明確な誤りなし（0件）**。歯科/眼科/薬局の専門語も全て正確なPIV語。
- 良好確認: `po du…piloloj`(配分poの正用), `gingivoj`(歯ぐき),`plombon`(詰め物),`dentprotezon`(入れ歯),
  `absceson`,`kario`(虫歯),`gargari`,`dioptriojn`,`hipermetropa/miopa`(遠視/近視),`astigmatismon`,
  `kontaktlensojn`,`kadrojn`(フレーム),`termometron`,`tablojdoj`,`inhalilon`,`kontraŭdolorilojn`,
  `fastante`(空腹時),`voĉlegi`。

### バッチ47: 行4601–4700（PhraseID 4756–4855 / 薬局・電話・職場の電話）
- 確認: 100件。**明確な誤りなし（0件）**。
- スキャン候補 [4761]`paracetamolo` = 標準的な薬剤借用語 → そのまま。
- 良好確認: `jodo`,`aspirino`,`kromefikojn`(副作用),`dormigiloj`,`nikotinajn plastrojn`,`misdigesto`,
  `dormemigi`,`kapti signalon`,`telefonbudon`,`vokan signalon`(発信音),`vokon pagatan de la ricevanto`
  (コレクトコール),`aŭtomatan respondilon`,`aŭdilon`(受話器),`klavi la numeron`(ダイヤル),`linio…okupata`。

### バッチ48: 行4701–4800（PhraseID 4856–4955 / 職場の電話・マスメディア・郵便局）
- 確認: 100件。**明確な誤りなし（0件）**。
- スキャン候補 `retpoŝtadreso`,`Skajpon`,`Tvitero`,`name@example.com`,`Facebook` = 複合語/商標/URL断片で正当。
- 良好確認: `uzantonomo`,`ensalutu/elsalutu`(ログイン/アウト),`retmesaĝon`,`tajpu…simbolon`,`kanalon`,
  `eldonkvanto`(発行部数),`poŝtkesto`,`vatitan koverton`(クッション封筒),`aerpoŝto`,`afranko`(郵送料),
  `rekomendita poŝto`(書留),`pesilon`(はかり),`fotokabinon`。

### バッチ49: 行4801–4900（PhraseID 4956–5055 / 郵便・手紙・時刻・カレンダー）
- 確認: 100件。**明確な誤りなし（0件）**。
- 手紙の定型句も正確: `Estimata Sinjorino`,`Sincere via`,`Respektplene via`,`Al la koncernatoj`(関係者各位),
  `Antaŭdankon`,`kunsendas…vivresumon`,`aldonaĵon`(添付),`poŝtrestante`(局留)。
- 時刻/暦も正確: `kvarono antaŭ/post`,`tagmezo`/`noktomezo`,`horloĝo malfruas`/`antaŭiras`,
  `vekiĝis`/`enlitiĝas`,`Labortagoj`,`libertago`。

### バッチ50（最終）: 行4901–5000（PhraseID 5056–5155 / 暦・時間表現・天気）
- 確認: 100件。**明確な誤りなし（0件）**。
- 天気の非人称動詞も的確: `Pluvas/Neĝas/Hajlas/Fulmas/Frostas`,`Pluvetadas`(小雨),`Pluvegas`(土砂降り),
  `Ekpluvas`,`fulmotondro`,`veterprognozo`,`atmosfera premo`,`aĉa tago`,`malvarmete`,`nuboj disiĝas`,
  `Antaŭhieraŭ`/`Postmorgaŭ`。

---

# 最終まとめ（全5,000件 = 100% 点検完了, 2026-06-07）

## 結論
**本CSVのエスペラントは極めて高品質。捏造語の懸念は実質的に当たらない。**

## 点検手法（三重）
1. **全体スキャン①（捏造語検出）**: 全エス単語形4,814種をPIV2020語根と形態照合 → 未掲載55語のみ、
   うち実候補3件を精査。固有名詞・借用語・正当な複合語が大半。
2. **全体スキャン②（機械的整合）**: x-system残存0／空白異常0／外来文字混入0。
3. **意味・文法点検（バッチ1–50, 全5,000件）**: 文法・語法・自然さ・意味ズレ・文脈整合を逐一確認。

## 確定修正（CSV適用済, 1件）
- **[PhraseID 4355] `kafeoj` → `kafejoj`**（カフェ）。`kafejo`はPIV標準、`kafeo`は非語。
  EN cafes/JA カフェ/ZH 咖啡馆/KO 카페/RU кафе と完全一致。綴り誤りの明確な確認。意味不変。
  git差分=1行のみ・+1バイト・5000行維持。

## 要確認（修正せず＝全て理解可能・意味ズレ無し。露語カルク/語法の微差）
- [3682] `duzeno`(ダース): NPIV非掲載だが露 дюжина 由来で理解可能（標準は dekduo）。
- [1752] `konstruktiva`(建設的): 標準は `konstrua`。露 конструктивный 由来の国際語形。
- [420] `komuniki`(意思疎通): 自動詞は `komunikiĝi` がより標準。
- [826] `fotoroboto`(モンタージュ): 露 фоторобот のカルク。
- [732] `ŝildo`(標識): `trafiksigno` がより精確。
- [1856] `rekten`(まっすぐ): 様態副詞への方向対格は非標準（他所は `rekte`）。
- [4073] `regatto`(レガッタ): PIV見出しは regatt/o だが本文用例は regato。PIV内部不一致。
- [4022] `arbitracianto`(審判): `arbitro` がより慣用。
- 同義語の併用（誤りではない）: konfitaĵo/marmelado, pilo/baterio, dombesto/hejmbesto,
  plaĝo/strando, flugkompanio/aviokompanio, presi/printilo 等。

## 所見
- 専門領域（自動車整備・航空・船舶・医療・歯科・眼科・農業・植物/料理・金融）の希少語彙が
  すべて正確なPIV語または透明な複合語。捏造の痕跡は皆無。
- ロシア語原文に由来する国際語形カルク（duzeno, konstruktiva, fotoroboto 等）が散見されるが、
  いずれも理解可能で「文脈別許容」の範囲内。学習教材として問題なし。

---

# 要確認8項目の精査と追加修正（2026-06-07・第2ラウンド）

PIV2020（ローカル＝本プロジェクトの基準辞書）を逐語的に引き直し、各項目を再検証。
「自信を持って・意味を変えず・新たな曖昧さを生まない」ものだけ修正。各修正は全列のうち
**エス列のみ**が変わるバイト単位の置換で適用（他言語列はバイト不変）。

## 追加修正（3件・適用済み。CSV差分は計4行＝本3件＋既出 kafejoj）
- **[420] `komuniki` → `komunikiĝi`**（"Mi povas komunikiĝi itale"）。
  PIV `komunik/i` は**他動詞**（ion al iu）。意図は自動詞「意思疎通できる／なんとか通じる」で、
  PIV標準は `komunikiĝi`。RU原文 **изъясняться**（自分の意を伝える＝再帰的）と正確に一致。意味不変。
- **[1856] `rekten` → `rekte`**（"Daŭrigu rekte preter kelkaj semaforoj"）。
  様態副詞 `rekte` への方向対格 `rekten` は非標準。同ファイル他所(1777/1821/1839/1841)は一貫して `rekte`。
  標準形かつ内部一貫性の改善。意味不変・ゼロリスク。
- **[4073] `regatto` → `regato`**（"…en ĉi tiu regato?"）。
  PIV本文は単一t `regato` を11回使用＝現代標準形（生HTML見出しも regat/o）。二重t `regatto` は
  標準・本文用例のいずれとも不一致。学習教材として標準形に正規化。意味不変。

## 修正せず（5件・理由を確定）
- **[4022] `arbitracianto`（審判）= KEEP。【重要な反転】**
  PIVの派生語 **arbitracianto**: 「Tiu, kiu arbitracias: **[Sporto] internacia arbitracianto**」
  ＝PIV自身がスポーツ審判の語として掲載。一方 PIV の **arbitro** は「**arbitreco**＝恣意性
  (eco de io arbitra)」であり**審判ではない**。よって `arbitro` に変えると**重大な誤りを導入**する。
  → そのまま。当初の改善案(arbitro)は誤りだったと訂正。
- **[3682] `duzeno`（半ダース）= KEEP。** PIV native は `dekduo`(12のまとまり)。"duon-dekduon" は不自然、
  "ses ovoj"(6個) は文言変更。`duzeno`(露 дюжина 由来)は理解可能。標準置換が無いため維持。
- **[1752] `konstruktiva`（建設的）= KEEP。** PIV純正案 `konstrua` は第一義が「建築の」で
  "konstrua kritiko" は曖昧化の恐れ。`konstruktiva`(露 конструктивный)は曖昧さを避ける国際語形。
  変更は新たな曖昧さを生むため維持。
- **[826] `fotoroboto`（モンタージュ）= KEEP。** 警察の合成肖像を表す単一の確立EO語は無し。
  記述句に置換すると語調が変わる。理解可能な借用語(露 фоторобот)を維持。
- **[732] `ŝildo`（標識）= KEEP。** 標識板は ŝildo の一種。`trafiksigno/vojsigno` はより精確だが、
  EN/RU は単に "sign/знак" で、過剰特定の恐れ。維持。

## 最終集計
- **確定修正 計4件**: [420]komunikiĝi, [1856]rekte, [4073]regato, [4355]kafejoj。
- **維持(要確認→検証済で維持) 4件**: arbitracianto(PIVで正)・duzeno・konstruktiva・fotoroboto・ŝildo。
  ※ arbitracianto は「PIVで正しい」と確定したため要確認から除外、実質「正」。
- CSV git差分=4行のみ・各行エス列のみ変更・5000行維持。アプリコード非変更。

---

# 修正3文の音声差し替え（RHVoice/spomenka, 2026-06-07）

CSV修正に伴い、3文の収録音声を **RHVoice の spomenka 音声**で作り直した（4355/kafejojは前回実施済）。

## 実施（ローカル・すべて整合）
- `tools/reconcile_phrase_audio_rhvoice.py` を dry-run で候補=**ちょうど3件**と確認後に本実行：
  - 生成（spomenka, 24kHz WAV）: `0265_…komunikigxi…`, `1701_…rekte…`, `3918_…regato`
  - 旧WAVを `Esperanto例文5000文_収録音声/archived_replaced_audio_20260607/` へ退避（kafeojと同居）
  - 監査: `編集ログ/*_20260607_round2.csv` ＋ `audio_alignment_report_20260607_round2.md`
  - 結果: **rows=5000 / exact_wav=5000 / bad_audio=0**
- モバイル音声 `mobile_app/sentence-audio/`：新3WAVをコピー(664)＋旧3WAV削除（計5000維持）。
- `tools/build_mobile_data.py` 再生成：**vocab.json は完全不変**、**sentences.json は該当3件の `eo`/`audioKey` のみ更新**（4355含め全件整合）。
- `validate_mobile_assets.py --quick`：vocab/sentence の data↔root_wav↔mobile_wav は**全件OK**。

## 保留（Google Drive依存・要ユーザー操作）
- `validate_mobile_assets.py` は **ERROR**：`audio_manifest.json`（Drive由来）に新キー4件
  （komunikigxi/rekte/regato/**kafejoj**）が無く、旧キー4件（…/**kafeoj**）が残存。
- **kafejojも欠落**＝前回セッションからの既存保留。マニフェストは `build_drive_audio_manifest.py` が
  **Google Driveのフォルダ（sentence: 1Mz5wgbIEBV-YMDxIwtklx7A4SFdLD53z）から生成**するため、
  **新WAV4件をDriveに上げてからマニフェスト再生成**しないと解消しない（ローカルだけでは不可）。
- デプロイ版アプリは manifest 経由でDrive音声を再生するため、Drive更新までは当該4文の音声が
  旧テキストのまま/未取得になりうる。ローカルのバンドル音声(mobile/sentence-audio)は更新済。

## 訂正：音声ソースの優先順位（Driveは「後段フォールバック」）
`mobile_app/app.js` の `getAudioUrls()` を精読した結果、音声は**ローカル優先**：
- `SENTENCE_AUDIO_BASE = IS_STREAMLIT_COMPONENT ? "./sentence-audio/" : "../Esperanto例文5000文_収録音声/"`
- URL列＝[①ローカル `${base}${audioKey}.wav` → ②(manifestにキーがあれば)Drive]。`useDriveManifest` 既定 false。
→ **①ローカルを両方（mobile/sentence-audio・メイン音声）更新済みなので、修正版音声はローカルから再生される。**
  Driveマニフェストは①が無い時のみ使う**フォールバック**。よって manifest の ERROR は再生を妨げない
  低優先の監査事項（kafejojも以前から同状態）。前回の「Drive必須」という記載は過大評価で訂正する。

---

# 第3ラウンド：複合語カルクの深掘り検証（2026-06-07）

初回スキャンは「語根がPIVにあるか」で判定したため、**有効な語根を非PIV語義で組んだカルク**は素通りしうる、という盲点があった。そこで「PIV見出し語そのものでない＝派生・複合レンマ」を全抽出し、希少な複合語を辞書照合する第3パスを実施。

## ユーザー指摘で確定した新規「要確認」
- **[2618/2780/2798] `minibaro`（ホテルのミニバー, 計3回）= 要確認・修正せず。**
  - PIV: `minibar(o)` 無し。`bar/o` の語義は①障壁系／②圧力単位barのみで**「飲食のバー」の語義無し**（接頭辞 `mini/` 自体はPIV掲載で正当）。Glosbe: `minibaro` ページ無し(404)。ウェブ辞書でも「バー/酒場」は `drinkejo/trinkejo`。
  - ＝露 мини-бар／international "minibar" のカルク（mini+baro）。本データ自身も酒場には `drinkejo`(8回) を使用。
  - **ただし「ホテルのミニバー」を表す確立したPIV単一語が存在せず**、`drinkejo`(=酒場・店) は別概念で置換不可。
    代替案（`trinkŝranko`／`minibufedo` 等）は**いずれも非標準の造語**で、かえって「AIが語を捏造」する事態に。
  - → 「角を矯めて牛を殺さない」「確証なきものは無理に修正せず要確認」に従い**そのまま**。意味は明確（RU原文と一致）。
  - 自動スキャンが取りこぼした理由：頻度3で「≤2」フィルタ外＋`baro`が有効語根のため複合語として正当に見えた。
    ＝「有効語根×非標準語義」のカルクは自動検出が困難で、人手の目視が有効（本件はユーザーの指摘で捕捉）。

## 頻度3〜6帯の複合語・未解決語の総点検
- minibaro 以外に同種カルクは**無し**。当該帯の他の語（alvenas/atendis/bankaŭtomato/benzinejo/
  retpoŝtadreso/studentino/tekkomputilo/revenbileto/servokotizo 等）は全て正当な標準語（粗い分割器の誤検出）。

## 要確認リスト（更新・全て修正せず）
duzeno[3682], konstruktiva[1752], fotoroboto[826], ŝildo[732], **minibaro[2618等]** ＝ いずれも
国際語/露語カルクで理解可能・標準置換が無いか曖昧。arbitracianto[4022] は検証の結果PIVで正＝問題なし。
（komuniki/rekten/regatto は第2ラウンドで修正済。）

---

# 第4ラウンド：2巡目レビュー（観点3＝文法/語法/自然さ/意味ズレ・対RU）2026-06-07

初回が語彙/捏造中心だったため、ロシア語原文との意味整合を主軸に再通読。
- 手動再読: 行1–822（**PhraseID 156–977**）→ 明確な誤り **0件**（420は修正済komunikiĝi確認）。
- **機械検査（全5,000件）：形容詞–名詞の数・格一致** → 真の不一致 **0件**。
  検出66件は全て誤検出（≈55件は前置詞`da`+名詞、残6件は trovi後の目的語述語主格[551]・
  分詞+目的語[1939]・複数主語[2707]・述語+時間対格[3383/3958]・別節述語[3086]）。
  ＝全件で形容詞一致は正しいと系統的に確認。

## 第4ラウンド（2巡目）完了
全5,000件（PhraseID 156–5155）を、対ロシア語原文の意味整合を主軸に、文法・語法・自然さ・
意味ズレ・文脈整合の観点で連続再読し終えた。**追加の明確な誤り＝0件。**
（既出の修正4件＝kafejoj/komunikiĝi/rekte/regato は反映済み確認。要確認語＝
minibaro/duzeno/konstruktiva/fotoroboto/ŝildo は全て理解可能な国際語・露語カルクで標準置換が
無いか曖昧なため維持。arbitracianto は検証の結果PIVで正。）

### 総括（多重検証の結論）
1) 初回 全5,000件 通読（語彙/捏造中心）：0誤り
2) 語根スキャン（全語形 vs PIV）：捏造なし（固有名詞・借用語・正当な複合語のみ）
3) 複合語カルク深掘り（希少複合語＋頻度3–6帯）：minibaro 以外に同種なし
4) 形容詞–名詞 一致 機械検査（全5,000件）：真の不一致0件
5) 2巡目 全5,000件 通読（文法/意味ズレ・対RU）：0誤り
→ **データは専門的に高品質。「AIによる捏造語」懸念はほぼ杞憂。** 修正は確証の取れた4件のみ。

---

# Drive音声フォールバックの完全同期（2026-06-07）
旧Drive例文フォルダがゴミ箱化していたため、所有者が新フォルダ
`1tmb4_k3zRv2JjOmHCNvv5zIbbneeKwYZ`（同名・公開=閲覧者）を作成し全5000WAVをアップロード。
- `tools/build_drive_audio_manifest.py` の sentence folder_id を新フォルダへ張替。
- スクリプト2点を修正：(a) `str.removesuffix`(3.9+)→3.8互換、(b) 1フォルダでも0件だと全体中断
  していた挙動を「その区画は既存マニフェストを温存して続行＋warning」に堅牢化。
- マニフェスト再生成 → `validate_mobile_assets.py` **PASS**（sentence=5000・修正版4キー在・旧4キー消滅）。
- 仕上げ検証：Drive URL から修正版4件をDLしローカルspomenkaと **byte完全一致**。
- 留意：vocab用Driveフォルダ `1YBN5sNxSTHKXh…` も現在0件＝別途破損。今回は既存区画を温存
  （vocab音声はローカル `./audio/` から再生されるため実害なし）。要対応なら例文同様に再アップロード。

---

# 第6ラウンド：修正済み「誤りクラス」の全件再走査（2026-06-07）
直した2クラスについて、他に取りこぼしが無いか全5000件を機械走査：
- **方向の-n誤用（rekten型）**：末尾 -en の全語を抽出 → aliloken/eksterlanden/eksterurben/
  malproksimen/malsupren/ferien 等はすべて**正当な方向の対格**。誤りは [1856] の1件のみ＝修正済で完了。
- **不自然な重子音（regatto型）**：重子音を含む全語を抽出 → 固有名詞か形態素境界の正当な重子音
  （allog/cel+lok/dom+mastr/el+las/lit+tuk/malsek+kostum/sav+vest/tek+komputil/tut+tag/finn-）のみ。
  タイポは [4073] の1件のみ＝修正済で完了。
→ 両クラスとも**他に潜在誤りなし**を確認。

# 点検・修正タスクの最終ステータス
全5,000件を **7手法**で検証完了：①初回通読 ②語根スキャン ③複合語カルク ④形容詞一致機械検査
⑤2巡目通読(対RU) ⑥方向-n走査 ⑦重子音走査。**確定修正は4件のみ**（kafejoj/komunikiĝi/rekte/regato、
全てPIV照合・意味保存）。要確認(維持)：minibaro/duzeno/konstruktiva/fotoroboto/ŝildo。
音声(spomenka)・モバイルデータ・Driveフォールバックまで完全一致で整備済み。データは専門的に高品質。
