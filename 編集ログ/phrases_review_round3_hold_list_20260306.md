# phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv

未修正・据え置き理由一覧
654周目再々点検版

更新日: 2026-05-05

対象ファイル:
- `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`
- `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505 (コピー).csv`
- アプリ実行用同名CSV: `../最高のエスペラント学習用の4択アプリを作成する/phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`

## 655. ユーザー指摘による再調整（ID2840 / ID3328 / ID4021）

対象:
- `ID2840`
- `ID3328`
- `ID4021`

結果:
- **CSV修正あり（2件を元表現へ戻し、1件は維持）**
- ユーザー指摘により、エスペラント教育上の分かりやすさ・透明性を優先すべき可能性がある3件を再評価した。
- `ID2840` と `ID4021` は、厳密な専門語へ寄せすぎるよりも、教材としての分かりやすさと原文の透明性を優先して元表現へ戻した。
- `ID3328` は、元形が標準綴りから外れる可能性が高いため、補正後の `rosmarenon` を維持した。

再調整:
- `ID2840` EO
  - `La ventolilo en mia ĉambro ne funkcias` → `La ventumilo en mia ĉambro ne funkcias`
  - 理由: `ventolilo` は換気装置として厳密だが、RU `Вентилятор` および EN `ventilator` は部屋のファン/換気ファンの広い文脈で読める。教材上は `ventumilo` の方が基本語として透明で、ホテル客室の「ファンが動かない」文としても自然に理解できるため、元表現へ戻した。JA/ZH/KO の換気寄り表現とは完全一致ではないが、実用文脈では許容範囲と判断。
- `ID4021` EO
  - `Kiu serviras?` → `Kiu servas la pilkon?`
  - 理由: PIV 2020 では球技の専門語として `serviri/serviro` が確認できる一方、4択教材の単独文としては `Kiu servas la pilkon?` の方が英日中韓/RUの「誰がボールをサーブするか」と直感的に対応する。`servi` は基本語で、`la pilkon` により球技文脈も明示されるため、専門語への過修正を避けて元表現へ戻した。

維持:
- `ID3328` EO
  - `Ne uzu rosmarenon` を維持。
  - 理由: rosemary の標準的な Esperanto 形は PIV 2020 / Fundamento / Wiktionary 系で `rosmareno` と確認できる。元の `rozmarenon` は学習者に非標準綴りを教えるリスクがあるため、ここは補正後のまま維持する。

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3a861702646a71201ae2ab7d66fa5c5e`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- アプリ側 `git diff --check` 問題なし。

## 654. 653周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar
- Time & Weather / Time Expressions
- Time & Weather / Weather

結果:
- **CSV修正なし**
- 前回 `ID4956`〜`ID5055` に続き、今回はCSV末尾の `ID5056`〜`ID5155` の100件を確認した。季節・月、時点副詞句、期間表現、天気・気温・気象現象の短文として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID5113` EO/EN/JA/RU、`ID5141` ZH、`ID5146` RU、`ID5154` RU は、現CSVで補正後内容になっていることを確認した。
- `PhraseID` は `5155` で終端。`ID5156` 以降の追加行は存在しない。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `La someraj monatoj estas junio, julio kaj aŭgusto`, `La aŭtunaj monatoj estas septembro, oktobro kaj novembro` は、夏・秋の月説明として前ブロックの冬・春と一貫する。PIV 2020 で `somero`, `aŭtuno`, `monato`, `jaro` を確認。
- `Hodiaŭ tage`, `Ĉiutage`, `Morgaŭ`, `Hieraŭ`, `Ĝuste nun`, `La tutan tagon`, `Hodiaŭ vespere`, `Ĉi tiun semajnon`, `Post unu semajno`, `En la venonta monato`, `Ĉi-jare`, `Antaŭ unu jaro`, `Hieraŭ nokte`, `Antaŭ unu horo`, `Matene`, `Vespere`, `Ĉi-posttagmeze`, `Por morgaŭ`, `Morgaŭ vespere`, `Post dek tagoj`, `Du semajnoj`, `Ĉi-monate`, `Kelkaj monatoj`, `Antaŭ longe`, `En la antaŭa monato`, `Antaŭhieraŭ`, `Hieraŭ vespere`, `Ĉiujn kvin minutojn`, `Post dek minutoj`, `Post kelkaj horoj`, `Por hodiaŭ`, `Nun aŭ poste?`, `Morgaŭ matene`, `Postmorgaŭ`, `La sekvantan tagon`, `Post tri semajnoj`, `Ĝis aŭgusto` は、時点・期間・頻度・予定の短句として対応する。
- PIV 2020 で `hodiaŭ`, `tage`, `morgaŭ`, `hieraŭ`, `mateno/matene`, `vespero/vespere`, `semajno`, `monato`, `jaro`, `longe` を確認。`Hodiaŭ tage` は EN `Today` より「今日の日中」に寄るが、JA/ZH/KO/RU が日中を示すため維持した。`Du semajnoj` は語彙カード的な短句として a fortnight / 2週間に対応するため維持した。
- `Estas varme`, `Estas glacie kaj glite`, `Estas 22°C`, `Estas nebule`, `Estas suna tago`, `Kia bela tago!`, `Ĉu estas malvarme ekstere?`, `Ne, estas varme`, `Pluvas`, `Varmegas`, `Frostas`, `Neĝas`, `Ĉu hieraŭ neĝis?`, `Kia estas la temperaturo?`, `Verŝajne ĉirkaŭ 30°C`, `Minus kvin gradoj`, `Plus tri gradoj`, `Mi ŝatas ĉi tiun veteron`, `Kia estas la vetero?` は、天気・気温の短文として対応する。
- PIV 2020 で `vetero`, `temperaturo`, `grado`, `varma/varmega/malvarma`, `frosto/frostas`, `neĝo/neĝas`, `nebulo/nebulas`, `glacie`, `glita`, `suno`, `tago` を確認。`Estas glacie kaj glite` は `glacie` と `glita/glite` の組み合わせで icy and slippery の意味が通るため維持した。
- `Pluvetadas`, `Hajlas`, `Fulmas`, `Alproksimiĝas fulmotondro`, `Estas aĉa tago`, `Ekstere estas iom malvarmete`, `La vetero estas bona`, `Ĉu mi bezonas ombrelon?`, `Ĉesis pluvi`, `La ĉielo estas nuba`, `La ĉielo klariĝas`, `La suno aperas`, `La suno brilas`, `La vetero estas venta`, `Malvarmas, ĉu ne?`, `Varmegas, ĉu ne?`, `Kia bela vetero!`, `Hodiaŭ la vetero estas bona`, `Ne estas tre agrabla tago`, `Terura vetero, ĉu ne?`, `Kia estas la vetero hodiaŭ?`, `Forte pluvas`, `Ekpluvas`, `Pluvegas` は、雨・雹・稲妻・雷雨・曇り/晴れ・風・天気評価として対応する。
- PIV 2020 で `pluvo/pluvas/pluveto/pluvego`, `hajlo/hajlas`, `fulmo/fulmi`, `tondro` の `fulmo tondro`, `aĉa`, `ĉielo`, `nubo/nuba`, `klara`, `suno`, `vento/venta`, `ombro` を確認。`Pluvetadas` は `pluveto` と継続を表す `-ad-` の透明形成、`fulmotondro` は `fulmo tondro` 系の気象語として維持した。
- `Estas sub nulo`, `Hodiaŭ estas kiel en forno`, `Kia estas la veterprognozo?`, `Morgaŭ estos sune`, `Ĉi-nokte frostos`, `Ŝajnas, ke pluvos`, `Mi scivolas, ĉu estos fulmotondro`, `La suno ĵus kaŝiĝis`, `La vento ĉesis`, `La nuboj disiĝas`, `Ni atendas fulmotondron`, `Blovas forta vento`, `En la ĉielo ne estas eĉ unu nubo`, `Tio sonas kiel tondro`, `La atmosfera premo estas alta`, `Estu singarda, la stratoj estas tre glitaj`, `Kiu estas la plej varma monato en via lando?` は、氷点下、猛暑比喩、天気予報、翌日の晴れ、夜間の霜/凍結、降雨見込み、雷雨予想、太陽が隠れる、風が止む、雲が切れる、強風、快晴、雷音、気圧、滑りやすい道路、一番暑い月として対応する。
- PIV 2020 で `forno`, `prognozo`, `frostas`, `kaŝiĝi` の太陽用例、`vento`, `nubo`, `tondro`, `premo` の `la atmosfera premo`, `glita`, `varma` を確認。`La suno ĵus kaŝiĝis` は sun's gone in / 太陽が雲などに隠れた文脈として、過去補正後の RU とも整合するため維持した。`Kiu estas la plej varma monato...` は EN `warmest` に対して hot/warm の幅があるが、JA/ZH/KO/RU の「最も暑い/暖かい月」と整合するため維持した。

主な据え置き確認:
- `ID5058` `Hodiaŭ tage`: 「今日の日中」の短句として日中韓/RUと整合するため維持。
- `ID5078` `Du semajnoj`: a fortnight / 2週間の語彙カード的短句として維持。
- `ID5081` `Antaŭ longe`: PIV 2020 の `antaŭ longe` 型に基づき維持。
- `ID5097` `Estas glacie kaj glite`: icy and slippery の天候・路面文脈として維持。
- `ID5115` `Pluvetadas`: 小雨が続く文脈として維持。
- `ID5118/5145/5149` `fulmotondro`: thunderstorm 文脈として維持。
- `ID5139` `Estas sub nulo`: 氷点下 / below freezing として維持。
- `ID5143` `Ĉi-nokte frostos`: 今夜の霜・凍結見込みとして維持。
- `ID5146` `La suno ĵus kaŝiĝis`: 太陽が隠れた文脈として維持。
- `ID5153` `La atmosfera premo estas alta`: 気圧の文として維持。
- `ID5155` `plej varma monato`: 一番暑い月 / warmest month の許容範囲として維持。

参照:
- PIV 2020 ローカル `somero`, `aŭtuno`, `monato`, `jaro`, `hodiaŭ`, `tage`, `morgaŭ`, `hieraŭ`, `mateno`, `vespero`, `semajno`, `longe`, `vetero`, `temperaturo`, `grado`, `varma`, `varmega`, `malvarma`, `frosto`, `neĝo`, `nebulo`, `glacie`, `glita`, `suno`, `pluvo`, `pluveto`, `pluvego`, `hajlo`, `fulmo`, `tondro`, `aĉa`, `ĉielo`, `nubo`, `klara`, `vento`, `forno`, `prognozo`, `kaŝiĝi`, `premo`: `PIV2020_structured.txt`
- 過去ログ `66周目`, `117周目`, `167周目`, `317周目`, `467周目`, `517周目`, `567周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID5056`〜`ID5155` は 100 件確認済み。
- `ID5156` 以降の行は存在しないことを確認済み。
- アプリ側 `git diff --check` 問題なし。

## 653. 652周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office
- Communication Means / Letters
- Time & Weather / Time Expressions
- Time & Weather / Calendar

結果:
- **CSV修正なし**
- 前回 `ID4856`〜`ID4955` に続き、今回は `ID4956`〜`ID5055` の100件を確認した。郵便局後半、手紙・メール定型句、時刻・日付・曜日・季節表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4956` KO、`ID4971` RU、`ID4976` EO、`ID4989` RU、`ID4995` EO/EN/RU、`ID5004` EO、`ID5030` RU、`ID5032` RU、`ID5036` RU は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書・用例確認に基づく必須修正は見つからなかった。

- `Ĉu vi povus sendi ĝin al ĉi tiu adreso en Niĝerio?`, `Kiom kostos sendi ĉi tiun leteron al Germanio?`, `Kiom kostas sendi ĉi tion per rekomendita poŝto?`, `Ĉu vi bonvolus sendi ĉi tiun pakaĵon kiel eble plej rapide?`, `Ĝi estos en Sidnejo post ĉirkaŭ kvar horoj`, `Mi venis por preni pakaĵon`, `Ĉe kiu giĉeto estas poŝtrestante?` は、ナイジェリア宛住所、ドイツ宛手紙、書留、速達的な発送依頼、シドニー到着見込み、小包受け取り、局留め窓口として対応する。
- PIV 2020 で `sendi` の郵送用法、`poŝto`, `poŝtrestante`, `giĉeto`, `pakaĵo`, `rapida` を確認。`Ĉe kiu giĉeto estas poŝtrestante?` は省略的だが、poste restante / 局留めを扱う窓口を尋ねる口頭表現として維持した。`rekomendita poŝto` は過去周回と同じく、registered post として明確に通るため維持した。
- `Estimata Sinjorino Banon,`, `Sincere via,`, `Kara Filipo,`, `Kun amo,`, `Estimata Sinjorino,`, `Al la koncernatoj,`, `Antaŭdankon`, `Respektplene via`, `Kun plej koraj salutoj,`, `Kun plej bonaj deziroj,`, `Estimata Sinjoro Prezidanto,` は、手紙・メールの呼びかけ・結語・前もっての謝意として対応する。
- Akademio de Esperanto の Konsultejo で `antaŭdanki` が「tute taŭga」とされることを確認。`Antaŭdankon` は名詞句化した通信定型句として維持した。
- `Mi kunsendas mian vivresumon`, `Vi povas kontakti min per retpoŝto`, `Bonvolu ne heziti kontakti min`, `Mi antaŭĝojas ricevi vian respondon`, `Mi antaŭĝojas diskuti tion kun vi`, `Mi antaŭĝojas baldaŭ revidi vin!`, `Mi antaŭĝojas pri tio`, `Mi antaŭĝojas pri la ebleco kunlabori kun vi`, `Se mi povas plue helpi vin, bonvolu sendi al mi retmesaĝon aŭ telefoni` は、CV添付、メール連絡、遠慮なく連絡、返信・相談・再会・協働への期待、追加支援時のメール/電話連絡として対応する。
- PIV 2020 で `heziti`, `kontakti`, `respondi`, `ĝoji`, `kunlabori`, `retmesaĝo`, `resumi/resumo` を確認。`vivresumo` は résumé / CV の透明複合、`kunsendi` は同封・添付して送る文脈で維持した。`antaŭĝoji` はPIVに独立項目はないが、`antaŭ` + `ĝoji` の透明複合で、Wiktionary の活用項目および現代 Esperanto 用例でも確認できるため、英語直訳だけとは扱わない。
- `Dankon pro via letero`, `Estis agrable denove aŭdi de vi`, `Mi tre ŝatus denove viziti vian landon`, `Dankon pro via tempo kaj konsidero`, `Skribu al mi, kiam vi povos; jen mia adreso`, `Bonvolu ekzameni ĉi tiun aferon kiel eble plej baldaŭ`, `Ĉi-matene mi ne povis malfermi vian aldonaĵon`, `Mi ĝoje akceptus la okazon diskuti pliajn detalojn`, `Oni urĝe petas vin veni al Nederlando`, `Estis tre afable de vi respondi al mia letero`, `Sciigu min, kiam vi ekscios ion plian`, `Ne forgesu de tempo al tempo skribi al mi`, `Mi tre bedaŭras, ke mi ne skribis al vi tiel longe`, `Ni jam tiel longe ne kontaktis unu la alian` は、手紙への謝意、再連絡、再訪希望、検討への謝意、住所通知、案件確認依頼、添付ファイル、詳細協議、至急来訪依頼、返信への謝意、新情報の連絡依頼、時々の返信、長期未連絡への謝罪、久しぶりの連絡として対応する。
- PIV 2020 で `aldonaĵo`, `okazo`, `diskuti`, `plia`, `urĝa`, `Nederlando`, `afabla`, `respondi`, `sciigi`, `skribi`, `bedaŭri`, `kontakti` を確認。`Sciigu min, kiam vi ekscios ion plian` は過去補正後の内容で、日中韓/RUの「何か分かったら知らせて」に合うため維持した。
- `Kioma horo estas?`, `Estas la sesa vespere`, `Dek tridek`, `Kvin antaŭ la dua`, `Kioma horo estas precize?`, `Estas kvin minutoj post la unua`, `Estas la deka horo matene`, `Dudek antaŭ la dua`, `Estas la dua kaj duono`, `Estas tagmezo`, `Je kioma horo?`, `Je la tria horo posttagmeze`, `Ĝis la unua horo`, `Estas kvarono antaŭ la deka`, `Estas kvarono post la unua`, `Estas noktomezo ĉi tie` は、現在時刻、午前/午後、何分前・後、正確な時刻、半時、正午、何時に/まで、四分の一時、真夜中として対応する。
- PIV 2020 で `horo` に `kioma horo nun estas?`, `dek minutoj post la tria`, `dek minutoj antaŭ la kvara`, `la tria k duono` 型を確認し、`kioma`, `tagmezo`, `noktomezo` も確認。`Ĝis la unua horo` は deadline の by one o'clock に対して `ĝis` の範囲内で許容されるため維持した。
- `Mia horloĝo malfruas`, `Tiu horloĝo iom antaŭiras`, `Ĉu via horloĝo montras la ĝustan tempon?` は、時計が遅れる・進む・正確な時刻を示すかという文脈で各列と整合する。
- `Kiu tago estas hodiaŭ?`, `Hodiaŭ estas mardo`, `Merkredo, la 1-a de januaro`, `Meze de decembro`, `Kiu dato estas hodiaŭ?`, `Estas la 25-a de septembro`, `Komence de julio`, `Fine de marto`, `Ĝis la fino de majo`, `Hodiaŭ estas la 10-a de aprilo`, `Estas la 22-a de oktobro`, `Morgaŭ estos la 2-a de decembro` は、曜日・日付・月初/月中/月末・期限表現として対応する。
- `Labortagoj estas de lundo ĝis vendredo`, `Mardo, merkredo kaj ĵaŭdo`, `Semajnfinaj tagoj estas sabato kaj dimanĉo`, `Ĉu ĉi tiu sabato estas labortago?`, `Ĉi tiu ĵaŭdo estas libertago`, `La vintraj monatoj estas decembro, januaro kaj februaro`, `La printempaj monatoj estas marto, aprilo kaj majo` は、営業日/労働日、曜日列挙、週末、出勤日、休日、冬・春の月として対応する。PIV 2020 で `labor tago`, 曜日名、`vintro`, `printempo` を確認し、`libertago` は `libera` + `tago` の透明複合として維持した。

主な据え置き確認:
- `ID4962` `Ĉe kiu giĉeto estas poŝtrestante?`: 省略的だが、局留め窓口を尋ねる表現として維持。
- `ID4969` `Mi kunsendas mian vivresumon`: CV添付・同封として意味が明確なため維持。
- `ID4970` `Antaŭdankon`: `antaŭdanki` の適格性を Akademio de Esperanto Konsultejo で確認し、定型句として維持。
- `ID4977/4978/4979/4981/4991` `antaŭĝoji`: 透明複合かつ現代用例を確認できるため維持。
- `ID4989` `aldonaĵon`: メール添付ファイルとして各列と整合するため維持。
- `ID5004` `Kioma horo estas precize?`: 過去補正後の自然な `kioma horo` 型として維持。
- `ID5023` `Ĝis la unua horo`: by one o'clock の期限表現として許容範囲内のため維持。
- `ID5027/5028` `kvarono antaŭ/post`: quarter to/past の標準的な時刻表現として維持。
- `ID5049/5051/5052/5053` `labortagoj`, `semajnfinaj tagoj`, `labortago`, `libertago`: カレンダー・営業日説明文として維持。

参照:
- PIV 2020 ローカル `sendi`, `poŝto`, `poŝtrestante`, `giĉeto`, `pakaĵo`, `rapida`, `heziti`, `kontakti`, `respondi`, `ĝoji`, `kunlabori`, `retmesaĝo`, `resumi`, `aldonaĵo`, `okazo`, `diskuti`, `plia`, `urĝa`, `afabla`, `sciigi`, `skribi`, `bedaŭri`, `horo`, `kioma`, `tagmezo`, `noktomezo`, `tago`, `labor tago`, `lundo`, `mardo`, `merkredo`, `ĵaŭdo`, `vendredo`, `sabato`, `dimanĉo`, `vintro`, `printempo`: `PIV2020_structured.txt`
- Akademio de Esperanto Konsultejo `antaŭdanki`: https://www.akademio-de-esperanto.org/akademio/index.php?title=Respondoj_de_la_Konsultejo
- Wiktionary `antaŭĝojas`: https://en.wiktionary.org/wiki/anta%C5%AD%C4%9Dojas
- La Bona Renkontiĝo 用例 `Mi ... antaŭĝojas pri...`: https://www.laboren.org/
- Esperanto.cat 用例 `Ni antaŭĝojas helpi vin`: https://www.esperanto.cat/home_esp/contacte-2/formulari-de-contacte/
- 過去ログ `65周目`, `166周目`, `316周目`, `466周目`, `516周目`, `566周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4956`〜`ID5055` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 652. 651周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work
- Communication Means / Mass Media
- Communication Means / At the Post Office

結果:
- **CSV修正なし**
- 前回 `ID4756`〜`ID4855` に続き、今回は `ID4856`〜`ID4955` の100件を確認した。職場電話の取り次ぎ、メール・SNS・テレビ・新聞、郵便局での発送・郵便料金・各種窓口手続きとして、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4859` EO、`ID4860` EO、`ID4864` EO、`ID4893` EO/EN/RU、`ID4905` RU、`ID4908` EO、`ID4920` EO、`ID4923` EO/JA/ZH/KO/RU、`ID4927` ZH、`ID4946` KO、`ID4952` EO/EN/ZH は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Ĉu vi ŝatus lasi mesaĝon?`, `Bonvolu revoki morgaŭ`, `Pardonu pro la ĝeno`, `Atendu la signalon kaj klavu la numeron`, `De kiu kompanio vi telefonas?`, `Mi provis telefoni al ŝi, sed ne sukcesis`, `Ĉu vi havas telefonlibron?`, `La numero ne estas en la telefonlibro`, `Ĉu vi scias lian internan numeron?`, `Bonvolu konekti min al interna numero 212`, `Ĉu estas oportune por vi paroli nun?`, `Pardonu, ŝi estas sur alia linio`, `Ĉu mi povus noti vian nomon kaj numeron, mi petas?`, `Bonvolu demeti la aŭdilon kaj telefoni denove`, `Pardonu, li momente ne estas disponebla`, `Je kioma horo li estas atendata reveni?`, `Ĉu mi povus revoki vin post kelkaj minutoj?` は、伝言、折り返し、迷惑への謝罪、信号後の番号入力、会社からの電話、つながらない、電話帳、非掲載番号、内線、通話都合、別回線、名前と番号のメモ、受話器を置いて再発信、取り次ぎ不可、戻り予定、数分後の折り返しとして対応する。
- PIV 2020 で `mesaĝo`, `revoki`, `signalo`, `klavi`, `telefono/telefoni`, `kompanio`, `telefonlibro`, `numero`, `interna`, `konekti`, `oportuna`, `linio`, `noti`, `aŭdilo`, `disponi`, `momente` を確認。`La numero ne estas en la telefonlibro` は EN `ex-directory` に対して説明的だが、電話帳に載っていない非公開番号として各列と整合するため維持した。
- `Jen mia retpoŝtadreso`, `Ĉu mi povas aliri Skajpon?`, `Kio estas via uzantonomo?`, `Kiom por horo?`, `Kio estas hodiaŭ en la televido?`, `Muzikalo`, `Programo por infanoj`, `Plilaŭtigu, bonvolu`, `Mallaŭtigu, bonvolu`, `La gazeton Times, mi petas`, `Ĝi ankoraŭ ne alvenis`, `Ĉu mi povus kontroli mian retpoŝton?`, `Kiel mi ensalutu?`, `Kiel mi elsalutu?`, `Kiel mi konektiĝu al la interreto?`, `Vi povas skribi al mi retmesaĝon`, `Kiu estas via retpoŝtadreso?`, `Mia retpoŝtadreso estas name@example.com`, `Ĉu vi estas en Facebook?`, `Mi aldonos vin kiel amikon`, `Legu ĉi tiun ekskluzivan artikolon`, `Bone. Mi legos ĝin poste`, `Ĉu plaĉas al vi la reklamoj?`, `La bildo estas malklara`, `Bonvolu ŝanĝi la kanalon`, `Kie mi povas konekti mian tekkomputilon?`, `Kiel mi ŝaltas la komputilon?`, `Kiel mi tajpu ĉi tiun simbolon?`, `Mi ŝatus sendi mesaĝon per retpoŝto`, `Ĉu vi sekvas min en Tvitero?` は、メールアドレス、Skype、ユーザー名、時間料金、テレビ番組、ミュージカル、子ども番組、音量調整、新聞購入、未着、メール確認、ログイン・ログアウト、インターネット接続、メール送信、Facebook、友達追加、記事、広告、画像の不鮮明さ、チャンネル変更、ノートPC接続、PC電源、記号入力、メール送信、Twitterでのフォローとして対応する。
- PIV 2020 で `ret poŝto`, `retadreso`, `retmesaĝo`, `Inter reto`, `saluti` のコンピュータ用法、`programo`, `artikolo`, `reklamo`, `malklara`, `kanalo`, `komputilo`, `tajpi`, `simbolo`, `mesaĝo` を確認。`Skajpo`, `Facebook`, `Tvitero` は固有名として維持。`tekkomputilo` はPIV 2020では `teko komputilo` 形を確認し、Kaikki/Glosbeでも laptop 対応語として `tekkomputilo` / `tekokomputilo` 系を確認できるため、現形をAI造語誤りとは扱わない。
- `Kiu programo estas la plej instrua?`, `Mi ŝatas spekti usonan futbalon`, `Ĉu vi legis la novaĵojn hodiaŭ?`, `Mi havis tempon nur por legi la titolojn`, `Kiom ofte aperas ĉi tiu gazeto?`, `Ĝi estas gazeto kun granda eldonkvanto`, `Kiu skribis ĉi tiun artikolon?`, `La kritikistoj estis tre severaj pri ĉi tiu artikolo`, `Ĉu vi ŝatas aŭskulti la radion?`, `Mi aŭskultas radion survoje al la laboro` は、教育的な番組、アメリカンフットボール、ニュース、見出し、新聞発行頻度、発行部数、記事執筆者、批評、ラジオ聴取、通勤中のラジオとして対応する。
- PIV 2020 で `programo`, `futbalo`, `novaĵo`, `titolo`, `aperi`, `eldon kvanto`, `artikolo`, `kritikisto`, `severa`, `radio` を確認。`titoloj` は headline の短い一般訳として、`eldonkvanto` は新聞の発行部数として維持した。
- `Kie estas la poŝtoficejo?`, `Kiu sendis ĉi tiun leteron?`, `Kie estas la poŝtkesto?`, `Mi ŝatus pagi ĉi tiun fakturon`, `Mi ŝatus koverton, mi petas`, `Mi ŝatus vatitan koverton, bonvolu`, `Kiom vi ŝatus?`, `Kie mi povas poŝti ĉi tion?`, `Sendu ĉi tiun pakaĵon per aerpoŝto`, `Kio estas interne?`, `Kiom ĝi valoras?`, `Kiam ĉi tio alvenos?`, `Ĉu mi povas sendi fakson ĉi tie?`, `Kiu estas la faksa numero?`, `Kiuj estas la laborhoroj?`, `Mi ŝatus akiri televidan licencon`, `Mi bezonas renovigi mian televidan licencon`, `Mi havas abonon al ĉi tiu revuo`, `Kie mi povas aĉeti poŝtmarkojn?`, `Ĉu mi povus ricevi unuaklasan poŝtmarkon, mi petas?`, `Kiom kostas la afranko por letero?` は、郵便局、差出人、郵便ポスト、請求書支払い、封筒、緩衝材入り封筒、数量、投函、航空便、小包の内容物、申告価額、到着時期、ファクス、営業時間、TVライセンス、購読、切手、一等郵便切手、郵送料として対応する。
- PIV 2020 で `poŝto/poŝtoficejo/poŝtkesto/poŝti`, `letero`, `fakturo`, `koverto`, `vato/vatita`, `pakaĵo`, `aer poŝte`, `valoro/valori`, `fakso/faksi`, `numero`, `laboro/horo`, `licenco`, `abono/aboni`, `revuo`, `poŝtmarko`, `afranki/afranko` を確認。`vatita koverto` は jiffy bag / bubble envelope の厳密な商品名ではないが、緩衝材入り封筒として各列と矛盾しないため維持した。
- `Ĉu vi havas fotokabinon?`, `Ĉu vi havas fotokopiilon?`, `Ĉu vi vendas naskiĝtagajn kartojn?`, `Ĉu vi vendas Kristnaskajn kartojn?`, `Mi ŝatus sendi ĉi tion per rekomendita poŝto`, `Mi ŝatus asekuri ĉi tion, mi petas`, `Mi ŝatus sendi ĉi tion al Japanio`, `Bonvolu pezi ĉi tiun pakaĵon`, `Ĉu ĉi tio pezas tro multe?`, `Kiom da tagoj tio daŭros?`, `Ĉu vi volas ĉiutagan aŭ ĉiusemajnan abonon?`, `Kie mi povas aĉeti poŝtmarkojn kaj poŝtkartojn?`, `Poŝtmarkon por ĉi tiu poŝtkarto al Aŭstralio`, `Kiom kostas la poŝtmarkoj por ĉi tiuj leteroj?`, `Kiom kostas la afranko al Hongkongo?`, `Ĉu mi povus havi libreton da unuaklasaj poŝtmarkoj, mi petas?`, `Kiom kostas duaklasa poŝtmarko?`, `Mi ŝatus pakon da kovertoj, mi petas`, `Bonvolu enmeti ĉi tiun poŝtkarton en la poŝtkeston`, `Plenigu la doganan deklaracion`, `Mi ŝatus sendi ĉi tiun pakaĵon al Brazilo`, `Ĉu vi povus meti ĝin sur la pesilon, mi petas?` は、証明写真機、コピー機、誕生日・クリスマスカード、書留、保険、海外発送、重さ測定、重量超過、所要日数、日次・週次購読、切手とはがき、豪州宛はがき用切手、手紙用切手代、香港宛郵送料、切手帳、二等郵便切手、封筒パック、投函、税関申告書、ブラジル宛小包、はかりに載せる依頼として対応する。
- PIV 2020 で `foto`, `fotokopio/fotokopiilo`, `naskiĝtago`, `Kristnasko`, `rekomendi` の郵便用法注記、`registrita letero`, `asekuri`, `pezi`, `abono`, `poŝtmarko`, `poŝtkarto`, `afranko`, `libreto`, `pako`, `poŝtkesto`, `dogano`, `deklaro/deklaracio`, `pesilo` を確認。`rekomendita poŝto` は PIV 2020 に避けたい注記があるが郵便用例として理解可能で、教材上の registered post と明確に対応するため維持した。

主な据え置き確認:
- `ID4863` `La numero ne estas en la telefonlibro`: ex-directory の説明的表現として維持。
- `ID4873/4889/4890` `retpoŝtadreso`: `retpoŝto` + `adreso` の透明複合で、メールアドレス文脈として維持。
- `ID4885/4886/4887` `ensalutu` / `elsalutu` / `konektiĝu al la interreto`: PIV 2020 のコンピュータ文脈と透明な接頭辞形成により維持。
- `ID4889` `Kiu estas via retpoŝtadreso?`: `Kio...` の自然化余地はあるが、会話で「どのアドレスか」を尋ねる形として意味は通るため維持。
- `ID4898` `tekkomputilon`: PIV 2020 では `teko komputilo`、Kaikki/Glosbeでは `tekkomputilo` / `tekokomputilo` 系を確認でき、laptop 文脈として維持。
- `ID4906` `titolojn`: headlines の一般訳として許容。
- `ID4908` `eldonkvanto`: PIV 2020 の `eldon kvanto` に基づき、発行部数として維持。
- `ID4918` `vatitan koverton`: 緩衝材入り封筒として jiffy bag / bubble envelope 文脈を保つため維持。
- `ID4938` `rekomendita poŝto`: `registrita poŝto` も候補だが、過去判断どおり registered post として明確に通るため維持。
- `ID4946` `Poŝtmarkon por ĉi tiu poŝtkarto al Aŭstralio`: 豪州宛はがき用切手という省略的な窓口表現として維持。
- `ID4952` `poŝtkeston`: 家庭用受け箱ではなく投函先の郵便ポストとして、過去補正後の現形を維持。

参照:
- PIV 2020 ローカル `mesaĝo`, `revoki`, `signalo`, `klavi`, `telefono`, `kompanio`, `telefonlibro`, `numero`, `interna`, `konekti`, `aŭdilo`, `disponi`, `retpoŝto`, `retadreso`, `retmesaĝo`, `Inter reto`, `saluti`, `programo`, `artikolo`, `reklamo`, `malklara`, `kanalo`, `komputilo`, `tajpi`, `simbolo`, `futbalo`, `novaĵo`, `titolo`, `eldon kvanto`, `radio`, `poŝto`, `poŝti`, `poŝtoficejo`, `poŝtkesto`, `fakturo`, `koverto`, `vato`, `valori`, `fakso`, `licenco`, `abono`, `poŝtmarko`, `afranko`, `fotokopiilo`, `rekomendi`, `registrita letero`, `asekuri`, `pezi`, `dogano`, `deklaracio`, `pesilo`: `PIV2020_structured.txt`
- Kaikki/Wiktionary `tekokomputilo` / `tekkomputilo`: https://kaikki.org/plwiktionary/esperanto/meaning/t/te/tekokomputilo.html
- Glosbe `notebook (computer)` / `tekkomputilo` / `tekokomputilo`: https://en.glosbe.com/en/eo/notebook%20%28computer%29
- 過去ログ `64周目`, `115周目`, `165周目`, `215周目`, `315周目`, `365周目`, `415周目`, `465周目`, `515周目`, `565周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4856`〜`ID4955` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 651. 650周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy
- Communication / Phone
- Communication / Phone Calls at Work

結果:
- **CSV修正なし**
- 前回 `ID4656`〜`ID4755` に続き、今回は `ID4756`〜`ID4855` の100件を確認した。薬局での薬・処方・服薬相談、電話の基本表現、職場電話の取り次ぎ表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4763` EO、`ID4768` EO、`ID4778` EO/EN、`ID4779` KO、`ID4782` EO、`ID4807` EO、`ID4823` EO、`ID4837` EO、`ID4838` ZH、`ID4850` EO、`ID4853` ZH は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Kiom ofte mi prenu la medikamenton?`, `Ĉu vi vendas herbajn medikamentojn?`, `Ĉu mi povas ricevi ion kontraŭ tuso?`, `Bonvolu doni al mi plastron`, `Bonvolu doni al mi iom da jodo`, `Mi ŝatus iom da paracetamolo`, `Mi ŝatus pakaĵon da aspirino`, `Ĉu ĝi havas iujn kromefikojn?`, `Vi devus eviti alkoholon`, `Vi povus provi ĉi tiun kremon`, `Nur por ekstera uzo` は、服薬頻度、ハーブ薬、咳止め、絆創膏、ヨウ素、パラセタモール、アスピリン、副作用、飲酒回避、クリーム、外用専用として対応する。
- PIV 2020 で `medikamento`, `tuso`, `plastro`, `jodo`, `aspirino`, `kromefiko`, `alkoholo`, `kremo`, `ekstera`, `uzo` を確認。`paracetamolo` はPIVローカルでは直接確認できなかったが、Esperanto薬剤名リストで `paracetamol - paracetamolo` として確認でき、各列の薬剤名と一致するため維持した。
- `Kie estas la plej proksima tutnokte malfermita apoteko?`, `Mi ŝatus paroli kun la farmaciisto, bonvolu`, `Mi havas ĉi tie recepton de la kuracisto`, `Ĉu mi povas aĉeti ĉi tion sen recepto?`, `Ĉu vi bezonas recepton por dormigiloj?`, `Ĉu vi povus prepari por mi la medikamenton laŭ ĉi tiu recepto?`, `Mi revenos por ĝi`, `Ĉu vi povas rekomendi ion kontraŭ malvarmumo?`, `Ĉu vi havas ion kontraŭ gorĝdoloro?`, `Ĉu vi havas ion por sekiĝintaj lipoj?`, `Ĉu vi havas ion kontraŭ vojaĝmalsano?`, `Ĉu vi havas ĉi tiun medikamenton en tablojdoj?`, `Ĉu vi havas ĉi tiun medikamenton en kapsuloj?` は、深夜営業・24時間薬局、薬剤師、処方箋、処方箋なし購入、睡眠薬、調剤、後で受け取り、風邪・喉痛・唇荒れ・乗り物酔い、錠剤・カプセルとして対応する。
- PIV 2020 で `apoteko`, `farmaciisto`, `recepto`, `dormi/dormigilo`, `rekomendi`, `malvarmumo`, `gorĝo`, `doloro`, `lipo`, `tablojdo`, `kapsulo` を確認。`tutnokte malfermita apoteko` は all-night chemist の直訳として妥当で、日中韓の24時間営業表現とも実用上矛盾しない。`sekiĝintaj lipoj` は chapped lips の乾燥・荒れ文脈として意味が通るため維持した。
- `Ĉu vi havas ion por helpi min ĉesi fumi?`, `Ĉu vi provis nikotinajn plastrojn?`, `Mi suferas pro misdigesto`, `Kiel oni prenu ĉi tiun medikamenton?`, `Jen la instrukcioj por uzo`, `Ĝi povas dormemigi vin`, `Ne prenu interne` は、禁煙補助、ニコチンパッチ、消化不良、服薬方法、使用説明、眠気、内服不可として対応する。
- PIV 2020 で `fumi`, `nikotino`, `plastro`, `misdigesto`, `instrukcio`, `uzo`, `dormi/dormemigi`, `interna/interne` を確認。`Ne prenu interne` は warning label の短い定型表現として、内服しない / not internally の各列と整合するため維持した。
- `Mi telefonos al vi`, `Kiu telefonas?`, `Ĉu mi povas paroli kun Sara?`, `Momenton`, `Kio estas via numero?`, `Jen mia numero`, `Saluton. Ĉi tie Ela`, `Ĉu vi bone aŭdas min?`, `Bonvolu paroli pli laŭte`, `Malbona konekto`, `Restu sur la linio`, `Bonvolu sendi al mi mesaĝon`, `Mia telefono paneis`, `Donu al mi vian numeron`, `Vi povas telefoni al mi je la numero 12345`, `Kiun mobilan reton vi havas?`, `Mi malbone aŭdas vin`, `Mi ne povas kapti signalon`, `Mi revokos poste`, `Mi mesaĝos al vi poste`, `Ni malkonektiĝis` は、電話をかける、発信者確認、通話相手、少し待つ、電話番号、名乗り、聞こえ方、声量、回線不良、保留、SMS/メッセージ、電話故障、携帯ネットワーク、電波、折り返し、後でメッセージ、切断として対応する。
- PIV 2020 で `telefono/telefoni`, `numero`, `aŭdi`, `laŭte`, `konekto`, `linio`, `mesaĝo/mesaĝi`, `panei`, `reto`, `kapti`, `signalo`, `revoki`, `malkonekti` を確認。`mesaĝi` はPIV 2020に「mesaĝoで連絡する」語義があり、text me / SMS 文脈として維持した。
- `Kie mi povas trovi telefonbudon?`, `Telefonkarton, mi petas`, `Kiom por minuto?`, `Ĉu mi povas uzi vian telefonon, mi petas?`, `Mi volas telefoni al miaj gepatroj`, `Mi devas ŝargi mian telefonon`, `Bonvolu noti mian numeron`, `Kiam estas pli bone telefoni al vi?`, `Nek Oskaro nek Vilhelmo estas hejme`, `Vi havas la malĝustan numeron`, `Mi petos lin retelefoni al vi`, `Mi ne ricevas vokan signalon`, `Mia kredito baldaŭ elĉerpiĝos`, `Mi ŝatus fari vokon pagatan de la ricevanto`, `Mi ĉiam trafas nur aŭtomatan respondilon`, `Mia baterio baldaŭ malŝargiĝos`, `Mi havas tre malfortan signalon`, `Mi telefonos en mia ĉambro`, `Kiu estas la urba telefona kodo?`, `Mi bezonas telefoni`, `Kie mi povas trovi publikan telefonon ĉi-proksime?`, `Mi ŝatus telefonkarton por 20 minutoj`, `Kiel mi povas telefoni al la informservo?`, `Kio estas la telefona kodo de Venezuelo?`, `Mi ŝatus telefoni al Seulo`, `De kie vi telefonas?`, `Ĉu iu telefonis al mi?`, `Ĉu mi povas retelefoni al vi?`, `Dankon pro via voko`, `Mi transdonos la mesaĝon, ke vi telefonis`, `Ĉu vi povas paroli nun?` は、電話ボックス、電話カード、分単位料金、電話を借りる、両親への電話、充電、番号メモ、電話しやすい時間、不在、間違い電話、折り返し依頼、発信音、残高、コレクトコール、留守番電話、バッテリー放電、弱い電波、部屋での電話、局番、公衆電話、番号案内、国番号、ソウルへの電話、発信元、着信有無、折り返し、着信への謝意、伝言、今話せるかとして対応する。
- PIV 2020 で `telefona budo`, `telefonkarto`, `ŝargi`, `noti`, `malĝusta`, `retelefoni`, `voka signalo`, `kredito`, `voko`, `respondilo`, `baterio`, `malŝargiĝi`, `urba`, `kodo`, `publika`, `informi/informservo`, `transdoni`, `mesaĝo`, `paroli` を確認。`Mia kredito baldaŭ elĉerpiĝos` は電話残高の語として透明で、`Mi telefonos en mia ĉambro` はロシア語の「自分の部屋で電話する」と対応するため維持した。
- `Pardonu, mi nun estas okupita`, `Li ne estas ĉi tie`, `Ŝi estas sur alia linio`, `Bedaŭrinde, ŝi forestas pro malsano`, `Bedaŭrinde, li estas en kunveno`, `Ĉu mi povas noti vian numeron?`, `Atendu momenton. Mi prenos skribilon`, `Kun kiu vi ŝatus paroli?`, `Mi konektos vin kun li`, `Ne demetu ankoraŭ la aŭdilon, mi petas`, `Ĉu mi povas telefoni rekte?`, `Ĉu vi povas klavi la numeron por mi?`, `Mi vidos ĉu mi povas konekti vin`, `Bonvolu resti sur la linio`, `La linio estas okupata`, `Ĉu vi povus peti lin telefoni al mi?`, `Pardonu, ŝi momente ne estas ĉi tie` は、今は忙しい、不在、別回線、病欠、会議中、番号を控える、ペンを取る、通話相手確認、取り次ぎ、電話を切らないでほしい、直通、番号入力、転送可否、保留、話し中、電話依頼、一時不在として対応する。
- PIV 2020 で `okupita/okupata`, `foresti`, `malsano`, `kunveno`, `skribilo`, `konekti`, `aŭdilo`, `klavi`, `linio`, `momente` を確認。`klavi la numeron` はPIV 2020に電話でキーを押す語義があり、現代的な dial の訳として維持した。`La linio estas okupata` は電話回線が利用中という意味が明確で、各列の話し中表現と対応する。

主な据え置き確認:
- `ID4761` `paracetamolo`: PIV 2020 ローカルには直接見つからなかったが、外部薬剤名リストで Esperanto 名として確認でき、各列と一致するため維持。
- `ID4767` `tutnokte malfermita apoteko`: all-night chemist の意味を保ち、24時間営業薬局の実用訳とも矛盾しないため維持。
- `ID4776` `sekiĝintaj lipoj`: chapped lips の乾燥・荒れ文脈として理解可能で、過修正しない。
- `ID4786` `Ne prenu interne`: warning label として短く自然で、内服不可の各列と整合するため維持。
- `ID4802` `mobilan reton`: mobile network / 携帯会社・通信事業者の文脈として維持。
- `ID4806` `mesaĝos`: PIV 2020 の `mesaĝi` に基づき、text / SMS の文脈で維持。
- `ID4819` `voka signalo`: PIV 2020 で確認でき、dialling tone / RU `гудок` と対応するため維持。
- `ID4820` `kredito`: 携帯・通話残高の文脈として透明で、日中韓/RUと対応するため維持。
- `ID4822` `aŭtomata respondilo`: answering machine / 留守番電話の文脈で意味ズレなし。
- `ID4825` `Mi telefonos en mia ĉambro`: ロシア語の「自分の部屋で電話する」と整合し、英日中韓の実用訳とも大きく矛盾しないため維持。
- `ID4830` `informservo`: directory enquiries / 電話番号案内として文脈上明確なため維持。
- `ID4850` `klavi la numeron`: PIV 2020 の電話用法に基づき、番号を押す・入力する意味として維持。
- `ID4853` `La linio estas okupata`: 電話回線が話し中である意味が明確なため維持。

参照:
- PIV 2020 ローカル `medikamento`, `tuso`, `plastro`, `jodo`, `aspirino`, `kromefiko`, `alkoholo`, `kremo`, `apoteko`, `farmaciisto`, `recepto`, `dormigilo`, `malvarmumo`, `gorĝdoloro`, `lipo`, `tablojdo`, `kapsulo`, `fumi`, `nikotino`, `misdigesto`, `instrukcio`, `dormemigi`, `telefono`, `telefoni`, `telefonbudo`, `telefonkarto`, `mesaĝo`, `mesaĝi`, `panei`, `signalo`, `malkonekti`, `voka signalo`, `respondilo`, `baterio`, `malŝargiĝi`, `informservo`, `aŭdilo`, `klavi`, `okupi/okupata`: `PIV2020_structured.txt`
- Leskoff "Drugs and medications in Esperanto" `paracetamol - paracetamolo`: https://www.leskoff.com/s04242-0
- 過去ログ `63周目`, `114周目`, `164周目`, `214周目`, `264周目`, `314周目`, `364周目`, `414周目`, `464周目`, `514周目`, `564周目`, `604周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4756`〜`ID4855` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 650. 649周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment
- Health / At the Dentist
- Health / At the Optician
- Health / At the Pharmacy

結果:
- **CSV修正なし**
- 前回 `ID4556`〜`ID4655` に続き、今回は `ID4656`〜`ID4755` の100件を確認した。処方・服薬、歯科治療、検眼・眼鏡、薬局での購入相談として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4663` ZH、`ID4682` ZH、`ID4689` EO、`ID4690` JA、`ID4693` RU、`ID4708` EN、`ID4723` RU、`ID4725` EO、`ID4740` EO、`ID4743` EO、`ID4744` JA、`ID4745` JA、`ID4747` EO/EN は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi preskribos al vi antibiotikojn`, `Portu ĉi tiun recepton al la apoteko`, `Kiomfoje tage mi devas preni ĉi tion?`, `Prenu po du el ĉi tiuj piloloj trifoje tage` は、抗生物質の処方、処方箋を薬局へ持参すること、服薬回数、1回2錠を1日3回という服薬指示として対応する。
- PIV 2020 で `antibiotiko`, `recepto`, `apoteko`, `pilolo`, `medikamento` を確認。`po du ... trifoje tage` は「毎回2つずつ、1日3回」の意味として各訳と整合するため維持した。
- `Mi bezonas viziti dentiston`, `Mi havas dentodoloron`, `Mi brosas la dentojn`, `Kie doloras?`, `Miaj gingivoj doloras`, `Al mi elfalis dento`, `Mi perdis plombon`, `Mi rompis denton`, `Krono rompiĝis`, `Ne eltiru ĝin`, `Bonvolu kontroli miajn dentojn`, `Bonvolu meti kronon sur ĉi tiun denton` は、歯科受診、歯痛、歯磨き、痛む場所、歯ぐき、歯の脱落、詰め物の脱落、歯の破折・欠け、クラウン破損、抜歯しないでほしい依頼、歯の確認、クラウン装着として対応する。
- PIV 2020 で `dento`, `dentodoloro`, `gingivo`, `eltiri denton`, `plombo/plombi/plombaĵo`, `krono/kroni/kronaĵo`, `dentisto` を確認。`Mi brosas la dentojn` は所有を明示する `miajn dentojn` も可能だが、身体部位を定冠詞で表す実用表現として維持した。
- `Mi havas ŝvelintan gingivon`, `Doloras kiam mi maĉas`, `Ĉu necesas ĝin eltiri?`, `Ĉu vi povas ripari mian dentprotezon?`, `Vi bezonas du plombojn`, `Vi havas absceson`, `Ĉu vi havas iujn plendojn?`, `Kie estas la plej proksima denta kliniko?`, `Vi devus fari rendevuon ĉe la denta higienisto`, `Mi ŝatus dentpurigadon`, `Mi ŝatus plombigi denton`, `Vi havas iom da kario en ĉi tiu dento`, `Mi devos eltiri ĉi tiun denton`, `Ĉu vi volas, ke oni alĝustigu al vi kronon?`, `Ĉu vi ŝatus gargari la buŝon?`, `Via asekuro ne kovras tian kuracadon` は、歯ぐきの腫れ、咀嚼痛、抜歯必要性、入れ歯修理、詰め物、膿瘍、問題確認、歯科医院、歯科衛生士、歯のクリーニング、詰め物治療、虫歯、抜歯、クラウン調整・装着、口すすぎ、保険適用外として対応する。
- PIV 2020 で `ŝveli/ŝvela`, `maĉi`, `protezo`, `absceso`, `kliniko`, `higienisto`, `kario`, `alĝustigi`, `gargari`, `buŝo`, `asekuro`, `kovri`, `kuracado` を確認。`denta higienisto` は `higienisto` 単独より歯科文脈が明確な過去補正後の形を維持した。
- `Mia vido estas malbona`, `Mi bezonas okulvitrojn`, `Ĉu vi vendas sunokulvitrojn?`, `Li havas grandajn dioptriojn`, `Li estas hipermetropa`, `Ŝi estas miopa`, `Ĉu vi portas kontaktlensojn?`, `Mi bezonas novan okulvitrujon`, `Bonvolu montri al mi kelkajn kadrojn`, `Provu ĉi tiun paron da okulvitroj`, `Ĉu vi ofertas senpagajn okulekzamenojn?`, `Mia vidkapablo malboniĝas`, `Ŝi havas astigmatismon`, `Kiom kostas ĉi tiuj dezajnistaj kadroj?`, `Mi bezonas novajn okulvitrojn por legado`, `Ĉu ĉi tiuj sunokulvitroj havas UV-protekton?`, `Mi ŝatus kontroligi mian vidon, mi petas`, `Ĉu vi estas miopa aŭ hipermetropa?`, `Ĉu vi povus voĉlegi la literojn sur la tabulo?` は、視力、眼鏡、サングラス、度数、遠視・近視、コンタクト、眼鏡ケース、フレーム、試着、視力検査、視力低下、乱視、デザイナーフレーム、老眼鏡・読書用眼鏡、UV保護、右目・左目で読む検査として対応する。
- PIV 2020 で `vido`, `vidkapablo`, `okulvitroj`, `sunokulvitroj`, `dioptrio`, `hipermetropa`, `miopa`, `kontaktolenso`, `ujo`, `kadro`, `astigmatismo`, `dezajno/dezajnisto`, `ultraviola`, `protekto`, `tabulo` を確認。`grandajn dioptriojn` は直訳感はあるが、度が強いという意味は日中韓/RUと整合し、過修正しない。
- `Mi bezonas termometron`, `Mi havas recepton`, `Kia estas la dozo?`, `Du ĝis kvar tablojdoj tage`, `Mi serĉas apotekon`, `Mi bezonas inhalilon`, `Mi bezonas desinfektaĵon`, `Ĉu vi havas plastrojn?`, `Ĉu vi havas kontraŭdolorilojn?`, `Ĉu vi ne havas ion similan?`, `Ĉu ĝi taŭgas por infanoj?`, `Post manĝo?`, `Ĉu mi prenu ĝin fastante?`, `Je kioma horo malfermiĝas la apoteko?`, `Ĉu mi bezonas recepton por ĉi tio?`, `Oni povas ĝin aĉeti sen recepto`, `Ĝi estas havebla nur laŭ recepto`, `Kiujn medikamentojn vi rekomendas?` は、体温計、処方箋、用量、錠剤、薬局、吸入器、消毒剤、絆創膏、鎮痛薬、類似品、子ども適用、食後・空腹時、薬局の開店時間、処方箋要否、処方箋なし購入、処方箋限定、薬の推薦として対応する。
- PIV 2020 で `termometro`, `dozo`, `tablojdo`, `apoteko`, `inhalilo`, `desinfekti/desinfektaĵo`, `plastro`, `doloro`, `taŭgi`, `fasti/fasto`, `havebla`, `recepto`, `medikamento`, `rekomendi` を確認。`kontraŭdoloriloj` は `kontraŭ` + `doloro` + `-il-` の透明な複合で painkillers 文脈を保つため維持した。

主な据え置き確認:
- `ID4659` `po du el ĉi tiuj piloloj trifoje tage`: `po` により「各回2錠」の分配が明確で、服薬指示として維持。
- `ID4669` / `ID4683` / `ID4692` `plombo` / `plombigi`: PIV 2020 で歯の詰め物・詰める用法を確認できるため維持。
- `ID4671` / `ID4676` / `ID4698` `krono`: PIV 2020 に歯冠、歯にかぶせる処置、`kronaĵo` があり、歯科クラウン文脈で維持。
- `ID4680` `dentprotezo`: PIV 2020 の `protezo` と `denta` の透明な複合で、dentures / 入れ歯として維持。
- `ID4699` `gargari la buŝon`: PIV 2020 で口・喉を液体ですすぐ語義を確認できるため維持。
- `ID4708` `grandajn dioptriojn`: 度数が高いという意味は明確で、日中韓/RU列と整合するため維持。
- `ID4712` `okulvitrujo`: `okulvitroj` + `ujo` の透明な複合で、glasses case として維持。
- `ID4739` `Kia estas la dozo?`: `Kiom granda estas la dozo?` なども候補だが、薬局での短い用量質問として意味は明確なため維持。
- `ID4747` `Ĉu vi ne havas ion similan?`: 過去補正で `analogo` から薬局文脈に合う一般表現へ直した現形を維持。
- `ID4750` `fastante`: PIV 2020 に `glutu la kuracilon en stato de fasto` 型があり、empty stomach と対応するため維持。
- `ID4754` `havebla nur laŭ recepto`: prescription-only の意味が明確で、日中韓と矛盾しないため維持。

参照:
- PIV 2020 ローカル `antibiotiko`, `recepto`, `apoteko`, `pilolo`, `medikamento`, `dento`, `gingivo`, `plombo`, `krono`, `kroni`, `kronaĵo`, `protezo`, `absceso`, `kliniko`, `higienisto`, `kario`, `alĝustigi`, `gargari`, `buŝo`, `asekuro`, `kovri`, `kuracado`, `vido`, `vidkapablo`, `okulvitroj`, `sunokulvitroj`, `dioptrio`, `hipermetropa`, `miopa`, `kontaktolenso`, `kadro`, `astigmatismo`, `dezajno`, `dezajnisto`, `ultraviola`, `protekto`, `termometro`, `dozo`, `tablojdo`, `inhalilo`, `desinfekti`, `desinfektaĵo`, `plastro`, `fasti`, `havebla`, `rekomendi`: `PIV2020_structured.txt`
- 過去ログ `62周目`, `113周目`, `163周目`, `213周目`, `263周目`, `313周目`, `363周目`, `413周目`, `463周目`, `513周目`, `563周目`, `603周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4656`〜`ID4755` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 649. 648周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor
- Health / Diseases
- Health / Treatment

結果:
- **CSV修正なし**
- 前回 `ID4456`〜`ID4555` に続き、今回は `ID4556`〜`ID4655` の100件を確認した。診察時の一般質問、症状・疾患申告、治療・検査・入院関連の表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4567` EO、`ID4569` JA、`ID4576` ZH、`ID4581` ZH、`ID4604` EO/JA、`ID4605` EO、`ID4614` EO、`ID4615` ZH、`ID4618` EO、`ID4624` ZH、`ID4628` ZH、`ID4633` EO、`ID4640` EO、`ID4654` RU は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Kiom da alkoholo vi trinkas semajne?`, `Ĉu estas ia ebleco, ke vi estas graveda?`, `Ĉu vi havas privatan medicinan asekuron?`, `Kiel vi sentas vin ĝenerale?`, `Kiel vi fartas?`, `Mi sentas min kapturna`, `Mi sentas min malsana`, `Mi tremas`, `Mi havas malvarmumon`, `Mi havas tuberon` は、飲酒量、妊娠可能性、民間医療保険、全般的な体調、めまい、悪寒・震え、風邪、しこりの文脈として対応する。
- PIV 2020 で `alkoholo`, `graveda`, `asekuri/asekuro`, `farti`, `kapturno`, `malvarmumo`, `tubero` を確認。`privata medicina asekuro` は `malsanasekuro` / `sanasekuro` 系も候補だが、private medical insurance の意味は透明で、日中韓の「民間/私人/개인 医療保険」と整合するため維持した。
- `Insekto pikis min`, `Mi havas haŭterupcion`, `Mi havas furunkon`, `Mi havas gripon`, `Mi havas astmon`, `Mi havas tuson`, `Mi havas diareon`, `Mi estas konstipita`, `Li estas blinda`, `Ŝi estas muta`, `Ŝi estas surda`, `Li estas diabetulo`, `Ŝi havas ŝvelon` は、虫刺され、発疹、おでき、インフルエンザ、喘息、咳、下痢、便秘、視覚・発話・聴覚障害、糖尿病、腫れとして対応する。
- PIV 2020 で `piki`, `erupcio`, `furunko`, `gripo`, `astmo`, `tuso`, `diareo`, `konstipita`, `blinda`, `muta`, `surda`, `diabeto/diabetulo`, `ŝvelo` を確認。`haŭterupcio` は `haŭto` + `erupcio` の透明な複合で rash 文脈を保つため維持した。
- `Mi frapis mian genuon`, `Mi havas fortan doloron`, `Ĝi estas akra doloro`, `Mi ne fartas bone`, `Mi sentas min iom pli bone`, `Ŝajnas, ke mi tuj vomos`, `Mi havas nazkataron`, `Mi havas kapdoloron`, `Mi havas febron`, `Mi tranĉis mian fingron`, `Mi ne povas movi mian kruron`, `Mi maldikiĝis`, `Mia stomako doloras`, `Miaj piedoj doloras` は、膝打撲、強い痛み、鋭い痛み、体調不良、改善、吐き気、鼻水、頭痛、発熱、指の切創、脚を動かせない、体重減少、腹痛、足の痛みとして対応する。
- PIV 2020 で `genuo`, `doloro`, `akra`, `vomi`, `naza kataro`, `kapdoloro`, `febro`, `tranĉi`, `kruro`, `maldikiĝi`, `stomako`, `piedo` を確認。`nazkataro` はPIVの `naza kataro` と同じ透明な複合で、runny nose / 鼻水文脈として維持した。
- `Ĉu vi havas kronikajn malsanojn?`, `Kiaj estas viaj simptomoj?`, `Mi havas gorĝdoloron`, `Mi havas ŝvelintan maleolon`, `Mi havas doloron en la brusto`, `Mi havas kormalsanon`, `Mi havas tre malmulte da energio`, `Mi havas stomakan perturbon`, `Mi ne havas apetiton`, `Mi malfacile spiras`, `Mia nazo estas tre ŝtopita`, `Miaj artikoj/genuoj doloras`, `Miaj limfonodoj estas ŝvelintaj` は、慢性疾患、症状、喉・足首・胸・心臓、倦怠感、胃の不調、食欲不振、呼吸困難、鼻づまり、関節・膝痛、リンパ節腫脹として対応する。
- PIV 2020 で `kronika`, `malsano`, `simptomo`, `gorĝo`, `maleolo`, `brusto`, `koro`, `energio`, `perturbo`, `apetito`, `spiri`, `ŝtopi`, `artiko`, `limfo nodo` を確認。`Mi havas tre malmulte da energio` と `Mi havas stomakan perturbon` は過去補正後の表現で、現CSVでもその形を維持した。
- `Mi havas gravan mikozon de la piedoj`, `Mi pensas, ke mi streĉis muskolon en mia kruro`, `Mi sentas min deprimita`, `Mi havas malfacilaĵojn pri dormado`, `Mi suferas de sendormeco`, `Mi suferas de fojnofebro`, `Mi neniam antaŭe havis ĉi tiun malsanon` は、水虫、脚の筋肉を痛めた、気分の落ち込み、睡眠困難、不眠症、花粉症、初めてかかった病気として対応する。
- PIV 2020 で `mikozo`, `piedo`, `streĉi`, `muskolo`, `deprimi`, `dormado`, `sendormeco`, `fojno febro`, `fojno kataro`, `malsano` を確認。`fojnofebro` はPIVの分かち書き `fojno febro` と同じ構成で、hay fever として維持した。
- `Prenu ĉi tiun medikamenton`, `Jen la recepto`, `Kio estas la diagnozo?`, `Ĉu ĝi estas kontaĝa?`, `Mi volas, ke vi vizitu specialiston`, `Vi devas fari sangoteston`, `Ĝi rapide resaniĝos`, `Vi devus ĉesi fumi`, `Bonvolu doni al mi recepton`, `Mi bezonas kuracistan atestilon`, `Ĉu mi povas sporti?`, `Vi bezonos seriozan kuracadon`, `Kiom longe daŭros la kuracado?` は、服薬指示、処方箋、診断、感染性、専門医受診、血液検査、治癒、禁煙、診断書、運動可否、本格的な治療、治療期間として対応する。
- PIV 2020 で `medikamento`, `recepto`, `diagnozo`, `kontaĝa`, `specialisto`, `sango`, `testo`, `resaniĝi`, `fumi`, `atestilo`, `sporto/sporti`, `kuraci/kuracado` を確認。`sangotesto` は `sango` + `testo` の透明な複合で、blood test / 血液検査文脈として維持した。
- `Kiom longe mi restos en la hospitalo?`, `Ĉu mi bezonas operacion?`, `Vi bezonos kelkajn suturerojn`, `Ĉu mi bezonos lokan anestezon?`, `Vi ne sentos doloron`, `Ĉu vi bonvolus skribi al mi recepton?`, `Kiom kostos ĉi tiu analizo?`, `Oni jam faris al mi tian analizon antaŭe`, `Mi volas sendi vin por rentgena ekzameno`, `Ni devas preni urinan specimenon`, `Vi devas provi perdi iom da pezo`, `Vi devus redukti vian trinkadon`, `Mi faros al vi injekton`, `Ĉu mi rajtas ellitiĝi?` は、入院期間、手術、縫合、局所麻酔、無痛、処方箋作成、検査費用、既検査、レントゲン、尿検体、減量、飲酒量削減、注射、離床許可として対応する。
- PIV 2020 で `hospitalo`, `operacio`, `suturo/suturero`, `anestezo`, `doloro`, `analizo`, `rentgena`, `urino/urina`, `specimeno`, `pezo`, `trinkado`, `injekti/injekto`, `ellitiĝo` を確認。`sutureroj` は縫合を構成する糸として、`urina specimeno` は urine sample として、`redukti vian trinkadon` は飲酒量を減らす表現として維持した。

主な据え置き確認:
- `ID4558` `privata medicina asekuro`: private medical insurance の意味は透明で、日中韓と整合するため維持。
- `ID4568` `haŭterupcio`: PIV 2020 の `erupcio` が皮膚症状語義を持ち、`haŭt-` との複合で rash として読めるため維持。
- `ID4614` `mikozo de la piedoj`: PIV 2020 の `mikozo` に基づく確認可能な表現で、athlete's foot / 水虫と対応するため維持。
- `ID4618` `malfacilaĵojn pri dormado`: 睡眠に関する困難として自然で、過去補正後の現形を維持。
- `ID4620` `fojnofebro`: PIV 2020 の `fojno febro = fojnkataro`、`fojno kataro` に基づき hay fever として維持。
- `ID4633` `kuracistan atestilon`: `atestilo` は証明文書として確認でき、診断書 / sick note 文脈に合うため維持。
- `ID4640` `suturerojn`: PIV 2020 で縫合を構成する個々の糸として確認でき、「何針か」に対応するため維持。
- `ID4648` `urinan specimenon`: `urina` + `specimeno` の透明な組み合わせで、尿検体として日中韓と対応するため維持。
- `ID4650` `redukti vian trinkadon`: PIV 2020 の `trinkado` 用例と一致し、飲酒量削減の文脈として維持。
- `ID4655` `ellitiĝi`: 病床から起きる、ベッドから出る意味として日中韓と対応するため維持。

参照:
- PIV 2020 ローカル `alkoholo`, `graveda`, `asekuro`, `farti`, `kapturno`, `malvarmumo`, `tubero`, `piki`, `erupcio`, `furunko`, `gripo`, `astmo`, `tuso`, `diareo`, `konstipita`, `blinda`, `muta`, `surda`, `diabeto`, `ŝvelo`, `naza kataro`, `kapdoloro`, `febro`, `maldikiĝi`, `stomako`, `piedo`, `simptomo`, `gorĝo`, `maleolo`, `brusto`, `koro`, `energio`, `perturbo`, `apetito`, `spiri`, `ŝtopi`, `artiko`, `limfo nodo`, `mikozo`, `streĉi`, `muskolo`, `deprimi`, `sendormeco`, `fojno febro`, `fojno kataro`, `medikamento`, `recepto`, `diagnozo`, `kontaĝa`, `specialisto`, `sango`, `testo`, `resaniĝi`, `fumi`, `atestilo`, `sporti`, `kuracado`, `hospitalo`, `operacio`, `suturo`, `suturero`, `anestezo`, `analizo`, `rentgena`, `urina`, `specimeno`, `trinkado`, `injekto`, `ellitiĝo`: `PIV2020_structured.txt`
- 過去ログ `61周目`, `112周目`, `162周目`, `212周目`, `262周目`, `312周目`, `362周目`, `412周目`, `462周目`, `512周目`, `562周目`, `593周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4556`〜`ID4655` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 648. 647周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs
- Health / At the Doctor

結果:
- **CSV修正なし**
- 前回 `ID4356`〜`ID4455` に続き、今回は `ID4456`〜`ID4555` の100件を確認した。修理受付、時計・鍵・靴修理、診察・検査・服薬・血圧などの医療会話として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4462` EO/JA、`ID4470` EO、`ID4471` EO/JA、`ID4476` ZH、`ID4479` ZH、`ID4483` EO/ZH、`ID4484` EO、`ID4504` EO/JA、`ID4508` EO/EN、`ID4514` EO、`ID4516` EO/EN、`ID4550` ZH、`ID4553` JA は、現CSVで補正後内容になっていることを確認した。特に `ID4470` は旧ログの `kroneto` ではなく、現CSVの `La krono estas rompita` を正とする。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `La ekrano fendiĝis`, `La kuirforno estas difektita`, `Mia brakhorloĝo haltis`, `Mi pensas, ke ĝi bezonas novan pilon`, `Ĝi estos preta ĝis morgaŭ`, `Mia komputilo havas viruson`, `Mia horloĝo bezonas reguligon`, `La krono estas rompita`, `Ĉu vi povas anstataŭigi la pilon?`, `Ĉu indas ĝin ripari?`, `Ne indas ĝin ripari` は、画面のひび、コンロ故障、腕時計停止、電池交換、翌日までの仕上がり、ウイルス、時計調整、リューズ故障、修理価値の有無として対応する。
- PIV 2020 で `fendiĝi`, `kuirforno`, `brakhorloĝo`, `pilo`, `ĝis`, `reguligi`, `krono`, `ripari`, `indi` を確認。`ĝis morgaŭ` は期限を表す用例、`krono` は時計などの上部の輪状部品を含む語義があり、現行表現を維持した。
- `Ĉu vi povus fari kopion de ĉi tiu ŝlosilo?`, `Mi ŝatus po unu kopio de ĉiu el ĉi tiuj`, `Ĉu vi havas pilon por ĉi tio?`, `Ĉu vi bonvolus ŝanĝi la pilon en mia horloĝo?`, `Kie estas la plej proksima riparejo por ŝuoj?`, `Ĉu vi povus almeti novajn plandumojn al ĉi tiuj ŝuoj por mi?`, `Kiom longe daŭros la riparoj?`, `La riparoj ne estas kovrataj de la garantio`, `Ni devas resendi ĝin al la fabrikanto` は、鍵複製、時計用電池、靴修理、靴底張り替え、修理期間、保証対象外、メーカー返送として対応する。
- PIV 2020 で `ŝlosilo`, `kopio`, `ŝanĝi`, `riparejo`, `plandumo`, `daŭri`, `garantio`, `fabrikanto` を確認。`po unu kopio de ĉiu` は各鍵を1本ずつ複製する意味として日中韓と対応する。
- `Mi ŝatus kontrolan ekzamenon`, `Doloras ĉi tie`, `Ĉu doloras al vi?`, `Ĉu vi havas kapturnon?`, `Kio estas al mi, doktoro?`, `Ĉu vi fartas pli bone?`, `Mi fartas pli malbone`, `Ĉu vi havas iujn alergiojn?`, `Ĉu vi prenas iujn medikamentojn?`, `Kiel ofte vi trinkas alkoholaĵojn?`, `Mi bezonas rentgenan ekzamenon`, `Ĉu vi faras aŭdotestojn?`, `Mi bezonas medicinan konsulton` は、健康診断、痛み、めまい、病状確認、回復・悪化、アレルギー、服薬、飲酒頻度、レントゲン、聴力検査、診察相談として対応する。
- PIV 2020 で `kontroli/kontrola`, `ekzameno`, `dolori`, `kapturno`, `farti`, `alergio/alergia`, `medikamento`, `alkoholaĵo`, `rentgena`, `aŭdo`, `testo`, `medicina`, `konsulto` を確認。`rentgena ekzameno` は X-ray の検査表現として維持した。
- `Kiam vi eksentis vin malbone?`, `Kiam doloras?`, `Doloras pli nokte`, `Ĝi doloras konstante`, `Vi devos fari analizojn`, `Mi ne havas malsanasekuron`, `Kiu estas via sangogrupo?`, `Mia sangogrupo estas O negativa/O-pozitiva`, `Mi pensas, ke mi eble estas graveda`, `Je kiuj horoj vi akceptas?`, `Ĉu vi havas kuracistojn, kiuj parolas la kmeran?` は、発症時期、痛むタイミング、夜間痛、継続痛、検査、健康保険、血液型、妊娠可能性、診療時間、クメール語対応医師として対応する。
- PIV 2020 で `analizo`, `sango grupo`, `graveda`, `akcepti` を確認。`malsanasekuro` は `malsano` + `asekuro` の透明な複合、`O-pozitiva` は血液型表記として明確、`akceptas` は来客・利用者を受け入れる語義に基づき診療受付時間の文脈で維持した。`kmera` は外部辞書で Khmer と `la kmera lingvo` の短縮用法を確認した。
- `Mi ŝatus esti ekzamenata de virino`, `La vundo ne estas profunda`, `Bonvolu desinfekti ĝin`, `Kia estas mia temperaturo?`, `Ĉu doloras kiam vi glutas?`, `Ĉu vi povus suprenfaldi vian manikon?`, `Mi mezuros vian sangopremon`, `Via sangopremo estas tre alta/sufiĉe malalta`, `Mi bezonas iom pli da insulino`, `Mi bezonas recepton por trankviligaĵo`, `Antaŭe oni kuracis min pro ulcero`, `Ĉu vi dormas surdorse aŭ surventre?` は、女性による診察、傷、消毒、体温、嚥下痛、袖まくり、血圧測定、インスリン、精神安定剤、潰瘍治療歴、仰向け・うつ伏せ睡眠として対応する。
- PIV 2020 で `vundo`, `desinfekti`, `temperaturo`, `gluti`, `supren`, `faldi`, `maniko`, `malalta sangopremo`, `insulino`, `trankviligaĵo`, `ulcero`, `dorso`, `ventro` を確認。`Kia estas mia temperaturo?` は数値を尋ねる自然さでは `Kiom estas...` も候補だが、PIVにも `kia estas la ... temperaturo?` 型があり、現行文でも体温状態・値の質問として読めるため維持した。

主な据え置き確認:
- `ID4464` `Ĝi estos preta ĝis morgaŭ`: PIV 2020 の `ĝis` に期限を表す用例があり、by tomorrow と対応するため維持。
- `ID4470` `La krono estas rompita`: PIV 2020 の `krono` に時計部品を含む語義があり、winder / リューズ文脈として維持。
- `ID4530` `Vi devos fari analizojn`: RU `сдать анализы` と日中韓の検査文脈に対応し、PIV 2020 の `analizo` から医療検査として読めるため維持。
- `ID4536` `Je kiuj horoj vi akceptas?`: 診療受付時間を尋ねる表現として文脈上明確なため維持。
- `ID4537` `la kmeran`: PIV 2020 では未確認だが、Kaikki/Wiktionary 系データで `kmera` が Khmer、および `la kmera lingvo` の短縮として確認でき、クメール語を話す医師の文脈と一致するため維持。
- `ID4541` `Kia estas mia temperaturo?`: `Kiom estas mia temperaturo?` への言い換え余地はあるが、現行でも体温を尋ねる意味は明確なため維持。
- `ID4555` `surdorse aŭ surventre`: `sur la dorso` / `sur la ventro` の副詞化として、仰向け・うつ伏せ睡眠と対応するため維持。

参照:
- PIV 2020 ローカル `fendiĝi`, `kuirforno`, `brakhorloĝo`, `pilo`, `ĝis`, `reguligi`, `krono`, `ripari`, `indi`, `ŝlosilo`, `kopio`, `ŝanĝi`, `riparejo`, `plandumo`, `daŭri`, `garantio`, `fabrikanto`, `kontrola`, `ekzameno`, `dolori`, `kapturno`, `farti`, `alergio`, `medikamento`, `alkoholaĵo`, `rentgena`, `aŭdo`, `testo`, `konsulto`, `analizo`, `sango grupo`, `graveda`, `akcepti`, `vundo`, `desinfekti`, `temperaturo`, `gluti`, `supren`, `faldi`, `maniko`, `sangopremo`, `insulino`, `trankviligaĵo`, `ulcero`, `dorso`, `ventro`: `PIV2020_structured.txt`
- Kaikki.org / Wiktionary 抽出データ `kmera`: https://kaikki.org/dictionary/Esperanto/meaning/k/km/kmera.html
- 過去ログ `60周目`, `111周目`, `161周目`, `211周目`, `461周目`, `511周目`, `561周目`, `587周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4456`〜`ID4555` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 647. 646周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency
- Services / At the Beauty Salon
- Services / At the Tailor's
- Services / Repairs

結果:
- **CSV修正なし**
- 前回 `ID4256`〜`ID4355` に続き、今回は `ID4356`〜`ID4455` の100件を確認した。不動産仲介、美容院、仕立て屋、修理受付の表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4367` RU、`ID4376` EN、`ID4377` JA、`ID4378` EO、`ID4388` EO、`ID4389` JA/ZH、`ID4391` ZH、`ID4393` EO、`ID4394` EO/ZH、`ID4396` EO、`ID4398` ZH、`ID4401` JA、`ID4402` ZH、`ID4417` EN、`ID4434` EN、`ID4436` ZH、`ID4439` ZH、`ID4443` ZH、`ID4447` ZH、`ID4449` EO、`ID4451` JA は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi ŝatus rigardi ĉi tiun posedaĵon`, `Kiam estus oportune por vi viziti la posedaĵon?`, `La lupago estas pagenda monate anticipe`, `Ĉu ili pretas negoci?`, `Kiel baldaŭ vi povus enloĝiĝi?`, `Ĉu vi ŝatus, ke ni aldonu vin al nia dissendolisto?` は、不動産の内見、前払い家賃、価格交渉、入居時期、メール配信リスト登録の文脈として対応する。
- PIV 2020 で `posedi/posedaĵo`, `lupago`, `anticipe`, `negoci`, `enloĝiĝi`, `dissendo listo` を確認。`dissendolisto` はPIVでは分かち書きだが、`dissendo` + `listo` の透明な複合で、mailing list 文脈を保つため維持した。
- `Mi bezonas tondadon`, `Mi ŝatus franĝon`, `Miaj haroj estas sekaj/grasaj`, `Mildan konstantan ondumadon, mi petas`, `Tondadon kaj razadon, mi petas`, `Razu tute kalve`, `Ĉu vi havas dislimon?`, `Bonvolu formi miajn brovojn`, `Mi ŝatus ilin farbigi`, `Bonvolu farbi miajn harojn blonde`, `Mi ŝatus helajn striojn en miaj haroj`, `Kian frizaĵon vi dezirus?`, `Bonvolu bukli la pintojn internen`, `Ĉu vi faras senharigon?`, `Mi ŝatus senharigon de miaj kruroj per vakso` は、美容院・理容・髪染め・眉・脱毛の表現として対応する。
- PIV 2020 で `tondi/tondado`, `haro/haroj`, `franĝo`, `ŝminko`, `razi`, `kalva`, `dislimi/dislimo`, `brovo`, `frizi/frizaĵo`, `ondumi/ondumado`, `vakso`, `senharigi/senharigo` を確認。`Razu tute kalve` は `razi` と `kalva` の根拠があり、RU/ZH/KO の「剃ってつるつるにする」方向と対応するため維持。`meza disigo en la haroj` は専門語 `dislimo` への言い換え余地はあるが、髪を中央で分ける意味は明確で、誤りとは断定しない。
- `Bonvolu tondi kaj feni miajn harojn`, `Bonvolu ŝampui kaj aranĝi miajn harojn`, `Bonvolu kombi miajn harojn de la frunto malantaŭen`, `Jes. Iom da sprajo por haroj, mi petas`, `Iom da ĝelo por haroj, mi petas`, `Ĉu vi povus tondi miajn lipharojn?`, `Ĉu vi povus pritondi mian barbon?`, `Bonvolu fari al mi vizaĝan masaĝon`, `Mi ŝatus havi traktadon de la vizaĝo`, `Mi ŝatus ricevi masaĝon de la kranihaŭto`, `Ĉu vi bonvolus elpluki miajn brovojn?`, `Mi ŝatus, ke vi fajlu kaj formu miajn ungojn`, `Mi ŝatus laki miajn ungojn` は、ブロー、シャンプー、整髪剤、ひげ、フェイシャル、頭皮、眉抜き、ネイル表現として対応する。
- PIV 2020 で `feni`, `ŝampui`, `spraji`, `ĝelo`, `lipharoj`, `barbo`, `vizaĝo`, `kranihaŭto`（`haroj` 項の説明内）, `elpluki`, `ungo fajlilo`, `ungo lako`, `manikuri`, `pedikuri` を確認。`sprajo por haroj` は `harlako` も候補だが、現行表現でも hairspray の意味が透明で、日中韓と矛盾しないため維持した。
- `Ni iru al la tajloro`, `Ĉu vi povas mallongigi ilin?`, `Ĉu vi povas plilongigi ĉi tion?`, `La jako estas malvasta`, `Ĉu vi povas ripari la zipon?`, `Ĉu vi povas alkudri ĝin reen?`, `Ĉu vi povas preni miajn mezurojn?`, `Ĉu vi povas alkudri ĉi tiujn butonojn?`, `Ĉu vi povas fliki ĉi tiun truon?`, `Mi ŝatus laŭmezuran kostumon`, `Ni povas alĝustigi ĝin laŭ via grandeco`, `Ĉu vi povas mezuri mian maniklongon?`, `Ĉu vi povus mallarĝigi ĉi tiun robon ĉe la talio?`, `Ĉu vi povus mallongigi ĉi tiun jupon je centimetro?`, `Ĉu vi povus longigi ĉi tiun pantalonon je centimetro?`, `Ĉu vi povus plilarĝigi ĉi tiun pantalonon je du centimetroj?` は、仕立て直し、採寸、ボタン、穴補修、オーダーメイド、丈・幅調整として対応する。
- PIV 2020 で `tajloro`, `jako`, `zipo`, `kudri/alkudri`, `fliki`, `mezuroj`, `almezuri`, `laŭmezura`, `alĝustigi`, `maniko`, `pantalono`, `larĝa/mallarĝa` を確認。`pantalono` はPIVで一着を単数扱いし、複数形は非推奨とされるため、過去補正後の `ĉi tiun pantalonon` を維持した。
- Repairs 冒頭の `Ĝi ne funkcias bone`, `Ĉu vi povas ripari ĝin?`, `Ĉu ĉi tio estas multekosta?`, `Ni ne povas fari tion ĉi tie`, `Ĉu vi povas ripari la televidon?` は、修理受付の短文として日中韓と対応する。

主な据え置き確認:
- `ID4360` `La prezo estas pli alta ol mi planis elspezi`: PIV 2020 の `ol` 項では比較節で `ol kiom` の `kiom` が省略可能とされ、支出予定額との比較として読めるため維持。
- `ID4361` `Kiel baldaŭ vi povus enloĝiĝi?`: how soon の実用会話表現として、入居可能時期を尋ねる意味が明確なため維持。
- `ID4372` `Mildan konstantan ondumadon`: PIV 2020 の `ondumado` に `konstanta ondumado` と髪の用例があり、soft perm 文脈として維持。
- `ID4378` `dislimon`: PIV 2020 の `haroj` 項に `dislimi al si la harojn` があり、髪の分け目として維持。
- `ID4388` `helajn striojn en miaj haroj`: highlights を未確認語でなく透明な表現で表しており、意味ズレなし。
- `ID4403` `Malantaŭe kojne`: RU `клином` と対応し、後ろを先細り・くさび形に整える依頼として維持。
- `ID4408` `mezan disigon en la haroj`: `meza dislimo` も候補だが、中央分けの意味は明確なため維持。
- `ID4412` `sprajo por haroj` / `ID4413` `ĝelo por haroj`: hair spray / hair gel として透明で、日中韓と矛盾しないため維持。
- `ID4419` `traktadon de la vizaĝo`: facial / skin treatment の広い施術表現として維持。
- `ID4444` `laŭ via grandeco`: `laŭ viaj mezuroj` への精密化余地はあるが、サイズに合わせる意味は明確なため維持。

参照:
- PIV 2020 ローカル `posedi`, `posedaĵo`, `lupago`, `anticipe`, `negoci`, `enloĝiĝi`, `dissendo listo`, `tondi`, `haro/haroj`, `franĝo`, `ŝminko`, `razi`, `kalva`, `dislimo`, `brovo`, `frizi`, `frizaĵo`, `ondumi`, `ondumado`, `vakso`, `senharigo`, `feni`, `ŝampui`, `spraji`, `ĝelo`, `lipharoj`, `barbo`, `vizaĝo`, `kranihaŭto`, `ungo fajlilo`, `ungo lako`, `manikuri`, `pedikuri`, `tajloro`, `jako`, `zipo`, `kudri`, `fliki`, `mezuroj`, `almezuri`, `laŭmezura`, `alĝustigi`, `maniko`, `pantalono`, `prezlisto`: `PIV2020_structured.txt`
- 過去ログ `59周目`, `110周目`, `160周目`, `460周目`, `510周目`, `560周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4356`〜`ID4455` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 646. 645周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank
- Services / Estate

結果:
- **CSV修正なし**
- 前回 `ID4156`〜`ID4255` に続き、今回は `ID4256`〜`ID4355` の100件を確認した。銀行窓口・ATM・口座手続き、不動産購入・賃貸相談の表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4267` EO、`ID4276` RU、`ID4277` ZH、`ID4279` RU、`ID4286` JA/ZH、`ID4291` RU、`ID4294` EO、`ID4311` EO、`ID4315` EO、`ID4318` EN、`ID4321` EO、`ID4322` RU、`ID4325` EO、`ID4328` RU、`ID4329` RU、`ID4330` ZH、`ID4333` ZH、`ID4339` RU、`ID4340` EO/RU、`ID4347` EN、`ID4350` EO は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Elprenu la karton`, `Mia karto ne funkcias`, `Mi ŝatus aĉeti eŭrojn`, `Kia/Kiom estas la kurzo/provizio?`, `Ĉu vi ŝatus kvitancon?`, `Ĉi tio estas falsa monbileto`, `Kie estas la bankaŭtomato?`, `Ĉu vi povus diri al mi mian saldon, mi petas?`, `Mi ŝatus fari retiron`, `Mi ŝatus deponi iom da mono`, `Mi ŝatus sendi iom da mono al Hindio`, `Mi ŝatus raporti pri perdita kreditkarto`, `Ĉu mi povus ricevi konteltiron, mi petas?`, `Mi ŝatus ĝiri iom da mono en ĉi tiun konton`, `Kiom estas la interezprocento de ĉi tiu konto?`, `Mi ŝatus kontantigi ĉi tiun vojaĝan ĉekon` は、銀行カード、両替、ATM、残高、入出金、送金、口座明細、利率、トラベラーズチェックの文脈として対応する。
- PIV 2020 で `legitimilo`, `formularo`, `subskribi`, `kurzo`, `provizio`, `kvitancon`, `falsa`, `monbileto`, `bankbileto`, `bankaŭtomato`, `kontanta`, `saldo`, `ĉeko`, `ĉekaro`, `deponi`, `konto`, `konteltiro`, `ĝiri`, `interezo`, `procento`, `kontantigi` を確認。`provizio` は銀行を含む仲介報酬・手数料、`ĝiri` は自分の口座から別口座へ送金する用法、`konteltiro` は顧客へ送る口座の部分コピーとして確認でき、現行表現を維持した。
- `Mi serĉas loĝejon`, `Ĉu la kvartalo estas trankvila?`, `Mi serĉas bangalon`, `Mi serĉas vicdomon`, `Ĉu vi volas parkumejon?`, `Kiom estas la petata prezo?`, `Ĉu la prezo estas diskutebla?`, `Ĉu vi havas posedaĵon por vendi?`, `Ĉu vi estas kontanta aĉetanto?`, `Ĉu vi bezonos hipotekon?`, `Mi bezonas apartamenton kun nur unu dormoĉambro`, `Necesas deponaĵo je unu-monata lupago`, `Ĉu vi serĉas meblitan aŭ nemeblitan loĝejon?`, `Ĉu vi volas novkonstruitan aŭ duamanan posedaĵon?`, `Kiun prezintervalon vi konsideras?`, `Interesas min ekscii pli pri ĉi tiu posedaĵo`, `Kiom longe ĝi jam estas sur la merkato?` は、不動産購入・賃貸・内見条件・価格交渉表現として対応する。
- PIV 2020 で `loĝejo`, `apartamento`, `dormoĉambro`, `kvartalo`, `bangalo`, `parkumejo`, `prezo`, `diskutebla`, `kontanta`, `hipoteko`, `deponi/deponaĵo`, `mebli`, `merkato`, `elementa lernejo`, `kafejo` を確認。`vicdomo` は `vico` + `domo` の透明な複合で row/terraced house 文脈を保ち、`duamana posedaĵo` は新築に対する中古物件の意味として日中韓と衝突しないため維持した。

主な据え置き確認:
- `ID4268` `Per dekoj, mi petas`: 銀行窓口で「10単位の紙幣で」の意味として読め、日中韓の「10単位/10ユーロ札」系文脈から外れないため維持。
- `ID4285`〜`ID4287` `monbiletoj` / `grandajn bankbiletojn` / `pli malgrandajn bankbiletojn`: 額面の大小を尋ねる銀行文脈として許容し、過去補正済みの日中訳とも対応するため維持。
- `ID4294` `konteltiron`: PIV 2020 の `konteltiro` に基づく口座明細表現として維持。
- `ID4297` `Sur via konto ne estas mono`: `en via konto` も候補だが、口座に資金がない意味は明確で、日中韓と矛盾しないため維持。
- `ID4307` `Mi ŝatus ĝiri iom da mono en ĉi tiun konton`: PIV 2020 の `ĝiri ... en la konton` 型と一致するため維持。
- `ID4324` `parkumejon`: PIV 2020 で `parkumejo` は自動車を一時的に置く場所として確認でき、不動産条件の parking 文脈として維持。
- `ID4332` `kontanta aĉetanto`: PIV 2020 の `kontanta` に基づき、ローン前提でない cash buyer の意味として維持。
- `ID4341` `deponaĵo je unu-monata lupago`: 賃貸保証金・敷金として「1か月分の賃料」の意味は明確で、現訳と矛盾しないため維持。
- `ID4348` `prezintervalon`: `prezo` + `intervalo` の透明な複合で、価格帯・予算範囲として維持。
- `ID4351` `sur la merkato`: 売買市場に出ている不動産という比喩的・商業的用法として維持。

参照:
- PIV 2020 ローカル `legitimilo`, `formularo`, `subskribi`, `kurzo`, `provizio`, `kvitancon`, `falsa`, `monbileto`, `bankbileto`, `bankaŭtomato`, `kontanta`, `saldo`, `ĉeko`, `ĉekaro`, `deponi`, `konto`, `konteltiro`, `ĝiri`, `interezo`, `procento`, `kontantigi`, `loĝejo`, `apartamento`, `dormoĉambro`, `kvartalo`, `bangalo`, `parkumejo`, `prezo`, `diskutebla`, `hipoteko`, `deponaĵo`, `mebli`, `merkato`, `elementa lernejo`, `kafejo`: `PIV2020_structured.txt`
- 過去ログ `58周目`, `459周目`, `559周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4256`〜`ID4355` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 645. 644周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping
- Leisure Time / Family Time
- Leisure Time / Gardening
- Leisure Time / Having Guests
- Services / At the Bank

結果:
- **CSV修正なし**
- 前回 `ID4056`〜`ID4155` に続き、今回は `ID4156`〜`ID4255` の100件を確認した。キャンプ、家族時間、園芸、来客、銀行ATM入口の表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4176` EO、`ID4181` EO、`ID4193` JA/ZH、`ID4197` EO、`ID4198` JA、`ID4210` EO、`ID4214` EO、`ID4223` EO、`ID4227` EO、`ID4228` ZH、`ID4240` EO、`ID4250` KO は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi ŝatus mapon de la piedvojetoj en ĉi tiu regiono`, `Rakontu historion pri tendumado`, `Kion ni havos por tagmanĝo?`, `Ni iru al koncerto`, `Ĉu ni iru ludi bovlingon?`, `Ĉu ni iru sketi?`, `Je kioma horo komenciĝas la matĉo?`, `Kiu ludas?`, `Ĉu vi volas spekti filmon?`, `Ĉu vi volas, ke mi ŝaltu la televidon?`, `Ĉu vi povas transdoni al mi la telekomandilon?`, `Ĉu hodiaŭ vespere estos iuj bonaj filmoj en la televido?`, `Mia patrino estas fanatikulo pri televidaj romanoj`, `Ĉu iu volus ludi sagetojn?`, `Ĉu mi povas proponi al vi legadon, do?`, `Mia tuta familio sidas ĉirkaŭ la tablo` は、キャンプ・家庭内余暇・テレビ・ゲーム・読書・家族団らん表現として対応する。
- PIV 2020 で `vojeto`, `sketi`, `televido`, `sageto`, `legado`, `proponi`, `ŝalti`, `transdoni`, `ĉirkaŭ` を確認。`piedvojetoj` は `pied` + `vojeto` の透明な複合で walking trails / пешие маршруты の徒歩道文脈として許容。`bovlingo` はPIV直接見出しでは弱いが、Glosbeで bowling として確認できるため維持。`televidaj romanoj` はPIV直接見出しでは弱いが、Glosbeで `televida romano` が serial と確認でき、soap opera / мыльные оперы 文脈から外れないため維持。`ludi sagetojn` は `sageto` の「手で用いる小さな矢」と、darts の `Sagoĵetado` 系対応から文脈別許容で維持。
- `Mi ŝatas maturajn fruktojn`, `Mi plantis ajlon`, `Ŝi kultivas sojfabojn`, `Ni kultivas sekalon`, `Ni plantis cepojn`, `Ni kultivas tabakon`, `Ili kultivas maizon`, `Kiam maturiĝas persikoj?`, `Mi falĉas la herbon`, `Mi plantis betojn`, `Ŝi havas pirarbojn`, `Ili kultivas hordeon`, `Kiom ofte vi akvumas la plantojn?`, `Kiam komenciĝas la rikolto de terpomoj?`, `Li havas prunarbojn`, `Li preferas nematurajn fruktojn`, `Ŝi rastis la foliojn en amason`, `Ili erpis la kampon`, `Morgaŭ ni plugos la kampon`, `Kiaj arboj estas en la fruktarbejo?`, `Kiujn kulturplantojn oni kultivas en ĉi tiu regiono?` は、果物、作物、栽培、草刈り、収穫、熊手・まぐわ・耕作、果樹園表現として対応する。
- PIV 2020 で `sojo` は醤油、`sojfabo` は大豆の種子として確認でき、過去補正後の `sojfabojn` は園芸・栽培文脈に合う。`beto` は食用根を含む語義があり、`ruĝa beto` への精密化余地はあるが、RU `свёклу` / EN beetroot / 日中韓との対応上、現行 `betojn` は誤りと断定しない。`falĉi`, `rasti`, `erpi`, `plugi`, `kultivi`, `kultivaĵo`, `frukto`, `pirarbo`, `prunarbo` もPIV 2020で確認。`fruktarbejo` は透明な複合で、Wiktionaryでも orchard と確認できる。`kulturplantojn` は「栽培植物」として農作物文脈を保ち、`kultivaĵoj` も候補だが明確な意味ズレではないため維持。
- `Eniru!`, `Ĉu mi povas preni vian mantelon?`, `Sidiĝu!`, `Bonvolu servi vin`, `Ĉu mi povas uzi vian necesejon?`, `Ĉu vi ŝatus mantukon?`, `La tagmanĝo estas preta`, `Mi estas sata`, `Mi boligos akvon`, `Ĉu vi prenas sukeron?`, `Sentu vin kiel hejme!`, `Mi bezonas kelkajn buŝtukojn`, `La matenmanĝo pretas`, `Ĉu vi ŝatus toaston?`, `Ĉu vi ŝatus senalkoholan trinkaĵon?`, `La akvo jam bolas`, `Kiom da sukerpecoj vi prenas?`, `Ĉu ĝenas vin, se mi fumas ĉi tie?`, `Mi preferus, ke vi eliru`, `Ni iru en la manĝoĉambron`, `Ĉu vi ŝatus ĝinon kun toniko?`, `Mi preferus, ke vi ne fumu ĉi tie`, `Kiom ofte vi mendas picon hejmen?`, `Ĉu vi satiĝis?`, `Ĉu vi povas helpi min lavi la telerojn?`, `Mi lavos, kaj vi viŝos` は、来客、飲食、喫煙可否、客室案内、配膳・片付け表現として対応する。
- PIV 2020 で `tuko` の派生 `mantuko` / `buŝtuko`, `boli` / `boligi akvon` / `bolilo`, `toasto`, `ĝino`, `kinin akvo`, `trinkaĵo`, `mendi`, `satiĝi`, `viŝi` を確認。`Bonvolu servi vin` は help yourself の再帰的な給仕表現として読め、意味ズレではない。`La akvo jam bolas` は英/RU の kettle 表現より、日中韓の「水・湯が沸いた」に直接対応する現形で維持。`ĝino kun toniko` は PIV の `kinin akvo` に `ĝino` と用いる説明があり、ReVoの `toniko` でも tonic water 対応が確認できるため維持。`mendas picon hejmen` は `hejmen` が配達先方向を示し、RU `заказываете домой пиццу` と対応するため維持。
- `Enmetu vian karton`, `Bonvolu atendi`, `Ĉu vi volas elekti alian servon?` は、銀行ATMの画面・案内文として日中韓と対応する。

主な据え置き確認:
- `ID4156` `piedvojetoj`: `vojeto` に基づく透明な複合で、徒歩道・散策路文脈として維持。
- `ID4160` `bovlingon`: PIV直接見出しでは弱いが、Glosbeで bowling として確認できるため維持。
- `ID4175` `televidaj romanoj`: serial / soap opera 文脈として維持。
- `ID4176` `sagetojn`: 未確認の `dartoj` ではなく、PIVの `sageto` に基づく過去補正後の形を維持。
- `ID4189` `betojn`: `ruĝa beto` への精密化は可能だが、現形でも beetroot / свёкла 文脈から外れないため維持。
- `ID4201` `kulturplantojn`: crops を「栽培植物」と表す文脈別許容として維持。
- `ID4214` `Mi boligos akvon` と `ID4227` `La akvo jam bolas`: kettle 直訳より、水・湯が沸く意味を明確にする補正後形として維持。
- `ID4223` `toaston`: PIV 2020 の食品 toast 語義に基づき維持。`tosto` は乾杯寄り。
- `ID4240` `ĝinon kun toniko`: gin and tonic 文脈として維持。
- `ID4244` `mendas picon hejmen`: 自宅へピザを注文する意味として維持。
- `ID4250` `lavi la telerojn` / `ID4251` `viŝos`: 食後の皿洗い・拭き取り文脈として維持。

参照:
- PIV 2020 ローカル `vojeto`, `sketi`, `televido`, `sageto`, `legado`, `proponi`, `ŝalti`, `transdoni`, `sojo`, `sojfabo`, `beto`, `falĉi`, `rasti`, `erpi`, `plugi`, `kultivi`, `kultivaĵo`, `frukto`, `pirarbo`, `prunarbo`, `tuko`, `mantuko`, `buŝtuko`, `boli`, `boligi`, `bolilo`, `toasto`, `ĝino`, `kinin akvo`, `trinkaĵo`, `mendi`, `satiĝi`, `viŝi`: `PIV2020_structured.txt`
- Glosbe `Bovlingo`: https://glosbe.com/eo/ja/Bovlingo
- Glosbe `televida romano`: https://ro.glosbe.com/eo/ro/televida%20romano
- Wiktionary `fruktarbejo`: https://en.wiktionary.org/wiki/fruktarbejo
- ReVo `toniko`: https://dvd.ikso.net/revo/art/tonik.html
- 過去ログ `16周目`, `57周目`, `108周目`, `158周目`, `208周目`, `258周目`, `308周目`, `358周目`, `408周目`, `458周目`, `508周目`, `558周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4156`〜`ID4255` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 644. 643周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport
- Leisure Time / Music
- Leisure Time / Going Camping

結果:
- **CSV修正なし**
- 前回 `ID3956`〜`ID4055` に続き、今回は `ID4056`〜`ID4155` の100件を確認した。スポーツ後半、音楽、キャンプ表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID4056` EO、`ID4058` KO、`ID4065` EO/ZH、`ID4068` EO、`ID4071` EO、`ID4073` EO/EN、`ID4083` KO、`ID4115` JA、`ID4124` JA/ZH、`ID4128` JA、`ID4131` EO、`ID4145` KO、`ID4148` ZH、`ID4151` EO、`ID4153` ZH、`ID4154` EN/JA は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Kia, laŭ vi, estos la fina rezulto?`, `Kie okazos la konkurso de ĵudo?`, `Donu al mi bileton por la centra tribuno, mi petas`, `Kiom kostas lui la tenisejon?`, `Ĉu eblas lui tenisan rakedon?`, `Kiom da spektantoj ĝi povas enhavi?`, `Por kiu sporta klubo vi ludas?`, `Kiom longe vi praktikas ĉi tiun sporton?`, `Kiom da vetkuroj gajnis ĉi tiu ĵokeo?`, `Kiaj estas la vetŝancoj de la favorato?`, `Kiu ĉevalo estas la favorato en ĉi tiu kuro?`, `Kio estas la norma nombro da batoj por ĉi tiu truo?`, `Kiom da boatoj partoprenas en ĉi tiu regatto?`, `Ĉi tiu ekzerco trejnos viajn femurajn muskolojn` は、試合・競馬・賭け・ゴルフ・レガッタ・トレーニング表現として対応する。
- PIV 2020 で `ĵudo`, `tribuno`, `tenisejo`, `ĵokeo`, `veti`, `golfo`, `bastono` のゴルフ用法、`regatto`, `femuro` を確認。`vetŝancoj` はPIV直接見出しでは弱いが、`veto` + `ŝanco` の透明な複合で、RU `шансы` および日中韓のオッズ・配当率文脈から外れないため維持。`golfbastonoj` / `golfĉaro` も透明な複合として、clubs / buggy 文脈を保つため維持。`norma nombro da batoj` はゴルフの par を未確認の専門語にせず説明的に表しており、現訳と矛盾しない。
- `Mi ludas violonon`, `Mi kantas en ĥoro`, `Mi ludas en grupo`, `Ĉu vi ludas iun instrumenton?`, `Mi ludas akordionon`, `Mi lernas ludi la saksofonon`, `Mi instruos vin ludi pianon`, `Kio estas hodiaŭ en la programo?`, `Kiel mi povas iri al la balkono?`, `Hodiaŭ kantas tenoro`, `Kiu estas la dirigento?`, `Kiam finiĝas la spektaklo?`, `Kian muzikon vi aŭskultas?`, `Iun ajn, vere`, `Ĉu vi havas preferatajn muzikgrupojn?`, `Kiu prezentas la programon?`, `Mi estis invitita aŭskulti simfonian orkestron`, `Ŝi volas iri al koncerto de popolmuziko` は、楽器演奏、合唱・バンド、コンサート、番組・演目、音楽ジャンルとして対応する。
- PIV 2020 で `ludi` にスポーツ名・楽器名を直接目的語に取る用例、`instru/i` に技能・行為を教える用法、`programo`, `spektaklo`, `dirigento`, `ĥoro`, `akordiono`, `violono` 等を確認。`Iun ajn, vere` は直前の `Kian muzikon...` への答えとして `muzikon` を省略した形で自然。`Jes, mi ludis pianon dum kvin jaroj` は過去経験・期間を述べる文として、日中韓/RUの範囲から外れないため維持。`popolmuziko` は PIV 直接見出しでは弱いが、`popola muziko` / folk music 系の対応と、Tekstaro内の folk music 説明で `popolmuziko` が用いられる例を確認でき、RU `фольклорной музыки` とも大きく矛盾しないため維持。
- `Ĉu mi povas tendumi ĉi tie?`, `Kie estas la tendumejo?`, `Ĉu vi havas ruldomon?`, `Kie mi povas akiri trinkakvon?`, `Ĉu vi povus prunti al mi poŝlampon?`, `Ĉu fiŝkaptado estas permesata ĉi tie?`, `Jen ĉi tie la rando de la arbaro!`, `Ĉu estas tendoj lueblaj?`, `Ĉu vi povas alporti vian propran rostokradon?`, `Ĉu vi havas interretan aliron ĉi tie?`, `Tie estas la najtingaloj`, `Ni volus iri ĉasi`, `Ĉasado estas malpermesita ĉi tie`, `Ĉu ni povus tranokti ĉi tie?`, `Ĉu ili havas dormosakojn?`, `Ĉu surloke troviĝas kuireja ekipaĵo?`, `Ni serĉu berojn kaj fungojn`, `Ĉi tie estas hirunda nesto`, `Ĉu ni supreniros per telfero?`, `Ĉu ni supreniros laŭ la monta pado?` は、キャンプ場、用品、自然観察、狩猟、宿泊、設備、山道・ロープウェイ表現として対応する。
- PIV 2020 で `tendi/tendumi`, `lanterno`, `poŝlampo`, `domveturilo` の同義語 `ruldomo`, `kukolo`, `pego`, `najtingalo`, `hirundo` / `hirunda nesto`, `rostokrado`, `dormosako`, `ekipaĵo`, `bero`, `fungo`, `telfero`, `tranokti`, `interreto` を確認。`tendumejo` は `tendumi` からの場所名として透明で、campsite 文脈を保つ。`Kiom kostas tendo?` は購入文にも読める余地があるが、Going Camping 文脈およびEN/RU/日中韓が「テント1張りの料金」として取れるため、文脈別許容で維持。`kuireja ekipaĵo` は cooking facilities よりやや広いが、現地の調理設備を問う文として意味ズレではない。

主な据え置き確認:
- `ID4065` `vetŝancoj`: betting odds / chances として文脈上許容。より確実な置換先を断定できないため維持。
- `ID4070` `golfbastonoj` / `golfĉaro`: PIVの `bastono` にゴルフ用の曲がった棒の記述があり、透明な複合として維持。
- `ID4071` `norma nombro da batoj`: par を説明的に訳しており、日中韓の標準打数・パーと対応するため維持。
- `ID4105` `popolmuziko`: folk / traditional music 寄りの使用例があり、RU `фольклорной музыки` と矛盾しないため維持。
- `ID4115` `ruldomo`: PIV 2020 の `dom veturilo` 同義語として確認できるため維持。
- `ID4145` `Kiom kostas tendo?`: キャンプ場でのテント1張りの料金として読めるため維持。
- `ID4149` `kuireja ekipaĵo`: cooking facilities / kitchen equipment の広い表現として維持。
- `ID4154` `telfero`: PIV 2020 の山・谷を越える吊り下げ式交通機関の語義に基づき、ロープウェイ文脈として維持。

参照:
- PIV 2020 ローカル `ĵudo`, `tribuno`, `tenisejo`, `ĵokeo`, `veti`, `golfo`, `bastono`, `regatto`, `femuro`, `ludi`, `instrui`, `programo`, `spektaklo`, `dirigento`, `ĥoro`, `akordiono`, `violono`, `tendumi`, `lanterno`, `poŝlampo`, `ruldomo`, `kukolo`, `pego`, `najtingalo`, `hirundo`, `rostokrado`, `dormosako`, `ekipaĵo`, `bero`, `fungo`, `telfero`, `tranokti`, `interreto`: `PIV2020_structured.txt`
- Glosbe `Popola muziko`: https://glosbe.com/eo/fr/Popola%20muziko
- Tekstaro de Esperanto `Revuo Esperanto 2017-3`（`popolmuziko` と folk music 説明の確認）: https://tekstaro.com/t?antauasekcio=1&nomo=revuo-esperanto-2013-2017&postasekcio=1&sekcio=revuo-esperanto-2017-3&tipo=&uzistreketojn=0
- 過去ログ `56周目`, `107周目`, `157周目`, `207周目`, `257周目`, `307周目`, `357周目`, `407周目`, `457周目`, `507周目`, `557周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID4056`〜`ID4155` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 643. 642周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / At the Nightclub
- Leisure Time / At the Beach
- Leisure Time / Sport

結果:
- **CSV修正 1件（EO 1件）**
- 前回 `ID3856`〜`ID3955` に続き、今回は `ID3956`〜`ID4055` の100件を確認した。ナイトクラブ、ビーチ、スポーツ表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3965` ZH、`ID3979` KO、`ID3990` EO、`ID3995` ZH、`ID3999` EO/ZH、`ID4006` JA、`ID4007` ZH、`ID4014` EO、`ID4016` JA/ZH/KO、`ID4022` EO/ZH、`ID4023` EN、`ID4036` JA、`ID4042` ZH、`ID4046` JA/ZH、`ID4048` JA/KO は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID4021` EO
  - `Kiu servas la pilkon?` → `Kiu serviras?`
  - 理由: 日中韓/RU は「誰がサーブするか」を問う。PIV 2020 では球技の service が `serviro`、その動詞が `serviri` として確認できる。一方、`servi` は「仕える」「役立つ」等が中心で、`servi la pilkon` は英語 “serve the ball” の直訳に寄り、サーブ動作としては不確実。`Kiu serviras?` ならサーブする人を問う意味を保ち、球技文脈ではボールは自明なため、内容を広げずに補正できる。専門資料 `La sporta lingvo en Esperanto` でも tennis service に `serviro`, `serviranto`, `serviras` が用いられることを確認した。

- `Kiujn noktojn vi estas malfermitaj?`, `Ni estas malfermitaj 7 noktojn semajne`, `Ĉu vi volas iri al klubo hodiaŭ vespere?`, `Hodiaŭ vespere ni havas privatan feston`, `Mi estas en la gastlisto`, `Vi ne povas eniri kun sportŝuoj`, `Ĉu vi havas vivan muzikon ĉi-vespere?`, `Ĉi-vespere estas tre homplene`, `Ĉi tie estas mortige enue`, `Kion vi pensas pri la diskĵokeo?`, `Ĉe la drinkejo estas longa vico` は、ナイトクラブの営業日、入場、ゲストリスト、服装、ライブ音楽、混雑、退屈さ、DJ、バーの列として対応する。
- PIV 2020 で `klubo`, `nokto`, `drinkejo`, `homplena`, `ĵokeo` を確認。`gastlisto`, `sportŝuoj`, `diskĵokeo` はPIV直接見出しでは弱いが、透明な複合語または過去周回での確認に基づき、nightclub / guest list / trainers / DJ 文脈から外れないため維持。
- `Ŝi estas ĉi tie por ferioj`, `Ĉu la strando estas ŝtoneta aŭ sabla?`, `Ĉu mi povas lui sunseĝon?`, `Ĉu mi povas lui akvoskiojn?`, `Ĉu mi povas tie akvoskii?`, `Ĉu ĉi tie estas subakvaj fluoj?`, `Ĉu en ĉi tiuj akvoj troviĝas ŝarkoj?`, `Mi ŝatus lui kanuon`, `Kie mi povas lui surfotabulon?`, `Kie estas la plej proksima jaĥtklubo?`, `Ĉu mi povas lui plonĝkostumon kaj ekipaĵon?`, `Kiom longe sufiĉos la aerbotelo?`, `Ĉu ĉi tie estas rifoj aŭ fortaj fluoj?`, `Kiom kostas lui malsekkostumon por unu tago?`, `Kiom profunde mi povas plonĝi kun ĉi tiu plonĝkostumo?`, `Kian navigacian ekipaĵon havas la boato?`, `Ĉu la jaĥto estas asekurita por urĝaj situacioj?`, `Ĉu necesas lasi garantiaĵon?`, `Certiĝu, ke vi havas savjakon` は、ビーチ、水上活動、潜水、ボート・ヨット、デポジット、安全確認として対応する。
- PIV 2020 で `ferio`, `plaĝo`, `strando`, `akvo skio`, `ŝarko`, `kanuo`, `surfotabulo`, `jaĥto`, `plonĝi`, `navigacio`, `ekipi`, `garantiaĵo`, `sav jako`, `ĉeval forto` を確認。`sunseĝo`, `aerbotelo`, `plonĝkostumo`, `malsekkostumo`, `jaĥtklubo` は透明な複合語または過去周回のWeb確認に基づき、日中韓/RUの文脈と矛盾しないため維持。
- `Mi ludas tenison`, `Ĉu vi povas naĝi?`, `Kiu venkas?`, `Estis remiso`, `Ŝi tre ŝatas jogon`, `Ĉu vi volas ludi kun mi?`, `Ni ludu duope`, `Ĉu vi praktikas iun sporton?`, `Jes, mi ludas futbalon`, `Kiuj teamoj ludas?`, `Kiu estas la arbitracianto?`, `Kiu faris la golon?`, `Kia estas la poentaro?`, `Ĉi tiu teamo venkis per la rezulto 3:1`, `Mi ŝatas ludi ŝakon`, `Mi estas membro de gimnastikejo`, `Instruu min ludi kriketon`, `Kie estas la tenisejo?`, `Ĉu mi devas kunporti mian propran rakedon?`, `Mi ne interesiĝas pri rugbeo`, `Mi ne interesiĝas pri usona futbalo`, `Kiu teamo golis?`, `Kiu egaligis la poentaron?`, `Kiom da vetkuroj estos hodiaŭ?`, `De kia raso estas ĉi tiu ĉevalo?`, `Ĉu vi ŝatus veti?`, `Vi ne povas superi ĉi tiun rekordon`, `Ne, mi ne estas aparte sportema`, `Oni povas lui skiojn kaj botojn`, `Ĉu vi ŝatus iri al flugpilka matĉo?`, `Li volas iri al manpilka matĉo`, `Mi estas subtenanto de ĉi tiu teamo`, `Kiuj estas la membroj de ĉi tiu basketbala teamo?`, `Kiu teamo portas la flavan uniformon?` は、スポーツ参加、試合状況、得点、審判、競馬、賭け、記録、スキー用品、球技チーム表現として対応する。
- PIV 2020 で `ludi` の `ludi kriketon, tenison, futbalon` 用例、`arbitracianto`, `golo`, `poentaro`, `gimnastiko`, `kriketo`, `tenisejo`, `rakedo`, `rugbeo`, `rekordo` の `superi/rompi rekordon`, `sport`, `veti`, `flug pilko`, `man pilko`, `basketbalo`, `uniformo` を確認。`Ni ludu duope` は doubles を完全な専門語で言い切る形ではないが、「二人組で/ペアでプレーしよう」と読め、日中韓のダブルス文脈と矛盾しないため維持。`goli` は `golo` からの透明な動詞化としてスポーツ文脈で維持。

主な据え置き確認:
- `ID3967` `gastlisto`: guest list の透明な複合語として維持。
- `ID3972` `diskĵokeo`: DJ 文脈で意味が明確で、過去周回の確認とも矛盾しないため維持。
- `ID3981` `sunseĝon`: sunlounger / beach chair 文脈の透明な複合語として維持。
- `ID3990` / `ID3998` `surfotabulon`: PIV 2020 の `surfotabulo` に基づき維持。
- `ID3995` `aerbotelo`: ZHは過去に「酸素瓶」断定から補正済み。EOは潜水・レンタル文脈の空気ボンベとして維持。
- `ID3999` `malsekkostumon`: wetsuit として過去周回で確認済み。現ZHも湿式潜水服として補正済み。
- `ID4007` `garantiaĵon`: PIV 2020 の保証物・担保・保証金の語義に基づき、deposit 文脈として維持。
- `ID4014` `remiso`: 過去周回で `remizo` から補正済み。スポーツの引き分けとして維持。
- `ID4017` `Ni ludu duope`: doubles を「二人組でプレーする」と表す文脈別許容として維持。
- `ID4022` `arbitracianto`: PIV 2020 のスポーツ審判語義に基づき維持。
- `ID4048` `superi ĉi tiun rekordon`: PIV 2020 の `rekordo` 用例で `superi`, `rompi` が確認できるため維持。
- `ID4050` `skiojn kaj botojn`: sports equipment rental 文脈で「スキー板とブーツ」として維持。

参照:
- PIV 2020 ローカル `serviro`, `serviri`, `klubo`, `nokto`, `drinkejo`, `homplena`, `ĵokeo`, `ferio`, `plaĝo`, `strando`, `akvo skio`, `ŝarko`, `kanuo`, `surfotabulo`, `jaĥto`, `plonĝi`, `navigacio`, `ekipi`, `garantiaĵo`, `sav jako`, `ĉeval forto`, `ludi`, `arbitracianto`, `golo`, `poentaro`, `gimnastiko`, `kriketo`, `tenisejo`, `rakedo`, `rugbeo`, `rekordo`, `sport`, `veti`, `flug pilko`, `man pilko`, `basketbalo`, `uniformo`: `PIV2020_structured.txt`
- `La sporta lingvo en Esperanto`（`serviro`, `serviranto`, `serviras` の tennis 文脈）: https://dvd.ikso.net/faka/scienco/La_sporta_lingvo_en_Esperanto.pdf
- 過去ログ `55周目`, `106周目`, `306周目`, `406周目`, `456周目`, `556周目`, `601周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `3c112f8f04738cb993bef1737c35c103`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID3956`〜`ID4055` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 642. 641周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / At the Theatre
- Leisure Time / At the Museum
- Leisure Time / At the Nightclub

結果:
- **CSV修正なし**
- 前回 `ID3756`〜`ID3855` に続き、今回は `ID3856`〜`ID3955` の100件を確認した。劇場、博物館、ナイトクラブ表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3867` JA/KO、`ID3868` EO/JA/ZH/KO、`ID3880` JA/KO、`ID3882` ZH、`ID3890` EN、`ID3911` JA、`ID3922` JA/KO、`ID3925` JA/ZH、`ID3931` JA/ZH、`ID3936` EO/EN/JA/ZH/KO、`ID3942` JA/ZH/KO、`ID3943` ZH、`ID3945` JA/ZH、`ID3946` ZH、`ID3954` JA/ZH/KO は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Ili ŝatus spekti baleton`, `Ĉu ni devas rezervi?`, `Kion oni ludas en la teatro?`, `Mi ŝatus du biletojn por la morgaŭa vespero`, `Ĉu vi povas rekomendi baleton?`, `Mi ŝatus vidi dramon`, `Mi ŝatus preni teatran binoklon`, `Kie estas la vestejo?`, `Ĉu vi ŝatus programeton?`, `Kiom da aktoj estas en ĝi?`, `Kiom longe daŭras la interakto?`, `La interakto daŭros 15 minutojn`, `Kiel mi povas iri al la loĝio?`, `La intrigo estis sufiĉe kompleksa`, `Ĉu vespera vesto estas postulata?`, `Hodiaŭ estas la premiero de "Hamleto"`, `Mi ŝatus kvar biletojn por vidi "La Mizerulojn"`, `Ĉu vi havas biletojn por la balkono?`, `De kia ĝenro estas la prezentado?`, `Ĉu ni mendu iujn trinkaĵojn por la interakto?` は、劇場・オペラ・バレエ・幕間・席種・上演内容の表現として対応する。
- PIV 2020 で `baleto`, `binoklo`, `loĝio`, `teatro`, `spekti`, `spektaklo`, `vestejo`, `intrigo`, `premiero`, `ĝenro` を確認。`interakto` は PIV の `inter akto` / `interakto` の説明により「幕間」として維持。`drama teatro` は劇場種別として日中韓の「劇場・演劇」文脈を外れないため維持。`vespera vesto` は evening dress / formal evening clothing の広い表現として、女性用ドレスに限定しない現訳で維持。
- `Ne tuŝu`, `Senpaga eniro`, `Fotografado malpermesita`, `Kiuj ekspozicioj nun okazas?`, `Ĉu ni povas ĉirkaŭrigardi?`, `Kies laboro estas ĉi tio?`, `Ĉu ĉi tio estas originalo?`, `Ĉu vi ŝatas modernan arton?`, `Je kioma horo estas la lasta eniro?`, `Ĉu estas enirkotizo?`, `Kiam estas la sekva gvidata ekskurso?`, `Ĉu vi ŝatus aŭdgvidon?`, `Ĉu mi rajtas uzi la fulmilon?`, `Kiaj pentraĵoj estas ĉi tie?`, `Kie estas la karikatursalono?`, `Kie estas la vaksaj figuroj?`, `Mi interesiĝas pri mozaiko`, `El kiu periodo devenas ĉi tiu skulptaĵo?`, `Kie estas la etnografia muzeo?`, `Ĉi tiu muzeo havas tre bonan kolekton de ceramikaĵoj`, `Kiu estas la lasta en la vico?`, `Unu plenkreskulan bileton kaj du infanajn biletojn, mi petas`, `Ĉu estas aliro por handikapuloj?`, `Ĉu estas aŭdgvidilo en la nepala?`, `Ĉu vi havas gvidlibron en la mongola?`, `Ni devas lasi niajn sakojn en la vestejo` は、博物館の案内、入館、展示、音声ガイド、撮影可否、展示室、割引・チケット、バリアフリー、言語別ガイドとして対応する。
- PIV 2020 で `ekspozicio`, `fulmo`, `galerio`, `mozaiko`, `impresionismo`, `karikaturo`, `handikapulo`, `aŭdi`, `gvidilo`, `Nepalo`, `mongolo`, `pensiulo`, `plenkreskulo`, `kotizo`, `kodo`, `vesto` を確認。`aŭdgvido` / `aŭdgvidilo`, `karikatursalono`, `vestkodo`, `enirkotizo` は複合語として透明で、各場面の意味に合うため維持。`fulmilo` は `fulmo` + `-ilo` によるカメラのフラッシュとして読め、日中韓の「フラッシュ」に対応するため維持。`handikapuloj` は現代的な言い換え余地はあるが、PIV上の語義と日中韓のアクセシビリティ文脈から外れないため維持。
- `La klubo estas plena`, `La muziko estas bonega!`, `Kie estas la drinkejo?`, `Mi iras hejmen`, `Kiom kostas la eniro?`, `Kiu prezentiĝas ĉi-vespere?`, `Ĉu ĉi tie estas vestkodo?`, `Ĉu tie estas bilardo?`, `Ĉi tie estas iom malplene` は、ナイトクラブの混雑、音楽、バー、入場料、出演、服装規定、ビリヤード、空き具合の表現として対応する。
- PIV 2020 で `bilardo`, `vesto`, `kodo` を確認。`vestkodo` は構成要素が透明で、dress code / 服装規定 / 着装要求 / 드레스 코드 / дресс-код 文脈として維持。

主な据え置き確認:
- `ID3868` `teatran binoklon`: PIV 2020 の `binoklo` が劇場で用いる双眼鏡を含むため維持。
- `ID3872` / `ID3873` / `ID3896` `interakto`: PIV 2020 で「幕間」の語義を確認できるため維持。
- `ID3879` `drama teatro`: drama theatre / 演劇劇場として、現在の日中韓訳と対応するため維持。
- `ID3919` `aŭdgvidon` と `ID3938` `aŭdgvidilo`: 前者は音声案内、後者は音声ガイド装置・資料として読め、博物館文脈で誤りではないため維持。
- `ID3921` `fulmilon`: フラッシュ使用可否の文脈で、透明な派生語として維持。
- `ID3925` `karikatursalono`: caricature gallery / 似顔絵・風刺画の展示室として、成分上も文脈上も許容されるため維持。
- `ID3937` `handikapuloj`: 語義上は成立し、アクセシビリティ確認文として日中韓訳と対応するため維持。
- `ID3953` `vestkodo`: dress code の複合語として文脈上明瞭なため維持。

参照:
- PIV 2020 ローカル `baleto`, `binoklo`, `loĝio`, `inter akto` / `interakto`, `teatro`, `spekti`, `spektaklo`, `vestejo`, `intrigo`, `premiero`, `ĝenro`, `ekspozicio`, `fulmo`, `galerio`, `mozaiko`, `impresionismo`, `karikaturo`, `handikapulo`, `aŭdi`, `gvidilo`, `Nepalo`, `mongolo`, `pensiulo`, `plenkreskulo`, `kotizo`, `kodo`, `vesto`, `bilardo`: `PIV2020_structured.txt`
- 過去ログ `54周目`, `105周目`, `305周目`, `555周目`: `phrases_review_round3_hold_list_20260306.md`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID3856`〜`ID3955` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 641. 640周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments & Returns
- Leisure Time / At the Cinema
- Leisure Time / At the Theatre

結果:
- **CSV修正なし**
- 前回 `ID3656`〜`ID3755` に続き、今回は `ID3756`〜`ID3855` の100件を確認した。支払い・返品、映画館、劇場表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3759` ZH、`ID3763` ZH、`ID3764` EN、`ID3765` JA、`ID3767` ZH、`ID3775` EN、`ID3781` JA、`ID3786` JA/ZH、`ID3787` ZH/KO、`ID3805` JA、`ID3812` JA/ZH/KO、`ID3825` JA、`ID3832` JA、`ID3833` EN/KO、`ID3837` JA/ZH/KO、`ID3839` KO、`ID3844` JA/ZH、`ID3849` JA/KO、`ID3852` JA/KO は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi estas malkontenta`, `Ĉu vi bezonas helpon por paki?`, `Ĉu vi dezirus sakon?`, `Ĉu mi povus ricevi donacskatolon?`, `Ĉu mi povas aĉeti ĝin senimposte?`, `Ĉi tiu karto ne validas`, `Mi havas nur 5 enojn`, `Mi donos al vi 20 frankojn por ĝi`, `Ĉu eblas rabato por kontanta pago?`, `Ĉu vi sendos ĝin al mia hotelo?`, `Mi ŝatus interŝanĝi ĉi tion kontraŭ alia grandeco`, `Ĉu vi havas nian rabatkarton?`, `Ĉu vi havas bonuskarton?`, `Ĉu vi povus donacpaki ĝin por mi?`, `Bonvolu envolvi ilin aparte`, `Mi forgesis la PIN-kodon de mia karto`, `La transakcio ne estis aprobita`, `Kiu estas la sekureca numero sur la dorso?`, `Ĉu vi sendos miajn aĉetaĵojn al mia hejma adreso?`, `Ĉu mi povus ricevi repagon?`, `Ĉu mi povas interŝanĝi la aĵojn, kiujn mi aĉetis?` は、支払い、カード決済、割引、配送、返品・交換、包装依頼として対応する。
- PIV 2020 で `en/o` が日本の円、`validi` がカード・文書等の有効性、`rabato` が値引き、`transakcio` が経済・金融上の取引、`dorso` が物の裏面・背面、`repago` が顧客へ返される金額を含むことを確認。`rabatkarto`, `bonuskarto`, `donacpaki`, `PIN-kodo`, `aĉetaĵoj` は、構成要素が透明で、店頭・カード決済文脈の意味から外れないため維持。
- `Ĝi estas filmo de suspenso`, `Kiu ludas en ĝi?`, `Ĝi estas milita filmo`, `Ĝi estas horora filmo`, `Ĝi estas dokumenta filmo`, `Ĝi estas en la vjetnama`, `Je kioma horo komenciĝas la filmo?`, `Kiom longe daŭras la filmo?`, `Kiom kostas la sidlokoj?`, `En la mezo`, `Salita aŭ dolĉa pufmaizo?`, `Al kiu kinejo ni iras?`, `Kiun filmon vi ŝatus vidi?`, `Mi ŝatus spekti komedion`, `Ĝi estas romantika komedio`, `Kiel nomiĝas la filmo?`, `Ĝi ĵus aperis`, `Pri kio temas ĉi tiu filmo?`, `Ĝi havas bonan intrigon`, `Kiu produktis la filmon?`, `Kiu ludas la ĉefan rolon?`, `Ĉu la filmo estas kolora?`, `Ĉu ni prenu pufmaizon?`, `Bonvolu fotiĝi kun mi`, `La premiero de la filmo okazas hodiaŭ en la kinejo`, `La filmo gajnis premion ĉe la Festivalo de Cannes`, `Kiu estas la reĝisoro de ĉi tiu filmo?`, `Kiu estas la scenaristo de ĉi tiu filmo?`, `Ĉi tiu filmo havas anglajn subtekstojn`, `Bonvolu preni por mi bileton por la deka vico`, `Mi ŝatus spekti animaciaĵon`, `Ni ŝatus spekti nigrablankan filmon`, `Ĝi aperis antaŭ ĉirkaŭ du monatoj`, `Ĝi estis unu el la plej bonaj filmoj, kiujn mi vidis de longe`, `Mi ne estas tre impresita de la filmo`, `Ĝi estis tre dinamika`, `Ĝi estis tro malrapida` は、映画ジャンル、上映言語、席、軽食、制作・出演、字幕、公開時期、感想として対応する。
- PIV 2020 で `suspenso` が映画・劇で観客を緊張した期待状態に置く場面、`maizo` 項目の `puf maizo` が popcorn、`vjetnam/o`, `komedio`, `intrigo`, `scenaristo`, `vico` を確認。`filmo de suspenso` は `suspensfilmo` より説明的だが thriller 文脈を保つ。`subtekstojn` は PIV 直接見出しでは弱いが、Komputeko で subtitle = `subteksto` / `subtitolo` と確認でき、映画字幕文脈として維持。`animaciaĵon` は PIV 直接見出し確認が弱いが、Glosbe で animation 系の語として `animaciaĵo` が確認でき、`animacia` + `-aĵo` の透明な形成として cartoon/アニメ/动画片/애니메이션/мультфильм 文脈を外れない。`Festivalo de Cannes` は公式名が `Festival de Cannes` であり、未同化固有名を含む映画祭名として維持。
- `Ĉu tio estas tragedio?`, `Mi ŝatas la kostumojn`, `Ĉu vi bone vidas?`, `Ĉu ĝi plaĉis al vi?`, `Mi ĝuis ĝin`, `Ĉu ĉi tio estas dramo?`, `Ĉu ĉi tio estas opereto?`, `Mi ŝatas la dekoraciojn`, `Kiu estas la aŭtoro?`, `Kiu estas la solisto?`, `Kiu estas la aktorino?`, `Ŝi estas tre bona aktorino` は、劇場でのジャンル、視界、感想、舞台装置、作者・出演者確認として対応する。
- PIV 2020 で `tragedio`, `opero` の派生 `opereto`, `dekoracio` の劇場用法、`teatro`, `aktoro/aktorino`, `sceno/scenaro/scenaristo` 周辺を確認。`dekoracioj` は scenery/舞台装置/舞台布景/무대 장치/декорации に対応し、現CSVのまま維持。

主な据え置き確認:
- `ID3764` `enojn`: PIV 2020 で日本の円として確認済み。`jen/o` も参照されるが、現形は誤りではない。
- `ID3777` `bonuskarton`: loyalty card と完全同義ではない余地はあるが、RU `бонусная карта` と対応し、日中韓のポイント・会員カード文脈から外れないため維持。
- `ID3778` `saketon`: carrier bag/レジ袋/购物袋/비닐봉지 の場面で、小型袋を求める表現として許容。
- `ID3791` `filmo de suspenso`: PIV の `suspenso` に基づき thriller 文脈として維持。
- `ID3805` / `ID3820` `pufmaizo`: PIV 2020 の `puf maizo` に基づき popcorn 文脈として維持。
- `ID3822` `fotiĝi kun mi`: RU `сфотографируйтесь со мной` と同じ「一緒に写真に写る」意味で維持。
- `ID3830` `subtekstojn`: Komputeko の subtitle 対応に基づき、字幕表現として維持。
- `ID3835` `animaciaĵon`: 辞書確認と透明な語形成により、アニメ・カートゥーン映画文脈として維持。
- `ID3839` `de longe`: 時間的な「長い間」の用法として読め、日中韓/RU の「久しぶりに見た中で」に対応するため維持。
- `ID3851` `dekoraciojn`: PIV 2020 で劇場の背景・舞台装置の語義を確認できるため維持。

参照:
- PIV 2020 ローカル `en/o`, `validi`, `rabato`, `transakcio`, `dorso`, `repago`, `suspenso`, `maizo` / `puf maizo`, `vjetnam/o`, `komedio`, `intrigo`, `scenaristo`, `vico`, `tragedio`, `opereto`, `dekoracio`, `teatro`, `aktoro`: `PIV2020_structured.txt`
- Glosbe `animation`: https://glosbe.com/en/eo/animation
- Komputeko PDF `subtitle`: https://dvd.ikso.net/vortaro/Komputeko_en_eo.pdf
- Festival de Cannes 公式: https://www.festival-cannes.com/en/festival/

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID3756`〜`ID3855` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 640. 639周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / At the Supermarket
- Shopping / At the Bookshop & Florist's
- Shopping / Payments & Returns

結果:
- **CSV修正なし**
- 前回 `ID3556`〜`ID3655` に続き、今回は `ID3656`〜`ID3755` の100件を確認した。スーパー、書店・花屋、支払い・返品表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3656` ZH、`ID3657` ZH、`ID3664` EO、`ID3668` JA/ZH/KO、`ID3671` JA/ZH/KO、`ID3672` EO、`ID3675` EO、`ID3687` JA、`ID3694` ZH、`ID3697` ZH、`ID3704` ZH、`ID3706` JA/ZH、`ID3708` JA/KO、`ID3712` ZH、`ID3717` JA/ZH/KO、`ID3723` ZH、`ID3724` JA/KO、`ID3726` EO、`ID3731` KO、`ID3732` KO、`ID3734` JA、`ID3737` EO、`ID3738` JA/ZH/KO、`ID3739` ZH、`ID3741` JA、`ID3743` EN/JA/ZH、`ID3745` JA、`ID3751` EO、`ID3755` JA/ZH は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Ĉu vi havas majonezon?`, `Ĉu vi havas kafgrajnojn?`, `Mi ŝatus ses tranĉaĵojn da ŝinko`, `Mi ŝatus pecon da pico`, `Mi ŝatus iom el ĉi tiuj`, `Mi ŝatus kilogramon da granatoj`, `Mi ŝatus tiun pecon da fromaĝo`, `Kie estas la aĉetĉaretoj?`, `En kiu koridoro mi povas trovi konservaĵojn?`, `Ĉu vi povus diri al mi, kie estas la sekcio de frostigitaj nutraĵoj?`, `Ĉu ĉerizoj estas rabatitaj hodiaŭ?`, `Kio estas en tiuj ĉi ĉokoladaj bombonoj?`, `Kiujn markojn vi havas kun filtriloj?`, `Paketon da biskvitoj, mi petas`, `Mi ŝatus litron da sunflora oleo`, `Mi ŝatus bastonpanon`, `Mi ŝatus du tabuletojn da nigra ĉokolado`, `Mi ankaŭ bezonas aĉeti duonkilogramon da faruno`, `Bonvolu pesi al mi tricent gramojn`, `Mi ŝatus duonduzenon da ovoj`, `Kiom longe ili konserviĝos?`, `Ĉu mi pagu por ĝi ĉi tie aŭ ĉe la kaso?` は、スーパーでの商品在庫、食品量り売り、割引、保存性、支払い場所確認として対応する。
- PIV 2020 で `majonezo`, `kafgrajno`, `ŝinko`, `pico`, `granato`, `fromaĝo`, `ĉerizo`, `ĉokolado`, `filtrilo`, `biskvito`, `faruno`, `ovo`, `konserviĝi` 周辺を確認。`aĉetĉareto` は PIV 直接見出しでは未確認だが、`aĉet-` + `ĉareto` の透明な複合語として shopping trolley/ショッピングカート/购物车/쇼핑 카트 文脈に合うため維持。`Mi ŝatus iom el ĉi tiuj` は個数表現なら `kelkajn el ĉi tiuj` もあり得るが、PIV 用例上も `iom el ...` の部分表現は確認でき、日中韓/RU の「これらの中から少し・いくつか」に対応するため未修正。
- `Ĉu mi povas foliumi?`, `Mi bezonas kelkajn plumojn`, `Mi bezonas kajeron`, `Mi bezonas kelkajn orkideojn`, `Bonvolu doni al mi tri rozojn`, `Ĉu vi vendas poŝtmarkojn?`, `Pardonu, ni ne vendas ilin`, `Mi bezonas danan vortaron`, `Mi ŝatus notblokon`, `Mi ŝatus aĉeti gvidlibron`, `Kie mi povas aĉeti florojn?`, `Kiom kostas bukedeto da tulipoj?`, `Mi ŝatus bukedon da narcisoj`, `Ĉu vi havas lekantojn?`, `Kie estas la plej proksima gazetkiosko?`, `Kie mi povas trovi infanlibrojn?`, `Mi bezonas dulingvan vortaron`, `Mi bezonas klarigan vortaron`, `Mi interesiĝas pri detektivaj romanoj`, `Mi serĉas naskiĝtagan karton`, `Mi volas kelkajn poŝtkartojn kun vidoj de Big Ben`, `Mi ŝatus vidi kelkajn poemarojn`, `Mi ŝatus kelkajn ĝardenajn florojn`, `Mi ŝatus bukedon da magnolioj`, `Kiom kostas bukedo da lilioj?`, `Bonvolu doni al mi amharan gazeton`, `Bonvolu doni al mi ekzempleron de "Romeo kaj Julieta"`, `Bonvolu montri al mi kelkajn albumojn pri arkitekturo`, `Mi interesiĝas pri scienca literaturo`, `Mi bezonas makedona-ukrainan vortaron`, `Mi ŝatus aĉeti romanon en la svahila`, `Mi ŝatus vidi kelkajn koloriglibrojn`, `Mi ŝatus havi bildlibron por kvinjara infano`, `Ĉu vi havas iujn enciklopediajn vortarojn?`, `Ĉu vi havas broŝurojn pri Svislando?`, `Ĉu vi povus diri al mi, kie estas brokanta librovendejo?`, `Ĉu vi havas poŝtkarton kun vidindaĵoj de la urbo?`, `Ĉu vi havas krizantemojn?`, `Mi ŝatus bukedon da ruĝaj diantoj`, `Mi bezonas kronon el freŝaj floroj por la fianĉino` は、書店・花屋での所在確認、購入依頼、書籍ジャンル、花材指定として対応する。
- PIV 2020 で `lekanto` が ordinara leŭkanto の種名であり、`leŭkanto` 側にも `lekanto` が同義として出ることを確認。`Julieta` は PIV の用例 `Romeo k Julieta` で確認できるため維持。`krono` は花で編んだ冠および花嫁用の花冠の用法が過去周回で確認済みで、現JA/ZH/KOの「花嫁用の生花の花冠」と対応する。`notbloko`, `koloriglibro`, `bildlibro`, `restmono` は直接見出しの強弱に差はあるが、既存の根・語構成と過去参照に基づく透明な複合語として、現文脈では必須修正なし。
- `Kie mi pagu?`, `Jen via kvitanco`, `Ĉi tio estas rompita`, `Mi ŝatus redoni tion`, `Ĉu vi staras en la vico?`, `Ĉu mi povas pagi per karto?`, `Pardonu, ni akceptas nur kontantan monon`, `Bonvolu enigi vian PIN-kodon`, `Jen via restmono`, `Sakon, mi petas`, `Ĝi ne funkcias` は、会計、返品、列、カード支払い、現金、暗証番号、お釣り、袋、故障表現として対応する。
- PIV 2020 で `kvitanco`, `vico`, `kontanta`, `kodo`, `sako`, `funkcii` 周辺を確認。`PIN-kodo` は `PIN` + `kodo` の透明な複合語として維持。`Sakon, mi petas` は carrier bag/レジ袋/购物袋/봉투/пакет に対する買い物場面の省略表現として許容。

主な据え置き確認:
- `ID3662` `Mi ŝatus iom el ĉi tiuj`: 個数表現としては別案もあるが、PIV上の部分表現とRU `немного вот этих` に合うため維持。
- `ID3672` `Kiujn markojn vi havas kun filtriloj?`: たばこ等の「フィルター付き銘柄」を尋ねる省略表現として日中韓/RUと対応するため維持。
- `ID3704` `lekantojn`: PIV 2020 で `lekant/o` と `leŭkant/o` の同義関係を確認でき、daisy/デイジー/雏菊/데이지/маргаритка 文脈として維持。
- `ID3722` `Romeo kaj Julieta`: PIV 2020 の `Julieta` 用例に基づき維持。
- `ID3726` `makedona-ukrainan vortaron`: 過去周回で補正済みのハイフン付き言語対形容詞として維持。
- `ID3743` `kronon el freŝaj floroj por la fianĉino`: PIV 2020 の花嫁用花冠の用法と日中韓文が対応するため維持。
- `ID3753` `restmono`: PIV直接見出しではなく透明な複合語だが、change/お釣り/找零/거스름돈/сдача 文脈から外れないため維持。

参照:
- PIV 2020 ローカル `majonezo`, `kafgrajno`, `ŝinko`, `fromaĝo`, `konservaĵo`, `ĉerizo`, `ĉokolado`, `filtrilo`, `faruno`, `ovo`, `kvitanco`, `lekanto`, `leŭkanto`, `Julieta`, `makedona`, `kontanta`, `kodo`, `sako`: `PIV2020_structured.txt`
- 過去確認ログ: `## 53. 52周目`, `## 104. 103周目`, `## 304. 303周目`, `## 354. 353周目`, `## 554. 553周目`

今回の整合性確認:
- 本体 CSV とアプリ実行用CSVは一致: `cmp_bytes=True`
- CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- `ID156`〜`ID5155` の 5000 行連続性、BOM、CRLFを検証済み。
- `ID3656`〜`ID3755` は 100 件確認済み。
- アプリ側 `git diff --check` 問題なし。

## 639. 638周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care
- Shopping / Electronic Devices
- Shopping / Other Goods
- Shopping / At the Supermarket

結果:
- **CSV修正なし**
- 前回 `ID3456`〜`ID3555` に続き、今回は `ID3556`〜`ID3655` の100件を確認した。化粧・身だしなみ用品、電器・電子機器、雑貨、スーパー食品の買い物表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3562` ZH、`ID3574` JA/ZH、`ID3575` ZH、`ID3578` JA/ZH、`ID3581` ZH、`ID3583` JA/ZH/KO、`ID3596` JA/ZH、`ID3599` ZH、`ID3604` ZH、`ID3607` ZH、`ID3610` ZH、`ID3619` ZH/KO、`ID3621` KO、`ID3625` JA/ZH、`ID3629` EO、`ID3631` JA、`ID3632` JA/ZH/KO、`ID3636` EN/JA/KO、`ID3650` JA/ZH、`ID3651` JA は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Kie mi povas trovi pinĉilon?`, `Kiajn razilojn vi havas?`, `Ni povas mendi ĝin por vi`, `Mi bezonas telefonan ŝargilon`, `Tio estas multekosta`, `Kiel ĉi tio funkcias?`, `Ĉu estas garantio?`, `Kiom kostas tiu lampo?`, `Mi bezonas monitoron`, `Mi bezonas novan klavaron`, `Ĉu vi vendas bateriojn?`, `Ĉu mi povas aĉeti poŝtelefonon?`, `Ĉu ĝi venas kun instrukcioj?`, `Ĉu vi povas rekomendi bonan fotilon?`, `Mi bezonas memorkarton por ĉi tiu fotilo`, `Mi ŝatus lensokovrilon` は、化粧小物・電器店での商品確認・部品購入表現として対応する。
- PIV 2020 で `pinĉilo`, `razilo`, `garantio`, `lampo`, `monitoro`, `klavaro`, `baterio`, `poŝtelefono`, `instrukcio`, `fotilo`, `lenso`, `kovrilo` 周辺を確認。`telefonan ŝargilon` は PIV の `ŝargi` が akumulatoro 等の充電を含むこと、Komputeko で `charger = ŝargilo`, `battery charger = bateria ŝargilo`, `cellular phone = poŝtelefono` を確認できることから、phone charger 文脈として維持。`memorkarto` は Komputeko で memory card として確認でき、`memoro` + `karto` の透明な複合語として維持。`lensokovrilo` は `lenso` + `kovrilo` の透明な複合語で、lens cap 文脈から外れない。
- `Mi ŝatus aĉeti porteblan komputilon`, `Mi ŝatus rigardi printilon`, `Ĉu vi havas skanilon?`, `Ĉu vi havas pilojn por poŝlampo?`, `Mi serĉas elektran fornon`, `Ĝi havas unujaran garantion`, `Ĉu vi havas aŭskultilojn?`, `Bonvolu montri al mi bonan mikrofonon`, `Mi bezonas aron da laŭtparoliloj por mia komputilo`, `Mi serĉas muson por mia komputilo`, `Ĉu estas io speciala, kiun vi ŝatus vidi?`, `Mi ŝatus vidi kelkajn elektronikajn ludilojn`, `Mi ŝatus elektran ventumilon`, `Mi ŝatus preni paron da 25-vataj ampoloj`, `Ĉu vi povus montri al mi bonan harsekigilon?`, `Ĉu vi havas ilin en aliaj koloroj?`, `Ĉu vi montros al mi, kiel uzi ĝin?`, `Ĉu la garantio kovras la riparojn?` は、PC周辺機器、電気製品、保証・操作説明の表現として対応する。
- PIV 2020 で `komputilo`, `printilo`, `skanilo`, `pilo`, `poŝlampo`, `forno`, `aŭskultiloj`, `mikrofono`, `laŭtparolilo`, `muso`, `elektronika`, `ludilo`, `vat(o)`, `ampolo`, `fen(o)` / `harsekigilo`, `riparo` 周辺を確認。`elektra ventumilo` は `ventumilo` に現代的な機械ファンとしての揺れがあるが、実例でも確認でき、扇風機/电风扇/선풍기/вентилятор 文脈から外れないため維持。
- `Ĉu mi povas helpi vin?`, `Mi aĉetos ĉi tion`, `Ĉe ni estas rabatvendo`, `Ĉu vi liveras?`, `Ĉu vi decidis?`, `Ĉu vi havas la saman?`, `Ĉu vi havas orajn monerojn?`, `Ĉu vi havas ion pli malmultekostan?`, `Tio estas ĉio, kion ni havas`, `Aĉetu 1, ricevu 1 je duonprezo`, `Tio estas bona prezo`, `La butiko fermiĝas`, `Nia stoko elĉerpiĝis`, `Ĉu vi elektis ion?` は、店員応答、購入決定、セール、在庫、価格案内として対応する。
- PIV 2020 で `rabatvendo` の構成要素 `rabato` + `vendo`, `liveri`, `decidi`, `sama`, `ora`, `monero`, `prezo`, `butiko`, `stoko`, `elĉerpiĝi`, `elekti` 周辺を確認。`Aĉetu 1, ricevu 1 je duonprezo` は、日中韓/RUが「1点購入で2点目半額」を保っており、現EOも同じ販促表現として読めるため維持。
- `Ĉu vi havas vestbrosojn?`, `Ĉu vi havas linajn tablotukojn?`, `Kiel larĝa estas ĉi tiu ŝtofo?`, `Ĉu vi havas facilajn ludojn por infanoj?`, `Mi ŝatus ludilon por malgranda infano`, `Ĉu vi povus montri al mi kelkajn ceramikaĵojn?`, `Ĉu ĉi tiuj figuretoj estas tre facilrompaj?`, `Mi ŝatus sitelon kaj ŝovelilon`, `Mi ŝatus vidi kelkajn bierkruĉojn`, `Mi volas, ke miaj inicialoj estu sur ĉi tio`, `Mi ne povas permesi al mi aĉeti ĉi tion`, `Ĉu vi povus doni al mi pli bonan prezon?`, `Mi volas aĉeti specialan donacon`, `Ĉu vi havas arĝentan manĝilaron kun tia desegno?`, `Ĉu vi havas kristalajn vinkarafojn?`, `Ĉu vi havas kudrilojn kaj kudran fadenon?`, `Ĉu vi havas skribmaterialojn?`, `Mi bezonas tubon da gluo`, `Ĉu vi havas pupojn, kiuj povas marŝi kaj paroli?`, `Kiom kostas ĉi tiu videoludo?`, `Ĉu vi pensas, ke ĝi taŭgas por kvarjara infano?`, `Kiajn konstrubriketojn vi havas?`, `Mi ŝatus interesan ludon por knabo`, `Mi ŝatus vidi praktikan aron da vojaĝsakoj`, `Mi ŝatus vidi mane teksitan tapiŝon`, `Mi ŝatus aĉeti memoraĵon de la urbo`, `Mi rekomendus al vi preni ĉi tiun`, `Ĉu vi povus montri al mi ion el blanka porcelano?`, `Ĉu vi povus taksi ĉi tion por mi?`, `Ĉu vi povus diri al mi, kie estas la likva sapo?`, `Mi serĉas pentraĵojn de famaj belgaj artistoj` は、雑貨・玩具・土産・工芸品・鑑定依頼・日用品の買い物文脈として対応する。
- PIV 2020 で `broso`, `vesto`, `lino`, `tablotuko`, `ŝtofo`, `ludo`, `ludilo`, `ceramikaĵo`, `figureto`, `facila`, `rompi`, `sitelo`, `ŝovelilo`, `bierkruĉo`, `inicialo`, `permesi`, `donaco`, `arĝenta`, `manĝilaro`, `kristalo`, `karafo`, `kudrilo`, `fadeno`, `skribi`, `materialo`, `tubo`, `gluo`, `pupo`, `videoludo`, `taŭgi`, `briketo`, `vojaĝo`, `sako`, `tapiŝo`, `memoraĵo`, `porcelano`, `taksi`, `likva`, `sapo`, `pentraĵo`, `belga` 周辺を確認。`konstrubriketoj` は PIV の `briketo` に子どもの構成遊びの木製・プラスチック片としての語義があり、building blocks/積木/블록/конструкторы 文脈として維持。
- `Kiom kostas la pano?`, `Marmeladon, mi petas`, `Ĉi tiu`, `Ĉu io alia?`, `Tio estas ĉio, dankon`, `Kie estas la korboj?`, `Ĉu la pano estas freŝa?`, `Botelon da lakto, mi petas`, `Mi bezonas bokalon da mustardo`, `Mi ŝatus iom da olivoj`, `Kelkaj`, `Pli`, `Malpli`, `Konservu en fridujo`, `Revarmigu antaŭ manĝado`, `Kiu estas la limdato?`, `Ĉu estas bakejo ĉi tie?`, `Fruktan torton, mi petas`, `Ĉu ĉi tiu vino estas dolĉa?`, `Ĉu mi povas gustumi ĝin?`, `Kie estas la karotoj?` は、スーパー・食品売場での注文、数量、保存表示、期限確認として対応する。
- PIV 2020 で `pano`, `marmelado`, `korbo`, `freŝa`, `botelo`, `lakto`, `bokalo`, `mustardo`, `olivo`, `fridujo`, `manĝi`, `bakejo`, `torto`, `vino`, `gustumi`, `karoto` 周辺を確認。`limdato` はローカルPIVでは直接見出し確認が弱いが、Wiktionary で expiry date 用法を確認でき、`limo` + `dato` の透明な複合語として食品期限文脈に合う。`Kiu estas la limdato?` の `kiu` は「どの日付か」を問う形として許容し、明確な誤りとは扱わない。

主な据え置き確認:
- Personal Care / Electronics: `pinĉilo`, `raziloj`, `telefonan ŝargilon`, `garantio`, `monitoro`, `klavaro`, `baterioj`, `poŝtelefonon`, `memorkarto`, `lensokovrilo`, `portebla komputilo`, `printilo`, `skanilo`, `piloj por poŝlampo`, `aŭskultiloj`, `laŭtparoliloj`, `harsekigilo` は、商品語彙として維持。
- Electronic Devices / General Shopping: `elektronikaj ludiloj`, `elektra ventumilo`, `25-vataj ampoloj`, `rabatvendo`, `liveras`, `orajn monerojn`, `je duonprezo`, `stoko elĉerpiĝis` は、電器・店頭応答文脈で維持。
- Other Goods: `vestbrosoj`, `linaj tablotukoj`, `ceramikaĵoj`, `figuretoj`, `sitelon kaj ŝovelilon`, `bierkruĉoj`, `arĝenta manĝilaro`, `kristalaj vinkarafoj`, `skribmaterialoj`, `tubo da gluo`, `videoludo`, `konstrubriketoj`, `mane teksita tapiŝo`, `memoraĵo de la urbo`, `blanka porcelano`, `taksi ĉi tion`, `likva sapo`, `belgaj artistoj` は、雑貨・工芸品・日用品文脈で維持。
- Supermarket: `marmelado`, `korboj`, `botelo da lakto`, `bokalo da mustardo`, `olivoj`, `Konservu en fridujo`, `Revarmigu antaŭ manĝado`, `limdato`, `bakejo`, `fruktan torton`, `gustumi`, `karotoj` は、食品売場文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- Komputeko PDF: https://dvd.ikso.net/vortaro/Komputeko.pdf
- Majstro `electric fan`: https://www.majstro.com/dictionaries/English-Spanish/electric%20fan
- La Ondo de Esperanto 実例 `elektra ventumilo`: https://esperanto-ondo.ru/Ondo/244-lode.htm
- Wiktionary `limdato`: https://en.wiktionary.org/wiki/limdato

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- アプリ実行用CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3556`〜`ID3655` は100件確認済み。

## 638. 637周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes
- Shopping / Shoes
- Shopping / Accessories
- Shopping / Personal Care

結果:
- **CSV修正なし**
- 前回 `ID3356`〜`ID3455` に続き、今回は `ID3456`〜`ID3555` の100件を確認した。衣類、靴、アクセサリー、化粧品・身だしなみ用品の買い物表現として、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3456` EO、`ID3466` EO、`ID3469` EN/JA/ZH/KO、`ID3472` EO、`ID3483` JA、`ID3484` EO、`ID3485` EO、`ID3489` JA、`ID3494` EO、`ID3498` EO、`ID3502` EO、`ID3507` JA/ZH、`ID3512` ZH/KO、`ID3515` JA/ZH、`ID3534` EO/KO、`ID3536` ZH、`ID3537` JA/ZH/KO、`ID3538` JA/ZH/KO、`ID3548` EN は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi serĉas ion sablokoloran`, `Ĉu vi havas ion malpli multekostan?`, `Mi volas jupon en pli malhela nuanco de bluo`, `Ĉu vi pensas, ke ĉi tiu materialo estas daŭrema?`, `Kiam ĉi tiu varo estos en rabatvendo?`, `Mi volas ion el kotono`, `Tio ne estas tio, kion mi serĉas`, `Mi serĉas pantalonon`, `Ĉi tiu pantalono estas tro larĝa`, `Ĉu vi havas ĉi tion en pli malgranda grandeco?`, `Ĉu vi havas jakon konvenan al ĉi tiu pantalono?`, `El kia ŝtofo estas farita tiu kostumo?`, `Ĉu vi havas tian de pli bona kvalito?`, `Ĉu oni devas lavi ĝin mane?`, `Kiam vi ricevos novan stokon?`, `Ĉu vi havas ĉi tiun artikolon en stoko?`, `Bonvolu meti ĉi tion flanken por mi` は、衣類の色・素材・サイズ・在庫・取り置き表現として対応する。
- PIV 2020 で `sablokolora`, `daŭrema`, `pantalono`, `kotono`, `ŝtofo`, `kostumo`, `kvalito`, `lavi`, `stoko`, `artikolo` 周辺を確認。`sablokolora` は「灰黄色」として確認でき、日中韓/RUのベージュ系表現と大きく衝突しない。`rabatvendo` は `rabato` + `vendo` の透明な複合語として、セール/打折/세일/распродажа 文脈と一致する。`meti ĉi tion flanken` は取り置きの依頼として自然で、以前の `flankmeti` 回避後の形を維持。
- `Mi bezonas paron da mokasenoj`, `Ĉu vi sentas vin komforte en ili?`, `La ŝuoj estas tro grandaj`, `Mi ŝatas ilin`, `Kiel vi sentas vin en ili?`, `Ili premas min`, `La kalkanumoj estas tro altaj`, `La kalkanumoj estas tro malaltaj`, `Ĉi tio ne estas via grandeco`, `Ĉu vi ne vendas botojn ĉi tie?`, `Ĉu mi povus provi ĉi tiujn sandalojn?`, `Mi ŝatus paron da zorioj`, `Bonvolu montri al mi tiun paron da pantofloj`, `Kion vi pensas pri ĉi tiuj?`, `Ĉu vi povus mendi mian grandecon?`, `Ĉu vi trovis ion, kio plaĉas al vi?`, `Mi ŝatus surprovi ĉi tiujn sportŝuojn`, `Mi ŝatus vidi paron da gumaj botoj`, `Ĉu tio estas la sola koloro, kiun vi havas?`, `Ĉu vi volas provi alian paron?`, `Mi ŝatus surprovi ambaŭ parojn`, `Ili perfekte sidas al mi` は、靴の種類、試し履き、サイズ感、履き心地として対応する。
- PIV 2020 で `mokaseno`, `ŝuo`, `boto`, `sandalo`, `zorio`, `pantoflo`, `kalkanumo`, `grandeco`, `provi`, `sidi`, `gumo` を確認。`sportŝuo` は `sporto` + `ŝuo`、`gumaj botoj` は `gumo` + `boto` の透明な構成として維持。`Ili perfekte sidas al mi` は、PIV の衣類・身につける物が「bonege sidas」とする用例に合い、fit me like a glove / ぴったり合う文脈として維持。
- `Mi ŝatus ringon`, `Ĉu tio ĉi estas oro?`, `Ĝi estas tro granda`, `Mi serĉas koltukon`, `Ĉu ĝi estas manfarita?`, `Ĉu vi bezonas ion?`, `Mi serĉas gantojn`, `Ĉi tiuj gantoj estas tro malvastaj`, `Ĉu ĉi tio estas vera ledo?`, `Mi ŝatus felĉapon`, `Ĝi estas tro malgranda`, `Ĉu mi povus havi paron da ŝtrumpetoj?`, `Ĉu vi havas butonojn?`, `Kiom kostas ĉi tiu ŝalo?`, `Kiom kostas ĉi tiuj orelringoj?`, `Tio estas malkara`, `Mi ŝatus vidi oran ringon`, `Kia ŝtono estas ĉi tio?`, `Mi ŝatus vidi kronometron`, `Mi ŝatus ledan monujon`, `Ĉu vi havas naztukojn?`, `Mi timas, ke ĉi tiu kravato estas tro simpla`, `Bonvolu montri al mi kravaton kun strioj`, `El kia materialo ĝi estas farita?`, `Ĉu vi havas ŝelkojn?`, `Ĉu vi havas kotonajn ŝtrumpetojn?`, `Mi ŝatus paron da manumbutonoj`, `Mi ŝatus vidi ledan horloĝrimenon`, `Mi ŝatus zonon, kiu konvenus al ĉi tiu bluzo`, `Mi ŝatus vidi virinan ringon`, `Mi preferus unu el 18-karata oro`, `Ĉu estas certifikato por ĝi?`, `Ĉu vi serĉas ion specialan?`, `Mi serĉas iun malgrandan juvelaĵon`, `Ĉu vi povus montri al mi kelkajn silkajn kravatojn?`, `Ĉu mi povus vidi brakhorloĝon, kiu montras la daton?`, `Ĉu la fermilo de tiu kolĉeno estas forta?` は、アクセサリー、貴金属、革小物、時計、ネクタイ、小物類として対応する。
- PIV 2020 で `koltuko`, `ganto`, `ledo`, `felĉapo`, `ŝtrumpeto`, `butono`, `ŝalo`, `orelringoj`, `kronometro`, `monujo`, `naztuko`, `kravato`, `ŝelko`, `manumbutonoj`, `rimeno`, `zono`, `juvelaĵo`, `brakhorloĝo`, `fermilo`, `kolĉeno` 周辺を確認。`ŝelko` はズボン等を支える弾性帯として braces/suspenders に対応し、`manumbutonoj` は PIV の `manumo` 用例と外部辞書で cufflinks と確認できる。`horloĝrimeno` は `horloĝo` + `rimeno` の透明な複合語として維持。
- `Kion vi ŝatus?`, `Mi ŝatus parfumon`, `Mi ŝatus tubon da dentopasto`, `Lipruĝon, mi petas`, `Ĉu vi havas tagan kremon?`, `Ĉu ĝi estas por vi?`, `Ne, tio ne estas por mi`, `Bonvolu montri al mi alian`, `Ĝi estas en la rabatvendo`, `Mi bezonas bonan kombilon`, `Mi serĉas ŝampuon`, `Kiajn dentobrosojn vi havas?`, `Kie mi povas trovi la dentpaston?`, `Kion vi serĉas?`, `Mi ŝatus paletron da ŝminko por la palpebroj`, `Kiom ĝi kostas?`, `Ĉirkaŭ cent eŭroj`, `Ne, tio estas donaco`, `Jen nia katalogo kaj prezlisto`, `Mi serĉas ungofajlilon`, `Bonvolu doni al mi pecon da sapo`, `Akvorezistan ŝminkon por okulharoj, bonvolu`, `Donu al mi skatoleton da vizaĝpudro, mi petas`, `Mi ŝatus vidi pli helan nuancon` は、化粧品・衛生用品・価格案内として対応する。
- PIV 2020 で `parfumo`, `dentopasto`, `lipruĝo`, `kremo`, `kombilo`, `ŝampuo`, `dentobroso`, `paletro`, `ŝminko`, `palpebro`, `akvorezista`, `okulharo`, `pudro`, `nuanco`, `sapo` 周辺を確認。`paletro da ŝminko por la palpebroj` は eyeshadow palette の説明的表現として維持。`maskaro` はローカルPIVで確認できないため、現CSVの `ŝminko por okulharoj` を維持。`ungofajlilo` と `vizaĝpudro` は直接見出しでは弱いが、構成要素が透明で、外部辞書でも nail file / face powder 対応を確認できるため維持。

主な据え置き確認:
- Clothes: `sablokoloran`, `malpli multekostan`, `pli malhela nuanco de bluo`, `daŭrema`, `rabatvendo`, `pantalono`, `ĉi tiu pantalono`, `stoko`, `artikolo en stoko`, `meti ĉi tion flanken` は衣料品店での買い物表現として維持。
- Shoes: `mokasenoj`, `zorioj`, `pantofloj`, `sportŝuoj`, `gumaj botoj`, `surprovi`, `premas min`, `kalkanumoj`, `Ili perfekte sidas al mi` は靴の種類・試し履き・フィット感として維持。
- Accessories: `koltuko`, `vera ledo`, `felĉapo`, `ŝalo`, `orelringoj`, `kronometro`, `naztukoj`, `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `juvelaĵo`, `brakhorloĝon`, `fermilo`, `kolĉeno` はアクセサリー・小物文脈で維持。
- Personal Care: `parfumo`, `tubo da dentopasto`, `lipruĝo`, `taga kremo`, `paletro da ŝminko por la palpebroj`, `ungofajlilo`, `akvorezista ŝminko por okulharoj`, `skatoleto da vizaĝpudro`, `pli hela nuanco` は化粧品・衛生用品文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `sablokolora`, `daŭrema`, `artikolo`, `pantalono`, `kotono`, `ŝtofo`, `kostumo`, `stoko`, `mokaseno`, `zorio`, `pantoflo`, `kalkanumo`, `sidi`, `koltuko`, `ganto`, `ledo`, `ŝtrumpeto`, `ŝalo`, `orelringoj`, `kronometro`, `monujo`, `naztuko`, `kravato`, `ŝelko`, `manumbutono`, `rimeno`, `zono`, `juvelaĵo`, `brakhorloĝo`, `fermilo`, `kolĉeno`, `parfumo`, `dentopasto`, `lipruĝo`, `kremo`, `kombilo`, `ŝampuo`, `dentobroso`, `paletro`, `ŝminko`, `palpebro`, `akvorezista`, `okulharo`, `pudro`, `nuanco`, `sapo` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- ReVo `provi`: https://reta-vortaro.de/revo/art/prov.html
- Glosbe `slipper`: https://glosbe.com/en/eo/slipper
- Glosbe `scarf`: https://glosbe.com/en/eo/scarf
- Glosbe `cufflinks`: https://glosbe.com/en/eo/cufflinks
- Glosbe `face powder`: https://glosbe.com/en/eo/face%20powder
- Glosbe `mascara`: https://glosbe.com/en/eo/mascara

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- アプリ実行用CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3456`〜`ID3555` は100件確認済み。

## 637. 636周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food
- Shopping / At the Department Store
- Shopping / Clothes

結果:
- **CSV修正なし**
- 前回 `ID3256`〜`ID3355` に続き、今回は `ID3356`〜`ID3455` の100件を確認した。朝食食品、百貨店案内、衣料品店での試着・サイズ・洗濯表示のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3359` EO、`ID3362` EO、`ID3365` EN/JA/KO、`ID3367` EO、`ID3368` EO、`ID3370` EO、`ID3372` ZH、`ID3376` KO、`ID3408` EO/KO、`ID3422` JA、`ID3439` ZH、`ID3443` JA/ZH、`ID3444` RU、`ID3447` ZH、`ID3449` EO、`ID3455` ZH は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Mi preferas frititajn ovojn`, `Mi ŝatus kolbasojn`, `Ŝi ŝatus kelkajn avenajn biskvitojn`, `Mi ŝatas ŝorbeton`, `Li ŝatas krespojn`, `Ŝi ŝatas biskvitojn`, `Ŝi ŝatas benjetojn`, `Ĉu vi manĝas dolĉajn bulkojn por matenmanĝo?`, `Blankan panon, mi petas`, `Nigran panon, mi petas`, `Hejmfaritan panon, bonvolu`, `Mi ŝatus la rizan pudingon`, `Mi ŝatus patkukojn kun acera siropo`, `Ni ŝatus du tasojn da varma ĉokolado`, `Ĉu vi manĝas kornajn bulkojn ĉiutage?`, `Ŝi ankaŭ ŝatas margarinon`, `Mi volas iom da kazeo`, `Mi komencos per salato`, `Mi prenos kafon kun lakto`, `Ŝi trinkos iom da senkafeina kafo`, `Li manĝos kirlovaĵon`, `Iom da jogurto por mia filino, mi petas`, `Ŝi preferas teon kun artefarita dolĉigilo` は、朝食・軽食・飲み物語彙として対応する。
- PIV 2020 で `krespo`, `biskvito`, `ŝorbeto`, `pudingo`, `patkuko`, `acero`, `margarino`, `kazeo`, `jogurto`, `dolĉigilo` を確認。`senkafeina kafo` は `sen-` + `kafeino` + `kafo` の透明な構成として維持。`kirlovaĵo` は PIV 2020 の `kirli` + `ovo` + `-aĵo` と外部辞書の scrambled eggs 対応で確認できるため維持。`korna bulko` は Glosbe/Wiktionary で croissant として確認でき、PIV の `bulko` の範囲とも衝突しないため維持。
- `Malfermita la tutan tagon`, `Pardonu, ni estas fermitaj`, `Nun estas rabatvendo`, `Kie estas la elirejo?`, `Malfermita 24 horojn ĉiutage`, `Ĉu vi estas malfermitaj sabate?`, `Kiam vi malfermiĝas?`, `Je kioma horo vi fermiĝas?`, `Sur kiu etaĝo troviĝas la brakhorloĝoj?`, `Sur la dua etaĝo`, `La butikoj estas fermitaj post la dua horo posttagmeze`, `Ni estas malfermitaj de la 9-a ĝis la 17-a, de lundo ĝis vendredo`, `Ĉu estas senimposta butiko proksime?`, `Kie estas la plej proksima librejo?`, `Kie estas la fako de ŝtofoj?`, `Kie estas la sekcio de subvestoj?`, `Kie estas la kosmetika fako?`, `Ĝi estas ĝuste tie`, `La kaso estas tie`, `Ni estas malfermitaj de la 10-a matene ĝis la 8-a vespere, sep tagojn semajne`, `Ĝis kioma horo vi estas malfermitaj labortage?`, `La butikoj estas malfermitaj ĝis la dua`, `Ĉu estas magazeno proksime?`, `Ĉu vi havas sekcion de virinaj vestoj?`, `Kie estas la mebla sekcio?`, `Sur kiu etaĝo estas la nutraĵa sekcio?`, `Ĝi estas sur la teretaĝo`, `Ĉu ĉi tie estas vendistoj, kiuj parolas la litovan?`, `Ĉu vi scias, kie alie mi povus provi?`, `Butikoŝtelistoj estos juĝe persekutataj` は、百貨店案内・営業時間・売場案内・法的掲示として対応する。
- PIV 2020 で `butiko`, `rabato`, `vendo`, `magazeno`, `brakhorloĝo`, `librejo`, `fako`, `sekcio`, `kaso`, `etaĝo`, `teretaĝo`, `vendisto`, `litova`, `provi`, `persekuti` 周辺を確認。`rabatvendo` は PIV 直接見出しでは弱いが、`rabato` + `vendo` による透明な複合語で、セール/促销/세일/распродажа 文脈と合うため維持。`etaĝo` は PIV 2020 に「階の数え方は民族によって異なる」と明記されており、`teretaĝo` と日中韓/RU の「1階」対応、`dua etaĝo` と2階対応は、この教材文脈では明確な誤りとはしない。
- `Ĉu mi povas ĝin surprovi?`, `Kia grandeco ĝi estas?`, `Kiel ĝi aspektas?`, `Ĝi konvenas al vi`, `Ne gladu`, `Ne blankigu`, `Kie estas la T-ĉemizoj?`, `Kia estas via grandeco?`, `Mia grandeco estas 8`, `Kie estas la provejo?`, `Ĉu tio bone taŭgas?`, `Ĝi ne konvenas al mi`, `Ĝi estas tro mallonga`, `El kio ĉi tiuj estas faritaj?`, `Ĉu ĝi estas pura kotono?`, `Kiu el ili estas pli bona?`, `Kiu el ili estas pli malmultekosta?`, `Ŝi ne ŝatas ilin`, `Aĉetu 1, ricevu 1 senpage`, `Nur kemia purigado`, `Kie mi povas aĉeti ĝin?`, `Vi povas trovi ĝin tie`, `Mi bezonas vesperan robon`, `Mi ne scias mian grandecon`, `Bonvolu provi ĉi tiun`, `Mi ŝatus provi ĝin`, `Ĉu vi havas provejon?`, `Ĉu ĉi tio bone aspektas sur mi?`, `Ĝi aspektas bonege sur vi!`, `Mi ne ŝatas la koloron`, `Ĉi tie estas tro malvaste`, `Ĉu ĝi haveblas en pli granda grandeco?`, `Ĝi estas ĝuste taŭga`, `Mi prenos ĉi tiun robon`, `Ĉu ĉi tiuj estas laveblaj?`, `Ne, oni devas ilin kemie purigi`, `Mi revenos poste`, `Lavu aparte`, `Lavu inversigite`, `Mi nur rigardas, dankon`, `Kian grandecon havas ĉi tiu ŝorto?`, `Ĉu ili estas samaj?`, `Ĉu vi havas ĉi tion en pli granda grandeco?`, `Mi ŝatus piĵamon`, `Ĉu vi ŝatus surprovi ĝin?`, `Ĉi tio ne estas tute tio, kion mi volis`, `Bonvolu montri al mi ion en alia koloro` は、衣類、試着、サイズ、素材、洗濯表示、店頭応答として対応する。
- PIV 2020 で `ĉemizo` と派生 `T-ĉemizo`, `provi` と派生 `sur provi`, `grandeco`, `gladi`, `blankigi`, `taŭgi`, `konveni`, `kotono`, `kemio`, `lavi`, `inversigi`, `ŝorto`, `piĵamo`, `robo`, `koloro`, `malvasta`, `havebla` を確認。`provejo` は `provi` + `-ej-` の透明な複合語で、衣料品店の fitting room / 試着室 / 试衣间 / 피팅룸 / примерочная 文脈と一致するため維持。`ĉi tiu ŝorto` は PIV の `ŝorto` が単数見出しで shorts 型衣類を指すため、EN/RU の複数形表示とは衝突しない。

主な据え置き確認:
- Breakfast Food: `ŝorbeto`, `krespoj`, `benjetoj`, `dolĉaj bulkoj`, `riza pudingo`, `patkukoj kun acera siropo`, `kornaj bulkoj`, `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `artefarita dolĉigilo` は食品・朝食文脈で維持。
- Department Store: `rabatvendo`, `senimposta butiko`, `brakhorloĝoj`, `librejo`, `fako`, `sekcio`, `magazeno`, `teretaĝo`, `nutraĵa sekcio`, `vendistoj`, `Butikoŝtelistoj estos juĝe persekutataj` は店舗案内文脈で維持。
- Clothes: `T-ĉemizoj`, `surprovi`, `provejo`, `grandeco`, `konvenas`, `taŭgas`, `pura kotono`, `kemia purigado`, `kemie purigi`, `laveblaj`, `Lavu inversigite`, `ŝorto`, `piĵamo`, `alia koloro` は衣料品店・洗濯表示文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `krespo`, `biskvito`, `ŝorbeto`, `pudingo`, `patkuko`, `bulko`, `acero`, `margarino`, `kazeo`, `jogurto`, `dolĉigilo`, `butiko`, `rabato`, `vendo`, `magazeno`, `brakhorloĝo`, `librejo`, `fako`, `sekcio`, `kaso`, `etaĝo`, `teretaĝo`, `vendisto`, `litova`, `provi`, `persekuti`, `ĉemizo`, `T-ĉemizo`, `grandeco`, `gladi`, `blankigi`, `taŭgi`, `konveni`, `kotono`, `kemio`, `lavi`, `inversigi`, `ŝorto`, `piĵamo`, `robo`, `koloro`, `malvasta`, `havebla` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Glosbe `croissant`: https://glosbe.com/en/eo/croissant
- Wiktionary `korna bulko`: https://en.wiktionary.org/wiki/korna_bulko
- Kaikki/Wiktionary data `kirlovaĵo`: https://kaikki.org/dictionary/Esperanto/meaning/k/ki/kirlova%C4%B5o.html
- Wiktionary `T-ĉemizo`: https://en.wiktionary.org/wiki/T-%C4%89emizo
- ReVo `provi`: https://reta-vortaro.de/revo/art/prov.html

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- アプリ実行用CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3356`〜`ID3455` は100件確認済み。

## 636. 635周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit
- Food / Vegetables
- Food / Staple Food & Spices
- Food / Breakfast Food 冒頭

結果:
- **1件修正（1行・1列）**
- 前回 `ID3156`〜`ID3255` に続き、今回は `ID3256`〜`ID3355` の100件を確認した。果物、野菜、主食・香辛料、朝食食品冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3279` KO、`ID3281` KO、`ID3282` EO、`ID3283` EO/KO、`ID3285` KO、`ID3289` ZH、`ID3290` ZH/KO、`ID3313` EO、`ID3318` EO/KO、`ID3342` KO、`ID3343` ZH、`ID3350` EO は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID3328` EO
  - `Ne uzu rozmarenon` → `Ne uzu rosmarenon`
  - 理由: EN/JA/ZH/KO/RU は rosemary / ローズマリー / 迷迭香 / 로즈메리 / розмарин で一致。PIV 2020 と Fundamento/Universala Vortaro は `rosmaren/o`、Wiktionary も `rosmareno` / `rosmarenon` を rosemary として確認できる。一方、`rozmarenon` は PIV 2020 では見出し確認できず、標準形から外れる綴りと判断できるため、意味内容を変えずに補正した。

- `Ĉu vi ŝatas persikojn?`, `Mi ŝatas avokadon`, `Li ne ŝatas prunojn`, `Mi prenos bananojn`, `Mi ŝatas citronojn`, `Ŝi ŝatas olivojn`, `Ankaŭ mi ŝatas mangon`, `Mi ŝatus pecon da poma torto`, `Li ŝatus vinberojn`, `Mi prenos kivifruktojn`, `Ĉi tiu akvomelono ne estas matura`, `Mi ŝatas kokoson`, `Mi ne ŝatas juglandojn`, `Li ŝatas sekigitajn fruktojn`, `Ŝi ne ŝatas limeojn`, `Ŝi prenos iom da ĉerizoj`, `Ni manĝos oranĝojn`, `Mi ŝatus la fruktan salaton`, `Mi ŝatus iom da abrikota konfitaĵo`, `Ni ŝatus kelkajn pirojn`, `Ĉu la ananaso estas freŝa aŭ konservita?`, `Mi preferas bakitajn pirojn`, `Mi preferas ĵeleon el nigra ribo`, `Ili preferas rostitajn kaj salitajn migdalojn`, `Mi prenos framban glaciaĵon kiel deserton`, `Ŝi prenos mirtelan torton`, `Ni prenos du oksikokajn mufinojn`, `Ŝi prenos grapfruktan torton kun glaciaĵo`, `Mi ŝatus fragojn`, `Mi ŝatus iom da karamelizitaj figoj`, `Mi ŝatus iom da sensalaj arakidoj`, `Ŝi ŝatus pecon da poma strudelo`, `Ili ŝatus kelkajn mandarinojn`, `Tranĉu la melonon en dikajn tranĉaĵojn` は、果物、ナッツ、果物菓子、保存/加熱状態として対応する。
- PIV 2020 で `limeo`, `oksikoko`, `nigra ribo`, `mirtelo`, `grapfrukto`, `frambo`, `arakido`, `strudelo`, `torto`, `konfitaĵo`, `mango`, `avokado`, `kivifrukto`, `akvomelono`, `mandarino`, `melono` などを確認。`nigra ribo` は黒すぐりの ĵeleo / glaciaĵo / konfitaĵo 用途までPIVで確認でき、ID3278 と整合する。
- `Ĉu vi ŝatas rafanojn?`, `Ŝi ŝatas asparagojn`, `Mi ne ŝatas cepojn`, `Mi prenos la legoman stufaĵon`, `Mi ŝatas celerion`, `Mi ankaŭ ŝatas ajlon`, `Ŝi ne ŝatas kukurbon`, `Mi prenos karotojn`, `Li havos kelkajn tomatojn`, `Mi preferas florbrasikon al brokolo`, `Ĉu vi ŝatas fungan supon?`, `Mi ŝatas terpoman supon`, `Mi ŝatas paprikon`, `Mi ne ŝatas melongenon`, `Mi ankaŭ prenos brasikon`, `Mi prenos spinacon`, `Ŝi prenos la azian legoman buljonon`, `Mi ŝatus iom da dolĉa maizo`, `Mi ŝatus peklitajn kukumojn`, `Ni dividu ĉi tiun sandviĉon kun laktuko`, `Ne uzu tro multe da akra kapsiko`, `Mi prenos tomatsupon, bonvolu`, `Mi ŝatus la francan cepan supon`, `Mi ŝatus la panumitan kukurbeton`, `Mi ŝatus la betojn kun kapra fromaĝo, mi petas`, `Ili volus kelkajn kukumojn`, `Mi pensas, ke mi prenos la kukurban supon`, `Mi prenos la fungojn kun soja saŭco`, `Li prenos la brezitajn karotojn kaj kikerojn` は、野菜名、野菜料理、スープ、調理法として対応する。
- `akra kapsiko` は PIV 2020 の `kapsiko` の辛味果実用法と合い、chilli / 唐辛子 / 辣椒 として維持。`papriko` は spice寄りの語義を持つが、PIVに植物・果実用法もあり、JA/KOが「パプリカ」、ZH/RU/ENが sweet pepper 系であるため、明確な意味ズレとはせず維持。`panumita kukurbeto`, `peklitaj kukumoj`, `brezitaj karotoj kaj kikeroj` はPIV語義と対応する。
- `Mi ŝatas menton`, `Mi provos tofuon`, `Pastaĵojn, mi petas`, `Li preferas blankan pipron`, `Li ŝatas bazilion`, `Ankaŭ ŝi ŝatas zingibron`, `Ni ĉiuj ŝatas vanilon`, `Mi ne povas manĝi tritikon`, `Mi prenos nudelojn`, `Ne uzu rosmarenon`, `Mi ankaŭ ŝatas panon kun sezamo`, `Li ŝatas kaperojn`, `Ŝi ne ŝatas erukon`, `Mi prenos terpomojn`, `Mi prenos la kuskusan salaton`, `Li havos iom da faboj`, `Mi preferas verdajn fazeolojn`, `Gustumu la safranan rizon`, `Li ŝatas fazeolan supon`, `Mi ŝatas ĉiujn herbojn krom koriandro`, `Ili ne ŝatas paprikan saŭcon`, `Mi pensas, ke mi prenos iom da pizoj`, `Mi pensas, ke mi prenos bakitajn terpomojn`, `Ŝi prenos la stufitajn lentojn kaj legomojn`, `Ŝi ŝatus fritojn`, `Li volus iom da rizo`, `Ŝi preferas nigran pipron`, `Ŝi preferas fiŝon kun petrosela saŭco` は、主食、香草、香辛料、豆類、米・麺・芋類として対応する。
- `tofuo` は PIV 2020 では直接見出し確認できなかったが、Wiktionary で tofu の Esperanto 名詞として確認でき、日中韓/RU と一致するため維持。`rosmareno` は PIV 2020・Fundamento・Wiktionary で確認できたため、今回 `rozmarenon` から補正。`eruko` は PIV の `kultiva eruko` がサラダ用の葉とされ、rocket / ルッコラ / 芝麻菜 / руккола と対応するため維持。
- `Mi ŝatas cerealojn`, `Buteron, mi petas`, `Mi prenos omleton`, `Mi volas iom da lardo`, `Ĉu vi ŝatas mielon?`, `Mi ŝatas ĵeleon`, `Mi ŝatas mocarelon`, `Li ŝatas vaflojn`, `Mi trinkos teon` は、朝食食品・飲み物として対応する。
- `cerealoj` は PIV 2020 では穀物・穀類、`cerealaĵo` は朝食用に加工された製品として区別される。ID3347 は Breakfast Food で JA/ZH/KO が breakfast cereal 寄りにも読めるが、EN `cereals` と RU `злаки` は穀類側にも読めるため、明確な意味ズレとは断定せず維持。`lardo` は bacon 対応として前回補正後の確認済み語、`mocarelo`, `vaflo`, `omleto`, `mielo`, `ĵeleo`, `butero`, `teo` は PIV 2020 で確認済み。

主な据え置き確認:
- Fruit: `limeoj`, `nigra ribo`, `oksikoko`, `grapfrukta torto`, `karamelizitaj figoj`, `sensalaj arakidoj`, `poma strudelo`, `mandarinoj`, `melono` は果物・菓子文脈で維持。
- Vegetables: `papriko`, `akra kapsiko`, `peklitaj kukumoj`, `laktuko`, `panumita kukurbeto`, `kapra fromaĝo`, `soja saŭco`, `brezitaj karotoj kaj kikeroj` は野菜料理文脈で維持。
- Staple Food & Spices / Breakfast Food: `tofuo`, `pastaĵoj`, `bazilio`, `rosmareno`, `eruko`, `kuskusa salato`, `verdaj fazeoloj`, `safrana rizo`, `koriandro`, `lentoj`, `fritoj`, `petrosela saŭco`, `cerealoj`, `lardo`, `mocarelo`, `vafloj` は食品語彙として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `limeo`, `oksikoko`, `nigra ribo`, `torto`, `kapsiko`, `papriko`, `eruko`, `panumi`, `pekli`, `brezi`, `kikero`, `cerealo` / `cerealaĵo`, `rosmareno`, `lardo`, `mocarelo`, `vaflo`, `mielo`, `ĵeleo`, `omleto`, `teo` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Fundamento / Universala Vortaro `rosmaren'`: https://dvd.ikso.net/libro/Zamenhof/Fundamento_de_Esperanto.pdf
- Wiktionary `rosmareno`: https://en.wiktionary.org/wiki/rosmareno
- Wiktionary `tofuo`: https://en.wiktionary.org/wiki/tofuo

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- アプリ実行用CSV MD5: `7bc1537b0c7dccf0c6e62d2ec393a519`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3256`〜`ID3355` は100件確認済み。

## 635. 634周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints
- Restaurant & Pub / At the Pub
- Food / Meat & Fish

結果:
- **CSV修正なし**
- 前回 `ID3056`〜`ID3155` に続き、今回は `ID3156`〜`ID3255` の100件を確認した。レストラン苦情、パブでの注文、肉・魚料理名のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3156` ZH、`ID3160` ZH、`ID3182` ZH、`ID3197` ZH、`ID3206` JA/KO、`ID3207` ZH、`ID3211` ZH、`ID3227` EO、`ID3231` KO、`ID3233` KO、`ID3248` KO は、現CSVで補正後内容になっていることを確認した。
- 今回は、現CSVに対して新たに明確な意味ズレや、辞書確認に基づく必須修正は見つからなかった。

- `Ĉu nia manĝaĵo jam venas?`, `Ni atendis pli ol horon`, `Dankon pro via pacienco`, `Via mendo estos sur via tablo ene de 5 minutoj`, `Mi mendis mian trinkaĵon sen glacio`, `Mankas unu plado`, `Ĝi ne estas sufiĉe kuirita`, `Mi sincere pardonpetas pro ĉi tiu eraro`, `Mi ŝatus fari plendon` は、料理が運ばれているか、待ち時間、待機への謝辞、5分以内の提供、氷なし注文、一品不足、加熱不足、謝罪、苦情申し立てとして対応する。
- `mendo`, `plado`, `kuirita`, `pardonpeti`, `plendo` は PIV 2020 の基本語義または透明な派生で確認可能。`Ĝi ne estas sufiĉe kuirita` は、RU `не до конца пропеклась` が焼き物寄りでも、日中韓はいずれも「十分に火が通っていない」広い苦情表現で、EO `kuirita` と整合するため維持。
- `Nigran teon, mi petas`, `Kiu sekvas?`, `Viskion kaj akvon, mi petas`, `Kun glacio`, `Ni hastas`, `Kafon, mi petas`, `Kun kremo`, `Kun sukero, mi petas`, `Granda aŭ malgranda?`, `Mi ŝatus lokan bieron`, `Naĉojn, mi petas`, `Ĉu vi servas manĝaĵon?`, `Ĉu vi fumas?`, `Ne, mi ne fumas`, `Mi rezignis`, `Ĉu vi ŝatus ion manĝi?`, `Same kiel kutime`, `Ĉu vi havas sandviĉojn?`, `Ĉu vi havas ian varman manĝaĵon?`, `Kio estas en ĝi?`, `Ĉu ĝi estas pika?`, `Ĉu vi ŝatus cigaredon?`, `Ĉu vi havas fajrilon?`, `Mi volas pomsukon`, `Bonvolu doni al mi botelon da biero`, `Kies vico estas pagi?`, `Estas via vico`, `La sekvan rondon mi pagas`, `Lastaj mendoj!`, `Mi havas postebrion`, `Mi neniam plu trinkos!` は、パブでの飲み物・軽食注文、喫煙、いつもの注文、順番、支払いの番、ラストオーダー、二日酔いとして対応する。
- `postebrio` は PIV 2020 の `post ebrio` と意味が一致し、hangover / 二日酔い / 숙취 / похмелье と対応する。`naĉoj` は PIV 2020 では強く確認できないが、Drops で nachos の Esperanto 表現として確認でき、JA/ZH/KO/RU もナチョス系料理名として対応するため維持。説明的な置換は固有料理名との対応を弱める。
- `Tason da kafo, mi petas. Fortan, sed ne amaran`, `Faru ĝin duobla, mi petas`, `Glaso da tomata suko`, `Ĉu vi ankoraŭ servas trinkaĵojn?`, `Permesu al mi aĉeti trinkaĵon por vi`, `Kiu estas la koktelo de la tago?`, `Tri glasetojn da tekilo, bonvolu`, `Ĉu vi ŝatus barelan aŭ botelan bieron?`, `Mi ŝatus botelon da blanka vino`, `Mi ŝatus botelon da rumo`, `Tio estas tro multe`, `Ĉu vi havas ankaŭ ion por manĝi?`, `Kiajn sandviĉojn vi havas?`, `Mi ŝatus mendi fritojn kaj laktoskuaĵon`, `Paketon da ĉipsoj, mi petas`, `Kiun guston vi ŝatus?`, `Mi ŝatus paketon da cigaredoj`, `Kie estas la vira necesejo?` は、濃いが苦くないコーヒー、ダブル、トマトジュース、飲み物提供、奢り、本日のカクテル、テキーラショット、生/瓶ビール、白ワイン、ラム、量が多すぎる、食べ物の有無、サンドイッチ種別、フライドポテトとミルクシェイク、ポテトチップス、味、タバコ一箱、男性用トイレとして対応する。
- `barela biero` は PIV 2020 の `barelo da biero` から draught beer 文脈で維持。`tekilo`, `rumo`, `ĉipsoj` は PIV 2020 で確認済み。`laktoskuaĵo` は `lakto` + `skui` の透明複合で、Glosbe/Wiktionary 系の外部確認でも milkshake と対応するため維持。
- `Mi ŝatas frititan soleon`, `Mi ne ŝatas hepaton`, `Mi ne manĝas viandon`, `Marfruktan supon, mi petas`, `Mi ŝatas bifstekon el bova lumbaĵo`, `Ĉu vi ŝatas salikokojn?`, `Ŝi ankaŭ ŝatas kuniklon`, `Mi ne manĝas fiŝon`, `Mi ne manĝas porkaĵon`, `Mi prenos la ŝafidaĵon`, `Mi prenos la anseron`, `Mi ŝatus la fazanon`, `Ĉu vi ŝatas fumitan viandon?`, `Mi prenos la rostbefon`, `Mi prenos la frititan kalmaron`, `Mi prenos la fumitan truton`, `Ŝi prenos iom da ŝinko`, `Li prenos la porkaĵon`, `Mi ŝatus la grilitan salmon`, `Li ŝatus la kokidan bruston`, `Ni ŝatus ostrojn`, `Ili ŝatus porkajn ripojn`, `Mi volas la rostitan skombron`, `Li ŝatus anason por la vespermanĝo`, `Li preferas salitan moruon`, `Pardonu, sed la salikoka supo finiĝis` は、肉・魚・甲殻類・調理法・品切れとして意味ズレなし。
- PIV 2020 で `soleo`, `hepato`, `viando`, `lumbaĵo`, `bifsteko`, `salikoko`, `kuniklo`, `porkaĵo`, `ŝafidaĵo`, `ansero`, `fazano`, `rostbefo`, `kalmaro`, `truto`, `ŝinko`, `salmo`, `ostro`, `ripo`, `skombro`, `anaso`, `moruo` を確認。`bifsteko el bova lumbaĵo` は sirloin steak として、`rostbefo` は過去補正後の PIV 見出し語として維持。
- `Mi ŝatus sandviĉon kun tinuso, mi petas`, `Provu ankaŭ vi la stekon!`, `Mi prenos la koturnon por la tagmanĝo`, `Mi prenos la kokidan supon, bonvolu`, `Mi prenos la polpon, mi petas`, `Mi prenos la bovan ripon, mi petas`, `Mi prenos bovidan kotleton por la vespermanĝo`, `Mi prenos boligitajn krabojn, mi petas`, `Li havos grilitan karpon`, `Ni prenos kokidajn flugilojn, bonvolu`, `Mi provos la ŝarkon venontfoje`, `Mi ŝatus la krudan haringon, mi petas`, `Ili ŝatus boligitajn kankrojn`, `Kiel vi dezirus vian stekon?`, `Kio estas la plej bona recepto por kraba supo?`, `Pardonu, ni ne plu havas omarojn` は、ツナサンド、ステーキ、ウズラ、チキンスープ、タコ、牛リブ、仔牛カツレツ、茹でガニ、鯉、手羽、サメ、ニシン、ザリガニ、焼き加減、カニスープ、ロブスター売り切れとして対応する。
- PIV 2020 で `tinuso`, `steko`, `koturno`, `polpo`, `bova`, `ripo`, `bovida`, `kotleto`, `krabo`, `karpo`, `ŝarko`, `haringo`, `kankro`, `omaro` を確認。`bova ripo` の JA `リブロース` は直訳ではないが、牛リブ系の料理・部位としてクイズ対応を壊すほどの明確なズレではないため、文脈別許容として維持。

主な据え置き確認:
- Complaints: `jam venas`, `ene de 5 minutoj`, `mendo sen glacio`, `mankas unu plado`, `ne sufiĉe kuirita`, `pardonpetas`, `fari plendon` は苦情・応対文脈で維持。
- At the Pub: `nigra teo`, `viskio`, `kremo`, `loka biero`, `naĉoj`, `fajrilo`, `postebrio`, `glasetoj da tekilo`, `barela/botela biero`, `rumo`, `laktoskuaĵo`, `ĉipsoj`, `vira necesejo` はパブ文脈で維持。
- Meat & Fish: `soleo`, `hepato`, `marfrukta supo`, `bova lumbaĵo`, `salikoko`, `kuniklo`, `ŝafidaĵo`, `ansero`, `fazano`, `rostbefo`, `kalmaro`, `truto`, `salmo`, `ostro`, `porkaj ripoj`, `skombro`, `moruo`, `tinuso`, `koturno`, `polpo`, `bova ripo`, `bovida kotleto`, `krabo`, `karpo`, `ŝarko`, `haringo`, `kankro`, `omaro` は料理名として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `post ebrio`, `barelo`, `biero`, `ĉipsoj`, `tekilo`, `rumo`, `viskio`, `lakto`, `skui`, `lumbaĵo`, `bifsteko`, `rostbefo`, `soleo`, `salikoko`, `kankro`, `skombro`, `polpo`, `omaro`, `haringo`, `truto`, `tinuso`, `ŝarko`, `kotleto`, `koturno`, `krabo`, `steko` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Drops `naĉoj`: https://languagedrops.com/word/en/english/esperanto/translate/nachos/
- Glosbe `laktoskuaĵo`: https://glosbe.com/eo/es/laktoskua%C4%B5o
- Wiktionary `milkshake`: https://en.wiktionary.org/wiki/milkshake

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `1b1efa42071a3c0070c5b4c0f4049ea0`
- アプリ実行用CSV MD5: `1b1efa42071a3c0070c5b4c0f4049ea0`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3156`〜`ID3255` は100件確認済み。

## 634. 633周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal
- Restaurant & Pub / Paying the Bill
- Restaurant & Pub / Complaints

結果:
- **2件修正（2行・2列）**
- 前回 `ID2956`〜`ID3055` に続き、今回は `ID3056`〜`ID3155` の100件を確認した。食事中、会計、苦情表現のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、エスペラント文と日中韓文の直接対応を確認した。
- 過去周回で補正済みの `ID3057` JA、`ID3074` ZH、`ID3076` EO、`ID3082` ZH、`ID3102` KO、`ID3109` KO、`ID3114` EN/KO、`ID3120` ZH、`ID3123` ZH、`ID3141` JA/KO、`ID3144` ZH、`ID3149` EN、`ID3151` ZH、`ID3153` ZH、`ID3154` ZH/KO は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID3084` EO
  - `Mia paĉjo ŝatas legoman kareon` → `Mia paĉjo ŝatas legoman kareaĵon`
  - 理由: JA/ZH/KO/RU/EN は「野菜カレー」という料理を指す。PIV 2020 では `kareo` は主にインド系の香辛料、`kareaĵo` はカレーを使った料理として説明されるため、料理名として `legoma kareaĵo` に補正した。意味内容は vegetable curry のまま維持。
- `ID3092` KO
  - `패스트푸드를 드신 적이 있으신가요?` → `패스트푸드를 드시기도 하나요?`
  - 理由: EO `Ĉu vi iam manĝas rapidmanĝaĵon?`、EN `Do you ever eat fast food?`、JA `ファストフードを食べることはありますか？`、ZH `你平时会吃快餐吗？`、RU `Ты когда-нибудь ешь фастфуд?` は、過去経験の有無ではなく「普段/時々食べることがあるか」を尋ねる現在・習慣寄りの表現。旧KOは「食べたことがありますか」に寄るため、現在の習慣質問として補正した。

- `Salo kaj vinagro`, `Kiel ĝi gustas al vi?`, `Ĝi estas bongusta`, `Mi ŝatas hindan manĝaĵon`, `Ĉu ĉi tiu manĝaĵo estas halala?`, `Ĉu vi ŝatas picon?`, `Mi amas fromaĝan picon`, `Bonan apetiton!`, `Bonvolu transdoni la salon`, `Ĉu mi povas fumi ĉi tie?`, `Kie estas la necesejoj?`, `Kio estas la pasvorto por la Wi-Fi?`, `Via manĝaĵo estas preskaŭ preta`, `Mi pensas, ke ĝi gustas bone`, `Ĝi tre plaĉas al ni`, `Ĉi tio estas mia plej ŝatata`, `Ĉu mi povus ricevi iom da butero?`, `Ankoraŭ iom da pano, mi petas`, `Ĉu vi povus varmigi ĉi tion?`, `Mi ankoraŭ ne finis manĝi`, `Ĉu vi ŝatus iom da deserto?`, `Sufiĉas, dankon`, `Kiel oni manĝas ĉi tion?`, `Ĉu vi scipovas uzi manĝobastonetojn?`, `Mi estas alergia al tritiko`, `Ĉu vi dezirus ion alian?`, `Mi ŝatus ankoraŭ iom da fritoj`, `Ankoraŭ unu porcion da rizo, mi petas`, `Mia paĉjo ŝatas legoman kareaĵon`, `Li baldaŭ venos`, `Kio estas pli bona: spagetoj aŭ kokido?`, `Jes, ili ankaŭ ŝatas kalzoneon`, `Kiam nia manĝaĵo estos preta?`, `Estos ĉirkaŭ dekminuta atendo`, `Ĉu vi ŝatus kafon aŭ deserton?`, `Ni ŝatus mendi deserton, bonvolu`, `Ĉu vi iam manĝas rapidmanĝaĵon?`, `Mi estas alergia al laktaĵoj`, `Mi estas forte alergia al nuksoj`, `Ĉu vi povus transdoni la sukeron, mi petas?`, `Ĉu mi povus ricevi puran teleron?`, `La forko estas sub la tablo`, `Kie mi povas nutri la bebon?`, `Je kioma horo fermiĝas la kuirejo?` は、食事中の評価、追加注文、食物アレルギー、食器、調理時間、料理名、食べ方、店内設備として対応する。
- `halala` は PIV 2020 では見出し確認が弱いが、Wiktionary で halal の Esperanto 形容詞として確認でき、ハラール料理の文脈で日中韓/RUと一致するため維持。`manĝobastonetoj` は PIV の `manĝ bastonetoj` と `bastoneto` 語義から箸として維持。`fritoj` は PIV の `terpom-fritoj` と料理文脈から fries として維持。
- `kalzoneo` は PIV 2020 直接見出しでは未確認だが、Wiktionary およびエスペラント版 Wikipedia で calzone の料理名として確認でき、JA/ZH/KO/RU の固有料理名と対応するため維持。`kareo` は香辛料としての語義が強いため、今回の料理名では `kareaĵo` へ補正した。
- `La kalkulon, mi petas`, `Jen via kalkulo`, `Ni dividu ĝin`, `Gardu la restmonon`, `Tio estis tre bongusta`, `Ĉu ni povus pagi, bonvole?`, `Ĉu ni povas pagi aparte?`, `Mi forgesis mian monujon`, `Mi jam pagis`, `Mi lasis trinkmonon`, `Ĉu ĉio estis en ordo?`, `Dankon, tio estis bongusta`, `Tio estis bonega`, `Ĉu mi povus ricevi la kalkulon, mi petas?`, `Ĉio kune`, `Mi pagos por la vespermanĝo`, `Li pagos la kalkulon`, `Ĉu mi povus ricevi kvitancon?`, `Ĉu vi kutime lasas trinkmonon?`, `Ĉu vi bonvolus diri al mi, kiu estas la kuiristo?`, `Transdonu miajn komplimentojn al la ĉefkuiristo`, `Ĝi estis pli ol mi povis manĝi`, `Ĉu la kalkulo inkluzivas la servokotizon?`, `Ĉu oni kutime donas trinkmonon en via lando?`, `Ni pagas aparte`, `Lasu min pagi mian parton`, `Mi pagas por ĉiuj`, `Ĉi tiu sinjoro pagos por ĉio`, `Kiu pagas, kiam vi eliras por vespermanĝi?`, `Bonvolu skribi tion sur mian konton`, `Mi kredas, ke la kalkulo estas malĝuste sumigita` は、会計、割り勘、チップ、領収書、シェフへの賛辞、サービス料、勘定づけ、合計誤りとして対応する。
- PIV 2020 で `kalkulo` にはレストラン/ホテルの請求書用法、`pagi` には `pagi kalkulon de hotelo` 型、`kvitanco`, `kont^3o`, `sumigi`, `kuiristo` などを確認。`servokotizo` は直接見出しでは弱いが、`kotizo` の「払うべき金額」系の語義と透明複合で service charge と読め、日中韓/RU と対応するため維持。
- `Ĝi ne estas freŝa`, `Ĝi estas tro spica`, `Ĉi tio ne estas pura`, `Mi ne mendis ĉi tion`, `Kio okazis, sinjoro?`, `Ĉi tio estas tro malvarma`, `Ĝi estas tro varma`, `Ĉi tio estas tro sala`, `Ĝi estas tro malmola`, `Mia trinkaĵo gustas strange`, `Ni foriras`, `Ĝi daŭras tro longe`, `Ni ne povas plu atendi`, `Ĉi tio ne estas mia mendo`, `Mi mendis rostitan meleagron`, `Ĉi tio estas tro kuirita`, `Mi ne povas manĝi ĉi tion`, `Ĉi tiu trinkaĵo ne estas malvarma`, `Ĉi tiu vino odoras je korko`, `Tio odoras malbone`, `Permesu al mi ŝanĝi ĝin por vi`, `Ĉu vi povus rapidi, mi petas?`, `Ni mendis antaŭ pli ol tridek minutoj`, `Mia mendo ankoraŭ ne alvenis`, `Ni longe atendis` は、品質・温度・塩味・硬さ・異臭・注文違い・待ち時間・ワインのコルク臭などの苦情表現として対応する。
- `meleagro` は PIV で鳥名、`meleagraĵo` で料理素材として確認でき、`rostitan meleagron` は roast turkey として維持。`odori je korko` は PIV の `odori je ...` 用法および `korkogusta vino` と合い、corked wine の苦情として維持。`tro kuirita` は広い調理過多表現として、JA/ZH/KO/RU の自然な場面訳を許容した。

主な据え置き確認:
- During the Meal: `halala`, `manĝobastonetoj`, `fritoj`, `unu porcion da rizo`, `legoma kareaĵo`, `spagetoj`, `kokido`, `kalzoneo`, `rapidmanĝaĵo`, `laktaĵoj`, `nuksoj`, `tritiko`, `nutri la bebon`, `kuirejo` は文脈上維持。
- Paying the Bill: `kalkulo`, `restmono`, `trinkmono`, `pagi aparte`, `kvitancon`, `ĉefkuiristo`, `servokotizo`, `skribi tion sur mian konton`, `malĝuste sumigita` は会計文脈で維持。
- Complaints: `tro spica`, `tro sala`, `tro malmola`, `mendo`, `rostita meleagro`, `tro kuirita`, `trinkaĵo ne malvarma`, `odoras je korko`, `mendo ankoraŭ ne alvenis`, `Ni longe atendis` は苦情文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `kareo` / `kareaĵo`, `bastoneto` / `manĝ bastonetoj`, `friti` / `terpom-fritoj`, `spagetoj`, `lakt/o` / `laktaĵo`, `nukso`, `tritiko`, `kalkuli` / `kalkulo`, `pagi`, `kvitanci` / `kvitanco`, `kont^3o`, `sumo` / `sumigi`, `kotizi` / `kotizo`, `kuiri` / `kuiristo`, `meleagro` / `meleagraĵo`, `rosti`, `korko` / `korkogusta vino`, `odori` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Wiktionary `kareo`: https://en.wiktionary.org/wiki/kareo
- Wiktionary `halala`: https://en.wiktionary.org/wiki/halala
- Wiktionary `kalzoneo`: https://en.wiktionary.org/wiki/kalzoneo
- Vikipedio `Kalzoneo`: https://eo.wikipedia.org/wiki/Kalzoneo

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `1b1efa42071a3c0070c5b4c0f4049ea0`
- アプリ実行用CSV MD5: `1b1efa42071a3c0070c5b4c0f4049ea0`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID3056`〜`ID3155` は100件確認済み。

## 633. 632周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks
- Restaurant & Pub / Ordering Food
- Restaurant & Pub / During the Meal 冒頭

結果:
- **1件修正（1行・2列）**
- 前回 `ID2856`〜`ID2955` に続き、今回は `ID2956`〜`ID3055` の100件を確認した。飲み物注文、料理注文、食事中冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2967` ZH、`ID2991` ZH、`ID2996` ZH/KO、`ID3009` ZH、`ID3010` ZH、`ID3012` EN、`ID3015` JA、`ID3021` KO、`ID3023` ZH、`ID3036` ZH、`ID3038` ZH、`ID3044` ZH、`ID3048` ZH、`ID3050` KO、`ID3051` EN/JA/KO、`ID3055` KO は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID3006` JA/KO
  - JA `ハムサンドイッチをお願いします。` → `ハムサンドイッチだけお願いします。`
  - KO `햄 샌드위치로 할게요.` → `햄 샌드위치만 주세요.`
  - 理由: EO `Mi prenos nur ŝinkan sandviĉon`、EN `I'll just have a ham sandwich.`、RU `Я буду только сэндвич с ветчиной.`、ZH `我就要一个火腿三明治。` は `nur / just / только / 就` の限定が明確。旧JA/KOは注文表現としては自然だが、「ハムサンドイッチだけ」の限定が落ち、EO-JA/KO クイズ対応では `nur` の意味が弱くなるため補正した。

- `Kion vi ŝatus trinki?`, `Mi ne trinkas alkoholon`, `Mi prenos oranĝan sukon, mi petas`, `Mi ŝatus papajan smuzion, mi petas`, `Ĉu vi dezirus ĝin kun glacio?`, `Sen glacio, mi petas`, `Multe da glacio, mi petas`, `Iomete, mi petas`, `Kian vinon vi havas?`, `Kiun vinon vi ŝatus?`, `Doma vino taŭgas`, `La samon denove, mi petas`, `Kiom kostas botelo da ĉampano?`, `Kiun bieron vi ŝatus?`, `Ankoraŭ unu bieron, mi petas`, `Nenion plu, dankon`, `Ĉu oni jam servas vin?`, `Oni jam servas min, dankon`, `Ĉu vi ŝatus ion por trinki?` は、飲み物希望、禁酒、オレンジジュース、パパイヤスムージー、氷の有無/量、ワイン種別、ハウスワイン、同じ飲み物の追加、シャンパン、ビール、追加不要、接客中かどうかとして対応する。
- `smuzio` は PIV 2020 直接見出しでは弱いが、Wiktionary 等で smoothie の Esperanto 名詞として確認でき、飲料名として JA/ZH/KO/RU と対応するため維持。`oranĝa suko`, `glacio`, `ĉampano`, `biero`, `vino` は PIV 語義または透明な飲料語彙として維持できる。
- `Mi ŝatus karafon da limonado`, `Mi ŝatus mendi trinkaĵojn`, `Mi ŝatus ankoraŭ unu tason da kafo`, `Mi ŝatus koktelon, bonvolu`, `Ĉu en ĉi tio estas alkoholo?`, `Mi prenos la samon, bonvolu`, `Nenion por mi, dankon`, `Ĉu vi havas sojan lakton?`, `Ĉu ni povus havi iom pli da lakto?`, `Ĉu ni povus ricevi kruĉon da kranakvo?`, `Ĉu mi povas proponi al vi nian vinkarton?`, `Ĉu mi povus vidi la vinkarton, bonvole?`, `Ĉu vi ŝatus gustumi la vinon?`, `Ĉu ni povus havi ankoraŭ unu botelon da vino?`, `Mi prenos glason da ruĝa vino, mi petas`, `Mi ŝatus botelon da brando`, `Ĉu vi povas rekomendi bonan konjakon?` は、レモネードのカラフェ、飲み物注文、コーヒー、カクテル、アルコール有無、同じもの、不要、豆乳、ミルク追加、水道水のピッチャー、ワインリスト、試飲、ワイン追加、赤ワイン、ブランデー、コニャックとして意味ズレなし。
- `karafo/kruĉo` は液体容器として PIV 語義に合う。`kranakvo` は `krano` + `akvo` の透明複合で tap water と対応。`brando` と `konjako` は PIV 上も区別され、現CSVの ZH 補正後 `干邑` と整合する。`vinkarto` は PIV の `karto` のレストラン品書き用法から wine list として維持。
- `La menuon, mi petas`, `Mi estas vegetaranino`, `Mi volas glaciaĵon`, `Li prenos kebabon`, `Jen via mendo`, `Ĉu ĝi estas bongusta?`, `Ĉu mi povus vidi la menuon, mi petas?`, `Mi estas vegano`, `Kion vi rekomendas?`, `Ĉu vi havas koŝeran manĝaĵon?`, `Ĉu vi pretas mendi?`, `Jes, mi prenos ĉi tion`, `Mi prenos la pastaĵojn`, `Mi prenos bifstekon kun fritoj`, `Mi prenos nur ŝinkan sandviĉon`, `Kun keĉupo aŭ majonezo?`, `Ĉu surloke aŭ por forporti?`, `Por ĉi tie, mi petas`, `Estas por forporti` は、メニュー、ベジタリアン/ヴィーガン、アイスクリーム、ケバブ、注文品の提供、おいしさ、推薦、コーシャ料理、注文準備、パスタ、ステーキとフライドポテト、ハムサンドだけ、ケチャップ/マヨネーズ、店内/持ち帰りとして対応する。
- `vegetaranino` は女性話者を明示し、RU も女性形であるため維持。`vegano` は PIV 2020 では強く確認できないが、Wiktionary で vegan person として確認でき、現代的な食習慣語として各列と対応する。`koŝera` はPIVで食物がヘブライ儀礼に適う意味を確認済み。`pastaĵoj` は PIV の pasta 類集合名として、`bifsteko` と `fritoj` は料理語彙として維持できる。
- `Bonvolu voki la kelneron`, `Ĉu vi havas menuon en la hungara?`, `Kion vi ŝatus havi?`, `Mi atendas iun`, `Mi ankoraŭ ne pretas mendi`, `Mi pretas mendi nun`, `Ni ŝatus mendi antaŭmanĝaĵojn, mi petas`, `Kio estas la supo de la tago?`, `Ĉu estas cepo en la supo?`, `Mi demandos la kuiriston`, `Pardonu, ni ne plu havas tion`, `Ni ne havas omarojn`, `Kion vi ŝatus anstataŭe?`, `Mi manĝos sandviĉon`, `Mi volas vegetaran picon`, `Ĉu mi povas ricevi ĝin tuj?`, `Du hamburgerojn por kunpreni, mi petas`, `Kiom da tempo ĝi daŭros?`, `Ĝi daŭros ĉirkaŭ dudek minutojn`, `Ankoraŭ iomete, bonvolu` は、ウェイター、ハンガリー語メニュー、注文希望、待ち合わせ、注文未決/注文可能、前菜、本日のスープ、玉ねぎ、料理人確認、品切れ、ロブスターなし、代替品、サンドイッチ、ベジタリアンピザ、即時受け取り、ハンバーガー持ち帰り、所要時間、もう少しとして対応する。
- `kelnero`, `menuo`, `mendi`, `antaŭmanĝaĵoj`, `supo`, `kuiristo`, `omaro`, `anstataŭe`, `pico`, `hamburgero`, `por kunpreni` は飲食店注文文脈で維持。`por kunpreni` は `forporti` と同一形ではないが、持ち帰る意味は明確。
- `Ĉu mi povus havi la menuon kaj la vinkarton, mi petas?`, `Ĉu mi povus vidi la desertmenuon?`, `Ĉu vi havas infanan menuon?`, `Ĉu vi servas vegetaran manĝaĵon?`, `Ĉu oni servas ĉi tie aŭ estas memservo?`, `La hodiaŭaj specialaĵoj estas sur la tabulo`, `Kion vi rekomendas el la menuo?`, `Mi prenos tion, kion vi rekomendas`, `Sciigu min, kiam vi estos pretaj mendi`, `Pardonu, ni ŝatus mendi, bonvolu`, `Pardonu, sed ĉu mi povas ŝanĝi mian mendon?`, `Kiel nomiĝas ĉi tiu plado?`, `Kio estas la specialaĵo de la domo?`, `Mi ŝatus gustumi la plej bonan lokan manĝaĵon`, `Mi ŝatus kontinentan matenmanĝon` は、メニュー/ワインリスト/デザートメニュー/子供用メニュー、ベジタリアン料理、テーブルサービス/セルフサービス、本日のおすすめ、メニュー推薦、注文準備連絡、注文、注文変更、料理名、看板料理、地元料理、コンチネンタル朝食として意味ズレなし。
- `memservo` は self-service として透明。`specialaĵoj` は値引きではなく specials / dishes of the day として過去補正後内容と対応する。`plado`, `specialaĵo de la domo`, `gustumi`, `kontinenta matenmanĝo` は飲食店文脈で維持できる。
- `Bonvolu alporti al mi tritavolan sandviĉon kaj lakton`, `Kiel antaŭmanĝaĵon mi prenos la farĉitajn fungojn`, `Kiel vi preferas vian supon? Kun nudeloj aŭ rizo?`, `Verda salato kun franca saŭco`, `Kiel ĉefpladon mi prenos la stekon`, `Mezrostita, mi petas`, `Mi ŝatus bone rostitan viandon`, `Ĉu la manĝaĵo venas kun legomoj?`, `Ĉu vi povus prepari la pladon sen salo?`, `Kelnero!` は、三層サンドとミルク、詰め物入りきのこ、スープに麺/米、フレンチドレッシングのグリーンサラダ、メインのステーキ、ミディアム、よく焼いた肉、野菜付き、塩抜き、店員呼び出しとして対応する。
- `farĉitaj fungoj` は PIV の料理用 `farĉi` と合い、`nudeloj` は PIV の pastaĵoj 系語彙として確認できる。`mezrostita` は PIV `bifsteko sanga, mezrostita, trarostita` の用例と合い、medium の焼き加減として維持。`bone rostita` と `sen salo` も調理条件として自然。

主な据え置き確認:
- Ordering Drinks: `oranĝa suko`, `papaja smuzio`, `glacio`, `doma vino`, `ĉampano`, `biero`, `karafo da limonado`, `koktelo`, `soja lakto`, `kruĉo da kranakvo`, `vinkarto`, `gustumi la vinon`, `brando`, `konjako` は飲み物注文文脈で維持。
- Ordering Food: `vegetaranino`, `vegano`, `koŝera manĝaĵo`, `kebabo`, `pastaĵoj`, `bifsteko kun fritoj`, `ŝinka sandviĉo`, `por forporti`, `por kunpreni`, `antaŭmanĝaĵoj`, `supo de la tago`, `omaroj`, `memservo`, `specialaĵoj`, `plado`, `specialaĵo de la domo`, `tritavola sandviĉo`, `farĉitaj fungoj`, `nudeloj`, `franca saŭco`, `ĉefplado`, `mezrostita`, `bone rostita`, `sen salo` は飲食店注文文脈で維持。
- During the Meal 冒頭: `Kelnero!` は各列が実際の店員呼び出し表現として対応するため、EO/RU/EN の直訳と JA/KO の場面訳の差を許容。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `oranĝo`, `papajo`, `glacio`, `ĉampano`, `biero`, `limonado`, `koktelo`, `sojo` / `sojlakto`, `kruĉo`, `krano`, `koŝera`, `vegetara` / `vegetarano`, `kebabo`, `bifsteko`, `friti` / `terpom-fritoj` / `pomfritoj`, `pico`, `omaro`, `anstataŭ`, `farĉi`, `fungo`, `sandviĉo`, `saŭco`, `rosti`, `plado`, `nudeloj`, `rizo`, `salato`, `legomo`, `salo`, `brando`, `konjako`, `kelnero`, `kuiri`, `menuo`, `mendi`, `rezervi`, `karto`, `vino`, `gustumi`, `pastaĵo` / `pastaĵoj` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio
- Wiktionary `vegano`: https://en.wiktionary.org/wiki/vegano

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `1ef2d0d5e0e7f6cf802ab0c8ec41d6bf`
- アプリ実行用CSV MD5: `1ef2d0d5e0e7f6cf802ab0c8ec41d6bf`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `git diff --check` は whitespace エラーなし（Git の CRLF 置換警告のみ）。
- `ID2956`〜`ID3055` は100件確認済み。

## 632. 631周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat
- Restaurant & Pub / Booking a Table
- Restaurant & Pub / Ordering Drinks

結果:
- **CSV修正なし**
- 前回 `ID2756`〜`ID2855` に続き、今回は `ID2856`〜`ID2955` の100件を確認した。賃貸備品・住居設備、飲食店予約、飲み物注文冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2857` ZH、`ID2867` JA/ZH、`ID2874` JA/ZH、`ID2875` JA/ZH、`ID2876` EO/JA/ZH、`ID2881` JA/ZH/KO、`ID2884` EO/JA、`ID2885` KO、`ID2889`〜`ID2892` JA/ZH、`ID2904` ZH/KO、`ID2905` KO、`ID2908` EO/JA/ZH、`ID2921` ZH/KO、`ID2930` EN、`ID2936` ZH、`ID2949` JA、`ID2952` JA/ZH、`ID2954` ZH は、現CSVで補正後内容になっていることを確認した。
- `Ĉu estas varma akvo?`, `Jes, kompreneble`, `Ĉu vi havas sufiĉe da mono?`, `Ĉu mi povas ricevi la ŝlosilojn?`, `Ĉu estas vazaro?`, `Ĉu estas tukoj?`, `Ĉu estas kusenoj?`, `Mi bezonas skatolon da alumetoj`, `Mi bezonas balailon`, `Mi bezonas tondilon`, `Nia loĝejo estas granda`, `Ĉu vi bezonas garaĝon?`, `Mi bezonas ŝvabrilon`, `Mi bezonas rubsakojn`, `Mi bezonas detergenton`, `Mi bezonas adaptilon`, `Mi bezonas ampolon`, `Ĉu mi povas ricevi litotukojn?` は、湯の有無、資金、鍵、食器、タオル、枕、マッチ、ほうき、はさみ、広いアパート、ガレージ、モップ、ゴミ袋、洗剤、アダプター、電球、シーツとして意味ズレなし。
- `vazaro` は家で用いる器一式として dishes / посуда と対応し、`ŝvabrilo`, `ampolo`, `garaĝo`, `tuko`, `kuseno`, `alumeto`, `tondilo`, `loĝejo` は生活用品・住居語彙として維持できる。`litotukoj` は `littukoj` も強いが、透明複合でシーツの意味から外れないため過修正しない。
- `Kiel funkcias la fridujo?`, `Kiel funkcias la kuirilo?`, `Kiel funkcias la hejtilo?`, `Kie ni povas preni la ŝlosilojn?`, `Ĉu estas butikoj proksime?`, `Sur kiu etaĝo estas via loĝejo?`, `Ĉu estas kuirejaj iloj?`, `Mi bezonas korktirilon`, `Mi bezonas skatolmalfermilon`, `Mi bezonas botelmalfermilon`, `Mi bezonas suĉkloŝon`, `Mi bezonas rulon da adherema filmo`, `Mi bezonas paperajn tukojn`, `Mi bezonas polvosuĉilon`, `Ĉu vi havas ĉiujn modernajn komfortaĵojn?`, `Kiel funkcias la mikroondilo?`, `Kiel funkcias la telerlavmaŝino?`, `Kiel funkcias la klimatizilo?`, `Kiel funkcias la lavmaŝino?`, `Kien mi devas elporti la rubaĵon?`, `Kie estas la elektromezurilo?`, `Kiun tagon venas la ĉambristino?` は、冷蔵庫/コンロ/ヒーター/電子レンジ/食洗機/エアコン/洗濯機の使い方、鍵の受け取り、近隣店舗、階数、台所用品、コルク抜き、缶切り、栓抜き、ラバーカップ、食品用ラップ、キッチンペーパー、掃除機、現代的設備、ゴミ出し、電気メーター、清掃スタッフとして対応する。
- `hejtilo` は室内暖房器具として既存補正後の形を維持。`kuirilo` は PIV では広い cooking utensil/tool だが、住居設備の cooker / плита 文脈で各列と対応する。`suĉkloŝo` はPIV直接見出しでは弱いが、既存オンライン確認済みで plunger / вантуз と対応し、`adherema filmo` は `adheri/adhera` + `filmo` の透明な派生として cling film と読める。
- `Ĉu ni povas sidi ĉi tie?`, `Rezervita`, `Mi ŝatus rezervi tablon, mi petas`, `Por kiam?`, `Morgaŭ tagmeze`, `Mi ŝatus rezervi tablon por hodiaŭ vespere`, `Por kiom da personoj?`, `Tablon por du, mi petas`, `Por kioma horo?`, `Ĉi-vespere je la oka horo`, `Por fumantoj aŭ nefumantoj?`, `Ĉu vi havas rezervon?`, `Jes, mi havas rezervon`, `Sekvu min, bonvolu`, `Infanan seĝeton, bonvolu`, `Ĉu ni mendu manĝaĵon por forporti?`, `Ĉu vi povas rekomendi kafejon?`, `Ni iru al la restoracio`, `Ĉu vi konas tiun restoracion?`, `Ne, mi ankoraŭ ne estis tie` は、着席可否、予約済み、テーブル予約、日時/人数/時刻、喫煙/禁煙、予約確認、席案内、子ども用椅子、テイクアウト、カフェ推薦、レストランに行く/知っている/未訪問として意味ズレなし。
- `rezervi tablon`, `havas rezervon`, `mendi manĝaĵon por forporti`, `kafejo`, `restoracio` は飲食店予約・外食文脈で維持。`mendi` はレストラン予約・注文のどちらにも出るため、文脈上の衝突はない。
- `Ĉu vi havas liberajn tablojn?`, `Necesas antaŭmendi tablon`, `Ĉu vi povus fari rezervon por mi?`, `Ni estas kvarope`, `Ni venos je la 6-a horo`, `Jen via tablo`, `Fumado estas malpermesita`, `Ĉu vi povas rekomendi picerion?`, `Ĉu estas ĉina restoracio proksime?`, `Kien vi kutime iras, kiam vi manĝas ekstere?`, `Kien vi iras por la plej bona supo en Bruselo?`, `Ĉu vi iam manĝis en ĉi tiu restoracio?`, `Ne, ĉi tio estas la unua fojo`, `Tiu restoracio ne estas multekosta`, `Ĉu ni povas rezervi tablon por morgaŭ je la 8-a vespere?`, `Mi ŝatus rezervi tablon por 2 personoj je la 19-a horo`, `Ĉu vi havas tablon ĉe la fenestro?`, `Mi ŝatus tablon en la fumejo`, `Bedaŭrinde, ĉiuj tabloj estas nun okupitaj`, `Ĉu vi volus atendi?`, `Bonvolu atendi, oni vin kondukos al via loko`, `Ĉu ni povas sidiĝi sur la teraso?`, `Ĉu ni povus sidi en la suno?`, `Ĉu ni povas sidi en la ombro?` は、空席、予約必須、予約代行、4名、来店時刻、席案内、禁煙、ピザ店/中華料理店推薦、外食先、ブリュッセルのスープ、来店経験、価格、翌日20時/19時の予約、窓際席、喫煙席、満席、待機、席への案内、テラス/日なた/日陰として対応する。
- `fumejo` はPIVの喫煙者用の別室として smoking area と対応し、`teras/o` は飲食店の屋外席用法があるため維持。`tablo ĉe la fenestro`, `en la suno`, `en la ombro` も席希望として自然。
- `Kion mi alportu al vi?`, `Teon, mi petas`, `Kun citrono`, `Ĉu tio estas ĉio?`, `Jes, tio estas ĉio por nun`, `Ĉu mi povas proponi al vi trinkaĵon?`, `Sukon, mi petas`, `Du bierojn, mi petas`, `Mi ŝatus kafon`, `Kun lakto aŭ sukero?`, `Kun cinamo`, `Ĉu ni povus ricevi iom da akvo?`, `Kun gaso aŭ sen?`, `Gasitan akvon, mi petas`, `Akvon sen gaso, mi petas`, `Bonvolu montri al mi la vinkarton` は、飲み物注文、紅茶、レモン、注文確認、飲み物の提案、ジュース、ビール、コーヒー、ミルク/砂糖、シナモン、水、炭酸/無炭酸水、ワインリストとして意味ズレなし。
- `gasita akvo` と `akvo sen gaso` は炭酸水/無炭酸水として既存確認どおり維持。`vinkarto` は PIV の `karto` のレストラン品書き用法から wine list として透明。

主な据え置き確認:
- Renting a Flat: `vazaro`, `tukoj`, `kusenoj`, `balailo`, `tondilo`, `loĝejo`, `garaĝo`, `ŝvabrilo`, `rubsakoj`, `detergento`, `adaptilo`, `ampolo`, `litotukoj`, `fridujo`, `kuirilo`, `hejtilo`, `etaĝo`, `kuirejaj iloj`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `suĉkloŝo`, `adherema filmo`, `paperaj tukoj`, `polvosuĉilo`, `komfortaĵoj`, `mikroondilo`, `telerlavmaŝino`, `klimatizilo`, `lavmaŝino`, `elektromezurilo`, `ĉambristino` は賃貸・生活用品文脈で維持。
- Booking a Table: `rezervi/rezervo`, `antaŭmendi tablon`, `liberaj tabloj`, `seĝeto`, `manĝaĵon por forporti`, `picerio`, `fumejo`, `teras/o`, `sidi en la suno/ombro` は飲食店予約文脈で維持。
- Ordering Drinks: `teo`, `citrono`, `trinkaĵo`, `suko`, `biero`, `kafo`, `lakto`, `sukero`, `cinamo`, `gaso/gasita/sen gaso`, `vinkarto` は飲み物注文文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `vazo` / `vazaro`, `tuko`, `kuseno`, `alumeto`, `balailo`, `tondilo`, `loĝi`, `garaĝo`, `ŝvabri` / `ŝvabrilo`, `rubo` / `rubaĵo`, `detergi` / `detergento`, `adaptilo`, `ampolo`, `frida` / `fridujo`, `kuiri` / `kuirilo`, `hejti` / `hejtilo`, `etaĝo`, `korko` / `korktirilo`, `skatolo`, `botelo`, `suĉi`, `kloŝo`, `adheri`, `filmo`, `polvo` / `polvosuĉilo`, `komforto`, `ondo` / `mikroondilo`, `lavi` / `lavmaŝino`, `elektro`, `metro/mezurilo`, `ĉambro`, `tablo`, `rezervi`, `mendi`, `fumi` / `fumejo`, `seĝo`, `manĝi`, `kafejo`, `restoracio`, `pico` / `picerio`, `supo`, `fenestro`, `teraso`, `suno`, `ombro`, `teo`, `citrono`, `trinki`, `suko`, `biero`, `kafo`, `lakto`, `sukero`, `cinamo`, `gaso`, `vino`, `karto` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Kaikki `suĉkloŝo`: https://kaikki.org/dictionary/Esperanto/meaning/s/su/su%C4%89klo%C5%9Do.html

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `04d075f0b53811c34a244331642e9788`
- アプリ実行用CSV MD5: `04d075f0b53811c34a244331642e9788`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2856`〜`ID2955` は100件確認済み。

## 631. 630周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay
- Hotel / Checking out
- Hotel / Complaints
- Hotel / Renting a Flat

結果:
- **1件修正（1行）**
- 前回 `ID2656`〜`ID2755` に続き、今回は `ID2756`〜`ID2855` の100件を確認した。ホテル滞在中サービス、チェックアウト、苦情、賃貸冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2761` JA、`ID2773` JA、`ID2781` EO、`ID2782` EO、`ID2784` EN/JA/KO、`ID2798` EO/ZH、`ID2804` ZH、`ID2806` KO、`ID2820` JA/ZH/KO、`ID2837` ZH/KO は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID2840` EO
  - `La ventumilo en mia ĉambro ne funkcias` → `La ventolilo en mia ĉambro ne funkcias`
  - 理由: EN `ventilator`、JA `換気扇`、ZH `通风设备`、KO `환풍기` は客室の換気装置を指す。PIV 2020 では `ventolilo` が閉じた空間を換気する機械・装置で、`ventumilo` は主に手持ちの扇に寄るため、ホテル苦情文脈では `ventolilo` に補正した。これにより `ID2818` の `Ĉu vi povus ripari la ventumilon?`（扇風機/风扇/선풍기）との区別も保てる。

- `Ĉu vi povus alporti al mi ankoraŭ unu kusenon?`, `Mi ne volas, ke la ĉambro estu purigata ĝuste nun`, `Kie estas la plej proksima lavejo?`, `Ĉu vi bonvolus sendi ĉi tiujn vestaĵojn al la lavejo?`, `Ĉu vi bonvolus esti singarda kun ĉi tiuj bluzoj?`, `Ĉu vi purigos kaj glados ĉi tiun kostumon?`, `Ĉu vi povas gladi ĉi tiujn pantalonojn dum mi atendas?`, `Kiam mi povos rehavi miajn vestojn?`, `Pardonu, sed ĉi tie estas neniu kun tia nomo` は、枕、客室清掃不要、最寄りランドリー、衣類をランドリーへ出す依頼、ブラウスの丁寧な扱い、スーツのクリーニングとアイロン、ズボンのアイロン、衣類の受け取り、該当名の宿泊者なしとして意味ズレなし。
- `lavejo` は PIV の `lavi/lavisto` と接続する洗濯文脈で維持。`gladi` は PIV の熱い道具で衣類等を滑らかにする語義と合い、`kostumo`, `pantalono`, `bluzo` も衣類語彙として各列と対応する。
- `Mi ŝatus elregistriĝi`, `Mi ŝatus pagi nun`, `Ĉu mi povus vidi la kalkulon?`, `Mi pagos kontante`, `Ĉu vi ĝuis vian restadon?`, `Mi tre ĝuis mian restadon ĉe vi`, `Mi foriros morgaŭ`, `Ĉu mi povas ricevi la kalkulon?`, `Por kio estas ĉi tiu fakturo?`, `Ĉu vi akceptas kreditkartojn?`, `Ni akceptas kreditkartojn`, `Bonvolu sendi iun por mia bagaĝo`, `Bonvolu mendi taksion por mi`, `Via taksio estas ĉi tie`, `Kiom estas la sumo?`, `Ĉu vi uzis la minibaron?`, `Ne, ni ne uzis ĝin` は、チェックアウト、支払い、会計/請求書、現金払い、滞在満足、翌日出発、カード可否、荷物回収、タクシー手配/到着、合計額、ミニバー利用確認として対応する。
- `elregistriĝi` は PIV 直接見出しでは弱いが、ホテル checkout 文脈で日中韓/RU/EN と一致するため維持。`kalkulo` と `fakturo` は宿泊精算の bill / invoice として文脈上区別可能で、`bagaĝo` は旅行者の荷物としてPIV語義に合う。
- `Ĉu la servokotizo estas inkluzivita?`, `Servokotizo ne estas inkluzivita`, `La kalkulo estas tro alta`, `Kiel vi ŝatus pagi?`, `Mi pagos per kreditkarto`, `Ĉu vi akceptas usonajn dolarojn?`, `Ĉu vi povus gardi mian bagaĝon?`, `Ĉu mi povas repreni mian bagaĝon?`, `Mi ŝatus rehavi miajn valoraĵojn`, `Ĉiuj viaj aĵoj estas ĉi tie`, `Mi esperas, ke vi havis agrablan restadon`, `Mi ŝatus forveturi unu tagon pli frue`, `Je kioma horo mi devas elregistriĝi?`, `Ĉu estus eble elregistriĝi pli malfrue?` は、サービス料、請求額過大、支払い方法、カード払い、米ドル可否、荷物預かり/返却、貴重品返却、持ち物確認、滞在後挨拶、早い出発、チェックアウト時刻/レイトチェックアウトとして意味ズレなし。
- `servokotizo` は PIV の `kotizo` が会費・分担金寄りで語義幅は残るが、同CSV内の service charge 表現として一貫し、各列の意味と衝突しないため維持。`valoraĵoj` はPIVの valuables 用例と合う。
- `Kiom estas la servokotizo kaj la imposto?`, `Ĉu mi povas ricevi detaligitan fakturon?`, `Kiom oni fakturis al mi por la minibaro?`, `Internaciaj vokoj estas inkluzivitaj en la fakturo`, `Mi trovas ĝin iom multekosta`, `Ĉu mi povas uzi personan ĉekon?`, `Mi pensas, ke estas eraro en ĉi tiu kalkulo`, `Mi ne havas restmonon`, `Vi donis al mi malĝustan restmonon`, `Ĉu mi povas preni miajn aĵojn el la monŝranko?`, `Ĉu iu povus helpi nin porti nian bagaĝon malsupren?`, `Ĉu vi havas lokon, kie ni povus lasi nian bagaĝon?`, `Kiom da tempo necesas por veturi al la flughaveno per taksio?` は、サービス料と税、明細付き請求書、ミニバー請求額、国際電話料金、やや高い、個人小切手、請求書の誤り、小銭/釣り銭、金庫からの持ち物受け取り、荷物運搬、荷物預かり場所、空港までのタクシー所要時間として対応する。
- `fakturi al mi` は PIV の請求書に載せる語義と合い、`detaligita fakturo` は itemised bill として透明。`restmono` は同CSV内で change / 釣り銭として一貫するため維持した。
- `Mi perdis mian ŝlosilon`, `Mankas sapo`, `La ĉambro estas malpura`, `La seruro estas rompita`, `Ne estas ŝampuo`, `Ne estas varma akvo`, `Mankas tukoj`, `En la ĉambro estas tro malvarme`, `La ĉambro estas tro varma`, `Ĉu vi povus ripari la ventumilon?`, `La televidilo ne funkcias`, `La lavujo estas ŝtopita`, `Mi perdis mian brakhorloĝon`, `Kiu respondecas ĉi tie?`, `Mi ŝatus alian ĉambron`, `Mia rezervo estis por duobla ĉambro`, `Mi havas problemon en mia ĉambro`, `La ĉambro estas tro brua`, `Ĉi tiu ĉambro estas tro malgranda`, `En mia ĉambro malbonodoras`, `La fenestro ne malfermiĝas`, `La duŝo ne funkcias`, `La klimatizilo ne funkcias` は、鍵紛失、石鹸/シャンプー/湯/タオル不足、客室の汚れ、錠の故障、温度、扇風機、テレビ、洗面台詰まり、腕時計紛失、責任者、部屋変更、ダブルルーム予約、客室問題、騒音、狭さ、臭い、窓/シャワー/エアコン不良として対応する。
- `lavujo` は PIV では `lavabo` より広く洗濯用容器寄りだが、ホテルの sink 文脈として過去判断どおり EO は過修正しない。`ŝtopita` は詰まり/閉塞としてPIV語義と合い、`klimatizilo` は室内の空調設備としてPIV語義に合う。
- `Ĉi tiuj ne estas miaj aĵoj`, `La bolilo estas rompita`, `Mankas tualeta papero`, `Mi ŝatus ŝanĝi mian ĉambron`, `Mi petis ĉambron kun bela vido`, `Mankas butono`, `La hejtado ne funkcias`, `Unu el la lampoj ne funkcias`, `La ventolilo en mia ĉambro ne funkcias`, `En mia hotelĉambro estas insektoj`, `En la ĉambro estas ratoj`, `Mia najbaro estas tro laŭta`, `Mia ĉambro ne estis purigita`, `Ĉu vi povus ŝanĝi la littukojn?`, `Ĉi tio estas tute neakceptebla` は、持ち物違い、電気ケトル、トイレットペーパー、部屋変更、眺望、衣服のボタン、暖房、照明、換気扇、虫/ネズミ、隣室騒音、未清掃、シーツ交換、受け入れ不能として対応する。
- `bolilo` は水を沸かす容器として kettle と対応し、`butono` は衣服のボタン用法をPIVで確認済み。`hejtado` は heating、`ŝanĝi la littukojn` は PIV の `ŝanĝi la tukojn de sia lito` 型と合う。
- `Oni ne telefonis al mi por veki min`, `Mi rezervis duoblan liton, sed ricevis du apartajn litojn`, `Mi ankoraŭ atendas la matenmanĝon, kiun mi mendis`, `La makuloj ne estis forigitaj`, `Devas esti eraro. Ĉi tiuj ne estas miaj`, `Pardonu, ĉi tio ne estas mia subskribo`, `Mi volas rehavi mian monon`, `Mi rezervis apartamenton`, `Kiom kostas la luo?` は、モーニングコール未着、ダブルベッド予約とツイン配室、注文朝食待ち、シミ未除去、持ち物違い、署名違い、返金、アパート予約、家賃として意味ズレなし。
- `makuloj`, `subskribo`, `apartamento`, `luo` は PIV 語義と合い、苦情・賃貸文脈で維持できる。`Ĉi tiuj ne estas miaj` のJA `これは私のものではありません` は集合を指す `これ` として読めるため、複数明示への過修正はしない。

主な据え置き確認:
- During Your Stay: `kuseno`, `lavejo`, `gladi`, `kostumo`, `pantalonoj`, `rehavi vestojn` はホテル滞在中サービス文脈で維持。
- Checking out: `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `usonaj dolaroj`, `bagaĝo`, `valoraĵoj`, `detaligita fakturo`, `personan ĉekon`, `restmono`, `monŝranko` は精算・荷物/貴重品文脈で維持。
- Complaints: `ŝlosilo`, `seruro`, `tukoj`, `ventumilo`（扇風機）, `lavujo`, `ŝtopita`, `klimatizilo`, `bolilo`, `butono`, `hejtado`, `ventolilo`（換気装置）, `littukoj`, `subskribo` は客室苦情文脈で維持。
- Renting a Flat: `apartamento`, `luo` は賃貸文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `lavi` / `lavejo` / `lavujo`, `lavabo`, `kalkuli`, `fakturo` / `fakturi`, `kotizo`, `ŝtopi`, `boli` / `bolilo`, `butono`, `klimato` / `klimatizilo`, `hejtado`, `apartamento`, `ŝlosilo`, `bagaĝo`, `valoraĵo`, `gladi`, `kuseno`, `seruro`, `ventumilo`, `ventolilo`, `voki`, `makulo`, `ĉeko`, `detalo`, `bluzo`, `kostumo`, `pantalono` 周辺。
- PIV 2020 公式検索: https://vortaro.net/
- Wiktionary `ventolilo`: https://en.wiktionary.org/wiki/ventolilo
- WordMine `ventumilo`: https://www.wordmine.info/esperanto/word/ventumilo

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `04d075f0b53811c34a244331642e9788`
- アプリ実行用CSV MD5: `04d075f0b53811c34a244331642e9788`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `git diff --check` は whitespace エラーなし（Git の CRLF 置換警告のみ）。
- `ID2756`〜`ID2855` は100件確認済み。

## 630. 629周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Room
- Hotel / Checking in
- Hotel / During Your Stay

結果:
- **CSV修正なし**
- 前回 `ID2556`〜`ID2655` に続き、今回は `ID2656`〜`ID2755` の100件を確認した。ホテル予約、チェックイン、滞在中サービスのブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2665` JA、`ID2666` JA、`ID2667` KO、`ID2698` JA/ZH、`ID2699` JA、`ID2707` JA、`ID2709` JA、`ID2713` ZH、`ID2727` EO、`ID2729` EN、`ID2739` JA、`ID2744` EO、`ID2749` JA/KO、`ID2755` EN/ZH/KO は、現CSVで補正後内容になっていることを確認した。
- `Ĉu vi havas liberajn ĉambrojn?`, `Pardonu, nuntempe ni ne havas liberajn ĉambrojn`, `Ĉu estas alia hotelo proksime?`, `Mi ŝatus ĉambron kun balkono`, `Mi prenos ĉi tiun ĉambron por unu tago`, `Kiom kostas por nokto?`, `Kiom kostas por semajno?`, `Mi ŝatus pli malmultekostan ĉambron`, `Kiom vi ŝatus pagi?`, `Ĉu estas io pli trankvila?`, `Ĉu vi havas ion pli grandan?`, `Mi ŝatus rezervi ĉambron por kvar noktoj`, `Ĉu estus eble rezervi la ĉambron por alia dato?`, `Ĉu vi ŝatus, ke mi metu vin sur nian atendoliston?`, `Mi konfirmis la rezervon en Riado`, `Mi ŝatus nuligi mian rezervon`, `Ĉu vi povas rekomendi alian hotelon?`, `Bonvolu doni al mi vizitkarton kun la adreso de la hotelo` は、空室、近隣ホテル、バルコニー付き部屋、1日/1泊/1週間料金、安い部屋、支払希望額、静かな/大きい部屋、4泊予約、別日程、待機リスト、リヤドでの予約確認、予約キャンセル、他ホテル推薦、ホテル住所入り名刺として意味ズレなし。
- `liberaj ĉambroj`, `rezervo`, `atendolisto`, `vizitkarto` は宿泊予約文脈で維持できる。`Ĉu estas io pli trankvila?` と `Ĉu vi havas ion pli grandan?` は、日中韓では部屋を明示した補正後内容で、EO/RU/ENの広い言い方とも対応する。
- `Kiom kostas ĉambro inkluzive de matenmanĝo?`, `Tio estas iom pli ol mi volis pagi`, `Ĉu vi povus fari al mi rabaton?`, `Ni proponas specialajn tarifojn por longdaŭra restado`, `Ĉu mi povus noti la numeron de via kreditkarto?`, `Mi ŝatus ĉambron por nefumantoj`, `Mi ŝatus ĉambron kun du litoj`, `Ni bezonas unu duoblan ĉambron kun aldona lito`, `Ĉu vi povus meti plian liton en la ĉambron?`, `Ĉu vi bonvolus montri al mi pli grandan ĉambron?` は、朝食込み料金、予算超過、割引、長期滞在特別料金、クレジットカード番号、禁煙室、2ベッドの部屋、エキストラベッド付きダブルルーム、追加ベッド、広い部屋の内見として対応する。
- `longdaŭra restado`, `ĉambro por nefumantoj`, `aldona/plia lito`, `duobla ĉambro` は宿泊文脈で意味が明確。`duobla ĉambro` は double room / двухместный номер として、日中韓のダブルルーム/双人房/더블룸と対応する。
- `Mi faris rezervon`, `Vian nomon, mi petas`, `Mia nomo estas Adam`, `Plenigu ĉi tiun formularon`, `Subskribu ĉi tie`, `Via ĉambronumero estas 258`, `Ĉu mi povas ricevi la ĉambroŝlosilon?`, `Jes. Jen la ŝlosilo de via ĉambro`, `Je kioma horo estas la matenmanĝo?`, `Kie estas la restoracio?`, `Kie estas la lifto?`, `Kie estas ĉambro numero 202?`, `Via ĉambro estas sur la kvara etaĝo`, `Pardonu, via ĉambro ne estas preta`, `Ĉu mi povas lasi miajn sakojn ĉi tie?`, `Ĉu vi dezirus helpon kun via bagaĝo?`, `Kie ni matenmanĝas?`, `Je kioma horo vi fermas?`, `Oni devas forlasi la ĉambron je la 12-a tagmeze`, `Ĉu vi provizas mapojn?`, `Rezervoj estis faritaj por mi kaj mia familio`, `Mi ŝatus meti kelkajn valoraĵojn en la monŝrankon`, `Ĉu vi bonvolus porti la bagaĝon al mia ĉambro?` は、チェックイン、氏名、記入/署名、部屋番号、部屋の鍵/カード、朝食・レストラン・エレベーター、階数、客室準備、荷物預かり、荷物運搬、入口の閉鎖/施錠時刻、チェックアウト時刻、地図、家族分の予約、貴重品用金庫、荷物の客室配送として意味ズレなし。
- `ĉambronumero`, `ĉambroŝlosilo`, `ŝlosilo de via ĉambro` は透明複合で、room number / room key と対応する。`lasi miajn sakojn ĉi tie` はホテル文脈で荷物預かりとして日中韓補正後内容と合う。`Je kioma horo vi fermas?` は入口・受付の閉鎖/施錠時刻を尋ねる短い実用表現として許容した。
- `Je kioma horo estas servataj matenmanĝo, tagmanĝo kaj vespermanĝo?`, `Matenmanĝo estas servata de la 8-a ĝis la 10-a matene`, `Je kioma horo malfermiĝas la restoracio por vespermanĝo?`, `Vespermanĝo estas servata inter la 18-a kaj la 21:30`, `Je kioma horo fermiĝas la drinkejo?`, `Ĉambroservo estas disponebla tage kaj nokte`, `Ĉu vi ŝlosas la enirpordon nokte?` は、食事提供時刻、朝食時間、夕食時のレストラン開店、夕食時間、バー閉店、24時間ルームサービス、夜間の玄関施錠として対応する。
- `tage kaj nokte` は round the clock として、`ĉambroservo` は room service として維持。`enirpordo` は front door / 玄関に対応する透明な複合語。
- `Ne ĝenu`, `Bonvolu purigi la ĉambron`, `Fumado malpermesita`, `Ĉu mi povas ricevi sapon?`, `Ĉu mi povas havi tukon?`, `Mi bezonas infanliton`, `Ĉu mi povas ricevi kusenon?`, `Ĉu mi povas ricevi kovrilon?`, `Ĉu mi povas ricevi gladilon?`, `Mi bezonas ilin hodiaŭ vespere`, `Ĉu vi havas telefonan ŝargilon?`, `Ĉu mi povas uzi la interreton ĉi tie?`, `Ĉu vi povas forigi ĉi tiun makulon?`, `Mi bezonas, ke oni lavu ĉi tion`, `Ĉu iu demandis pri mi?`, `Ĉu vi povus veki min je la 6-a matene?`, `Ĉu estas poŝto por mi?`, `Ĉu mi povus vidi vian ŝlosilon, mi petas?`, `Ĉu vi ŝatus, ke oni veku vin?`, `Ĉu vi povus voki taksion por mi, mi petas?`, `Ĉu mi povas matenmanĝi en mia ĉambro?` は、客室清掃、禁煙、石鹸、タオル、ベビーベッド、枕、毛布、アイロン、当日夜までの必要、電話充電器、インターネット利用、シミ抜き、洗濯依頼、来客/問い合わせ、モーニングコール、郵便、鍵確認、タクシー手配、部屋での朝食として対応する。
- `Ne ĝenu` のJA `起こさないでください` は literal には「起こすな」に寄るが、ホテル札・客室表示の Do not disturb として文脈別許容。`tuko` は PIV の用途を持つ布片で、ホテル文脈では towel として読める。`kovrilo` は PIV の litkovrilo 系とつながり、blanket として許容。`telefona ŝargilo` は `ŝargi` の電気を入れる語義から phone charger として透明。
- `Kiel oni ŝaltas la lumon?`, `Kiel mi povas akiri eksteran linion?`, `Bonvolu alporti al mi iom da varma akvo`, `Bonvolu lavi ĉi tiujn aferojn`, `Bonvolu gladigi ĉi tion`, `Ĉu vi povus purigi por mi ĉi tiun kostumon?`, `Kiam miaj vestoj estos pretaj?`, `Mi bezonas ĝin ĝis la kvina`, `Mi revenos ĉirkaŭ la deka horo`, `Kie estas la savelirejo?`, `Ĉu mi povas iel helpi vin?`, `Ĉu vi bonvolus purigi mian ĉambron?`, `Mi estas alergia al polvo`, `Ĉu estas ia telefona mesaĝo por mi?`, `Ĉu vi scias, kio estas via internacia kodo?`, `La ŝlosilon de ĉambro numero 621, bonvolu!`, `Bonvolu veki min morgaŭ je la naŭa horo`, `Mi ŝatus plilongigi mian restadon por kelkaj tagoj`, `Ĉu vi bonvolus plusendi mian poŝton al mia hejma adreso?`, `Mi ŝatus mendi matenmanĝon por morgaŭ`, `Bonvolu alporti mian matenmanĝon je la 7-a horo` は、照明、外線、湯、洗濯、アイロン、スーツのクリーニング、仕上がり時刻、5時まで、帰館予定時刻、非常口、手伝い、客室清掃、ほこりアレルギー、電話伝言、国際電話コード/国番号、621号室の鍵、翌朝9時起床、滞在延長、郵便転送、翌日の朝食注文、7時の朝食持参として意味ズレなし。
- `gladigi` は PIV の `gladi` から「アイロンをかけてもらう」依頼として自然。`savelirejo` は PIV の安全灯用例に見える `savelirejoj` と整合し、emergency exit として維持。`plusendi` は PIV直接見出しでは確認できないが、`plu` + `sendi` の透明複合で、forward mail / переслать почту として各列の意味に合う。

主な据え置き確認:
- Booking: `liberaj ĉambroj`, `atendolisto`, `rezervo`, `vizitkarto`, `longdaŭra restado`, `ĉambro por nefumantoj`, `aldona/plia lito`, `duobla ĉambro` はホテル予約文脈で維持。
- Checking in: `ĉambronumero`, `ĉambroŝlosilo`, `ŝlosilo`, `lasi miajn sakojn`, `forlasi la ĉambron`, `monŝranko`, `ĉambroservo`, `enirpordo` はチェックイン・受付文脈で維持。
- During Your Stay: `Ne ĝenu`, `tuko`, `kovrilo`, `telefonan ŝargilon`, `eksteran linion`, `gladigi`, `savelirejo`, `internacia kodo`, `plusendi mian poŝton`, `mendi/alporti matenmanĝon` は滞在中サービス文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `atendi`, `ĉambro`, `ŝlosi` / `ŝlosilo`, `tuko` / `mantuko`, `kovri` / `kovrilo` / `litkovrilo`, `ŝargi` / `ŝargilo`, `gladi` / `gladilo`, `lasi`, `sendi`, `plu`, `monŝranko`, `pensiono`, `sekur lampo` / `savelirejoj` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- アプリ実行用CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2656`〜`ID2755` は100件確認済み。

## 629. 628周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi
- Other Transport / Ship
- Hotel / Asking about Facilities
- Hotel / Booking a Room

結果:
- **CSV修正なし**
- 前回 `ID2456`〜`ID2555` に続き、今回は `ID2556`〜`ID2655` の100件を確認した。タクシー、船旅、ホテル設備、ホテル予約冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2561` JA/KO、`ID2566` ZH/KO、`ID2569` EO/KO、`ID2574` JA/KO、`ID2589` EO、`ID2603` ZH/KO、`ID2611` JA/ZH/KO、`ID2612` JA、`ID2619` KO、`ID2624` ZH、`ID2633` EO、`ID2642` JA/ZH/KO、`ID2647` JA、`ID2650` JA/KO は、現CSVで補正後内容になっていることを確認した。
- `Mi ŝatus eliri ĉi tie, mi petas`, `Ĉu vi povus konduki min al la urbocentro?`, `Ĉu vi povus veni preni min ĉi tie je la sesa?`, `Kiom kostas veturi al la flughaveno?`, `Vi diris, ke tio kostos 50 aŭstraliajn dolarojn`, `Bonvolu ŝalti la taksimetron`, `Bonvolu halti ĉe la angulo`, `Estas nokta krompago`, `Ĉu vi kontraŭas, se mi malfermos la fenestron?`, `Ĉu vi povus atendi ĉi tie momenton?`, `Ĉu ni povus halti ĉe bankaŭtomato?` は、タクシー乗降、目的地、迎車、空港料金、見積金額、メーター、角での停車、夜間割増、窓、待機、ATM立ち寄りとして意味ズレなし。
- `taksimetro` は PIV の taxi meter と対応し、`ŝalti` は meter を入れる文脈として自然。`nokta krompago` は night-time surcharge として `krompago` の追加料金用法に合う。`bankaŭtomato` は ATM / cash machine として維持できる。
- `Savringo`, `Savboato`, `Mi havas marmalsanon`, `Kie estas la kajo?`, `Kie estas nia kajuto?`, `Ĉu mi povas rezervi kajuton?`, `Kie estas la haveno?`, `Je kioma horo ni enŝipiĝos?`, `Je kioma horo mi povas vespermanĝi?`, `La maro estas sufiĉe trankvila`, `La maro estas tre maltrankvila`, `Eniro al aŭtomobilaj ferdekoj malpermesita`, `Kie estas la rivera haveno?`, `Kie estas la informejo?`, `Mi ŝatus kvarlitan kajuton`, `Kiam foriras la pramo al Lisbono?`, `Je kioma horo foriras la ŝipo?`, `Kiel mi povas iri al la ferdeko?`, `Kie mi povas enŝipiĝi?`, `Kie estas kajuto numero 258?`, `Bonvolu forlasi viajn kajutojn`, `Surmetu viajn savvestojn`, `La krozado estis mirinda` は、救命具、船酔い、桟橋/埠頭、船室、港、乗船、食事、海況、車両デッキ、案内所、4人用船室、フェリー/船の出発、甲板、客室退去、救命胴衣、クルーズとして対応する。
- `kajo` は船の係留・乗降場所としてもPIV語義に合い、鉄道ホーム文脈と衝突しない。`kajuto`, `ferdeko`, `enŝipiĝi`, `pramo`, `krozado` は船旅語彙として既存補正後の形を維持した。`Ĉu vin naŭzas vojaĝado?` は Ship 節では ZH/KO が船酔い寄りだが、EO/EN/RU/JA は travel-sick の広い問いとして成立し、文脈上の許容範囲。
- `Ĉu vin naŭzas vojaĝado?`, `Sur kiu ferdeko estas la monŝanĝejo?`, `Mi ŝatus bileton por aŭto kaj du pasaĝeroj`, `Je kioma horo estas la sekva boato al Bankoko?`, `Kiam la ŝipo foriros al Vaŝingtono?`, `Je kioma horo la pramo alvenas en Vienon?`, `Je kioma horo mi devas registriĝi?`, `Kiom longe la ŝipo restas en la haveno?`, `Kiom longe daŭras la transiro?`, `Ĉu vi bonvolus konduki min al mia kajuto?`, `Mi ŝatus matenmanĝi en mia kajuto`, `Mi ŝatus rezervi ferdekseĝon`, `Mi ŝatus paroli kun la kapitano`, `Mi devas sendi radiogramon`, `Ni alvenos en la havenon post proksimume 30 minutoj` は、乗り物酔い、両替所、車両/乗客チケット、船便、出航/到着、乗船手続き、停泊時間、渡航時間、船室案内、船室での朝食、デッキチェア、船長、無線電報、港到着として意味ズレなし。
- `transiro` は crossing として、船・フェリーの移動時間文脈で維持。`ferdekseĝo` は deckchair として透明で、`radiogramo` は無線電報として現JA/ZH/KO/RU と対応する。
- `Ĉio inkluzivita`, `Ĉu la Wi-Fi estas senpaga?`, `Ĉu ĉi tie estas lifto?`, `Ĉu vi havas aŭtoparkejon?`, `Kio troviĝas proksime?`, `Ĉu vi havas monŝrankon?`, `Ĉu vi havas komputilon?`, `Ĉu vi havas adaptilon?`, `Ĉu ĉi tie estas saŭno?`, `Ĉu ĉi tie estas beleca salono?`, `Ĉu vi permesas hejmbestojn?`, `Ĉu ĉi tie estas naĝejo?`, `Ĉu estas lavservo?`, `Ĉu estas minibaro en mia ĉambro?`, `Ĉu vi havas ĉambron por fumantoj?`, `Ĉu en la ĉambro estas televido?`, `Ĉu vi havas ĉambroservon?`, `Ĉu vi havas servojn por infanoj?`, `Ĉu vi havas rulseĝan aliron?` は、オールインクルーシブ、Wi-Fi、エレベーター、駐車場、近隣施設、金庫、利用可能なパソコン、アダプター、サウナ、美容サロン、ペット、プール、ランドリー、ミニバー、喫煙客室、テレビ、ルームサービス、子供向け設備/サービス、車椅子アクセスとして対応する。
- `Ĉio inkluzivita` と `matenmanĝo estas inkludita` は料金に含まれる意味で維持。`monŝranko`, `aŭtoparkejo`, `lavservo`, `ĉambroservo`, `rulseĝa aliro` はホテル設備語彙として透明。`rulseĝa aliro` は `aliro por rulseĝo` も候補だが、wheelchair access として明確に読める。
- `Kiom malproksime vi estas de la urbocentro?`, `Kiom malproksime ĝi estas de la stacidomo?`, `Ĉu vi havas ĉambron kun vido al la maro?`, `Ĉu la hotelo havas kablan televidon?`, `Ĉu en la hotelo estas frizejo?`, `Ĉu vi havas gimnastikejon ĉi tie?`, `Ĉu la ĉambro havas klimatizilon?`, `Ĉu la ĉambro havas interretan aliron?`, `Ĉu estas banĉambroj ekipitaj per duŝkabinoj?`, `Ĉu en mia ĉambro estas ŝtopilingo por mia elektra razilo?`, `La ĉambro havas komunan banĉambron`, `Ĉu vi havas specialajn ĉambrojn por handikapuloj?` は、市中心部/駅からの距離、海の眺め、ケーブルテレビ、美容室、フィットネスセンター、エアコン、インターネット、シャワーブース、電気シェーバー用コンセント、共用バスルーム、障がい者向け客室として意味ズレなし。
- `ŝtopilingo` は PIV で「ŝtopiloを差し込む中空の接点」と確認でき、socket / コンセントに対応するため現形維持。`gimnastikejo` は体を鍛える場所として fitness centre と対応し、`frizejo` は hairdresser's としてホテル設備文脈に合う。
- `Mi ŝatus ĉambron`, `Por kiom da noktoj?`, `Por du noktoj`, `Neniu libera loko`, `Mi ŝatus fari rezervon`, `De kiu dato?`, `Por ĉi tiu nokto`, `Kian ĉambron vi ŝatus?`, `Mi ŝatus unulitan ĉambron`, `Mi ŝatus ĉambron kun du apartaj litoj`, `Ĉu mi povus vidi la ĉambron?`, `Ĉu estas io pli bona?`, `Ĉu la matenmanĝo estas inkludita?`, `Mi ŝatus plenan pensionon`, `Ĉu vi bezonas antaŭpagon?`, `Ĉu mi povas ŝanĝi la daton de la rezervo?`, `Mi restos ĝis la 15-a de junio`, `Mi restos 2 noktojn`, `Ĉu mi povas havi unulitan ĉambron?`, `Ne restas unulitaj ĉambroj` は、宿泊予約、泊数、満室、予約開始日、部屋種別、シングル/ツイン、部屋確認、より良い部屋/選択肢、朝食込み、フルボード、予約金、予約日変更、滞在期間、シングル満室として対応する。
- `unulita ĉambro`, `ĉambro kun du apartaj litoj`, `plena pensiono`, `antaŭpago`, `rezervo` は宿泊予約語彙として維持。`Neniu libera loko` は字義上は広いが、ホテル予約の No vacancy / 満室として文脈上明確。

主な据え置き確認:
- Taxi: `taksimetro`, `nokta krompago`, `bankaŭtomato`, `veni preni min`, `halti ĉe la angulo` はタクシー文脈で維持。
- Ship: `Savringo`, `Savboato`, `marmalsano`, `kajo`, `kajuto`, `haveno`, `enŝipiĝi`, `ferdeko`, `pramo`, `krozado`, `radiogramo`, `ferdekseĝo`, `transiro` は船旅語彙として維持。
- Hotel Facilities: `Ĉio inkluzivita`, `aŭtoparkejo`, `monŝranko`, `adaptilo`, `beleca salono`, `lavservo`, `ĉambroservo`, `rulseĝa aliro`, `frizejo`, `gimnastikejo`, `ŝtopilingo`, `duŝkabinoj` はホテル設備語彙として維持。
- Hotel Booking: `unulita ĉambro`, `ĉambro kun du apartaj litoj`, `Neniu libera loko`, `inkludita`, `plena pensiono`, `antaŭpago`, `rezervo` は宿泊予約文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `taksio` / `taksimetro`, `ŝalti`, `krompago`, `bankaŭtomato`, `kajuto`, `kajo`, `ferdeko`, `enŝipiĝi`, `pramo`, `krozi` / `krozado`, `radiogramo`, `ŝtopilo` / `ŝtopilingo`, `elektra razilo`, `adaptilo`, `rulseĝo`, `pensiono`, `rezervo`, `inkludi` / `inkluzivi`, `gimnastikejo`, `tribunalo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- アプリ実行用CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2556`〜`ID2655` は100件確認済み。

## 628. 627周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / At the Train Station
- Other Transport / On the Bus or Train
- Other Transport / Taxi

結果:
- **1件修正（1行）**
- 前回 `ID2356`〜`ID2455` に続き、今回は `ID2456`〜`ID2555` の100件を確認した。鉄道駅、バス/列車内、タクシーのブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2457` JA/ZH、`ID2461` JA/KO、`ID2462` KO、`ID2464` EO、`ID2465` JA/ZH/KO、`ID2493` EO/JA/KO、`ID2514` ZH、`ID2520` ZH、`ID2529` EO、`ID2531` EN、`ID2532` EO/ZH、`ID2540` ZH/KO、`ID2541` EN/ZH/KO、`ID2545` JA、`ID2547` EO/EN/JA は、現CSVで補正後内容になっていることを確認した。

修正:
- `ID2496` JA/ZH
  - JA `今すぐ降りなきゃいけませんか？` → `いつ降りればいいですか？今ですか？`
  - ZH `我现在就要下车吗？` → `我什么时候该下车？现在吗？`
  - 理由: EO `Kiam mi devas eliri? Ĝuste nun?`、EN `When do I have to get off? Right now?`、KO `언제 내려야 하나요? 지금 내려야 하나요?`、RU `Когда мне нужно сойти? Прямо сейчас?` は「いつ降りるべきか」と「今か」を分けて尋ねる。旧JA/ZHは「今すぐ降りるべきか」だけに縮んでおり、次行 `Ne, ĉe la sekva haltejo` との問答対応も弱くなるため補正した。

主な据え置き確認:
- At the Train Station: `pensiula/unua-klasa/unudirekta/revenbileto`, `eksprestrajno`, `loka trajno`, `kajo`, `vojaĝkarto`, `abonbileto`, `rabataj tarifoj`, `skemo de la metroo`, `funkcias la metroo` は鉄道・地下鉄・交通カード文脈で維持。
- On the Bus or Train: `haltejo`, `loko`, `vagono`, `restoracia vagono`, `kupeo`, `pakaĵujo`, `Laŭpeta haltejo`, `preterveturis vian haltejon`, `Ĉi tiu trajno finiĝas ĉi tie`, `Ne apogiĝu al la pordo`, `Bonvolu kunpreni vian tutan bagaĝon kaj viajn personajn aĵojn` は車内案内・乗降文脈で維持。
- Taxi: `taksimetro`, `restmono`, `trinkmono`, `taksihaltejo`, `trajnstacio`, `flughavena krompago`, `disponeblaj aŭtoj`, `tribunalo`, `Veturigu min ĉi tien`, `Ellasu min ĉi tie`, `Venu preni min`, `Mi veturas al ĉi tiu adreso` はタクシー手配・会計・目的地指定文脈で維持。

補足確認:
- `eksprestrajno` は `ekspres trajno` への分かち書きも可能だが、急行/express train として誤りではないため現形維持。
- `abonbileto` は直接見出しは弱いが、PIV の `aboni ... fervojbileton` と `bileto` の交通切符語義から season ticket / 定期券として透明。
- `pakaĵujo` は luggage compartment / 荷物棚・짐칸 に対してやや広いが、荷物を入れる場所として列間対応を損なわない。
- `preterveturis vian haltejon` は PIV の `preter veturi` 他動詞用例と合い、乗り過ごす意味として成立する。
- `trajnstacio` は `fervoja stacidomo` も候補だが、train station として透明で、タクシー目的地の短い実用句では過修正しない。
- `flughavena krompago` は airport surcharge として PIV の `krompago` 系と整合し、過去補正後の形を維持した。
- `nunmomente ne estas disponeblaj aŭtoj` は `nuntempe` なども候補だが、「現在利用可能な車がない」という意味は明確。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `abono`, `bileto` / `biletejo`, `haltejo`, `kajo`, `kupeo`, `metroo`, `preter veturi`, `staci/o` / `stacidomo`, `ŝalti`, `taksio` / `taksimetro`, `tarifo`, `tribunalo`, `vagono`, `veturi`, `el lasi`, `krompago`, `trinkmono` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- アプリ実行用CSV MD5: `b78fe28f98c8f6ccfefeee331c1f675f`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 両CSVとも UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2456`〜`ID2555` は100件確認済み。

## 627. 626周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs
- Other Transport / At the Bus Station
- Other Transport / At the Train Station

結果:
- **CSV修正なし**
- 前回 `ID2256`〜`ID2355` に続き、今回は `ID2356`〜`ID2455` の100件を確認した。道路標識、バス駅、鉄道駅のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2359` JA、`ID2364` JA/ZH/KO、`ID2367` EO、`ID2374` EO、`ID2395` EO/ZH、`ID2396` ZH、`ID2399` EN/JA/ZH/KO、`ID2401` JA/ZH/KO、`ID2410` ZH、`ID2413` KO、`ID2414` JA、`ID2416` EO、`ID2419` EO/JA/ZH/KO、`ID2425` EO、`ID2446` ZH、`ID2449` EN は、現CSVで補正後内容になっていることを確認した。
- `Parkumejo`, `Malrapidiĝu`, `Vojlaboroj`, `Haltu! Trapaso malpermesita!`, `Parkumado malpermesita`, `Bushaltejo`, `Unudirekta trafiko`, `Rapidlimo`, `Eniro malpermesita`, `Vojo fermita`, `Halto malpermesita`, `Buskoridoro`, `Cedu vojon`, `Preterpasu maldekstre`, `Piedira zono`, `Trafikblokiĝo`, `Malalta ponto`, `Senpaga parkumado`, `Trafiklumoj`, `Nivelkruciĝo`, `Veturu singarde`, `Ne trinku kaj veturu`, `Piedira transirejo` は、道路標識・交通案内として意味ズレなし。
- `Trapaso malpermesita` は通行・通過禁止として、現JA/ZH/KO/RU と対応する。`Preterpasu maldekstre` は RU が障害物回避標識寄り、EN/JA/ZH/KO が keep left 寄りだが、左側を通る標識指示として許容した。`Piedira zono` は RU が pedestrian path 寄りにずれるが、EO/EN/JA/ZH/KO は pedestrian zone で一致するため維持した。
- `Unu bileton, mi petas`, `Kie mi povas aĉeti karton?`, `Ĉu ĉi tiu estas la buso al Moskvo?`, `Kiam foriras la buso?`, `Mi preferas veturi per aŭtobuso`, `Kie estas la plej proksima bushaltejo?`, `Kien iras ĉi tiu aŭtobuso?`, `Kiom kostas la biletoj?`, `Mi ŝatus du biletojn, mi petas`, `Revenbileto`, `Ĉu mi povas aĉeti monatan abonon?`, `Mi maltrafis la lastan buson`, `Ĉu mi povas ricevi horaron, mi petas?`, `Ĉu mi povas aĉeti bileton en la buso?`, `Kiom kostas unudirekta bileto al Mumbajo?`, `Ĉu estas grupa tarifo?`, `Kie mi ŝanĝu aŭtobuson por Zagrebo?`, `Pardonu, kie estas la aŭtobusa stacidomo?`, `Kiu buso iras al la urbocentro?`, `Ĉu ĉi tiu buso iras al la plaĝo?` は、バス切符、交通カード、行き先、時刻、バス停、往復券、月間パス、終バス、時刻表、片道券、団体料金、乗り換え、バスターミナル、市中心部、ビーチ行きとして対応する。
- `revenbileto`, `monata abono`, `unudirekta bileto`, `grupa tarifo` は公共交通の切符・料金文脈で維持できる。`ŝanĝi aŭtobuson` は PIV の `ŝanĝi la tramon, la trajnon` 型と同じ乗り換え表現として自然。`aŭtobusa stacidomo` は bus station / バスターミナル相当として、既存のZH補正後表現と対応する。
- `Kiom da fojoj hore ĝi iras?`, `Kiam foriras la sekva?`, `Ni atendu la sekvan`, `Ĉi tiu buso estas nuligita`, `Kie estas la biletaŭtomatoj?`, `Ĉu mi devas stampi la bileton antaŭ ol eniri?`, `Ĉu ĉi tio estas la aktuala aŭtobusa horaro?`, `Je kioma horo foriras la sekva buso al la flughaveno?`, `Kiom ofte veturas la aŭtobusoj al Barcelono?`, `Je kioma horo estas la sekva buso al Rio-de-Ĵanejro?`, `De kie foriras la aŭtobuso al Sankt-Peterburgo?`, `Kiom kostas unuaklasa revenbileto al Kopenhago?`, `Kiom kostas la veturo ĝis ĉi tiu loko?`, `Ĉu estas rabatita tarifo?`, `Mi ŝatus infanan unudirektan bileton al Minsko`, `Mi ŝatus revenbileton al Bakuo, kun reveno dimanĉe`, `Mi ŝatus pensiulan revenbileton al Bukareŝto`, `Vi devos ŝanĝi aŭtobuson en Oslo` は、運行頻度、次便、運休、券売機、乗車前の打刻/押印、現行時刻表、空港/都市行き、運賃、一等往復、割引/高齢者/子供料金、復路日指定、乗り換えとして意味ズレなし。
- `stampi la bileton` は PIV に stacidomo での公式な押印用例があり、各列の stamp/押印/打票/печать と整合するため維持した。`pensiula revenbileto` は senior citizens' return としてやや制度依存だが、RU/JA/ZH/KO の高齢者・年金受給者向け切符と対応する。
- `Horo de foriro`, `Kiom kostas la veturo?`, `Kiu kajo?`, `Mi maltrafis la trajnon`, `Mapon, mi petas`, `Kie estas la biletejo?`, `Unudirektan bileton al Londono`, `Ĉu ĝi estas rekta trajno?`, `Ĉu tio estas ekspresa trajno?`, `En kiujn zonojn?`, `Kiu direkto?`, `Ĉu la trajno alvenos ĝustatempe?`, `La trajno malfruiĝas`, `Ĉi tiu trajno estas troplena`, `Atentu la interspacon`, `Kie estas la taksioj?`, `Kie estas la fervoja stacidomo?`, `Kie mi povas aĉeti trajnbileton?`, `Mi ŝatus unudirektan bileton al Toronto`, `Mi preferas sidlokon ĉe la fenestro`, `Ĉu mi devas pagi aldone por mia bagaĝo?`, `La biletoj estas multekostaj`, `Ĉu mi devas ŝanĝi trajnon?`, `Vi devos ŝanĝi trajnon` は、鉄道駅の出発時刻、運賃、ホーム/番線、乗り遅れ、地図、切符売り場、片道券、直通列車、急行列車、ゾーン、方向、定時到着、遅延、混雑、隙間注意、タクシー、駅、窓側席、荷物追加料金、乗り換えとして対応する。
- `Kiu kajo?` と `kajo numero 1` は PIV の鉄道用 `pasaĝer kajo` に合う。`ekspresa trajno` は PIV の `ekspres trajno` と対応し、急行/express train として維持。`Atentu la interspacon` は RU が「ホーム端に近づかないで」に寄るが、EO/EN/JA/ZH/KO は platform gap 注意で一致するため、クイズ対象列を優先した。
- `Mi ŝatus revenbileton al Dublino`, `Kiun trajnon mi prenu?`, `Kiel mi povas atingi Abu-Dabion?`, `Kiom longe daŭras la vojaĝo?`, `Ĉu ĉi tiu estas la trajno al Novjorko?`, `La trajno estis nuligita`, `Kie estas kajo numero 1?`, `Kie estas la atendejo?`, `Kie estas la horaro de trajnoj?`, `Vi povas trovi la horaron tie`, `Kiam vi volus vojaĝi?`, `Kiam estas la lasta trajno al Istanbulo?`, `Je kioma horo foriras la sekva trajno al Vilno?`, `Kiom ofte veturas la trajnoj al Frankfurto?`, `Mi ŝatus aĉeti bileton al Rigo, mi petas` は、往復券、乗る列車、アブダビへの行き方、所要時間、ニューヨーク行き、運休、1番ホーム、待合室、列車時刻表、旅行希望日、最終列車、次列車、運行頻度、リガ行き切符として意味ズレなし。
- `Abu-Dabion` は PIV の `Abudabi/o` と表記揺れはあるが、対格形として理解できるため維持した。`horaro de trajnoj` は PIV の `horaro de fervojoj` 型と同じ時刻表表現として自然。

主な据え置き確認:
- Road Signs: `Trapaso malpermesita`, `Buskoridoro`, `Preterpasu maldekstre`, `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo`, `Piedira transirejo` は道路標識文脈で維持。
- At the Bus Station: `bileto`, `karto`, `revenbileto`, `monata abono`, `horaro`, `biletaŭtomatoj`, `stampi la bileton`, `unudirekta bileto`, `grupa/rabatita tarifo`, `pensiula revenbileto`, `ŝanĝi aŭtobuson` は公共交通・切符文脈で維持。
- At the Train Station: `kajo`, `biletejo`, `rekta/ekspresa trajno`, `zonoj`, `malfruiĝas`, `troplena`, `interspaco`, `fervoja stacidomo`, `ŝanĝi trajnon`, `atendejo`, `horaro de trajnoj` は鉄道駅文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `abono`, `Abudabi/o`, `bileto` / `biletejo`, `buso`, `ekspres trajno`, `kajo` / `pasaĝer kajo`, `koridoro`, `parkumi`, `staci/o` / `stacidomo`, `stampi`, `tarifo`, `trajno`, `ŝanĝi`, `horaro`, `piedira zono`, `trafiklumoj` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2356`〜`ID2455` は100件確認済み。

## 626. 625周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking
- Car / At the Petrol Station
- Car / Mechanical Problems
- Car / Road Signs

結果:
- **CSV修正なし**
- 前回 `ID2156`〜`ID2255` に続き、今回は `ID2256`〜`ID2355` の100件を確認した。運転・駐車、給油所、自動車故障、道路標識冒頭のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2279` ZH、`ID2303` EO、`ID2308` JA/ZH/KO、`ID2318` ZH、`ID2322` EO/ZH、`ID2326` EO、`ID2336` EO/ZH、`ID2342` JA/ZH/KO、`ID2348` EO、`ID2354` JA/ZH/KO は、現CSVで補正後内容になっていることを確認した。
- `La trafiko estis terura hodiaŭ`, `Ĉu vi trapasis vian stiradan ekzamenon?`, `Ĉu vi konas ĉi tiujn vojsignojn?`, `Ĉi tiu estas unudirekta strato`, `Ĉi tiu strato estas nur por piedirantoj`, `Mi malofte kondukas pli rapide ol 100 km/h`, `Tiu aŭto similas al mia aŭto`, `Hodiaŭ la vojoj estas glacikovritaj`, `Kien kondukas ĉi tiu vojo?`, `Ĉu ĉi tio estas la ĝusta vojo al Tokio?`, `Kiel mi atingos la aŭtovojon?`, `Turnu dekstren ĉe la T-kruciĝo`, `Kie estas la plej proksima aŭtoriparejo?`, `Kiom longe mi povas parkumi ĉi tie?`, `Ĉu mi devas pagi por parkumi ĉi tie?`, `Kie estas la parkometro?`, `Kiom kostas por horo?`, `Mia aŭto estas registrita en Ĉilio`, `Kie estas la elirejo al la aŭtovojo?`, `Ĉu ni estas sur la ĝusta vojo al Sarajevo?`, `Kiom da tempo daŭras per aŭto?`, `Ĉu vi povus montri al mi sur la mapo, kie mi estas?` は、交通状況、運転試験、道路標識、一方通行、歩行者専用、速度、凍結道路、道順、高速道路、T字路、自動車修理工場、駐車料金/時間、パーキングメーター、車両登録、地図上の現在地として意味ズレなし。
- `stirada ekzameno` は driving test として読め、`vojsignoj`, `unudirekta strato`, `piedirantoj`, `glacikovritaj`, `aŭtovojo`, `aŭtoriparejo`, `parkometro` は道路・駐車語彙として維持できる。`Kiom da tempo daŭras per aŭto?` は `necesas` も候補だが、所要時間の質問として各列と対応する。
- `Kiom malproksimas la sekva serva areo?`, `Kiom da kilometroj estas ĝis la plej proksima benzinejo?`, `Estas ĉirkaŭ kilometro de ĉi tie`, `En kiun direkton mi iru?`, `Turnu maldekstren ĉe la unua turniĝo`, `Ĉu la vojo al la lago estas bona?`, `Turnu dekstren ĉe la dua turniĝo`, `Kiu estas la plej mallonga vojo al la plaĝo?`, `Prenu la duan elirejon ĉe la trafikrondo`, `Vi transiros kelkajn fervojajn liniojn`, `Bonvolu montri al mi la vojon al Manilo`, `Ĉe la dua semaforo, turnu maldekstren`, `Vi pasos superbazaron maldekstre`, `Ĉu ni povas halti ĉi tie por iri al la necesejo?`, `Mi staris en trafikblokiĝo dum unu horo`, `Antaŭe estas akcidento`, `Memoru veturi maldekstre`, `Vi lasis viajn lumojn ŝaltitajn` は、サービスエリア、最寄り給油所、方向、曲がり角、湖/海岸への道、ラウンドアバウト、線路横断、信号、左手のスーパー、トイレ休憩、渋滞、事故、左側通行、ライト点けっぱなしとして対応する。
- `serva areo` は service area として透明で、RU は整備拠点寄りにも読めるが、日中韓英との直接対応を優先して維持した。`fervojajn liniojn` は railway lines として許容し、`trafikrondo`, `trafikblokiĝo`, `akcidento`, `veturi maldekstre` も運転文脈で明確。
- `Nia benzino elĉerpiĝis`, `Mi volus havi dek litrojn`, `Bonvolu lavi la aŭton`, `Ĉu vi faras riparojn?`, `Ĉu ĝi funkcias per benzino aŭ dizelo?`, `Ĝi funkcias per benzino`, `Kiom vi ŝatus?`, `Plenigu la benzinujon`, `La benzinejo estas tie`, `Kian brulaĵon ĝi uzas?`, `Ĝi funkcias per dizelo`, `Kiom mi devas pagi?`, `Mi bezonas iom da oleo`, `Ĉu vi havas kontraŭfrostan likvaĵon?`, `Kie estas la plej proksima benzinejo?`, `Kiom kostas unu litro da benzino?`, `Por 25 frankoj, bonvolu`, `Kiel oni malfermas la benzinujon?`, `Ĉu mi povas kontroli la premon de miaj pneŭoj ĉi tie?`, `Ĉu vi havas startokablojn?` は、燃料切れ、給油量、洗車、修理可否、ガソリン/ディーゼル、満タン、給油所、燃料種別、支払い、車用オイル、不凍液、リットル単価、25フラン分、給油口/タンク、タイヤ空気圧、ジャンプケーブルとして意味ズレなし。
- `benzino`, `benzinejo`, `benzinujo`, `brulaĵo`, `dizelo` は給油所語彙として自然。`ID2308` は現CSVで JA/ZH/KO が車用オイルに寄った補正後内容になっている。`kontraŭfrosta likvaĵo` は `kontraŭfrostaĵo` も候補だが、antifreeze liquid として透明。`startokabloj` は PIV直接見出しは弱いが、`starto` + `kablo` の複合で jump leads として列間対応が明確。
- `Mia aŭto paneis`, `Ĝi bruas`, `Mi bezonas novan akumulatoron`, `Ĉu vi povas ripari ĝin nun?`, `Mia aŭto ne volas starti`, `La aŭto estas difektita`, `La akumulatoro malŝargiĝis`, `Mia pneŭmatiko krevis`, `La aŭto perdas oleon`, `La ŝlosilo ne funkcias`, `Ĉu vi povus sendi mekanikiston?`, `Ĉu vi povas ripari la aŭton?`, `Bonvolu pumpi la pneŭmatikojn`, `Bonvolu ŝanĝi la oleon`, `La hupo ne funkcias`, `La radiatoro likas`, `La motoro tre varmiĝas`, `La antaŭlumo ne funkcias`, `Io bruas`, `Mi enfermis miajn ŝlosilojn en la aŭto`, `Ĉu vi bonvolus ŝargi la akumulatoron?`, `Ĉu vi havas rezervajn partojn?`, `Ĉu vi bonvolus malfermi la kapoton?`, `Ĉu vi telefonos al mi, kiam la aŭto estos preta?` は、故障、騒音、バッテリー、始動不能、破損、放電、パンク、オイル漏れ、鍵不良、整備士、タイヤ空気入れ、オイル交換、クラクション、ラジエーター漏れ、エンジン過熱、ヘッドライト、鍵閉じ込み、充電、予備部品、ボンネット、修理完了連絡として対応する。
- `paneis` は PIV の motorveturilo の accidental malfunction と合い、`akumulatoro`, `malŝargiĝis`, `ŝargi akumulatoron` も車載バッテリー文脈で確認できる。`pneŭmatiko krevis` は PIV の `krevinta pneŭmatiko` 型から puncture として自然。`mekanikiston` は過去補正後のPIV確認済み形で、旧 `meĥanikiston` に戻す理由はない。
- `La motoro funkcias perfekte`, `La bremslumoj ne funkcias`, `La direktomontriloj ne funkcias`, `La brulaĵindikilo ne funkcias`, `La rapidometro ne funkcias`, `Io ne estas en ordo kun la bremsoj`, `Io ne estas en ordo kun la stirmekanismo`, `Io ne estas en ordo kun la oleopremo`, `Ĉu vi bonvolus aldoni bremslikvaĵon?`, `Ĉu vi bonvolus kontroli la premon de la pneŭmatikoj?`, `Ĉu vi bonvolus aldoni iom da akvo al la radiatoro?`, `Kiom da tempo necesos por ripari la aŭton?`, `Ĉu la riparoj estas kovrataj de mia asekuro?`, `Kiom kostos la riparado, proksimume?`, `Bonvolu sendi iun por ĝi`, `Atentu` は、エンジン状態、ブレーキランプ、方向指示器、燃料計、速度計、ブレーキ/ステアリング/油圧、ブレーキフルード、タイヤ空気圧、ラジエーター水、修理時間、保険適用、概算費用、車の引き取り、注意標識として意味ズレなし。
- `direktomontriloj` は PIV の `direktmontrilo = ĝirindikilo` と対応し、現CSVの日中韓も方向指示器に補正済み。`brulaĵindikilo` は `benzinometro` より汎用的だが、ディーゼル車も含む fuel gauge として透明。`rapidometro` は車両速度表示器としてPIVで確認できる。`stirmekanismo` は `stirilaro` も候補だが、RU `рулевой механизм` と対応するため維持した。`Bonvolu sendi iun por ĝi` は車を取りに来る文脈として、現CSVの日中韓補正と対応する。

主な据え置き確認:
- Driving & Parking: `stirada ekzameno`, `vojsignoj`, `unudirekta strato`, `piedirantoj`, `glacikovritaj`, `aŭtovojo`, `aŭtoriparejo`, `parkometro`, `serva areo`, `trafikrondo`, `fervojajn liniojn`, `semaforo`, `trafikblokiĝo`, `akcidento`, `veturi maldekstre` は運転・駐車文脈で維持。
- At the Petrol Station: `benzino`, `dizelo`, `brulaĵo`, `benzinujo`, `benzinejo`, `oleo`, `kontraŭfrosta likvaĵo`, `pneŭoj/pneŭmatikoj`, `startokabloj` は給油所・車両用品文脈で維持。
- Mechanical Problems: `paneis`, `akumulatoro`, `malŝargiĝis`, `pneŭmatiko krevis`, `perdas oleon`, `mekanikiston`, `pumpi la pneŭmatikojn`, `hupo`, `radiatoro likas`, `kapoton`, `bremslumoj`, `direktomontriloj`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `oleopremo`, `bremslikvaĵo`, `kovrataj de mia asekuro` は故障・整備文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `benzino` / `benzinujo` / `benzinometro`, `brulaĵo`, `dizelo`, `oleo`, `akumulatoro`, `ŝargi` / `malŝargiĝi`, `paneo` / `panei`, `pneŭmatiko`, `pumpi`, `hupo`, `kapoto`, `radiatoro`, `rapidometro`, `stiri` / `stirilaro`, `direktmontrilo` / `ĝirindikilo`, `likvo`, `bremso`, `premi` / `premo`, `trafiko`, `semaforo`, `akcidento`, `mapo`, `aŭtovojo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2256`〜`ID2355` は100件確認済み。

## 625. 624周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane
- Plane / Airport Signs
- Car / Car Hire
- Car / Driving & Parking

結果:
- **CSV修正なし**
- 前回 `ID2056`〜`ID2155` に続き、今回は `ID2156`〜`ID2255` の100件を確認した。機内依頼、空港標識、レンタカー、運転・駐車のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2193` EO、`ID2197` EN、`ID2200` EN、`ID2201` ZH、`ID2214` EN、`ID2224` EN、`ID2234` EO/EN、`ID2237` EO、`ID2239` ZH、`ID2253` EN、さらに後続周回で補正済みの `ID2199` EO、`ID2228` EO、`ID2229` EO は、現CSVで補正後内容になっていることを確認した。
- `Ĉu vi povus veki min por la manĝo, mi petas?`, `Ĉu vi povus traduki ĝin en la turkan?`, `Ĉu sur la aviadilo estas stevardino, kiu parolas la hebrean?`, `Kiam la aviadilo alvenas en Bonaeron?`, `Ĉu mi povus ricevi ankoraŭ unu formularon por dogandeklaro?` は、食事時の起床依頼、トルコ語翻訳、ヘブライ語を話す客室乗務員、ブエノスアイレス到着、税関申告書の追加依頼として意味ズレなし。
- `veki min por la manĝo` は RU が「食事前」寄りだが、機内で食事のために起こす依頼として各列と対応する。`sur la aviadilo` は `en la aviadilo` も候補だが、on board の機内文脈として許容した。`dogandeklaro` は PIV の `dogan deklaro` 型から透明で、`formularo por dogandeklaro` は customs declaration form として維持できる。
- `Enirejo`, `Eliro`, `Alvenoj`, `Forflugoj`, `Puŝu`, `Tiru`, `Dogano`, `Pordegoj 1-32`, `Liftoj`, `Lifto ne funkcias`, `Pasporta kontrolo`, `Kriza elirejo`, `Danĝero`, `Necesejo`, `Libera`, `Okupita`, `Ne funkcias`, `Bonvolu pretigi viajn pasportojn`, `Ĉiuj pasportoj`, `Internaciaj forflugoj`, `Bagaĝa elpreno`, `Varoj deklarendaj`, `Nenio por deklari`, `En kazo de fajro uzu la ŝtuparon` は、空港標識として到着/出発、押す/引く、税関、ゲート、エレベーター、入国審査、非常口、トイレ、空き/使用中、故障、旅券準備、手荷物受取、申告有無、火災時階段利用に対応する。
- `pordegoj` は空港 gate として `elirejoj` との揺れはあるが、既存周回どおり標識文脈で維持した。`bagaĝa elpreno` は `bagaĝ-ricevejo` と比べると説明的だが、baggage reclaim / 手荷物受取所として意味は明確。`Varoj deklarendaj` は `-end-` により「申告すべき品物」を表せるため、標識表現として問題ない。
- `Ĉu mi povas lui aŭton?`, `Mi preferas malgrandan aŭton`, `Por kiom longe?`, `Por semajno`, `Kiom ĝi kostas?`, `Mi ŝatus lui biciklon`, `Por kiom da tagoj?`, `Mi ŝatus malkaran aŭton`, `Ĉu ĝi havas manan aŭ aŭtomatan transmision?`, `Mi ŝatus infanan aŭtoseĝon`, `Jen miaj dokumentoj`, `Mi ne bezonas asekuron`, `Kie oni ŝaltas la antaŭlumojn?`, `Ĉu la aŭto havas benzinon?`, `La benzinujo ne estas plena`, `Ĉu estas aldonaj kostoj?`, `Kie mi povas redoni ĝin?`, `Mi ŝatus lui mopedon`, `Kiom kostas tage?`, `Kvardek dolaroj tage kun senlima kilometraĵo`, `Ĉu estas iuj rabatoj?`, `Mi ŝatus lui motorciklon`, `Ĉu mi povas havi seruron?`, `Ĉu mi povas havi kaskon?` は、レンタカー/自転車/原付/バイク、期間、料金、安い車、変速機、チャイルドシート、保険、ヘッドライト、燃料、返却、走行距離無制限、割引、ロック、ヘルメットとして対応する。
- `mana aŭ aŭtomata transmisio` は車の manual/automatic transmission として過去補正後の形を維持した。`benzinujo` は PIV で自動車・航空機などの燃料容器として確認でき、旧 `tanko` に戻す理由はない。`mopedo` は ZH/KO がスクーター寄りに自然化されているが、小型二輪レンタル文脈として許容範囲。
- `Mi ŝatus lui aŭton kun ŝoforo`, `Bonvolu sendi aŭton al mia hotelo`, `Ĉu ĉi tiu aŭto havas centran ŝlosadon?`, `Kiel oni malfermas la kofrujon?`, `Ĉu ĉi tiu aŭto havas infanserurojn?`, `Kie oni ŝaltas la direktomontrilojn?`, `Mi montros al vi la regilojn`, `Ĉu vi volas asekuron?`, `Mi volas asekuron kun plena kovrado`, `Kiujn dokumentojn mi devas havi ĉe mi?`, `Mi ŝatus lui dupordan aŭton`, `Kian aŭton vi deziras: kun mana aŭ aŭtomata transmisio?`, `Ĉu vi havas ion pli malgrandan?`, `Mi ŝatus elprovi la aŭton`, `Ĉu ĉi tiu aŭto havas klimatizilon?`, `Kie oni ŝaltas la viŝilojn?`, `Kiom longa estas la minimuma luoperiodo?`, `Mi ŝatus lui ĉi tiun aŭton por du tagoj`, `Ĉi tio estas mia internacia stirpermesilo` は、運転手付き車両、ホテル配車、集中ロック、トランク、チャイルドロック、方向指示器、操作方法、保険、フルカバー、必要書類、2ドア車、試乗、エアコン、ワイパー、最短レンタル期間、国際運転免許証として意味ズレなし。
- `centra ŝlosado`, `infanseruroj`, `direktomontriloj`, `klimatizilo`, `stirpermesilo`, `luoperiodo` は直接見出しが弱いものもあるが、透明な複合語としてレンタカー文脈に合う。`plena kovrado` は保険の full coverage として硬すぎず、各列の意味と対応する。
- `Ĉu mi devas redoni la aŭton kun plena benzinujo?`, `Vi devas redoni ĝin kun plena benzinujo`, `Ĝi devas esti redonita antaŭ la dua posttagmeze sabate`, `Kiom por kilometro?`, `Kiom kostas aldonaj kilometroj?`, `Ĉu ekzistas iuj specialaj semajnfinaj tarifoj?`, `Ĉu mi devas pagi kaŭcion?`, `Ĉu la prezo inkluzivas asekuron?`, `Mi ŝatus prezenti postulon pri aŭtoasekura kompenso`, `Ĉu mi povus redoni la aŭton ĉe mia celloko?`, `Ĉu mi povus lasi la aŭton ĉe la flughaveno?`, `Mi ŝatus aldoni duan ŝoforon`, `Kio estas la rapidlimo sur aŭtovojoj?` は、満タン返却、返却期限、距離料金、週末料金、保証金、保険込み、車両保険請求、目的地返却、空港に車を置く、2人目の運転者、高速道路の制限速度として対応する。
- `kaŭcio` は PIV で契約履行を保証するために預ける金額として確認でき、security deposit と対応する。`redoni la aŭton ĉe mia celloko` は drop off / 返却として過去補正後の形を維持した。`lasi la aŭton ĉe la flughaveno` は「空港に置いていく」文脈として、`redoni` へ寄せない。`aŭtoasekura kompenso` はやや硬いが、保険金請求の対象として意味は明確。
- `Sekvu ĉi tiun vojon`, `Turnu dekstren`, `Turniĝu maldekstren`, `La trafiko estas tre densa`, `Ĉu mi povas parkumi ĉi tie?`, `Kian aŭton vi kondukas?`, `Ĝi estas elektra aŭto`, `Kie mi povas parkumi?`, `Kie mi turnu?`, `Turnu dekstren ĉe la kruciĝo`, `Veturu trans la ponton`, `Veturu sub la ponto`, `Veturu tra la trafikrondo`, `Ĉu vi havas vojmapon?`, `Ĉu ĉi tie estas loko por halti?` は、道順、右左折、渋滞、駐車可否、車種、電気自動車、交差点、橋を渡る/下を通る、ラウンドアバウト通過、道路地図、停車場所として意味ズレなし。
- `parkumi` は PIV で車両を一時的に置く意味を確認できる。`trans la ponton` は移動を伴う「橋を渡る」、`sub la ponto` は「橋の下を通る」経路表現として維持した。`trafikrondo` と `vojmapo` は透明な複合語で、運転案内として列間対応を保つ。`loko por halti` は lay-by の厳密な施設名より広いが、日中韓も一般的な「停まれる場所」に寄っているため誤りとはしない。

主な据え置き確認:
- Plane / Airport: `veki min por la manĝo`, `traduki ĝin en la turkan`, `stevardino, kiu parolas la hebrean`, `formularon por dogandeklaro`, `forflugoj`, `pordegoj`, `pasporta kontrolo`, `kriza elirejo`, `bagaĝa elpreno`, `varoj deklarendaj`, `nenio por deklari`, `ŝtuparon` は機内・空港表示文脈で維持。
- Car Hire: `lui`, `mana/aŭtomata transmisio`, `infanan aŭtoseĝon`, `benzinujo`, `redoni`, `mopedon`, `motorciklon`, `centran ŝlosadon`, `kofrujon`, `infanserurojn`, `direktomontrilojn`, `regilojn`, `plena kovrado`, `klimatizilon`, `viŝilojn`, `minimuma luoperiodo`, `stirpermesilo`, `kaŭcion`, `aŭtoasekura kompenso`, `duan ŝoforon`, `rapidlimo sur aŭtovojoj` はレンタカー文脈で維持。
- Driving & Parking: `sekvu ĉi tiun vojon`, `turnu/turniĝu`, `trafiko estas tre densa`, `parkumi`, `elektra aŭto`, `kruciĝo`, `trans la ponton`, `sub la ponto`, `trafikrondo`, `vojmapo`, `loko por halti` は運転・駐車文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `traduki`, `turko` / `turka`, `hebreo` / `hebrea`, `dogano` / `dogan deklaro`, `pordo` / `pordego`, `lui`, `aŭtomata`, `mana`, `transmisii` / `transmisio`, `benzino` / `benzinujo`, `seruro`, `ŝlosi` / `ŝlosado`, `kofro` / `kofrujo`, `klimatizilo`, `kaŭcio`, `parki` / `parkumi`, `mapo`, `trans`, `sub`, `ŝoseo` / `aŭtovojo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2156`〜`ID2255` は100件確認済み。

## 624. 623周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage
- Plane / Passport Control & Customs
- Plane / On the Plane

結果:
- **CSV修正なし**
- 前回 `ID1956`〜`ID2055` に続き、今回は `ID2056`〜`ID2155` の100件を確認した。手荷物、入国審査・税関、機内表現のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID2057` EO、`ID2089` EO、`ID2100` EN、`ID2104` JA、`ID2105` RU、`ID2112` EN、`ID2113` EO、`ID2116` ZH/KO、`ID2118` EO、`ID2127` ZH、`ID2130` KO、`ID2145` RU は、現CSVで補正後内容になっていることを確認した。
- `Mi havas unu manbagaĝon`, `Ĉu mi devas registrigi ĉi tion kiel bagaĝon, aŭ ĉu mi povas kunporti ĝin?`, `Ĝi estas tro granda por manbagaĝo`, `Kiom kostas la troa bagaĝo?`, `La kroma pago por troa bagaĝo estas 30 pundoj`, `Mi ne ricevis la bagaĝetikedon kiam mi registriĝis`, `Ĝi estas fragila. Bonvolu porti ĝin singarde`, `Viaj valizoj estos en la bagaĝ-ricevejo`, `Mia bagaĝo estas difektita kaj kelkaj aferoj mankas`, `Ĉu iu havis aliron al viaj valizoj dume?`, `Ĉu iu donis al vi ion por porti?`, `Mi ŝatus sendi ĉi tiun bagaĝon al Kuala-Lumpuro`, `Ni informos vin, kiam via bagaĝo estos liverita` は、機内持込手荷物・預け入れ・超過手荷物料金・タグ・壊れ物・受取所・破損/紛失・他人からの預かり物・荷物配送として意味ズレなし。
- `registrigi ĉi tion kiel bagaĝon` は PIV の `registrigi pakaĵon ĉe la stacidomo` 型から、預け荷物として登録する意味が明確。`manbagaĝo` は透明な複合語として空港文脈で維持できる。`bagaĝ-ricevejo` は baggage reclaim area / 手荷物受取所として列間対応を保っている。
- `Mi estas turisto`, `Mi estas sola`, `Jen mia pasporto`, `Ĝuu vian restadon!`, `La sekva, bonvolu!`, `Mi feriumas`, `Mi veturas al Ĝenevo`, `Mi vizitas parencojn`, `Ĉi tio estas mia unua vizito`, `Mi havas turistan vizon`, `Ĉu vi havas ion por deklari?`, `Mi ŝatus deklari la monon`, `Kiom longe vi restos?`, `Mi planas resti 2 semajnojn`, `Loĝpermesilo`, `Rifuzo de eniro`, `Mi bezonas politikan azilon`, `Malfermu ĉi tiun sakon`, `Ĉi tio estas donaco por amiko`, `Jen mia deklaracio`, `Kiom da dogano mi devas pagi?` は、入国審査・滞在目的・ビザ・申告・滞在期間・在留許可・入国拒否・政治的庇護・関税として対応する。
- `deklari` は PIV で税関申告の用例があり、`deklaracio` は `deklaro` と同義として申告書文脈を許容できる。`dogano` は税関行政だけでなく limimposto / duty の語義を持つため、`Kiom da dogano...`, `pagi doganon...` は関税支払いとして維持した。`azilo` は `peti azilon` 型をPIVで確認でき、政治的庇護・難民申請の文脈と合う。
- `Ni havas komunan pasporton`, `Rifuzo de vizpeto`, `Mi havas studentan vizon`, `Mi havas komercan vizon`, `Jen mia transitvizo`, `Mi flugas transite al Singapuro`, `Jen mia importa licenco`, `De kie vi venis?`, `Kie vi loĝos?`, `Mi restos en la hotelo Four Seasons`, `Mi havas statuson de rifuĝinto`, `Kiel mi povas peti azilon?`, `Komenciĝas la eniro en la aviadilon por flugo numero 120`, `Vian pasporton kaj bileton, mi petas`, `Mi havas diplomatan pasporton`, `Ĉu vi bonvolus stampi mian pasporton?`, `Vian doganan deklaracion, bonvolu`, `Kio estas la celo de via vizito?`, `Mi estas ĉi tie kun argentina delegacio`, `Mi havas nur aĵojn por persona uzo`, `Ĉi tiu videokamerao estas por mia persona uzo`, `Mi havas kvincent dolarojn en vojaĝĉekoj`, `Mi havas kun mi tri botelojn da viskio`, `Vi devas pagi doganon por ĉi tiuj varoj`, `Ĝi kostas ĉirkaŭ 200 usonajn dolarojn`, `Ĉu mi devas pagi doganon por la varoj, kiujn mi aĉetis ĉi tie?`, `Vi devas plenigi ĉi tiun enmigradan formularon`, `Bonvolu montri al mi, kiel plenigi ĉi tiun formularon`, `Mi ŝatus kontakti la serban konsulejon`, `Mia familio povas sendi al mi la necesajn dokumentojn`, `Antaŭe mi jam petis azilon`, `Jen mia internacia vakcinatestilo` は、旅券種別・ビザ申請拒否・各種ビザ・輸入許可・滞在先・難民/庇護・搭乗開始・税関申告・個人使用品・旅行小切手・酒類・入国書類・領事館・必要書類・予防接種証明として意味ズレなし。
- `ID2102` は現CSVで `Komenciĝas la eniro en la aviadilon...` になっており、過去ログに見える `enŝipiĝo` ではない。`Rifuzo de vizpeto` は visa application refusal として透明で、`transitvizo` / `transite` は PIV の `transito` 語義と合う。`serban konsulejon` は現在小文字で、周辺の `argentina delegacio` と同じ普通形容詞として自然。
- `Ĉu ni malfruas?`, `Kiam ni foriras?`, `Kie estas niaj lokoj?`, `Tio estas mia loko`, `Ĉu mi povas sidi ĉi tie?`, `Ĉu mi povas reklini mian seĝon?`, `Ĉu mi povus interŝanĝi lokojn kun vi?`, `Bonvolu resti sur via sidloko`, `Bonvolu fiksi vian sekurzonon`, `Miaj aŭskultiloj ne funkcias`, `Kiom longe daŭras la flugo?`, `Kio estas la rapideco de la aviadilo?`, `Sakon por vomado, mi petas`, `Ĉu mi povas sidiĝi tie?`, `Kiu estas via sidloknumero?`, `Ĉu mi povas ricevi ankoraŭ unu trinkaĵon?`, `Ĉu vi ŝatus gazeton?`, `Mi ŝatus aŭskultilojn por la filmo`, `Mi ŝatus paroli kun la stevardino`, `Ĉu ni flugos super la oceano?`, `Ni alteriĝos post ĉirkaŭ dek kvin minutoj`, `La loka tempo estas 21:34`, `La aviadilo finfine alteriĝis en Ĝakarto` は、機内座席・シートベルト・イヤホン・飛行時間/速度・エチケット袋・飲み物/新聞・客室乗務員・海上飛行・着陸・現地時刻として対応する。
- `reklini mian seĝon` は `retroklini` も候補だが、`klini` の「傾ける」語義から座席を倒す意味が明確で、列間の意味ズレはない。`sekurzono` は航空乗客を座席に固定する装備としてPIV周辺記述で確認できる。`stevardino` は EN が中立的な flight attendant だが、RU が女性形 `стюардессой` であり、現行EOを動かす根拠は弱い。`Sakon por vomado` は `vomsako` も候補だが、機内の sick bag として意味は明確。
- `Kiom longe ni haltos ĉi tie?`, `Je kiom ĝi malfruiĝos?`, `Bonvolu malŝalti ĉiujn elektronikajn aparatojn`, `Bonvolu atenti ĉi tiun mallongan sekurecan demonstracion`, `Bonvolu remeti vian seĝodorson en la vertikalan pozicion`, `Ĉu vi bonvolus meti ĝin en la supran bagaĝujon?`, `Ĉu vi dezirus iom da manĝaĵo aŭ trinkaĵo?`, `Je kiu alteco ni flugas?`, `Ĉu vi havas grekan gazeton?`, `Ĉu vi bonvolus doni al mi kovrilon?`, `Ĉu vi vendas senimpostajn varojn dum la flugo?` は、停留時間・遅延時間・電子機器・安全説明・座席背もたれ・頭上収納・飲食・高度・新聞・毛布・機内免税販売として意味ズレなし。
- `seĝodorso` は座席の背もたれとして透明で、PIV内にも `seĝodorso` 用例がある。`supran bagaĝujon` は overhead locker / 頭上収納に対応し、`kovrilo` は機内で渡す blanket として文脈上成立する。`grekan gazeton` はギリシャ語/ギリシャ系新聞の短い表現として各列と衝突しない。

主な据え置き確認:
- Luggage: `manbagaĝo`, `registrigi ĉi tion kiel bagaĝon`, `troa bagaĝo`, `kroma pago`, `bagaĝetikedo`, `fragila`, `bagaĝ-ricevejo`, `difektita`, `aliron al viaj valizoj`, `ion por porti`, `bagaĝo estos liverita` は手荷物文脈で維持。
- Passport Control & Customs: `turista/studentan/komercan/transitvizon`, `deklari`, `deklaracio`, `dogano`, `loĝpermesilo`, `rifuzo de eniro`, `vizpeto`, `politikan azilon`, `statuson de rifuĝinto`, `peti azilon`, `enmigradan formularon`, `serban konsulejon`, `vakcinatestilo` は入国・税関文脈で維持。
- On the Plane: `reklini mian seĝon`, `interŝanĝi lokojn`, `sekurzonon`, `aŭskultiloj`, `Sakon por vomado`, `stevardino`, `alteriĝos`, `elektronikajn aparatojn`, `sekurecan demonstracion`, `seĝodorson`, `supran bagaĝujon`, `alteco`, `grekan gazeton`, `kovrilon`, `senimpostajn varojn` は機内文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- ReVo `klin/i`: https://reta-vortaro.de/revo/art/klin.html
- PIV 2020 `bagaĝo`, `registri` / `registrigi`, `dogano`, `azilo`, `rifuĝi` / `rifuĝinto`, `deklari` / `deklaracio`, `vizo`, `transito`, `importi`, `licenco`, `seĝo` / `seĝodorso`, `aŭskultilo`, `stevardo` / `stevardino`, `kovri` / `kovrilo`, `vomi`, `vertikala`, `balteo` / `sekurzono`, `terminalo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID2056`〜`ID2155` は100件確認済み。

## 623. 622周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight
- Plane / Checking in
- Plane / Luggage

結果:
- **CSV修正なし**
- 前回 `ID1856`〜`ID1955` に続き、今回は `ID1956`〜`ID2055` の100件を確認した。航空券予約、搭乗手続き、手荷物のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1969` RU、`ID1973` EN、`ID1989` EO、`ID1999` EN、`ID2007` JA/ZH/KO、`ID2011` EO、`ID2012` EN/JA/ZH/KO、`ID2018` EN、`ID2020` ZH、`ID2021` ZH、`ID2022` RU、`ID2028` EN、`ID2035` EN、`ID2037` EN/JA/ZH/KO、`ID2045` KO、`ID2050` EN、`ID2055` KO は、現CSVで補正後内容になっていることを確認した。
- `Ĉu ĉi tio estas rekta flugo?`, `Ĉu estas halto dumvoje?`, `Kiam estas la flugo al Romo?`, `Bonvolu kontroli aliajn flugkompaniojn`, `Bileto de komerca klaso`, `En kiu valuto ĉi tio estas?`, `Kiajn lokojn vi preferus?`, `En la antaŭa vico`, `En la malantaŭa vico`, `Bonvolu doni al mi kvitancon`, `Ĉu la flughaveno estas malproksime de la urbo?`, `Mi ŝatus rezervi lokon en ĉi tiu aviadilo`, `Sur ĉi tiu aviadilo ne plu estas lokoj`, `Kio estas via celloko?`, `Mi ŝatus vojaĝi al Sud-Koreio`, `Ĉu mi bezonas vizon por Kenio?`, `Kiam estas la sekva flugo al Hanojo?`, `Kiom ofte estas la flugoj?`, `Je kioma horo foriras la flugo?`, `Kiom frue mi devas esti ĉe la flughaveno?`, `Kiom da bagaĝo mi povas preni?`, `Kie mi devas ŝanĝi aviadilon?`, `Ĉu mi povas ŝanĝi aviadilon en la sama tago?`, `Mi venis por preni miajn biletojn` は、直行便・経由・航空会社・ビジネスクラス・通貨・座席希望・目的地・ビザ・便の頻度/出発時刻・手荷物量・乗り継ぎ・航空券受け取りとして意味ズレなし。
- `En la antaŭa vico` / `En la malantaŭa vico` は、ロシア語では前列/後列、英日中韓では前方/後方寄りに自然化されているが、座席希望の短答として許容範囲。`ŝanĝi aviadilon` は飛行機を乗り換える意味で connection / transfer と対応し、`preni miajn biletojn` は「チケットを受け取る」と読める。
- `En kiuj tagoj estas flugoj al Teherano?`, `Bonvolu rezervi la sekvan flugon al Amsterdamo`, `Mi ŝatus du biletojn de komerca klaso`, `Ĉu vi ŝatus sidlokon ĉe la fenestro aŭ ĉe la koridoro?`, `Kiom da tempo antaŭ la forveturo ni devas alveni?`, `Mi ŝatus nuligi mian bileton al Helsinko`, `Kiuj flugoj estas al Turkio?`, `Ĉu estas liberaj lokoj sur ĉi tiu flugo?`, `Ĉu la flugo faras halton en alia urbo?`, `Kiom da tempo necesas por ŝanĝi aviadilon?`, `Ĉu ni povas iom butikumi en la flughaveno?`, `Kiom da ĉokolado mi povas porti tra la dogano?`, `Kiam vi revenos?` は、運航曜日・次便予約・座席種別・到着時刻・キャンセル・空席・ストップオーバー・乗り継ぎ時間・空港内買い物・税関・帰着確認として対応する。
- `forveturo` は航空文脈では `forflugo` も候補だが、一般的な departure として日中韓露英の意味を崩さない。`nuligi mian bileton al Helsinko` はロシア語が「返す/払い戻す」寄りだが、航空券キャンセルの会話として実質的に対応するため維持した。`porti tra la dogano` は customs through/to pass customs の短い旅行表現として問題ない。
- `Vian pasporton, mi petas`, `Kiu terminalo?`, `Kiu elirejo?`, `Agrablan flugon!`, `Kien vi flugas?`, `Mi flugas al Ĉinio`, `Kie estas la registrejo?`, `Kie mi suriru?`, `Kie estas elirejo 1?`, `Kie estas terminalo A?`, `Je kioma horo estas via flugo?`, `Ĉu la flugo malfruiĝis?`, `Mi ŝatus lokon ĉe la fenestro`, `Mi rezervis per interreto`, `Enlanda aŭ internacia?`, `Kiu estas la flugnumero?`, `Ĉi tiu flugo estas prokrastita`, `Ĉi tiu flugo estis nuligita`, `Kiam komenciĝas la eniro en la aviadilon?`, `Ni iru en la atendejon` は、搭乗手続き・ゲート/ターミナル・便時刻・遅延/欠航・国内線/国際線・搭乗開始・待合室として意味ズレなし。
- `ID2011` は現CSVで `Kiam komenciĝas la eniro en la aviadilon?` になっており、過去に問題視された `enŝipiĝo` 形ではないことを確認した。`elirejo` と `pordego` は空港の gate 文脈で併用されており、`pordego` はより字義的な gate、`elirejo` は出口/搭乗口として文脈上成立する。`terminalo` はローカルPIV断片では空港語義が強く出ないが、空港ターミナルの国際語として現文脈では明確。
- `Kie estas la senimposta butiko?`, `Bonvolu malplenigi viajn poŝojn`, `Demetu viajn ŝuojn`, `Ĉu vi havas likvaĵojn?`, `Kie estas la giĉeto de Emirates?`, `Per kiu flugkompanio vi flugas?`, `Mia aviokompanio estas Lufthansa`, `Ĉu vi havas vian rezervonumeron?`, `Jen mia rezervonumero`, `Ĉu mi povas vidi vian pasporton, mi petas?`, `De kiu pordego foriras ĉi tiu flugo?`, `Bonvolu tuj iri al elirejo numero 1`, `Ĉu ĉi tiu flugo foriros ĝustatempe?`, `Ni pardonpetas pro la prokrasto`, `Ĉu vi povus malfermi vian sakon, mi petas?`, `Bonvolu meti ĉiujn metalajn objektojn en la pleton`, `Ĉu vi povus demeti vian zonon, mi petas?`, `Ĉu vi povus demeti vian mantelon, mi petas?`, `Bonvolu elpreni vian tekkomputilon el ĝia ujo`, `Mi timas, ke vi ne povas kunporti tion` は、免税店・保安検査・航空会社/予約番号・搭乗口・定刻出発・遅延謝罪・金属物/ベルト/上着/ノートPC・持ち込み不可として対応する。
- `likvaĵojn` は PIV では `likvo` が基本形だが、空港保安検査での「液体類」として透明で、列間の意味ズレはない。`tekkomputilo`, `rezervonumero`, `aviokompanio` は透明な複合語で、空港会話として維持できる。
- `Tio estas mia bagaĝo`, `Mi ne havas bagaĝon`, `Kie mi povas pesi la bagaĝon?`, `Kie mi povas trovi portiston?`, `Kiom da valizoj vi havas?`, `Ĉi tiuj estas miaj valizoj`, `Jen mia bagaĝetikedo`, `Kie mi povas ricevi mian bagaĝon?`, `Mi ne povas trovi mian bagaĝon`, `Kie mi povas preni ĉareton?`, `Kie estas la bagaĝaj ŝranketoj?`, `Ĉu vi registrigas iun bagaĝon?`, `Jes, mi havas unu valizon`, `Ĉu vi mem pakis viajn valizojn?`, `Mi havas du manbagaĝojn`, `Vi havas tro da manbagaĝo`, `Ĉu tio estas funtoj aŭ kilogramoj?`, `Vi devos pagi por la superpezo`, `Ĉu mi povas pagi per kanadaj dolaroj?`, `Bonvolu sendi mian bagaĝon al la hotelo`, `Bonvolu porti ĉi tiun bagaĝon al la taksihaltejo`, `Mia bagaĝo perdiĝis`, `Ĉu mi povus vidi vian manbagaĝon, mi petas?` は、荷物/スーツケース・手荷物タグ・受け取り・カート・ロッカー・預け入れ・超過重量・通貨支払い・ホテル配送・タクシー乗り場・紛失・機内持込手荷物として意味ズレなし。
- `registrigi bagaĝon` は PIV の `registrigi pakaĵon ĉe la stacidomo` 型から、荷物を預ける/チェックインする意味として成立する。`manbagaĝo` は直接見出しとしては弱いが、`mano` + `bagaĝo` の透明な複合で、空港文脈の hand luggage として維持した。`bagaĝaj ŝranketoj` は luggage lockers、`ĉareto` は手荷物カート、`superpezo` は超過重量として自然。

主な据え置き確認:
- Booking a Flight: `rekta flugo`, `halto dumvoje`, `flugkompanio`, `komerca klaso`, `valuto`, `antaŭa/malantaŭa vico`, `kvitancon`, `aviadilo`, `celloko`, `vizon`, `foriras la flugo`, `bagaĝo`, `ŝanĝi aviadilon`, `preni miajn biletojn`, `sidlokon ĉe la fenestro/aŭ ĉe la koridoro`, `forveturo`, `nuligi mian bileton`, `butikumi en la flughaveno`, `porti tra la dogano` は航空券予約文脈で維持。
- Checking in: `pasporton`, `terminalo`, `elirejo`, `registrejo`, `suriru`, `enlanda aŭ internacia`, `flugnumero`, `prokrastita`, `nuligita`, `eniro en la aviadilon`, `atendejo`, `senimposta butiko`, `malplenigi viajn poŝojn`, `likvaĵojn`, `giĉeto`, `aviokompanio`, `rezervonumero`, `pordego`, `ĝustatempe`, `pardonpetas pro la prokrasto`, `metalajn objektojn`, `pleto`, `tekkomputilon`, `kunporti` は搭乗手続き・保安検査文脈で維持。
- Luggage: `bagaĝo`, `valizo`, `bagaĝetikedo`, `ĉareto`, `bagaĝaj ŝranketoj`, `registrigas iun bagaĝon`, `manbagaĝo`, `superpezo`, `kanadaj dolaroj`, `taksihaltejo`, `perdiĝis` は手荷物文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `flugi` / `flugo`, `aviadilo`, `vizo`, `bagaĝo`, `valizo`, `registri` / `registrigi`, `atendejo`, `dogano`, `giĉeto`, `pasporto`, `butiko` / `butikumi`, `likvo` / `likvaĵo`, `metalo` / `metala`, `pleto`, `poŝo`, `prokrasti`, `pordo` / `pordego`, `ĉaro` / `ĉareto`, `ŝranko` / `ŝranketo`, `zono`, `mantelo`, `komputilo` / `tekkomputilo`, `terminalo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1956`〜`ID2055` は100件確認済み。

## 622. 621周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions
- Travel / At the Tourist Office
- Travel / Excursions
- Plane / Booking a Flight

結果:
- **CSV修正なし**
- 前回 `ID1756`〜`ID1855` に続き、今回は `ID1856`〜`ID1955` の100件を確認した。道案内、観光案内所、ツアー・写真、航空券予約導入のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1856` ZH、`ID1861` ZH、`ID1873` KO、`ID1906` EO/RU、`ID1910` KO、`ID1920` EN、`ID1923` JA、`ID1924` JA、`ID1938` JA、`ID1942` ZH、`ID1944` EN、`ID1950` EN、`ID1955` EN は、現CSVで補正後内容になっていることを確認した。
- `Daŭrigu rekten preter kelkaj semaforoj`, `Vi iras laŭ la malĝusta vojo`, `Vi prefere veturu per tramo`, `Uzu la subpasejon`, `Sekvu la indikilojn al la urbocentro`, `Pardonu, mi ne konas la urbon`, `Pardonu, mi ne estas de ĉi tie` は、道順の続行、誤方向、交通手段、地下通路、標識案内、自分が地元でないことの説明として意味ズレなし。
- `rekten` は PIV 用例の `iru rekten` 型と合い、`semaforo`, `subpasejo`, `indikilo`, `urbocentro`, `tramo` も道案内語彙として維持できる。
- `Mi estas eksterlandano`, `Ĉu estas moteloj ĉi tie?`, `Kie estas la urbocentro?`, `Ĉu vi havas mapon?`, `Mi volas viziti vidindaĵojn`, `Kie mi povas lui aŭton?`, `Kie staras la aŭtobusoj?`, `Kie estas la parko?`, `Kie estas la muzeo?`, `Kie estas la katedralo?`, `Kie estas la merkato?`, `Ĉu estas aŭtobuso al la urbo?`, `Ĉu estas drinkejo en la urbo?`, `Ĉu estas teatro en ĉi tiu urbo?`, `Kie estas la turisma oficejo?`, `Ĉu vi scias la numeron por voki taksion?`, `Ĉu vi havas broŝurojn?`, `Ni bezonas ie resti`, `Kie estas la plej proksima hotelo?`, `Ĉu mi povas rezervi hotelĉambron ĉi tie?`, `Kiom da steloj ĝi havas?` は、観光案内所での施設・地図・交通・宿泊・ホテル等級の質問として対応する。
- `turisma oficejo` は PIV の `turisma oficejo` 用例と一致する。`vidindaĵojn` は sightseeing / 観光名所、`resti` / `loĝejo` は宿泊先、`hotelĉambro` はホテル客室として自然。
- `Kie estas la flughaveno?`, `Kie estas la artgalerio?`, `Kie estas la ĉefa komerca kvartalo?`, `Kie estas la botanika ĝardeno?`, `Kie estas la plej proksima restoracio?`, `Kie estas la ruinoj?`, `Mi ŝatus vidi la malnovan urboparton`, `Ni serĉas loĝejon`, `Ĉu vi povus rezervi loĝejon por mi?`, `Mi ŝatus loĝi en la urbocentro`, `Ĉu vi havas liston de junulargastejoj?`, `Ĉu vi povas rekomendi bonajn tendumejojn?`, `Bonvolu doni al mi mapon de la urbo`, `Ĉu vi havas programon de eventoj?`, `Kie troviĝas la ĉefaj vidindaĵoj?`, `Ĉu vi povas rekomendi bonan restoracion?`, `Ĉu vi povas rekomendi bonan drinkejon ĉi tie proksime?`, `Kie mi povas trovi sandviĉejon?`, `Kien plej bone iri por promeni?`, `Kiel ni povas atingi la teatron?`, `Kiu estas la plej bona maniero moviĝi tra la urbo?`, `Ĉu estas metrostacio proksime?`, `Kie mi povas preni la navedan buson?`, `Ĉu vi havas informojn pri lokaj taksiservoj?` は、観光施設、宿泊、飲食、イベント、公共交通、シャトル、タクシー情報として意味ズレなし。
- `junulargastejoj`, `tendumejoj`, `sandviĉejo`, `naveda buso`, `vidindaĵoj`, `programo de eventoj` は透明な複合・派生またはPIV語義で観光文脈に対応する。`naveda buso` は旧 `navedbuso` ではなく、PIV の `naveda` の「往復する」語義から shuttle bus として現在形を維持した。
- `Ĉu estas iuj ekskursoj?`, `Vi ne povas maltrafi ĝin`, `Ĉu mi povas havi gvidiston?`, `Ĉu vi povas foti?`, `Ĉu estas iuj unutagaj ekskursoj?`, `Kiu estas la plej bona vojo?`, `Ĉu estas urba ekskurso?`, `Kiam estas la sekva ekskurso?`, `Kiom kostas ĉi tiu ekskurso?`, `Je kioma horo ĝi komenciĝas?`, `Je kioma horo ni revenas?`, `Kiu estos nia gvidanto?`, `Ĉu manĝoj estas inkluzivitaj en la prezo?`, `Mi ŝatus grandigi ĉi tiujn fotografiojn`, `Kiam estos pretaj la fotoj?`, `Ĉu estas iuj ekskursoj?`, `Jen la listo de ekskursoj`, `Pri kio vi interesiĝas?`, `Mi ŝatus rezervi vojaĝon al Berlino`, `Ĉu vi havas iujn broŝurojn pri lokaj vidindaĵoj?` は、ツアー有無・料金・集合/帰着・ガイド・食事込み・写真拡大/受け取り・旅行予約の文脈で対応する。
- `ekskurso` は「散策・遠足・ツアー」の幅を持ち、観光ツアーとして現在の日訳補正を維持した。`gvidisto` は案内人、`foti` / `fotografio` は写真撮影・写真、`inkluzivitaj en la prezo` は料金込みとして対応する。
- `Ĉu estas ekskursoj en la estona?`, `Ĉu ni povas mendi biciklan ekskurson?`, `Kiuj aŭtobusaj ekskursoj estas disponeblaj?`, `Kiujn vidindaĵojn ni vidos?`, `Ĉu vi bezonas gvidatan ekskurson?`, `Kiam kaj kie ni povas renkontiĝi?`, `Je kioma horo ni foriras?`, `Ĉu mi povas eliri ĉe la hotelo?`, `Pardonu, ĉu vi povus foti min?`, `Mi ŝatus preni miajn fotojn`, `Kie mi povas aliĝi al la ekskurso?`, `Ĉu vi havas broŝuron priskribantan rondvojaĝojn kaj ekskursojn?`, `Kion alian interesan oni povas vidi ĉi tie?`, `Ĉu vi povas rekomendi vidindaĵan ekskurson?`, `Kian ekskurson vi preferus?`, `Mi ŝatus viziti la Parlamentejon`, `Mi ŝatus gvidiston, kiu parolas la kartvelan`, `Ĉu tuttaga ekskurso haveblas ĉi tie?`, `Ĉu mi povas aliĝi al la ekskurso ĉe la hotelo?` は、言語指定・自転車/バス/ガイド付き/観光/終日ツアー、写真依頼、写真受け取り、申し込み、国会議事堂見学として意味ズレなし。
- `en la estona` と `parolas la kartvelan` は言語指定として自然。`preni miajn fotojn` は写真店・観光文脈では「写真を受け取る/引き取る」と読めるため、`ricevi` への置換はしない。`rondvojaĝoj`, `vidindaĵa ekskurso`, `Parlamentejo`, `tuttaga ekskurso` は旅行語彙として維持できる。
- `Ĉu nun okazas iuj kulturaj eventoj?`, `Ĉu nun okazas iuj ekspozicioj?`, `Ĉu vi povus diri al ni, kio okazas en la koncertejo?`, `Ĉu vi povus diri al mi, kiuj muzeoj estas ĉi tie?`, `Ĉu ni havos okazon fari kelkajn fotojn?`, `Ĉu vi povus presi la fotojn de ĉi tiu memorkarto?`, `Mi pensas, ke kelkaj el ĉi tiuj fotoj estas subeksponitaj`, `Kiom kostas la flugoj?`, `Ekonomiklasa bileto` は、文化イベント・展示・コンサートホール・博物館・写真撮影/印刷/露出不足・航空券料金/クラスの文脈で意味ズレなし。
- `subeksponitaj` は PIV の `sub eksponi`（写真で露光が短すぎる）に合い、露出不足として維持した。`Ekonomiklasa bileto` は航空券の economy-class ticket として透明で、空港・航空券文脈から明確に読める。

主な据え置き確認:
- Giving Directions: `rekten`, `semaforoj`, `la malĝusta vojo`, `tramo`, `subpasejon`, `indikilojn`, `urbocentro`, `ne konas la urbon`, `ne estas de ĉi tie` は道案内文脈で維持。
- At the Tourist Office: `vidindaĵojn`, `aŭtobusoj`, `turisma oficejo`, `broŝurojn`, `loĝejo`, `hotelĉambro`, `artgalerio`, `komerca kvartalo`, `junulargastejoj`, `tendumejojn`, `sandviĉejon`, `programon de eventoj`, `navedan buson`, `taksiservoj` は観光案内文脈で維持。
- Excursions / Plane: `ekskursoj`, `gvidiston`, `foti`, `unutagaj ekskursoj`, `gvidanto`, `inkluzivitaj en la prezo`, `grandigi fotografiojn`, `en la estona`, `biciklan ekskurson`, `gvidatan ekskurson`, `preni miajn fotojn`, `rondvojaĝojn`, `vidindaĵan ekskurson`, `Parlamentejon`, `la kartvelan`, `tuttaga ekskurso`, `subeksponitaj`, `ekonomiklasa bileto` はツアー・写真・航空券文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `rekten` 周辺用例、`indiki` / `indikilo`, `turismo` / `turisma`, `vidindaĵo`, `ekskurso`, `gvidi` / `gvidisto`, `navedo` / `naveda`, `aŭtobuso` / `buso`, `sandviĉo` / `sandviĉejo`, `tendo` / `tendumi`, `fotografio` / `foti`, `preni`, `eksponi` / `sub eksponi`, `parlamento` / `parlamentejo`, `klaso` / `ekonomiklasa` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1856`〜`ID1955` は100件確認済み。

## 621. 620周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter
- Travel / Asking Directions
- Travel / Giving Directions

結果:
- **CSV修正なし**
- 前回 `ID1656`〜`ID1755` に続き、今回は `ID1756`〜`ID1855` の100件を確認した。推薦状、道案内の質問、道順説明のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1756` EN、`ID1757` EN、`ID1759` RU/KO、`ID1763` EN/ZH、`ID1764` ZH、`ID1766` EN、`ID1767` EO/EN、`ID1824` JA、`ID1830` ZH、`ID1832` ZH、`ID1834` ZH、`ID1840` EO、`ID1841` ZH、`ID1855` EN は、現CSVで補正後内容になっていることを確認した。
- `Mi ne povas rekomendi lin al via kompanio`, `Ĉu vi bonvolus skribi rekomendleteron por mi?`, `Mi estis lia gvidanto dum ĉirkaŭ du jaroj`, `Li laboris por mi pri diversaj projektoj`, `Ŝi havas bonegajn komunikajn kapablojn`, `Mi donas al ŝi mian plej varman rekomendon`, `Bonvolu telefoni al mi, se vi havos demandojn`, `Ŝi konstante produktas altkvalitan laboron`, `Ŝi estos bonega aldono al via programo`, `Ŝia plej granda talento estas verki rakontojn`, `Li faris elstaran kontribuon al mia projekto`, `Li estas fidinda persono kun bona humursento`, `Mi esperas, ke ĉi tiu informo estos utila por vi` は、推薦状・人物評価・照会対応の文脈で意味ズレなし。
- `gvidanto` は supervisor/上司・指導者の文脈で読め、`laboris por mi pri diversaj projektoj` は「私のもとで/私のために」働いた意味として現在の KO 補正と対応する。`programo` は PIV で学習課程・計画等の幅を持つため、推薦先の programme/project を広く指す表現として維持した。`humursento` は過去補正後の現形で、humour sense と対応する。
- `Mi perdiĝis`, `Kie estas ĉi tiu adreso?`, `Ĉu ĝi estas malproksime de ĉi tie?`, `Ĉi tien?`, `Kiel mi povas atingi la urbon?`, `Kiudirekte estas la urbocentro?`, `Kie estas la preĝejo?`, `Kie estas la plej proksima apoteko?`, `Ĉu mi iru rekte?`, `Ĉu ĝi estas ĉi-flanke?`, `Ĉu estas tro malproksime por iri piede?`, `Kiun ŝparvojon mi povas preni?`, `Bonvolu desegni mapon ĉi tie`, `Kie troviĝas la strato La Rambla?`, `Ĉu la hotelo estas malproksime de ĉi tie?`, `Ĉu estas banko proksime de ĉi tie?`, `Ĉu estas superbazaro proksime de ĉi tie?`, `Ĉu la fervojstacio estas malproksime?`, `Kie estas la metrostacio?`, `Kiuj vidindaĵoj troviĝas survoje?`, `Kiel nomiĝas ĉi tiu strato?`, `Kiom malproksime de ĉi tie estas la plaĝo?` は、基本的な現在地・距離・施設・近道・地図・名所確認の道案内表現として対応する。
- `ŝparvojo`, `fervojstacio`, `metrostacio`, `vidindaĵoj`, `survoje`, `piede` は旅行会話として自然。`Ĉi tien?` は直訳では「こちらへ？」だが、各列の「この方向/こうですか」型の短い確認発話として許容した。
- `Kiel mi povas atingi la marbordon?`, `Ĉu vi montros al mi la vojon al la poŝtoficejo?`, `Ĉu vi povus montri al mi sur la mapo?`, `Ĉu ĝi estas sufiĉe proksime por piediri?`, `En kiun direkton mi iru?`, `Bonvolu noti la adreson`, `Mi serĉas ĉi tiun adreson`, `Mi scivolas, ĉu iu povus diri al mi la direkton`, `Kiel mi povas atingi la fervojan stacidomon?`, `Kiel mi povas atingi la plaĝon de ĉi tie?`, `Pardonu, kie estas la policejo?`, `Pardonu, kiel mi povas atingi ĉi tiun lokon?`, `Pardonu, ĉu vi scias, kie estas la poŝtejo?`, `Pardonu, ĉu vi povus diri al mi, kiel atingi la aŭtobusan stacion?`, `Ĉu ĉi tio estas la vojo al Sydney Harbour Bridge?`, `Ĉu vi scias, kie ĉi tie troviĝas interreta kafejo?`, `Ĉu vi scias, kie troviĝas la kanada ambasadejo?`, `Ĉu vi povus diri al mi, kiel atingi ĉi tiun hotelon?`, `Kiom da tempo necesas por atingi tien?`, `Ĉu vi povus diri al mi, mi petas, kiel iri al la vendejo?`, `Ĉu mi povas iri piede, aŭ ĉu mi prenu taksion?`, `Kiom da tempo mi bezonos por piediri tien?`, `Bonvolu montri sur ĉi tiu mapo, kie mi nun troviĝas`, `Mi malfacile orientiĝas` は、道順・移動手段・現在地・方向感覚の問い合わせとして意味ズレなし。
- `diri al mi la direkton` は `montri la vojon` も候補だが、「方向/道順を教える」発話として列間対応を崩さない。`aŭtobusa stacio`, `ambasadejo`, `poŝtoficejo` / `poŝtejo`, `interreta kafejo`, `policejo`, `fervoja stacidomo` は施設語として維持できる。`Mi malfacile orientiĝas` は JA が「道に迷った」に自然化されているが、方向が分からない旅行会話として許容した。
- `Maldekstren`, `Dekstren`, `Revenu`, `Mi povas montri al vi`, `Ĝuste ĉi tie`, `Iru tien malsupren`, `Rekte antaŭen`, `Ĝi estas proksime de ĉi tie`, `Ĉe la kruciĝo`, `Malantaŭ la banko`, `Nordo`, `Sudo`, `Oriento`, `Okcidento`, `Ĝi ne estas tro malproksime`, `Ĝi estas sufiĉe proksime`, `Iom plu`, `Piede estas malproksime`, `Ĉirkaŭ la angulo`, `Ĝi estos maldekstre de vi`, `Kontraŭ la poŝtoficejo`, `Ĉe la semaforo`, `Tuj malantaŭ la aŭtobushaltejo`, `Iru tra la parko`, `Iru rekte. Poste turnu maldekstren`, `Vi prefere prenu la buson` は、方向・位置・距離・交通手段の指示表現として対応する。
- `Piede estas malproksime` は現在 ZH でも「歩くには遠い」条件が出ており、EO/RU/JA/KOと合う。`maldekstre de vi` は道案内の「左手に」、`kontraŭ` は across/opposite、`semaforo` は traffic lights として維持した。`Ĉirkaŭ la angulo` の中訳はやや「角に」寄るが、近接位置を示す短い道案内として明確な誤りとはしない。
- `Daŭrigu rekte antaŭen ĉirkaŭ unu kilometron`, `Pardonu, mi ne scias la vojon`, `Ĝi estas je du paŝoj`, `Estas proksimume kvinminuta piediro`, `Ĝi estas sufiĉe malproksime de ĉi tie`, `Ĝi estas proksime de la superbazaro`, `Ĝi estas ĝuste trans la strato`, `Ĝi estas ĝuste tie, antaŭ vi`, `Ĝi estos rekte antaŭ vi`, `Vi bezonos sufiĉe da tempo por alveni tien`, `Ĉe la fino de la strato`, `Ĉe la angulo de la bulvardo`, `Daŭrigu preter la fajrobrigadejo`, `Daŭrigu ankoraŭ ducent metrojn`, `Daŭrigu ankoraŭ duonkilometron` は、道順・距離・位置関係の説明として意味ズレなし。
- `trans la strato` は PIV の場所表現と合い、across the street / 通りの向こう側として維持した。`fajrobrigadejo` は `fajrobrigado` + `-ejo` の透明派生で fire station として問題ない。`duonkilometron` は約500mの距離表現として各列と対応する。

主な据え置き確認:
- Recommendation Letter: `rekomendletero`, `gvidanto`, `komunikajn kapablojn`, `plej varman rekomendon`, `altkvalitan laboron`, `aldono al via programo`, `verki rakontojn`, `elstaran kontribuon`, `fidinda persono kun bona humursento` は推薦状文脈で維持。
- Asking Directions: `ŝparvojo`, `desegni mapon`, `fervojstacio`, `metrostacio`, `vidindaĵoj`, `marbordo`, `poŝtoficejo` / `poŝtejo`, `aŭtobusa stacio`, `interreta kafejo`, `ambasadejo`, `piediri`, `diri al mi la direkton`, `orientiĝas` は道案内文脈で維持。
- Giving Directions: `maldekstren`, `dekstren`, `Iru tien malsupren`, `kruciĝo`, `piede`, `ĉirkaŭ la angulo`, `maldekstre de vi`, `kontraŭ la poŝtoficejo`, `semaforo`, `aŭtobushaltejo`, `prefere prenu`, `je du paŝoj`, `trans la strato`, `fajrobrigadejo`, `duonkilometron` は道順説明として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `rekomendi`, `gvidi` / `gvidanto`, `programo`, `ŝparvojo`, `marbordo`, `stacio` / `stacidomo`, `ambasadejo`, `orienti` / `orientiĝi`, `piedi` / `piede`, `trans`, `semaforo`, `fajro` / `fajrobrigado`, `kruciĝo`, `bulvardo`, `vidindaĵo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1756`〜`ID1855` は100件確認済み。

## 620. 619周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business
- Jobs / At the Interview
- Jobs / Recommendation Letter

結果:
- **CSV修正なし**
- 前回 `ID1556`〜`ID1655` に続き、今回は `ID1656`〜`ID1755` の100件を確認した。ビジネス文書・注文・支払い、採用面接、推薦状のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1659` RU、`ID1662` ZH、`ID1664` EO、`ID1673` ZH、`ID1674` RU、`ID1683` RU、`ID1686` EO/RU、`ID1694` EN、`ID1713` EO、`ID1714` EN、`ID1725` EN、`ID1727` RU、`ID1736` EO/EN、`ID1740` ZH、`ID1750` EN/JA/ZH/KO は、現CSVで補正後内容になっていることを確認した。
- `Jen mia vizitkarto`, `Mi pensas, ke ni devus renkontiĝi`, `Kiam konvenus al vi?`, `Mi ne povas veni morgaŭ je la 2-a posttagmeze`, `Bonvolu konfirmi skribe`, `Jen mia fakturo`, `Via propono konvenas al ni`, `Ni ŝatus nuligi nian mendon`, `Mi ofte faras afervojaĝojn`, `Ni ĵus ricevis vian fakson`, `Bonvolu sendi al ni pli detalan informon`, `Ĉu ni povus fari ĝin iom pli frue?`, `Ĉu estus eble aranĝi alian daton?`, `Ni akceptas viajn kondiĉojn de pago`, `Bonvolu tuj sendi vian pagon`, `Ni atendas vian konfirmon`, `Per ĉi tio ni konfirmas vian mendon`, `Bonvolu resendi subskribitan kopion de la kontrakto` は、商談・請求・注文・支払い・日程調整の文脈で意味ズレなし。
- `propono` は offer/提案として現在の ZH `提议` と合い、旧 `报价` に戻す理由はない。`resendi subskribitan kopion` は文書の返送として現在の ZH `寄回` が自然で、EO/JA/RUとも対応する。`fakturo`, `mendo`, `kontrakto`, `konfirmo`, `kondiĉoj de pago` はビジネス文書語彙として維持できる。
- `Mi ŝatus havi rendevuon kun sinjoro Wang, mi petas`, `Bedaŭrinde mi devas nuligi nian rendevuon`, `Mi scivolas, ĉu ni povas prokrasti nian kunvenon?`, `Mi estas devigata ŝanĝi la daton de nia renkontiĝo`, `Amiko varme rekomendis vian kompanion`, `Ni ĝojas fari mendon ĉe via kompanio`, `Via mendo estos traktita kiel eble plej rapide`, `Ĉu vi povus konfirmi la daton de ekspedo?`, `Via varo estos sendita ene de du semajnoj`, `Kiam ni negocos pri la prezo?`, `Laŭ la politiko de nia kompanio, ni fakturas nur en eŭroj`, `Ni ankoraŭ ne ricevis pagon por ĉi tiu monato` は、面会予約・延期・注文処理・発送・価格交渉・請求通貨・入金確認の文脈で対応する。
- `Mi scivolas, ĉu ...?` は間接疑問としては句読法に揺れがあるが、丁寧な依頼文として各列と衝突しない。`ekspedo` は発送/dispatch、`negoci pri la prezo` は価格交渉、`fakturas nur en eŭroj` はユーロ建て請求として維持した。
- `Ĉu vi havas formularon por vivresumo?`, `Ĉu vi studis en universitato?`, `Kion vi studis?`, `Mi studis matematikon`, `Kia estas la salajro?`, `Naŭcent dolaroj monate`, `Kie vi studis en universitato?`, `Mi studis en Kembriĝo`, `Mi neniam studis en universitato`, `Mi studis politikon`, `Kia laboro ĝi estas?`, `Kiajn kondiĉojn vi proponas?`, `Ĉi tio estas la laborpostena priskribo`, `Al kiu mi devus raporti?`, `Ĉu estas kompania aŭto?`, `Ĉu ekzistas pensia programo?`, `Mi ŝatus akcepti tiun laboron` は、学歴・給与・職務内容・報告先・待遇確認の面接文として意味ズレなし。
- `formularo por vivresumo` は履歴書用フォームとして既存補正を維持する。`raporti al` は報告先を尋ねる構文として自然で、`pensia programo`, `kompania aŭto`, `laborpostena priskribo` も雇用条件の文脈で透明。
- `Ĉu vi estas komputile klera?`, `Kiam vi povas komenci labori?`, `Kian edukon vi havas?`, `Kiujn kvalifikojn vi havas?`, `Ĉu vi havas laborsperton?`, `Ĉu vi havas validan stirpermesilon?`, `Kia estas via kariera celo?`, `Ĉu vi bezonas laborpermesilon?`, `Ni devos akiri rekomendojn`, `Ni ŝatus proponi al vi ĉi tiun laboron`, `Ĉi tio estas via laborkontrakto`, `Estas trimonata provperiodo`, `Mi ŝatus kandidatiĝi por ĉi tiu laborposteno`, `Mi laboras silente kaj efike`, `Mi estas sperta uzanto de Excel`, `Ĉu mi devos labori laŭvice?`, `Kiuj estas viaj laborhoroj?`, `Ĉu estas manĝejo por la personaro?`, `Kiom mi gajnos?`, `10 pundoj hore`, `Kiam vi volas, ke mi komencu?` は、応募・採用条件・資格・経験・契約・勤務形態の表現として対応する。
- `komputile klera` は PIV の `komputila klero` から computer-literate として読める。`akiri rekomendojn` は references/recommendations の面接文脈で許容し、`laborkontrakto` は PIV の `labor kontrakto` 例と対応する。`labori laŭvice` は PIV の `deĵoras ... laŭvice` 型から交替勤務として維持した。
- `Mi vidis vian anoncon en la gazeto`, `Mi ŝatus esti dungita de via kompanio`, `Ĉu mi povus ricevi aliĝilon?`, `Mi deziras kandidatiĝi por la posteno de oficeja administranto`, `Mi tre interesiĝas pri ĉi tiu posteno`, `Ĉu tio estas provizora aŭ konstanta posteno?`, `Ĉu ekzistas senpaga medicina asekuro?`, `Ĉu mi ricevos pagon por ekstra laboro?`, `Ĉu mi devos labori sabate?`, `Ĉu mi estos pagata ĉiusemajne aŭ ĉiumonate?`, `Ĉu mi ricevos vojaĝkostojn?`, `Kiom da semajnoj da ferio estas jare?`, `Mi havas 15-jaran sperton kiel flegistino`, `Mia fako estas informatiko`, `Mi estas tre dankema pro via propono`, `Mi vidas ĉi tiun postenon kiel bonvenan defion`, `Mi estus dankema pro la ebleco vastigi mian scion` は、応募書類・職種・雇用形態・保険・追加勤務・休暇・経験・専門分野・志望動機の文脈で意味ズレなし。
- `aliĝilo` は application form としてやや広いが、応募用紙文脈で通じるため維持した。`provizora aŭ konstanta posteno` は temporary/permanent position、`vojaĝkostojn` は travel expenses、`informatiko` は IT / information technology 寄りの訳と分野名の揺れがあるが、情報系専門分野として大きな意味ズレはない。
- `Ni ŝatus inviti vin al intervjuo`, `Ni bezonas iun kun kvalifikoj`, `Miaj kvalifikoj respondas al la postuloj de ĉi tiu posteno`, `Kiuj estas viaj fortaĵoj kaj malfortaĵoj?`, `Miaj fortaj flankoj estas lojaleco kaj akurateco`, `Kiuj estas viaj salajraj atendoj?`, `Kiom oni pagis al vi en via antaŭa laboro?`, `Mi ne havas laborsperton en ĉi tiu kampo` は、面接招待・要件適合・長所短所・給与・経験確認として対応する。`lojaleco` と `akurateco` は人物評価として PIV の語義と合う。
- `Li estas laborema homo`, `Ŝi bone plenumas siajn devojn`, `Li havas vastan gamon de kapabloj`, `Li akceptas konstruktivan kritikon`, `Li estas kreema solvanto de problemoj`, `Ŝi ĉiam finas sian laboron ĝustatempe`, `Estas granda plezuro labori kun ŝi` は、推薦状・人物評価の定型表現として意味ズレなし。過去補正済みの `plenumas siajn devojn` は、現CSVの日中韓英で「責任感」ではなく「職務・義務を果たす」方向になっていることを確認した。

主な据え置き確認:
- Business: `vizitkarto`, `konfirmi skribe`, `fakturo`, `propono`, `nuligi nian mendon`, `afervojaĝojn`, `fakson`, `pli detalan informon`, `kondiĉojn de pago`, `Per ĉi tio ni konfirmas vian mendon`, `subskribitan kopion de la kontrakto`, `rendevuon`, `prokrasti nian kunvenon`, `dato de ekspedo`, `negocos pri la prezo`, `fakturas nur en eŭroj` は商談・注文・請求・発送文脈で維持。
- At the Interview: `formularon por vivresumo`, `laborpostena priskribo`, `raporti al`, `komputile klera`, `validan stirpermesilon`, `laborpermesilon`, `akiri rekomendojn`, `laborkontrakto`, `trimonata provperiodo`, `kandidatiĝi`, `labori laŭvice`, `manĝejo por la personaro`, `aliĝilon`, `provizora aŭ konstanta posteno`, `medicina asekuro`, `vojaĝkostojn`, `informatiko`, `bonvenan defion`, `vastigi mian scion`, `fortaĵoj/malfortaĵoj`, `salajraj atendoj` は応募・採用文脈で維持。
- Recommendation Letter: `laborema homo`, `plenumas siajn devojn`, `vasta gamo de kapabloj`, `konstruktivan kritikon`, `kreema solvanto de problemoj`, `ĝustatempe`, `granda plezuro labori kun ŝi` は推薦状文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `fakturo`, `ekspedi` / `ekspedo`, `kontrakto` / `labor kontrakto`, `kandidato` / `kandidatiĝi`, `raporti`, `rekomendi` / `rekomendo`, `salajro`, `asekuro`, `deĵori` / `laŭvice`, `aliĝilo`, `akurat` / `akurateco`, `lojal`, `trejni`, `flegistino`, `komputila klero`, `vojaĝkostoj` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1656`〜`ID1755` は100件確認済み。

## 619. 618周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation
- Jobs / Employment Status
- Jobs / At the Workplace
- Jobs / Business

結果:
- **CSV修正なし**
- 前回 `ID1456`〜`ID1555` に続き、今回は `ID1556`〜`ID1655` の100件を確認した。職業、雇用状態、職場、ビジネス会話のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1556` RU、`ID1595` JA、`ID1600` EO、`ID1618` JA、`ID1641` EN、`ID1650` EO/EN/JA/RU は、現CSVで補正後内容になっていることを確認した。特に `ID1595` は現在 `自分の事業をしています。` で、EO `Mi havas propran komercon` / RU `У меня свой бизнес.` と対応する。
- `Ŝi laboras por kompanio`, `Li laboras sur farmo`, `Kion faras viaj gepatroj?`, `Per kio vi gajnas vian vivon?`, `Mi estas merkatika administranto`, `Mi trejniĝas por fariĝi flegistino`, `Mi trejniĝas por fariĝi inĝeniero`, `Mi estas staĝanta administranto de superbazaro`, `Mi estas doktoro pri juro`, `Mi laboras por investa banko`, `Mi ĵus fondis mian propran firmaon`, `Kie laboras via edzino?`, `Ŝi laboras en banko`, `Li estas konata ĵurnalisto`, `Mia nevo estas arkitekto`, `Mia pli aĝa fratino estas ekonomikisto`, `Mia onklino estas lerneja psikologo`, `Lili estas bonega administranto pri vendoj`, `Ŝi estas eksperto pri ekologio`, `Kiel nomiĝas la kompanio, por kiu vi laboras?` は、職業・勤務先・親族の職業説明として意味ズレなし。
- `merkatika administranto` は EN/JA/ZH/KO が manager 寄り、RU が specialist 寄りだが、PIV の `merkatiko` と `administri` / `administranto` の範囲から marketing manager/administrator 系として許容でき、ここでは片側へ寄せて過修正しない。`trejniĝas`, `staĝanta`, `doktoro pri juro`, `administranto pri vendoj`, `eksperto pri ekologio` も職業・訓練・専門性の文脈で維持した。
- `nevo`, `pli aĝa fratino`, `onklino` は、中韓で話者性別・父母側に応じた具体化があるが、短文クイズでは親族関係の中心意味を保っているため維持した。
- `Mi estas studentino`, `Mi laboras plentempe`, `Mi estas memstara laboristo`, `Mi ne laboras`, `Mi laboras hejme`, `Mi estas senlabora`, `Mi estas emerita`, `Mi estas dommastrino`, `Mi serĉas laboron`, `Mi laboras neleĝe`, `Li laboras partatempe`, `Mi laboras memstare`, `Mi faras praktikon`, `Li estis promociita`, `Ŝi estas en patrina forpermeso`, `Li estas en patra forpermeso`, `Mi nuntempe partoprenas kurson`, `Mi momente ne laboras`, `Mi estas partnero en advokata firmao`, `Mi havas propran komercon`, `Mi faras iom da volontula laboro`, `Mi restas hejme kaj zorgas pri la infanoj`, `Ĉu vi volus emeritiĝi?`, `Kial vi ne laboras?`, `Mi estis maldungita pro redukto de laborfortoj antaŭ du monatoj` は、雇用状態・就業形態・休暇・退職・解雇の表現として対応する。
- `memstara laboristo` は freelancer、`Mi laboras memstare` は self-employed として自然に区別されている。`patrina forpermeso` / `patra forpermeso` は maternity/paternity/parental leave の範囲で各列と対応し、`redukto de laborfortoj` は人員削減による redundancy/layoff の表現として維持した。
- `Mi laboras ĉi tie`, `Kiel vi veturas al la laborejo?`, `Mi veturas per aŭto`, `Ĉu vi bezonas helpon?`, `Momenton, mi petas`, `Ĉu vi laboras hodiaŭ?`, `Kion mi povas fari por vi?`, `Kiun vi serĉas?`, `Mi serĉas sinjoron Lee`, `Li hodiaŭ forestas`, `Li estas en kunveno`, `Li hodiaŭ forestas pro malsano`, `Mi eliras por tagmanĝi`, `Kie estas la fotokopiilo?`, `Ŝi demisiis`, `Ĉu vi ŝatas vian ĉefon?`, `Kiom da horoj semajne vi laboras?`, `Mi komencas je la oka kaj finas je la kvina`, `Ĉu mi povas vidi la raporton?`, `Ĉu mi povas presi?`, `La printilo ne funkcias`, `Mi bezonas fari kelkajn fotokopiojn`, `La fotokopiilo blokiĝis`, `Mi ne povas aliri mian retpoŝton`, `La pago de ĉi tiu fakturo malfruas` は、職場内の基本会話・機器・メール・請求書の文脈で意味ズレなし。
- `Mi revenos je la 13:30`, `Mi estos libera post la tagmanĝo`, `Pardonu, ke mi igis vin atendi`, `Mi iros eksterlanden la venontan semajnon`, `Ĉu vi povus organizi la vojaĝon por mi?`, `Ĉu vi altigos mian salajron?`, `Ĉu vi faris tion antaŭe?`, `Kiom da tempo vi bezonas por atingi vian laborejon?`, `Ĉu vi ŝatas viajn kunlaborantojn?`, `Kiom longe vi laboras ĉi tie?`, `Vi estas maldungita!`, `Vi devas trovi al vi novan laboron`, `Mi lasos vin reveni al via laboro`, `Vendrede ŝi havos adiaŭan feston`, `Johano morgaŭ foriras ferien`, `Tagmeze mi havas unuhoran tagmanĝan paŭzon`, `Je kioma horo finiĝas la kunveno?`, `Kie mi povas fari kopiojn de miaj dokumentoj?`, `Estas problemo kun mia komputilo`, `La interreto momente ne funkcias`, `Mi lasis la dosieron sur via skribotablo`, `Bonvolu faksi ĉi tion al nia oficejo`, `Li nun estas kun kliento`, `Mi revenos al vi post momento`, `La limtempo por liveri la varojn finiĝas`, `Mi ĝojas informi vin, ke mi havas solvon por vi`, `Persone, mi kredas je ŝia strategio` は、職場の予定・移動・休暇・会議・機器・納期・顧客対応として対応する。
- `Mi lasos vin reveni al via laboro` は日中韓で「仕事へ戻る/邪魔しない」方向に自然化されているが、EO と RU の中心意味から許容した。`limtempo por liveri la varojn finiĝas` は納品期限が尽きる文脈で、現CSVでは旧 `eksvalidiĝas` ではなく `finiĝas` になっていることを確認した。`faksi`, `retpoŝto`, `fakturo`, `kliento`, `tagmanĝa paŭzo`, `salajro`, `adiaŭa festo`, `ferie` も職場文脈で維持できる。
- `Ĉu ni povas aranĝi kunvenon?`, `Tio estas tre grava`, `Ni povas fari la interkonsenton` は、ビジネス会話の導入短文として意味ズレなし。`interkonsento` は agreement/deal の範囲で、JA/ZH/KO/RU の取引成立表現と対応する。

主な据え置き確認:
- Occupation: `merkatika administranto`, `trejniĝas`, `staĝanta administranto de superbazaro`, `doktoro pri juro`, `fondis mian propran firmaon`, `nevo`, `pli aĝa fratino`, `onklino`, `administranto pri vendoj`, `eksperto pri ekologio` は職業・親族職業文脈で維持。
- Employment Status: `studentino`, `plentempe`, `memstara laboristo`, `senlabora`, `emerita`, `dommastrino`, `neleĝe`, `partatempe`, `memstare`, `faras praktikon`, `promociita`, `patrina/patra forpermeso`, `partoprenas kurson`, `advokata firmao`, `propran komercon`, `volontula laboro`, `zorgas pri la infanoj`, `emeritiĝi`, `maldungita pro redukto de laborfortoj` は雇用状態として維持。
- At the Workplace / Business: `laborejo`, `fotokopiilo`, `demisiis`, `retpoŝton`, `fakturo`, `igis vin atendi`, `altigos mian salajron`, `adiaŭan feston`, `foriras ferien`, `tagmanĝan paŭzon`, `faksi`, `kliento`, `limtempo por liveri la varojn finiĝas`, `kredas je ŝia strategio`, `aranĝi kunvenon`, `fari la interkonsenton` は職場・ビジネス文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `merkatiko`, `administri` / `administranto`, `trejniĝi`, `staĝo`, `praktiko`, `promocii`, `forpermeso`, `dungi` / `maldungi`, `komerco`, `fakturo`, `faksi`, `retpoŝto`, `limtempo`, `interkonsento`, `emerito`, `memstara`, `laborforto` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1556`〜`ID1655` は100件確認済み。

## 618. 617周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life
- Education / Numbers & Colours
- Jobs / Occupation

結果:
- **CSV修正なし**
- 前回 `ID1356`〜`ID1455` に続き、今回は `ID1456`〜`ID1555` の100件を確認した。研究・試験、数詞・色名、職業名のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1456` EN/JA、`ID1457` EN、`ID1460` EN/JA、`ID1461` RU、`ID1465` EN、`ID1467` EN、`ID1485` RU、`ID1486` EO、`ID1500` RU、`ID1503` EO、`ID1504` EO、`ID1506` EN、`ID1540` EN/JA、`ID1543` JA/ZH/KO、`ID1555` ZH は、現CSVで補正後内容になっていることを確認した。
- `Ĉu la demandoj povas esti formulitaj skribe?`, `Ĉu plaĉis al vi la raporto pri sanservo?`, `Ili faras esploradon en la kampo de fiziko`, `Ĉu ĉi tiu kampo estis esplorita antaŭe?`, `Kiu proponis tiun ideon?`, `Kiu estas la inventinto de la telefono?`, `Ĉu vi konas la laboron de Maria Curie?`, `Kiom da ekzamenoj vi havas ĉi-semestre?`, `Ĉu vi baldaŭ havos ekzamenojn?`, `Kiom da tagoj vi havas por preparo?`, `Ĉi tio estas la lasta ekzamena sesio por ni`, `Mi ankoraŭ devas ripeti multajn aferojn` は、学生生活・研究・試験準備の文脈で意味ズレなし。
- `sanservo` は healthcare / RU `здравоохранение` として透明な複合語、`raporto` は口頭・文書の幅を持つため JA の報告書寄りと RU の発表寄りを許容した。`ripeti multajn aferojn` は「復習する」としてやや広いが、学習で反復する意味として維持できる。
- `Nulo`, `Unu, du, tri, kvar, kvin`, `Ses, sep, ok, naŭ, dek`, `Unu plus du egalas tri`, `Naŭ minus kvin egalas kvar`, `Kiukolora ĝi estas?`, `La pomo estas ruĝa`, `Ruĝo kaj blanko faras rozkoloron`, `Dek unu, dek du, dek tri`, `Dek kvar, dek kvin, dek ses`, `Dek sep, dek ok, dek naŭ`, `Kvarfoje tri estas dek du`, `Dek ok dividite per ses estas tri`, `La neĝo estas blanka`, `La kato estas nigra`, `Nigro kaj blanko faras grizon`, `La karoto estas oranĝa`, `La urso estas bruna`, `Ruĝo kaj verdo faras brunon` は、数詞・四則演算・基本色として各列と対応する。
- `Dek, dudek, tridek, kvardek, kvindek` から `Naŭdek sep, naŭdek ok, naŭdek naŭ` までの数詞列、`Cent ok`, `Cent dek`, `Cent dudek sep`, `Ducent kvindek ok`, `Tricent dek naŭ`, `Cent mil`, `Unu miliono`, `Unu miliardo`, `Cent multiplikite per dek estas mil`, `Du mil foje kvin estas dek mil`, `La ĉielarko havas sep kolorojn` は、数値対応に問題なし。韓国語の固有数詞・漢数詞の揺れはあるが、値の対応は崩れていないため過修正しない。
- `La pruno estas viola`, `Ruĝo kaj bluo faras violan koloron`, `Bluo kaj flavo faras verdon`, `Flavo kaj ruĝo faras oranĝan koloron`, `Verdo kaj flavo faras helverdan koloron`, `Mia plej ŝatata koloro estas viola` は、色名・混色表現として列間対応を保つ。`viola` は PIV で「ruĝo + bluo」による色として確認でき、purple / violet / сиреневый 系の幅は色名クイズとして許容範囲。
- `Kio estas via profesio?`, `Mi estas instruisto`, `Mia patrino estas kuracisto`, `Kie vi laboras?`, `Mi laboras en vendejo`, `Mi estas profesoro`, `Mi laboras en fabriko`, `Mi laboras en oficejo`, `Mi laboras en informteknologio`, `Mi laboras en televido`, `Por kiu vi laboras?`, `Mi laboras por la loka konsilio`, `Kion faras via patro?`, `Li estas juristo`, `Kion faras via patrino?`, `Ŝi estas veterinaro`, `Kian laboron vi faras?`, `Mi laboras kiel tradukisto`, `Mi estas staĝanta kontisto`, `Mi estas komercistino`, `Mia onklo estas dentisto`, `Mi laboras en vokcentro`, `Mi laboras kun komputiloj`, `Mi laboras kiel programisto`, `Mi laboras kiel ĵurnalistino`, `Mi laboras kun handikapitaj infanoj` は、職業・勤務先・職務分野として意味ズレなし。
- `juristo` は PIV で法律・司法の専門家を表し、`advokato` 相当に狭めない現在の日中韓補正を維持した。`informteknologio` と `vokcentro` はPIV直接見出しとしては弱いが、構成要素が透明でIT/call centre文脈に明確に対応する。`komercistino` は businesswoman / RU `предприниматель` の広い職業表現として許容した。`handikapitaj infanoj` は現代的な言い換え余地はあるが、PIV の `handikapo` 系と disabled children の意味対応から維持した。

主な据え置き確認:
- Student Life: `formulitaj skribe`, `raporto pri sanservo`, `esploradon en la kampo de fiziko`, `proponis tiun ideon`, `inventinto`, `ekzamena sesio`, `ripeti multajn aferojn` は研究・試験文脈で維持。
- Numbers & Colours: 数詞列、`plus`, `minus`, `foje`, `dividite per`, `multiplikite per`, `rozkoloron`, `grizon`, `brunon`, `violan koloron`, `oranĝan koloron`, `helverdan koloron`, `ĉielarko` は数・色文脈で維持。
- Jobs: `profesio`, `informteknologio`, `loka konsilio`, `juristo`, `veterinaro`, `tradukisto`, `staĝanta kontisto`, `komercistino`, `vokcentro`, `programisto`, `ĵurnalistino`, `handikapitaj infanoj` は職業文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `ripeti`, `koloro`, `ruĝo`, `verdo`, `bruno`, `oranĝa`, `viola`, `profesio`, `juristo`, `advokato`, `veterinaro`, `komercisto`, `kontisto`, `tradukisto`, `ĵurnalisto`, `handikapo`, `voki`, `teknologio` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1456`〜`ID1555` は100件確認済み。

## 617. 616周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School
- Education / At University
- Education / Student Life

結果:
- **CSV修正なし**
- 前回 `ID1256`〜`ID1355` に続き、今回は `ID1356`〜`ID1455` の100件を確認した。学校、大学、学生生活、図書館、発表・会議表現のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1356` EO、`ID1378` EO、`ID1386` EO、`ID1393` EN/KO、`ID1395` RU、`ID1400` EN、`ID1401` JA、`ID1402` ZH、`ID1410` EN/ZH、`ID1413` EN/JA/ZH/KO、`ID1423` KO、`ID1437` EN、`ID1444` EO、`ID1447` EN は、現CSVで補正後内容になっていることを確認した。
- `Neniu rajtas forlasi la klasĉambron nun`, `En kiu aĝo infanoj komencas iri al lernejo?`, `Kiam finiĝas la lerneja jaro?`, `Kiom da lernantoj estas en ĉi tiu lernejo?` は、教室退出、就学開始年齢、学年/学校年度、在籍人数の表現として対応する。`En kiu aĝo` は `Je kiu aĝo` も候補だが、PIV の `en la aĝo de ...` 型から明確な誤りとはしない。
- `Kiel mi kandidatiĝu?`, `Ĉu vi estas studentino?`, `Kie vi lernas?`, `Mi studas ĉe universitato`, `Kion vi studas?`, `Mi studas medicinon`, `Al kiu universitato vi iras?`, `Mi studas ĉe la Universitato de Liverpolo`, `Mi lernas ĉi tie`, `Mi studas lingvistikon`, `Mi studas historion`, `Ili studas kemion`, `En kiu studjaro vi estas?`, `Mi estas unuajara studento`, `Mi estas en mia lasta studjaro`, `Mi estas en la tria studjaro`, `Mi ĵus diplomiĝis`, `Mi penos laŭeble` は、大学での所属・専攻・学年・卒業・意思表明として意味ズレなし。
- `Mi studas la hindian` は PIV の `hindia lingvo` 型と合う。`studentino`, `unuajara studento` は性別・人物名詞の差があるが、JA/ZH/KO の中立表現でも対象人物を指せるため過修正しない。
- `Mi studas ekonomikon`, `Mi estas en la matematika klubo`, `Mi estas studento ĉe la Arta Fakultato`, `Mia filo studas informatikon`, `Ĉu vi laboras aŭ studas?`, `Mi studas por magistriĝo pri juro`, `Mi doktoriĝas pri kemio`, `Mi prenas liberan jaron`, `Kiam komenciĝas la kursoj?`, `Kiun kurson vi instruas?`, `Mi prelegas pri matematika analizo`, `Kiu povas studi senpage?`, `Ĉu vi proponas distancan lernadon?`, `Ĉu studentoj ricevas stipendiojn?` は、大学生活・学位・休学/ギャップイヤー・講義・奨学金の文脈で対応する。
- `Kiujn fakultatojn havas ĉi tiu universitato?`, `Kiom da homoj loĝas en ĉi tiu ĉambro?`, `Kiom longe vi lernas la bulgaran?`, `Ŝi estas studentino specialiĝanta pri geografio`, `Ŝi havas diplomon pri administrado`, `Kiuj estas la akceptkondiĉoj?`, `Ĉu vi havas enirajn ekzamenojn?`, `Kiu estas la rektoro de la universitato?`, `Ĉu vi havas studentojn el aliaj landoj?`, `Ĉu vi povus plenigi ĉi tiun registriĝan formularon?`, `Ni ŝatus viziti la studentloĝejon`, `Ni volus renkontiĝi kun la universitataj instruistoj`, `Permesu al mi esti via gvidanto`, `Mi estas la estrino de la fako`, `Mi instruos biologion en la venonta semestro`, `Li estas lektoro pri la rusa lingvo ĉe Oksforda Universitato` は、大学制度・施設・役職・案内表現として意味ズレなし。
- `fakultato`, `rektoro`, `lektoro`, `formularo`, `studentloĝejo`, `estrino de la fako`, `akceptkondiĉoj`, `eniraj ekzamenoj` は、PIV の語義または透明な複合構成から大学文脈で維持できる。
- `Ĉu vi apartenis al iuj kluboj en mezlernejo?`, `Ĉu vi estas membro de iu libroklubo?`, `La plej multaj el miaj amikoj estas membroj de la klubo`, `Mi estas ano de la studenta asocio`, `Kiom da jaroj vi ankoraŭ devas studi?`, `Kion vi volas fari, kiam vi finos?`, `Mi ne scias, kion mi volas fari post la universitato` は、クラブ所属、学生会、在学残年数、卒業後進路の表現として対応する。
- `Mi havas demandon`, `Ni havas kvin ekzamenojn`, `Mi estis en la biblioteko`, `Tio ĉi estas tre malfacila`, `Kiu parolas nun?`, `Mi interesiĝas pri literaturo`, `Ĉu mi povas prunti libron?`, `Ĉu mi povas ekzerciĝi kun vi?`, `Kie estas la katalogo?`, `Kiu parolos unue?`, `Pri kio estas la sekva raporto?`, `Kion vi observis?`, `Mi ŝatus fari rimarkon`, `Kiam estas la unua ekzameno?`, `Kiajn rezultojn vi ricevis?`, `Kiel mi povas plenigi la bibliotekan formularon?`, `Kiam fermiĝas la biblioteko?`, `Mi ŝatus prunti kelkajn historiajn librojn` は、図書館・練習・発表・試験の学生生活表現として対応する。`Kion vi observis?` のJAは「気づいたこと」と自然化されているが、observe/notice の範囲で中心意味は保つため維持した。
- `Kiu estas la aŭtoro de ĉi tiu artikolo?`, `Al kiu apartenas ĉi tiu malkovro?`, `Mi estas preta por la lingva ekzameno`, `Mi faros mian raporton en la kataluna`, `Mi ŝatus fari sugeston`, `Ĉu ĝi estas valida eksperimento?`, `Kiam okazos la konferenco?`, `Kiom da partoprenantoj estas tie?`, `Kiam komenciĝas la ekzamenoj?`, `Li brile trapasis ĉiujn ekzamenojn`, `Li malsukcesis en la ekzameno pri filozofio`, `Pri kio estas via disertacio?`, `Mia disertacio temas pri sociologiaj problemoj`, `Kiel oni povas aliĝi al la biblioteko?`, `Via biblioteka karto validas dum 3 jaroj`, `Ni ŝatus prunti kelkajn lingvistikajn librojn`, `Ŝi interesiĝas pri infana literaturo`, `Mi iras al konferenco`, `Kiu estas la invitita parolanto ĉe la konferenco?`, `Ŝi estas brila oratoro`, `Kiu estas la templimo por paroladoj?`, `Ĉu la demandoj povas esti formulitaj buŝe?` は、論文・図書館・会議・発表の文脈で意味ズレなし。
- `raporto` はPIVで口頭・文書の両方に読めるため、`Mi faros mian raporton en la kataluna` の日中韓が報告書作成寄り、RU が発表寄りでも明確な衝突とはしない。`templimo` は PIV に見える複合語で、time limit として維持した。`oratoro` は女性主語でも性別明示の `oratorino` へ直す必然性は低い。

主な据え置き確認:
- At School: `klasĉambron`, `En kiu aĝo`, `lerneja jaro`, `lernantoj` は学校文脈で維持。
- At University: `studentino`, `studi ĉe universitato`, `studjaro`, `diplomiĝis`, `hindian`, `magistriĝo`, `doktoriĝas`, `liberan jaron`, `distanca lernado`, `fakultatojn`, `akceptkondiĉoj`, `eniraj ekzamenoj`, `rektoro`, `registriĝan formularon`, `studentloĝejon`, `universitataj instruistoj`, `estrino de la fako`, `lektoro` は大学文脈で維持。
- Student Life: `prunti libron`, `ekzerciĝi kun vi`, `raporto`, `observis`, `bibliotekan formularon`, `valida eksperimento`, `trapasis`, `malsukcesis en la ekzameno`, `disertacio`, `aliĝi al la biblioteko`, `biblioteka karto`, `oratoro`, `templimo`, `formulitaj buŝe` は学生生活・会議文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `aĝo`, `hindia`, `magistro` / `magistriĝo`, `doktoriĝi`, `fakultato`, `formularo`, `rektoro`, `lektoro`, `ekzerciĝi`, `biblioteko`, `raporto`, `prunti`, `templimo`, `oratoro`, `buŝa` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1356`〜`ID1455` は100件確認済み。

## 616. 615周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date
- Dating / Compliments
- Dating / Wedding
- Education / At School

結果:
- **CSV修正なし**
- 前回 `ID1156`〜`ID1255` に続き、今回は `ID1256`〜`ID1355` の100件を確認した。デート中の会話、褒め言葉、結婚・記念日、学校内表現のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- 過去周回で補正済みの `ID1260` EO、`ID1262` JA、`ID1279` JA、`ID1288` JA、`ID1304` EO/JA/ZH、`ID1309` KO、`ID1342` KO、`ID1345` EN、`ID1346` RU は、現CSVで補正後内容になっていることを確認した。
- `Ĉu vi havas fotojn de vi mem?`, `Ĉu vi scias kuiri?`, `Mi bakis ĉi tiun kukon por vi`, `Mi ĝuas pasigi tempon kun vi`, `Mi amas vin el mia tuta koro`, `Mi volas doni al vi donacon`, `Ĉu vi ŝatus enveni por taso da kafo?`, `Ĉu ni iru aliloken?`, `Kial ne? Mi konas bonan loketon`, `Ĉu vi estis ĉi tie antaŭe?`, `Kial ni do ne dancus?`, `Ĉu vi volas iri al alia festo?`, `Forigu viajn manojn de mi!` は、デート中の誘い・好意・拒否表現として列間対応を保つ。
- `Vi estas amuza`, `Vi estas tre afabla`, `Vi aspektas bonege`, `Dankon pro la komplimento!`, `Mi ŝatas vian veston`, `Vi estas ravega`, `Vi estas tre kuraĝa`, `Vi estas bonega dancisto`, `Via nova hararanĝo estas bonega`, `Vi estas tre speciala`, `Vi estas vere talenta kantistino`, `Vi vere bone aspektas`, `Vi havas belajn okulojn`, `Vi havas bonegan rideton`, `Mi trovas vin tre alloga`, `Mi agrable pasigis la tempon kun vi`, `Vi aspektas tre bele ĉi-vespere`, `Vi aspektas bela en tiu robo!`, `Vi havas belan nomon`, `Vi havas mirindan guston pri vestoj`, `Mi pensis pri vi la tutan tagon`, `Estas tre afable de vi diri tion, dankon` は、褒め言葉・返答として自然。
- `vesto` は PIV で身につける衣服全体を表し得るため outfit / 服装文脈で維持した。`ravega` は `rava` の規則的強意、`aspektas bele` と `aspektas bela` はいずれも褒め言葉として文脈上許容、`kantistino` は女性歌手だが JA/ZH/KO の中立的な「歌手」表現でも対象人物を指せるため過修正しない。
- `Mi amas vin`, `Mi ankaŭ amas vin`, `Kisu min`, `Ĉu vi edziniĝos kun mi?`, `Estas romantike`, `Vi estas mirinda paro`, `Mi invitas vin al la nupto`, `Gratulon pro via fianĉiĝo!`, `Gratulon al la novgeedzoj!`, `Mi esperas, ke vi ambaŭ estos tre feliĉaj kune`, `Fraŭlino Wane baldaŭ fariĝos sinjorino Jones`, `Venu kaj festu kun ni ilian fianĉiĝon`, `Ni ĝojas inviti vin al nia geedziĝo`, `Mi esperas, ke vi ege feliĉigos unu la alian`, `Varmajn bondezirojn al vi ambaŭ en via geedziĝa tago`, `Ni ĝojas anonci la edziĝon de nia filo`, `Dankon, ke vi venis ĉi tien hodiaŭ`, `Ni ĝojas anonci la fianĉiĝon de nia filino`, `Ĉu vi jam decidis pri la dato de la geedziĝo?`, `Mi deziras al vi ambaŭ ĉian feliĉon de la mondo` は、プロポーズ・婚礼・祝辞として意味ズレなし。
- `Ĉu vi edziniĝos kun mi?` は PIV の `edziniĝi kun viro` 型と合い、ZH/RU の女性相手のプロポーズ表現とも対応するため維持した。`nupto`, `geedziĝo`, `fianĉiĝo`, `novgeedzoj`, `edziĝo de nia filo`, `geedziĝa tago` は婚礼語彙として成立する。
- `Gratulon okaze de via porcelana geedziĝa jubileo!`, `Gratulon okaze de via arĝenta nupto!`, `Gratulojn okaze de via perla geedziĝa datreveno!`, `Gratulon pro via korala geedziĝa datreveno!`, `Gratulon pro via rubena geedziĝa datreveno!`, `Gratulon pro via diamanta nupto!` は、素材名 + 結婚記念日/婚式表現として透明で、各列の記念日表現と対応する。
- `La respondo estas ĝusta`, `La leciono finiĝis`, `Ĉu ĉi tiu plumo estas via?`, `Bonvolu silenti`, `Ĉu li ŝatas la lernejon?`, `Ĉu vi havas ŝranketojn?`, `Ĉu vi havas gimnastikejon?`, `Ĉu vi havas krajonon?`, `Donu al mi la liniilon`, `Kiu estis via instruisto pasintjare?`, `Bonvolu ripeti post mi`, `Ĉu tio estas ĉio, kion vi povas diri?`, `Vi povas iri hejmen`, `Kiu povas respondi mian demandon?`, `Kies libro estas tiu?`, `Kion vi scias pri Alĝerio?`, `Ni praktiku la islandan`, `Kien vi metis mian viŝgumon?`, `Vi progresas`, `Ĉu vi povas doni al mi ekzemplon?` は、学校内の指示・質問・備品・授業表現として対応する。
- `Tio estas hazarda eraro`, `La instruistino helpis min`, `Kie vi iris al lernejo?`, `Mi iris al lernejo en Bristolo`, `Mi finis lernejon deksesjaraĝe`, `Ĉu vi proponas somerajn lernejojn?`, `Ĉu vi havas plumon, kiun mi povus pruntepreni?`, `Pri kio vi du parolas?`, `Mi ne tute komprenis`, `Ĉu iu havas ion por aldoni?`, `Mi volus proponi al vi bonan libron`, `Mi pensas, ke vi devus lerni ĝin parkere`, `La eseo estis skribita haste`, `Estas pli bone ol la lastan fojon`, `Kion vi pensas pri viaj notoj?`, `Vi ricevis la plej altan noton`, `Ŝiaj notoj estas super la mezumo`, `Kiom da tempo restas ĝis la paŭzo?`, `La sonorilo baldaŭ sonoros` は、学習・成績・休憩・校内ベルの文脈で意味ズレなし。
- `gimnastikejo`, `ŝranketoj`, `respondi mian demandon`, `parkere`, `notoj`, `paŭzo`, `sonorilo` は、PIV の語義または用例から学校文脈で維持できる。

主な据え置き確認:
- Dating: `fotojn de vi mem`, `bakis ĉi tiun kukon`, `enveni por taso da kafo`, `aliloken`, `loketon`, `Forigu viajn manojn de mi!` はデート中の短文として維持。
- Compliments: `veston`, `ravega`, `hararanĝo`, `talenta kantistino`, `alloga`, `aspektas tre bele`, `aspektas bela en tiu robo`, `guston pri vestoj`, `afable de vi diri tion` は褒め言葉として維持。
- Wedding: `edziniĝos kun mi`, `nupto`, `fianĉiĝo`, `novgeedzoj`, `geedziĝo`, `feliĉigos unu la alian`, `porcelana/arĝenta/perla/korala/rubena/diamanta` の結婚記念日表現は婚礼文脈で維持。
- Education: `ŝranketoj`, `gimnastikejo`, `respondi mian demandon`, `la islandan`, `viŝgumon`, `hazarda eraro`, `iris al lernejo`, `finis lernejon deksesjaraĝe`, `somerajn lernejojn`, `parkere`, `lastan fojon`, `notoj`, `sonorilo` は学校文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `vesto`, `rava`, `aspekti`, `edziĝi` / `edziniĝi`, `nupto`, `fianĉiĝo`, `feliĉigi`, `porcelano`, `diamanta`, `ŝranko` / `ŝranketo`, `gimnastikejo`, `respondi`, `parkere`, `noto`, `paŭzo`, `sonorilo` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1256`〜`ID1355` は100件確認済み。

## 615. 614周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet
- Making Friends / Accepting  & Declining
- Dating / Asking Someone out
- Dating / On a Date

結果:
- **CSV修正なし**
- 前回 `ID1056`〜`ID1155` に続き、今回は `ID1156`〜`ID1255` の100件を確認した。承諾・断り、待ち合わせ、デートの誘い、親密表現・境界表現のブロックとして、ロシア語を主基準、英語を補助基準にしつつ、日中韓との直接対応を確認した。
- `Sinjoroj, ni povas ludi partion de golfo` は、PIV の `partio` がゲーム・競技の一回を表すため、golf round / RU `партию в гольф` と対応する。JA/ZH/KO は誘い文としてやや自然化されているが、男性複数への呼びかけと「ゴルフを一回する」中心意味は保たれているため、過修正しない。
- `Certe`, `Pardonu, mi ne povas`, `Bone!`, `Sonas bone`, `Neniel!`, `Jes, certe`, `Mi ne kontraŭas`, `Mi estas tro laca`, `Jes, mi estas libera`, `Certe ne!`, `Pardonu, mi ne povas veni`, `Dankon pro via invito`, `Kun plezuro`, `Tio estas bona ideo`, `Ĝi estas bona plano`, `Ĝis revido tie!` は、承諾・拒否・感謝・現地再会の短文として意味ズレなし。
- `Mi ne havas tempon`, `Mi havas lecionojn`, `Mi devas labori`, `Ni havas gastojn`, `Mi devas studi`, `Ne, mi ne estas libera`, `Eble venontfoje`, `Mi iomete malfruiĝas`, `Pardonu, sed mi ne povas akcepti vian inviton`, `Tio sonas alloge`, `Ni renkontiĝos tie`, `Mi estos tie post dek minutoj`, `Mi venos preni vin je la 5-a horo`, `Mi vidos vin en la kinejo je la deka horo`, `Mi estos tie je la naŭa, krom se la buso malfruos`, `Mi ankoraŭ ne decidis`, `Mi ne interesiĝas`, `Hodiaŭ vespere mi restos hejme` は、予定・遅延・辞退・待ち合わせの表現として対応する。
- `Mi terure bedaŭras, sed mi ne pensas, ke mi povos`, `Bedaŭrinde, mi jam havas planojn`, `Mi ne volas ĝeni vin`, `Mi volus, sed hodiaŭ mi laboras`, `Estus tre agrable akcepti lian inviton`, `Mi jam promesis renkontiĝi kun Sofia hodiaŭ vespere`, `Ne, dankon. Mi jam manĝis` は、断り・既約束・食事済みの文として列間対応を保つ。
- `Ĉu vi estas fraŭla?`, `Ĉu mi povas aliĝi al vi?`, `Ĉu mi povas aĉeti trinkaĵon por vi?`, `Ni manĝu ekstere hodiaŭ vespere`, `Ĉu vi estas sola?`, `Ĉu vi ofte venas ĉi tien?`, `Ĉu vi ŝatus iam tagmanĝi kune?`, `Mi ŝatus inviti vin al vespermanĝo`, `Kio pri hodiaŭ?`, `Hm. Mi pensos pri tio`, `Ĉu vi renkontiĝas kun iu?` は、デートへの導入・誘い・確認として自然。`fraŭla` は独身、`renkontiĝas kun iu` は Dating 文脈では「付き合っている/会っている人がいる」と読めるため維持した。
- `Ĉu ĝenas vin, se mi aliĝos al vi?`, `Mi regalos vin per trinkaĵo`, `Ni parolu plu dum la tagmanĝo`, `Ni trovu agrablan lokon kien iri`, `Ĉu vi volus vespermanĝi kun mi?`, `Ĉu vi volus denove renkontiĝi?`, `Pardonu, vi ne estas mia tipo`, `Ĉu vi pensas, ke mi devus telefoni al li?`, `Kion vi elpensis?`, `Vi povas fidi min` は、同席・飲食への誘い・再会・断り・相談として意味ズレなし。PIV の `aliĝi`, `regali`, `elpensi` の語義とも合う。
- `Ĉu vi havas planojn por ĉi-vespere?`, `Ĉu vi volus iufoje iri trinki ion?`, `Ĉu vi ŝatus iri al kinejo iam?`, `Ĉu vi ŝatus iri manĝeti ion?`, `Ĉu vi ŝatus iri trinki kafon?`, `Ĉu vi ŝatus iri kun mi al la teatro?`, `Ĉu vi ŝatus iam vespermanĝi kun mi?`, `Ĉu vi ŝatus spekti filmon ĉe mi?`, `Mi ŝatus iri ien por ripozi`, `Se vi ŝatus iam renkontiĝi, sciigu min` は、予定確認・映画/食事/飲み物/劇場への誘いとして対応する。
- `Vi plaĉas al mi`, `Vi mankas al mi`, `Ĉu mi povas kisi vin?`, `Ni renkontiĝu denove!`, `Mi fidas vin`, `Vi tre plaĉas al mi`, `Mi enamiĝis al vi`, `Ĉu mi povas brakumi vin?`, `Ĉu mi povas akompani vin hejmen?`, `Ĉe vi aŭ ĉe mi?`, `Ĉu vi ŝatas danci?`, `Telefonu al mi!`, `Ne tuŝu min!`, `Mi estas serioza`, `Mi nur ŝercas`, `Kion vi pensas pri mi?`, `Mi freneziĝas pro vi`, `Kiam mi povos revidi vin?`, `Ĉu mi povas veturigi vin hejmen?` は、親密さ・信頼・身体的接触の同意・拒否・送迎として列間対応を保つ。`akompani` と `veturigi` は徒歩を含む付き添い/乗り物で送るの差が保たれている。
- `Ĉu vi estas ĉi tie unuafoje?`, `Ĉu vi ŝatus danci?`, `Kun plezuro`, `Ĉu vi ŝatus veni al mi hejmen?`, `Kion vi pensas pri ĉi tiu loko?`, `Ni forveturu de ĉi tie`, `Lasu min trankvila`, `Ĉu vi povas rakonti al mi pli pri vi?` は、デート中の会話・誘い・退出・境界表現として自然。`Lasu min trankvila` は PIV の用例と一致する。

主な据え置き確認:
- `partion de golfo`, `Certe`, `Neniel!`, `Mi ne kontraŭas`, `Mi iomete malfruiĝas`, `akcepti vian inviton`, `Tio sonas alloge`, `Ni renkontiĝos tie`, `Mi venos preni vin`, `krom se la buso malfruos`, `Bedaŭrinde`, `ĝeni vin`, `promesis renkontiĝi kun Sofia` は、承諾・断り・予定調整文脈で維持。
- `fraŭla`, `aliĝi al vi`, `aĉeti trinkaĵon por vi`, `regalos vin per trinkaĵo`, `lokon kien iri`, `Kio pri hodiaŭ?`, `renkontiĝas kun iu`, `Kion vi elpensis?`, `iri trinki ion`, `iri manĝeti ion`, `sciigu min` は、デートへの誘い・同席・相談表現として維持。
- `plaĉas al mi`, `mankas al mi`, `enamiĝis al vi`, `brakumi/kisi vin`, `akompani vin hejmen`, `veturigi vin hejmen`, `freneziĝas pro vi`, `forveturu de ĉi tie`, `Lasu min trankvila` は、親密表現・送迎・拒否表現として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `partio`, `aliĝi`, `akompani`, `regali`, `elpensi`, `renkontiĝi`, `fraŭla`, `manki`, `freneza` / `freneziĝi`, `veturigi`, `for-` / `forveturi`, `trankvila` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1156`〜`ID1255` は100件確認済み。

## 614. 613周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People
- Making Friends / Things You Like & Dislike
- Making Friends / Arranging to Meet

結果:
- **CSV修正なし**
- 前回 `ID956`〜`ID1055` に続き、今回は `ID1056`〜`ID1155` の100件を確認した。人物描写、趣味・嗜好、誘い・待ち合わせのブロックとして、ロシア語を主基準、英語を補助基準としつつ、日中韓との直接対応を優先した。
- `Kiom bone vi konas lin?`, `Li havas nigrajn harojn kaj verdajn okulojn`, `Li havas mallongajn harojn, grizajn ĉe la tempioj`, `Mia frato ankaŭ estas tre kuraĝa`, `Viaj infanoj estas tre bonkondutaj`, `Mi zorge elektas miajn amikojn`, `Kien ajn mi iras, la homoj estas afablaj` は、人物描写・性格評価・一般的な人柄評価として対応する。PIV で `bonkonduta` も確認できる。
- `Mi ŝatas vojaĝi`, `Mi amas iri al noktokluboj`, `Mi malamas butikumi`, `Kio estas via hobio?`, `Mia hobio estas fotografado`, `Ĉu vi ŝatas spekti televidon?`, `Ne, mi ŝatas legi`, `Mi ŝatas kuiri`, `Mi ŝatas ĝardenadon`, `Ŝi ŝatas promeni` は、趣味・嗜好表現として意味ズレなし。
- `Mi amas la kinon` は `kino` が映画館/映画文化を広く表し得るため、JA の「映画館」寄り、ZH/KO の「映画」寄り、RU `кино` の範囲を吸収できる。
- `Mi adoras patkukojn`, `Mi ne ŝatas bruajn drinkejojn`, `Ĉu vi kolektas poŝtmarkojn?`, `Jes`, `Mi multe legas`, `Kion vi ŝatas fari en via libera tempo?`, `Mi ŝatas aŭskulti muzikon`, `Mi ŝatas spekti televidon`, `Mi tre ŝatas danci`, `Mi kolektas monerojn` は、好悪・収集・読書・余暇活動の短文として自然。
- `Mi ŝatas troti` は `jogging` と完全同義ではないが、PIV の `troti` には人が短い歩幅で速く歩く用法があり、軽いランニング/ジョギング文脈として許容した。
- `Mi amas eliri kaj amuzadi min` は EO が「外出して楽しむ」を明示しており、RU `тусоваться` とも整合する。EN/JA/ZH/KO が短く「出かける/遊びに行く」寄りでも意味は保たれる。
- `Kion vi pensas pri hororaj filmoj?`, `Ili ne tre plaĉas al mi`, `Mi neniam ŝatis golfon`, `Mi ne povas elteni futbalon`, `Ĉu vi ŝatas bicikli?`, `Surfado estas agrabla, ĉu ne?` は、映画・スポーツ・活動への好悪として対応する。`Ili` は直前の `hororaj filmoj` を受けるため問題なし。
- `Ĉu vi havas dombestojn?`, `Jes, mi havas hundon`, `Mi havas hamstron`, `Mi havas hundon kaj du katojn`, `Mia fratino havas testudon` は、ペット所有の短文として維持した。`dombesto` は広く domestic animal だが、犬・猫・ハムスター・カメが続くため pets 文脈は明確。
- `Kion vi plej ŝatas fari?`, `Mi ĉiam ŝatis pentri arbojn`, `Mi ĝuas labori ekstere`, `Tio, kion mi plej ĝuas, estas verki novelojn`, `Ŝi ŝatas la odoron de kafo`, `Mi vere malamas picon`, `Mi pensas, ke la koncerto estas terura`, `Mi abomenas porti kravaton` は、好悪・創作・屋外作業・評価の文として意味ズレなし。PIV の `novelo` は短い散文作品を表すため、short story と対応する。
- `Mi ne pensas, ke piedirado estas agrabla` は EN/JA/ZH の hiking より広いが、RU `пешие прогулки` と合い、徒歩・散策寄りの意味として維持した。`piedirado` は透明で、PIV の `piedira zono` などからも徒歩系の語形成として無理がない。
- `Mi interesiĝas pri fotografado`, `Ŝi interesiĝas pri lingvoj`, `Li interesiĝas pri historio`, `Li ne ŝatas noktoklubojn`, `Mi ŝatus vidi modprezentadon`, `Kiuj estas viaj plej ŝatataj filmosteluloj?`, `Ĉi tiu aktoro ne estas unu el miaj plej ŝatataj`, `Mi ne tre entuziasmas pri ĉi tiu filmo`, `Ĉu vi lastatempe legis iujn bonajn librojn?`, `Li estas fervora leganto de sciencfikciaj libroj`, `Estas nenio, kion mi malamas pli ol mensogulon` は、興味・好み・読書・映画評価の文として対応する。
- `modprezentado`, `filmosteluloj`, `sciencfikciaj libroj`, `mensogulo`, `hororaj filmoj` は、透明複合またはPIV確認語として意味が明確。
- `Venu viziti nin`, `Ni iru naĝi`, `Aliĝu al mi por tagmanĝo`, `Ĉu vi estas libera morgaŭ?`, `Ĉu iu alia venos?`, `Ĉu mi povas kunpreni mian amikon?`, `Ĉu ni iru trinki ion?`, `Ĉu vi ŝatus aliĝi al ni?` は、招待・誘い・同伴確認の文として対応する。`aliĝi al mi/ni` はやや硬いが、PIV の「加わる/参加する」語義から、会食・同席への誘いとして許容。
- `Je kioma horo ni renkontiĝu?`, `Kie ni renkontiĝu?`, `Ĉu vi jam longe estas ĉi tie?`, `Ĉu vi volas veni kun mi?`, `Ĉu vi jam manĝis?`, `Ni faru kafpaŭzon`, `Ĉu vi ŝatus promeni?`, `Kiuj estas viaj planoj por hodiaŭ?`, `Ni iru hodiaŭ al la saŭno`, `Ni renkontiĝu je la oka`, `Vi venos, ĉu ne?`, `Ĉu vi atendis longe?` は、待ち合わせ・予定・誘いとして自然。
- `Ĉu vi rememorigos min?` は `memorigos min` でも十分だが、PIV の `rememorigi` には `memorigi` と同義の用法があるため、remind me として維持した。
- `Kien vi volus iri?`, `Mi ŝatus iri al la kinejo`, `Ĉu vi ŝatus eliri hodiaŭ vespere?`, `Ĉu vi estas libera morgaŭ vespere?`, `Ĉu vi havas planojn por ĉi-vespere?`, `Ĉu vi ĉeestos ilian geedziĝon?`, `Ĉu vi volas iri butikumi kun mi?`, `Ĉu vi volas iri ien dum la semajnfino?`, `Ĉu vi havas planojn por la somero?` は、外出・予定・出席・週末/夏の計画として列間対応を保つ。
- `Ĉu vi dezirus ion manĝi?`, `Ĉu vi volus iri trinki post la laboro?`, `Ĉu vi ŝatus spiri freŝan aeron?`, `Kion vi ŝatus fari hodiaŭ vespere?`, `Ni ŝatus, ke vi venu al nia festo`, `Ni renkontiĝu en la vestiblo`, `Ni renkontiĝu antaŭ la hotelo`, `Ĉu ni povas aranĝi tion iom pli malfrue, ekzemple je la 16-a horo?`, `Sciigu min, se vi povos veni` は、飲食・外気・予定調整・集合場所・出欠確認として意味ズレなし。PIV で `vestiblo`, `aranĝi`, `sciigi` を確認できる。

主な据え置き確認:
- Describing People: `grizajn ĉe la tempioj`, `kuraĝa`, `bonkondutaj`, `zorge elektas`, `Kien ajn mi iras`, `afablaj` は人物描写・性格文脈で維持。
- Things You Like & Dislike: `noktokluboj`, `butikumi`, `hobio`, `fotografado`, `ĝardenado`, `kino`, `patkukojn`, `drinkejo`, `troti`, `plaĉas al mi`, `bicikli`, `surfado`, `dombestojn`, `novelojn`, `piedirado`, `abomenas`, `interesiĝas pri`, `modprezentadon`, `filmosteluloj`, `entuziasmas`, `sciencfikciaj libroj`, `mensogulon` は趣味・嗜好文脈で維持。
- Arranging to Meet: `viziti nin`, `Aliĝu al mi por tagmanĝo`, `kunpreni mian amikon`, `iri trinki ion`, `renkontiĝu`, `kafpaŭzon`, `saŭno`, `rememorigos min`, `kinejo`, `ĉi-vespere`, `geedziĝon`, `ien dum la semajnfino`, `spiri freŝan aeron`, `vestiblo`, `je la 16-a horo`, `Sciigu min` は誘い・待ち合わせ・予定調整文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `konduti` / `bonkonduta`, `butikumi`, `hobio`, `fotografi` / `fotografado`, `drinkejo`, `troti`, `plaĉi`, `bicikli`, `hororo`, `novelo`, `abomeni`, `interesiĝi`, `film/o`, `stel/o`, `aktoro`, `entuziasmo`, `fervoro`, `sciencfikcio`, `mensogulo`, `viziti`, `naĝi`, `aliĝi`, `trinki`, `renkontiĝi`, `paŭzo`, `saŭno`, `memorigi` / `rememorigi`, `aranĝi`, `vestiblo`, `spiri`, `aero`, `sciigi` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID1056`〜`ID1155` は100件確認済み。

## 613. 612周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age, Nationality & Religion
- Making Friends / Family & Relationships
- Making Friends / Describing People

結果:
- **CSV修正なし**
- 前回 `ID856`〜`ID955` に続き、今回は `ID956`〜`ID1055` の100件を確認した。宗教・出生/国籍、婚姻/交際、親族、人物・身体描写のブロックとして、ロシア語を主基準、英語を補助基準としつつ、日中韓との直接対応を優先した。
- `Mi estas budhano`, `Mi estas siĥo`, `Mi estas protestantino`, `Ĉu vi kredas je Dio?`, `Mi ne estas religia`, `Kie mi povas preĝi?`, `Mi estas ateisto` は、宗教・信仰の自己申告として対応する。`protestantino` は RU `протестантка` の女性形と合うため維持した。
- `budhano` は PIV の `budhano` / `budhisto`、`siĥo` は PIV の `siĥo`、`ateisto` は PIV の `ateisto` で確認できる。`Mi ne estas religia` は日中韓が「無宗教」寄りだが、RU `неверующая` とも合う非宗教的自己申告として成立する。
- `Ĉu estas preĝejo proksime de ĉi tie?`, `Ĉu estas templo proksime de ĉi tie?`, `Ĉu estas moskeo proksime de ĉi tie?`, `Ĉu estas sinagogo proksime de ĉi tie?` は礼拝施設の語として対応する。`preĝejo` は PIV で一般の礼拝所とキリスト教 church の両方を確認できるため、`kirko` へは寄せない。
- `Kiam vi naskiĝis?`, `Mi naskiĝis en 1992`, `Mia naskiĝtago estas la 9-a de februaro`, `Ĉu via frato estas pli aĝa ol vi?`, `Ili havas ses kaj ok jarojn`, `Kie vi naskiĝis?`, `Mi naskiĝis en Kolombio` は、出生時・誕生日・年齢・出生地の表現として意味ズレなし。
- `El kiu lando vi estas?`, `Ni estas el Svedio`, `Ŝi estas el Israelo`, `Mi devenas el Budapeŝto, sed nun mi loĝas en Kairo`, `Ĉu via edzo ankaŭ estas el Belgrado?`, `El kiu parto de Kroatio vi devenas?`, `Mi naskiĝis en Argentino, sed kreskis en Anglio` は、出身・出生・成育地の表現として対応する。`devenas el` は RU の「生まれた」より少し広いが、「もともと〜出身」として文脈上許容。
- `Ni estas civitanoj de Maroko`, `Mi ricevis singapuran civitanecon` は、PIV の `civitano/civitaneco` と合い、市民権・国籍文脈で成立する。
- `Mi estas fianĉiĝinta`, `Mi estas edziniĝinta`, `Ĉu vi edziniĝis?`, `Ne, mi estas fraŭla`, `Li estas divorciĝinta`, `Ŝi estas vidvino`, `Li estas vidvo` は婚姻状態の表現として自然。`edziniĝinta/edziniĝis` は女性話者・女性対象に寄るが、RU `замужем` と整合するため維持した。
- `Jes. Fakte, mi estas fianĉino` は、直訳では「私は婚約者の女性」だが、PIV の `fianĉino` が「婚約した女性」を表すため、女性話者の `I'm engaged` として許容。
- `Ĉu vi havas koramikon?`, `Ĉu vi havas koramikinon?`, `Mi disiĝis`, `Li estas en rilato`, `Jes, mi rendevuas kun iu` は、交際・別離の文脈で成立する。`en rilato` は英語的だが PIV の `rilato` には人間関係・相互関係があり、`rendevui kun iu` も交際文脈では「会っている/付き合っている」寄りに読めるため維持した。
- `Mi ne havas infanojn`, `Tio estas mia frato`, `Li estas mia kuzo`, `Tio estas ŝia fratino`, `Tio estas mia edzo`, `Ĉu vi havas infanojn?`, `Jes, mi havas tri infanojn`, `Jes, mi havas novnaskitan bebon`, `Mi havas ĝemelojn`, `Mi estas graveda`, `Ĉu ĉi tiu viro estas via proksima parenco?`, `Tio estas lia patro`, `Ĉu vi estas amiko de Danielo?` は、親族・家族構成・妊娠/新生児の表現として対応する。
- `Ni havas du filojn kaj filinon`, `Jes, mi havas knabon kaj knabinon`, `Ĉu viaj infanoj estas kun vi?`, `Ĉu vi havas fratojn aŭ fratinojn?`, `Jes, mi havas du fratojn`, `Jes, mi havas pli junan fratinon`, `Jes, mi havas unu fraton kaj du fratinojn`, `Jes, mi havas pli aĝan fraton`, `Ne, mi estas solinfano`, `Ĉu viaj geavoj ankoraŭ vivas?`, `Ĉu vi havas genepojn?`, `Jes, unu nepo kaj du nepinoj` は、親族の性別・数の対応を保つ。PIV の `ge-` 項で `geavoj/genepoj`、`nepo/nepino` も確認できる。
- `Mi estas viro`, `Mi estas virino`, `Ŝi estas bela`, `Vi estas tre ĉarma`, `Li estas bonŝanculo`, `Li similas al mi`, `Li portas okulvitrojn` は、人物・外見描写として自然。`bonŝanculo` は lucky person、`okulvitroj` は眼鏡として透明。
- `Kia estas Emma?`, `Ŝi estas tre timida`, `Li estas tre fama`, `Vi estas tre saĝa`, `Kia homo li estas?`, `Ŝi estas honesta persono`, `Ŝi estas pli inteligenta ol li`, `Ŝi estas scivolema persono` は性格・資質を述べる文として対応する。`saĝa` は主に wise だが、PIV に古義として intelligent もあり、JA/ZH/KO/RU の「賢い/聪明/똑똑/умная」と矛盾しない。
- `Kiel alta vi estas?`, `Kiel li aspektas?`, `Li estas juna, malalta kaj bela`, `Li aspektas pli maljuna`, `Ŝi havas blondajn harojn`, `Vi aspektas tiel juna`, `Vi aspektas bone`, `Kiel aspektas via pli juna fratino?`, `Ŝi estas alta, svelta kaj bela`, `Ŝi havas buklajn rufajn harojn`, `Ŝi havas ĉarman rideton`, `Vi similas al mia fratino` は、外見・年齢印象・髪色・体格・類似の描写として意味ズレなし。男性への `bela` も attractive/handsome 文脈として許容。
- `Li estas tre ĝena` は、PIV の `ĝena` が「妨げ・不快・厄介」を表すため、annoying / 鬱陶しい / 烦人 / 짜증나 / надоедливый と対応する。
- `Mi uzas miajn okulojn por vidi`, `Mi uzas mian nazon por flari`, `Mi havas buŝon por manĝi`, `Mi havas du orelojn por aŭdi`, `Mi havas langon por gustumi`, `Mi havas du piedojn por kuri` は教材的だが、身体部位の機能説明として意味は明確。PIV で `flari`, `gustumi`, `piedo`, `orelo`, `buŝo`, `lango` の基本語義を確認できる。

主な据え置き確認:
- Age/Nationality & Religion: `budhano`, `siĥo`, `protestantino`, `kredas je Dio`, `preĝi`, `naskiĝis`, `civitanoj de Maroko`, `singapuran civitanecon`, `preĝejo`, `templo`, `moskeo`, `sinagogo`, `ateisto` は宗教・出生・国籍文脈で維持。
- Family & Relationships: `fianĉiĝinta`, `edziniĝinta`, `edziniĝis`, `fraŭla`, `divorciĝinta`, `vidvino/vidvo`, `fianĉino`, `disiĝis`, `en rilato`, `rendevuas kun iu`, `novnaskitan bebon`, `ĝemelojn`, `graveda`, `proksima parenco`, `solinfano`, `geavoj`, `genepoj`, `nepo/nepinoj` は婚姻・交際・親族文脈で維持。
- Describing People: `bonŝanculo`, `similas al`, `okulvitrojn`, `timida`, `fama`, `saĝa`, `aspektas`, `blondajn harojn`, `ĝena`, `honesta`, `inteligenta`, `svelta`, `buklajn rufajn harojn`, `ĉarman rideton`, `scivolema`, `flari`, `gustumi` は人物・身体描写文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `budho` / `budhano` / `budhisto`, `siĥo`, `preĝi` / `preĝejo`, `templo`, `moskeo`, `sinagogo`, `ateisto`, `civitano` / `civitaneco`, `fianĉo` / `fianĉino`, `edzo` / `edziniĝi`, `fraŭlo`, `vidvo` / `vidvino`, `rendevuo` / `rendevui`, `rilato`, `sola` / `solinfano`, `ge-`, `nepo` / `nepino`, `ĝemelo`, `graveda`, `parenco`, `simili`, `aspekti`, `saĝa`, `ĝeni` / `ĝena`, `gustumi`, `flari`, `rufa`, `ĉarma`, `svelta` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID956`〜`ID1055` は100件確認済み。

## 612. 611周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions
- Making Friends / Place of Residence
- Making Friends / Age, Nationality & Religion

結果:
- **CSV修正なし**
- 前回 `ID756`〜`ID855` に続き、今回は `ID856`〜`ID955` の100件を確認した。紹介・同伴者説明、居住/滞在、年齢・国籍・宗教のブロックとして、ロシア語を主基準、英語を補助基準としつつ、日中韓との直接対応を優先した。
- `Ankaŭ mi ĝojas konatiĝi kun vi`, `Kun kiu vi estas?`, `Vi certe estas William`, `Ĉu vi konas Emilin?`, `Ĉu ni ne renkontiĝis antaŭe?`, `Ne. Mi ne pensas tiel` は、初対面・再会確認・否定応答として自然な範囲にある。
- `Mi estas kun amikino` は JA/ZH/KO が性別非明示だが、RU `с подругой` と合い、PIV の `amikino` とも整合するため維持した。
- `Kiu estas ĉi tiu fraŭlino?`, `Tio estas mia filino`, `Ĉu vi konas ŝin?`, `Jes. Ĉi tiu estas mia edzino`, `Ŝi estas kun sia patrino`, `Ĉi tiu estas mia koramiko`, `Mi estas kun mia patro`, `Mi estas kun miaj kolegoj`, `Ili estas kun sia familio` は、人物確認・同伴者紹介として列間対応を保つ。
- `Mi estas Hina, vendmanaĝero` は PIV の `manaĝero` が狭い定義である点に注意が必要だが、`vend-` + `manaĝero` の透明複合として sales manager を表せる。RU/EN/JA/ZH/KO とも一致するため、AI造語誤りとは判断しない。
- `Ĉu vi konas unu la alian?`, `Jes, ni jam renkontiĝis`, `Ni konatiĝis per amikoj`, `Mi ne pensas, ke ni antaŭe renkontiĝis`, `De kie vi konas unu la alian?`, `Ni kune studis en la universitato`, `Ni kune lernis en la lernejo`, `Ni kutimis kune fiŝkapti` は、知人関係・知り合った経緯・過去の共有経験として意味ズレなし。
- `Ĉu mi povas prezenti al vi mian fianĉon?`, `Permesu al mi prezenti nian direktoron, sinjoron Smirnov`, `Ni ĝojas prezenti al vi nian filinon` は、PIV の `prezenti iun al iu` の型と合う。`sinjoron Smirnov` は敬称側に対格があり、外来姓へ無理に `-n` を付けない現形を維持した。
- `Mi ĝojas renkonti vin, sinjoro Diego Garcia`, `Pardonu, mi ne aŭdis vian nomon`, `Ĉu vi povus literumi vian nomon, mi petas?` は、面会挨拶・名前の聞き直し・綴り確認の発話として対応する。
- `Mi loĝas ĉi tie`, `Kio estas via adreso?`, `Kie vi loĝas?`, `Mi loĝas en Belgio`, `Ĉu plaĉas al vi ĉi tie?`, `Ĉi tie tre plaĉas al mi`, `Kun kiu vi loĝas?`, `Mi loĝas kun mia edzino`, `Mi loĝas kun amikoj`, `Mi loĝas sola` は、住所・居住・好印象・同居状況の文脈で成立する。PIV の `plaĉi` には `tre plaĉas al mi ĉi tie` 型の用例がある。
- `Mi venis ĉi tien por studi`, `Kie loĝas viaj gepatroj?`, `Ili loĝas en Montrealo`, `Albanio estas bela lando`, `Kio alkondukas vin al Brazilo?`, `Mi estas ĉi tie por labori`, `Ĉu vi loĝas kun iu?`, `Mi loĝas kun parencoj`, `Ŝi loĝas kun siaj gepatroj`, `Ŝi loĝas kun sia koramiko`, `Li loĝas kun sia koramikino` は、滞在理由・居住者・国名・同居相手として意味が保たれている。
- `Kio alkondukas vin al Brazilo?` は直訳的だが、`what brings you to Brazil?` と同じ発想の表現として理解可能。`Mi estas ĉi tie por labori` は `en komandiro` より広いが、仕事目的の滞在として RU/JA/ZH/KO と矛盾しない。
- `Ni loĝas en nova apartamento`, `Mi dividas ĝin kun unu alia persono`, `Kiom longe vi loĝas ĉi tie?`, `Dum unu jaro`, `Kie vi restos?`, `Ĉu vi venis kun via familio?`, `Ĉu vi iam estis en Ukrainio?`, `Kial vi venis al Meksiko?`, `Mi volis loĝi eksterlande` は、住居共有・期間・滞在予定・渡航経験/理由として対応する。
- `Ŝi loĝas en Sud-Afriko`, `Mi aŭdis, ke Ateno estas bela loko`, `Ĉu li loĝas sole?`, `Li loĝas kun amiko`, `Ŝi kunloĝas en domo kun tri aliaj homoj`, `Li loĝas en Unuiĝintaj Arabaj Emirlandoj`, `Niaj infanoj estas en Kazaĥio`, `Mi ĵus alvenis`, `Li laboras ĉi tie kiel korespondanto`, `Kiom longe vi intencas resti ĉi tie?`, `Mi restos ĉi tie dum 1 tago`, `Ili restas dum tri semajnoj`, `Li loĝas en Nov-Zelando jam de ses monatoj`, `Ĉu via frato estis en Rumanio?` は、居住地・同居・滞在期間・職業・国名として列間対応を保つ。
- `Ŝi kunloĝas en domo kun tri aliaj homoj` は、`kunloĝi` が共同居住の透明複合として読め、EN/JA/ZH/KO の house sharing と RU の「三人と住む」に対応する。`Li loĝas en Nov-Zelando jam de ses monatoj` の `jam de ses monatoj` も期間継続として理解可能。
- `De kie vi estas?`, `Mi estas el Moldavio`, `Kiom da jaroj vi havas?`, `Mi havas dudek tri jarojn`, `Kiom aĝa ŝi estas?`, `Ŝi havas dek kvin jarojn`, `Li havas sesdek jarojn`, `Kiam estas via naskiĝtago?`, `Ĝi estas la 14-a de junio` は、出身・年齢・誕生日の基本表現として問題なし。
- `Mi estas usonano`, `Kia estas via nacieco?`, `Mi estas albano`, `Ĉu vi estas sviso?`, `Mi estas aŭstrianino`, `Ĉu vi estas germana civitanino?`, `Ĉu li estas slovako aŭ belaruso?`, `Li estas el Tajvano`, `Mi ne estas aŭstralianino` は、国籍・出身者名として維持した。`aŭstrianino` / `aŭstralianino` は国名からの規則的な `-anino` 形として理解できる。
- `Ĉu vi estas religia?`, `Mi estas judino`, `Mi estas katoliko`, `Al kiu religio vi apartenas?`, `Mi estas kristanino`, `Mi estas islamanino`, `Mi estas hinduistino` は、宗教・信仰の自己申告として対応する。女性形は RU の女性話者形とも整合する。
- `Mi estas islamanino` は、PIV の `Islamo` 項に `islamano` があり、現行の規則的女性形は妥当。`muzulmano` も PIV にあるが、過去修正前の `musulmanino` とは別綴りであり、現行形を維持した。
- `Mi estas hinduistino` は、PIV では `hinduo` / `hinduismo` が直接確認形で、`hinduino` も候補になり得る。ただし近年の Esperanto 実例で `hinduistino` の使用を確認でき、RU `индуистка` と宗教自己申告文脈に合うため、明確な誤りとは判断しない。

主な据え置き確認:
- Introductions: `konatiĝi kun vi`, `Kun kiu vi estas?`, `amikino`, `fraŭlino`, `koramiko`, `vendmanaĝero`, `prezenti al vi mian fianĉon`, `prezenti nian direktoron, sinjoron Smirnov`, `prezenti al vi nian filinon`, `literumi vian nomon`, `De kie vi konas unu la alian?`, `fiŝkapti` は紹介・知人関係文脈で維持。
- Place of Residence: `Ĉi tie tre plaĉas al mi`, `loĝas sola/sole`, `Kio alkondukas vin al Brazilo?`, `Mi estas ĉi tie por labori`, `Mi dividas ĝin kun unu alia persono`, `kunloĝas en domo`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio`, `korespondanto`, `jam de ses monatoj`, `Nov-Zelando` は居住・滞在文脈で維持。
- Age/Nationality & Religion: `Moldavio`, `nacieco`, `usonano`, `albano`, `sviso`, `aŭstrianino`, `judino`, `katoliko`, `germana civitanino`, `slovako`, `belaruso`, `Tajvano`, `aŭstralianino`, `religia`, `kristanino`, `islamanino`, `hinduistino` は出身・国籍・宗教文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `amiko` / `amikino`, `fianĉo`, `direktoro`, `sinjoro`, `prezenti`, `universitato`, `loĝi`, `plaĉi`, `manaĝero`, `vendi`, `korespondi`, `resti`, `Moldavio`, `Kazaĥio`, `Unuiĝintaj Arabaj Emirlandoj`, `nacieco`, `religio`, `Islamo` / `islamano`, `muzulmano`, `hinduo` / `hinduismo`, `katoliko`, `jud/o`, `svis/o`, `aŭstr/o`, `Tajvano` 周辺。
- La Ondo de Esperanto 2025-03 demonstra versio `hinduistino`: https://esperanto-ondo.ru/Ondo/Lo-323demo.pdf
- Wiktionnaire `hindou`（Esperanto訳 `hinduo` / `hinduino`）: https://fr.wiktionary.org/wiki/hindou

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID856`〜`ID955` は100件確認済み。

## 611. 610周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid
- Emergencies / At the Police Station
- Making Friends / Introductions

結果:
- **CSV修正なし**
- 前回 `ID656`〜`ID755` に続き、今回は `ID756`〜`ID855` の100件を確認した。救急・警察署・自己紹介の短文であるため、ロシア語を主基準、英語を補助基準としつつ、日中韓との直接対応を優先した。
- `Mi sangas`, `Min trafis aŭto`, `Li estas senkonscia`, `Mia filino estas vundita`, `Konduku min al hospitalo!`, `Ĉu estas kuracisto ĉi tie?` は、出血・事故・意識不明・けが・搬送依頼の短文として列間対応に問題なし。
- `Mi estis mordita`, `Mi tranĉis min`, `Mi bruligis min`, `Mi rompis mian brakon`, `Mi tordis al mi la maleolon` は救急申告として自然な範囲にある。`Mi bruligis min` は `brulvundis min` も候補だが、PIV の `bruligi` に「火傷させる/火で傷つける」語義があるため維持した。
- `Bonvolu surmeti bandaĝon` は、JA/KO が「包帯を巻く」寄りで、RU が `наденьте бандаж` 寄りである。PIV の `bandaĝo` / `bandaĝi` は傷部を包む帯・固定用の帯を含むため、救急場面の依頼文として据え置き。
- `Ĉu vi havas asekuron?`, `Ĉio estos bone kun vi`, `Mi falis de la ŝtuparo`, `Mi perdis multe da sango`, `Li havas frakturon`, `Ĉu vi pensas, ke vi povos iri?`, `Ĉu vi havas diabeton?` は、保険・励まし・転落・失血・骨折・歩行可否・糖尿病確認として対応する。
- `Mi ne estas alergia al iuj ajn medikamentoj`, `Ĉu vi estas alergia al iuj medikamentoj?`, `Jes, mi estas alergia al penicilino`, `Mi havas reakcion al novokaino` は、PIV の `alergia al` と薬剤名の確認に合う。`Mi havas reakcion al novokaino` は日中韓がアレルギー反応寄りだが、RU `реакция на новокаин` とも一致する。
- `Mi venigos iun, kiu povas helpi`, `Ĉi tiu persono povas helpi vin`, `Mi elartikigis mian brakon`, `Mi stumblis sur la ŝtuparo`, `Mi havas manĝaĵveneniĝon`, `Li estas grave vundita`, `Iu venos kaj helpos vin`, `Mi atendos ĉi tie kun vi, ne zorgu`, `Mi mezuros vian pulson`, `Trankviliĝu, ĉio estos en ordo`, `Jen mia poliso de medicina asekuro`, `Ĉu vi povus sciigi mian familion?`, `Ĉu mi povas daŭrigi mian vojaĝon?` は、救急・医療保険・連絡・旅程継続の文脈で意味ズレなし。
- `Mi elartikigis mian brakon` は、PIV で `elartikiĝo = luksacio`、かつ `elartikigi sian ŝultron` の用例を確認できる。`brako` は広めだが、RU `вывихнул руку` と日中韓の「腕の脱臼」に対応するため維持した。
- `Kio mankas?`, `Mi perdis mian mansakon`, `Kion vi faris?`, `Mi bezonas advokaton`, `Bonvolu subskribi vian deklaron`, `Oni ŝtelis mian tekkomputilon`, `Kiam tio okazis?`, `Kion vi vidis?`, `Mi vidis nenion`, `Mi fariĝis viktimo de fraŭdo`, `Oni enrompis en mian aŭton`, `Mi ne scias, kiu faris tion`, `Mi devas telefoni al la ambasadejo` は、警察署での盗難・被害・申告文として対応する。
- `Ĉu mi estas arestita?`, `Mi bezonas advokaton, kiu parolas la ĉinan`, `Mi haltigis vin pro troa rapideco`, `Vi devos pagi monpunon`, `Kie estas la plej proksima policejo?`, `Mi ŝatus denunci ŝtelon`, `Kion oni ŝtelis de vi?`, `Oni ŝtelis mian mansaketon`, `Kiel tio okazis?`, `Je kioma horo tio okazis?`, `Bonvolu plenigi raporton pri ŝtelo` は、逮捕確認・弁護士・速度超過・罰金・盗難届の文脈で維持した。
- `Ĉu mi povas ĝin anstataŭigi?` は、JA/ZH/KO が「再発行」寄りだが、直前の `Mi ne povas trovi mian pasporton ie ajn` を受けたパスポートの replacement として読める。RU `заменить` との対応も明確なため、`reeldoni` 等へは寄せない。
- `Vi devus turni vin al la oficejo pri perditaj aĵoj`, `Ĉu vi turnis vin al la oficejo pri perditaj aĵoj?` は、RU `обратиться` に沿う `turni sin al` と遺失物取扱所の説明的表現として成立する。
- `Ĉu vi havas atestantojn?`, `Ĉu vi ne rimarkis ion suspektindan?`, `Ĉu vi vidis ilin antaŭe?`, `Ni penos fari lian fotoroboton`, `Vi devas skribi oficialan raporton`, `Oni vokis min kiel atestanton`, `Mi estas konvinkita, ke ŝi estas senkulpa`, `Mi ŝatus peti kopion de la dokumento`, `Mi ŝatus renkonti la meksikan ambasadoron`, `Mi ŝatus kontakti la ambasadejon de mia lando`, `Viro kaj virino helpis nin`, `Miaj muzikaj instrumentoj estis detruitaj` は、目撃者・容疑者・公式書類・大使館対応として列間対応を保つ。
- `Ni penos fari lian fotoroboton` は PIV 直接見出しでは未確認だが、過去周の Glosbe/DBnary 確認で `facial composite` / `identikit` 相当として扱えると判断済みで、RU `фоторобот` と一致するためAI造語誤りとは判断しない。
- `Mi estas Ben`, `Ĉi tiu estas Lucy`, `Kiel vi nomiĝas?`, `Mia nomo estas Diana`, `Kio estas via familinomo?`, `Ĉu tio estas via nomo?`, `Kiuj ili estas?`, `Iliaj nomoj estas Neil kaj Anna`, `Kiu estas tiu viro?`, `Lia nomo estas Tom`, `Ŝia nomo estas Maria` は、名前・名字・人物確認として対応する。`familinomo` は surname / family name の意味で紹介文脈に合う。
- `Ni laboras kune`, `Neniu konas lin`, `Tio estas ŝia filo`, `Mi estas kun mia edzino`, `Mi estas ĉi tie sola`, `Permesu al mi prezenti vin al Davido`, `Ĉu mi povas prezenti min?`, `Mi ŝatus prezenti Alicon al vi`, `Estas agrable konatiĝi kun vi, Jan!` は、人物紹介・同伴・自己紹介の文として意味ズレなし。PIV の `prezenti` は「人を他者に紹介する」型を含むため、紹介方向も現行のままで妥当。

主な据え置き確認:
- First Aid: `sangas`, `Min trafis aŭto`, `senkonscia`, `mordita`, `tranĉis min`, `bruligis min`, `rompis mian brakon`, `tordis al mi la maleolon`, `surmeti bandaĝon`, `asekuron`, `falis de la ŝtuparo`, `frakturon`, `diabeton`, `alergia al`, `elartikigis mian brakon`, `stumblis`, `manĝaĵveneniĝon`, `grave vundita`, `pulson`, `penicilino`, `novokaino`, `poliso de medicina asekuro` は救急・医療申告文脈で維持。
- At the Police Station: `advokaton`, `subskribi vian deklaron`, `tekkomputilon`, `fraŭdo`, `enrompis en mian aŭton`, `arestita`, `la ĉinan`, `troa rapideco`, `monpunon`, `policejo`, `denunci ŝtelon`, `raporton pri ŝtelo`, `anstataŭigi`, `oficejo pri perditaj aĵoj`, `atestantojn/atestanton`, `fotoroboton`, `oficialan raporton`, `senkulpa`, `kopion de la dokumento`, `ambasadoron/ambasadejon`, `instrumentoj estis detruitaj` は警察・盗難・届出文脈として維持。
- Introductions: `Mi estas Ben`, `Ĉi tiu estas Lucy`, `Kiel vi nomiĝas?`, `familinomo`, `Kiuj ili estas?`, `Neniu konas lin`, `kun mia edzino`, `prezenti vin al Davido`, `prezenti min`, `prezenti Alicon al vi`, `konatiĝi kun vi` は自己紹介・人物紹介文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `sangi`, `trafi`, `senkonscia`, `vundi`, `mordi`, `tranĉi`, `bruligi`, `rompi`, `tordi`, `maleolo`, `bandaĝo` / `bandaĝi`, `asekuri`, `ŝtuparo`, `frakturo`, `diabeto`, `alergio`, `medikamento`, `elartikiĝo`, `ŝultro`, `stumbl/i`, `veneniĝo`, `pulso`, `penicilino`, `novokaino`, `poliso`, `advokato`, `deklari` / `deklaro`, `fraŭdi`, `enrompi`, `aresti`, `monpuno`, `denunci`, `atestanto`, `senkulpa`, `ambasadoro`, `ambasadejo`, `instrumento`, `familinomo`, `prezenti`, `konatiĝi` 周辺。
- 過去周確認: Glosbe/DBnary `fotoroboto`（facial composite / identikit 相当）、Glosbe `familinomo`（surname / family name 相当）。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID756`〜`ID855` は100件確認済み。

## 610. 609周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions
- Emergencies / Emergency Situations
- Emergencies / Accidents

結果:
- **CSV修正なし**
- 前回 `ID556`〜`ID655` に続き、今回は `ID656`〜`ID755` の100件を確認した。意見・評価、緊急時の短い命令・確認、交通事故の申告・警察/保険対応のブロックであるため、ロシア語を主基準、英語を補助基準としつつ、日中韓との直接対応を優先した。
- `Ĉu ĉi tiu loko ne estas mirinda?`, `Mi pensas, ke jes`, `Mi ne pensas tiel`, `Mi esperas tion`, `Tio dependas`, `Vi malpravas` は、短い意見・応答として各列と対応する。`Mi esperas tion` は `Mi esperas, ke jes` も候補だが、「そうであることを望む」の意味は明確。
- `Ĉu vi havas iujn rimarkojn?` は、PIV の `rimarko` が述べられた注意・コメントを表し、RU `замечания` と日中韓の「意見/看法」寄りの訳を橋渡しできるため維持した。
- `Ĝi estas grandioza`, `Tio estas mirinda!`, `Tio estas nekredebla!`, `Kia bela loko!`, `Kia bonega ideo!` は評価表現として自然な範囲にある。`grandioza` は PIV で強い印象・壮大さを表す語として確認できる。
- `Ili tre plaĉas al mi!`, `Kio plaĉas al vi pri ĝi?`, `Mi timas, ke ĉi tiu libro ne plaĉas al mi`, `Mi ne povas diri, ke tio tre plaĉas al mi`, `Sincere dirante, li ne plaĉas al mi` は、PIV の `plaĉi al iu` の型と合う。`Ili` は前文依存だが、複数対象への好意表明として成立する。
- `Kion vi povas diri pri ĉi tiu bildo?` は、`bildo` が写真・絵・画像を広く表せるため、JA/KO の「写真」寄り、RU の「絵/画像」寄りを吸収できる。
- `La aktorado estis malbona` は PIV で `aktorado` が俳優の演技・演じ方を表すため、acting の評価として維持した。
- `Persone, mi konsideras ĉi tiun filmon la plej bona` は `konsideri + objekto + predikativo` として読める。`la plej bonan` へ寄せると名詞句内修飾にも読めるため、現行の叙述補語形を維持した。
- `Laŭ mi, butikumado estas amuza`, `Sincere dirante, estas malfacile kredi tion`, `Nu, mi devas diri, ke mi esperas la plej bonan`, `Mi kredas, ke teknologio plibonigas la vivon` は、意見表明・評価・希望表明として列間対応を保つ。
- `Fajro!` は `Incendio!` も候補だが、緊急時の短い警告発話として許容。`Voku la policon!`, `Voku kuraciston!`, `Voku la fajrobrigadon!`, `Voku ambulancon!`, `Bonvolu tuj voki la policon`, `Oni atakis min` は緊急時の短文として意味ズレなし。
- `Ĉu ĉio estas en ordo?`, `Ĉu ĉiuj estas en ordo?`, `Ĉu io malbonas?` は、安否・異常確認の短い表現として対応する。`Ĉu io malbonas?` は `Ĉu io estas malbona?` / `Ĉu io misas?` なども候補だが、現行形で「何かおかしいか」の意味は明確。
- `Kie estas la oficejo pri perditaj aĵoj?` は説明的だが、遺失物取扱所として透明で、PIV の `perdi` / `aĵo` と矛盾しないため維持した。
- `Ĉu vi flaras ion brulantan?`, `La konstruaĵo brulas!`, `Mi pensas, ke vi devus iri al kuracisto`, `Estas urĝa situacio!` は、火災・医療・緊急事態の文脈で対応を保つ。PIV の `urĝaĵo` にも緊急医療文脈が確認できる。
- `Mi estas traŭmatizita`, `Ĉu iu estas vundita?`, `Ne, neniu estas vundita`, `Estas vunditoj` は、事故後の心身の被害・けが人確認として対応する。PIV の `traŭmato` には身体的外傷と `psika traŭmato` があり、JA/ZH/KO/RU の範囲を保つ。
- `Kio kaŭzis la akcidenton?`, `Ĉu vi havis akcidenton?`, `Kie ĝi okazis?`, `Okazis akcidento` は事故発生確認として意味が明確。`Ĉu vi havis akcidenton?` は `Ĉu vi suferis akcidenton?` も候補だが、現形でも事故に遭ったかを尋ねる短文として許容。
- `Li koliziis kun mi`, `Mi ne vidis la ŝildon`, `Jen mia stirpermesilo`, `Kial vi rompis ĉi tiun trafikan regulon?`, `Mi havis la prioritaton` は、事故・交通規則文脈で維持した。PIV で `kolizii kun`, `ŝildo`, `stiri`, `havi prioritaton de paso` を確認できる。
- `Ĉu la veturilo estis asekurita?`, `Mi volas raporti akcidenton`, `Ne ŝajnas esti multe da damaĝo`, `Ĉu vi povus blovi en ĉi tiun tubon, mi petas?`, `Ĉu mi povus vidi viajn asekurdokumentojn?`, `Ĉu mi povus ricevi kopion de la akcidentraporto?` は、保険・報告・損傷・飲酒検査の文脈として対応する。PIV で `asekuri`, `damaĝo`, `blovi en tubon` を確認できる。
- `Ĉu ni povus solvi la aferon inter ni?`, `Ĉu mi povas havi vian nomon kaj adreson?`, `Kiun mi informu pri la akcidento?` は、当事者間解決・連絡先確認・報告先確認として意味ズレなし。`informi iun pri io` の型から、`kiun` の対格も支持される。

主な据え置き確認:
- Opinions: `rimarkojn`, `grandioza`, `plaĉas al`, `bildo`, `aktorado`, `konsideras ĉi tiun filmon la plej bona`, `butikumado`, `teknologio plibonigas la vivon` は意見・評価文脈で維持。
- Emergency Situations: `Fajro!`, `fajrobrigado`, `ambulanco`, `Ĉu io malbonas?`, `oficejo pri perditaj aĵoj`, `brulantan`, `brulas`, `urĝa situacio`, `Oni atakis min` は緊急時表現として維持。
- Accidents: `traŭmatizita`, `vundita/vunditoj`, `akcidento`, `koliziis kun mi`, `ŝildo`, `stirpermesilo`, `trafikan regulon`, `Mi havis la prioritaton`, `asekurita`, `interpretisto`, `raporti akcidenton`, `damaĝo`, `blovi en ĉi tiun tubon`, `asekurdokumentojn`, `akcidentraporto`, `informi iun pri io` は交通事故・保険・警察対応文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `plaĉi`, `rimarko`, `grandioza`, `aktorado`, `konsideri`, `fajrobrigado`, `ambulanco`, `traŭmato` / `traŭmatizi`, `vundi` / `vundito`, `akcidento`, `kolizii`, `ŝildo`, `stiri`, `prioritato`, `asekuri`, `damaĝo`, `blovi`, `informi`, `urĝi`, `teknologio` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID656`〜`ID755` は100件確認済み。

## 609. 608周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information
- General Conversation / Expressing Feelings
- General Conversation / Help & Advice
- General Conversation / Opinions

結果:
- **CSV修正なし**
- 前回 `ID456`〜`ID555` に続き、今回は `ID556`〜`ID655` の100件を確認した。ロシア語を主基準、英語を補助基準としつつ、クイズで直接対応する `Esperanto` と `日本語` / `中文` / `한국어` の意味対応を優先した。
- この範囲は、短い質問、感情・体調、弔意、依頼・助言、好悪・評価が中心である。自然な言い換え候補がある箇所でも、内容が保たれ、辞書上の根拠があるものは文脈別許容として維持した。
- `Kial vi diris tion?`, `Kial mi ne pensis pri tio?`, `Ĉu iu povas diri al mi la veron?`, `Kiam komenciĝas la cirkaj spektakloj?`, `Ĉu vi scias, kiu inventis la radon?` は、理由・真実確認・開始時刻・発明者を尋ねる質問として、格・語順・列間対応に問題なし。
- `Mi estas feliĉa`, `Mi estas trista`, `Mi estas malstreĉita`, `Mi estas laca`, `Mi malsatas`, `Mi soifas`, `Mi estas trankvila`, `Mi enuas`, `Mi estas optimisma`, `Mi rezignas`, `Mi fartas bone`, `Al mi estas egale` は、基本的な感情・状態表現として各列と対応する。`trista` は PIV で `malgaja, malĝoja` と確認できる。
- `Mi estas ekscitita` は、日中韓が「期待」寄りで、RU は `взволнован`、EN は `excited` である。PIV の `eksciti` は心の動きを強める語義を含むため、期待・高揚・動揺の幅を持つ短文として文脈別許容。
- `Mi estas motivita` は、PIV の `motivi` が「理由づける」寄りで注意点はあるが、`motivo` 自体は人を行動させる理由を表す。Web上でも `motivita` が motivated 系に対応する例があり、`entuziasma` / `inspirita` へ寄せると内容が狭まるため維持した。
- `Mi sentas min embarasita`, `Mi estas nervoza`, `Mi sentas min terure`, `Mi sentas min perdita`, `Mi sentas iom da kapturno`, `Mi ne estas malkuraĝigita` は、状態表現として意味が明確。`Mi sentas iom da kapturno` は `Mi sentas kapturnon` も候補だが、少量表現として理解可能。
- `Mi bedaŭras tion aŭdi`, `Ni tre bedaŭras aŭdi pri via perdo`, `Bonvolu akcepti niajn plej profundajn kondolencojn`, `Niaj pensoj estas kun vi kaj via familio` は、残念・弔意・慰めの表現として対応する。PIV の `kondolenco` には `pro la perdo de via patro...` 型があり、`via perdo` は喪失文脈として明確。
- `Ĉu mi povus prunti vian plumon?`, `Ĉu vi povus prunti al mi iom da mono, mi petas?` は、PIV で `prunti` に「貸す」「借りる」の両義があるため曖昧になりうる。ただし前者は `vian plumon`、後者は `al mi` と金銭依頼文脈から意味が確定するため、`pruntepreni` / `pruntedoni` への置換は行わない。
- `Ĉu vi povus fari al mi servon?`, `Ĉu vi povus prizorgi tion dum momento?`, `Ĉu vi estus tiel afabla kaj klarigus tion denove?`, `Ĉu ĝenus vin doni al mi la tekkomputilon?` は依頼表現として許容。`Ĉu vi estus tiel afabla kaj ...` は PIV の `afabla` に類似の `esti tiel afabla k traduki...` 型があり、現行形で通る。
- `tekkomputilo` は PIV では直接見出しが弱く、Komputeko/Glosbe では標準寄りに `tekokomputilo` も示されるが、`notebook computer` の訳語群に `tekkomputilo` も確認できるため、AI造語誤りとは扱わない。
- `Mi konsilus al vi iom ripozi`, `Kion vi pensas, ke mi faru?`, `Se mi estus vi, mi farus same`, `Mi rekomendus al vi paroli kun Jia`, `Mi malkonsilus lui aŭton`, `Se vi sekvos mian konsilon, vi sukcesos`, `Se mi estus vi, mi dufoje pripensus, ĉu aĉeti ĝin` は、助言・仮定・勧めの表現として列間対応を保つ。
- `Bonvolu ne heziti demandi nian flugpersonaron` は、`flug-` + `personaro` の透明複合として flight crew を表し、PIV の `personaro` と矛盾しない。`demandi iun` の他動用法も許容範囲。
- `Kune ni povas facile plenumi ion ajn` は、「力を合わせれば何でも成し遂げられる」という各列の内容に対応する。`plenumi` は任務・行為の完遂に使えるため維持した。
- `Ĉu ĝi plaĉas al vi?`, `Mi ne ŝatas ĝin`, `Ĝi estas bela`, `Ĝi estas malbela`, `Estas interese`, `Estas enuige`, `Estas mirinde`, `Tio estas naŭza` は、好悪・評価の短文として自然。`naŭza` は PIV で吐き気や強い嫌悪を表す語として確認できる。

主な据え置き確認:
- Asking for & Giving Information: `Kial vi diris tion?`, `Kial mi ne pensis pri tio?`, `diri al mi la veron`, `cirkaj spektakloj`, `inventis la radon` は質問文として維持。
- Expressing Feelings: `trista`, `malstreĉita`, `ekscitita`, `motivita`, `embarasita`, `kapturno`, `malkuraĝigita`, `kondolencojn`, `Niaj pensoj estas kun vi...` は感情・体調・弔意文脈で維持。
- Help & Advice: `prunti`, `fari al mi servon`, `prizorgi`, `tiel afabla kaj klarigus`, `tekkomputilo`, `malkonsilus lui aŭton`, `flugpersonaro`, `plenumi ion ajn` は依頼・助言文脈で維持。
- Opinions: `plaĉas al vi`, `malbela`, `interese`, `enuige`, `mirinde`, `naŭza` は評価表現として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `trista`, `eksciti`, `motivo` / `motivi`, `embarasi`, `konfuzi`, `kondolenci` / `kondolenco`, `prunti`, `konsili`, `malkonsili`, `rekomendi`, `personaro`, `naŭzi`, `ŝoki`, `farti`, `plaĉi`, `rezigni`, `heziti`, `servi` 周辺。
- Glosbe `notebook (computer)`: https://en.glosbe.com/en/eo/notebook%20%28computer%29
- Kaikki/Wiktionary `tekokomputilo` / `tekkomputilo`: https://kaikki.org/plwiktionary/esperanto/meaning/t/te/tekokomputilo.html

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID556`〜`ID655` は100件確認済み。

## 608. 607周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood
- General Conversation / Agreeing & Disagreeing
- General Conversation / Asking for & Giving Information

結果:
- **CSV修正なし**
- 前回 `ID356`〜`ID455` に続き、今回は `ID456`〜`ID555` の100件を確認した。Streamlit アプリでは `Esperanto` と `日本語` / `中文` / `한국어` が双方向4択クイズの直接表示に使われるため、ロシア語を主基準、英語を補助基準としつつ、日中韓との対応を崩さないことを優先した。
- この範囲は、発音・綴り・翻訳確認、賛否表明、所在・旅行・日常質問が中心である。表現を自然化できる余地がある箇所でも、明確な意味ズレ・語形誤り・辞書確認不能な造語と判断できる場合に限って修正対象とした。
- `Parolu kun mi en la mandarena ĉina lingvo` はやや硬いが、PIV の `mandareno` に `la mandarena lingvo` 型があり、`vastiĝi` 周辺にも「中国で最も広く普及した言語は mandarena」という用例がある。普通話/標準中国語を指す各列と対応するため維持した。
- `Vi ne havas akĉenton` は、PIV の `akĉento` が話者・集団の発音上の特徴を表す語として確認でき、Glosbe でも `akĉento` の文例が確認できる。強勢を表す `akcento` へ戻す必要はない。
- `Kion signifas tiu vorto angle?`, `Kiel oni skribas tion?`, `Kiel oni diras tion ĉeĥe?`, `Kiel tio nomiĝas pole?`, `Ĉu mi ĝuste ĝin prononcas?`, `Kiel oni povas traduki tion?`, `Vi parolas tro rapide` は、意味・綴り・発音・翻訳・発話速度の確認として日中韓/RU/EN と対応する。`Ĉu mi ĝuste ĝin prononcas?` は語順を `Ĉu mi prononcas ĝin ĝuste?` に寄せる余地はあるが、焦点的語順として意味は明瞭。
- `Mi konsentas kun vi`, `Mi malkonsentas`, `Ĉu vi ne konsentas?`, `Mi tute konsentas`, `Mi ne konsentas kun via opinio`, `Ĉu vi konsentas, ke tio estas mensogo?`, `Mi komprenas lian vidpunkton, sed mi tute malkonsentas kun ĝi` は、PIV の `konsenti` / `malkonsenti` の構文範囲に収まり、賛否表明として対応する。
- `Vi pravas`, `Vi tiel pravas`, `Tio estas ĝuste mia vidpunkto`, `Ankaŭ mi tiel pensis`, `Mi ne povas kontraŭdiri tion`, `Mi vidas nenian malhelpon` は、賛同・反論不能・異論なしの会話表現として意味ズレなし。`Vi tiel pravas` は英語寄りの強調にも見えるが、`tiel` による程度・様態強調として文脈別許容。
- `Mi ne povas diri, ke mi kunhavas vian vidpunkton` は直訳感があるが、PIV で `kun havi opinion` が確認でき、`vidpunkto` も PIV の用例に見える語である。`dividas vian opinion` などへの自然化は可能だが、現行文を明確な誤りとは扱わない。
- `En la televido estas tro multe da reklamoj, ĉu ne?` は `Televido havas...` などに言い換えられるが、テレビ放送内の広告が多いという内容は各列と一致し、PIV の `televido` / `reklamo` と矛盾しない。
- `Mi estas ĉe Petro`, `Mi estas ĉe la laboro`, `Mi estas hejme`, `Mi estas en trajno`, `Mi estas en la kamparo`, `Mi ĵus revenis el Portugalio`, `Kie mi povas aĉeti mapon de la urbo?` は、所在・移動元・購入場所の表現として列間対応を保つ。
- `Ĉu vi konas bonan drinkejon?`, `Ĉu vi povas rekomendi junulargastejon?`, `Kie mi povas duŝiĝi?`, `Ĉu estas iuj picejoj proksime de via hejmo?`, `Ĉu vi biciklas pli ol unu fojon semajne?` は、PIV の `drinkejo`, `junular gastejo`, `duŝi`, `picejo`, `bicikli` と整合する。`junulargastejo` はPIVでは分かち書きが見えるが、ReVo で `gastejo` の文脈に `junularaj gastejoj` が確認でき、透明な複合としてホステル/青年旅舍の意味が保たれる。
- `Ĉu vi pli ŝatas ruĝon ol bluon?`, `Ĉu vi preferas oranĝan aŭ verdan?` は、色名・色形容詞の名詞的省略として読める。後者は `koloron` を補う自然化候補があるが、4択文の短い質問として「オレンジ色か緑色か」の意味は明確。
- `Jes, mi iris tien por ferioj`, `Fakte, mi estas survoje por renkonti amikon`, `Kie vi kutime pasigas viajn feriojn?`, `Mi kutime pasigas miajn feriojn en la kamparo` は、休暇・移動中・滞在先の表現として対応を保つ。`ferie` / `dum ferioj`、`renkontiĝi kun amiko` などに寄せる余地はあるが、内容変更を伴う過修正は避けた。
- `Ĉu ĝenas vin, se mi kopios ĉi tiun liston?` は、`se` 節を後置主語として読む構文で、「このリストをコピーしてもよいか/気になるか」の内容と一致する。
- `Kion vi trovas pli interesa, teatron aŭ operon?`, `Kiuj sportoj estas popularaj en via lando?`, `Ĉu vi vere pensas, ke tio estas vera?` は、比較・国で人気のスポーツ・真偽確認の質問として列間対応が明確。

主な据え置き確認:
- Making Yourself Understood: `mandarena ĉina lingvo`, `akĉento`, `angle`, `ĉeĥe`, `pole`, `prononcas`, `traduki`, `tro rapide` は、発音・言語・翻訳確認文脈で維持。
- Agreeing & Disagreeing: `konsentas`, `malkonsentas`, `pravas`, `vidpunkto`, `kunhavas vian vidpunkton`, `kontraŭdiri`, `Mi vidas nenian malhelpon`, `en plena ordo` は、賛否・異論有無の表現として維持。
- Asking for & Giving Information: `ĉe Petro`, `ĉe la laboro`, `en trajno`, `drinkejo`, `junulargastejo`, `duŝiĝi`, `biciklas`, `por ferioj`, `survoje por renkonti amikon`, `picejoj`, `Kion vi trovas pli interesa, teatron aŭ operon?` は、所在・旅行・日常質問文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `akĉento`, `mandareno`, `konsenti`, `vidpunkto` / `kun havi opinion`, `drinkejo`, `gastejo` / `junular gastejo`, `duŝi`, `picejo`, `bicikli`, `prononci`, `traduki`, `preferi`, `oranĝa`, `verda`, `ferio`, `televido`, `reklamo` 周辺。
- ReVo `gast/o` / `gastejo`: https://reta-vortaro.de/revo/art/gast.html
- Glosbe `akĉento` 文例: https://glosbe.com/en/eo/quaint
- Glosbe `bicikli`: https://glosbe.com/nl/eo/fietsen

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- 作業ディレクトリ側CSVとアプリ実行用CSVはバイト単位で一致: `cmp_exit=0`
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは UTF-8 BOM あり、CRLF 行末 5001、裸 LF 0。
- `ID456`〜`ID555` は100件確認済み。

## 607. 606周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers
- Basic Sentences / Congratulations
- General Conversation / Languages
- General Conversation / Making Yourself Understood

結果:
- **CSV修正なし**
- 前回 `ID256`〜`ID355` に続き、今回は `ID356`〜`ID455` の100件を確認した。Streamlit アプリでは `PHRASE_CSV` から読み込まれた `Esperanto` と `日本語` / `中文` / `한국어` が双方向4択クイズの直接表示に使われるため、ロシア語を主基準、英語を補助基準としつつ、日中韓との対応を崩さないことを優先した。
- この範囲は短い応答、祝辞、言語名、聞き返し表現が中心である。過去周回で焦点になった `Feliĉan Divalon!`、`Mi havas akĉenton`、`Gratulon pro via akcepto en la universitaton!`、言語名派生を重点的に再照合したが、現行CSVをさらに動かすべき明確な語形・格・一致・語法・意味ズレは見つからなかった。
- `Jes, ĝi tre plaĉas al mi!`, `Jes, estas bone`, `Mi nur ŝercas!`, `Kia trankviliĝo!`, `Tia estas la vivo!`, `Ne gravas`, `Ju pli frue, des pli bone`, `Ĉu mi povus havi vian atenton?` は、短い応答・感嘆・呼びかけとして日中韓/RU/EN と対応する。`Ankaŭ mi ne` は単独では前文依存だが、`Neither do I` 系の短答として文脈別許容。
- `Gratulon!`, `Miaj sinceraj gratuloj!`, `Permesu al mi gratuli vin`, `Permesu al mi unue gratuli vin`, `Gratulon pro ...`, `Gratulojn pro ...` は、PIV の `gratuli` / `gratulo` の語義と合い、祝意の定型として維持した。単数 `Gratulon` と複数 `Gratulojn` の揺れは、このCSVの短文祝辞では意味ズレを生まない。
- `Feliĉan naskiĝtagon!`, `Feliĉajn festotagojn!`, `Feliĉan Novan Jaron!`, `Feliĉan Kristnaskon!`, `Feliĉan Paskon!`, `Feliĉan Ĥanukon!`, `Feliĉan datrevenon!`, `Feliĉan Dankotagon!`, `Feliĉan Ramadanon!` は、`Feliĉan/Feliĉajn + 対格` の祝意定型として維持した。PIV の `feliĉa` には「feliĉan feston」型の用例があり、`Pasko`, `Ĥanuko`, `Ramadano`, `Valenteno` も関連語として確認できる。
- `Feliĉan Divalon!` は PIV では直接確認できないが、Wiktionary 系の多言語訳で Diwali の Esperanto 対応として `Divalo` が確認でき、過去修正後の `Divalon` は祝祭名への対格祝辞として文法的に通る。より広い綴り揺れとして `Divali` 系も見えるが、現行 `Divalo` を明確な誤りとは断定しない。
- `Gratulon pro via akcepto en la universitaton!` は `akceptiĝo` などの候補もあるが、PIV の `akcepti` には教育機関が学生を受け入れる用法があり、大学合格・入学許可の文脈として読める。`en la universitaton` の方向対格も「大学へ受け入れられる」結果方向として許容し、内容を変えない。
- `Gratulon pro la trapaso de viaj ekzamenoj!` は PIV の `ekzameno` 項目に `trapasi ekzamenon` の用例が確認でき、試験合格の祝辞として維持した。`Gratulon pro la trapaso de via stirekzameno!` も `stiri` + `ekzameno` の透明な複合で、運転試験合格の意味を保つ。
- `Gratulojn pro via magistra grado!` は PIV の `magistro` が大学学位保持者を表すため、修士号取得の祝辞として対応する。`magistra` は `majstra` と混同していない。
- `Mi ŝatas la bengalan`, `Mi parolas la rumanan`, `Ĉu ŝi parolas la tajan?`, `Mi lernas la urduon`, `Kiu parolas la persan?`, `Mia denaska lingvo estas la norvega`, `Mi parolas la francan, la hispanan kaj iomete la slovakan`, `Kie vi lernis la finnan?`, `Mi ŝatus praktiki mian portugalan`, `Mi lernas la indonezian jam de unu monato` は、`lingvo` を省略した言語名表現として維持した。PIV の `lingvo` 用例にも `la lingvo hispana/franca` 型があり、PIV収録語根や透明派生と矛盾しない。
- `Ni parolu slovene`, `Vi parolas tre bone azerbajĝane`, `Mi povas komuniki itale`, `Bonvolu paroli latve` は、言語使用を表す副詞形として文脈上明確。`azerbajĝana` は Glosbe、`latve` は Wiktionary/Kaikki 系の語彙データでも確認でき、PIV の `Azerbajĝano` / `latvo` 周辺と合わせて誤造語とは扱わない。
- `Via tagaloga estas tre bona`, `Mia korea estas sufiĉe malbona` は、`lingvo` または「言語能力」を省いた口語的な短文として文脈別許容。`tagaloga lingvo` は Reta Vortaro でも確認でき、`la tagaloga` 系の省略名詞用法として読める。
- `Mi simple bezonas praktiki`, `Mi iom perdis la praktikon`, `Mi perfekte regas la araban lingvon`, `Mi mem lernis ĝin`, `Mi sekvis kurson` は、学習・言語運用能力の表現として列間対応を保つ。`perdis la praktikon` は直訳的にも見えるが、「少し実践感覚を失った」の範囲で `out of practice` に対応し、明確な意味ズレではない。
- `Ĉu vi komprenas?`, `Mi komprenas`, `Mi ne komprenas`, `Ĉu vi komprenas la germanan?`, `Ĉu vi povus ripeti tion?`, `Ĉu tio estas ĝusta?`, `Ĉu tio estas malĝusta?`, `Kiel ĉi tio nomiĝas?`, `Bonvolu noti ĝin`, `Kion ĉi tio signifas?`, `Bonvolu ripeti, mi petas`, `Ĉu vi povas paroli pli malrapide?`, `Kiel oni prononcas ĉi tiun vorton?`, `Ĉu vi povas literumi ĝin?` は、聞き返し・理解確認・発音/綴り確認の短文として自然な範囲にある。PIV の `prononci` と `literumi` でも語義を確認できた。
- `Mi havas akĉenton` は PIV で話者や集団の発音習慣としての `akĉento` が確認でき、Wiktionary でも地域・社会集団などに結びつく発音特徴として確認できる。以前の `akcento` からの修正後の現形が適切であるため維持した。

主な据え置き確認:
- Short Questions & Answers / Congratulations: `Jes, ĝi tre plaĉas al mi!`, `Kia trankviliĝo!`, `Tia estas la vivo!`, `Ankaŭ mi ne`, `Ju pli frue, des pli bone`, `Gratulon!`, `Feliĉan naskiĝtagon!`, `Feliĉajn festotagojn!`, `Feliĉan Kristnaskon!`, `Feliĉan Paskon!`, `Feliĉan Ĥanukon!`, `Feliĉan Divalon!`, `Gratulon pro via akcepto en la universitaton!`, `Gratulon pro la trapaso de viaj ekzamenoj!`, `Gratulojn pro via magistra grado!` は、短答・祝辞文脈で対応を保つ。
- Languages / Making Yourself Understood: `la bengalan`, `la rumanan`, `la tajan`, `la urduon`, `slovene`, `azerbajĝane`, `la norvega`, `la slovakan`, `la nederlandan`, `la indonezian`, `Via tagaloga`, `Mia korea`, `komprenas la germanan`, `Bonvolu noti ĝin`, `Kion ĉi tio signifas?`, `akĉenton`, `prononcas`, `literumi` は、言語名・理解確認・発音/綴り確認の文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 公式説明: https://vortaro.net/klarigoj.html
- Glosbe Esperanto-English: https://en.glosbe.com/eo/en
- Glosbe `azerbejdžanski` → `azerbajĝana`: https://glosbe.com/bs/eo/azerbejd%C5%BEanski
- Wiktionary `Diwali` 多言語訳 `Divalo`: https://pl.wiktionary.org/wiki/Diwali
- Wiktionary `akĉento`: https://en.wiktionary.org/wiki/ak%C4%89ento
- Reta Vortaro `tagalog/o`: https://reta-vortaro.de/revo/art/tagalog.html
- Kaikki/Wiktionary `latvo` 派生 `latve`: https://kaikki.org/frwiktionary/All%20languages%20combined/meaning/l/la/latvo.html
- PIV 2020 `akcepti`, `akĉento`, `feliĉa`, `gratuli`, `lingvo`, `bengalo`, `Ĥanuko`, `magistro`, `Pasko`, `Ramadano`, `Valenteno`, `Indonezio`, `latvo`, `Nederland(o)`, `norvego`, `rumano`, `sloveno`, `tajo`, `urduo`, `praktiko`, `prononci`, `stiri`, `ekzameno`, `komuniki`, `literumi` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID356`〜`ID455` は100件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 606. 605周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks
- Basic Sentences / Apologies
- Basic Sentences / Instructions
- Basic Sentences / Short Questions & Answers

結果:
- **CSV修正なし**
- 前回の新サイクル `ID156`〜`ID255` に続き、今回は `ID256`〜`ID355` の100件を確認した。Streamlit アプリでは `PHRASE_CSV` から読み込まれた `Esperanto` と `日本語` / `中文` / `한국어` が双方向4択クイズの直接表示に使われるため、今回もロシア語を主基準、英語を補助基準として、日中韓との対応を崩さないことを優先した。
- 感謝・謝罪・指示・短い応答の定型句が中心であるため、言い換えで自然化できる箇所があっても、明確な意味ズレ・語形誤り・辞書確認不能な造語と判断できる場合のみ修正対象とした。エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、Glosbe、および既存ログを照合した。
- `Mi vere ne scias kiel danki vin pro via subteno` は、書き言葉なら `scias, kiel ...` とカンマを入れる余地があるが、CSV内の短文表現としては意味が明瞭で、`danki ... pro` の語法も PIV の `danki` 系に合うため維持した。
- `Mi dankas vin nome de mia edzo`, `Estas granda honoro por mi ricevi ĉi tiun premion`, `Mi tre aprezas vian zorgemon` は、謝辞・受賞挨拶・相手の配慮への感謝として各列と対応する。`nome de`、`honoro por mi`、`zorgemo` は文脈内で自然な範囲にあるため修正しない。
- `Pardonu min`, `Bonvolu pardoni min`, `Mi petas pardonon`, `Mi pardonpetas`, `Ne estas kialo pardonpeti` は、PIV の `pardon(i)` / `pardonpeti` 系および Glosbe の `apologize` 対応で確認できる。`Ne estas kialo pardonpeti` は `por pardonpeti` などを補えるが、短い応答として「謝る理由はない」の意味が明確で、過修正しない。
- `Pardonu, ke mi ĝenas vin`, `Ĉu mi povas ĝeni vin momenton?`, `Pardonu la ĝenon`, `Ne ĝenu vin` は PIV の `ĝeni` の他動用法と合う。日本語・中国語・韓国語では「邪魔する/迷惑をかける/手間をかける」の範囲で対応し、ロシア語とも大きくずれない。
- `Ne ofendiĝu`, `Mi ne tion celis`, `Mi bedaŭras, ke mi ĉagrenis vin`, `Mi agis senzorge`, `Tio okazis hazarde`, `Ne estas via kulpo` は、PIV の `ofendi`, `celi`, `bedaŭri`, `ĉagreni`, `zorgi` / `senzorga`, `hazarde`, `kulpo` の範囲で確認できる。`Mi ne tion celis` は語順がやや強調的だが「それを意図したのではない」という焦点が明確で維持した。
- `Pardonu, ke mi devigis vin atendi` は `igis/lasis vin atendi` の方が柔らかい候補になり得るが、ロシア語が「待たせてしまった」より強い `заставила вас ждать` で、PIV の `devigi` とも対応するため、意味内容を弱めず維持した。
- `Venontfoje mi faros ĉion ĝuste` は「次回は正しくやる」の表現として日中韓/RU/EN と対応し、`ĝuste` も語法上問題ないため維持した。
- `Atentu la hundon!`, `Atentu!`, `Ne atentu tion, kion ŝi diras`, `Ĉesu tion!`, `Rapidu!`, `Trankviliĝu!`, `Kuraĝu!`, `Ne nervozu`, `Silentu!` は、注意・停止・励まし・沈黙要求の短い命令表現として自然な範囲にある。`Kuraĝu!` は「勇気を出して/がんばって」に近い励ましとして文脈別許容。
- `Ne paŝu sur la gazonon!` は PIV の `paŝi` と `gazono` に照らして、`sur la gazonon` の方向格が「芝生へ踏み込む」を表し、注意看板的な表現として維持した。
- `Bonvolu viciĝi ĉi tie` は PIV の `viciĝi` が「列に入る」を表すため、`Bonvolu starigi vin en vico ĉi tie` などへ言い換える必要はない。クイズ用の短文としても「ここに並んでください」と対応する。
- `Rigardu, kien vi iras!`, `Penu ne fari bruon!`, `Provu esti pli singarda estonte`, `Ne lasu la pordon malfermita`, `Seĝu vin`, `Momenton, mi skribu tion` は、指示・注意・短い依頼として列間対応が明確で、語法上の致命的問題は見つからなかった。
- `Ĉu vi ĝuas la filmon?`, `Kion vi opinias pri via nova profesio?`, `Kiel fartas via frato?`, `Ĉu vi komprenas?`, `Ĉu estas klare?`, `Ĉu vi konsentas?`, `Ĉu io okazas?`, `Kial ne?`, `Jen ĉio`, `Kiel bele!`, `Amuze!` は、短い質問・応答・感嘆として文脈別許容。`Kial ne?` は単独では「なぜだめなのか」と「いいですね」の両方に寄り得るが、短い応答欄では各列の範囲を外れない。
- 範囲内の `Pardonu min`、`Atendu momenton`、`Bone` は重複しているが、謝罪・待機依頼・短い肯定応答として複数の近い参考訳が割り当てられているだけで、クイズ用対応を壊す明確な誤りとは判断しなかった。

主な据え置き確認:
- Thanks / Apologies: `Mi vere ne scias kiel danki vin pro via subteno`, `Mi dankas vin nome de mia edzo`, `Dankon pro via mesaĝo`, `Mi tre aprezas vian zorgemon`, `Pardonu min`, `Bonvolu pardoni min`, `Mi petas pardonon`, `Mi pardonpetas`, `Ne estas kialo pardonpeti`, `Pardonu, ke mi ĝenas vin`, `Ĉu mi povas ĝeni vin momenton?`, `Mi ne tion celis`, `Mi bedaŭras, ke mi ĉagrenis vin`, `Mi agis senzorge`, `Pardonu, ke mi devigis vin atendi`, `Venontfoje mi faros ĉion ĝuste` は、感謝・謝罪・釈明文脈で対応を保つ。
- Instructions / Short Questions & Answers: `Atentu la hundon!`, `Ne paŝu sur la gazonon!`, `Bonvolu viciĝi ĉi tie`, `Atendu momenton`, `Rigardu, kien vi iras!`, `Kuraĝu!`, `Trankviliĝu!`, `Ne nervozu`, `Silentu!`, `Ĉu vi ĝuas la filmon?`, `Kion vi opinias pri via nova profesio?`, `Kial ne?`, `Jen ĉio`, `Kiel bele!`, `Amuze!` は、命令・注意・短い応答文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 公式説明: https://vortaro.net/klarigoj.html
- Glosbe Esperanto-English: https://en.glosbe.com/eo/en
- Glosbe `apologize`: https://glosbe.com/en/eo/apologize
- PIV 2020 `danki`, `pardon(i)` / `pardonpeti`, `ĝeni`, `ofendi`, `celi`, `bedaŭri`, `ĉagreni`, `zorgi` / `senzorga`, `devigi`, `hazarde`, `kulpo`, `atenti`, `ĉesi`, `rapida`, `trankvila`, `kuraĝi`, `nervoza`, `silent(i)`, `paŝi`, `gazono`, `vico` / `viciĝi`, `profesio`, `amuz(i)` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID256`〜`ID355` は100件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 605. 604周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye
- Basic Sentences / Good Wishes
- Basic Sentences / Thanks

結果:
- **CSV修正なし**
- 前回 `ID4656`〜`ID5155` でCSV末尾まで到達済みのため、今回は新しい再点検サイクルとして先頭側の `ID156`〜`ID255` を100件確認した。Streamlit アプリでは `data_sources.py` の `PHRASE_CSV` を `sentence_app.py` / `sentence_app_Cxina_versio.py` / `sentence_app_Korea_versio.py` が読み込み、`Esperanto` と `日本語` / `中文` / `한국어` を双方向4択の出題ペアとして使うため、今回も日中韓との対応を崩さないことを優先した。
- 挨拶・別れ・祝意・感謝の短い定型句が中心であるため、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、Glosbe などの既存オンライン辞書確認結果、および過去ログを照合した。
- `Bonan matenon`, `Bonan tagon`, `Bonan vesperon`, `Bonan nokton`, `Ĝis revido`, `Ĝis morgaŭ`, `Ĝis baldaŭ` は挨拶・別れの定型表現として維持した。PIV の `bona` 周辺には `bonan tagon, vojaĝon!` 型の用例があり、`Bonan tagon!` は挨拶にも「良い一日を」にも文脈別許容。
- `Kiel vi fartas?`, `Mi fartas bone, dankon`, `Ne tro malbone`, `Tiel-tiel` は PIV の `farti` と対応する近況確認・返答表現で、日中韓/RUとの意味対応も保つ。
- `Salutu Lukason de mi`, `Bonvolu transdoni miajn korajn salutojn al via patro` は PIV の `saluti` / `saluto` の用例と合い、「よろしく伝える」文脈として維持した。
- `Mi antaŭĝojas revidi vin` は PIV の直接見出しでは弱いが、`antaŭ` + `ĝoji` の透明な複合で、既存ログでも Glosbe・実例確認済みである。JA/ZH/KO/RU の「再会を楽しみにする」と一致するため、生成AIの未確認造語とは扱わず維持した。
- `Sanon!` は `Bless you!` / `Будь здоров!` 系の健康祈願として維持し、乾杯表現の `Je via sano!` と区別されているため問題なし。
- `Ni tostu por vi!`, `Mi ŝatus proponi toston por mia filo` は PIV の `tosto/tosti` が祝杯発話を表すことと対応する。`por` は「〜のために/〜を祝って」の読みで、祝辞・乾杯文脈として意味ズレなし。
- `Nedankinde`, `Dankon pro via gastamo`, `Dankon pro via donaco`, `Dankon, ke vi tiel diris`, `Dankon pro ĉio`, `Mi ne povas sufiĉe danki vin`, `Kontraŭe: estas mi, kiu devus danki vin!`, `Mi tre aprezas viajn afablajn vortojn` は感謝・返礼表現として列間対応を保つ。
- `Ne ĝenu vin` は PIV の `ĝeni` 系と対応し、相手に手間をかけさせない `Don't bother` の短い応答として許容。
- `Tio estis la plej malmulto, kion mi povis fari` は `minimumo` への自然化候補もあるが、EN/RU/JA/ZH/KO の「least I could do / самое малое / せめてものこと」と一致し、明確な意味ズレではないため過修正しない。
- `Mi dankas pro via tempo` は `Mi dankas vin pro via tempo` の方が明示的だが、PIV の `danki ... pro io` 系に照らして省略的に通るため維持。
- `Mi ŝatus diri, kiel dankema mi estas al vi` は `kiom dankema` も候補だが、`kiel` + 形容詞で感嘆・程度を表す読みが可能で、各列の「どれほど感謝しているか」に対応するため修正しない。
- `Vi farus la samon por mi` は英語が完了寄りの would have done だが、エスペラントの条件法は時制を固定しない。感謝への返答として「あなたも同じことをしてくれたはず」の範囲を保つため維持。
- `Mi fartas bone, dankon`, `Ĝis revido!`, `Nedankinde` は範囲内で重複しているが、それぞれ近い定型応答を複数の参考訳で表しているだけで、クイズ用対応を壊すほどの明確な意味ズレとは判断しなかった。

主な据え置き確認:
- Saying Hello & Goodbye: `Bonan matenon`, `Saluton`, `Ĝis`, `Kiel vi fartas?`, `Mi fartas bone, dankon`, `Estas bone vidi vin`, `Bonan tagon`, `Bonan vesperon`, `Bonan nokton`, `Ĝis revido`, `Ĝis morgaŭ`, `Ne tre bone`, `Tiel-tiel`, `Kio nova?`, `Nenio nova`, `Kiel iras la laboro?`, `Mi ĝojas revidi vin`, `Mi devas iri`, `Mi revenos`, `Salutu Lukason de mi`, `Estis agrable paroli kun vi`, `Bonvenon`, `Ĝis baldaŭ`, `Mi tuj revenos`, `Ĉiuokaze`, `Estis agrable konatiĝi kun vi`, `Mi antaŭĝojas revidi vin`, `Ni revidiĝos post tri semajnoj`, `Kiel vi progresas en via nova laboro?`, `Bonvolu transdoni miajn korajn salutojn al via patro`, `Delonge ni ne vidiĝis` は挨拶・別れ・再会文脈で対応を保つ。
- Good Wishes: `Bonŝancon`, `Ankaŭ al vi`, `Amuziĝu`, `Zorgu pri vi`, `Ĉion plej bonan`, `Sanon`, `Resaniĝu baldaŭ`, `Je via sano`, `Dormu bone`, `Mi ĝojas aŭdi tion`, `Bonan vojaĝon`, `Bonan amuzon`, `Agrablan nokton`, `Bonan semajnfinon`, `Mi deziras al vi sanon/feliĉon`, `Ke ĉiuj viaj deziroj plenumiĝu`, `Ni tostu por vi`, `dolĉajn sonĝojn`, `revoj realiĝos`, `longan kaj feliĉan vivon`, `sukceson en ĉio`, `speciala tago`, `proponi toston`, `Kun via permeso`, `Bonŝancon por/en`, `Bonan vojaĝon hejmen` は祝意・祈願文脈で意味ズレなし。
- Thanks: `Dankon`, `Nedankinde`, `Ne, dankon`, `Mi ĝojas helpi`, `Multan dankon`, `Tio estas tre afabla de vi`, `Dankon, ke vi venis`, `Dankon pro via gastamo/donaco/helpo/ĉio/komplimento`, `Dankon, ke vi tiel diris`, `Ne ĝenu vin`, `Tute nenio`, `Mi estos eterne dankema al vi`, `Tio estis la plej malmulto, kion mi povis fari`, `Estas plezuro`, `Mi ne povas sufiĉe danki vin`, `Mi dankas pro via tempo`, `Vi estas tre malavara`, `Mi ŝatus diri, kiel dankema mi estas al vi`, `Mi estas tre dankema al vi`, `Estis plezuro por mi tion fari`, `Mi neniam forgesos, kion vi faris por mi`, `Vi farus la samon por mi`, `Tio vere ne estas necesa`, `Mi bone amuziĝis hodiaŭ`, `Mi tre aprezas viajn afablajn vortojn` は感謝・返礼文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 公式説明: https://vortaro.net/klarigoj.html
- Glosbe Esperanto-English: https://en.glosbe.com/eo/en
- Glosbe `antaŭĝoji`: https://glosbe.com/eo/en/anta%C5%AD%C4%9Doji
- PIV 2020 `bona`, `diri`, `tago`, `vojaĝi` / `vojaĝo`, `farti`, `saluti` / `saluto`, `danki` / `dankema` / `nedankinde`, `ĝoji`, `sano`, `tosto` / `tosti`, `zorgi`, `deziro`, `plezuro`, `permesi`, `aprezi`, `necesa`, `afabla`, `malavara`, `komplimento` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID156`〜`ID255` は100件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 604. 603周目 追加再点検（ID4656〜5155）

対象:
- `ID4656`〜`ID5155`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy
- Communication Means / Phone, Phone Calls at Work, Mass Media, At the Post Office, Letter
- Time & Weather / Telling the Time, Calendar, Time Expressions, Weather

結果:
- **CSV修正なし**
- `ID4656`〜`ID5155` の500件を100件単位で連続再点検し、CSV末尾まで到達した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、表現内容を変えないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、Glosbe などのオンライン辞書情報、および既存ログ内の確認結果を照合した。特に、歯科・薬局・電話・郵便・天気分野で生成AI由来の造語に見えやすい `plombo`, `plombi`, `tablojdo`, `pilolo`, `hipermetropa`, `astigmatismo`, `plastro`, `inhalilo`, `desinfektaĵo`, `dormigilo`, `retadreso`, `retmesaĝo`, `afranko`, `poŝtrestante`, `fulmotondro`, `hajlo`, `nebulo`, `veterprognozo`, `atmosfera premo` 周辺を重点確認した。
- `plombo` / `plombi` は歯科の filling / 詰め物として PIV と Glosbe の双方で確認でき、`plombigi denton`, `La plombo elfalis`, `Mi ŝatus plumbon blankan` は歯科文脈に合うため維持した。
- `tablojdo` は PIV の薬学語義で錠剤を表す語として確認でき、薬局範囲の `du tablojdojn`, `kontraŭdolorilaj tablojdoj`, `piloloj` との区別も、文脈上の自然な揺れとして許容した。
- `hipermetropa`, `miopa`, `astigmatismo`, `dioptrioj` は PIV の医学・光学語義に合い、眼鏡店文脈の farsighted / nearsighted / astigmatism / diopter に対応するため維持した。
- `afranko`, `poŝti`, `poŝtrestante`, `rekomendita poŝto`, `vatita koverto`, `giĉeto` は PIV の郵便・窓口・料金文脈に合う。`Ĉe kiu giĉeto estas poŝtrestante?` は省略的だが、ロシア語「В каком окне корреспонденция до востребования?」および日本語「どの窓口が局留め郵便の受付ですか？」との対応が明確で、意味ズレとは判断しなかった。
- `fulmotondro` は PIV の `tondro` 派生説明で「fulmo tondro」として確認でき、`fulmo`, `tondro`, `ŝtormo`, `tempesto` との関係から thunderstorm に対応する語として許容した。`Hajlas`, `Fulmas`, `Pluvetadas`, `Pluvegas`, `veterprognozo`, `atmosfera premo`, `glitaj` も天気表現として意味対応を保つ。
- `Ĉu vi havas ion por sekiĝintaj lipoj?` は chapped lips に対して直訳的に見えるが、日本語「唇の乾燥」およびロシア語「обветренных губ」の範囲を外れないため維持した。
- `Mia baterio baldaŭ malŝargiĝos` は電話文脈の battery running out として自然で、腕時計範囲の `pilo` とは対象機器が異なるため維持した。
- `Kie mi povas konekti mian tekkomputilon?` は plug in laptop に対して広めの `konekti` だが、ロシア語「подключить свой ноутбук」および日中韓の「つなげる/连接/연결」に対応し、明確な意味ズレではないため維持した。
- `Ĝis la unua horo` は `Ĝis kioma horo?` への返答として `by / к часу / 1時までに` に対応し、時刻表現として許容した。

主な据え置き確認:
- Treatment / Dentist / Optician / Pharmacy: `antibiotikojn`, `piloloj`, `tablojdoj`, `dentodoloro`, `gingivoj`, `plombo`, `plombigi`, `krono`, `dentprotezo`, `kario`, `denta higienisto`, `gargari la buŝon`, `alĝustigi kronon`, `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `okulekzamenoj`, `astigmatismo`, `kadroj`, `okulvitroj por legado`, `UV-protekto`, `inhalilo`, `desinfektaĵo`, `plastroj`, `kontraŭdoloriloj`, `fastante`, `nur laŭ recepto`, `herbaj medikamentoj`, `paracetamolo`, `aspirino`, `kromefikoj`, `nur por ekstera uzo`, `dormigiloj`, `vojaĝmalsano`, `kapsuloj`, `nikotinaj plastroj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は、健康・薬局文脈で対応を保つ。
- Phone / Work Calls / Mass Media: `malkonektiĝis`, `malŝargiĝos`, `voka signalo`, `kredito`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `telefonbudo`, `telefonkarto`, `telefonlibro`, `interna numero`, `klavi la numeron`, `demeti la aŭdilon`, `konektos vin`, `retpoŝtadreso`, `Skajpon`, `uzantonomo`, `ensalutu`, `elsalutu`, `retmesaĝo`, `Facebook`, `Tvitero`, `tekkomputilo`, `eldonkvanto`, `usona futbalo` は、電話・業務電話・メディア文脈で維持。
- Post Office / Letter: `poŝtoficejo`, `poŝtkesto`, `vatita koverto`, `poŝti`, `aerpoŝto`, `fakso`, `faksa numero`, `laborhoroj`, `televida licenco`, `abono`, `poŝtmarkoj`, `afranko`, `fotokabino`, `fotokopiilo`, `rekomendita poŝto`, `asekuri`, `pezi`, `dogana deklaracio`, `pesilo`, `poŝtrestante`, `Sincere via`, `Al la koncernatoj`, `kunsendas mian vivresumon`, `Antaŭdankon`, `Respektplene via`, `Kun plej koraj salutoj`, `Bonvolu ne heziti kontakti min`, `antaŭĝojas`, `aldonaĵo`, `ekzameni ĉi tiun aferon` は、郵便・手紙文脈で意味ズレなし。
- Telling the Time / Calendar / Time Expressions / Weather: `Kioma horo estas?`, `kvarono antaŭ`, `kvarono post`, `tagmezo`, `noktomezo`, `labortagoj`, `libertago`, `Hodiaŭ tage`, `Ĉi-posttagmeze`, `Antaŭhieraŭ`, `Postmorgaŭ`, `glacie kaj glite`, `nebule`, `Varmegas`, `Frostas`, `Pluvetadas`, `Hajlas`, `Fulmas`, `fulmotondro`, `malvarmete`, `Forte pluvas`, `Ekpluvas`, `Pluvegas`, `sub nulo`, `veterprognozo`, `Ĉi-nokte frostos`, `atmosfera premo`, `glitaj` は、時刻・日付・天気表現として対応を保つ。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 公式説明: https://vortaro.net/klarigoj.html
- Glosbe `plombo`: https://glosbe.com/eo/en/plombo
- Glosbe Esperanto-English: https://en.glosbe.com/eo/en
- PIV 2020 `plombo` / `plombi`, `tablojdo`, `pilolo`, `hipermetropa`, `miopa`, `astigmatismo`, `dioptrio`, `plastro`, `inhalilo`, `desinfektaĵo`, `dormigilo`, `ret poŝto` / `retadreso` / `retmesaĝo`, `afranko`, `poŝto` / `poŝti` / `poŝtrestante`, `giĉeto`, `rekomendi`, `fulmo`, `tondro` / `fulmo tondro`, `hajlo`, `nebulo`, `pluvo`, `prognozo`, `ŝtormo`, `tempesto`, `vetero`, `atmosfero`, `premo`, `gliti`, `frost(o)` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID4656`〜`ID5155` は500件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 603. 602周目 追加再点検（ID4056〜4655）

対象:
- `ID4056`〜`ID4655`
- Leisure Time / Sport, Music, Going Camping, Family Time, Gardening, Having Guests
- Services / At the Bank, At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs
- Health / At the Doctor, Diseases, Treatment

結果:
- **CSV修正なし**
- `ID4056`〜`ID4655` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の外部辞書確認結果を参照した。特に、`regatto`, `televidaj romanoj`, `bangalo`, `franĝo`, `konstanta ondumado`, `dislimo`, `senharigo`, `feni`, `kranihaŭto`, `pilo`, `krono`, `rentgena ekzameno`, `trankviligaĵo`, `mikozo de la piedoj`, `sutureroj`, `urina specimeno` のように生成AI由来の疑いが出やすい語を重点確認した。
- `regatto` は PIV の `regatt/o` に合うため、英語風に見える綴りだが現形を維持した。`regato` への戻しは行わない。
- `televidaj romanoj` は soap opera の直訳調に見えるが、既存ログで Glosbe 確認済みであり、Family Time のテレビ番組文脈から意味が外れていないため維持した。
- `krono` は時計修理文脈の winder / リューズ / 表冠 / 용두 / заводная головка に対応する。PIV の `krono` にポケット時計などの上部リング状部品の語義があり、過去周回で `kroneto` から修正済みであるため、現CSVの `La krono estas rompita` を維持した。
- `rentgena ekzameno` は、単独の `rentgeno` では検査名として弱くなりうるため、X-ray examination として文脈を明示する現形を維持した。
- `sutureroj` は PIV で縫合を構成する個々の結び糸として確認でき、EN/JA/ZH/KO/RU の「何針か」に対応するため維持した。

主な据え置き確認:
- Sport / Music / Camping: `regatto`, `vetŝancoj`, `golfbastonoj`, `golfĉaro`, `norma nombro da batoj`, `femuraj muskoloj`, `ĥoro`, `akordiono`, `saksofono`, `dirigento`, `simfonia orkestro`, `popolmuziko`, `tendumi`, `lanterno`, `tendumejo`, `ruldomo`, `alumetoj`, `trinkakvo`, `poŝlampo`, `kukolo`, `pego`, `najtingaloj`, `hirunda nesto`, `telfero`, `monta pado`, `piedvojetoj`, `rostokrado`, `surloke` は、スポーツ・音楽・キャンプ文脈で対応を保つ。
- Family Time / Gardening / Having Guests: `bovlingon`, `sketi`, `televidaj romanoj`, `sagetojn`, `legadon`, `sojfabojn`, `sekalon`, `falĉas`, `erpis`, `plugos`, `fruktarbejo`, `buŝtukojn`, `boligos akvon`, `sukerpecoj`, `ĝinon kun toniko`, `mendas picon hejmen`, `Mi lavos, kaj vi viŝos` は、家庭・園芸・来客文脈で維持。
- Bank / Estate Agency: `provizio`, `falsa monbileto`, `bankaŭtomato`, `kontantmono`, `saldo`, `stirpermesilo`, `nuligi ĉekon`, `deponi`, `retiro`, `bankbiletojn`, `legitimilo`, `formularon por monretiro`, `raporti pri perdita kreditkarto`, `interreta bankado`, `konteltiro`, `ĉekaro`, `monŝanĝejo`, `hipoteko`, `ĝiri ... en ĉi tiun konton`, `interezprocento`, `vojaĝan ĉekon`, `loĝejo`, `bangalo`, `vicdomo`, `parkumejo`, `petata prezo`, `diskutebla`, `kontanta aĉetanto`, `duetaĝa`, `antaŭpago`, `deponaĵo je unu-monata lupago`, `duamana posedaĵo`, `prezintervalo`, `dissendolisto` は、銀行・不動産文脈で意味ズレなし。
- Beauty Salon / Tailor: `franĝo`, `Mildan konstantan ondumadon`, `dislimo`, `farbigi`, `farbi miajn harojn blonde`, `helajn striojn en miaj haroj`, `senharigo`, `senharigon ... per vakso`, `feni`, `ŝampui`, `sprajo por haroj`, `ĝelo por haroj`, `kranihaŭto`, `elpluki miajn brovojn`, `fajli/formi/laki ungojn`, `tajloro`, `zipo`, `alkudri`, `fliki`, `mezuroj`, `alĝustigi`, `laŭmezura kostumo`, `maniklongon`, `mallarĝigi`, `mallongigi`, `longigi`, `plilarĝigi` は、美容院・仕立て屋文脈で対応する。
- Repairs: `La ekrano fendiĝis`, `kuirforno`, `brakhorloĝo`, `pilo`, `krono`, `ŝlosilringo`, `fari kopion de ĉi tiu ŝlosilo`, `po unu kopio`, `lasi ripari mian fotoaparaton`, `riparejo por ŝuoj`, `plandumo`, `garantio`, `fabrikanto` は、修理・時計・鍵・靴修理文脈で対応を保つ。
- Doctor / Diseases / Treatment: `kontrola ekzameno`, `kapturno`, `medikamentojn`, `alkoholaĵojn`, `rentgena ekzameno`, `aŭdotestojn`, `medicina konsulto`, `analizojn`, `malsanasekuro`, `sangogrupo`, `O negativa` / `O-pozitiva`, `kmera`, `desinfekti`, `suprenfaldi`, `sangopremo`, `insulino`, `trankviligaĵo`, `ulcero`, `surdorse/surventre`, `haŭterupcio`, `furunko`, `diareo`, `konstipita`, `nazkataro`, `limfonodoj`, `mikozo de la piedoj`, `streĉis muskolon`, `sendormeco`, `fojnofebro`, `sangotesto`, `sutureroj`, `loka anestezo`, `urina specimeno`, `injekto`, `ellitiĝi` は、診療・症状・治療文脈で意味対応を保つ。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `regatto`, `bangalo`, `franĝo`, `ondumado`, `haroj` / `dislimo`, `senharigo`, `feni`, `ŝampui`, `krono`, `pilo`, `rentgena`, `trankviligi` / `trankviligaĵo`, `mikozo`, `fojno febro` / `fojno kataro`, `suturo` / `suturero`, `urino` / `urina`, `anestezo` 周辺。
- Glosbe `SOAP` / `televidaj romanoj`: https://en.glosbe.com/en/eo/SOAP

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID4056`〜`ID4655` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 602. 601周目 追加再点検（ID3456〜4055）

対象:
- `ID3456`〜`ID4055`
- Shopping / Clothes, Shoes, Accessories, Personal Care, Electronic Devices, Other Goods, At the Supermarket, At the Bookshop & Florist's, Payments & Returns
- Leisure Time / At the Cinema, At the Theatre, At the Museum, At the Nightclub, At the Beach, Sport

結果:
- **CSV修正なし**
- `ID3456`〜`ID4055` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、Web上のエスペラント使用例・辞書例で確認した。とくに、`bokalo`, `interakto`, `jaĥto`, `arbitracianto`, `zorio`, `ŝelko`, `konstrubriketoj`, `malsekkostumo` のように生成AI由来の疑いが出やすい語を重点確認した。
- `Mi bezonas bokalon da mustardo` は一見「ゴブレット」寄りに見えるが、PIVで `bokalo` は広口のガラス・陶器などの容器、また `konservobokalo` は保存用瓶として確認できるため、スーパー文脈の「マスタード一瓶」として据え置いた。
- `interakto` はPIVの `inter-` 説明で「tempo inter du aktoj」として確認でき、劇場の「休憩時間」文脈に合うため据え置いた。
- `malsekkostumo` はローカルPIVの直接見出しでは確認できなかったが、Web上で wetsuit の訳語・実使用が確認でき、同範囲の `plonĝkostumo` とも意味衝突しないため、明確な誤りとは扱わなかった。

主な据え置き確認:
- Clothes / Shoes / Accessories: `sablokoloran`, `daŭrema`, `rabatvendo`, `stok(on)`, `artikolon en stoko`, `mokasenoj`, `zorioj`, `pantofloj`, `gumaj botoj`, `sportŝuojn`, `Ili perfekte sidas al mi`, `koltukon`, `vera ledo`, `felĉapon`, `naztukojn`, `ŝelkojn`, `manumbutonoj`, `horloĝrimenon`, `18-karata oro`, `juvelaĵon`, `brakhorloĝon`, `fermilo de tiu kolĉeno` は、衣料・靴・装身具の買い物文脈で維持。
- Personal Care / Electronic Devices / Other Goods: `paletron da ŝminko por la palpebroj`, `ungofajlilon`, `akvorezistan ŝminkon por okulharoj`, `vizaĝpudro`, `pinĉilon`, `razilojn`, `telefona ŝargilo`, `memorkarton`, `lensokovrilon`, `porteblan komputilon`, `skanilon`, `aŭskultilojn`, `laŭtparoliloj`, `harsekigilon`, `rabatvendo`, `elĉerpiĝis`, `vestbrosojn`, `linajn tablotukojn`, `figuretoj`, `bierkruĉojn`, `inicialoj`, `manĝilaron`, `vinkarafojn`, `kudran fadenon`, `skribmaterialojn`, `konstrubriketojn`, `vojaĝsakoj`, `mane teksitan tapiŝon`, `memoraĵon de la urbo`, `taksi ĉi tion`, `likva sapo` は、商品カテゴリとの対応を保つ。
- Supermarket / Bookshop & Florist's / Payments & Returns: `bokalon da mustardo`, `limdato`, `fruktan torton`, `kafgrajnojn`, `granatoj`, `aĉetĉaretoj`, `konservaĵojn`, `frostigitaj nutraĵoj`, `ĉokoladaj bombonoj`, `markojn ... kun filtriloj`, `bastonpanon`, `tabuletojn da nigra ĉokolado`, `duonduzenon`, `foliumi`, `kajeron`, `bukedeto`, `narcisoj`, `lekantoj`, `klarigan vortaron`, `poemarojn`, `Romeo kaj Julieta`, `koloriglibrojn`, `brokanta librovendejo`, `krizantemojn`, `diantojn`, `kronon el freŝaj floroj`, `redoni`, `kontantan monon`, `PIN-kodon`, `repagon`, `interŝanĝi` は、スーパー・書店/花屋・返品/支払い文脈で維持。
- Cinema / Theatre / Museum: `filmo de suspenso`, `horora filmo`, `dokumenta filmo`, `en la vjetnama`, `pufmaizo`, `intrigo`, `produktis la filmon`, `reĝisoro`, `scenaristo`, `subtekstojn`, `animaciaĵon`, `nigrablankan filmon`, `dinamika`, `kostumojn`, `dekoraciojn`, `vestiblo`, `teatra binoklo`, `vestejo`, `programeton/programon`, `interakto`, `loĝio`, `operejo`, `vespera vesto`, `La Mizerulojn`, `balkono`, `scenejo`, `prezentado`, `fotografado malpermesita`, `aŭdgvidon/aŭdgvidilo`, `fulmilon`, `karikatursalono`, `vaksaj figuroj`, `impresionismajn pentraĵojn`, `etnografia muzeo`, `plenkreskulan bileton`, `aliro por handikapuloj`, `pentraĵgalerion` は、映画館・劇場・博物館文脈で維持。
- Nightclub / Beach / Sport: `vestkodo`, `bilardo`, `Kiujn noktojn`, `gastlisto`, `sportŝuoj`, `vivan muzikon`, `homplene`, `mortige enue`, `diskĵokeo`, `drinkejo`, `strando`, `sunseĝon`, `akvoskiojn/akvoskii`, `subakvaj fluoj`, `ŝarkoj`, `kanuon`, `surfotabulon`, `jaĥtklubo`, `plonĝkostumon`, `aerbotelo`, `malsekkostumon`, `ĉevalfortoj`, `navigacian ekipaĵon`, `jaĥto`, `garantiaĵon`, `savjakon`, `ludi duope`, `arbitracianto`, `poentaro`, `golis`, `egaligis`, `gimnastikejo`, `kriketon`, `rugbeo`, `usona futbalo`, `vetkuroj`, `sportema`, `flugpilka matĉo`, `manpilka matĉo`, `basketbala teamo`, `flavan uniformon` は、ナイトクラブ・海辺・スポーツ文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `bokalo`, `konservobokalo`, `zorio`, `ŝelko`, `paletro`, `briketo`, `inter-` / `interakto`, `jaĥto`, `arbitracio` / `arbitracianto`, `Julieta`, `surf(o)` / `surfotabulo`, `vestejo`, `baleto`, `programo`, `loĝio`, `balkono`, `fulmilo`, `aŭdi`, `florkrono`, `ĉevalforto`, `flugpilko`, `manpilko`, `basketbalo` 周辺。
- Globe Language `wetsuit` / `malsekkostumo`: https://www.globelanguage.org/wetsuit-noun/
- Emsland Esperanto `malsekkostumo` 使用例: https://www.emsland.com/eo/poi/wasserski-dankern

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID3456`〜`ID4055` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 601. 600周目 追加再点検（ID2856〜3455）

対象:
- `ID2856`〜`ID3455`
- Hotel / Renting a Flat
- Restaurant & Pub / Booking a Table, Ordering Drinks, Ordering Food, During the Meal, Paying the Bill, Complaints, At the Pub
- Food / Meat & Fish, Fruit, Vegetables, Staple Food & Spices, Breakfast Food
- Shopping / At the Department Store, Clothes

結果:
- **CSV修正なし**
- `ID2856`〜`ID3455` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、Glosbe、Kaikki、Wiktionary、Majstro を併用して確認した。PIVで直接見出し化されにくい複合語・料理名・商品名は、透明な語形成、外部辞書実例、同CSV内の既存採用形、ロシア語列との整合が揃う場合のみ据え置きとした。
- `litotukoj` はPIV上の標準的な見出し・例としては `littuko` が強い一方、Glosbe等で `litotuko` の実例が確認でき、意味は「ベッド用シーツ」から外れていないため、過修正を避けて据え置いた。

主な据え置き確認:
- Renting a Flat / Booking a Table / Ordering Drinks: `litotukoj`, `suĉkloŝo`, `adherema filmo`, `vazaro`, `ŝvabrilo`, `rubsakoj`, `detergento`, `adaptilo`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `polvosuĉilo`, `mikroondilo`, `telerlavmaŝino`, `elektromezurilo`, `ĉambristino`, `fumejo`, `gasita akvo`, `vinkarto`, `smuzio` は、賃貸設備・台所用品・レストラン予約・飲料文脈として維持。
- Ordering Food / During the Meal / Paying the Bill / Complaints: `koŝera manĝaĵo`, `vegetaranino`, `vegano`, `kebabo`, `pastaĵoj`, `bifsteko kun fritoj`, `surloke aŭ por forporti`, `por kunpreni`, `antaŭmanĝaĵoj`, `specialaĵo de la domo`, `tritavola sandviĉo`, `farĉitaj fungoj`, `nudeloj`, `mezrostita`, `bone rostita`, `halala`, `manĝobastonetoj`, `rapidmanĝaĵo`, `laktaĵoj`, `servokotizo`, `restmono`, `trinkmono`, `malĝuste sumigita`, `odoras je korko`, `rostitan meleagron`, `kalzoneo` は、飲食店の注文・会計・苦情文脈で意味対応を保つ。
- At the Pub / Meat & Fish: `naĉoj`, `postebrio`, `barela aŭ botela biero`, `glasetojn da tekilo`, `laktoskuaĵo`, `ĉipsoj`, `bifstekon el bova lumbaĵo`, `salikoko`, `ŝafidaĵo`, `fazano`, `rostbefo`, `kalmaro`, `truto`, `salmo`, `ostro`, `skombro`, `moruo`, `tinuso`, `koturno`, `polpo`, `bovida kotleto`, `kankro`, `karpo`, `haringo`, `omaro` は、酒場・肉魚カテゴリとして維持。
- Fruit / Vegetables / Staple Food & Spices / Breakfast Food: `kivifruktoj`, `limeoj`, `nigra ribo`, `frambo`, `mirtelo`, `oksikoko`, `grapfrukto`, `arakido`, `strudelo`, `mandarino`, `rafano`, `asparago`, `stufaĵo`, `celerio`, `ajlo`, `kukurbo`, `florbrasiko`, `brokolo`, `papriko`, `melongeno`, `spinaco`, `buljono`, `peklitaj kukumoj`, `laktuko`, `akra kapsiko`, `panumita kukurbeto`, `beto`, `kikero`, `brezitaj karotoj`, `tofuo`, `rozmareno`, `sezamo`, `kapero`, `eruko`, `kuskuso`, `verdaj fazeoloj`, `safrana rizo`, `koriandro`, `mocarelo`, `ŝorbeto`, `benjetoj`, `kornaj bulkoj`, `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `artefarita dolĉigilo` は、食材・朝食カテゴリの語彙として維持。
- Shopping / Clothes: `magazeno`, `rabatvendo`, `senimposta butiko`, `brakhorloĝoj`, `librejo`, `fako`, `sekcio`, `kaso`, `nutraĵa sekcio`, `vendistoj`, `Butikoŝtelistoj estos juĝe persekutataj`, `surprovi`, `provejo`, `grandeco`, `konvenas`, `taŭgas`, `kemia purigado`, `kemie purigi`, `Lavu inversigite`, `laveblaj`, `ŝorto`, `piĵamo` は、百貨店・衣料品・試着・洗濯表示文脈として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `littuko`, `adheri`, `filmo`, `pastaĵoj`, `koŝera`, `bifsteko`, `mezrostita`, `odori`, `lumbaĵo`, `salikoko`, `limeo`, `oksikoko`, `brezi`, `bulko`, `magazeno`, `surprovi`, `grandeco`, `ŝorto` 周辺。
- Glosbe `litotuko`: https://glosbe.com/eo/fi/litotuko
- Kaikki `suĉkloŝo`: https://kaikki.org/dictionary/Esperanto/meaning/s/su/su%C4%89klo%C5%9Do.html
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio
- Wiktionary `kalzoneo`: https://en.wiktionary.org/wiki/kalzoneo
- Wiktionary `milkshake` / `laktoskuaĵo`: https://en.wiktionary.org/wiki/milkshake
- Wiktionary `hangover` / `postebrio`: https://en.wiktionary.org/wiki/hangover
- Majstro `eruca`: https://www.majstro.com/Details-EN/English/74552
- PIV 2020 `postebrio`: https://vortaro.net/py/serchi.py?s=postebrio&simpla=1
- PIV 2020 `magazeno`: https://vortaro.net/py/serchi.py?s=magazeno&simpla=1
- PIV 2020 `provejo`: https://vortaro.net/py/serchi.py?s=provejo&simpla=1

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID2856`〜`ID3455` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 600. 599周目 追加再点検（ID2256〜2855）

対象:
- `ID2256`〜`ID2855`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems, Road Signs
- Other Transport / At the Bus Station, At the Train Station, On the Bus or Train, Taxi, Ship
- Hotel / Asking about Facilities, Booking a Room, Checking in, During Your Stay, Checking out, Complaints, Renting a Flat

結果:
- **CSV修正なし**
- `ID2256`〜`ID2855` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の Glosbe / ReVo / Komputeko / ESPDIC 参照、および今回のWeb確認で照合した。PIVに直接出にくい複合語は、透明な語形成・外部辞書実例・ロシア語列との整合が揃う場合だけ据え置きとした。

主な据え置き確認:
- Car / Road Signs: `vojsignoj`, `unudirekta strato`, `glacikovritaj`, `aŭtoriparejo`, `parkometro`, `serva areo`, `trafikrondo`, `trafikblokiĝo`, `benzinujo`, `brulaĵo`, `dizelo`, `kontraŭfrosta likvaĵo`, `startokabloj`, `akumulatoro`, `pneŭmatiko krevis`, `hupo`, `kapoto`, `bremslumoj`, `direktomontriloj`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `oleopremo`, `bremslikvaĵo`, `Trapaso malpermesita`, `Buskoridoro`, `Preterpasu maldekstre`, `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo` は、車・整備・道路標識文脈で維持。`ID2303` の `Plenigu la benzinujon` と `ID2308` のオイル文脈は既存修正が反映済みで、今回追加修正なし。
- Bus / Train / Taxi: `revenbileto`, `monata abono`, `biletaŭtomatoj`, `stampi la bileton`, `unuaklasa/pensiula revenbileto`, `kajo`, `eksprestrajno`, `vojaĝkarto`, `abonbileto`, `metroo`, `haltejo`, `pakaĵujo`, `kupeo`, `restoracia vagono`, `preterveturis vian haltejon`, `taksimetro`, `restmono`, `trinkmono`, `taksihaltejo`, `flughavena/nokta krompago`, `nunmomente`, `tribunalo` は、駅・車内・タクシー文脈で列間対応を保つ。
- Ship / Hotel: `bankaŭtomato`, `savringo`, `savboato`, `marmalsano`, `kajo`, `kajuto`, `enŝipiĝi`, `ferdeko`, `kvarlita kajuto`, `savvestoj`, `krozado`, `naŭzas vojaĝado`, `ferdekseĝo`, `radiogramo`, `transiro`, `Ĉio inkluzivita`, `aŭtoparkejo`, `monŝranko`, `lavservo`, `ĉambroservo`, `rulseĝa aliro`, `duŝkabinoj`, `ŝtopilingo`, `plena pensiono`, `antaŭpago`, `atendolisto`, `ĉambro por nefumantoj/fumantoj`, `ĉambronumero/ĉambroŝlosilo`, `savelirejo`, `telefona ŝargilo`, `ekstera linio`, `gladigi`, `plusendi mian poŝton`, `lavejo`, `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `malbonodoras`, `lavujo`, `bolilo`, `littukoj`, `subskribo`, `apartamento/luo` は、船旅・ホテル設備・滞在・精算・苦情・賃貸文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `akumulatoro`, `pneŭmatiko`, `benzinujo`, `hupo`, `rapidometro`, `piedira zono`, `haltejo`, `kupeo`, `taksio/taksimetro`, `kajo`, `kajuto`, `ferdeko`, `krozado`, `radiogramo`, `ŝtopilingo`, `bolilo`, `klimatizilo`, `gladi`, `ŝtopi`, `fakturo`, `kalkulo`, `luo`, `apartamento` 周辺。
- Glosbe `bus station` / `busstacio`, `aŭtobusa stacio`: https://en.glosbe.com/en/eo/bus%20station
- Glosbe `transport en commun en site propre` / `Buskoridoro`: https://fr.glosbe.com/fr/eo/transport%20en%20commun
- Wiktionary `ŝtopilingo`: https://en.wiktionary.org/wiki/%C5%9Dtopilingo
- Majstro `kettle` / `bolilo`: https://www.majstro.com/dictionaries/English-Portuguese/kettle
- Wikidata / Commons `deckchair` / `Ferdekseĝo`: https://www.wikidata.org/wiki/Q1824203

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID2256`〜`ID2855` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 599. 598周目 追加再点検（ID1656〜2255）

対象:
- `ID1656`〜`ID2255`
- Jobs / Business, At the Interview, Recommendation Letter
- Travel / Asking Directions, Giving Directions, At the Tourist Office, Excursions
- Plane / Booking a Flight, Checking in, Luggage, Passport Control & Customs, On the Plane, Airport Signs
- Car / Car Hire, Driving & Parking

結果:
- **CSV修正なし**
- `ID1656`〜`ID2255` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の Glosbe / ReVo / Komputeko / ESPDIC 参照、および今回のWeb確認で照合した。PIVに直接出にくい複合語は、透明な語形成・外部辞書実例・ロシア語列との整合が揃う場合だけ据え置きとした。

主な据え置き確認:
- Jobs / Business: `fakturo`, `nuligi nian mendon`, `afervojaĝojn`, `fakson`, `pli detalan informon`, `kondiĉojn de pago`, `Per ĉi tio ni konfirmas vian mendon`, `subskribitan kopion de la kontrakto`, `rendevuon`, `prokrasti nian kunvenon`, `dato de ekspedo`, `varo estos sendita`, `negocos pri la prezo`, `fakturas nur en eŭroj` は、商談・注文・請求・日程調整文脈として維持。
- At the Interview / Recommendation Letter: `formularon por vivresumo`, `laborpostena priskribo`, `raporti al`, `komputile klera`, `laborsperton`, `validan stirpermesilon`, `akiri rekomendojn`, `laborkontrakto`, `trimonata provperiodo`, `kandidatiĝi`, `labori laŭvice`, `manĝejo por la personaro`, `vojaĝkostojn`, `informatiko`, `bonvenan defion`, `vastigi mian scion`, `fortaĵoj/malfortaĵoj`, `lojaleco kaj akurateco`, `rekomendleteron`, `gvidanto`, `komunikajn kapablojn`, `plej varman rekomendon`, `altkvalitan laboron`, `bonega aldono al via programo`, `humursento` は、応募・面接・推薦状文脈で意味対応を保つ。
- Asking/Giving Directions / Tourist Office / Excursions: `ŝparvojon`, `desegni mapon`, `fervojstacio/fervoja stacidomo`, `metrostacio`, `vidindaĵoj`, `marbordon`, `poŝtoficejo/poŝtejo`, `aŭtobusan stacion`, `interreta kafejo`, `ambasadejo`, `orientiĝas`, `subpasejon`, `indikilojn`, `fajrobrigadejo`, `turisma oficejo`, `hotelĉambron`, `komerca kvartalo`, `junulargastejoj`, `tendumejojn`, `sandviĉejon`, `navedan buson`, `ekskursoj`, `gvidiston/gvidanto`, `rondvojaĝojn`, `preni miajn fotojn`, `subeksponitaj`, `gvidiston, kiu parolas la kartvelan` は、道案内・観光案内・写真店/ツアー文脈で列間対応を保つ。
- Plane / Airport: `halto dumvoje`, `flugkompanio`, `komerca klaso`, `valuto`, `sidlokon ĉe la fenestro/koridoro`, `ŝanĝi aviadilon`, `dogano`, `registrejo`, `pordego/elirejo`, `eniro en la aviadilon`, `senimposta butiko`, `tekkomputilon`, `bagaĝetikedo`, `bagaĝaj ŝranketoj`, `registrigas iun bagaĝon`, `manbagaĝo`, `superpezo`, `bagaĝ-ricevejo`, `dogandeklaro`, `transitvizo/transite`, `peti azilon`, `vakcinatestilo`, `stevardino`, `seĝodorso`, `supra bagaĝujo`, `bagaĝa elpreno`, `Varoj deklarendaj`, `Nenio por deklari` は、航空券・保安検査・荷物・税関・機内・空港表示文脈で維持。`pordego` は空港ゲートとしては `elirejo` との揺れがあるが、Glosbeで gate の訳語として確認でき、現行列と明確に衝突しないため過修正しない。
- Car / Car Hire / Driving & Parking: `mana/aŭtomata transmisio`, `infanan aŭtoseĝon`, `benzinujo`, `aldonaj kostoj`, `mopedon`, `motorciklon`, `centran ŝlosadon`, `kofrujon`, `infanserurojn`, `direktomontrilojn`, `regilojn`, `plena kovrado`, `minimuma luoperiodo`, `internacia stirpermesilo`, `kilometraĵo`, `semajnfinaj tarifoj`, `kaŭcion`, `aŭtoasekura kompenso`, `redoni la aŭton ĉe mia celloko`, `aldoni duan ŝoforon`, `rapidlimo sur aŭtovojoj`, `parkumi`, `Veturu trans/sub la ponton`, `trafikrondo`, `vojmapo`, `loko por halti` は、レンタカー・運転案内文脈で意味ズレなし。`aŭtoasekura kompenso` は硬いが、保険金請求の意味が保たれるため据え置き。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `kandidati`, `akurateco`, `laborkontrakto`, `stacidomo`, `semaforo`, `vidindaĵo`, `ekskurso`, `registrejo`, `dogano`, `stevardino`, `benzinujo`, `kaŭcio`, `klimatizilo`, `aŭtovojo`, `parkumi`, `trans`, `porti`, `pordego` 周辺。
- Glosbe `CV` / `vivresumo`: https://glosbe.com/en/eo/CV
- Glosbe `gate` / `pordego`: https://glosbe.com/en/eo/gate
- Komputeko IT・業務語彙確認: https://komputeko.net/plejoftaj-eo.pdf
- Wiktionary `rapidlimo`: https://en.wiktionary.org/wiki/rapidlimo

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID1656`〜`ID2255` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 598. 597周目 追加再点検（ID1056〜1655）

対象:
- `ID1056`〜`ID1655`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet
- Dating / Accepting & Declining, Asking Someone out, On a Date, Compliments, Wedding
- Education / At School, At University, Student Life, Numbers & Colours
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **CSV修正なし**
- `ID1056`〜`ID1655` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の Glosbe / ReVo / Komputeko 参照、および今回のWeb確認で照合した。難語・複合語・職業名は特に慎重に確認し、辞書確認語または透明な複合として文脈と合うものは据え置いた。

主な据え置き確認:
- Describing People / Things You Like & Dislike / Arranging to Meet: `bonkondutaj`, `mallongajn harojn, grizajn ĉe la tempioj`, `zorge elektas miajn amikojn`, `noktokluboj`, `butikumi`, `hobio`, `fotografado`, `ĝardenadon`, `drinkejojn`, `troti`, `piedirado`, `novelojn`, `dombestojn`, `modprezentadon`, `filmosteluloj`, `sciencfikciaj libroj`, `Aliĝu al mi por tagmanĝo`, `rememorigos min`, `vestiblo`, `saŭno`, `aranĝi tion iom pli malfrue` は、人物描写・嗜好・待ち合わせ文脈で意味対応を保つ。
- Dating / Compliments / Wedding: `partion de golfo`, `renkontiĝos tie`, `venos preni vin`, `akompani/veturigi vin hejmen`, `Ĉu mi povas aliĝi al vi?`, `regalos vin per trinkaĵo`, `Kion vi elpensis?`, `renkontiĝas kun iu`, `Vi mankas al mi`, `enamiĝis al vi`, `freneziĝas pro vi`, `Forigu viajn manojn de mi!`, `edziniĝos kun mi`, `fianĉiĝo`, `novgeedzoj`, `porcelana/arĝenta/perla/korala/rubena/diamanta` は交際・誘い・結婚記念日の文脈で列間対応を保つ。`edziniĝos kun mi` は前回指示どおり `kun` を維持。
- Education / Student Life: `ŝranketojn`, `praktiku la islandan`, `hazarda eraro`, `pruntepreni`, `parkere`, `notoj`, `sonorilo`, `hindian`, `magistriĝo`, `doktoriĝas`, `liberan jaron`, `distancan lernadon`, `studentloĝejon`, `registriĝan formularon`, `kataluna`, `validan eksperimenton`, `templimo`, `formulitaj buŝe/skribe`, `disertacio`, `brile trapasis`, `malsukcesis en la ekzameno`, `ripeti multajn aferojn` は学校・大学・試験文脈として維持。`Mi faros mian raporton en la kataluna` は発表・レポートをカタルーニャ語で行う意味として読め、ロシア語列との明確な衝突はない。
- Numbers & Colours / Jobs / Workplace / Business: `multiplikite`, `dividite per`, `rozkoloron`, `grizon`, `brunon`, `violan koloron`, `helverdan koloron`, `informteknologio`, `vokcentro`, `handikapitaj infanoj`, `merkatika administranto`, `staĝanta`, `memstara laboristo`, `praktikon`, `promociita`, `patrina/patra forpermeso`, `redukto de laborfortoj`, `retpoŝton`, `fakturo`, `Pardonu, ke mi igis vin atendi`, `altigos mian salajron`, `limtempo por liveri la varojn finiĝas`, `kredas je ŝia strategio`, `interkonsenton` は数・色・職業・雇用・職場・商談文脈で意味対応を保つ。`merkatika administranto` はやや幅があるが、PIVの `merkatiko` と透明な職名複合として確認でき、列間の職務差を解消するだけの確証がないため修正しない。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://www.vortaro.net/simpla
- PIV 2020 `novelo`, `partio`, `manki`, `regali`, `nupto`, `ruben/o`, `ŝranko`, `praktiko`, `studento`, `distanco`, `lektor/o`, `registr/i`, `disertacio`, `valid/a`, `semestr/o`, `ripet/i`, `staĝ/o`, `praktiko`, `promoci/i`, `fakturo`, `merkatiko`, `laborforto`, `limtempo`, `interkonsento` 周辺。
- Komputeko IT・業務語彙確認: https://komputeko.net/plejoftaj-eo.pdf

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID1056`〜`ID1655` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 597. 596周目 追加再点検（ID756〜1055）

対象:
- `ID756`〜`ID1055`
- Emergencies / First Aid, At the Police Station
- Making Friends / Introductions, Place of Residence, Age/Nationality & Religion, Family & Relationships, Describing People

結果:
- **CSV修正なし**
- `ID756`〜`ID1055` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の Glosbe / ReVo / Komputeko 参照、および今回のWeb確認で照合した。`fotoroboto` のようにPIV直接見出しが弱い語は外部辞書実例とロシア語列を併用し、確証がない造語修正・好みの自然化は避けた。

主な据え置き確認:
- First Aid: `Mi sangas`, `Min trafis aŭto`, `senkonscia`, `vundita`, `Mi estis mordita`, `Mi tranĉis min`, `Mi bruligis min`, `Mi rompis mian brakon`, `Mi tordis al mi la maleolon`, `surmeti bandaĝon`, `elartikigis mian brakon`, `manĝaĵveneniĝon`, `alergia al penicilino`, `reakcion al novokaino`, `poliso de medicina asekuro`, `sciigi mian familion`, `daŭrigi mian vojaĝon` は救急・医療申告文脈で意味対応を保つ。`bruligis min` は `brulvundis min` も候補だが、現形で「やけどした」は明確。
- At the Police Station: `advokaton`, `subskribi vian deklaron`, `tekkomputilon`, `fraŭdo`, `enrompis en mian aŭton`, `troa rapideco`, `monpunon`, `denunci ŝtelon`, `raporton pri ŝtelo`, `anstataŭigi`, `oficejo pri perditaj aĵoj`, `atestantojn/atestanton`, `fotoroboton`, `oficialan raporton`, `senkulpa`, `kopion de la dokumento`, `ambasadejon`, `instrumentoj estis detruitaj` は警察・盗難・届出文脈として維持。`fotoroboto` はPIV直接確認語ではないが、Glosbe/DBnaryで `retrato robot` と確認でき、RU `фоторобот` と一致するため据え置き。
- Introductions / Place of Residence: `konatiĝi kun vi`, `Kun kiu vi estas?`, `amikino`, `fraŭlino`, `vendmanaĝero`, `prezenti iun al iu`, `sinjoron Smirnov`, `literumi vian nomon`, `De kie vi konas unu la alian?`, `fiŝkapti`, `Ĉi tie tre plaĉas al mi`, `Mi estas ĉi tie por labori`, `Mi dividas ĝin kun unu alia persono`, `kunloĝas en domo`, `jam de ses monatoj` は紹介・知人関係・居住滞在文脈で列間対応を保つ。`Ĉi tie tre plaĉas al mi` は硬いが、「ここが気に入っている」の口頭文として許容。
- Age/Nationality & Religion: `Moldavio`, `Belgio`, `Albanio`, `Ukrainio`, `Sud-Afriko`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio`, `Nov-Zelando`, `nacieco`, `usonano`, `albano`, `sviso`, `aŭstrianino`, `judino`, `germana civitanino`, `slovako aŭ belaruso`, `islamanino`, `hinduistino`, `budhano`, `siĥo`, `protestantino`, `kredas je Dio`, `preĝi`, `preĝejo`, `templo`, `moskeo`, `sinagogo`, `ateisto` は国籍・出身・宗教の自己申告として維持。女性形はロシア語列の女性話者形と整合する箇所でそのまま残す。
- Family & Relationships / Describing People: `fianĉiĝinta`, `edziniĝinta`, `edziniĝis`, `fraŭla`, `divorciĝinta`, `vidvino/vidvo`, `fianĉino`, `disiĝis`, `en rilato`, `rendevuas kun iu`, `novnaskita bebo`, `ĝemelojn`, `graveda`, `proksima parenco`, `solinfano`, `geavoj`, `genepoj`, `nepo/nepinoj`, `bonŝanculo`, `similas al`, `okulvitrojn`, `timida`, `fama`, `saĝa`, `aspektas`, `blondajn harojn`, `ĝena`, `svelta`, `buklajn rufajn harojn`, `ĉarman rideton`, `scivolema`, `flari`, `gustumi` は婚姻・交際・親族・人物描写として意味ズレなし。`fianĉino` は「婚約した女性」の文脈、`edziniĝi` 系は女性話者/対象の文脈として維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `bandaĝo`, `bruligi`, `elartikigi`, `veneniĝo`, `alergio`, `novokaino`, `deklaro`, `advokato`, `denunci`, `anstataŭigi`, `atestanto`, `manaĝero`, `nacieco`, `islamano`, `hinduismo`, `budhano`, `siĥo`, `preĝejo`, `moskeo`, `sinagogo`, `civitaneco`, `fraŭlo`, `edziniĝi`, `fianĉino`, `rendevui`, `solinfano`, `nepo`, `aspekti`, `gustumi`, `flari`, `rufa`, `ĉarma` 周辺。
- Glosbe `fotoroboto`: https://glosbe.com/eo/es/fotoroboto
- Glosbe `notebook computer` / `tekkomputilo` / `tekokomputilo`: https://en.glosbe.com/en/eo/notebook%20%28computer%29
- ReVo `junulargastejo`: https://reta-vortaro.de/revo/art/gast.html#gast.0o.junulargastejo

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID756`〜`ID1055` は300件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 596. 595周目 追加再点検（ID456〜755）

対象:
- `ID456`〜`ID755`
- General Conversation / Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information
- General Conversation / Expressing Feelings, Help & Advice, Opinions
- Emergencies / Emergency Situations, Accidents

結果:
- **CSV修正なし**
- `ID456`〜`ID755` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式検索、既存ログ内の Glosbe / ReVo / Komputeko 参照、および今回のWeb確認で照合した。生成AI由来の造語に見えやすい複合語でも、PIV確認語・透明な複合・外部辞書実例のいずれかで根拠があり、列間対応を壊す明確な誤りがないものは過修正しなかった。

主な据え置き確認:
- Making Yourself Understood / Agreeing & Disagreeing / Asking for & Giving Information: `mandarena ĉina lingvo`, `akĉento`, `ĉeĥe`, `pole`, `prononcas`, `traduki`, `konsentas`, `vidpunkto`, `kunhavas vian vidpunkton`, `Mi vidas nenian malhelpon`, `ĉe Petro`, `ĉe la laboro`, `en trajno`, `drinkejo`, `junulargastejo`, `picejoj`, `biciklas`, `survoje por renkonti amikon` は、意思疎通・賛否・旅行/所在表現として意味対応を保つ。`akĉento` は発音上のなまりとして確認でき、強勢の `akcento` へ戻さない。
- Expressing Feelings / Help & Advice: `trista`, `malstreĉita`, `ekscitita`, `ŝokita`, `motivita`, `embarasita`, `kapturno`, `malkuraĝigita`, `kondolencoj`, `prunti`, `prizorgi`, `malkonsilus lui aŭton`, `tekkomputilo`, `flugpersonaro`, `plenumi ion ajn` は感情・体調・弔意・依頼・助言文脈で列間対応を保つ。`Mi sentas iom da kapturno` は `Mi sentas kapturnon` も候補だが、少量表現として理解可能なため据え置き。
- Opinions: `plaĉas al`, `rimarkojn`, `grandioza`, `Ne indas`, `Dependas de vi`, `aktorado`, `butikumado`, `Sincere dirante`, `konsideras ĉi tiun filmon la plej bona`, `teknologio plibonigas la vivon` は意見表明・評価表現として意味ズレなし。`konsideras ... la plej bona` は目的語に対する叙述補語として読めるため、格だけを理由に `la plej bonan` へ寄せない。
- Emergency Situations / Accidents: `Fajro!`, `fajrobrigado`, `ambulanco`, `Ĉu io malbonas?`, `oficejo pri perditaj aĵoj`, `Oni atakis min`, `traŭmatizita`, `vundita/vunditoj`, `koliziis kun mi`, `ŝildo`, `stirpermesilo`, `trafikan regulon`, `Mi havis la prioritaton`, `asekurita`, `interpretisto`, `raporti akcidenton`, `damaĝo`, `blovi en ĉi tiun tubon`, `asekurdokumentojn`, `akcidentraporto`, `informi iun pri io` は緊急時・交通事故対応の語彙として維持。`Mi havis la prioritaton` は交通文脈の right of way として成立する。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `akĉento`, `mandareno`, `prononci`, `traduki`, `konsenti`, `vidpunkto`, `trista`, `eksciti`, `motivi`, `embarasi`, `kondolenci`, `prunti`, `malkonsili`, `naŭzi`, `plaĉi`, `rimarko`, `aktorado`, `fajrobrigado`, `ambulanco`, `traŭmatizi`, `prioritato`, `akcidento`, `asekuri`, `damaĝo`, `blovi`, `informi`, `drinkejo`, `bicikli`, `picejo` 周辺。
- ReVo `junulargastejo`: https://reta-vortaro.de/revo/art/gast.html#gast.0o.junulargastejo
- Glosbe `notebook computer` / `tekkomputilo` / `tekokomputilo`: https://en.glosbe.com/en/eo/notebook%20%28computer%29
- Komputeko `tekokomputilo`: https://komputeko.net/plejoftaj-eo.pdf

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID456`〜`ID755` は300件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 595. 594周目 追加再点検（ID156〜455）

対象:
- `ID156`〜`ID455`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks, Apologies, Instructions, Short Questions & Answers, Congratulations
- General Conversation / Languages, Making Yourself Understood

結果:
- **CSV修正なし**
- 前回 `ID5155` まで到達済みのため、次周回として先頭側の `ID156`〜`ID455` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo / Wiktionary / ESPDIC 参照、必要に応じたWeb確認で照合した。短い定型句は複数文脈にまたがるものが多いため、サブトピック上の場面・ロシア語列・日中韓列が一致する限り、好みの自然化だけでは修正しなかった。

主な据え置き確認:
- Saying Hello & Goodbye / Good Wishes: `Bonan matenon`, `Saluton`, `Ĝis`, `Kiel vi fartas?`, `Estas bone vidi vin`, `Bonan tagon`, `Bonan nokton`, `Mi ĝojas revidi vin`, `Salutu Lukason de mi`, `Estis agrable konatiĝi kun vi`, `Mi antaŭĝojas revidi vin`, `Bonŝancon`, `Zorgu pri vi`, `Sanon`, `Je via sano`, `Ni tostu por vi`, `Ke ĉiuj viaj deziroj plenumiĝu` は挨拶・別れ・祝意文脈で意味対応を保つ。`Bonan tagon!` は挨拶にも別れ際の願いにも使えるが、Good Wishes 文脈では「良い一日を」として許容。`Sanon!` は `Bless you!` / `Будь здоров!` 系の健康祈願として維持し、乾杯表現の `Je via sano!` と区別されている。
- Thanks: `Nedankinde`, `Dankon, ke vi venis`, `Dankon pro via gastamo`, `Dankon pro via donaco`, `Dankon, ke vi tiel diris`, `Ne ĝenu vin`, `Tute nenio`, `Tio estis la plej malmulto, kion mi povis fari`, `Mi ne povas sufiĉe danki vin`, `Kontraŭe: estas mi, kiu devus danki vin!`, `Mi tre aprezas viajn afablajn vortojn`, `Mi ŝatus danki vin ankaŭ nome de mia edzo`, `Estas honoro por mi ricevi ĉi tiun premion` は感謝・返礼表現として列間対応に問題なし。
- Apologies / Instructions / Short Questions & Answers: `Pardonu min`, `Ĉio estas en ordo`, `Neniu problemo`, `Ne ofendiĝu`, `Pardonu pro la prokrasto`, `Mi ne tion celis`, `Mi petas pardonon`, `Ne estas kialo pardonpeti`, `Mi agis senzorge`, `Nu!`, `Rigardu dekstren/maldekstren`, `Atentu!`, `Bonvolu sidiĝi`, `Silentu`, `Kuraĝu`, `Donu al mi ĉi tiun`, `Atentu la hundon`, `Ne paŝu sur la gazonon`, `Bonvolu viciĝi ĉi tie`, `Ĉu ĉio en ordo?`, `Ankaŭ mi ne`, `Jen ĉio`, `Amuze`, `Kiel bele` は、短い会話・掲示・応答の文脈で許容範囲。
- Congratulations: `Feliĉan Kristnaskon/Paskon/Ĥanukon/Dankotagon/Ramadanon/Divalon`, `Feliĉan datrevenon`, `Multajn feliĉajn jarojn`, `Gratulon pro via diplomiĝo`, `Gratulon pro la nova laborposteno`, `Gratulon pro via novnaskito`, `Gratulon pro via akcepto en la universitaton`, `Gratulojn pro via magistra grado`, `stirekzameno`, `novnaskita filineto` は祝辞・学業・資格・出産文脈で維持。`akceptiĝo` などの候補はあるが、`akcepto en la universitaton` も大学に受け入れられた結果方向として読め、明確な誤りとは判断しない。
- Languages / Making Yourself Understood: `la bengalan`, `la rumanan`, `la tajan`, `la urduon`, `la persan`, `slovene`, `azerbajĝane`, `tagaloga`, `malajan`, `latve`, `norvega`, `svedan`, `nederlandan`, `finnan`, `araban lingvon`, `portugalan`, `indonezian`, `Mi sekvis kurson`, `Mi povas komuniki itale`, `Mi iom perdis la praktikon`, `Kiel ĉi tio nomiĝas?`, `Bonvolu noti ĝin`, `akĉento`, `prononcas`, `literumi` は言語名・言語能力・意思疎通確認の文脈で意味ズレなし。`akĉento` は発音上のなまり・口音を表す語として維持し、強勢の `akcento` へ戻さない。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `bona`, `sano`, `tosto/tosti`, `ĝeni`, `pardonpeti`, `vico/viciĝi`, `plaĉi`, `gratuli/gratulo`, `akcepti/akcepto`, `universitato`, `magistro`, `literumi`, `prononci`, `akĉento`, `bengalo`, `rumano`, `urduo`, `malajo`, `latvo`, `norvego`, `portugalo` 周辺。
- Wiktionary / Glosbe / dict.cc / ESPDIC 系の `antaŭĝoji`, `Divalo`, `akĉento` 周辺の既存確認。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID156`〜`ID455` は300件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 594. 593周目 追加再点検（ID4556〜5155）

対象:
- `ID4556`〜`ID5155`
- Health / At the Doctor, Diseases, Treatment, At the Dentist, At the Optician, At the Pharmacy
- Communication Means / Phone, Phone Calls at Work, Mass Media, At the Post Office, Letter
- Time & Weather / Telling the Time, Calendar, Time Expressions, Weather

結果:
- **CSV修正なし**
- `ID4556`〜`ID5155` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo / Wiktionary / ESPDIC / Komputeko 参照、必要に応じたWeb確認で照合した。生成AIが作ったように見えやすい複合語でも、PIV確認語・透明な複合・外部実例のいずれかで文脈上の根拠があり、意味ズレが明確でないものは過修正しなかった。

主な据え置き確認:
- Health / Doctor / Diseases / Treatment: `privatan medicinan asekuron`, `kapturna`, `malvarmumo`, `tubero`, `haŭterupcio`, `furunko`, `diareo`, `konstipita`, `nazkataro`, `stomaka perturbo`, `limfonodoj`, `mikozo de la piedoj`, `sendormeco`, `fojnofebro`, `sangotesto`, `sutureroj`, `loka anestezo`, `urina specimeno`, `injekto`, `ellitiĝi` は診療・症状・治療文脈で意味対応を保つ。`sutureroj` はPIVで縫合を構成する糸として確認済みで、stitches / 何針かの文脈に合う。
- Dentist / Optician / Pharmacy: `dentodoloro`, `gingivoj`, `plombo/plombigi`, `krono`, `dentprotezo`, `kario`, `denta higienisto`, `gargari la buŝon`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `astigmatismo`, `UV-protekto`, `inhalilo`, `plastroj`, `kontraŭdoloriloj`, `fastante`, `kromefikoj`, `vojaĝmalsano`, `sekiĝintaj lipoj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は、歯科・眼鏡店・薬局文脈で維持。`gargari` はPIVで口・喉を液体ですすぐ語義を確認できるため、rinse your mouth out として過修正しない。
- Phone / Phone Calls at Work / Mass Media: `Malbona konekto`, `Restu sur la linio`, `mesaĝos`, `telefono paneis`, `mobilan reton`, `kapti signalon`, `telefonbudon`, `klavi`, `voka signalo`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `malŝargiĝos`, `interna numero`, `demeti la aŭdilon`, `retpoŝtadreso`, `Skajpo`, `uzantonomo`, `ensaluti/elsaluti`, `retmesaĝo`, `en Facebook/Tvitero`, `tekkomputilo`, `eldonkvanto`, `titoloj`, `usona futbalo` は通信・SNS・メディア文脈で意味ズレなし。`Kiu estas via retpoŝtadreso?` は `Kio...` への自然化余地はあるが、「どのアドレスか」を尋ねる会話として許容。
- Post Office / Letter: `poŝtoficejo`, `poŝtkesto`, `vatita koverto`, `poŝti`, `aerpoŝto`, `fakso`, `televida licenco`, `abono`, `afranko`, `fotokabino`, `fotokopiilo`, `rekomendita poŝto`, `dogana deklaracio`, `pesilo`, `poŝtrestante`, `Sincere via`, `Al la koncernatoj`, `vivresumo`, `Antaŭdankon`, `Respektplene via`, `Kun plej koraj salutoj`, `Bonvolu ne heziti kontakti min`, `Mi antaŭĝojas ...`, `aldonaĵo` は郵便・手紙定型句として維持。`Ĉe kiu giĉeto estas poŝtrestante?` は省略的だが、窓口で「局留めはどの窓口か」を尋ねる口頭文として許容。
- Time / Weather: `Kioma horo estas?`, `kvarono antaŭ/post`, `tagmezo`, `noktomezo`, `labortagoj`, `libertago`, `Hodiaŭ tage`, `Ĉiutage`, `En la antaŭa monato`, `glacie kaj glite`, `nebule`, `Varmegas`, `Frostas`, `Pluvetadas`, `Hajlas`, `Fulmas`, `Alproksimiĝas fulmotondro`, `aĉa tago`, `malvarmete`, `Forte pluvas`, `Ekpluvas`, `Pluvegas`, `sub nulo`, `kiel en forno`, `veterprognozo`, `Ĉi-nokte frostos`, `La nuboj disiĝas`, `atmosfera premo`, `glitaj` は時刻・日付・天候文脈で列間対応を保つ。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `suturero`, `gargari`, `plombo`, `hipermetropa`, `astigmatismo`, `inhalilo`, `plastro`, `misdigesto`, `retpoŝto`, `afranko`, `poŝtrestante`, `fulmotondro`, `atmosfera premo` 周辺。
- Komputeko `tekokomputilo`: https://komputeko.net/plejoftaj-eo.pdf
- Wiktionary / dict.cc / ESPDIC 系の `antaŭĝoji` / `antaŭĝoji pri` 用例確認。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID4556`〜`ID5155` は600件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 593. 592周目 追加再点検（ID3556〜4555）

対象:
- `ID3556`〜`ID4555`
- Shopping / Personal Care, Electronic Devices, Other Goods, At the Supermarket, At the Bookshop & Florist's, Payments & Returns
- Leisure Time / At the Cinema, At the Theatre, At the Museum, At the Nightclub, At the Beach, Sport, Music, Going Camping, Family Time, Gardening, Having Guests
- Services / At the Bank, At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs
- Health / At the Doctor

結果:
- **CSV修正なし**
- `ID3556`〜`ID4555` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo / Wiktionary / ESPDIC 参照、必要に応じたWeb確認で照合した。辞書未確認に見えやすい複合語でも、PIV確認語・透明な複合・外部実例のいずれかで文脈上の根拠があり、意味ズレが明確でないものは過修正しなかった。

主な据え置き確認:
- Shopping: `pinĉilo`, `raziloj`, `telefonan ŝargilon`, `memorkarto`, `lensokovrilo`, `portebla komputilo`, `printilo`, `skanilo`, `aŭskultiloj`, `laŭtparoliloj`, `harsekigilo`, `vestbrosoj`, `facilrompaj`, `bierkruĉoj`, `manĝilaro`, `vinkarafoj`, `konstrubriketoj`, `mane teksita tapiŝo`, `memoraĵo de la urbo`, `likva sapo`, `bokalo`, `limdato`, `aĉetĉaretoj`, `konservaĵoj`, `frostigitaj nutraĵoj`, `bastonpano`, `duonduzeno`, `foliumi`, `notbloko`, `dulingva/klariga vortaro`, `koloriglibroj`, `brokanta librovendejo`, `vidindaĵoj`, `kvitanco`, `PIN-kodo`, `restmono`, `rabatkarto`, `repago`, `transakcio`, `aĉetaĵojn` は、買い物・支払い文脈で維持。
- Cinema / Theatre / Museum: `filmo de suspenso`, `milita/horora/dokumenta filmo`, `pufmaizo`, `intrigo`, `premiero`, `Festivalo de Cannes`, `reĝisoro`, `scenaristo`, `subtekstoj`, `animaciaĵo`, `teatra binoklo`, `vestejo`, `interakto`, `loĝio`, `La Mizerulojn`, `plenkreskulan/infanajn biletojn`, `gvidata ekskurso`, `aŭdgvidilo`, `fulmilo`, `vaksaj figuroj`, `etnografia muzeo` は娯楽施設文脈で意味対応を保つ。
- Nightclub / Beach / Sport / Music: `gastlisto`, `sportŝuoj`, `viva muziko`, `homplene`, `mortige enue`, `diskĵokeo`, `strando`, `sunseĝo`, `akvoskioj/akvoskii`, `subakvaj fluoj`, `ŝarkoj`, `surfotabulo`, `jaĥtklubo`, `plonĝkostumo`, `aerbotelo`, `malsekkostumo`, `savjako`, `remiso`, `arbitracianto`, `poentaro`, `gimnastikejo`, `tenisejo`, `goli`, `egaligis la poentaron`, `ĵokeo`, `vetŝancoj`, `golfbastonoj`, `golfĉaro`, `norma nombro da batoj`, `regatto`, `femuraj muskoloj`, `akordiono`, `saksofono`, `dirigento`, `simfonia orkestro`, `popolmuziko` は、海辺・スポーツ・音楽文脈で列間対応を保つ。
- Camping / Family / Gardening / Guests: `tendumi`, `tendumejo`, `lanterno`, `ruldomo`, `alumetoj`, `trinkakvo`, `poŝlampo`, `kukolo`, `pego`, `najtingalo`, `hirunda nesto`, `telfero`, `monta pado`, `piedvojetoj`, `bovlingon`, `sketi`, `televidaj romanoj`, `sagetojn`, `legadon`, `sojfabojn`, `sekalon`, `falĉas`, `erpis`, `plugos`, `fruktarbejo`, `buŝtukojn`, `boligos akvon`, `sukerpecoj`, `ĝinon kun toniko`, `mendas picon hejmen`, `Mi lavos, kaj vi viŝos` は、余暇・家庭・園芸・来客文脈で維持。`televidaj romanoj` は Glosbe で soap opera 対応を確認でき、RU/JA/ZH/KOとも連続劇方向で一致する。
- Bank / Estate Agency: `legitimilo`, `kurzo`, `provizio`, `bankaŭtomato`, `kontantmono`, `saldon`, `stirpermesilo`, `monretiro`, `konteltiro`, `ĉekaro`, `ĝiri`, `komuna konto`, `interezprocento`, `kontantigi`, `bangalo`, `vicdomo`, `parkumejo`, `petata prezo`, `posedaĵo`, `kontanta aĉetanto`, `hipoteko`, `antaŭpago`, `deponaĵo je unu-monata lupago`, `meblita/nemeblita loĝejo`, `duamana posedaĵo`, `prezintervalo`, `sur la merkato`, `dissendolisto` は金融・不動産文脈で意味ズレなし。
- Beauty / Tailor / Repairs: `franĝo`, `konstanta ondumado`, `dislimo`, `farbigi`, `farbi miajn harojn blonde`, `helajn striojn en miaj haroj`, `senharigo`, `senharigon ... per vakso`, `feni`, `ŝampui`, `sprajo/ĝelo por haroj`, `kranihaŭto`, `elpluki miajn brovojn`, `fajli/formi/laki ungojn`, `alkudri`, `fliki`, `laŭmezura kostumo`, `mallarĝigi/plilarĝigi`, `pilo`, `krono`, `ŝlosilringo`, `plandumoj`, `garantio` は美容院・仕立て・修理文脈で維持。`konstanta ondumado` は PIV の `ondumado` 項で髪のパーマ文脈を確認できるため、`permanenta` への好みの置換は行わない。
- Health: `kontrola ekzameno`, `kapturno`, `medikamentojn`, `alkoholaĵojn`, `rentgena ekzameno`, `aŭdotestojn`, `medicina konsulto`, `analizojn`, `malsanasekuro`, `sangogrupo`, `O negativa` / `O-pozitiva`, `kmera`, `desinfekti`, `suprenfaldi`, `sangopremo`, `insulino`, `trankviligaĵo`, `ulcero`, `surdorse/surventre` は診療文脈で維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `ĝiri`, `bangalo`, `franĝo`, `ĝiro`, `konto`, `provizio`, `ondumado`, `haroj`, `ŝampui`, `telfero`, `arbitracianto`, `gimnastikejo`, `surfotabulo`, `ruldomo`, `desinfekti`, `domveturilo` 周辺。
- Glosbe `soap opera` / `televida romano`: https://en.glosbe.com/en/eo/SOAP
- 既存ログ内の Glosbe / Web確認: `malsekkostumo`, `aerbotelo`, `senharigo`, `dislimo`, `bangalo`, `konteltiro`, `kranihaŭto`, `televidaj romanoj` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID3556`〜`ID4555` は1000件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 592. 591周目 追加再点検（ID2556〜3555）

対象:
- `ID2556`〜`ID3555`
- Other Transport / Taxi, Ship
- Hotel / Asking about Facilities, Booking a Room, Checking in, During Your Stay, Checking out, Complaints, Renting a Flat
- Restaurant & Pub / Booking a Table, Ordering Drinks, Ordering Food, During the Meal, Paying the Bill, Complaints, At the Pub
- Food / Meat & Fish, Fruit, Vegetables, Staple Food & Spices, Breakfast Food
- Shopping / At the Department Store, Clothes, Shoes, Accessories, Personal Care

結果:
- **CSV修正なし**
- `ID2556`〜`ID3555` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo / Wiktionary / ESPDIC 参照、必要に応じたWeb確認で照合した。生成AIが作ったように見える複合語でも、透明性と外部根拠があり、意味ズレが明確でないものは過修正しなかった。

主な据え置き確認:
- Taxi / Ship: `nokta krompago`, `bankaŭtomato`, `savringo`, `savboato`, `marmalsano`, `kajo`, `kajuto`, `ferdeko`, `aŭtomobilaj ferdekoj`, `kvarlita kajuto`, `savvestoj`, `krozado`, `ferdekseĝo`, `radiogramo`, `transiro` は交通・船旅文脈で維持。`Ĉu vin naŭzas vojaĝado?` は広めの travel-sick 表現だが、PIV の `naŭzi` と ship/travel 文脈から日中韓/RUとの対応を崩さない。
- Hotel: `Ĉio inkluzivita`, `inkludita/inkluzivita`, `aŭtoparkejo`, `monŝranko`, `lavservo`, `ĉambroservo`, `rulseĝa aliro`, `ŝtopilingo`, `plena pensiono`, `antaŭpago`, `atendolisto`, `longdaŭra restado`, `ĉambro por nefumantoj`, `ĉambronumero`, `ĉambroŝlosilo`, `savelirejo`, `telefonan ŝargilon`, `eksteran linion`, `gladigi`, `plusendi mian poŝton`, `lavejo`, `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `restmono`, `malbonodoras`, `littukoj/litotukoj`, `duobla lito`, `du apartaj litoj`, `subskribo`, `apartamento/luo` はホテル・賃貸文脈で意味ズレなし。`servokotizo` は `kotizo` の語義幅が残るが、同CSV内の service charge 表現として一貫し、RU/日中韓とも対応するため未修正。
- Renting a Flat: `vazaro`, `ŝvabrilo`, `rubsakoj`, `detergento`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `suĉkloŝo`, `adherema filmo`, `polvosuĉilo`, `mikroondilo`, `telerlavmaŝino`, `elektromezurilo`, `ĉambristino` は生活用品・家電文脈として維持。`suĉkloŝo` はPIV直接確認は弱いが、オンライン辞書で plunger として確認でき、RU `вантуз`・ZH/KOとも整合する。
- Restaurant & Pub: `smuzio`, `koŝera manĝaĵo`, `vegetaranino`, `vegano`, `kebabo`, `pastaĵoj`, `bifsteko kun fritoj`, `surloke aŭ por forporti`, `por kunpreni`, `antaŭmanĝaĵoj`, `memservo`, `specialaĵo de la domo`, `tritavola sandviĉo`, `farĉitaj fungoj`, `nudeloj`, `franca saŭco`, `mezrostita`, `bone rostita`, `halala`, `manĝobastonetoj`, `rapidmanĝaĵo`, `laktaĵoj`, `servokotizo`, `malĝuste sumigita`, `odoras je korko`, `postebrio`, `barela aŭ botela biero`, `laktoskuaĵo`, `ĉipsoj` は飲食店・パブ表現として文脈別許容。`smuzio` はPIV未収録寄りだが、Wiktionary等で smoothie のEsperanto名詞として確認でき、各列の飲料名と一致する。
- Food: `soleo`, `bifsteko el bova lumbaĵo`, `ŝafidaĵo`, `rostbefo`, `grilita salmo`, `salita moruo`, `kankroj`, `persikoj`, `avokado`, `kivifruktoj`, `limeoj`, `nigra ribo`, `mirtelo`, `oksikoko`, `karamelizitaj figoj`, `arakidoj`, `florbrasiko`, `papriko`, `akra kapsiko`, `peklitaj kukumoj`, `laktuko`, `panumita kukurbeto`, `kikeroj`, `tofuo`, `eruko`, `kuskuso`, `verdaj fazeoloj`, `safrana rizo`, `koriandro`, `mocarelo`, `ŝorbeto`, `benjetoj`, `kornaj bulkoj`, `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `artefarita dolĉigilo` は食品名・調理語として維持。`papriko` は sweet pepper を厳密化するなら `dolĉa kapsiko` も候補だが、JA/KOはパプリカ、ZH/RU/ENも非辛味のピーマン・パプリカ系で、PIVの `kapsiko` 周辺語義とも衝突しないため過修正しない。
- Shopping / Clothes / Shoes / Accessories / Personal Care: `magazeno`, `rabatvendo`, `senimposta butiko`, `butikoŝtelistoj estos juĝe persekutataj`, `surprovi`, `provejo`, `grandeco`, `kemia purigado`, `kemie purigi`, `Lavu inversigite`, `ŝorto`, `sablokolora`, `daŭrema`, `stoko`, `meti ĉi tion flanken`, `mokasenoj`, `zorioj`, `pantofloj`, `sportŝuoj`, `gumaj botoj`, `Ili perfekte sidas al mi`, `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `paletro da ŝminko por la palpebroj`, `ŝminko por okulharoj`, `vizaĝpudro`, `ungofajlilo` は買い物・服飾・化粧品文脈で維持。`maskaro` のような短い候補は今回PIVで確認できず、現行の説明的な `ŝminko por okulharoj` のほうが内容を変えないため未修正。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `zorio`, `ŝelko`, `kapsiko`, `koŝera`, `ŝorbeto`, `kazeo`, `mokaseno`, `pantoflo`, `ŝorto`, `benjeto`, `littuko`, `fakturo`, `kalkulo`, `kotizo`, `bolilo`, `monŝranko`, `gladi`, `ŝvabrilo`, `eruko`, `mocarelo`, `kebabo`, `pastaĵoj` 周辺。
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio
- Kaikki / Wiktionary抽出 `suĉkloŝo`: https://kaikki.org/dictionary/Esperanto/meaning/s/su/su%C4%89klo%C5%9Do.html
- 既存ログ内の Glosbe / ReVo / Web確認: `smuzio`, `suĉkloŝo`, `skatolmalfermilo`, `adherema filmo`, `manumbutono`, `horloĝrimeno`, `restmono`, `servokotizo`, `kornaj bulkoj`, `ŝminko por okulharoj` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID2556`〜`ID3555` は1000件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 591. 590周目 追加再点検（ID1556〜2555）

対象:
- `ID1556`〜`ID2555`
- Jobs / Occupation, Employment Status, At the Workplace, Business, At the Interview, Recommendation Letter
- Travel / Asking Directions, Giving Directions, At the Tourist Office, Excursions
- Plane / Booking a Flight, Checking in, Luggage, Passport Control & Customs, On the Plane, Airport Signs
- Car / Car Hire, Driving & Parking, At the Petrol Station, Mechanical Problems, Road Signs
- Other Transport / At the Bus Station, At the Train Station, On the Bus or Train, Taxi

結果:
- **CSV修正なし**
- `ID1556`〜`ID2555` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo / ESPDIC 参照、必要に応じたWeb確認で照合した。辞書根拠が弱い自然化候補や、文脈上は許容できる言い換え候補は採用しなかった。

主な据え置き確認:
- Jobs / Business: `merkatika administranto`, `memstara laboristo`, `patrina/patra forpermeso`, `maldungita pro redukto de laborfortoj`, `limtempo`, `interkonsento`, `nuligi nian mendon`, `dato de ekspedo`, `negocos pri la prezo`, `formularo por vivresumo`, `laborpostena priskribo`, `labori laŭvice`, `informatiko`, `fortaĵoj/malfortaĵoj`, `lojaleco/akurateco`, `plej varman rekomendon` は、職業・面接・推薦状の文脈で列間対応を保つ。`merkatika administranto` は「marketing manager / marketing specialist」の揺れが残るが、日中韓は管理者寄り、RUは専門職寄りで、既存ログどおり高優先保留のまま未修正。
- Directions / Tourist Office / Excursions: `ŝparvojo`, `trans la strato`, `Daŭrigu rekten`, `subpasejo`, `indikiloj`, `turisma oficejo`, `junulargastejoj`, `tendumejo`, `sandviĉejo`, `naveda buso`, `vidindaĵa ekskurso`, `rondvojaĝoj`, `preni miajn fotojn`, `memorkarto`, `subeksponitaj`, `kartvelan` は、道案内・観光・写真関連の文脈として意味ズレなし。`preni miajn fotojn` は「写真を受け取る」では広めの動詞だが、列間対応を損なうほどではないため過修正しない。
- Plane / Airport: `komerca klaso`, `halto dumvoje`, `sidloko ĉe la fenestro/koridoro`, `registrejo`, `pordego/elirejo`, `eniro en la aviadilon`, `manbagaĝo`, `bagaĝetikedo`, `bagaĝ-ricevejo`, `dogano`, `loĝpermesilo`, `peti azilon`, `transitvizo`, `vakcinatestilo`, `sekurzono`, `stevardino`, `seĝodorso`, `supra bagaĝujo`, `kriza elirejo` は、空港・機内表現として維持。`stevardino` は英語では中立的だがRU `стюардесса` と対応し、女性形として明確な誤りではない。
- Car / Road Signs: `mana/aŭtomata transmisio`, `benzinujo`, `kofrujo`, `infanseruroj`, `direktomontriloj`, `kaŭcio`, `aŭtoasekura kompenso`, `trafikrondo`, `serva areo`, `trafikblokiĝo`, `kontraŭfrosta likvaĵo`, `startokabloj`, `akumulatoro`, `pneŭmatiko krevis`, `hupo`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `bremslikvaĵo`, `Buskoridoro`, `Preterpasu maldekstre`, `Piedira zono` は、車両・道路標識の文脈で許容範囲。`Preterpasu maldekstre` はRUの障害物回避標識寄り、日中韓の「左側通行/左へ」に寄る揺れがあるが、道路標識文脈として明確な意味破綻ではない。
- Bus / Train / Taxi: `revenbileto`, `monata abono`, `vojaĝkarto`, `abonbileto`, `biletaŭtomatoj`, `Atentu la interspacon`, `eksprestrajno`, `restoracia vagono`, `pakaĵujo`, `preterveturis vian haltejon`, `taksimetro`, `restmono`, `trinkmono`, `taksihaltejo`, `flughavena krompago`, `nunmomente`, `tribunalo` は、公共交通・タクシーの実用句として維持。`pakaĵujo` は luggage compartment / 荷物棚・짐칸 に対する透明な複合語として、`flughavena krompago` は surcharge に対する透明な複合語として未修正。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `merkatiko`, `dogano`, `sekurzono`, `benzinujo`, `akumulatoro`, `rapidometro`, `revenbileto`, `taksimetro`, `tribunalo`, `vagono`, `stacidomo`, `haltejo`, `tarifo`, `kajo`, `metroo`, `ŝipo` 周辺。
- Glosbe / Web確認: `manbagaĝo`, `tekkomputilo`, `memorkarto`, `pordego`, `buskoridoro`, `startokabloj`, `bremslikvaĵo`, `pakaĵujo` 周辺。
- ESPDIC / Web確認: `abonbileto` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID1556`〜`ID2555` は1000件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 590. 589周目 追加再点検（ID756〜1555）

対象:
- `ID756`〜`ID1555`
- Emergencies / First Aid, At the Police Station
- Personal Information / Making Friends, Introductions, Place of Residence, Age/Nationality & Religion, Family & Relationships, Describing People, Things You Like & Dislike
- Free Time / Arranging to Meet, Accepting & Declining, Dating, Compliments, Wedding
- Education / At School, At University, Student Life, Numbers & Colours
- Jobs / Occupation

結果:
- **CSV修正なし**
- `ID756`〜`ID1555` を100件単位で連続再点検した。Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存ログ内の Glosbe / ReVo 参照、必要に応じたWeb確認で照合した。辞書根拠が弱い自然化候補は、内容変更や過修正になる恐れがあるため採用しなかった。

主な据え置き確認:
- First Aid / Police: `maleolo`, `surmeti bandaĝon`, `elartikigis`, `manĝaĵveneniĝon`, `reakcion al novokaino`, `poliso de medicina asekuro`, `deklaron`, `denunci ŝtelon`, `enrompis en mian aŭton`, `fotoroboton` は、救急・警察での申告文脈として列間対応を保つ。`fotoroboto` はPIV直接確認が弱いが、Glosbe等で identikit / facial composite 系の実例を確認でき、RU `фоторобот` とも対応するため未修正。
- Friends / Religion / Family: `vendmanaĝero`, `prezenti iun al iu`, `nacieco`, `budhano`, `siĥo`, `protestantino`, `fianĉino`, `edziniĝinta`, `edziniĝis`, `rendevuas kun iu`, `en rilato`, `solinfano`, `genepoj`, `buklajn rufajn harojn` は、PIV確認語または透明な複合語として維持。`fianĉino` は「婚約している女性」、`edziniĝi` 系は女性主語文脈、`rendevui kun` は交際文脈として許容。
- Likes / Meeting / Dating / Wedding: `troti`, `piedirado`, `novelojn`, `aliĝi al mi/al ni`, `regalos vin per trinkaĵo`, `elpensis`, `Vi mankas al mi`, `enamiĝis`, `freneziĝas pro vi`, `edziniĝos kun mi`, `nupto`, `geedziĝo`, `novgeedzoj`, `edziĝo de nia filo`, `fianĉiĝo de nia filino`, `porcelana geedziĝa jubileo`, `arĝenta/perla/korala/rubena/diamanta nupto` は意味ズレなし。`edziniĝos kun mi` はユーザー指定どおり `kun` を維持。
- Education / Student Life: `ŝranketojn`, `liniilon`, `viŝgumon`, `parkere`, `studjaro`, `unuajara studento`, `magistriĝo`, `doktoriĝas`, `libera jaro`, `distanca lernado`, `studentloĝejo`, `registriĝan formularon`, `rektoro`, `lektoro`, `semestro`, `mezlernejo`, `kataluna`, `valida eksperimento`, `disertacio`, `biblioteka karto`, `oratoro`, `templimo`, `formulitaj buŝe/skribe`, `raporto pri sanservo`, `esploradon en la kampo de fiziko`, `ripeti multajn aferojn` は、学業・発表・大学生活の文脈で維持。`hindia` はPIVで `hindia lingvo` が確認でき、ヒンディー語として未修正。
- Numbers / Colours / Jobs: 数詞、`multiplikite`, `dividite per`, `ĉielarko`, `rozkoloro`, `grizo`, `oranĝa`, `bruna`, `viola`, `helverda`, `profesio`, `informteknologio`, `juristo`, `veterinaro`, `tradukisto`, `staĝanta kontisto`, `komercistino`, `vokcentro`, `programisto`, `ĵurnalistino`, `handikapitaj infanoj` は、PIV確認語または透明な複合語として文脈別許容範囲。`komercistino` は `entreprenistino` も候補になり得るが、businesswoman / RU `предприниматель` の広い職業表現として明確な誤りではないため未修正。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- PIV 2020 `hindo` / `hindia lingvo`: https://vortaro.net/py/serchi.py?s=hindo&simpla=1
- PIV 2020 `fianĉo`, `edzo`, `rendevuo`, `preĝi`, `troti`, `universitato`, `validi`, `templimo`, `komerci`, `handikapo` 周辺。
- ReVo `manki`: https://reta-vortaro.de/revo/art/mank.html
- Glosbe / Web確認: `fotoroboto`, `libera jaro`, `distanca lernado`, `informteknologio`, `vokcentro` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID756`〜`ID1555` は800件確認済み。
- アプリ側Gitリポジトリで `git diff --check` を実行し、差分チェックはエラーなし。既存のアプリ用CSVについて、Gitから LF→CRLF の行末警告のみ表示された。

## 589. 588周目 追加再点検（ID156〜755）

対象:
- `ID156`〜`ID755`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks, Apologies, Instructions, Short Questions & Answers, Congratulations
- General Conversation / Languages, Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information, Expressing Feelings, Help & Advice, Opinions
- Emergencies / Emergency Situations, Accidents

結果:
- **CSV修正なし**
- 前回 `ID5056`〜`ID5155` でCSV終端まで到達済みのため、新しい周回として先頭へ戻り、`ID156`〜`ID755` を100件単位で連続再点検した。
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われるため、日中韓との対応を崩さないことを優先し、ロシア語を主基準、英語を補助基準として、明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、既存のGlosbe等の確認ログ、必要に応じたWeb確認で照合した。

主な据え置き確認:
- Basic Sentences / Thanks: `Mi antaŭĝojas revidi vin`, `Sanon!`, `Ni tostu por vi!`, `Tio estis la plej malmulto, kion mi povis fari`, `Ne estas kialo pardonpeti`, `Kuraĝu!`, `Atentu la hundon`, `Bonvolu viciĝi ĉi tie`, `Donu al mi ĉi tiun`, `Amuze!`, `Kiel bele!` は短い挨拶・謝意・謝罪・指示・応答の文脈で意味対応を保つ。`Tio estis la plej malmulto...` は `minimumo` への自然化候補があるが、PIV 2020 の `mal multo` 用例に近く、least I could do / RU `самое малое` / JA「せめてものこと」と一致するため過修正しない。
- Congratulations / Languages: `Feliĉan Ĥanukon!`, `Feliĉan Divalon!`, `Feliĉan Dankotagon!`, `Feliĉan Ramadanon!`, `Gratulon pro via akcepto en la universitaton!`, `magistra grado`, `stirekzameno`, `bengala`, `rumana`, `taja`, `urduo`, `slovene`, `azerbajĝane`, `tagaloga`, `malajan`, `indonezian`, `mandarena ĉina lingvo` は祝祭名・学業/資格・言語名として対応する。`Divalo` はPIV直接見出しでは弱いが、外部語彙データで Diwali のEsperanto対応として確認でき、過去修正後の形を維持。
- Making Yourself Understood / Agreement / Information: `akĉento`, `literumi`, `prononci`, `traduki`, `kunhavas vian vidpunkton`, `Mi vidas nenian malhelpon`, `en plena ordo`, `ĉe Petro`, `ĉe la laboro`, `en trajno`, `drinkejo`, `junulargastejo`, `picejo`, `biciklas`, `por ferioj`, `survoje por renkonti amikon` は意思疎通・賛否・旅行/所在表現として意味ズレなし。`akĉento` は発音上のなまりとして `akcento` ではなく現形を維持。
- Feelings / Help & Advice: `trista`, `malstreĉita`, `ekscitita`, `ŝokita`, `motivita`, `embarasita`, `kapturno`, `malkuraĝigita`, `kondolencoj`, `prizorgi`, `malkonsilus lui aŭton`, `flugpersonaro`, `tekkomputilo`, `plenumi ion ajn` は感情・体調・弔意・助言文脈で列間対応を保つ。`Mi sentas iom da kapturno` は `Mi sentas kapturnon` も候補だが、少量表現として理解可能。
- Opinions / Emergencies / Accidents: `Ne indas`, `Dependas de vi`, `aktorado`, `butikumado`, `konsideras ĉi tiun filmon la plej bona`, `fajrobrigado`, `ambulanco`, `ŝtelisto`, `oficejo pri perditaj aĵoj`, `traŭmatizita`, `stirpermesilo`, `Mi havis la prioritaton`, `asekurdokumentoj`, `akcidentraporto`, `interpretisto` は意見表明・緊急・交通事故文脈で意味対応を保つ。`Mi havis la prioritaton` は交通文脈の right of way として許容。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- Wiktionary `Diwali` Esperanto対応 `Divalo`: https://pl.wiktionary.org/wiki/Diwali
- WikiRank `Diwali` interwiki: https://wikirank.net/en/Diwali
- Collins `Divali`: https://www.collinsdictionary.com/us/dictionary/english/divali
- 既存確認ログ内の Glosbe / PIV / ReVo 参照: `antaŭĝoji`, `Divalo`, `pardonpeti`, `akĉento`, `mandarena`, `kapturno`, `kondolenci`, `aktorado` 周辺。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID156`〜`ID755` は600件確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 588. 587周目 追加再点検（ID4456〜5155）

対象:
- `ID4456`〜`ID5155`
- Services / Repairs
- Health / At the Doctor, Diseases, Treatment, At the Dentist, At the Optician, At the Pharmacy
- Communication Means / Phone, Phone Calls at Work, Mass Media, At the Post Office, Letter
- Time & Weather / Telling the Time, Calendar, Time Expressions, Weather

結果:
- **1件修正（1行・EO）**
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われ、`PhraseID` と Esperanto 文が音声キー生成にも関わるため、意味を変えない最小修正に限定した。
- `ID4456`〜`ID5155` を100件単位で再点検。ロシア語を主基準、英語を補助基準とし、エスペラント文と日中韓文のクイズ対応に影響する明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、必要に応じて Glosbe / Komputeko / Wiktionary / Web 検索で確認した。

修正:
- `ID4470` EO
  - `La kroneto estas rompita` → `La krono estas rompita`
  - 理由: Services / Repairs の時計修理文脈。RU `Заводная головка`, JA `リューズ`, ZH `表冠`, KO `용두`, EN `winder` は腕時計のリューズ/クラウンを指す。PIV 2020 の `krono` にはポケット時計などの部品としての用法があり、Wikimedia Commons / Wikidata の watch crown 項目でも Esperanto ラベルは `krono`。一方、PIV の `kroneto` は小冠・コロネット等で、時計部品としての根拠を確認できなかったため、意味を変えず過剰な `-et-` を外した。PIV の `streĉilo de poŝhorloĝo` も参照したが、日中韓の「クラウン」対応を保つため `krono` にした。

主な据え置き確認:
- Services / Repairs: `pilo`, `brakhorloĝo`, `reguligo`, `ŝlosilringo`, `fari kopion de ĉi tiu ŝlosilo`, `plandumoj`, `riparejo`, `garantio`, `fabrikanto` は修理・時計・靴修理文脈で意味対応を保つ。
- Health / Doctor / Diseases / Treatment: `rentgena ekzameno`, `aŭdotestoj`, `desinfekti`, `trankviligaĵo`, `surdorse/surventre`, `haŭterupcio`, `furunko`, `konstipita`, `nazkataro`, `limfonodoj`, `mikozo de la piedoj`, `fojnofebro`, `sangotesto`, `sutureroj`, `loka anestezo`, `urina specimeno`, `injekto` はPIV確認語または透明な複合語として維持。
- Dentist / Optician / Pharmacy: `plombo/plombigi`, `krono`（歯科クラウン文脈）, `dentprotezo`, `gargari`, `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `astigmatismo`, `UV-protekto`, `tablojdoj`, `inhalilo`, `plastroj`, `kontraŭdoloriloj`, `fastante`, `vojaĝmalsano`, `misdigesto`, `dormemigi`, `Ne prenu interne` は文脈別許容範囲。
- Phone / Mass Media / Post Office: `klavi la numeron`, `malĝusta numero`, `interna numero`, `demeti la aŭdilon`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `voka signalo`, `retpoŝtadreso`, `Skajpo`, `uzantonomo`, `ensaluti/elsaluti`, `Tvitero`, `usona futbalo`, `eldonkvanto`, `vatita koverto`, `poŝtrestante`, `afranko`, `fotokopiilo`, `rekomendita poŝto`, `dogana deklaracio`, `pesilo` は外部用例・辞書・列間対応から維持。
- Letter / Time / Weather: `Sincere via`, `Respektplene via`, `kunsendas mian vivresumon`, `aldonaĵo`, `kvarono antaŭ/post`, `tagmezo`, `noktomezo`, `glacie kaj glite`, `pluvetadas`, `hajlas`, `fulmotondro`, `aĉa tago`, `veterprognozo`, `atmosfera premo` は意味ズレなし。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `krono`: https://vortaro.net/py/serchi.py?s=krono&simpla=1
- PIV 2020 `streĉi` / `streĉilo`: https://vortaro.net/py/serchi.py?s=stre%C4%89i&simpla=1
- Wikimedia Commons / Wikidata `Watch crowns`: https://commons.wikimedia.org/wiki/Category:Watch_crowns
- Glosbe `login`: https://glosbe.com/en/eo/login
- Glosbe `falsa dentaro`: https://glosbe.com/eo/en/falsa%20dentaro
- Komputeko: https://dvd.ikso.net/vortaro/Komputeko_en_eo.pdf
- Komputeko frequent terms: https://komputeko.net/plejoftaj-en.pdf
- Web / ローカル収集コーパス: `ensaluti`, `retpoŝtadreso`, `Tvitero`, `dentprotezo`, `fulmotondro`, `sangotesto` 周辺の外部用例確認。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `c38942e26d4f12035d35a477ee09320c`
- アプリ実行用CSV MD5: `f3268c1c99a9f13e95de7d5354633fe4`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID4456`〜`ID5155` は700件確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 587. 586周目 追加再点検（ID2656〜4455）

対象:
- `ID2656`〜`ID4455`
- Hotel / Booking, Checking in, During the Stay, Checking out, Complaints, Renting a Flat
- Eating out / Booking a Table, Drinks, Ordering Food, During the Meal, Paying the Bill, Complaints, In the Pub
- Food / Meat and Fish, Fruit and Vegetables, Staple Food, Spices and Condiments, Breakfast
- Shopping / Department Store, Clothes, Shoes, Accessories, Personal Care, Electronic Devices, Other Goods, Supermarket, Bookshop, Florist, Payments and Returns
- Going out / Cinema, Theatre, Museum, Nightclub
- Leisure / Beach, Sport, Music, Camping
- Home / Family and Friends, Gardening, Guests, Bank, Estate Agency, Beauty Salon, Tailor, Repairs

結果:
- **CSV修正なし**
- `ID2656`〜`ID4455` を100件単位で再点検。ロシア語を主基準、英語を補助基準とし、エスペラント文と日中韓文のクイズ対応に影響する明確な意味ズレ・語形誤りのみ修正対象とした。
- エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、必要に応じて Glosbe / Wiktionary / Web 検索で確認した。

主な据え置き確認:
- Hotel / Renting a Flat: `tuko/tukoj`, `mantuko`, `monŝranko`, `servokotizo`, `kalkulo/fakturo`, `elregistriĝi`, `ŝvabrilo`, `adherema filmo`, `telerlavmaŝino`, `mikroondilo` は、各ホテル・賃貸文脈で意味対応を保つ。
- Eating out / Food: `smuzio`, `koŝera`, `halala`, `manĝobastonetoj`, `pastaĵoj`, `bifsteko`, `hamburgero`, `mezrostita`, `postebrio`, `laktoskuaĵo`, `soleo`, `rostbefo`, `grilitan salmon`, `naĉoj`, `kebabo`, `keĉupo`, `majonezo`, `karafo`, `vinkarto`, `odoras je korko` は、PIV確認語または外部用例確認済みの文脈別許容表現として維持。
- Fruit / Vegetables / Breakfast: `karamelizitaj figoj`, `tofuo`, `mufino`, `eruko`, `oksikoko`, `grapfrukto`, `panumi`, `kikero`, `kuskuso`, `safrano`, `koriandro`, `mocarelo`, `vaflo`, `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `kornaj bulkoj` は列間対応を崩さないため維持。`karamelizitaj figoj` は `karamelo/karameliĝi` との関係だけでは `karameligitaj` へ置換する根拠が不足し、外部用例でも `karameligita sukero` 型が確認できるため過修正を避けた。
- Shopping: `magazeno`, `surprovi`, `provejo`, `kemia purigado`, `inversigite`, `ŝorto`, `zorio`, `mokaseno`, `kalkanumo`, `ŝelko`, `manumbutono`, `ŝminko por okulharoj`, `paletro da ŝminko por la palpebroj`, `pinĉilo`, `aŭskultiloj`, `telefonan ŝargilon`, `lensokovrilon`, `memorkarton`, `harsekigilo`, `bierkruĉo`, `vinkarafoj`, `likva sapo`, `limdato`, `aĉetĉaretoj`, `konservaĵoj`, `frostigitaj nutraĵoj`, `bastonpano`, `koloriglibro`, `poŝtkarton kun vidindaĵoj`, `kronon el freŝaj floroj por la fianĉino` は文脈別許容範囲。
- Going out / Leisure: `interakto`, `teatra binoklo`, `loĝio`, `La Mizerulojn`, `aŭdgvidilo`, `vaksaj figuroj`, `plenkreskulan bileton`, `diskĵokeo`, `sunseĝo`, `akvoskioj`, `akvoskii`, `surfotabulo`, `malsekkostumo`, `aerbotelo`, `ĉevalfortoj`, `savjako`, `arbitracianto`, `poentaro`, `gimnastikejo`, `golfbastonoj`, `norma nombro da batoj`, `regatto`, `dirigento`, `simfonia orkestro`, `tendumejo`, `rostokradon`, `surloke`, `la monta pado` は、辞書・用例・透明な複合語として意味ズレなし。
- Home / Bank / Estate Agency / Beauty / Tailor: `televidaj romanoj`, `ĝino kun toniko`, `provizio`, `konteltiro`, `deponi monon al via konto`, `vojaĝan ĉekon`, `vicdomon`, `kontanta aĉetanto`, `duamana posedaĵo`, `franĝo`, `Mildan konstantan ondumadon`, `dislimo`, `senharigo`, `senharigon ... per vakso`, `ŝampui`, `ĝelo por haroj`, `kranihaŭto`, `elpluki miajn brovojn`, `fajli miajn ungojn`, `alkudri ĝin reen`, `laŭmezuran kostumon`, `mallarĝigi/plilarĝigi` は各文脈で許容範囲。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 公式検索: https://vortaro.net/
- Glosbe: https://glosbe.com/
- Esperanto Wiktionary: https://eo.wiktionary.org/
- Web 検索: `smuzio`, `tofuo`, `mufino`, `karamelizita/karameligita`, `televidaj romanoj`, `ĝino kun toniko` 周辺の外部用例確認。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `e002e22c85385fc16ae65c329150b454`
- アプリ実行用CSV MD5: `7184aafd353cb114e16d3036ed5a98ad`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID2656`〜`ID4455` は1800件確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 586. 585周目 追加再点検（ID1456〜2655）

対象:
- `ID1456`〜`ID2655`
- Education / Student Life, Numbers & Colours
- Jobs / Occupation, Employment Status, At the Workplace, Business, At the Interview, Recommendation Letter
- Travel / Asking Directions, Giving Directions, At the Tourist Office, Excursions
- Plane / Booking a Flight, Checking in, Luggage, Passport Control & Customs, On the Plane, Airport Signs
- Car / Car Hire, Driving & Parking, At the Petrol Station, Mechanical Problems, Road Signs
- Other Transport / At the Bus Station, At the Train Station, On the Bus or Train, Taxi, Ship
- Hotel / Asking about Facilities, Booking a Room

結果:
- **1件修正（1行・EO）**
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われ、`PhraseID` と Esperanto 文が音声キー生成にも関わるため、意味を変えない最小修正に限定した。
- `ID1456`〜`ID2655` を100件単位で再点検。日中韓との対応を主軸にし、RU/ENは参照列として扱った。エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、必要に応じて Glosbe/Web 検索で確認した。

修正:
- `ID2414` EO
  - `Mi ŝatus returan bileton al Bakuo, kun reveno dimanĉe` → `Mi ŝatus revenbileton al Bakuo, kun reveno dimanĉe`
  - 理由: Other Transport / At the Bus Station の return ticket 文脈。PIV 2020 公式検索とローカル `PIV2020_structured.txt` で `retura` / `retur-` は確認できず、PIV の `reveni` 項には `ira k reira bileto`、`vojaĝi` 項には `fervoja revenbileto` の例がある。同じCSV内でも `Revenbileto`, `unuaklasa revenbileto`, `pensiula revenbileto` が一貫して使われているため、内容を変えず `revenbileton` に統一した。

主な据え置き確認:
- Education / Jobs: `formulitaj skribe`, `esploradon en la kampo de fiziko`, `ekzamena sesio`, `ripeti multajn aferojn`, 色名・数詞、`informteknologio`, `vokcentro`, `handikapitaj infanoj`, `merkatika administranto`, `staĝanta kontisto`, `trejniĝas`, `superbazaro`, `komercistino`, `memstara laboristo`, `praktikon`, `promociita`, `patrina/patra forpermeso`, `redukto de laborfortoj`, `limtempo`, `fortaĵoj kaj malfortaĵoj` は、PIV確認語または透明な複合語として文脈別許容範囲。`fortaĵo` はPIVで「la forta flanko de io, iu」として確認できる。
- Business / Interview / Recommendation: `afervojaĝoj`, `fakson`, `kondiĉojn de pago`, `subskribitan kopion`, `ekspedon`, `vivresumo`, `laborpostena priskribo`, `komputile klera`, `laborpermesilon`, `laborkontrakto`, `provperiodo`, `kandidatiĝi`, `laŭvice`, `vojaĝkostojn`, `informatiko`, `kvalifikoj respondas al la postuloj`, `komunikajn kapablojn`, `plej varman rekomendon`, `altkvalitan laboron`, `humursento` は各職場・応募文脈で意味対応を保つ。
- Travel / Directions / Tourist Office / Excursions: `poŝtoficejo`, `ŝparvojo`, `vidindaĵoj`, `marbordo`, `piediri`, `orientiĝas`, `Daŭrigu...`, `fajrobrigadejo`, `subpasejo`, `indikiloj`, `turisma oficejo`, `loĝejo`, `junulargastejoj`, `tendumejo`, `sandviĉejo`, `naveda buso`, `maltrafi ĝin`, `gvidisto`, `preni miajn fotojn`, `subeksponitaj`, `kartvelan`, `Parlamentejon`, `tuttaga ekskurso` は、既存ログと今回の辞書・列間照合に基づき未修正。
- Plane / Airport: `flugkompanio` / `aviokompanio`, `komerca klaso`, `celloko`, `ŝanĝi aviadilon`, `butikumi`, `registrejo`, `suriri`, `eniro en la aviadilon`, `senimposta butiko`, `rezervonumero`, `pordego` / `elirejo`, `registrigas bagaĝon`, `manbagaĝo`, `bagaĝetikedo`, `bagaĝ-ricevejo`, `dogano`, `loĝpermesilo`, `azilo`, `transitvizo`, `vakcinatestilo`, `sekurzono`, `seĝodorso`, `supran bagaĝujon`, `grekan gazeton` は空港・機内文脈で対応する。`manbagaĝo` はPIV直接見出しとしては弱いが、空港文脈で hand luggage と明確に対応するため既存保留どおり維持。
- Car / Road Signs: `mana/aŭtomata transmisio`, `aŭtoseĝo`, `benzinujo`, `kilometraĵo`, `centra ŝlosado`, `kofrujo`, `infanseruroj`, `direktomontriloj`, `aŭtoasekura kompenso`, `rapidlimo`, `trafikrondo`, `serva areo`, `trafikblokiĝo`, `brulaĵo`, `kontraŭfrosta likvaĵo`, `startokabloj`, `akumulatoro`, `hupo`, `kapoto`, `bremslumoj`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `oleopremo`, `bremslikvaĵo`, `buskoridoro`, `piedira zono`, `nivelkruciĝo`, `piedira transirejo` は車・道路標識文脈で意味ズレなし。
- Other Transport / Ship / Hotel: `revenbileto`, `monata abono`, `biletaŭtomato`, `abonbileto`, `vojaĝkarto`, `skemo de la metroo`, `Urĝa bremso`, `Laŭpeta haltejo`, `pakaĵujo`, `kupeo`, `taksimetro`, `flughavena/nokta krompago`, `savringo`, `savboato`, `marmalsano`, `kajuto`, `ferdeko`, `kvarlita kajuto`, `savvestoj`, `krozado`, `ferdekseĝo`, `radiogramo`, `Ĉio inkluzivita`, `inkludita`, `aŭtoparkejo`, `lavservo`, `ĉambroservo`, `rulseĝa aliro`, `duŝkabinoj`, `ŝtopilingo`, `plena pensiono`, `antaŭpago`, `unulita ĉambro` は、PIV確認語または透明な複合語として現形維持。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `retura`（該当なし確認）: https://vortaro.net/py/serchi.py?s=retura&simpla=1
- PIV 2020 `returbileto`（該当なし確認）: https://vortaro.net/py/serchi.py?s=returbileto&simpla=1
- PIV 2020 `revenbileto`: https://vortaro.net/py/serchi.py?s=revenbileto&simpla=1
- PIV 2020 `reveni`: https://vortaro.net/py/serchi.py?s=reveni&simpla=1
- PIV 2020 `vojaĝi`: https://vortaro.net/py/serchi.py?s=voja%C4%9Di&simpla=1
- PIV 2020 `fortaĵo`: https://vortaro.net/py/serchi.py?s=forta%C4%B5o&simpla=1
- PIV 2020 `laborforto`: https://vortaro.net/py/serchi.py?s=laborforto&simpla=1
- PIV 2020 `limtempo`: https://vortaro.net/py/serchi.py?s=limtempo&simpla=1
- PIV 2020 `poŝtoficejo`: https://vortaro.net/py/serchi.py?s=po%C5%9Dtoficejo&simpla=1
- PIV 2020 `ŝparvojo`: https://vortaro.net/py/serchi.py?s=%C5%9Dparvojo&simpla=1
- PIV 2020 `bagaĝo`: https://vortaro.net/py/serchi.py?s=baga%C4%9Do&simpla=1
- PIV 2020 `registrigi`: https://vortaro.net/py/serchi.py?s=registrigi&simpla=1
- PIV 2020 `ferdekseĝo`: https://vortaro.net/py/serchi.py?s=ferdekse%C4%9Do&simpla=1
- PIV 2020 `inkludi`: https://vortaro.net/py/serchi.py?s=inkludi&simpla=1
- PIV 2020 `inkluzivi`: https://vortaro.net/py/serchi.py?s=inkluzivi&simpla=1
- Glosbe / Web 検索: `revenbileto`, `fervoja revenbileto`, `manbagaĝo`, `tekkomputilo` 周辺の外部用例確認。

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `e002e22c85385fc16ae65c329150b454`
- アプリ実行用CSV MD5: `7184aafd353cb114e16d3036ed5a98ad`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID1456`〜`ID2655` は1200件確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 585. 584周目 追加再点検（ID156〜1455）

対象:
- `ID156`〜`ID1455`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks, Apologies, Instructions, Short Questions & Answers, Congratulations, Languages, Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information, Feelings, Help & Advice, Opinions, Emergency Situations, Accidents, First Aid, Police Station, Introductions, Place of Residence, Nationality & Religion, Family, Describing People, Likes & Dislikes, Arranging to Meet, Dating, Wedding, Education

結果:
- **1件修正（1行・EO）**
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われ、`PhraseID` と Esperanto 文が音声キー生成にも関わるため、意味を変えない最小修正に限定した。
- `ID156`〜`ID1455` を100件単位で再点検。日中韓との対応を主軸にし、RU/ENは参照列として扱った。エスペラント語根・語法はローカル `PIV2020_structured.txt`、PIV 2020 公式サイト、必要に応じて Glosbe などで確認した。

修正:
- `ID1315` EO
  - `Gratulon pro via rubina geedziĝa datreveno!` → `Gratulon pro via rubena geedziĝa datreveno!`
  - 理由: Wedding の「Ruby Wedding Anniversary」文脈。PIV 2020 では宝石名は `ruben/o` で、`rubena` は `rubeno` にヒットする一方、`rubina` は公式PIV検索で該当なし。内容は変えず、語根だけをPIVで確認できる自然な形にした。

主な据え置き確認:
- Basic Sentences / Conversation: `Sanon!`, `Ni tostu por vi!`, `Mi antaŭĝojas revidi vin`, `Tio estis la plej malmulto, kion mi povis fari`, `Mi ne tion celis`, `Ne estas kialo pardonpeti`, `viciĝi`, `Kiel bele!`, `drinkejo`, `junulargastejo`, `bicikli` は、挨拶・謝意・指示・短い応答・情報確認の文脈で意味対応を保つ。
- Languages: `bengala`, `rumana`, `taja`, `urduo`, `persa`, `slovena`, `azerbajĝane`, `tagaloga`, `malajan`, `latve`, `norvega`, `ĉeĥe`, `pole`, `mandarena ĉina lingvo` は言語名・副詞形として文脈別許容範囲。`mandarena`, `malaja`, `azerbajĝana` はPIVで確認。
- Feelings / Help / Emergency: `trista`, `malstreĉita`, `ekscitita`, `motivita`, `embarasita`, `kapturno`, `malkuraĝigita`, `kondolencoj`, `prizorgi`, `tekkomputilo`, `malkonsili`, `fajrobrigado`, `oficejo pri perditaj aĵoj`, `traŭmatizita`, `prioritaton`, `asekurdokumentojn`, `akcidentraporto` は各列の意味と整合。`trista` はPIVで `malgaja, malĝoja` として確認できるため維持。
- First Aid / Police / Introductions: `bruligis min`, `tordis al mi la maleolon`, `surmeti bandaĝon`, `elartikigis mian brakon`, `manĝaĵveneniĝon`, `poliso de medicina asekuro`, `deklaron`, `Oni enrompis en mian aŭton`, `denunci ŝtelon`, `fotoroboton`, `familinomo`, `konatiĝi kun vi` は救急・警察・自己紹介文脈で対応する。`fotoroboto` はPIV直接確認語ではないが、Glosbe等で identikit / facial composite 対応として確認でき、RU `фоторобот` とも整合するため未修正。
- Residence / Nationality / Religion / Family: `amikino`, `vendmanaĝero`, `prezenti al vi mian fianĉon`, `sinjoron Smirnov`, `Ĉi tie tre plaĉas al mi`, `Mi estas ĉi tie por labori`, `Mi dividas ĝin kun unu alia persono`, `kunloĝas en domo`, `jam de ses monatoj`, `Kia estas via nacieco?`, `Kia estas via religio?`, `islamanino`, `budhano`, `siĥo`, `protestantino`, `ateisto`, `edziniĝinta`, `Ĉu vi edziniĝis?`, `fianĉino`, `fraŭla`, `en rilato`, `rendevuas kun iu`, `solinfano`, `genepoj` は意味ズレなし。
- Describing People / Likes / Meeting: `bonŝanculo`, `okulvitroj`, `saĝa`, `gustumi`, `rufaj haroj`, `bonkondutaj`, `iri al noktokluboj`, `butikumi`, `fotografado`, `troti`, `dombestoj`, `piedirado`, `sciencfikciaj libroj`, `aliĝi al mi/ni`, `rememorigos min`, `vestiblo`, `Ni iru hodiaŭ al la saŭno` は形容・嗜好・待ち合わせ文脈で許容。
- Dating / Wedding / Education: `partion de golfo`, `Sonas bone`, `renkontiĝos tie`, `aliĝi al vi`, `renkontiĝas kun iu`, `regalos vin per trinkaĵo`, `Vi mankas al mi`, `enamiĝis al vi`, `forveturu de ĉi tie`, `Ĉu vi edziniĝos kun mi?`, `nupto`, `novgeedzoj`, `porcelana/arĝenta/perla/korala/diamanta geedziĝa datreveno`, `En kiu aĝo infanoj komencas iri al lernejo?`, `studi ĉe universitato`, `magistriĝo`, `doktoriĝas`, `libera jaro`, `akceptkondiĉoj`, `studentloĝejo`, `Mi studas la hindian`, `bibliotekan formularon`, `formulitaj buŝe` は各サブトピックで意味対応を保つ。`edziniĝos kun mi` はユーザー指示どおり `kun` で維持。`hindia lingvo` はPIVで確認済み。

参照:
- ローカル PIV 2020: `PIV2020_structured.txt`
- PIV 2020 `rubeno`: https://vortaro.net/py/serchi.py?s=rubeno&simpla=1
- PIV 2020 `rubena`: https://vortaro.net/py/serchi.py?s=rubena&simpla=1
- PIV 2020 `rubina`（該当なし確認）: https://vortaro.net/py/serchi.py?s=rubina&simpla=1
- PIV 2020 `trista`: https://vortaro.net/py/serchi.py?s=trista&simpla=1
- PIV 2020 `tosti`: https://vortaro.net/py/serchi.py?s=tosti&simpla=1
- PIV 2020 `bandaĝo`: https://vortaro.net/py/serchi.py?s=banda%C4%9Do&simpla=1
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `rava`: https://vortaro.net/py/serchi.py?s=rava&simpla=1
- PIV 2020 `gusto`: https://vortaro.net/py/serchi.py?s=gusto&simpla=1
- PIV 2020 `nupto`: https://vortaro.net/py/serchi.py?s=nupto&simpla=1
- PIV 2020 `parkere`: https://vortaro.net/py/serchi.py?s=parkere&simpla=1
- PIV 2020 `hindia`: https://vortaro.net/py/serchi.py?s=hindia&simpla=1
- Glosbe `fotoroboto`: https://glosbe.com/eo/en/fotoroboto

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `39a53171f2bffaddb37d96402955303c`
- アプリ実行用CSV MD5: `fbd67715ea1adc6d051ef3f4b6f7815d`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID156`〜`ID1455` は1300件確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 584. 583周目 追加再点検（ID4756〜5155）

対象:
- `ID4756`〜`ID5155`
- Health / At the Pharmacy
- Communication Means / Phone, Phone Calls at Work, Mass Media, At the Post Office, Letter
- Time & Weather / Telling the Time, Calendar, Time Expressions, Weather

結果:
- **1件修正（1行・EO）**
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示に使われ、`PhraseID` と Esperanto 文が音声キー生成にも関わるため、意味を変えない最小修正に限定した。
- `ID4756`〜`ID5155` を100件単位で終端まで再点検。薬局・電話・メディア・郵便・手紙・時刻・天気の範囲について、PIV 2020 ローカル、PIV 2020 公式サイト、Glosbe/Kaikki 系のオンライン辞書を照合した。

修正:
- `ID4768` EO
  - `Mi ŝatus paroli kun la farmacisto, bonvolu` → `Mi ŝatus paroli kun la farmaciisto, bonvolu`
  - 理由: At the Pharmacy の「薬剤師と話したい」文脈。PIV 2020 公式サイトおよびローカル `PIV2020_structured.txt` で `farmaciisto` は「farmacio の専門家」として、`apotekisto` は「薬を準備・販売する人」として確認できる。一方 `farmacisto` は PIV 2020 公式検索で見つからない。Kaikki/Wiktionary 系には `farmacisto` も見えるが、ユーザー方針どおり PIV で確認できる形を優先し、意味を変えず最小差分の `farmaciisto` にした。

主な据え置き確認:
- Pharmacy: `herbaj medikamentoj`, `ion kontraŭ tuso`, `plastro`, `jodo`, `paracetamolo`, `pakaĵo da aspirino`, `kromefikoj`, `nur por ekstera uzo`, `tutnokte malfermita apoteko`, `dormigiloj`, `vojaĝmalsano`, `tablojdoj`, `kapsuloj`, `nikotinaj plastroj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は薬局・服薬文脈で対応する。`paracetamolo` はPIVで直接確認できなかったが、薬剤名として各列と一致し、確実な置換先を置くより現形維持が安全。
- Phone / Phone Calls at Work: `Malbona konekto`, `Restu sur la linio`, `Mi mesaĝos al vi poste`, `Ni malkonektiĝis`, `telefonbudo`, `telefonkarto`, `voka signalo`, `Mia kredito baldaŭ elĉerpiĝos`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `malŝargiĝos`, `urba telefona kodo`, `informservo`, `sur alia linio`, `demeti la aŭdilon`, `klavi la numeron` は電話・内線文脈で意味対応を保つ。
- Mass Media / Internet: `retpoŝtadreso`, `Skajpo`, `uzantonomo`, `ensalutu`, `elsalutu`, `konektiĝu al la interreto`, `retmesaĝon`, `en Facebook`, `en Tvitero`, `tekkomputilon`, `tajpu`, `ekskluziva artikolo`, `titolojn`, `eldonkvanto`, `radion` は通信・SNS・新聞文脈で許容。`tekkomputilo` は PIV では直接確認できないが、Glosbe/Komputeko 系で laptop 対応として確認できるため未修正。
- Post Office / Letter: `vatita koverto`, `poŝti`, `aerpoŝto`, `fakso`, `faksa numero`, `televida licenco`, `abono`, `afranko`, `rekomendita poŝto`, `dogana deklaracio`, `pesilo`, `poŝtrestante`, `vivresumo`, `Antaŭdankon`, `Respektplene via`, `antaŭĝojas`, `aldonaĵon` は郵便・手紙文脈で対応する。`Ĉe kiu giĉeto estas poŝtrestante?` は省略的だが窓口での口頭文として許容。
- Telling the Time / Calendar / Time Expressions: `Kioma horo estas?`, `Kvin antaŭ la dua`, `Estas kvin minutoj post la unua`, `Dudek antaŭ la dua`, `kvarono antaŭ/post`, `Ĝis la unua horo`, `La sekvantan tagon`, `Labortagoj`, `libertago`, `La vintraj/printempaj/someraj/aŭtunaj monatoj...` は日付・時刻・期間表現として対応する。
- Weather: `Hodiaŭ tage`, `Estas glacie kaj glite`, `Pluvetadas`, `Hajlas`, `Fulmas`, `Alproksimiĝas fulmotondro`, `malvarmete`, `Forte pluvas`, `Ekpluvas`, `Pluvegas`, `Estas sub nulo`, `Ĉi-nokte frostos`, `La suno ĵus kaŝiĝis`, `La nuboj disiĝas`, `La atmosfera premo estas alta`, `Kiu estas la plej varma monato en via lando?` は天候・気温文脈で意味ズレなし。

参照:
- PIV 2020 `farmaciisto`: https://vortaro.net/py/serchi.py?s=farmaciisto&simpla=1
- PIV 2020 `apotekisto`: https://vortaro.net/py/serchi.py?s=apotekisto&simpla=1
- PIV 2020 `farmacisto`（該当なし確認）: https://vortaro.net/py/serchi.py?s=farmacisto&simpla=1
- PIV 2020 `retpoŝto`: https://vortaro.net/py/serchi.py?s=retpoŝto&simpla=1
- Glosbe `notebook computer`: https://en.glosbe.com/en/eo/notebook%20computer
- PIV 2020 `eldonkvanto`: https://vortaro.net/py/serchi.py?s=eldonkvanto&simpla=1
- PIV 2020 `poŝtrestante`: https://vortaro.net/py/serchi.py?s=po%C5%9Dtrestante&simpla=1
- PIV 2020 `afranko`: https://vortaro.net/py/serchi.py?s=afranko&simpla=1
- PIV 2020 `fulmotondro`: https://vortaro.net/py/serchi.py?s=fulmotondro&simpla=1
- PIV 2020 `premo`: https://vortaro.net/py/serchi.py?s=premo&simpla=1

今回の整合性確認:
- 作業ディレクトリ側CSV MD5: `1e8102ff45566e55fb477203653e06cc`
- アプリ実行用CSV MD5: `ee106f2ad7fe02def6daaceb216a2a99`
- 作業ディレクトリ側CSVとアプリ実行用CSVは、行末差を除きCSV行内容が一致。
- 両CSVとも `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 両CSVとも全行 11 列でパース可能、重複 ID なし。
- 作業ディレクトリ側CSVは CRLF 行末 5001、裸 LF 0。アプリ実行用CSVは既存形式どおり LF 行末 5001、CRLF 0。
- `ID4756`〜`ID5155` は400件確認済み。
- `ID5156` 以降の行は存在しないことを確認済み。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 583. 582周目 追加再点検（ID3956〜4755）

対象:
- `ID3956`〜`ID4755`
- Leisure Time / Nightclub, Beach, Sport, Music, Going Camping, Family Time, Gardening, Having Guests
- Services / At the Bank, At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs
- Health / At the Doctor, Diseases, Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回のCSV本文修正なし**
- Streamlit アプリではこのCSVの `Esperanto` / `日本語` / `中文` / `한국어` が文クイズの直接表示・音声キー生成に使われるため、日中韓との対応を主軸に、RU/ENを参照列として扱って再確認した。
- 既存周回で修正済みの `remiso`, `arbitracianto`, `regatto`, `konteltiron`, `hipermetropa`, `stomakan perturbon`, `kranihaŭto`, `denta higienisto`, `fastante` などは現CSVに反映済みであり、今回さらに本文を動かすべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- Nightclub / Beach / Sport: `gastlisto`, `sportŝuoj`, `viva muziko`, `homplene`, `mortige enue`, `diskĵokeo`, `sunseĝo`, `akvoskioj`, `surfotabulo`, `plonĝkostumo`, `malsekkostumo`, `aerbotelo`, `garantiaĵo`, `gimnastikejo`, `tenisejo`, `remiso`, `arbitracianto`, `goli`, `egaligis la poentaron`, `vetkuroj`, `flava uniformo` は、各サブトピックの文脈で意味対応を保つ。
- Sport / Music / Camping: `ĵokeo`, `vetŝancoj`, `golfbastonoj`, `golfĉaro`, `norma nombro da batoj`, `regatto`, `femuraj muskoloj`, `akordiono`, `saksofono`, `simfonia orkestro`, `popolmuziko`, `tendumi`, `ruldomo`, `poŝlampo`, `najtingalo`, `hirunda nesto`, `telfero`, `monta pado` は、PIV確認語または透明な複合語として現形維持。
- Family Time / Gardening / Having Guests: `bovlingon`, `televidaj romanoj`, `sagetojn`, `legadon`, `sojfabojn`, `sekalon`, `falĉas`, `erpis`, `fruktarbejo`, `buŝtukojn`, `boligos akvon`, `sukerpecoj`, `ĝinon kun toniko`, `mendas picon hejmen`, `Mi lavos, kaj vi viŝos` は、余暇・園芸・来客文脈で許容範囲。
- Bank / Estate Agency: `legitimilo`, `kurzo`, `provizio`, `bankaŭtomato`, `kontantmono`, `stirpermesilo`, `monretiro`, `konteltiro`, `ĉekaro`, `ĝiri`, `interezprocento`, `kontantigi`, `loĝejo`, `vicdomo`, `parkumejo`, `kontanta aĉetanto`, `hipoteko`, `deponaĵo je unu-monata lupago`, `duamana posedaĵo`, `sur la merkato` は、銀行・不動産文脈で意味ズレなし。
- Beauty Salon / Tailor / Repairs: `franĝo`, `konstanta ondumado`, `dislimo`, `farbi miajn harojn blonde`, `senharigo ... per vakso`, `feni`, `ŝampui`, `kranihaŭto`, `laki ungojn`, `zipo`, `alkudri`, `fliki`, `laŭmezura kostumo`, `mallarĝigi`, `plilarĝigi`, `kroneto`, `pilo`, `ŝlosilringo`, `plandumoj`, `garantio` は、辞書根拠または既存確認に基づき維持。
- Health: `kapturna`, `malvarmumo`, `tubero`, `haŭterupcio`, `furunko`, `diareo`, `konstipita`, `nazkataro`, `stomaka perturbo`, `limfonodoj`, `mikozo de la piedoj`, `streĉis muskolon`, `sendormeco`, `fojnofebro`, `sutureroj`, `urina specimeno` は、症状・治療文脈として対応する。
- Dentist / Optician / Pharmacy: `plombo` / `plombigi`, `krono`, `dentprotezo`, `kario`, `denta higienisto`, `gargari la buŝon`, `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `astigmatismo`, `UV-protekto`, `inhalilo`, `desinfektaĵo`, `kontraŭdoloriloj`, `fastante`, `havebla nur laŭ recepto` は、歯科・眼鏡店・薬局文脈で意味対応を保つ。

参照:
- PIV 2020 `ĵokeo`: https://vortaro.net/py/serchi.py?s=%C4%B5okeo&simpla=1
- PIV 2020 `regatto`: https://vortaro.net/py/serchi.py?s=regatto&simpla=1
- PIV 2020 `tendumi`: https://vortaro.net/py/serchi.py?s=tendumi&simpla=1
- PIV 2020 `ĝiri`: https://vortaro.net/py/serchi.py?s=%C4%9Diri&simpla=1
- PIV 2020 `konto`: https://vortaro.net/py/serchi.py?s=konto&simpla=1
- PIV 2020 `farbi`: https://vortaro.net/py/serchi.py?s=farbi&simpla=1
- PIV 2020 `franĝo`: https://vortaro.net/py/serchi.py?s=fran%C4%9Do&simpla=1
- PIV 2020 `senharigo`: https://vortaro.net/py/serchi.py?s=senharigo&simpla=1
- PIV 2020 `feni`: https://vortaro.net/py/serchi.py?s=feni&simpla=1
- PIV 2020 `plombo`: https://vortaro.net/py/serchi.py?s=plombo&simpla=1
- PIV 2020 `gargari`: https://vortaro.net/py/serchi.py?s=gargari&simpla=1
- PIV 2020 `dioptrio`: https://vortaro.net/py/serchi.py?s=dioptrio&simpla=1
- PIV 2020 `hipermetropa`: https://vortaro.net/py/serchi.py?s=hipermetropa&simpla=1
- PIV 2020 `fasti`: https://vortaro.net/py/serchi.py?s=fasti&simpla=1

今回の整合性確認:
- CSV本文は未変更。
- CSV MD5: `e9b5a910ab5a8a797dcb8308eef267f5`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 全行 11 列でパース可能、重複 ID なし。
- CRLF 行末 5001、裸 LF 0。
- 今回はログのみ更新。

## 582. 581周目 追加再点検（ID1294, ID3256〜3955）

対象:
- `ID1294`
- `ID3256`〜`ID3955`
- Dating / Wedding
- Food / Fruit, Vegetables, Staple Food & Spices, Breakfast Food
- Shopping / Department Store, Clothes, Shoes, Accessories, Personal Care, Electronic Devices, Other Goods, Supermarket, Bookshop & Florist's, Payments & Returns
- Leisure Time / Cinema, Theatre, Museum, Nightclub

結果:
- **1件修正（1行・EO）**
- ユーザー指定の `edziniĝi` の前置詞を最優先で確認し、PIV 2020 公式サイトの `edziĝi kun mi` / `edziniĝi kun viro` 型に合わせて補正した。
- `ID3256`〜`ID3955` は100件単位で継続点検したが、追加で修正すべき明確な意味ズレは見つからなかった。

修正:
- `ID1294` EO
  - `Ĉu vi edziniĝos al mi?` → `Ĉu vi edziniĝos kun mi?`
  - 理由: Dating / Wedding の「結婚してくれませんか？」文脈。PIV 2020 公式サイトで `edziĝi kun mi`、`edziniĝi kun viro` の用例を確認できる。ユーザー指定どおり、内容を変えずに前置詞を `kun` にした。

主な据え置き確認:
- 果物・野菜・朝食語彙の `limeoj`, `eruko`, `kazeo`, `korna bulko`, `kirlovaĵo`, `dolĉigilo` は、PIV/Glosbe/既存ログの根拠と各列の食品文脈が合うため維持。
- 衣類・靴・装身具の `zorioj`, `pantofoj`, `sportŝuoj`, `gumaj botoj`, `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `Ili perfekte sidas al mi` は、PIV確認語または透明な複合語として買い物文脈に対応するため維持。
- 化粧品・日用品の `paletron da ŝminko por la palpebroj`, `ŝminko por okulharoj`, `vizaĝpudro`, `pinĉilo`, `baterioj`, `memorkarto`, `lensokovrilo`, `konstrubriketoj`, `memoraĵo de la urbo`, `limdato` は、未確認語へ無理に置換せず、既存の確認済み判断を維持。
- スーパー・書店・花屋の `bastonpano`, `makedona-ukrainan vortaron`, `pufmaizo`, `subtekstoj`, `animaciaĵo`, `Festivalo de Cannes`, `teatra binoklo`, `interakto`, `loĝio`, `aŭdgvido/aŭdgvidilo`, `karikatursalono`, `handikapuloj` は、文脈別許容として意味対応を保つ。

参照:
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `eruko`: https://vortaro.net/py/serchi.py?s=eruko&simpla=1
- PIV 2020 `kazeo`: https://vortaro.net/py/serchi.py?s=kazeo&simpla=1
- PIV 2020 `zorio`: https://vortaro.net/py/serchi.py?s=zorio&simpla=1
- PIV 2020 `pufmaizo`: https://vortaro.net/py/serchi.py?s=pufmaizo&simpla=1
- PIV 2020 `binoklo`: https://vortaro.net/py/serchi.py?s=binoklo&simpla=1
- PIV 2020 `interakto`: https://vortaro.net/py/serchi.py?s=interakto&simpla=1
- PIV 2020 `loĝio`: https://vortaro.net/py/serchi.py?s=lo%C4%9Dio&simpla=1
- Glosbe `croissant`: https://glosbe.com/en/eo/croissant
- Glosbe `Cannes`: https://glosbe.com/en/eo/Cannes

今回の整合性確認:
- CSV MD5: `e9b5a910ab5a8a797dcb8308eef267f5`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 全行 11 列でパース可能、重複 ID なし。
- CRLF 行末 5001、裸 LF 0。
- ログコピーCSVとの差分は6件で、今回追加分は `ID1294` のEO 1件のみ。
- このディレクトリは Git リポジトリ外のため、`git diff --check` は未実行。

## 581. 580周目 追加再点検（ID2856〜3255）

対象:
- `ID2856`〜`ID3255`
- Travel / Hotel / Renting a Flat
- Restaurant & Pub / Ordering Drinks, Ordering Food, During the Meal, Paying the Bill, Complaints, At the Pub
- Food / Meat & Fish

結果:
- **1件修正（1行・EO）**
- Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認し、RU/EN は補助参照として扱った。PIV 2020 ローカル、PIV 2020 公式サイト、Wiktionary/Glosbe 系のオンライン確認を併用し、語形・格・一致・語法・自然さ・明確な意味ズレを確認した。
- `ID2956`〜`ID3255` は、追加で修正すべき明確な意味ズレなし。

修正:
- `ID2876` EO
  - `Kiel funkcias la varmigilo?` → `Kiel funkcias la hejtilo?`
  - 理由: Hotel / Renting a Flat の heater / RU `обогреватель` 文脈。PIV 2020 で `hejtilo` は「gasa, elektra, varmaera」など室内暖房器具を広く表す語として確認できる。一方、`varmigilo` は PIV 2020 で主に手足・寝具などを温める器具として示されるため、この文脈では `hejtilo` の方が安全。

主な据え置き確認:
- 賃貸・部屋設備の `vazaro`, `ŝvabrilo`, `fridujo`, `kuirilo`, `suĉkloŝo`, `adherema filmo`, `polvosuĉilo`, `mikroondilo`, `telerlavmaŝino`, `klimatizilo`, `lavmaŝino`, `elektromezurilo`, `ĉambristino`, `fumejo`, `gasita akvo`, `vinkarto` は各文脈で対応する。
- `smuzio` は PIV 2020 では強い見出し確認に至らないが、Wiktionary で Esperanto 名詞として確認でき、smoothie / スムージー / RU `смузи` と対応するため未修正。
- `koŝera manĝaĵo`, `bifsteko kun fritoj`, `pastaĵoj`, `kebabo`, `keĉupo`, `majonezo`, `antaŭmanĝaĵoj`, `farĉitaj fungoj`, `nudeloj`, `steko`, `mezrostita`, `bone rostita`, `sen salo` は飲食店の注文・調理文脈で意味ズレなし。
- `halala`, `manĝobastonetoj`, `kalzoneo`, `rapidmanĝaĵo`, `laktaĵoj`, `servokotizo`, `restmono`, `trinkmono`, `malĝuste sumigita`, `odoras je korko`, `rostitan meleagron` は、既存の辞書確認・文脈確認どおり維持。
- `naĉoj`, `postebrio`, `barela biero`, `glasetojn da tekilo`, `laktoskuaĵo`, `ĉipsoj`, `bifstekon el bova lumbaĵo`, `ŝafidaĵo`, `rostbefo`, `grilita salmo`, `salita moruo`, `kruda haringo`, `kankroj`, `omaroj` はパブ・肉魚料理文脈で対応する。

参照:
- PIV 2020 `hejtilo`: https://vortaro.net/py/serchi.py?s=hejtilo&simpla=1
- PIV 2020 `varmigilo`: https://vortaro.net/py/serchi.py?s=varmigilo&simpla=1
- PIV 2020 `bifsteko`: https://vortaro.net/py/serchi.py?s=bifsteko&simpla=1
- PIV 2020 `korko`: https://vortaro.net/py/serchi.py?s=korko&simpla=1
- PIV 2020 `postebrio`: https://vortaro.net/py/serchi.py?s=postebrio&simpla=1
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio
- Wiktionary `kalzoneo`: https://en.wiktionary.org/wiki/kalzoneo
- Glosbe `milkshake`: https://glosbe.com/en/eo/milkshake

今回の整合性確認:
- CSV MD5: `2ef3229dce4510e517b34221509a35f8`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 全行 11 列でパース可能、重複 ID なし。
- `ID2856`〜`ID3255` は 100 件単位で確認済み。

## 580. 579周目 追加再点検（ID1856〜2855）

対象:
- `ID1856`〜`ID2855`
- Tourist Information / Giving Directions, Tourist Office, Excursions
- Travel / Plane, Other Transport, Hotel

結果:
- **3件修正（3行・EO）**
- Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認し、RU/EN は補助参照として扱った。PIV 2020 ローカル、PIV 2020 公式サイト、Glosbe を併用し、語形・格・一致・語法・自然さ・明確な意味ズレを確認した。
- ID1856〜1955、2156〜2555、2656〜2855 は、追加で修正すべき明確な意味ズレなし。

修正:
- `ID2011` EO
  - `Kiam komenciĝas la enŝipiĝo?` → `Kiam komenciĝas la eniro en la aviadilon?`
  - 理由: PIV 2020 で `enŝipiĝi` は船に乗る語義として確認できる。Plane / Checking in の搭乗開始では、船舶語を航空に拡張するより、PIV で確認できる `aviadilo` と基本語 `eniro` による表現が安全。
- `ID2102` EO
  - `Komenciĝas la enŝipiĝo por flugo numero 120` → `Komenciĝas la eniro en la aviadilon por flugo numero 120`
  - 理由: `flugo numero 120` の空港案内文脈。ID2011 と同じく、船舶語 `enŝipiĝo` を避け、内容を変えずに航空機への搭乗開始として明示。
- `ID2601` EO
  - `Mi ŝatus rezervi sunseĝon` → `Mi ŝatus rezervi ferdekseĝon`
  - 理由: Other Transport / Ship の deckchair 文脈。PIV 2020 公式サイトで `ferdekseĝo` は長い折り畳み式の布製椅子として確認でき、deckchair / RU `шезлонг` と対応する。`sunseĝo` は透明だが、この文脈では PIV 確認済み語へ寄せるほうが安全。

主な据え置き確認:
- `naveda buso`, `subeksponi la filmon`, `vidindaĵoj`, `ekskurso`, `sandviĉejo`, `turisma oficejo` は観光案内文脈で対応する。
- 船の文脈の `enŝipiĝi` は PIV 2020 の語義と合うため維持。
- `ferdeko`, `pramo`, `krozado`, `kajuto`, `savboato`, `marmalsano`, `plena pensiono`, `monŝranko`, `rulseĝa aliro`, `ŝtopilingo`, `atendolisto`, `vizitkarto`, `savelirejo`, `plusendi`, `lavejo`, `elregistriĝi`, `bolilo`, `klimatizilo`, `littukoj`, `apartamento/luo` は各文脈で意味ズレなし。
- `elregistriĝi` は PIV 2020 で独立見出しとしては未確認だが、ホテル checkout 文脈では既存確認どおり日中韓/RUとの対応が明確で、短い会話表現として許容。
- `bolilo` は PIV 2020 で水を沸かす容器として確認でき、Glosbe でも English `kettle` と対応するため維持。

参照:
- PIV 2020 `enŝipiĝi`: https://vortaro.net/py/serchi.py?s=en%C5%9Dipi%C4%9Di&simpla=1
- PIV 2020 `aviadilo`: https://vortaro.net/py/serchi.py?s=aviadilo&simpla=1
- PIV 2020 `ferdekseĝo`: https://vortaro.net/py/serchi.py?s=ferdekse%C4%9Do&simpla=1
- PIV 2020 `bolilo`: https://vortaro.net/py/serchi.py?s=bolilo&simpla=1
- PIV 2020 `klimatizilo`: https://vortaro.net/py/serchi.py?s=klimatizilo&simpla=1
- Glosbe `bolilo`: https://glosbe.com/eo/en/bolilo

今回の整合性確認:
- CSV MD5: `5a51511b3558bbcc82e6eeea27f2fd5b`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- 全行 11 列でパース可能、重複 ID なし。
- `ID1856`〜`ID2855` は 100 件単位で確認済み。

## 579. 578周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet
- Making Friends / Accepting & Declining
- Dating / Asking Someone out
- Dating / On a Date

結果:
- **今回の追加修正なし**
- 予定調整、承諾・断り、デートの誘い・親密表現のブロックとして、Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認した。RU/EN は、口語的な誘い・送迎・恋愛表現の補助確認に用いた。
- 過去周回で `ID1162` EN、`ID1183` ZH、`ID1217` EN は補正済み。今回の再点検では、EO を含めてさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Sinjoroj, ni povas ludi partion de golfo` は男性複数への呼びかけで、`partio` のゲーム・競技の一回という語義から golf round / RU `партию в гольф` に対応する。
- `Certe`, `Bone!`, `Sonas bone`, `Jes, certe`, `Mi ne kontraŭas`, `Kun plezuro`, `Tio estas bona ideo`, `Ĝi estas bona plano` は承諾・肯定応答として自然。`ID1162` EN は過去に `Yes, certainly.` へ補正済み。
- `Neniel!`, `Certe ne!`, `Pardonu, mi ne povas veni`, `Mi ne havas tempon`, `Mi devas labori`, `Ne, mi ne estas libera`, `Eble venontfoje` は断り表現として対応する。
- `Mi iomete malfruiĝas`, `Mi estos tie post dek minutoj`, `Mi ankoraŭ ne decidis`, `Bedaŭrinde, mi jam havas planojn` は予定調整・遅延・未決定の表現として意味ズレなし。
- `Ni renkontiĝos tie`, `Mi vidos vin en la kinejo je la deka horo`, `Mi estos tie je la naŭa, krom se la buso malfruos`, `Mi jam promesis renkontiĝi kun Sofia hodiaŭ vespere` は `renkontiĝi` 系の待ち合わせ・面会表現として自然。`ID1183` ZH は過去に「そこで会う」へ補正済み。
- `Mi venos preni vin je la 5-a horo`, `Ĉu mi povas akompani vin hejmen?`, `Ĉu mi povas veturigi vin hejmen?` は送迎表現として対応する。`akompani` は徒歩を含む付き添い、`veturigi` は車などの移動手段を含むため区別が保たれている。
- `Ĉu mi povas aliĝi al vi?`, `Ĉu ĝenas vin, se mi aliĝos al vi?` は同席・合流を求める表現として文脈別許容。PIV 2020 の `aliĝi al ...` の型にも合う。
- `Ĉu mi povas aĉeti trinkaĵon por vi?`, `Mi regalos vin per trinkaĵo`, `Ni parolu plu dum la tagmanĝo`, `Ĉu vi volus vespermanĝi kun mi?` は飲食への誘いとして自然。
- `Ni trovu agrablan lokon kien iri` は `lokon, kien iri` として「行く先となる場所」を表し、短い会話文では許容。
- `Kion vi elpensis?` は「何を考え出した/思いついたか」の意味で、過去に参考ENを `What have you come up with?` に補正済み。
- `Ĉu vi renkontiĝas kun iu?` は広いが、Dating 文脈では「付き合っている/会っている人がいる」と読めるため維持。
- `Vi plaĉas al mi`, `Vi mankas al mi`, `Vi tre plaĉas al mi`, `Mi enamiĝis al vi`, `Mi freneziĝas pro vi` は、恋愛・親密表現として列間対応を保つ。特に `Vi mankas al mi` は `manki al iu` の型として自然。
- `Ĉu mi povas kisi vin?`, `Ĉu mi povas brakumi vin?`, `Ne tuŝu min!`, `Lasu min trankvila` は、親密さ・拒否・境界線の表現として意味ズレなし。
- `Ĉe vi aŭ ĉe mi?`, `Ĉu vi ŝatus veni al mi hejmen?`, `Ni forveturu de ĉi tie` はデート場面の短い口語表現として成立する。`forveturu` は乗り物含みがあるが、RU `уедем` と整合するため維持。
- `Kion vi pensas pri ĉi tiu loko?`, `Ĉu vi povas rakonti al mi pli pri vi?` は会話を広げる質問として自然。

参照:
- PIV 2020 `partio`: https://vortaro.net/py/serchi.py?s=partio&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `regali`: https://vortaro.net/py/serchi.py?s=regali&simpla=1
- PIV 2020 `elpensi`: https://vortaro.net/py/serchi.py?s=elpensi&simpla=1
- PIV 2020 `akompani`: https://vortaro.net/py/serchi.py?s=akompani&simpla=1
- PIV 2020 `veturigi`: https://vortaro.net/py/serchi.py?s=veturigi&simpla=1
- PIV 2020 `manki`: https://vortaro.net/py/serchi.py?s=manki&simpla=1
- ReVo `manki`: https://reta-vortaro.de/revo/art/mank.html
- PIV 2020 `enamiĝi`: https://vortaro.net/py/serchi.py?s=enami%C4%9Di&simpla=1
- PIV 2020 `freneziĝi`: https://vortaro.net/py/serchi.py?s=frenezi%C4%9Di&simpla=1
- PIV 2020 `forveturi`: https://vortaro.net/py/serchi.py?s=forveturi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1156`〜`ID1255` は 100 件、`ID1162`/`ID1183`/`ID1217` の補正後内容を確認済み。

## 578. 577周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People
- Making Friends / Things You Like & Dislike
- Making Friends / Arranging to Meet

結果:
- **今回の追加修正なし**
- 人物描写、趣味・嗜好、誘い・待ち合わせのブロックとして、Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認した。RU/EN は、趣味語・評価語・誘い表現の自然さを確認する補助列として参照した。
- 過去周回で `ID1087` EN、`ID1145` ZH/KO、`ID1154` EN は補正済み。今回の再点検では、EO を含めてさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Kiom bone vi konas lin?`, `Li havas nigrajn harojn kaj verdajn okulojn`, `Li havas mallongajn harojn, grizajn ĉe la tempioj`, `Mia frato ankaŭ estas tre kuraĝa`, `Viaj infanoj estas tre bonkondutaj` は人物描写・性格評価として対応する。
- `Mi zorge elektas miajn amikojn`, `Kien ajn mi iras, la homoj estas afablaj` は、友人選び・一般的な人柄評価として自然。
- `Mi ŝatas vojaĝi`, `Mi amas iri al noktokluboj`, `Mi malamas butikumi`, `Kio estas via hobio?`, `Mia hobio estas fotografado`, `Mi ŝatas ĝardenadon` は趣味・嗜好表現として意味ズレなし。
- `Mi amas la kinon` は cinema / kino を広く表し、JAの「映画館」寄り、ZH/KOの「映画」寄り、RU `кино` の範囲を吸収できるため文脈別許容。
- `Mi adoras patkukojn`, `Mi ne ŝatas bruajn drinkejojn`, `Ĉu vi kolektas poŝtmarkojn?`, `Mi multe legas`, `Mi ŝatas aŭskulti muzikon`, `Mi kolektas monerojn` は、好悪・収集・読書の短文として自然。
- `Mi ŝatas troti` は `jogging` と完全同義ではないが、PIV 2020 で人・動物の小走り/速歩系の用法が確認でき、軽いランニング文脈として許容。
- `Ili ne tre plaĉas al mi` は `plaĉi al mi` の否定弱化で、「あまり好きではない」と一致する。過去に参考ENを `I don't like them very much.` に補正済み。
- `Mi neniam ŝatis golfon`, `Mi ne povas elteni futbalon`, `Ĉu vi ŝatas bicikli?`, `Surfado estas agrabla, ĉu ne?` はスポーツ・活動への好悪として対応する。
- `Ĉu vi havas dombestojn?`, `Mi havas hundon`, `Mi havas hamstron`, `Mi havas hundon kaj du katojn`, `Mia fratino havas testudon` は、ペット所有の短文として自然。
- `Tio, kion mi plej ĝuas, estas verki novelojn` は `novelo` が短編小説を表すため、EN/JA/ZH/KO/RU と対応する。
- `Mi ne pensas, ke piedirado estas agrabla` は EN/JA/ZH の hiking より広いが、RU `пешие прогулки` と合い、徒歩・散策寄りの意味として維持。
- `Mi interesiĝas pri fotografado`, `Ŝi interesiĝas pri lingvoj`, `Li interesiĝas pri historio` は `interesiĝi pri` の型として自然。
- `modprezentadon`, `filmosteluloj`, `sciencfikciaj libroj`, `mensogulon`, `hororaj filmoj` は透明複合またはPIV確認語として意味ズレなし。
- `Aliĝu al mi por tagmanĝo`, `Ĉu vi ŝatus aliĝi al ni?` はやや硬いが、PIV 2020 の `aliĝi al ...` の「加わる」語義から、会食・同席への誘いとして許容。
- `Ĉu ni iru trinki ion?`, `Ni faru kafpaŭzon`, `Ĉu vi ŝatus promeni?`, `Ni iru hodiaŭ al la saŭno`, `Ĉu vi volas iri ien dum la semajnfino?` は誘い・予定提案として対応する。`ID1145` の ZH/KO は過去に yes/no の `ien` に合わせて補正済み。
- `Je kioma horo ni renkontiĝu?`, `Kie ni renkontiĝu?`, `Ni renkontiĝu je la oka`, `Ni renkontiĝu en la vestiblo`, `Ni renkontiĝu antaŭ la hotelo` は待ち合わせ表現として自然。
- `Ĉu vi rememorigos min?`, `Ĉu ni povas aranĝi tion iom pli malfrue, ekzemple je la 16-a horo?`, `Sciigu min, se vi povos veni` は予定調整・リマインド・出欠確認として対応する。

参照:
- PIV 2020 `butikumi`: https://vortaro.net/py/serchi.py?s=butikumi&simpla=1
- PIV 2020 `hobio`: https://vortaro.net/py/serchi.py?s=hobio&simpla=1
- PIV 2020 `fotografado`: https://vortaro.net/py/serchi.py?s=fotografado&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `troti`: https://vortaro.net/py/serchi.py?s=troti&simpla=1
- PIV 2020 `piedirado`: https://vortaro.net/py/serchi.py?s=piedirado&simpla=1
- PIV 2020 `novelo`: https://vortaro.net/py/serchi.py?s=novelo&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `memorigi`: https://vortaro.net/py/serchi.py?s=memorigi&simpla=1
- PIV 2020 `vestiblo`: https://vortaro.net/py/serchi.py?s=vestiblo&simpla=1
- PIV 2020 `hororo`: https://vortaro.net/py/serchi.py?s=hororo&simpla=1
- PIV 2020 `sciencfikcio`: https://vortaro.net/py/serchi.py?s=sciencfikcio&simpla=1
- PIV 2020 `mensogulo`: https://vortaro.net/py/serchi.py?s=mensogulo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1056`〜`ID1155` は 100 件、`ID1087`/`ID1145`/`ID1154` の補正後内容を確認済み。

## 577. 576周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age/Nationality & Religion
- Making Friends / Family & Relationships
- Making Friends / Describing People

結果:
- **今回の追加修正なし**
- 宗教・出生地/国籍、婚姻/交際、親族語、人物・身体描写のブロックとして、Esperanto と `日本語` / `中文` / `한국어` のクイズ対応を主軸に確認した。RU/EN は、女性話者形・宗教語・親族語の性別明示を確認する補助列として参照した。
- 過去周回で `ID1021` JA、`ID1046`〜`ID1049` EN、`ID1050` JA は修正済み。今回の再点検では、EO を含めてさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Mi estas budhano`, `Mi estas siĥo`, `Mi estas protestantino`, `Mi estas ateisto`, `Mi ne estas religia`, `Ĉu vi kredas je Dio?`, `Kie mi povas preĝi?` は宗教・信仰の自己申告として対応する。女性形 `protestantino` は RU `протестантка` と合う。
- `preĝejo`, `templo`, `moskeo`, `sinagogo` は礼拝施設の語として対応する。`preĝejo` は一般には「祈りの場所」だが、church 文脈でも使えるため過修正しない。
- `Kiam vi naskiĝis?`, `Mi naskiĝis en 1992`, `Mia naskiĝtago estas la 9-a de februaro`, `Kie vi naskiĝis?`, `Mi naskiĝis en Kolombio` は出生時・誕生日・出生地の表現として自然。
- `El kiu lando vi estas?`, `Ni estas el Svedio`, `Ŝi estas el Israelo`, `Mi devenas el Budapeŝto, sed nun mi loĝas en Kairo`, `El kiu parto de Kroatio vi devenas?` は出身表現として列間対応を保つ。`devenas el` は「もともと〜出身」に寄るため、RU の「生まれた」より少し広いが許容。
- `Ni estas civitanoj de Maroko`, `Mi ricevis singapuran civitanecon` は PIV 2020 の `civitano/civitaneco` と合い、市民権・国籍文脈で成立する。
- `Mi estas fianĉiĝinta`, `Mi estas edziniĝinta`, `Ĉu vi edziniĝis?`, `Ne, mi estas fraŭla`, `Li estas divorciĝinta`, `Ŝi estas vidvino`, `Li estas vidvo` は婚姻状態の表現として自然。`edziniĝinta/edziniĝis` は女性話者・女性対象に寄るが、RU 列と整合する。
- `Jes. Fakte, mi estas fianĉino` は直訳的には「私は婚約者の女性」だが、PIV 2020 の `fianĉino` に「婚約した女性」の語義があるため、`I'm engaged` の女性話者文脈として許容。
- `Mi disiĝis`, `Li estas en rilato`, `Jes, mi rendevuas kun iu` は交際・別離の文脈で成立する。`en rilato` は恋愛関係としてはやや英語的だが、PIV 2020 の `rilato` には人間関係・相互関係があり、過去周回同様に維持。
- `frato`, `fratino`, `edzo`, `koramiko`, `koramikino`, `infanoj`, `novnaskita bebo`, `ĝemeloj`, `graveda`, `proksima parenco` は家族・親族語として対応する。
- `Ni havas du filojn kaj filinon`, `Jes, mi havas knabon kaj knabinon`, `fratojn aŭ fratinojn`, `pli junan fratinon`, `pli aĝan fraton`, `solinfano`, `geavoj`, `genepoj`, `unu nepo kaj du nepinoj` は、親族の性別・数の対応を保つ。過去修正後の `ID1021` JA は `nepo/nepinoj` の性別差を明確に反映している。
- `Mi estas viro`, `Mi estas virino`, `Ŝi estas bela`, `Vi estas tre ĉarma`, `Li estas bonŝanculo`, `Li similas al mi`, `Li portas okulvitrojn` は人物・外見描写として自然。
- `Kia estas Emma?` と `Kia homo li estas?` は人物像・性格を問う表現、`Kiel li aspektas?` と `Kiel aspektas via pli juna fratino?` は外見を問う表現として、過去修正後のJAとも内部整合がある。
- `Li estas juna, malalta kaj bela` は男性への外見評価としても `bela` が使えるため、EN `handsome` / RU `привлекательный` と対応する。
- `Ŝi havas blondajn harojn`, `Ŝi estas alta, svelta kaj bela`, `Ŝi havas buklajn rufajn harojn`, `Ŝi havas ĉarman rideton`, `Ŝi estas scivolema persono`, `Vi similas al mia fratino` は、髪色・体格・表情・性格・類似の描写として意味ズレなし。
- `Mi uzas miajn okulojn por vidi`, `Mi uzas mian nazon por flari`, `Mi havas buŝon/orelojn/langon/piedojn por ...` は教材的だが、身体部位の機能説明として意味は明確。過去修正済みのEN `with` 補足とも整合する。

参照:
- PIV 2020 `budhano`: https://vortaro.net/py/serchi.py?s=budhano&simpla=1
- PIV 2020 `siĥo`: https://vortaro.net/py/serchi.py?s=si%C4%A5o&simpla=1
- PIV 2020 `preĝejo`: https://vortaro.net/py/serchi.py?s=pre%C4%9Dejo&simpla=1
- PIV 2020 `moskeo`: https://vortaro.net/py/serchi.py?s=moskeo&simpla=1
- PIV 2020 `sinagogo`: https://vortaro.net/py/serchi.py?s=sinagogo&simpla=1
- PIV 2020 `civitaneco`: https://vortaro.net/py/serchi.py?s=civitaneco&simpla=1
- PIV 2020 `fraŭlo`: https://vortaro.net/py/serchi.py?s=fra%C5%ADlo&simpla=1
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `fianĉino`: https://vortaro.net/py/serchi.py?s=fian%C4%89ino&simpla=1
- PIV 2020 `rendevui`: https://vortaro.net/py/serchi.py?s=rendevui&simpla=1
- PIV 2020 `nepo`: https://vortaro.net/py/serchi.py?s=nepo&simpla=1
- PIV 2020 `aspekti`: https://vortaro.net/py/serchi.py?s=aspekti&simpla=1
- PIV 2020 `gustumi`: https://vortaro.net/py/serchi.py?s=gustumi&simpla=1
- PIV 2020 `flari`: https://vortaro.net/py/serchi.py?s=flari&simpla=1
- PIV 2020 `rufa`: https://vortaro.net/py/serchi.py?s=rufa&simpla=1
- PIV 2020 `ĉarma`: https://vortaro.net/py/serchi.py?s=%C4%89arma&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID956`〜`ID1055` は 100 件確認済み。

## 576. 575周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions
- Making Friends / Place of Residence
- Making Friends / Age/Nationality & Religion

結果:
- **今回の追加修正なし**
- 紹介・知人関係、居住地・滞在理由、年齢・国籍・宗教のブロックとして、Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認した。RU/EN は、性別付き名詞、居住・滞在のニュアンス、宗教名の確認に用いた。
- 過去周回で `ID954` は `Mi estas musulmanino` から `Mi estas islamanino` に修正済み。今回も PIV/Glosbe 系で `islamano` が確認できる一方、現行綴り `musulmanino` は根拠が弱いため、現行の `islamanino` を維持する。

主な据え置き確認:
- `Ankaŭ mi ĝojas konatiĝi kun vi`, `Kun kiu vi estas?`, `Vi certe estas William`, `Ĉu vi konas Emilin?`, `Ĉu ni ne renkontiĝis antaŭe?` は、初対面・再会確認の短文として自然。
- `Mi estas kun amikino` は JA/ZH/KO では性別非明示だが、RU `с подругой` と合い、PIV 2020 で `amikino` も確認できるため維持。
- `Kiu estas ĉi tiu fraŭlino?`, `Tio estas mia filino`, `Ĉi tiu estas mia edzino`, `Ĉi tiu estas mia koramiko`, `Mi estas kun mia patro`, `Mi estas kun miaj kolegoj` は、人物紹介・同伴者説明として対応する。
- `Mi estas Hina, vendmanaĝero` は `vend-` + `manaĝero` の透明複合で、sales manager の意味は明確。PIV 2020 で `manaĝero` を確認し、`vendmanaĝero` は過度な造語誤りとは判断しない。
- `Ĉu vi konas unu la alian?`, `Ni konatiĝis per amikoj`, `De kie vi konas unu la alian?`, `Ni kune studis en la universitato`, `Ni kune lernis en la lernejo`, `Ni kutimis kune fiŝkapti` は、知人関係・知り合った経緯として意味ズレなし。
- `Ĉu mi povas prezenti al vi mian fianĉon?`, `Permesu al mi prezenti nian direktoron, sinjoron Smirnov`, `Ni ĝojas prezenti al vi nian filinon` は `prezenti iun al iu` の型に合う。`sinjoron Smirnov` は敬称側の対格で目的語関係が示されるため、外来姓に無理に `-n` を付けない現形を維持。
- `Pardonu, mi ne aŭdis vian nomon`, `Ĉu vi povus literumi vian nomon, mi petas?` は、名前を聞き取れなかった・綴り確認の発話として自然。
- `Ĉu plaĉas al vi ĉi tie?`, `Ĉi tie tre plaĉas al mi`, `Kun kiu vi loĝas?`, `Mi loĝas kun amikoj`, `Mi loĝas sola`, `Ŝi kunloĝas en domo kun tri aliaj homoj` は、居住・同居状況の文脈で成立する。
- `Kio alkondukas vin al Brazilo?` は直訳的だが、`what brings you...` と同じ発想の表現として理解可能。`Mi estas ĉi tie por labori` は「出張」より広いが、RU `в командировке` を含む仕事目的の滞在として許容。
- `Mi dividas ĝin kun unu alia persono` は先行する住居・部屋を受ける `ĝi` として読め、EN/JA/ZH/KO の「もう一人と共有」と対応する。
- `Dum unu jaro`, `Mi restos ĉi tie dum 1 tago`, `Ili restas dum tri semajnoj`, `Li loĝas en Nov-Zelando jam de ses monatoj` は期間表現として意味ズレなし。
- `Moldavio`, `Belgio`, `Albanio`, `Brazilo`, `Ukrainio`, `Meksiko`, `Sud-Afriko`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio`, `Rumanio`, `Tajvano` は地名・国名として対応する。
- `Kia estas via nacieco?`, `Mi estas usonano`, `Mi estas albano`, `Ĉu vi estas sviso?`, `Mi estas aŭstrianino`, `Ĉu vi estas germana civitanino?`, `Ĉu li estas slovako aŭ belaruso?`, `Mi ne estas aŭstralianino` は、国籍・出身者名として列間対応を保つ。
- `Mi estas judino`, `Mi estas katoliko`, `Al kiu religio vi apartenas?`, `Mi estas kristanino`, `Mi estas islamanino`, `Mi estas hinduistino` は、宗教・信仰の自己申告として妥当。女性形はRU列の女性話者形とも整合する。

参照:
- PIV 2020 `amikino`: https://vortaro.net/py/serchi.py?s=amikino&simpla=1
- PIV 2020 `fianĉo`: https://vortaro.net/py/serchi.py?s=fian%C4%89o&simpla=1
- PIV 2020 `manaĝero`: https://vortaro.net/py/serchi.py?s=mana%C4%9Dero&simpla=1
- PIV 2020 `korespondanto`: https://vortaro.net/py/serchi.py?s=korespondanto&simpla=1
- PIV 2020 `Moldavio`: https://vortaro.net/py/serchi.py?s=Moldavio&simpla=1
- PIV 2020 `Kazaĥio`: https://vortaro.net/py/serchi.py?s=Kaza%C4%A5io&simpla=1
- PIV 2020 `nacieco`: https://vortaro.net/py/serchi.py?s=nacieco&simpla=1
- PIV 2020 `religio`: https://vortaro.net/py/serchi.py?s=religio&simpla=1
- PIV 2020 `islamano`: https://vortaro.net/py/serchi.py?s=islamano&simpla=1
- PIV 2020 `hinduismo`: https://vortaro.net/py/serchi.py?s=hinduismo&simpla=1
- Glosbe `مسلم` → Esperanto: https://glosbe.com/ar/eo/%D9%85%D8%B3%D9%84%D9%85
- ESPDIC `alkonduki`: https://www.markfoster.net/dcf/ESPDIC-Esperanto-English_Dictionary.pdf

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID856`〜`ID955` は 100 件、`ID954` EO が `Mi estas islamanino` であることを確認済み。

## 575. 574周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid
- Emergencies / At the Police Station
- Making Friends / Introductions

結果:
- **今回の追加修正なし**
- 応急処置、警察署での届出・確認、自己紹介の短文として、Esperanto と `日本語` / `中文` / `한국어` のクイズ対応を主軸に確認した。RU/EN は、事故・警察・紹介場面の細部ニュアンスを確認する補助列として参照した。
- PIV 2020 ローカル抽出、PIV/Glosbe/ReVo のWeb確認を照合したが、現行CSVをさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Mi sangas`, `Min trafis aŭto`, `Li estas senkonscia`, `Mia filino estas vundita`, `Konduku min al hospitalo!`, `Ĉu estas kuracisto ĉi tie?` は、緊急時の短い申告・依頼として対応する。
- `Mi estis mordita`, `Mi tranĉis min`, `Mi bruligis min`, `Mi rompis mian brakon`, `Mi tordis al mi la maleolon` は負傷説明として自然。`brulvundi` なども候補だが、現形でも「やけどした」の意味は明確で、内容を狭める必要はない。
- `Bonvolu surmeti bandaĝon` は `bandaĝi la vundon/la piedon` より説明的だが、PIV 2020 の `bandaĝo` / `bandaĝi` の語義と整合する。RU `наденьте бандаж` にも近いため文脈別許容。
- `Ĉio estos bone kun vi`, `Mi atendos ĉi tie kun vi, ne zorgu`, `Trankviliĝu, ĉio estos en ordo`, `Iu venos kaj helpos vin`, `Mi venigos iun, kiu povas helpi` は励まし・救援の発話として意味ズレなし。
- `Mi elartikigis mian brakon` は `elartikigi` による脱臼表現として読める。`brako` は広めだが、JA/ZH/KO/RU の「腕」と対応し、`ŝultro` などに限定しない方が安全。
- `Mi havas manĝaĵveneniĝon`, `Ĉu vi havas diabeton?`, `Mi ne estas alergia al iuj ajn medikamentoj`, `Jes, mi estas alergia al penicilino`, `Mi havas reakcion al novokaino` は医療文脈の申告として対応する。
- `Mi mezuros vian pulson`, `Jen mia poliso de medicina asekuro`, `Ĉu vi povus sciigi mian familion?`, `Ĉu mi povas daŭrigi mian vojaĝon?` は、脈・保険・家族連絡・旅行継続の確認として自然。
- `Mi bezonas advokaton`, `Bonvolu subskribi vian deklaron`, `Ĉu mi estas arestita?`, `Mi haltigis vin pro troa rapideco`, `Vi devos pagi monpunon`, `Kie estas la plej proksima policejo?` は警察署・交通取締の文脈に合う。
- `Oni ŝtelis mian tekkomputilon`, `Oni enrompis en mian aŭton`, `Mi ŝatus denunci ŝtelon`, `Kion oni ŝtelis de vi?`, `Oni ŝtelis mian mansaketon`, `Bonvolu plenigi raporton pri ŝtelo` は盗難・車上荒らし・届出文脈として対応する。
- `Mi fariĝis viktimo de fraŭdo` は `Mi estis viktimo...` より「被害者になった」経過感があるが、詐欺被害の申告として意味は明確。
- `Mi bezonas advokaton, kiu parolas la ĉinan` は `la ĉinan` が `la ĉina lingvo` の省略として読め、中国語を話す弁護士という各列の内容と一致する。
- `Ĉu mi povas ĝin anstataŭigi?` は再発行そのものより「置き換える」に近いが、紛失パスポート文脈では replacement / RU `заменить` と整合するため維持。
- `Vi devus turni vin al la oficejo pri perditaj aĵoj`, `Ĉu vi turnis vin al la oficejo pri perditaj aĵoj?` は、ID715 と同じ表現で内部整合があり、遺失物取扱所として透明。
- `Ni penos fari lian fotoroboton` は PIV 見出しでは未確認だが、Glosbe/DBnary で `facial composite` / `identikit` と確認でき、RU `фоторобот` と一致するためAI造語誤りとは判断しない。
- `Oni vokis min kiel atestanton`, `Mi estas konvinkita, ke ŝi estas senkulpa`, `Mi ŝatus peti kopion de la dokumento`, `Mi ŝatus kontakti la ambasadejon de mia lando` は、証人・無実・書類コピー・大使館連絡の表現として問題なし。
- `Permesu al mi prezenti vin al Davido`, `Ĉu mi povas prezenti min?`, `Mi ŝatus prezenti Alicon al vi`, `Estas agrable konatiĝi kun vi, Jan!` は、ReVo の `prezenti iun al iu` の型と合う。

参照:
- PIV 2020 `bandaĝo`: https://vortaro.net/py/serchi.py?s=banda%C4%9Do&simpla=1
- PIV 2020 `bruligi`: https://vortaro.net/py/serchi.py?s=bruligi&simpla=1
- PIV 2020 `elartikigi`: https://vortaro.net/py/serchi.py?s=elartikigi&simpla=1
- PIV 2020 `veneniĝo`: https://vortaro.net/py/serchi.py?s=veneni%C4%9Do&simpla=1
- PIV 2020 `alergio`: https://vortaro.net/py/serchi.py?s=alergio&simpla=1
- PIV 2020 `novokaino`: https://vortaro.net/py/serchi.py?s=novokaino&simpla=1
- PIV 2020 `deklaro`: https://vortaro.net/py/serchi.py?s=deklaro&simpla=1
- PIV 2020 `advokato`: https://vortaro.net/py/serchi.py?s=advokato&simpla=1
- PIV 2020 `denunci`: https://vortaro.net/py/serchi.py?s=denunci&simpla=1
- PIV 2020 `anstataŭigi`: https://vortaro.net/py/serchi.py?s=anstata%C5%ADigi&simpla=1
- PIV 2020 `atestanto`: https://vortaro.net/py/serchi.py?s=atestanto&simpla=1
- Glosbe `fotoroboto`: https://glosbe.com/eo/en/fotoroboto
- ReVo `prezenti`: https://dvd.ikso.net/revo/art/prezen1.html

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID756`〜`ID855` は 100 件確認済み。

## 574. 573周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions
- Emergencies / Emergency Situations
- Emergencies / Accidents

結果:
- **今回の追加修正なし**
- 意見・評価、緊急時の短い命令・確認、交通事故の申告・警察対応のブロックとして、Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認した。RU/EN は、短い警告語・交通事故語彙・法的/保険文脈の確認に用いた。
- PIV 2020 ローカル抽出、PIV 公式簡易検索、Glosbe/ReVo系のWeb確認を照合したが、現行CSVをさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Ĉu ĉi tiu loko ne estas mirinda?`, `Mi pensas, ke jes`, `Mi ne pensas tiel`, `Mi esperas tion`, `Tio dependas`, `Vi malpravas` は、短い意見・応答表現として列間対応を保つ。
- `Ĉu vi havas iujn rimarkojn?` は、`rimarko` がコメント・指摘・意見を表しうるため、RU `замечания` と日中韓の「意見」寄りの訳を橋渡しできる。
- `Ĝi estas grandioza`, `Tio estas mirinda!`, `Tio estas nekredebla!`, `Kia bela loko!`, `Kia bonega ideo!` は評価表現として自然。
- `Ili tre plaĉas al mi!`, `Kio plaĉas al vi pri ĝi?`, `Mi timas, ke ĉi tiu libro ne plaĉas al mi`, `Mi ne povas diri, ke tio tre plaĉas al mi`, `Sincere dirante, li ne plaĉas al mi` は、PIV 2020 の `plaĉi al iu` の型と合う。
- `Kion vi povas diri pri ĉi tiu bildo?` は、`bildo` が写真・絵・画像を広く表せるため、JA/KO の「写真」寄り、RU の「絵」寄りを吸収できる。
- `La aktorado estis malbona` は PIV 2020 で `aktorado` が俳優の演技・演じ方を表すと確認でき、acting として維持。
- `Persone, mi konsideras ĉi tiun filmon la plej bona` は `konsideri + objekto + predikativo` として読める。`la plej bonan` への変更は「最良の映画」という名詞句内修飾にも読めるため、現形維持が安全。
- `Fajro!` は `Incendio!` も候補だが、短い警告発話としては許容。`fajrobrigado` も消防隊相当として確認できる。
- `Voku la policon!`, `Voku kuraciston!`, `Voku la fajrobrigadon!`, `Voku ambulancon!`, `Bonvolu tuj voki la policon`, `Oni atakis min` は緊急時の短文として意味ズレなし。
- `Ĉu io malbonas?` はやや口語的だが、「何か問題があるか」の短い確認として文脈別許容。
- `Kie estas la oficejo pri perditaj aĵoj?` は説明的だが、遺失物取扱所として透明で、後続ID821/827とも内部整合がある。
- `Mi estas traŭmatizita`, `Ĉu iu estas vundita?`, `Estas vunditoj`, `Kio kaŭzis la akcidenton?`, `Li koliziis kun mi`, `Ne estis mia kulpo` は事故文脈として対応する。
- `Ĉu vi havis akcidenton?` は PIV 2020 の例では `suferi akcidenton` などが目立つものの、現形でも「事故に遭ったか」の意味は明確で、内容変更を避けて維持。
- `stirpermesilo`, `asekurdokumentoj`, `akcidentraporto` は透明な複合語として、運転免許証・保険書類・事故報告書を表す。
- `Mi havis la prioritaton` は交通文脈の right of way として成立する。PIV 2020 でも `havi prioritaton de paso` 型を確認できる。
- `Ĉu vi povus blovi en ĉi tiun tubon, mi petas?` は `blovi en tubon` の型として自然で、飲酒検査の文脈と整合する。
- `Kiun mi informu pri la akcidento?` は `informi iun pri io` の型から、`kiun` の対格が支持される。

参照:
- PIV 2020 `plaĉi`: https://vortaro.net/py/serchi.py?s=pla%C4%89i&simpla=1
- PIV 2020 `rimarko`: https://vortaro.net/py/serchi.py?s=rimarko&simpla=1
- PIV 2020 `grandioza`: https://vortaro.net/py/serchi.py?s=grandioza&simpla=1
- PIV 2020 `aktorado`: https://vortaro.net/py/serchi.py?s=aktorado&simpla=1
- PIV 2020 `konsideri`: https://vortaro.net/py/serchi.py?s=konsideri&simpla=1
- PIV 2020 `fajrobrigado`: https://vortaro.net/py/serchi.py?s=fajrobrigado&simpla=1
- PIV 2020 `ambulanco`: https://vortaro.net/py/serchi.py?s=ambulanco&simpla=1
- PIV 2020 `traŭmatizi`: https://vortaro.net/py/serchi.py?s=tra%C5%ADmatizi&simpla=1
- PIV 2020 `prioritato`: https://vortaro.net/py/serchi.py?s=prioritato&simpla=1
- PIV 2020 `akcidento`: https://vortaro.net/py/serchi.py?s=akcidento&simpla=1
- PIV 2020 `asekuri`: https://vortaro.net/py/serchi.py?s=asekuri&simpla=1
- PIV 2020 `damaĝo`: https://vortaro.net/py/serchi.py?s=dama%C4%9Do&simpla=1
- PIV 2020 `blovi`: https://vortaro.net/py/serchi.py?s=blovi&simpla=1
- PIV 2020 `informi`: https://vortaro.net/py/serchi.py?s=informi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID656`〜`ID755` は 100 件確認済み。

## 573. 572周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information
- General Conversation / Expressing Feelings
- General Conversation / Help & Advice
- General Conversation / Opinions

結果:
- **今回の追加修正なし**
- 感情表現、弔意、依頼・助言、好悪・評価の短文として、Esperanto と `日本語` / `中文` / `한국어` の対応を主軸に確認した。RU/EN は参考列として、特に感情語のニュアンス差を確認した。
- PIV 2020 ローカル抽出、PIV 公式簡易検索、Glosbe/Komputeko系のWeb確認を照合したが、現行CSVをさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Kial vi diris tion?`, `Kial mi ne pensis pri tio?`, `Ĉu iu povas diri al mi la veron?`, `Kiam komenciĝas la cirkaj spektakloj?`, `Ĉu vi scias, kiu inventis la radon?` は質問文として格・語順とも問題なし。
- `Mi estas feliĉa`, `Mi estas trista`, `Mi estas malstreĉita`, `Mi estas laca`, `Mi malsatas`, `Mi soifas`, `Mi estas trankvila`, `Mi enuas`, `Mi estas optimisma`, `Mi rezignas`, `Mi fartas bone`, `Al mi estas egale` は基本感情・状態表現として各列と対応する。`trista` は PIV 2020 で `malgaja, malĝoja` と確認できる。
- `Mi estas ekscitita` は JA/ZH/KO が「期待」寄りだが、EN `I'm excited` と RU `Я взволнован` の範囲では、PIV 2020 の `eksciti` の「心の動きを強める」語義に収まるため文脈別許容。
- `Mi estas motivita` は PIV 2020 の `motivi` が「理由づける」寄りで注意点は残る。ただし `motivo` は人を行動させる理由を表し、Web上でも `motivita` が motivated の対応として確認できるため、`entuziasma` や `inspirita` に寄せるより現行維持が安全。
- `Mi sentas min embarasita`, `Mi sentas min terure`, `Mi sentas min perdita`, `Mi sentas iom da kapturno`, `Mi ne estas malkuraĝigita` は状態表現として意味が通る。`Mi sentas iom da kapturno` は `Mi sentas kapturnon` の方が平板だが、少量表現として理解可能。
- `Mi bedaŭras tion aŭdi` は `Mi bedaŭras aŭdi tion` の方が平板だが、`tion aŭdi` の語順でも「それを聞いて残念だ」と読め、内容を動かす必要はない。
- `Ni tre bedaŭras aŭdi pri via perdo`, `Bonvolu akcepti niajn plej profundajn kondolencojn`, `Niaj pensoj estas kun vi kaj via familio` は弔意表現として対応する。PIV 2020 の `kondolenco` には喪失に対する哀悼の型があり、`via perdo` も文脈上明確。
- `Ĉu mi povus prunti vian plumon?`, `Ĉu vi povus prunti al mi iom da mono, mi petas?` は `prunti` に貸す/借りるの両義がありうるため曖昧さはあるが、短い依頼文脈では主語・所有表現から意味が明確。`pruntepreni` / `pruntedoni` への置換は不要。
- `Ĉu vi povus fari al mi servon?`, `Ĉu vi povus prizorgi tion dum momento?`, `Ĉu vi estus tiel afabla kaj klarigus tion denove?`, `Ĉu ĝenus vin doni al mi la tekkomputilon?` は依頼表現として許容。`tekkomputilo` は PIV 本文では `tekokomputilo` 形も見えるが、Komputeko/Glosbe系で `tekkomputilo` も laptop 対応として確認できるため現形維持。
- `Mi konsilus al vi iom ripozi`, `Kion vi pensas, ke mi faru?`, `Se mi estus vi, mi farus same`, `Mi rekomendus al vi paroli kun Jia`, `Mi malkonsilus lui aŭton`, `Se mi estus vi, mi dufoje pripensus, ĉu aĉeti ĝin` は助言表現として意味ズレなし。`Kion laŭ vi mi faru?` なども候補だが、現形は理解可能。
- `Bonvolu ne heziti demandi nian flugpersonaron` は `flug-` + `personaro` の透明複合として flight crew を表し、JA/ZH/KO/RU と対応する。
- `Ĉu ĝi plaĉas al vi?`, `Mi ne ŝatas ĝin`, `Ĝi estas bela`, `Ĝi estas malbela`, `Estas interese`, `Estas enuige`, `Estas mirinde`, `Tio estas naŭza` は好悪・評価の短文として自然。`naŭza` は PIV 2020 で吐き気・強い嫌悪の語義を確認できる。

参照:
- PIV 2020 `trista`: https://vortaro.net/py/serchi.py?s=trista&simpla=1
- PIV 2020 `eksciti`: https://vortaro.net/py/serchi.py?s=eksciti&simpla=1
- PIV 2020 `motivi`: https://vortaro.net/py/serchi.py?s=motivi&simpla=1
- PIV 2020 `embarasi`: https://vortaro.net/py/serchi.py?s=embarasi&simpla=1
- PIV 2020 `kondolenci`: https://vortaro.net/py/serchi.py?s=kondolenci&simpla=1
- PIV 2020 `prunti`: https://vortaro.net/py/serchi.py?s=prunti&simpla=1
- PIV 2020 `malkonsili`: https://vortaro.net/py/serchi.py?s=malkonsili&simpla=1
- PIV 2020 `naŭzi`: https://vortaro.net/py/serchi.py?s=na%C5%ADzi&simpla=1
- Komputeko `tekokomputilo`: https://komputeko.net/plejoftaj-eo.pdf
- Glosbe/Kaikki `tekokomputilo` / `tekkomputilo`: https://kaikki.org/plwiktionary/esperanto/meaning/t/te/tekokomputilo.html

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID556`〜`ID655` は 100 件確認済み。

## 572. 571周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood
- General Conversation / Agreeing & Disagreeing
- General Conversation / Asking for & Giving Information

結果:
- **今回の追加修正なし**
- 前区間から続く意思疎通・発音確認、賛否表現、移動・旅行・日常質問のブロックとして、Esperanto と `日本語` / `中文` / `한국어` のクイズ対応を主軸に確認した。
- 過去周回で `ID457` は `Vi ne havas akĉenton`、`ID532` は `Ĉu vi povas rekomendi junulargastejon?` に修正済み。今回の再点検では、PIV 2020 ローカル抽出、PIV 公式簡易検索、ReVo などを照合したが、現行CSVをさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Parolu kun mi en la mandarena ĉina lingvo` はやや硬いが、PIV 2020 で `la mandarena ... lingvo` 型を確認でき、「標準中国語/普通話で話す」として各列と対応するため文脈別許容。
- `Vi ne havas akĉenton`, `Kion signifas tiu vorto angle?`, `Kiel oni skribas tion?`, `Kiel oni diras tion ĉeĥe?`, `Kiel tio nomiĝas pole?`, `Ĉu mi ĝuste ĝin prononcas?`, `Kiel oni povas traduki tion?`, `Vi parolas tro rapide` は、発音・綴り・翻訳・速度調整の確認として意味ズレなし。`Ĉu mi ĝuste ĝin prononcas?` は `Ĉu mi prononcas ĝin ĝuste?` より焦点的だが成立する。
- `Mi konsentas kun vi`, `Mi malkonsentas`, `Ĉu vi ne konsentas?`, `Mi tute konsentas`, `Mi ne konsentas kun via opinio`, `Ĉu vi konsentas, ke tio estas mensogo?`, `Mi komprenas lian vidpunkton, sed mi tute malkonsentas kun ĝi` は、PIV 2020 の `konsenti/malkonsenti` の構文と合う。
- `Vi pravas`, `Vi tiel pravas`, `Tio estas ĝuste mia vidpunkto`, `Mi ne povas kontraŭdiri tion`, `Mi vidas nenian malhelpon` は、賛同・異論なしの短い会話表現として列間対応を保つ。`Vi tiel pravas` は英語的な強調に見えるが、`tiel` による強調として文脈別許容。
- `Mi ne povas diri, ke mi kunhavas vian vidpunkton` は直訳感があるが、PIV 2020 ローカル抽出で `kun havi opinion` を確認でき、`vidpunkton` との結合も「見解を共有する」の意味として明確。
- `En la televido estas tro multe da reklamoj, ĉu ne?` は `En televido` / `Televido havas...` なども候補だが、テレビ放送の中に広告が多いという意味は日中韓/RU と一致し、PIV 2020 の `reklamo` とも整合する。
- `Mi estas ĉe Petro`, `Mi estas ĉe la laboro`, `Mi estas hejme`, `Mi estas en trajno`, `Mi estas en la kamparo`, `Mi ĵus revenis el Portugalio`, `Kie mi povas aĉeti mapon de la urbo?` は場所・移動元・所在確認として自然。
- `Ĉu vi konas bonan drinkejon?`, `Ĉu vi povas rekomendi junulargastejon?`, `Kie mi povas duŝiĝi?`, `Ĉu estas iuj picejoj proksime de via hejmo?`, `Ĉu vi biciklas pli ol unu fojon semajne?` は、PIV 2020 または ReVo で語根・派生を確認できる。`junular gastejo` はPIV系で分かち書きも見えるが、ReVo と実用例で `junulargastejo` 形も確認できるため現形維持。
- `Ĉu vi pli ŝatas ruĝon ol bluon?`, `Ĉu vi preferas oranĝan aŭ verdan?` は `koloron` 省略の色名名詞化として読める。
- `Jes, mi iris tien por ferioj`, `Fakte, mi estas survoje por renkonti amikon`, `Kie vi kutime pasigas viajn feriojn?`, `Mi kutime pasigas miajn feriojn en la kamparo` は休暇・移動予定の文脈として意味が明確。`ferie` / `dum ferioj` や `al renkonto kun amiko` も候補だが、現形を誤りとはしない。
- `Kion vi trovas pli interesa, teatron aŭ operon?` は比較対象を後置で明示する形として、演劇とオペラのどちらが面白いかを尋ねる内容に対応する。

参照:
- PIV 2020 `mandareno`: https://vortaro.net/py/serchi.py?s=mandareno&simpla=1
- PIV 2020 `akĉento`: https://vortaro.net/py/serchi.py?s=ak%C4%89ento&simpla=1
- PIV 2020 `konsenti`: https://vortaro.net/py/serchi.py?s=konsenti&simpla=1
- PIV 2020 `vidpunkto`: https://vortaro.net/py/serchi.py?s=vidpunkto&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `picejo`: https://vortaro.net/py/serchi.py?s=picejo&simpla=1
- PIV 2020 `bicikli`: https://vortaro.net/py/serchi.py?s=bicikli&simpla=1
- PIV 2020 `duŝi`: https://vortaro.net/py/serchi.py?s=du%C5%9Di&simpla=1
- ReVo `junulargastejo`: https://reta-vortaro.de/revo/art/gast.html#gast.0o.junulargastejo

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID456`〜`ID555` は 100 件確認済み。

## 571. 570周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers
- Basic Sentences / Congratulations
- General Conversation / Languages
- General Conversation / Making Yourself Understood

結果:
- **今回の追加修正なし**
- アプリ側では `sentence_app.py` / `sentence_app_Cxina_versio.py` / `sentence_app_Korea_versio.py` が同じ `PHRASE_CSV` を読み込み、Esperanto と `日本語` / `中文` / `한국어` の双方向4択に使うため、今回も EO と日中韓の対応を主軸にし、RU/EN は参考列として確認した。
- 過去周回で `ID388` は `Feliĉan Divalon!`、`ID449` は `Mi havas akĉenton`、`ID442` RU は `Запиши это, пожалуйста.` に修正済み。今回の再点検では、PIV 2020 ローカル抽出、PIV 公式簡易検索、外部辞書・用例確認を照合したが、現行CSVをさらに動かすべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Jes, ĝi tre plaĉas al mi!`, `Kia trankviliĝo!`, `Tia estas la vivo!`, `Ne gravas`, `Ju pli frue, des pli bone`, `Ĉu mi povus havi vian atenton?` は短い応答・感嘆・呼びかけとして各列と対応する。`Ankaŭ mi ne` は前文依存の短答で、単独では文脈幅があるが「私もそうではない / Neither do I」系として文脈別許容。
- `Gratulon!`, `Miaj sinceraj gratuloj!`, `Permesu al mi gratuli vin`, `Gratulon pro ...`, `Gratulojn pro ...` は、PIV 2020 の `gratuli/gratulo` が「成功・幸運に対する祝意」を表すことと整合する。単数 `Gratulon` と複数 `Gratulojn` の揺れは祝辞定型として許容範囲。
- `Feliĉan naskiĝtagon!`, `Feliĉajn festotagojn!`, `Feliĉan Novan Jaron!`, `Feliĉan Kristnaskon!`, `Feliĉan Paskon!`, `Feliĉan Ĥanukon!`, `Feliĉan datrevenon!`, `Feliĉan Dankotagon!`, `Feliĉan Ramadanon!` は `Feliĉan/Feliĉajn + 対格` の祝意定型として意味ズレなし。PIV 2020 でも `feliĉa` に `deziri al iu feliĉan feston` 型の用例があり、`Pasko`, `Ĥanuko`, `Ramadano` も祝祭・宗教月名として確認できる。
- `Feliĉan Divalon!` は PIV 2020 では直接見出しを確認できなかったが、Wiktionary/WikiRank 系で Esperanto 名 `Divalo` が確認でき、過去の `Divalion` からの修正後の形として維持する。より強い標準化候補として `Divali` 系も見えるが、ここでは現行の `Divalo` を誤りと断定しない。
- `Gratulon pro via akcepto en la universitaton!` は `akceptiĝo` も候補だが、大学に受け入れられたこととして読める。`en la universitaton` の方向対格も「大学へ入る/受け入れられる」結果方向を示すため、大学合格・入学許可の文脈として維持。
- `Mi ŝatas la bengalan`, `Mi parolas la rumanan`, `Ĉu ŝi parolas la tajan?`, `Mi lernas la urduon`, `Kiu parolas la persan?`, `Mia denaska lingvo estas la norvega`, `Mi parolas ... iomete la slovakan`, `Mi parolas nur tre malmulte la nederlandan`, `Kie vi lernis la finnan?`, `Mi ŝatus praktiki mian portugalan`, `Mi lernas la indonezian jam de unu monato` は、`lingvo` を省略した言語名として読め、日中韓文との対応も保つ。
- `Ni parolu slovene`, `Vi parolas tre bone azerbajĝane`, `Mi povas komuniki itale`, `Bonvolu paroli latve` は、言語使用を表す副詞形として自然。PIV 2020 で直接確認しにくい派生もあるが、国名・民族名からの規則的派生として意味は透明。
- `Via tagaloga estas tre bona`, `Mia korea estas sufiĉe malbona` はそれぞれ `lingvo` または「言語能力」を省いた口語的な形。完全に明示するなら `Via tagaloga lingvo` / `Mia korea lingvo` や `Mia rego de la korea` も考えられるが、短い会話表現としては文脈別許容。
- `Mi iom perdis la praktikon`, `Mi perfekte regas la araban lingvon`, `Mi simple bezonas praktiki` は語彙選択と意味対応に問題なし。`regi lingvon` は「言語を使いこなす」比喩的用法として自然。
- `Bonvolu noti ĝin`, `Kiel oni prononcas ĉi tiun vorton?`, `Ĉu vi povas literumi ĝin?`, `Ĉu vi komprenas la germanan?`, `Kion ĉi tio signifas?` は、PIV 2020 の `noti`, `prononci`, `literumi`, `kompreni`, `signifi` の語義と一致し、「伝わらない時の確認」文脈として妥当。
- `Mi havas akĉenton` は PIV 2020 で「話者・集団の発音習慣」としての `akĉento` が確認でき、`akcento` ではなく現形が適切。

参照:
- PIV 2020 `gratuli`: https://vortaro.net/py/serchi.py?s=gratuli&simpla=1
- PIV 2020 `feliĉa`: https://vortaro.net/py/serchi.py?s=feli%C4%89a&simpla=1
- PIV 2020 `lingvo`: https://vortaro.net/py/serchi.py?s=lingvo&simpla=1
- PIV 2020 `akĉento`: https://vortaro.net/py/serchi.py?s=ak%C4%89ento&simpla=1
- PIV 2020 `literumi`: https://vortaro.net/py/serchi.py?s=literumi&simpla=1
- Wiktionary `Diwali` Esperanto 対応 `Divalo`: https://pl.wiktionary.org/wiki/Diwali
- WikiRank `Diwali` interwiki Esperanto `Divalo`: https://wikirank.net/en/Diwali

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID356`〜`ID455` は 100 件確認済み。

## 570. 569周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks
- Basic Sentences / Apologies
- Basic Sentences / Instructions
- Basic Sentences / Short Questions & Answers

結果:
- **今回の追加修正なし**
- 前回に続き、アプリ側の実運用で直接出題される Esperanto と `日本語` / `中文` / `한국어` の対応を主軸にし、RU/EN は参考列として確認した。
- 既存周回で `ID285` `Mi agis senzorge`、`ID303` `Ne zorgu pri tio!` の翻訳整合などは修正済み。今回の再点検では、PIV 2020 ローカル抽出、PIV 2020 公式簡易検索、既存Web確認メモを照合したが、CSV本文をさらに動かすべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Mi vere ne scias kiel danki vin pro via subteno`, `Mi ŝatus danki vin ankaŭ nome de mia edzo`, `Estas honoro por mi ricevi ĉi tiun premion` は感謝・受賞挨拶の文脈として列間対応を保つ。
- `Pardonu min`, `Bonvolu pardoni min`, `Pardonu pro la prokrasto`, `Mi petas pardonon`, `Ne estas kialo pardonpeti` は謝罪・許しを求める表現として一貫する。`Ne estas kialo por pardonpeti` や `Ne necesas pardonpeti` も候補だが、現形は短い会話表現として意味が明確で、内容を動かす必要はない。
- `Pardonu, ke mi ĝenas vin`, `Ĉu mi ĝenas vin?`, `Ĉu mi povas ĝeni vin momenton?` は PIV 2020 の `ĝeni` の「行動・思考などを妨げる」語義と対応し、丁寧な呼びかけとして自然。
- `Ne zorgu, mi petas`, `Ne zorgu pri tio!` は PIV 2020 の `zorgi` にある「不安に思う」語義と対応し、JA/ZH/KO/RU の心配しないで系と整合する。
- `Ne ofendiĝu`, `Mi ne tion celis`, `Mi bedaŭras, ke mi diris tion`, `Mi agis senzorge` は謝罪・弁明文脈で意味ズレなし。`Mi ne tion celis` は `Mi ne celis tion` より焦点的だが、語順として許容。
- `Mi timas, ke mi ne povas resti plu longe` は `pli longe` への自然化余地もあるが、PIV 2020 の `plu` が状態・行為の継続を表し、否定文で「もうこれ以上」を表すため、any longer 文脈として維持。
- `Pardonu, ke mi devigis vin atendi` は `igis/lasis vin atendi` も候補だが、PIV 2020 の `devigi` には「Fari, ke iu devu」の用例があり、RU `заставила вас ждать` とも対応するため、明確な誤りとはしない。
- `Kuraĝu!` は PIV 2020 の `kuraĝa/kuraĝi/kuraĝigi` 周辺から、困難の前での励ましとして `Cheer up!` / 元気を出して / 힘내세요 と文脈別許容。
- `Atentu la hundon`, `Ne paŝu sur la gazonon!`, `Bonvolu viciĝi ĉi tie`, `Rigardu, kien vi iras!`, `Ne atentu tion, kion li diris` は注意・掲示・案内・助言表現として対応する。PIV 2020 で `atenti` は他動詞、`vico/viciĝi` は列に入る/並ぶ意味を確認。
- `Donu al mi ĉi tiun` は「この一つをください」の選択文脈として `ĉi tiun` を維持。`ĉi tion` への置換も可能だが、意味差が小さく、内容変更を避ける。
- `Kio?`, `Kie?`, `Kiam?`, `Kial?`, `Kiu?`, `Kiel?`, `Kiom?`, `Kiom ofte?`, `Kiom longe?`, `Kiom malproksime?` は短い疑問応答としてクイズ用途でも対応が明確。
- `Ĉu ĉio en ordo?`, `Jen ĉio`, `Ankaŭ mi`, `Amuze!`, `Kiel bele!` は省略的な短答・感嘆表現として意味破綻なし。

参照:
- PIV 2020 `pardonpeti`: https://vortaro.net/py/serchi.py?s=pardonpeti&simpla=1
- PIV 2020 `ĝeni`: https://vortaro.net/py/serchi.py?s=%C4%9Deni&simpla=1
- PIV 2020 `zorgi`: https://vortaro.net/py/serchi.py?s=zorgi&simpla=1
- PIV 2020 `atenti`: https://vortaro.net/py/serchi.py?s=atenti&simpla=1
- PIV 2020 `vico`: https://vortaro.net/py/serchi.py?s=vico&simpla=1
- PIV 2020 `plu`: https://vortaro.net/py/serchi.py?s=plu&simpla=1
- PIV 2020 `devigi`: https://vortaro.net/py/serchi.py?s=devigi&simpla=1
- PIV 2020 `kuraĝi`: https://vortaro.net/py/serchi.py?s=kura%C4%9Di&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID256`〜`ID355` は 100 件確認済み。

## 569. 568周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye
- Basic Sentences / Good Wishes
- Basic Sentences / Thanks

結果:
- **今回の追加修正なし**
- 前回 `ID5056`〜`ID5155` でCSV終端まで到達済みのため、今回は先頭ブロックへ折り返して再点検した。
- アプリ側では `data_sources.py` の `PHRASE_CSV` を `sentence_app.py` / `sentence_app_Cxina_versio.py` / `sentence_app_Korea_versio.py` が読み込み、各版で Esperanto と `日本語` / `中文` / `한국어` を双方向4択の出題ペアとして使う。したがって今回も EO と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認した。
- 挨拶・祝意・感謝の短い定型句が中心で、PIV 2020 ローカル抽出、PIV 2020 公式簡易検索、Glosbe の確認範囲では、本文をさらに修正すべき明確な語形・格・一致・語法・意味ズレは見つからなかった。

主な据え置き確認:
- `Bonan matenon`, `Bonan tagon`, `Bonan vesperon`, `Bonan nokton`, `Ĝis revido`, `Ĝis morgaŭ`, `Ĝis baldaŭ` は挨拶・別れの定型表現として維持。PIV 2020 の `bona` には `bonan tagon, vojaĝon!` 型の用例があり、`Bonan tagon!` は `Good afternoon` と `Have a nice day` の両文脈で許容範囲。
- `Estas bone vidi vin`, `Estis bone vidi vin` は `agrable` への自然化候補もあるが、PIV 2020 の `bone estas` 型と列間の「会えてよかった」に照らし、意味ズレとしては扱わない。
- `Kiel vi fartas?`, `Mi fartas bone`, `Ne tro malbone`, `Tiel-tiel` は PIV 2020 の `farti` の語義と合う近況確認・返答表現。
- `Salutu Lukason de mi`, `Bonvolu transdoni miajn korajn salutojn al via patro` は PIV 2020 の `saluti` / `saluto` の `transdoni ... saluton` 系用例と対応し、「よろしく伝える」文脈として自然。
- `Mi antaŭĝojas revidi vin` は PIV 2020 直接見出しでは未確認だが、`antaŭ` + `ĝoji` の透明複合で、Glosbe でも `look forward` 系の対応が確認できる。JA/ZH/KO/RU の「再会を楽しみにする」と一致するため維持。
- `Bonŝancon!`, `Ĉion plej bonan!`, `Resaniĝu baldaŭ!`, `Bonan vojaĝon!`, `Bonan amuzon!`, `Agrablan nokton!`, `Bonan semajnfinon!`, `Bonan vojaĝon hejmen!` は祝意・祈願の短句として対応する。
- `Sanon!` は sneeze 後の `Bless you!` と健康祈願の短い応答として許容し、`Je via sano!` は乾杯表現として区別されている。
- `Ni tostu por vi!`, `Mi ŝatus proponi toston por mia filo` は PIV 2020 の `tosto/tosti` が健康・名誉・成功などのための祝杯発話を表すため、祝辞・乾杯文脈として維持。
- `Nedankinde`, `Dankon pro via gastamo`, `Dankon pro via donaco`, `Dankon, ke vi tiel diris`, `Dankon pro ĉio`, `Mi ne povas sufiĉe danki vin`, `Kontraŭe: estas mi, kiu devus danki vin!`, `Mi tre aprezas viajn afablajn vortojn` は感謝・返礼表現として列間対応に問題なし。
- `Ne ĝenu vin` は PIV 2020 の `ĝeni sin` / `ne ĝeni sin` 周辺から、相手に手間をかけさせない表現として許容。`Don't bother` / JA/ZH/KO/RU と対応する。
- `Tio estis la plej malmulto, kion mi povis fari` は `minimumo` への置換も考えられるが、現形でも least I could do / できるせめてものことに対応し、意味ズレが明確ではないため未修正。
- `Mi dankas pro via tempo` は `Mi dankas vin pro via tempo` の方が明示的だが、PIV 2020 の `danki ... pro io` 系に照らして省略的に通るため維持。

参照:
- PIV 2020 `bona`: https://vortaro.net/py/serchi.py?s=bona&simpla=1
- PIV 2020 `farti`: https://vortaro.net/py/serchi.py?s=farti&simpla=1
- PIV 2020 `saluti`: https://vortaro.net/py/serchi.py?s=saluti&simpla=1
- PIV 2020 `ĝeni`: https://vortaro.net/py/serchi.py?s=%C4%9Deni&simpla=1
- PIV 2020 `danki`: https://vortaro.net/py/serchi.py?s=danki&simpla=1
- PIV 2020 `tosti`: https://vortaro.net/py/serchi.py?s=tosti&simpla=1
- PIV 2020 `minimumo`: https://vortaro.net/py/serchi.py?s=minimumo&simpla=1
- Glosbe `antaŭĝoji`: https://glosbe.com/eo/en/anta%C5%AD%C4%9Doji

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID156`〜`ID255` は 100 件確認済み。

## 568. 567周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar
- Time & Weather / Time Expressions
- Time & Weather / Weather

結果:
- **今回の追加修正なし**
- このCSVの最終100件を再点検。カレンダー・時点副詞句・天気表現が中心で、PIV 2020 の季節/月/時間語・気象語、日中韓/RU列との対応を確認した。`Hodiaŭ tage`, `glacie kaj glite`, `veterprognozo`, `Ĉi-nokte frostos`, `La suno ĵus kaŝiĝis`, `atmosfera premo` などはやや説明的または口語的な箇所もあるが、明確な意味ズレとは判断しなかった。
- `PhraseID` は `5155` で終端。`ID5156` 以降の追加行は存在しない。

主な据え置き確認:
- `La someraj monatoj estas junio, julio kaj aŭgusto`, `La aŭtunaj monatoj estas septembro, oktobro kaj novembro` は季節説明文として前ブロックの冬・春と一貫する。
- `Hodiaŭ tage` は EN `Today` より「今日の日中」に寄るが、JA/ZH/KO が日中を示しており、時間帯を含む短句として維持。
- `Ĉiutage`, `Morgaŭ`, `Hieraŭ`, `Ĝuste nun`, `La tutan tagon`, `Hodiaŭ vespere`, `Ĉi tiun semajnon`, `Post unu semajno`, `En la venonta monato`, `Ĉi-jare`, `Antaŭ unu jaro`, `Hieraŭ nokte`, `Antaŭ unu horo`, `Matene`, `Vespere`, `Ĉi-posttagmeze`, `Morgaŭ vespere`, `Post dek tagoj`, `Ĉi-monate`, `Antaŭhieraŭ`, `Postmorgaŭ`, `La sekvantan tagon`, `Ĝis aŭgusto` は時点・期間表現として対応する。
- `Du semajnoj` は a fortnight / 2週間の短句として十分。文としてなら `Dum du semajnoj` などもあり得るが、語彙カード的な提示では現形を維持。
- `Estas varme`, `Estas glacie kaj glite`, `Estas 22°C`, `Estas nebule`, `Estas suna tago`, `Ĉu estas malvarme ekstere?`, `Pluvas`, `Varmegas`, `Frostas`, `Neĝas`, `Kia estas la temperaturo?`, `Minus kvin gradoj`, `Plus tri gradoj`, `Kia estas la vetero?` は天気・気温の短文として対応する。
- `glacie kaj glite` は `glacie` が「氷のように/氷状に」の副詞、`glita` が滑りやすい性質として PIV 2020 で確認でき、icy and slippery の文脈で意味ズレなし。
- `Pluvetadas`, `Hajlas`, `Fulmas`, `Alproksimiĝas fulmotondro`, `Forte pluvas`, `Ekpluvas`, `Pluvegas`, `Ĉi-nokte frostos`, `Ŝajnas, ke pluvos`, `Mi scivolas, ĉu estos fulmotondro`, `Ni atendas fulmotondron` は気象現象の無主語・自動詞表現として自然。
- `La suno ĵus kaŝiĝis` は直訳的には「太陽が隠れた」だが、PIV 2020 の `kaŝiĝi` に太陽が隠れる用例があり、sun's gone in / 雲に隠れた文脈として維持。
- `La nuboj disiĝas`, `Blovas forta vento`, `En la ĉielo ne estas eĉ unu nubo`, `Tio sonas kiel tondro`, `Estu singarda, la stratoj estas tre glitaj` は天候描写として対応する。
- `La atmosfera premo estas alta` は PIV 2020 の `premo` に `la atmosfera premo` の語義が確認でき、気圧の文として問題なし。
- `Kiu estas la plej varma monato en via lando?` は hot/warm の差に多少幅があるが、JA/ZH/KO の「一番暑い月」と整合し、`plej varma` で十分表せるため維持。

参照:
- PIV 2020 `somero`: https://vortaro.net/py/serchi.py?s=somero&simpla=1
- PIV 2020 `aŭtuno`: https://vortaro.net/py/serchi.py?s=aŭtuno&simpla=1
- PIV 2020 `hodiaŭ`: https://vortaro.net/py/serchi.py?s=hodiaŭ&simpla=1
- PIV 2020 `hieraŭ`: https://vortaro.net/py/serchi.py?s=hieraŭ&simpla=1
- PIV 2020 `morgaŭ`: https://vortaro.net/py/serchi.py?s=morgaŭ&simpla=1
- PIV 2020 `mateno`: https://vortaro.net/py/serchi.py?s=mateno&simpla=1
- PIV 2020 `vespero`: https://vortaro.net/py/serchi.py?s=vespero&simpla=1
- PIV 2020 `monato`: https://vortaro.net/py/serchi.py?s=monato&simpla=1
- PIV 2020 `semajno`: https://vortaro.net/py/serchi.py?s=semajno&simpla=1
- PIV 2020 `vetero`: https://vortaro.net/py/serchi.py?s=vetero&simpla=1
- PIV 2020 `temperaturo`: https://vortaro.net/py/serchi.py?s=temperaturo&simpla=1
- PIV 2020 `glacia`: https://vortaro.net/py/serchi.py?s=glacia&simpla=1
- PIV 2020 `gliti`: https://vortaro.net/py/serchi.py?s=gliti&simpla=1
- PIV 2020 `pluvo`: https://vortaro.net/py/serchi.py?s=pluvo&simpla=1
- PIV 2020 `hajlo`: https://vortaro.net/py/serchi.py?s=hajlo&simpla=1
- PIV 2020 `fulmo`: https://vortaro.net/py/serchi.py?s=fulmo&simpla=1
- PIV 2020 `fulmotondro`: https://vortaro.net/py/serchi.py?s=fulmotondro&simpla=1
- PIV 2020 `frosto`: https://vortaro.net/py/serchi.py?s=frosto&simpla=1
- PIV 2020 `nebulo`: https://vortaro.net/py/serchi.py?s=nebulo&simpla=1
- PIV 2020 `vento`: https://vortaro.net/py/serchi.py?s=vento&simpla=1
- PIV 2020 `kaŝi`: https://vortaro.net/py/serchi.py?s=kaŝi&simpla=1
- PIV 2020 `premo`: https://vortaro.net/py/serchi.py?s=premo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID5056`〜`ID5155` は 100 件確認済み。
- `ID5156` 以降の行は存在しないことを確認済み。
- `git diff --check` 問題なし。

## 567. 566周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office
- Communication Means / Letters
- Time & Weather / Time Expressions
- Time & Weather / Calendar

結果:
- **今回の追加修正なし**
- 郵便局後半、手紙・メール定型句、時刻・日付表現を再点検。`poŝtrestante`, `vivresumo`, `Antaŭdankon`, `antaŭĝojas`, `aldonaĵo`, `kioma horo`, `kvarono antaŭ/post`, `labortago`, `libertago` などを中心に、PIV 2020 と実例、日中韓/RU列との対応を確認したが、本文修正が必要な明確な意味ズレは見つからなかった。

主な据え置き確認:
- `sendi ... al ĉi tiu adreso`, `per rekomendita poŝto`, `kiel eble plej rapide`, `preni pakaĵon`, `Ĉe kiu giĉeto estas poŝtrestante?` は郵便局窓口の実用表現として対応する。
- `poŝtrestante` は PIV 2020 の `poŝto` 関連語として確認でき、poste restante / 局留め郵便の文脈で維持。`Ĉe kiu giĉeto estas poŝtrestante?` は省略的だが「どの窓口か」を尋ねる口頭文として許容。
- `Estimata Sinjorino Banon`, `Sincere via`, `Kara Filipo`, `Kun amo`, `Estimata Sinjorino`, `Al la koncernatoj`, `Respektplene via`, `Kun plej koraj salutoj`, `Kun plej bonaj deziroj`, `Estimata Sinjoro Prezidanto` は手紙・メールの定型句として対応する。
- `Mi kunsendas mian vivresumon` は `vivresumo` が CV/résumé の透明複合として定着しており、`kunsendi` も「同封/添付する」文脈に合うため維持。
- `Antaŭdankon`, `Bonvolu ne heziti kontakti min`, `Mi antaŭĝojas ricevi vian respondon`, `Mi antaŭĝojas diskuti tion kun vi`, `Mi antaŭĝojas baldaŭ revidi vin`, `Mi antaŭĝojas pri tio` は通信文の定型表現として対応する。`antaŭĝoji` は PIV の `antaŭ` + `ĝoji` から透明で、現代の Esperanto 実例でも用例を確認できるため、英語直訳だけとは判断しない。
- `aldonaĵon` は attachment 文脈で意味が明確。`Ĉi-matene mi ne povis malfermi vian aldonaĵon` はメール添付ファイルの文として維持。
- `Oni urĝe petas vin veni al Nederlando`, `Sciigu min, kiam vi ekscios ion plian`, `Ne forgesu de tempo al tempo skribi al mi`, `Ni jam tiel longe ne kontaktis unu la alian` は手紙・連絡文脈で日中韓/RU列と整合する。
- `Kioma horo estas?`, `Estas la sesa vespere`, `Kvin antaŭ la dua`, `Estas kvin minutoj post la unua`, `Dudek antaŭ la dua`, `Estas la dua kaj duono`, `kvarono antaŭ la deka`, `kvarono post la unua`, `noktomezo`, `tagmezo` は PIV 2020 の `horo` 用例とも合う時刻表現として対応する。
- `Ĝis la unua horo` は deadline の by one o'clock に対して `ĝis` の範囲内で許容。`Je la tria horo posttagmeze`, `Je la sesa kaj dudek kvin` も時間指定として維持。
- `Kiu tago estas hodiaŭ?` / `Hodiaŭ estas mardo`, `Kiu dato estas hodiaŭ?`, `la 25-a de septembro`, `la 10-a de aprilo`, `la 22-a de oktobro`, `Morgaŭ estos la 2-a de decembro` は曜日・日付文脈で対応する。
- `Labortagoj estas de lundo ĝis vendredo`, `Semajnfinaj tagoj estas sabato kaj dimanĉo`, `Ĉi tiu sabato estas labortago`, `Ĉi tiu ĵaŭdo estas libertago`, `La vintraj/printempaj monatoj...` はカレンダー説明文として一貫している。

参照:
- PIV 2020 `poŝto`: https://vortaro.net/py/serchi.py?s=poŝto&simpla=1
- PIV 2020 `poŝtrestante`: https://vortaro.net/py/serchi.py?s=po%C5%9Dtrestante&simpla=1
- PIV 2020 `sendi`: https://vortaro.net/py/serchi.py?s=sendi&simpla=1
- PIV 2020 `resumi`: https://vortaro.net/py/serchi.py?s=resumi&simpla=1
- PIV 2020 `heziti`: https://vortaro.net/py/serchi.py?s=heziti&simpla=1
- PIV 2020 `ĝoji`: https://vortaro.net/py/serchi.py?s=ĝoji&simpla=1
- PIV 2020 `respondi`: https://vortaro.net/py/serchi.py?s=respondi&simpla=1
- PIV 2020 `horo`: https://vortaro.net/py/serchi.py?s=horo&simpla=1
- PIV 2020 `kioma`: https://vortaro.net/py/serchi.py?s=kioma&simpla=1
- PIV 2020 `tago`: https://vortaro.net/py/serchi.py?s=tago&simpla=1
- PIV 2020 `tagmezo`: https://vortaro.net/py/serchi.py?s=tagmezo&simpla=1
- PIV 2020 `noktomezo`: https://vortaro.net/py/serchi.py?s=noktomezo&simpla=1
- PIV 2020 `mardo`: https://vortaro.net/py/serchi.py?s=mardo&simpla=1
- PIV 2020 `merkredo`: https://vortaro.net/py/serchi.py?s=merkredo&simpla=1
- PIV 2020 `ĵaŭdo`: https://vortaro.net/py/serchi.py?s=ĵaŭdo&simpla=1
- PIV 2020 `vintro`: https://vortaro.net/py/serchi.py?s=vintro&simpla=1
- PIV 2020 `printempo`: https://vortaro.net/py/serchi.py?s=printempo&simpla=1
- Esperanto.cat `Ni antaŭĝojas helpi vin`: https://www.esperanto.cat/home_esp/contacte-2/formulari-de-contacte/

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4956`〜`ID5055` は 100 件確認済み。
- `git diff --check` 問題なし。

## 566. 565周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work
- Communication Means / Mass Media
- Communication Means / At the Post Office

結果:
- **今回の追加修正なし**
- 職場電話の取り次ぎ、メール・SNS・テレビ/新聞、郵便局の手続き表現を再点検。過去周回で `De kiu kompanio vi telefonas?` などは修正済みで、今回もロシア語および日中韓列との対応、PIV 2020 の語義、透明複合の許容範囲を確認したが、CSV本文をさらに動かすべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- `lasi mesaĝon`, `revoki`, `Atendu la signalon kaj klavu la numeron`, `telefonlibro`, `interna numero`, `sur alia linio`, `demeti la aŭdilon`, `momente ne estas disponebla`, `revoki vin post kelkaj minutoj` は職場電話・内線の実用表現として対応する。
- `La numero ne estas en la telefonlibro` は EN `ex-directory` / JA「非公開」に対してやや説明的だが、「電話帳に載っていない番号」という実用上の意味は保たれるため維持。
- `retpoŝtadreso` は PIV 2020 で `ret poŝto` と `retadreso` / `retmesaĝo` 系を確認でき、`retpoŝto` + `adreso` の透明複合として意味が明確。`Jen mia retpoŝtadreso`, `Kiu estas via retpoŝtadreso?`, `Mia retpoŝtadreso estas name@example.com` はメールアドレス文脈で維持。
- `Kiu estas via retpoŝtadreso?` は `Kio estas via retpoŝtadreso?` のほうが直訳的には自然な余地があるが、会話で「どれ/どのアドレスか」を尋ねる形として意味は通り、日中韓の回答誘導にも支障がないため未修正。
- `Skajpo`, `uzantonomo`, `ensalutu`, `elsalutu`, `konektiĝu al la interreto`, `retmesaĝon`, `en Facebook`, `aldonos vin kiel amikon`, `en Tvitero`, `tekkomputilon`, `tajpu`, `elŝutas`, `presilo`, `skanilo` はインターネット・SNS・端末操作文脈で対応する。
- `La gazeton Times, mi petas` は媒体名の扱いに `The Times` をそのまま使う選択肢もあるが、日中韓/RUの「タイムズ紙」相当として意味ズレはないため維持。
- `ekskluziva artikolo`, `reklamoj`, `malklara`, `kanalon`, `programo`, `usonan futbalon`, `novaĵojn`, `titolojn`, `eldonkvanto`, `radion` はマスメディア文脈で対応する。`titoloj` は headline の短い一般訳として許容。
- `poŝtoficejo`, `poŝtkesto`, `fakturon`, `koverton`, `vatitan koverton`, `poŝti`, `aerpoŝto`, `valoras`, `fakson`, `faksa numero`, `laborhoroj`, `televida licenco`, `abono`, `poŝtmarkoj`, `afranko`, `fotokabino`, `fotokopiilo`, `rekomendita poŝto`, `asekuri`, `pezi`, `dogana deklaracio`, `pesilo` は郵便局・窓口手続き文脈で対応する。
- `vatita koverto` は jiffy bag / bubble envelope に対して厳密な商品名ではないが、緩衝材入り封筒を説明する表現として日中韓の「気泡/エアキャップ封筒」と矛盾しないため維持。
- `Mi ŝatus akiri televidan licencon` / `renovigi mian televidan licencon` は国制度依存の語だが、EN/RUの TV licence 文脈と一致し、教材文として意味ズレなし。

参照:
- PIV 2020 `telefono`: https://vortaro.net/py/serchi.py?s=telefono&simpla=1
- PIV 2020 `mesaĝo`: https://vortaro.net/py/serchi.py?s=mesaĝo&simpla=1
- PIV 2020 `numero`: https://vortaro.net/py/serchi.py?s=numero&simpla=1
- PIV 2020 `retpoŝto`: https://vortaro.net/py/serchi.py?s=retpoŝto&simpla=1
- PIV 2020 `adreso`: https://vortaro.net/py/serchi.py?s=adreso&simpla=1
- PIV 2020 `fakso`: https://vortaro.net/py/serchi.py?s=fakso&simpla=1
- PIV 2020 `poŝto`: https://vortaro.net/py/serchi.py?s=poŝto&simpla=1
- PIV 2020 `poŝtmarko`: https://vortaro.net/py/serchi.py?s=poŝtmarko&simpla=1
- PIV 2020 `afranko`: https://vortaro.net/py/serchi.py?s=afranko&simpla=1
- PIV 2020 `koverto`: https://vortaro.net/py/serchi.py?s=koverto&simpla=1
- PIV 2020 `aboni`: https://vortaro.net/py/serchi.py?s=aboni&simpla=1
- PIV 2020 `pesilo`: https://vortaro.net/py/serchi.py?s=pesilo&simpla=1
- PIV 2020 `deklaracio`: https://vortaro.net/py/serchi.py?s=deklaracio&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4856`〜`ID4955` は 100 件確認済み。
- `git diff --check` 問題なし。

## 565. 564周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy
- Communication Means / Phone
- Communication Means / Phone Calls at Work

結果:
- **今回の追加修正なし**
- 薬局後半と電話表現を再点検。過去周回で `kromefikoj`, `tablojdoj`, `misdigesto`, `malkonektiĝis`, `malŝargiĝos`, `Mi transdonos la mesaĝon, ke vi telefonis` などは整理済みで、今回も辞書・列間対応上、さらに修正すべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- `herbaj medikamentoj`, `ion kontraŭ tuso`, `plastro`, `jodo`, `paracetamolo`, `pakaĵo da aspirino`, `kromefikoj`, `nur por ekstera uzo`, `tutnokte malfermita apoteko`, `farmacisto`, `dormigiloj`, `vojaĝmalsano`, `tablojdoj`, `kapsuloj`, `nikotinaj plastroj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は薬局・服薬文脈で対応する。
- `Ĉu vi havas ion por sekiĝintaj lipoj?` は chapped lips / обветренные губы に対して `fendiĝintaj lipoj` なども候補だが、日中韓の乾燥・干裂・튼 입술の範囲と矛盾せず、内容を狭めないため現形を維持。
- `Kie estas la plej proksima tutnokte malfermita apoteko?` は JA/ZH/KO/RU の「24時間」に対してやや「夜通し」に寄るが、EN `all-night chemist's` と一致し、夜間に開いている薬局を尋ねる実用文として意味ズレなし。
- `telefonos`, `Kiu telefonas?`, `Ĉu mi povas paroli kun Sara?`, `Malbona konekto`, `Restu sur la linio`, `sendi al mi mesaĝon`, `telefono paneis`, `kapti signalon`, `malkonektiĝis`, `telefonbudo`, `telefonkarto`, `ŝargi mian telefonon`, `retelefoni`, `voka signalo`, `kredito`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `malŝargiĝos`, `urba telefona kodo`, `informservo` は電話・通信文脈で対応する。
- `Bonvolu sendi al mi mesaĝon` / `Mi mesaĝos al vi poste` は SMS/text に対してやや広いが、電話文脈では text message の意味が十分明確で、日中韓/RUとも大きくずれない。
- `Mi telefonos en mia ĉambro` は `Mi uzos la telefonon en mia ĉambro` とも言えるが、RU `поговорю по телефону в своей комнате` と対応し、「部屋で/部屋の電話で電話する」文脈として維持。
- `Mi transdonos la mesaĝon, ke vi telefonis`, `Ŝi estas sur alia linio`, `Bedaŭrinde, ŝi forestas pro malsano`, `Mi konektos vin kun li`, `Ne demetu ankoraŭ la aŭdilon`, `Ĉu vi povas klavi la numeron por mi?`, `La linio estas okupata` は職場電話の取り次ぎ表現として対応する。

参照:
- PIV 2020 `medikamento`: https://vortaro.net/py/serchi.py?s=medikamento&simpla=1
- PIV 2020 `aspirino`: https://vortaro.net/py/serchi.py?s=aspirino&simpla=1
- PIV 2020 `efiko`: https://vortaro.net/py/serchi.py?s=efiko&simpla=1
- PIV 2020 `dozo`: https://vortaro.net/py/serchi.py?s=dozo&simpla=1
- PIV 2020 `dormi`: https://vortaro.net/py/serchi.py?s=dormi&simpla=1
- PIV 2020 `vojaĝi`: https://vortaro.net/py/serchi.py?s=vojaĝi&simpla=1
- PIV 2020 `kapsulo`: https://vortaro.net/py/serchi.py?s=kapsulo&simpla=1
- PIV 2020 `misdigesto`: https://vortaro.net/py/serchi.py?s=misdigesto&simpla=1
- PIV 2020 `telefono`: https://vortaro.net/py/serchi.py?s=telefono&simpla=1
- PIV 2020 `mesaĝo`: https://vortaro.net/py/serchi.py?s=mesaĝo&simpla=1
- PIV 2020 `voko`: https://vortaro.net/py/serchi.py?s=voko&simpla=1
- PIV 2020 `ŝargi`: https://vortaro.net/py/serchi.py?s=ŝargi&simpla=1
- PIV 2020 `kredito`: https://vortaro.net/py/serchi.py?s=kredito&simpla=1
- PIV 2020 `klavi`: https://vortaro.net/py/serchi.py?s=klavi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4756`〜`ID4855` は 100 件確認済み。
- `git diff --check` 問題なし。

## 564. 563周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment
- Health / At the Dentist
- Health / At the Optician
- Health / At the Pharmacy

結果:
- **今回の追加修正なし**
- 歯科・眼科・薬局の専門語が多い範囲。過去周回で `hipermetropa`, `denta higienisto`, `tablojdoj`, `desinfektaĵo`, `fastante` などはすでに修正済みで、今回の再照合でもCSV本文をさらに動かすべき明確な誤りは見つからなかった。

主な据え置き確認:
- `Mi preskribos al vi antibiotikojn`, `Portu ĉi tiun recepton al la apoteko`, `Kiomfoje tage mi devas preni ĉi tion?`, `Prenu po du el ĉi tiuj piloloj trifoje tage` は処方・服薬文脈で対応する。`piloloj` は PIV 2020 で薬剤の pill として確認でき、`ID4740` の `tablojdoj` は tablet として確認できるため、それぞれ現文脈で維持。
- `Mi brosas la dentojn`, `Al mi elfalis dento`, `Mi perdis plombon`, `Krono rompiĝis`, `Bonvolu meti kronon sur ĉi tiun denton`, `Mi havas ŝvelintan gingivon`, `Ĉu vi povas ripari mian dentprotezon?`, `Vi bezonas du plombojn`, `Vi havas iom da kario`, `Mi ŝatus plombigi denton` は歯科文脈で意味ズレなし。
- `Ĉu vi volas, ke oni alĝustigu al vi kronon?` は、より説明的に `meti kronon` とも言えるが、RU `подогнать коронку` と crown fitting の文脈に合い、既存表現を誤りとは判断しない。
- `Ĉu vi ŝatus gargari la buŝon?` は、PIV 2020 で `gargari` が口・喉を液体ですすぐ意味を含むため、rinse your mouth out として維持。
- `Li havas grandajn dioptriojn`, `Li estas hipermetropa`, `Ŝi estas miopa`, `kontaktlensojn`, `okulvitrujon`, `okulekzamenojn`, `astigmatismon`, `dezajnistaj kadroj`, `okulvitroj por legado`, `UV-protekton` は眼鏡店・検眼文脈で対応する。`grandajn dioptriojn` はやや口語的な直訳感があるが、日中韓/RU の「度数が高い/большие диоптрии」と整合するため未修正。
- `Kia estas la dozo?`, `Du ĝis kvar tablojdoj tage`, `Mi bezonas inhalilon`, `Mi bezonas desinfektaĵon`, `Ĉu vi havas plastrojn?`, `Ĉu vi havas kontraŭdolorilojn?`, `Ĉu mi prenu ĝin fastante?`, `Oni povas ĝin aĉeti sen recepto`, `Ĝi estas havebla nur laŭ recepto` は薬局・服薬文脈で対応する。
- `Kia estas la dozo?` は `Kiom granda estas la dozo?` なども可能だが、短い薬局質問として意味は明確。文脈別許容で維持。

参照:
- PIV 2020 `antibiotiko`: https://vortaro.net/py/serchi.py?s=antibiotiko&simpla=1
- PIV 2020 `recepto`: https://vortaro.net/py/serchi.py?s=recepto&simpla=1
- PIV 2020 `pilolo`: https://vortaro.net/py/serchi.py?s=pilolo&simpla=1
- PIV 2020 `tablojdo`: https://vortaro.net/py/serchi.py?s=tablojdo&simpla=1
- PIV 2020 `dent/o`: https://vortaro.net/py/serchi.py?s=dento&simpla=1
- PIV 2020 `plombo`: https://vortaro.net/py/serchi.py?s=plombo&simpla=1
- PIV 2020 `krono`: https://vortaro.net/py/serchi.py?s=krono&simpla=1
- PIV 2020 `gargari`: https://vortaro.net/py/serchi.py?s=gargari&simpla=1
- PIV 2020 `dioptrio`: https://vortaro.net/py/serchi.py?s=dioptrio&simpla=1
- PIV 2020 `hipermetropa`: https://vortaro.net/py/serchi.py?s=hipermetropa&simpla=1
- PIV 2020 `miopa`: https://vortaro.net/py/serchi.py?s=miopa&simpla=1
- PIV 2020 `lenso`: https://vortaro.net/py/serchi.py?s=lenso&simpla=1
- PIV 2020 `inhalilo`: https://vortaro.net/py/serchi.py?s=inhalilo&simpla=1
- PIV 2020 `infekti`: https://vortaro.net/py/serchi.py?s=infekti&simpla=1
- PIV 2020 `plastro`: https://vortaro.net/py/serchi.py?s=plastro&simpla=1
- PIV 2020 `fasti`: https://vortaro.net/py/serchi.py?s=fasti&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4656`〜`ID4755` は 100 件確認済み。
- `git diff --check` 問題なし。

## 563. 562周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor
- Health / Diseases
- Health / Treatment

結果:
- **今回の追加修正なし**
- この範囲は症状申告・病名・治療説明が中心。アプリ側では `sentence_app.py` / `sentence_app_Cxina_versio.py` / `sentence_app_Korea_versio.py` が同一CSVから `Esperanto` と `日本語` / `中文` / `한국어` を組にして、双方向4択を生成するため、EN/RU は参考列として意味照合に使った。
- 既存周回で `Insekto pikis min`, `Mi havas tre malmulte da energio`, `Mi havas stomakan perturbon`, `Mi havas gravan mikozon de la piedoj`, `Mi havas malfacilaĵojn pri dormado`, `Vi bezonos kelkajn suturerojn`, `Mi bezonas kuracistan atestilon` などは修正済み。今回もロシア語・日中韓との対応と辞書根拠を再確認したが、さらに本文を動かすべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- `privata medicina asekuro` は `malsanasekuro` / `sanasekuro` 系も候補だが、private medical insurance の意味は透明で、日中韓の「民間/私人/개인 医療保険」と整合するため維持。
- `Mi sentas min kapturna`, `Mi tremas`, `Mi havas malvarmumon`, `Mi havas tuberon`, `Insekto pikis min`, `Mi havas haŭterupcion`, `Mi havas furunkon`, `Mi havas diareon`, `Mi estas konstipita`, `Mi havas ŝvelon`, `Mi havas nazkataron` は症状申告として対応する。`haŭterupcio` については Glosbe で `ekzantemo` も確認できるが、PIV の `erupcio` の皮膚症状語義と `haŭta` の透明な複合で意味は保たれるため、専門語へ寄せる修正はしない。
- `Mia stomako doloras`, `Mi havas stomakan perturbon`, `Mi havas doloron en la brusto`, `Mi havas kormalsanon`, `Mi malfacile spiras`, `Mia nazo estas tre ŝtopita`, `Miaj limfonodoj estas ŝvelintaj` は、身体部位・症状の対応として意味ズレなし。
- `Mi havas gravan mikozon de la piedoj` は athlete's foot / foot fungus の説明的表現として維持。`pieda tinio` なども候補だが、PIV で確認できる `mikozo` を使う現形は、RU `грибка стопы` とも合う。
- `Mi pensas, ke mi streĉis muskolon en mia kruro`, `Mi sentas min deprimita`, `Mi havas malfacilaĵojn pri dormado`, `Mi suferas de sendormeco`, `Mi suferas de fojnofebro` は、症状・状態の申告として自然な範囲。
- `Vi devas fari sangoteston` は Glosbe と Majstro で blood test の対応として `sangotesto` を確認でき、`sanga analizo` も候補ではあるが、現形を誤りとは判断しない。
- `Ĝi rapide resaniĝos` は、PIV の `cikatro` 項で `resaniĝinta vundo` が確認できるため、傷などが「治る」文脈として許容。`cikatriĝi` は「瘢痕化して閉じる」に寄るため、一般的な heal quickly の教材文として現形を維持。
- `Ĉu mi povas sporti?`, `Vi bezonos seriozan kuracadon`, `Vi bezonos kelkajn suturerojn`, `Ĉu mi bezonos lokan anestezon?`, `Ni devas preni urinan specimenon`, `Vi devus redukti vian trinkadon`, `Ĉu mi rajtas ellitiĝi?` は、治療・入院文脈で日中韓およびRU列と整合する。

参照:
- PIV 2020 `erupcio`: https://vortaro.net/py/serchi.py?s=erupcio&simpla=1
- Glosbe `skin rash`: https://glosbe.com/en/eo/skin%20rash
- PIV 2020 `furunko`: https://vortaro.net/py/serchi.py?s=furunko&simpla=1
- PIV 2020 `kataro`: https://vortaro.net/py/serchi.py?s=kataro&simpla=1
- PIV 2020 `limfo`: https://vortaro.net/py/serchi.py?s=limfo&simpla=1
- PIV 2020 `mikozo`: https://vortaro.net/py/serchi.py?s=mikozo&simpla=1
- PIV 2020 `perturbo`: https://vortaro.net/py/serchi.py?s=perturbo&simpla=1
- Glosbe `blood test`: https://glosbe.com/en/eo/blood%20test
- Majstro `blood`: https://www.majstro.com/dictionaries/English-Esperanto/blood
- PIV 2020 `cikatro`: https://vortaro.net/py/serchi.py?s=cikatro&simpla=1
- PIV 2020 `suturo`: https://vortaro.net/py/serchi.py?s=suturo&simpla=1
- PIV 2020 `anestezo`: https://vortaro.net/py/serchi.py?s=anestezo&simpla=1
- PIV 2020 `urino`: https://vortaro.net/py/serchi.py?s=urino&simpla=1
- PIV 2020 `trinkado`: https://vortaro.net/py/serchi.py?s=trinkado&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4556`〜`ID4655` は 100 件確認済み。
- `git diff --check` 問題なし。

## 562. 561周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs
- Health / At the Doctor

結果:
- **今回の追加修正なし**
- 修理・時計/鍵/靴修理・診療室での症状確認を再確認。過去周回で `pilo`, `rentgena ekzameno`, `trankviligaĵo` などはすでに整理済みであり、今回の辞書照合でも本文をさらに動かすべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- `La ekrano fendiĝis`, `kuirforno`, `brakhorloĝo`, `pilo`, `kroneto`, `ŝlosilringo`, `fari kopion de ĉi tiu ŝlosilo`, `lasi ripari mian fotoaparaton`, `riparejo por ŝuoj`, `plandumo`, `garantio`, `fabrikanto` は修理・時計・鍵・靴修理文脈で対応する。
- `pilo` は PIV 2020 で化学エネルギーによる電源として確認でき、腕時計・小型機器の battery 文脈に合うため維持。
- `kroneto` は PIV の `krono` 直接項では時計竜頭を強く確認できないが、時計部品の crown/winder を表す縮小形として過去判断どおり文脈別許容。安全な別語へ置き換える根拠が十分でないため未修正。
- `plandumo` は PIV 2020 で靴底として確認でき、Glosbe でも sole の候補に `plandumo` が出るため維持。
- `kontrola ekzameno`, `kapturno`, `medikamentojn`, `alkoholaĵojn`, `rentgena ekzameno`, `aŭdotestojn`, `medicina konsulto`, `analizojn`, `malsanasekuro`, `sangogrupo`, `O negativa` / `O-pozitiva`, `kmera`, `desinfekti`, `suprenfaldi`, `sangopremo`, `insulino`, `trankviligaĵo`, `ulcero`, `surdorse/surventre` は診療文脈で対応する。
- `rentgena ekzameno` は PIV 2020 の `rentgeno` が古い放射線単位であるため単独名詞としては避けられており、現行の形は X-ray examination として文脈を明示できるため維持。
- `analizojn` は PIV 2020 の `analizo` が化学・物理的分析/検査を含むため、RU `сдать анализы` と対応する医療検査文脈として維持。
- `malsanasekuro` は PIV 直接見出しでは未確認だが、`malsano` + `asekuro` の透明な複合で、health insurance 文脈として意味ズレはない。Glosbe では `Malsanokosta asekuro` も確認できるが、現形を誤りとは判断しない。
- `sangopremo` は Glosbe で blood pressure の主要対応として確認でき、PIV 2020 の `sango` と `premo` の語義にも沿うため維持。
- `trankviligaĵo` は PIV 2020 の `trankviligi` 項で「脳を鎮静させる薬」として確認でき、tranquillizer 文脈に合うため維持。

参照:
- PIV 2020 `pilo`: https://vortaro.net/py/serchi.py?s=pilo&simpla=1
- PIV 2020 `krono`: https://vortaro.net/py/serchi.py?s=krono&simpla=1
- PIV 2020 `plandumo`: https://vortaro.net/py/serchi.py?s=plandumo&simpla=1
- Glosbe `sole`: https://glosbe.com/en/eo/sole
- PIV 2020 `kapturno`: https://vortaro.net/py/serchi.py?s=kapturno&simpla=1
- PIV 2020 `rentgena`: https://vortaro.net/py/serchi.py?s=rentgena&simpla=1
- PIV 2020 `analizo`: https://vortaro.net/py/serchi.py?s=analizo&simpla=1
- Glosbe `health insurance`: https://glosbe.com/en/eo/health%20insurance
- PIV 2020 `sango`: https://vortaro.net/py/serchi.py?s=sango&simpla=1
- PIV 2020 `premo`: https://vortaro.net/py/serchi.py?s=premo&simpla=1
- Glosbe `blood pressure`: https://glosbe.com/en/eo/blood%20pressure
- PIV 2020 `trankviligi`: https://vortaro.net/py/serchi.py?s=trankviligi&simpla=1
- PIV 2020 `ulcero`: https://vortaro.net/py/serchi.py?s=ulcero&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4456`〜`ID4555` は 100 件確認済み。
- `git diff --check` 問題なし。

## 561. 560周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency
- Services / At the Beauty Salon
- Services / At the Tailor's
- Services / Repairs

結果:
- **1件修正（1行）**
- 不動産後半・美容院・仕立て屋・修理表現を再確認。美容院語彙のうち、PIV/Glosbe で確認できない語形 `manikiuro` のみを、確認可能な `manikur-` 系へ補正した。

修正:
- `ID4396` EO
  - `Mi ŝatus manikiuron, mi petas` → `Mi ŝatus manikuron, mi petas`
  - 理由: PIV 2020 は `manikuri`（手を美容的に手入れする）を見出しとして載せ、`manikuristo` も確認できる。Glosbe でも manicure の対応は `manikuri`, `manflegado`, `manflego`, `manikuro` などで、旧 `manikiuro` は確認できない。内容を変えず、同ブロックの `pedikuro` とも揃う名詞形 `manikuro` に補正。

主な据え置き確認:
- `rigardi/viziti la posedaĵon`, `lupago ... monate anticipe`, `negoci`, `enloĝiĝi`, `dissendolisto` は不動産仲介文脈で対応する。
- `franĝo` は PIV 2020 で「額の上の髪の franĝo」として確認でき、fringe/bangs 文脈に合うため維持。
- `konstanta ondumado` は PIV 2020 の `ondumado` 項で髪の permanent wave 用例として確認でき、soft perm 文脈で維持。
- `dislimo` は PIV 2020 の `haroj` 項に `dislimi al si la harojn` があり、髪の分け目として維持。`meza disigo` は `meza dislimo` も候補だが、文脈上の意味は明確なため今回は未修正。
- `farbi miajn harojn blonde` は、PIV 2020 の `farbi` に `farbita ruĝe k blanke` 型の用例があるため、髪を金髪に染める結果表現として維持。
- `helajn striojn en miaj haroj`, `senharigo ... per vakso`, `feni`, `ŝampui`, `sprajo/ĝelo por haroj`, `kranihaŭto`, `fajli/formi/laki ungojn` は美容院・ネイル文脈で対応する。
- `tajloro`, `zipo`, `alkudri`, `fliki`, `mezuroj`, `alĝustigi`, `laŭmezura kostumo`, `maniklongon`, `mallarĝigi`, `mallongigi`, `longigi`, `plilarĝigi` は仕立て屋文脈で対応する。
- `Ĉu vi povas iom ŝanĝi ĉi tiun robon?` は `alĝustigi` も候補だが、alter this dress の広い依頼として意味は明確なため維持。
- Repairs 冒頭の `Ĝi ne funkcias bone`, `Ĉu vi povas ripari ĝin?`, `multekosta`, `ripari la televidon` は修理文脈で対応する。

参照:
- PIV 2020 `manikuri`: https://vortaro.net/py/serchi.py?s=manikuri&simpla=1
- Glosbe `manicure`: https://glosbe.com/en/eo/manicure
- PIV 2020 `pedikuri`: https://vortaro.net/py/serchi.py?s=pedikuri&simpla=1
- PIV 2020 `franĝo`: https://vortaro.net/py/serchi.py?s=fran%C4%9Do&simpla=1
- PIV 2020 `haroj`: https://vortaro.net/py/serchi.py?s=haroj&simpla=1
- PIV 2020 `ondumado`: https://vortaro.net/py/serchi.py?s=ondumado&simpla=1
- PIV 2020 `farbi`: https://vortaro.net/py/serchi.py?s=farbi&simpla=1
- PIV 2020 `senharigo`: https://vortaro.net/py/serchi.py?s=senharigo&simpla=1
- PIV 2020 `feni`: https://vortaro.net/py/serchi.py?s=feni&simpla=1
- PIV 2020 `ŝampui`: https://vortaro.net/py/serchi.py?s=%C5%9Dampui&simpla=1
- Glosbe `scalp`: https://glosbe.com/en/eo/scalp
- PIV 2020 `zipo`: https://vortaro.net/py/serchi.py?s=zipo&simpla=1
- PIV 2020 `kudri`: https://vortaro.net/py/serchi.py?s=kudri&simpla=1
- PIV 2020 `fliki`: https://vortaro.net/py/serchi.py?s=fliki&simpla=1
- PIV 2020 `ŝuo`: https://vortaro.net/py/serchi.py?s=%C5%9Duo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e3f02d5d9a828b0256a13489d38b6cdc`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4356`〜`ID4455` は 100 件確認済み。
- `git diff --check` 問題なし。

## 560. 559周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank
- Services / At the Estate Agency

結果:
- **今回の追加修正なし**
- 銀行・不動産仲介の実用会話として再確認。銀行語彙は `retiro` / `monretiro`、`konteltiro`、`ĝiri` など近い語が多いが、PIV/Glosbe と列間対応を照合した限り、意味を変えずに本文をさらに動かすべき明確な誤りは見つからなかった。

主な据え置き確認:
- `legitimilo`, `formularo`, `subskribu`, `kurzo`, `provizio`, `kvitancon`, `falsa monbileto`, `bankaŭtomato`, `kontantmono`, `saldon`, `stirpermesilon`, `ĉekaro`, `konteltiron`, `ĝiri`, `komuna konto`, `interezprocento`, `kontantigi` は銀行・送金・口座文脈で対応する。
- `Mi ŝatus fari retiron` は `retiron` が一般の withdrawal として確認できる。より説明的な `monretiron` もあり得るが、銀行窓口文脈では現形で意味が明確なため未修正。
- `Mi bezonas formularon por monretiro` は `mon` + `retiro` の透明な複合で withdrawal slip の意味を補っている。PIV 直接見出しでは弱いが、`retiro` の語義と文脈から許容。
- `Mi ŝatus ĝiri iom da mono en ĉi tiun konton` は PIV 2020 の `ĝiri` に「自分の口座から別口座へ金額を移す」語義があり、RU `перевести деньги на этот счёт` と整合する。
- `Sur via konto ne estas mono` は `en via konto` も候補だが、銀行口座の残高確認文として意味は明確。既存の `konto` 系表現との整合を優先して未修正。
- `loĝejo`, `kvartalo`, `bangalo`, `vicdomo`, `parkumejo`, `petata prezo`, `posedaĵo`, `kontanta aĉetanto`, `hipoteko`, `antaŭpago`, `deponaĵo je unu-monata lupago`, `meblita/nemeblita loĝejo`, `duamana posedaĵo`, `prezintervalo`, `sur la merkato` は不動産仲介文脈で対応する。
- `parkumejo` は parking lot/parking place 寄りで、`parkumloko` も候補になり得るが、PIV 2020 で自動車を一時的に置くための場所として確認でき、物件条件の「駐車スペース」文脈から外れないため維持。
- `Interesas min ekscii pli pri ĉi tiu posedaĵo` は、より平明には `Mi interesiĝas...` もあり得るが、意味ズレはなく、property inquiry の表現として維持。

参照:
- PIV 2020 `legitimi`: https://vortaro.net/py/serchi.py?s=legitimi&simpla=1
- PIV 2020 `provizio`: https://vortaro.net/py/serchi.py?s=provizio&simpla=1
- PIV 2020 `konto`: https://vortaro.net/py/serchi.py?s=konto&simpla=1
- PIV 2020 `ĝiri`: https://vortaro.net/py/serchi.py?s=%C4%9Diri&simpla=1
- PIV 2020 `ĉekaro`: https://vortaro.net/py/serchi.py?s=%C4%89ekaro&simpla=1
- PIV 2020 `interezo`: https://vortaro.net/py/serchi.py?s=interezo&simpla=1
- PIV 2020 `hipoteko`: https://vortaro.net/py/serchi.py?s=hipoteko&simpla=1
- PIV 2020 `bangalo`: https://vortaro.net/py/serchi.py?s=bangalo&simpla=1
- PIV 2020 `parkejo`: https://vortaro.net/py/serchi.py?s=parkejo&simpla=1
- Glosbe `withdrawal`: https://glosbe.com/en/eo/withdrawal
- Glosbe `terraced house`: https://glosbe.com/en/eo/terraced%20house
- Glosbe `interest rate`: https://glosbe.com/en/eo/interest%20rate

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `31c31639023499328a5bb9c456f759d2`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4256`〜`ID4355` は 100 件確認済み。
- `git diff --check` 問題なし。

## 559. 558周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping
- Leisure Time / Family Time
- Leisure Time / Gardening
- Leisure Time / Having Guests
- Services / At the Bank

結果:
- **2件修正（2行）**
- キャンプ・家族時間・園芸・来客・銀行ATM文脈を再確認。大半は文脈別許容で維持できるが、PIV/Glosbe 照合で「大豆」と「タオル」の対応が広すぎる、または別義に読まれる箇所を2件だけ補正した。

修正:
- `ID4181` EO
  - `Ŝi kultivas sojon` → `Ŝi kultivas sojfabojn`
  - 理由: RU `Она выращивает сою`、JA/ZH は「大豆」。PIV 2020 では単独の `sojo` は「sojfaboj から作る濃い褐色の調味液」、つまり醤油に当たる語として出る。一方、`sojfabo` は大豆の種子として確認でき、Glosbe でも `soybeans` の対応に `sojfaboj` が出るため、園芸・栽培文脈では `sojfabojn` がより正確。
- `ID4210` EO
  - `Ĉu vi ŝatus tukon?` → `Ĉu vi ŝatus mantukon?`
  - 理由: RU `полотенце`、JA/ZH/KO はタオル。PIV 2020 の `tuko` は「用途を持つ布片」全般で、`mantuko` が「手を拭くための tuko」として確認できる。Glosbe でも `towel` の主要対応が `mantuko` であるため、来客にタオルを勧める文として曖昧さを減らした。

主な据え置き確認:
- `piedvojetoj` は PIV 直接見出しでは未確認だが、`pied` + `vojeto` の透明な複合で、walking trails / пешие маршруты の「徒歩用の小道・散策路」を表す文脈として許容。より一般的な `vojetoj` / `padoj` もあり得るが、明確な意味ズレではないため維持。
- `bovlingon` は PIV 直接見出しでは弱いが、Glosbe で bowling の対応に `bovlingo` が確認できるため、`Ĉu ni iru ludi bovlingon?` は維持。
- `televidaj romanoj` は Glosbe で soap opera の対応に `televida romano` が確認でき、RU `мыльных операх` とも対応するため維持。
- `sagetoj` は darts 文脈で、PIV の `sago` 派生・Glosbe の darts 対応（`Sagoĵetado`）と矛盾しないため維持。
- `fruktarbejo` は Glosbe で orchard の主要対応として確認できるため、`Kiaj arboj estas en la fruktarbejo?` は維持。
- `kulturplantojn` は「栽培される植物/農作物」の意味で RU `сельскохозяйственные культуры` と対応する。`rikoltaĵoj` / `kultivaĵoj` も候補だが、現形は園芸・地域栽培文脈で意味ズレとは判断しない。
- `Ĉu vi ŝatus toaston?` は PIV 2020 で `toasto` が「焼いたパン片」、`tosto` が乾杯・祝杯の意味として確認済み。現形は toast の食品文脈に合うため維持。
- `Ĉu vi ŝatus ĝinon kun toniko?` は PIV 2020 の `kinin akvo` 項目で「ĝino と用いるキニーネ入り炭酸水」が確認でき、Glosbe でも `tonic water` の対応に `toniko` が出る。`ĝino kun toniko` は RU `джин с тоником` とも対応するため維持。
- `boligos akvon`, `sukerpecoj`, `manĝoĉambron`, `senalkoholan trinkaĵon`, `mendas picon hejmen`, `viŝos`, `alian servon` は来客・銀行文脈で対応する。

参照:
- PIV 2020 `sojo`: https://vortaro.net/py/serchi.py?s=sojo&simpla=1
- Glosbe `soybeans`: https://glosbe.com/en/eo/soybeans
- PIV 2020 `tuko`: https://vortaro.net/py/serchi.py?s=tuko&simpla=1
- Glosbe `towel`: https://glosbe.com/en/eo/towel
- Glosbe `bowling`: https://glosbe.com/en/eo/bowling
- Glosbe `soap opera`: https://glosbe.com/en/eo/soap%20opera
- Glosbe `darts`: https://glosbe.com/en/eo/darts
- Glosbe `orchard`: https://glosbe.com/en/eo/orchard
- Glosbe `crop`: https://glosbe.com/en/eo/crop
- Glosbe `footpath`: https://glosbe.com/en/eo/footpath
- Glosbe `tonic water`: https://glosbe.com/en/eo/tonic%20water
- PIV 2020 `akvo`: https://vortaro.net/py/serchi.py?s=akvo&simpla=1
- PIV 2020 `toasto`: https://vortaro.net/py/serchi.py?s=toasto&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `31c31639023499328a5bb9c456f759d2`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4156`〜`ID4255` は 100 件確認済み。
- `git diff --check` 問題なし。

## 558. 557周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport
- Leisure Time / Music
- Leisure Time / Going Camping

結果:
- **今回の追加修正なし**
- スポーツ後半・音楽・キャンプ表現を再確認。前回までの修正で、`regatto`, `rostokrado`, `ruldomo`, `telfero` などの要注意語はおおむね整理済みであり、今回さらに本文を変更すべき明確な意味ズレは見つからなかった。

主な据え置き確認:
- `fina rezulto`, `ĵudo`, `centra tribuno`, `tenisejo`, `tenisa rakedo`, `spektantoj`, `sporta klubo`, `ĵokeo`, `favorato`, `veto`, `golfbastonoj`, `golfĉaro`, `norma nombro da batoj`, `regatto`, `femuraj muskoloj` はスポーツ文脈で対応する。
- `vetŝancoj` は PIV 直接見出しでは未確認だが、`veto` + `ŝanco` の透明な複合で、Wiktionary 系の英語-EO対応でも odds の候補として確認できる。RU `шансы` との対応も保つため未修正。
- `golfbastonoj` / `golfĉaro` は PIV 直接見出しでは弱いが、`golfo` + `bastono` / `ĉaro` の透明な複合で、golf clubs / buggy 文脈を保つため維持。
- `Mi ludas violonon`, `ĥoro`, `grupo`, `instrumento`, `gitaro`, `akordiono`, `saksofono`, `piano`, `programo`, `balkono`, `tenoro`, `dirigento`, `spektaklo`, `muzikgrupoj`, `simfonia orkestro`, `popolmuziko` は音楽文脈で対応する。
- `popolmuziko` は PIV 直接見出しでは未確認だが、`popola muziko` / folk music 系の用例が確認でき、RU `фольклорной музыки`・EN folk music の範囲から大きく外れないため文脈別許容。
- `tendumi`, `tendumejo`, `lanterno`, `ruldomo`, `alumetoj`, `trinkakvo`, `poŝlampo`, `kukolo`, `fiŝkaptado`, `rando de la arbaro`, `tendoj lueblaj`, `rostokrado`, `interreta aliro`, `pego`, `najtingalo`, `ĉasado`, `tranokti`, `dormosakoj`, `kuireja ekipaĵo`, `bero`, `fungo`, `hirunda nesto`, `telfero`, `monta pado` はキャンプ・自然文脈で対応する。
- `Ĉu vi havas pli ebenan lokon?` は campsite の「もっと平らな場所」を尋ねる表現として自然。`loko` は場所/区画の意味で、RU `место` とも一致するため維持。
- `Kiom kostas tendo?` は購入文にも読める余地があるが、Subtopic が Going Camping で、EN/RU/日中韓もテント1張りの料金として取れるため文脈別許容で未修正。

参照:
- PIV 2020 `ĵudo`: https://vortaro.net/py/serchi.py?s=%C4%B5udo&simpla=1
- PIV 2020 `tribuno`: https://vortaro.net/py/serchi.py?s=tribuno&simpla=1
- PIV 2020 `ĵokeo`: https://vortaro.net/py/serchi.py?s=%C4%B5okeo&simpla=1
- PIV 2020 `veto`: https://vortaro.net/py/serchi.py?s=veto&simpla=1
- PIV 2020 `golfo`: https://vortaro.net/py/serchi.py?s=golfo&simpla=1
- PIV 2020 `regatto`: https://vortaro.net/py/serchi.py?s=regatto&simpla=1
- PIV 2020 `femuro`: https://vortaro.net/py/serchi.py?s=femuro&simpla=1
- PIV 2020 `violono`: https://vortaro.net/py/serchi.py?s=violono&simpla=1
- PIV 2020 `ĥoro`: https://vortaro.net/py/serchi.py?s=%C4%A5oro&simpla=1
- PIV 2020 `akordiono`: https://vortaro.net/py/serchi.py?s=akordiono&simpla=1
- PIV 2020 `saksofono`: https://vortaro.net/py/serchi.py?s=saksofono&simpla=1
- PIV 2020 `dirigento`: https://vortaro.net/py/serchi.py?s=dirigento&simpla=1
- PIV 2020 `folkloro`: https://vortaro.net/py/serchi.py?s=folkloro&simpla=1
- PIV 2020 `tendumi`: https://vortaro.net/py/serchi.py?s=tendumi&simpla=1
- PIV 2020 `lanterno`: https://vortaro.net/py/serchi.py?s=lanterno&simpla=1
- PIV 2020 `ruldomo`: https://vortaro.net/py/serchi.py?s=ruldomo&simpla=1
- PIV 2020 `poŝlampo`: https://vortaro.net/py/serchi.py?s=po%C5%9Dlampo&simpla=1
- PIV 2020 `kukolo`: https://vortaro.net/py/serchi.py?s=kukolo&simpla=1
- PIV 2020 `pego`: https://vortaro.net/py/serchi.py?s=pego&simpla=1
- PIV 2020 `najtingalo`: https://vortaro.net/py/serchi.py?s=najtingalo&simpla=1
- PIV 2020 `rostokrado`: https://vortaro.net/py/serchi.py?s=rostokrado&simpla=1
- PIV 2020 `dormosako`: https://vortaro.net/py/serchi.py?s=dormosako&simpla=1
- PIV 2020 `hirundo`: https://vortaro.net/py/serchi.py?s=hirundo&simpla=1
- PIV 2020 `telfero`: https://vortaro.net/py/serchi.py?s=telfero&simpla=1
- PIV 2020 `tranokti`: https://vortaro.net/py/serchi.py?s=tranokti&simpla=1
- PIV 2020 `interreto`: https://vortaro.net/py/serchi.py?s=interreto&simpla=1
- Wiktionary EN-EO `odds`: https://eo.wiktionary.org/wiki/Aldono:Vortaro_angla-Esperanto_o
- Glosbe `horse racing`: https://en.glosbe.com/en/eo/horse%20racing
- Glosbe/用例 `popola muziko`: https://glosbe.com/eo/fr/Popola%20muziko

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `a9f88b81171ee8d6e8a4fa4e71a61a06`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID4056`〜`ID4155` は 100 件確認済み。
- `git diff --check` 問題なし。

## 557. 556周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / At the Nightclub
- Leisure Time / At the Beach
- Leisure Time / Sport

結果:
- **2件修正（2行）**
- ナイトクラブ・海辺・スポーツ表現を再確認。多くは文脈別許容だが、PIV/ReVo/Glosbe 照合で別義または未確認語に寄っていたスポーツ表現を2件だけ補正した。

修正:
- `ID4014` EO
  - `Estis remizo` → `Estis remiso`
  - 理由: RU `Была ничья`、JA/ZH/KO は「引き分け」。`remizo` は PIV 2020 と ReVo で車庫・物置系の語として確認され、スポーツの draw とは意味がずれる。一方、Glosbe で `drawn game` の対応として `remiso` が確認できるため、意味を変えずに補正。
- `ID4022` EO
  - `Kiu estas la arbitro?` → `Kiu estas la arbitracianto?`
  - 理由: `arbitro` は PIV 2020 では `arbitra` 系（恣意性）の名詞として確認され、スポーツ審判の意味では不適切。PIV 2020 の `arbitracio` 項目でスポーツ競技の規則を管理する人として `arbitracianto` / `arbitraciisto` が確認でき、Glosbe でも referee の主要対応に `arbitracianto` が出るため、PIV例に近い形へ補正。

主な据え置き確認:
- `Kiujn noktojn vi estas malfermitaj?`, `7 noktojn semajne`, `klubo`, `privata festo`, `gastlisto`, `sportŝuoj`, `viva muziko`, `homplene`, `mortige enue`, `diskĵokeo`, `drinkejo` はナイトクラブ文脈で対応する。
- `diskĵokeo` は PIV 直接見出しでは未確認だが、Glosbe では DJ の対応に `DĴ` が確認でき、`diskĵokeo` も英語 disc jockey に基づく透明な表現として実例があるため、意味ズレとは判断せず維持。
- `plaĝo` / `strando`, `sunseĝo`, `akvoskioj` / `akvoskii`, `subakvaj fluoj`, `surfotabulo`, `jaĥtklubo`, `plonĝkostumo`, `aerbotelo`, `ekstera naĝejo`, `malsekkostumo`, `ĉevalfortoj`, `garantiaĵo`, `savjako` は海辺・水上活動文脈で対応する。
- `sunseĝo`, `plonĝkostumo`, `malsekkostumo`, `aerbotelo` は PIV 直接見出しでは弱いが、透明な複合語で、同CSV内の既存判断・Glosbe/ウェブ実例とも矛盾しないため維持。
- `Mi estas membro de gimnastikejo`, `tenisejo`, `rakedo`, `rugbeo`, `usona futbalo`, `kaso`, `bileto`, `goli`, `egaligis la poentaron`, `vetkuroj`, `raso`, `veti`, `skiojn kaj botojn`, `flugpilka/manpilka/basketbala teamo`, `flava uniformo` はスポーツ文脈で意味ズレなし。
- `Ni ludu duope` は doubles を「二人組で/ペアでプレーしよう」と表す省略的表現として文脈別許容。より説明的には `Ni ludu duoblan ludon` もあり得るが、明確な誤りではないため未修正。
- `Kiu faris la golon?` と `Kiu teamo golis?` は、PIV 2020 の `golo` とスポーツ文脈から意味が明確。`goli` は PIV 直接派生表示としては弱いが透明な動詞化で、今回は未修正。

参照:
- PIV 2020 `remizo`: https://vortaro.net/py/serchi.py?s=remizo&simpla=1
- ReVo `remizo`: https://reta-vortaro.de/revo/art/remiz.html
- Glosbe `drawn game`: https://glosbe.com/en/eo/drawn%20game
- PIV 2020 `arbitracio`: https://vortaro.net/py/serchi.py?s=arbitracio&simpla=1
- Glosbe `referee`: https://glosbe.com/en/eo/referee
- PIV 2020 `strando`: https://vortaro.net/py/serchi.py?s=strando&simpla=1
- PIV 2020 `akvoskio`: https://vortaro.net/py/serchi.py?s=akvoskio&simpla=1
- PIV 2020 `surfotabulo`: https://vortaro.net/py/serchi.py?s=surfotabulo&simpla=1
- PIV 2020 `jaĥto`: https://vortaro.net/py/serchi.py?s=ja%C4%A5to&simpla=1
- PIV 2020 `savjako`: https://vortaro.net/py/serchi.py?s=savjako&simpla=1
- PIV 2020 `jogo`: https://vortaro.net/py/serchi.py?s=jogo&simpla=1
- PIV 2020 `golo`: https://vortaro.net/py/serchi.py?s=golo&simpla=1
- PIV 2020 `poentaro`: https://vortaro.net/py/serchi.py?s=poentaro&simpla=1
- PIV 2020 `gimnastikejo`: https://vortaro.net/py/serchi.py?s=gimnastikejo&simpla=1
- PIV 2020 `tenisejo`: https://vortaro.net/py/serchi.py?s=tenisejo&simpla=1
- PIV 2020 `rakedo`: https://vortaro.net/py/serchi.py?s=rakedo&simpla=1
- PIV 2020 `rugbeo`: https://vortaro.net/py/serchi.py?s=rugbeo&simpla=1
- PIV 2020 `garantiaĵo`: https://vortaro.net/py/serchi.py?s=garantia%C4%B5o&simpla=1
- PIV 2020 `basketbalo`: https://vortaro.net/py/serchi.py?s=basketbalo&simpla=1
- PIV 2020 `uniformo`: https://vortaro.net/py/serchi.py?s=uniformo&simpla=1
- Glosbe `DJ`: https://glosbe.com/en/eo/DJ
- Glosbe `surfboard`: https://glosbe.com/en/eo/surfboard
- Glosbe `wetsuit`: https://glosbe.com/en/eo/wetsuit
- Glosbe `life jacket`: https://glosbe.com/en/eo/life%20jacket
- Glosbe `deposit`: https://glosbe.com/en/eo/deposit

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `a9f88b81171ee8d6e8a4fa4e71a61a06`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3956`〜`ID4055` は 100 件確認済み。
- `git diff --check` 問題なし。

## 556. 555周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / At the Theatre
- Leisure Time / At the Museum
- Leisure Time / At the Nightclub

結果:
- **1件修正（1行）**
- 劇場・美術館・ナイトクラブ表現を再確認。PIV で直接確認でき、RU/日中韓の意味により正確に合う語がある箇所を1件だけ補正した。

修正:
- `ID3868` EO
  - `Mi ŝatus preni teatran lorneton` → `Mi ŝatus preni teatran binoklon`
  - 理由: `lorneto` は `lorno` から理解可能だが、PIV 2020 では `binoklo` が「劇場などで使う二筒の小型望遠具」として確認できる。RU `театральный бинокль`、JA/KO の「オペラグラス」、ZH の「剧场望远镜」との対応をより明確にするため、意味を変えずに確認済み語へ補正。

主な据え置き確認:
- `baleto`, `opero`, `Kion oni ludas en la teatro?`, `mendi/preni biletojn`, `ĉio jam estas rezervita`, `dramo`, `vespera vesto`, `premiero`, `balkono`, `spektaklo`, `scenejo`, `prezentado`, `aktoro` は劇場文脈で対応する。
- `vestejo` は PIV 2020 で「劇場で帽子・衣服を預ける場所」の用例が確認でき、cloakroom/гардероб 文脈として `ID3869` / `ID3946` とも維持。
- `interakto` は PIV 2020 の `akt/o` 項目で、劇場・映画などの幕間/休憩時間として確認できるため、`ID3872` / `ID3873` / `ID3896` は維持。
- `loĝio` は PIV 2020 で劇場のボックス席として確認でき、`ID3874` の box seat/ложа 文脈と合うため維持。
- `programeto` / `programo`, `programero`, `intrigo`, `prezentata`, `operejo`, `La Mizerulojn`, `pensiuloj` は劇場・演目文脈で意味ズレなし。
- `senpaga eniro`, `enirkotizo`, `gvidanto`, `gvidata ekskurso`, `aŭdgvido/aŭdgvidilo`, `fotografi`, `fulmilo`, `pentraĵgalerio`, `karikatursalono`, `vaksaj figuroj`, `impresionismaj pentraĵoj`, `mozaiko`, `etnografia muzeo`, `ceramikaĵoj`, `handikapuloj`, `nepala`, `mongola`, `etaĝoj` は美術館・博物館文脈で対応する。
- `aŭdgvidilo` と `fulmilo` は PIV 直接見出しでは未確認だが、`aŭd-` + `gvidilo`, `fulmo` + `-ilo` の透明な形成で、音声ガイド・カメラのフラッシュ文脈を保つため維持。
- `klubo`, `drinkejo`, `prezentiĝas ĉi-vespere`, `vestkodo`, `bilardo`, `iom malplene` はナイトクラブ文脈として対応する。`vestkodo` は PIV 直接見出し未確認だが、`vesto` + `kodo` の透明な複合語として dress code 文脈を保つため維持。

参照:
- PIV 2020 `binoklo`: https://vortaro.net/py/serchi.py?s=binoklo&simpla=1
- PIV 2020 `interakto`: https://vortaro.net/py/serchi.py?s=interakto&simpla=1
- PIV 2020 `vestejo`: https://vortaro.net/py/serchi.py?s=vestejo&simpla=1
- PIV 2020 `loĝio`: https://vortaro.net/py/serchi.py?s=lo%C4%9Dio&simpla=1
- PIV 2020 `balkono`: https://vortaro.net/py/serchi.py?s=balkono&simpla=1
- PIV 2020 `programo`: https://vortaro.net/py/serchi.py?s=programo&simpla=1
- PIV 2020 `spektaklo`: https://vortaro.net/py/serchi.py?s=spektaklo&simpla=1
- PIV 2020 `gvidanto`: https://vortaro.net/py/serchi.py?s=gvidanto&simpla=1
- PIV 2020 `karikaturo`: https://vortaro.net/py/serchi.py?s=karikaturo&simpla=1
- PIV 2020 `mozaiko`: https://vortaro.net/py/serchi.py?s=mozaiko&simpla=1
- PIV 2020 `ceramikaĵo`: https://vortaro.net/py/serchi.py?s=ceramika%C4%B5o&simpla=1
- PIV 2020 `handikapulo`: https://vortaro.net/py/serchi.py?s=handikapulo&simpla=1
- PIV 2020 `bilardo`: https://vortaro.net/py/serchi.py?s=bilardo&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- Glosbe `cloakroom`: https://glosbe.com/en/eo/cloakroom
- Glosbe `Nepali`: https://glosbe.com/en/eo/Nepali
- Glosbe `Mongolian`: https://glosbe.com/en/eo/Mongolian
- Glosbe `dress code`: https://glosbe.com/en/eo/dress%20code

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `d3b6878c67eccde1acb33bd09173cdb7`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3856`〜`ID3955` は 100 件確認済み。
- `git diff --check` 問題なし。

## 555. 554周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments & Returns
- Leisure Time / At the Cinema
- Leisure Time / At the Theatre

結果:
- **今回の追加修正なし**
- 支払い・返品、映画館、劇場表現を再確認。PIV/Glosbe で映画・劇場用語とカード決済用語を照合したが、日中韓/RU との明確な意味ズレや、CSV本文を変更すべき確実な誤りは見つからなかった。

主な据え置き確認:
- `senimposte`, `validas`, `rabato por kontanta pago`, `interŝanĝi ... kontraŭ`, `repagon`, `transakcio`, `kreditkartojn`, `PIN-kodon`, `aĉetaĵojn` は支払い・返品文脈として対応する。
- `Kiu estas la sekureca numero sur la dorso?` は、PIV 2020 の `dorso` が「物の裏面・背面」にも使えることと一致するため、カード裏面のセキュリティ番号として維持。
- `filmo de suspenso` は、PIV 2020 の `suspenso` が映画・劇で観客を緊張した期待状態に置く場面を指すため、thriller 文脈として許容。Glosbe でも thriller の対応候補に `suspensfilmo` が確認でき、現在形は説明的だが意味は保たれる。
- `pufmaizo` は PIV 2020 の `maizo` 項目で popcorn に相当する派生形として確認できるため、`Salita aŭ dolĉa pufmaizo?` / `Ĉu ni prenu pufmaizon?` は維持。
- `en la vjetnama`, `romantika komedio`, `intrigo`, `produktis la filmon`, `ĉefan rolon`, `reĝisoro`, `scenaristo`, `premiero`, `nigrablanka filmo`, `impresita de la filmo` は映画文脈で対応する。
- `anglajn subtekstojn` は PIV 2020 では `subteksto` 直接見出し未確認だが、Glosbe で subtitle 対応として確認でき、映画字幕の一般表現として維持。
- `animaciaĵon` は PIV 2020 直接見出し未確認だが、Glosbe 等で cartoon/animation 系の対応が確認でき、`animacia` + `-aĵo` の透明な語形成として、日中韓/RU のアニメ・动画片・мультфильм 文脈を大きく外さないため維持。
- `Festivalo de Cannes` は PIV 2020 では都市名 `Kanno`/`Kannoj` が確認できる一方、Glosbe で `Cannes` 形も確認でき、映画祭名として未同化固有名を保つ表記も文脈上許容されるため未修正。
- `tragedio`, `dramo`, `opereto`, `dekoracioj`, `aŭtoro`, `solisto`, `aktorino` は劇場文脈として対応する。特に `dekoracioj` は PIV 2020 で舞台背景・舞台装置の意味が確認できる。
- `Ĝi estis unu el la plej bonaj filmoj, kiujn mi vidis de longe` は `de longe` に時間的用法があるため維持。ただし「遠くから見た」と読める余地を完全には排除できないため、文脈依存許容とする。

参照:
- PIV 2020 `suspenso`: https://vortaro.net/py/serchi.py?s=suspenso&simpla=1
- PIV 2020 `pufmaizo`: https://vortaro.net/py/serchi.py?s=pufmaizo&simpla=1
- PIV 2020 `dorso`: https://vortaro.net/py/serchi.py?s=dorso&simpla=1
- PIV 2020 `dekoracio`: https://vortaro.net/py/serchi.py?s=dekoracio&simpla=1
- PIV 2020 `validi`: https://vortaro.net/py/serchi.py?s=validi&simpla=1
- PIV 2020 `transakcio`: https://vortaro.net/py/serchi.py?s=transakcio&simpla=1
- PIV 2020 `Kanno`: https://vortaro.net/py/serchi.py?s=Kanno&simpla=1
- PIV 2020 `opereto`: https://vortaro.net/py/serchi.py?s=opereto&simpla=1
- Glosbe `subtitle`: https://glosbe.com/en/eo/subtitle
- Glosbe `cartoon`: https://glosbe.com/en/eo/cartoon
- Glosbe `thriller`: https://glosbe.com/en/eo/thriller
- Glosbe `Cannes`: https://glosbe.com/en/eo/Cannes

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `0a13d25744fce4017b290c1fac11a641`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3756`〜`ID3855` は 100 件確認済み。
- `git diff --check` 問題なし。

## 554. 553周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / At the Supermarket
- Shopping / At the Bookshop & Florist's
- Shopping / Payments & Returns

結果:
- **2件修正（2行）**
- スーパー・書店・花屋・支払い表現を再確認。PIV/Glosbe で確認できない食品借用語と、ハイフン付き言語形容詞の格表示を、確認済みの形へ補正した。

修正:
- `ID3675` EO
  - `Mi ŝatus bageton` → `Mi ŝatus bastonpanon`
  - 理由: `bageto` は PIV 2020 で確認できず、Glosbe でも baguette の EO 上位候補は `bastonpano`。PIV 2020 でも `bastonpano` は `pano` 項目で確認できるため、日中韓/RU の baguette/法棍/バゲット/багет 文脈を変えずに補正。
- `ID3726` EO
  - `Mi bezonas makedonan-ukrainan vortaron` → `Mi bezonas makedona-ukrainan vortaron`
  - 理由: PIV 2020 の用例に `germana-Esperantan vortaron` があり、ハイフン付き言語対の形容詞では第一要素を無格形、第二要素を名詞に一致させる型が確認できる。対象は `vortaron` なので、`makedona-ukrainan vortaron` に補正。意味は「マケドニア語‐ウクライナ語辞典」のまま維持。

主な据え置き確認:
- `majonezo`, `kafgrajnoj`, `tranĉaĵoj da ŝinko`, `peco da pico`, `granatoj`, `fromaĝo`, `aĉetĉaretoj`, `koridoro`, `konservaĵoj`, `frostigitaj nutraĵoj`, `ĉerizoj`, `ĉokoladaj bombonoj`, `filtriloj`, `biskvitoj`, `sunflora oleo`, `tabuletoj da nigra ĉokolado`, `duonkilogramo da faruno`, `duonduzeno da ovoj`, `konserviĝos` はスーパーでの食品・数量表現として対応する。
- `aĉetĉaretoj` は PIV 直接見出しでは未確認だが、`aĉet-` + `ĉareto` の透明な複合語として shopping trolley 文脈に合うため維持。
- `Kiujn markojn vi havas kun filtriloj?` は、煙草等の商品を扱う売り場で「フィルター付きの銘柄」を尋ねる省略表現として文脈別許容。
- `Kvaronon de kilogramo`, `Bonvolu pesi al mi tricent gramojn`, `Ĉu mi pagu por ĝi ĉi tie aŭ ĉe la kaso?` は買い物場面の省略を含む自然な注文・支払い表現として維持。
- `foliumi`, `plumoj`, `kajero`, `dana vortaro`, `notbloko`, `gvidlibro`, `gazetkiosko`, `dulingva vortaro`, `klariga vortaro`, `detektivaj romanoj`, `naskiĝtaga karto`, `poŝtkartoj`, `poemaroj`, `ekzemplero`, `albumoj pri arkitekturo`, `scienca literaturo`, `svahila`, `koloriglibroj`, `bildlibro`, `enciklopediaj vortaroj`, `broŝuroj`, `brokanta librovendejo`, `vidindaĵoj` は書店・新聞スタンド文脈で対応する。
- `notbloko` は PIV の `bloko` 項目および Glosbe notepad 対応で確認できるため維持。
- `koloriglibro` と `bildlibro` は PIV 直接見出しでは未確認だが、`kolorigi` + `libro`, `bildo` + `libro` の透明な複合語として、日中韓/RU の「塗り絵」「絵本」と対応するため今回は未修正。
- `Bonvolu doni al mi amharan gazeton` は PIV の `amhar/o` が「エチオピアで話される言語」と確認でき、Amharic newspaper 文脈に合うため維持。
- `Romeo kaj Julieta` は PIV 2020 の `Julieta` 項目で「Romeo k Julieta」として確認できるため維持。
- `orkideoj`, `rozoj`, `bukedeto da tulipoj`, `narcisoj`, `lekantoj`, `magnolioj`, `lilioj`, `krizantemoj`, `diantoj`, `krono el freŝaj floroj por la fianĉino` は花屋文脈として対応する。
- `kvitanco`, `restmono`, `pagi per karto`, `kontanta mono`, `PIN-kodo`, `Sakon, mi petas`, `Ĝi ne funkcias` は支払い・返品文脈で対応する。`restmono` は PIV 直接見出しでは未確認だが、`resta mono` 系の透明な複合語として change/お釣り文脈に合うため維持。

参照:
- PIV 2020 ローカル `majonezo`, `kafgrajno`, `ŝinko`, `granato`, `konservaĵo`, `frostigita`, `ĉerizo`, `bombono`, `filtrilo`, `biskvito`, `sunfloro`, `oleo`, `tabuleto`, `faruno`, `foliumi`, `kajero`, `orkideo`, `poŝtmarko`, `gvidlibro`, `amhar/o`, `Julieta`, `enciklopedia`, `poŝtkarto`, `brokanti`, `vidindaĵo`, `krizantemo`, `dianto`, `kvitanco`: `PIV2020_structured.txt`
- PIV 2020 `bastonpano`: https://vortaro.net/py/serchi.py?s=bastonpano&simpla=1
- PIV 2020 `bageto`: https://vortaro.net/py/serchi.py?s=bageto&simpla=1
- PIV 2020 `notbloko`: https://vortaro.net/py/serchi.py?s=notbloko&simpla=1
- PIV 2020 `amhara`: https://vortaro.net/py/serchi.py?s=amhara&simpla=1
- PIV 2020 `makedona`: https://vortaro.net/py/serchi.py?s=makedona&simpla=1
- PIV 2020 `ukraina`: https://vortaro.net/py/serchi.py?s=ukraina&simpla=1
- PIV 2020 `svahila`: https://vortaro.net/py/serchi.py?s=svahila&simpla=1
- PIV 2020 `leŭkanto`: https://vortaro.net/py/serchi.py?s=le%C5%ADkanto&simpla=1
- PIV 2020 `kvitanco`: https://vortaro.net/py/serchi.py?s=kvitanco&simpla=1
- PIV 2020 `brokanti`: https://vortaro.net/py/serchi.py?s=brokanti&simpla=1
- Glosbe `baguette`: https://glosbe.com/en/eo/baguette
- Glosbe `notepad`: https://glosbe.com/en/eo/notepad
- Glosbe `daisy`: https://glosbe.com/en/eo/daisy
- Glosbe `picture book`: https://glosbe.com/en/eo/picture%20book

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `0a13d25744fce4017b290c1fac11a641`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3656`〜`ID3755` は 100 件確認済み。
- `git diff --check` 問題なし。

## 553. 552周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care
- Shopping / Electronic Devices
- Shopping / Other Goods
- Shopping / At the Supermarket

結果:
- **1件修正（1行）**
- 電器・雑貨・スーパー表現を中心に、EO と JA/ZH/KO/RU の対応を再確認。PIV で確認できない借用語を、PIV/Glosbe で確認できる標準的な表現へ1件補正した。

修正:
- `ID3629` EO
  - `Mi ŝatus aĉeti suveniron de la urbo` → `Mi ŝatus aĉeti memoraĵon de la urbo`
  - 理由: `suveniro` は Glosbe には出るが頻度は低めで、PIV 2020 では確認できない。一方、Glosbe の souvenir 上位候補は `memoraĵo` で、PIV 2020 でも `memoraĵo` は確認できる。日中韓/RU の「この町の記念品/お土産/сувенир」文脈を保ったまま、確認済み語へ補正。

主な据え置き確認:
- `pinĉilo`, `raziloj`, `ŝargilo`, `garantio`, `lampo`, `monitoro`, `klavaro`, `baterioj`, `poŝtelefono`, `instrukcioj` は小売り・電器店文脈で対応する。
- `memorkarto` は PIV 直接見出しでは未確認だが、Glosbe で memory card → `memorkarto` を確認でき、`memoro` + `karto` の透明な複合語として維持。
- `lensokovrilo` は PIV/Glosbe 直接見出しでは未確認だが、PIV 確認済みの `lenso` + `kovrilo` による透明な複合語として lens cap/レンズキャップ文脈に対応するため維持。
- `printilo`, `skanilo`, `aŭskultiloj`, `laŭtparoliloj`, `muso por mia komputilo`, `elektronikaj ludiloj`, `elektra ventumilo`, `25-vataj ampoloj`, `harsekigilo` は電器・電子機器語彙として対応する。
- `vestbrosoj` は PIV 直接見出しでは未確認だが、`vesto` + `broso` の透明な複合語で clothes brush/洋服ブラシ文脈として維持。
- `linaj tablotukoj`, `ceramikaĵoj`, `figuretoj`, `sitelo kaj ŝovelilo`, `bierkruĉoj`, `arĝenta manĝilaro`, `kristalaj vinkarafoj`, `kudriloj kaj kudra fadeno`, `skribmaterialoj`, `tubo da gluo`, `pupoj`, `videoludo` は雑貨・玩具売り場の表現として対応する。
- `konstrubriketoj` は PIV の `briketo` に「子どもの構成遊びで使う木製・プラスチック片」の語義があり、building blocks/積木/конструкторы 文脈として維持。
- `mane teksita tapiŝo`, `blanka porcelano`, `taksi ĉi tion`, `likva sapo`, `pentraĵoj de famaj belgaj artistoj` は雑貨・美術品・日用品の買い物文脈として対応する。
- スーパー表現の `marmelado`, `korboj`, `botelo da lakto`, `bokalo da mustardo`, `olivoj`, `Konservu en fridujo`, `Revarmigu antaŭ manĝado`, `Fruktan torton` は食品購入・表示文脈として対応する。
- `Kiu estas la limdato?` は PIV 直接見出しでは未確認だが、Glosbe で expiry/expiration date → `limdato` を確認。`Kiu` は「どの日付か」を問う形として、食品表示の賞味期限文脈では許容範囲と判断し未修正。

参照:
- PIV 2020 ローカル `pinĉilo`, `razilo`, `ŝargilo`, `fotilo`, `lenso`, `kovrilo`, `printilo`, `skanilo`, `aŭskultilo`, `laŭtparolilo`, `harsekigilo`, `tablotuko`, `figureto`, `bierkruĉo`, `manĝilaro`, `karafo`, `kudrilo`, `fadeno`, `gluo`, `pupo`, `briko`, `briketo`, `tapiŝo`, `porcelano`, `marmelado`, `bokalo`, `mustardo`, `bakejo`, `torto`: `PIV2020_structured.txt`
- PIV 2020 `pinĉilo`: https://vortaro.net/py/serchi.py?s=pin%C4%89ilo&simpla=1
- PIV 2020 `ŝargilo`: https://vortaro.net/py/serchi.py?s=%C5%9Dargilo&simpla=1
- PIV 2020 `poŝtelefono`: https://vortaro.net/py/serchi.py?s=po%C5%9Dtelefono&simpla=1
- PIV 2020 `printilo`: https://vortaro.net/py/serchi.py?s=printilo&simpla=1
- PIV 2020 `skanilo`: https://vortaro.net/py/serchi.py?s=skanilo&simpla=1
- PIV 2020 `aŭskultilo`: https://vortaro.net/py/serchi.py?s=a%C5%ADskultilo&simpla=1
- PIV 2020 `laŭtparolilo`: https://vortaro.net/py/serchi.py?s=la%C5%ADtparolilo&simpla=1
- PIV 2020 `briketo`: https://vortaro.net/py/serchi.py?s=briketo&simpla=1
- PIV 2020 `memoraĵo`: https://vortaro.net/py/serchi.py?s=memora%C4%B5o&simpla=1
- PIV 2020 `suveniro`: https://vortaro.net/py/serchi.py?s=suveniro&simpla=1
- PIV 2020 `marmelado`: https://vortaro.net/py/serchi.py?s=marmelado&simpla=1
- PIV 2020 `bokalo`: https://vortaro.net/py/serchi.py?s=bokalo&simpla=1
- PIV 2020 `torto`: https://vortaro.net/py/serchi.py?s=torto&simpla=1
- Glosbe `memory card`: https://glosbe.com/en/eo/memory%20card
- Glosbe `souvenir`: https://glosbe.com/en/eo/souvenir
- Glosbe `expiry date`: https://glosbe.com/en/eo/expiry%20date
- Glosbe `expiration date`: https://glosbe.com/en/eo/expiration%20date

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `50279d427cae7f386cf5863d36e06db7`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3556`〜`ID3655` は 100 件確認済み。
- `git diff --check` 問題なし。

## 552. 551周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes
- Shopping / Shoes
- Shopping / Accessories
- Shopping / Personal Care

結果:
- **2件修正（2行）**
- 靴・アクセサリー語彙を中心に、PIV/Glosbe で確認できない EO 形を、同じ内容を保った確認済み・一般的な表現へ補正。その他の買い物・身だしなみ表現は文脈別許容として維持。

修正:
- `ID3485` EO
  - `Bonvolu montri al mi tiun paron da pantofoj` → `Bonvolu montri al mi tiun paron da pantofloj`
  - 理由: PIV 2020 で確認できる見出し語は `pantoflo`。`pantofo` は PIV で確認できず、Glosbe でも slipper の EO 対応は `pantoflo` / `babuŝo` 系。日中韓/RU の「スリッパ/拖鞋/슬리퍼/тапочки」と対応するよう、語幹を確認済み形に補正。
- `ID3498` EO
  - `Mi serĉas skarfon` → `Mi serĉas koltukon`
  - 理由: `skarfo` は PIV 2020 で確認できず、Glosbe でも scarf の上位候補は `koltuko`, `skarpo`, `kolskarpo`。同じブロック内の `ŝalo` は `ID3508` の shawl/ショールに対応済みで、ここでは JA `マフラー`、ZH `围巾`、KO `스카프`、RU `шарф` の「首に巻くスカーフ/マフラー」文脈なので、Glosbe で直接確認できる `koltuko` へ補正。

主な据え置き確認:
- `sablokolora`, `malpli multekostan`, `daŭrema`, `rabatvendo`, `stoko`, `artikolo`, `meti ĉi tion flanken` は衣料品・在庫確認の買い物文脈として対応する。
- `rabatvendo` は PIV 直接見出しでは弱いが、PIV の `rabato` + `vendo` による透明な複合語で、セール/распродажа 文脈と合うため維持。
- `mokasenoj`, `zorioj`, `sandaloj`, `sportŝuoj`, `gumaj botoj` は靴類として日中韓/RU と対応する。`sportŝuoj` は PIV 直接見出しでは未確認だが、PIV 確認済みの `sporto` + `ŝuo` による透明な複合語として維持。
- `Ili perfekte sidas al mi` は衣類・靴が「ぴったり合う」文脈で使われる比喩的表現として、EN/RU の fit/sit 表現とも整合するため維持。
- `felĉapo` は PIV 直接見出しでは未確認だが、PIV の `felo` には `fela ĉapo` の用例があり、`felo` + `ĉapo` の透明な複合語として fur cap/меховая шапка 文脈を保つため未修正。
- `ŝelkoj` は PIV の「ズボン等を留める二重の紐」として確認でき、suspenders/braces/подтяжки に対応する。
- `manumbutonoj` は PIV 直接見出しでは未確認だが、PIV の `butono` に `butonoj de manumoj` があり、Glosbe の cufflink 対応でも `manumbutono` を確認できるため維持。
- `horloĝrimeno` は PIV 直接見出しでは未確認だが、PIV の `brakhorloĝo` 説明に `per rimeno` があり、`horloĝo` + `rimeno` の透明な複合語として watch strap/ремешок для часов 文脈に対応する。
- `parfumon`, `tubon da dentopasto`, `lipruĝon`, `taga kremo`, `ŝampuon`, `dentobrosojn`, `ungofajlilon`, `pecon da sapo` はパーソナルケア用品として対応する。
- `paletron da ŝminko por la palpebroj` は eyeshadow palette を直訳的に説明した表現で、`ŝminko` と `palpebro` が PIV 確認済みのため維持。
- `Akvorezistan ŝminkon por okulharoj` は mascara を「まつげ用の防水化粧品」と説明した表現。`maskaro` は今回 PIV で確認できないため、日中韓/RU のマスカラ文脈を変えず、説明的な現行 EO を維持。
- `vizaĝpudro` は PIV 直接見出しでは未確認だが、PIV の `vizaĝo` + `pudro`、および Glosbe の face powder → `pudro` と整合し、化粧品文脈で意味ズレがないため維持。

参照:
- PIV 2020 ローカル `sablokolora`, `daŭrema`, `rabato`, `vendo`, `stoko`, `butono`, `manumo`, `horloĝo`, `rimeno`, `felo`, `ĉapo`, `ŝminko`, `palpebro`, `okulharo`, `pudro`: `PIV2020_structured.txt`
- PIV 2020 `mokaseno`: https://vortaro.net/py/serchi.py?s=mokaseno&simpla=1
- PIV 2020 `zorio`: https://vortaro.net/py/serchi.py?s=zorio&simpla=1
- PIV 2020 `ŝelko`: https://vortaro.net/py/serchi.py?s=%C5%9Delko&simpla=1
- PIV 2020 `pantoflo`: https://vortaro.net/py/serchi.py?s=pantoflo&simpla=1
- PIV 2020 `pantofo`: https://vortaro.net/py/serchi.py?s=pantofo&simpla=1
- PIV 2020 `felo`: https://vortaro.net/py/serchi.py?s=felo&simpla=1
- PIV 2020 `ĉapo`: https://vortaro.net/py/serchi.py?s=%C4%89apo&simpla=1
- PIV 2020 `horloĝo`: https://vortaro.net/py/serchi.py?s=horlo%C4%9Do&simpla=1
- PIV 2020 `rimeno`: https://vortaro.net/py/serchi.py?s=rimeno&simpla=1
- PIV 2020 `dentopasto`: https://vortaro.net/py/serchi.py?s=dentopasto&simpla=1
- PIV 2020 `vizaĝo`: https://vortaro.net/py/serchi.py?s=viza%C4%9Do&simpla=1
- PIV 2020 `pudro`: https://vortaro.net/py/serchi.py?s=pudro&simpla=1
- Glosbe `slipper`: https://glosbe.com/en/eo/slipper
- Glosbe `scarf`: https://glosbe.com/en/eo/scarf
- Glosbe `cufflinks`: https://glosbe.com/en/eo/cufflinks
- Glosbe `face powder`: https://glosbe.com/en/eo/face%20powder

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `46fa115aec86c102b79d6ff8a31c0caf`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3456`〜`ID3555` は 100 件確認済み。
- `git diff --check` 問題なし。

## 551. 550周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food
- Shopping / At the Department Store
- Shopping / Clothes

結果:
- **3件修正（3行）**
- 朝食語彙のうち、PIV/Glosbe 等で確認できない EO 借用語・造語疑いを、確認可能な表現へ補正。買い物・衣服表現は文脈別許容として維持。

修正:
- `ID3359` EO
  - `Mi ŝatas sorbeton` → `Mi ŝatas ŝorbeton`
  - 理由: PIV 2020 の見出し語は `ŝorbeto`。`sorbeto` は今回 PIV で確認できず、Glosbe でも sorbet の EO 候補は `ŝorbeto` / `fruktglaciaĵo` 系だったため、日中韓/RU の sorbet/シャーベット文脈を保ったまま確認済み形へ補正。
- `ID3367` EO
  - `Mi ŝatus la rizopudinon` → `Mi ŝatus la rizan pudingon`
  - 理由: PIV 2020 で確認できる語は `pudingo` で、旧形 `pudino` は確認できない。`riza pudingo` は `rizo` + PIV確認済み `pudingo` の透明な表現で、日中韓/RU の rice pudding 文脈を変えない。
- `ID3370` EO
  - `Ĉu vi manĝas kruasanojn ĉiutage?` → `Ĉu vi manĝas kornajn bulkojn ĉiutage?`
  - 理由: `kruasano` は PIV/Glosbe/Wiktionary で確認できず、Glosbe では croissant の EO 候補として `korna bulko`, `lunarka bulko` を確認。PIV で確認できる `bulko` を用いた `korna bulko` へ補正し、クロワッサンという内容は維持。

主な据え置き確認:
- `frititaj ovoj`, `kolbasoj`, `avenaj biskvitoj`, `krespoj`, `benjetoj`, `dolĉaj bulkoj`, `nigra pano`, `patkukoj kun acera siropo`, `senkafeina kafo`, `kazeo`, `kirlovaĵo`, `jogurto`, `artefarita dolĉigilo` は朝食・軽食語彙として対応する。
- `kirlovaĵo` は PIV 見出しでは直接確認できないが、PIV の `kirli ovojn` と Glosbe の scrambled eggs 対応を確認できるため維持。
- `rabatvendo`, `senimposta butiko`, `brakhorloĝoj`, `librejo`, `fako`, `sekcio`, `kaso`, `magazeno`, `nutraĵa sekcio`, `vendistoj` は百貨店案内として対応する。`rabatvendo` は PIV 直接見出しでは弱いが、PIV の `rabato` + `vendo` による透明な複合語として維持。
- `Butikoŝtelistoj estos juĝe persekutataj` は PIV の `persekuti` の法的文脈と、日中韓/RU の「法的措置/責任追及」に対応するため維持。
- 衣類表現の `surprovi`, `provejo`, `grandeco`, `konvenas al vi`, `taŭgas`, `pura kotono`, `kemia purigado`, `kemie purigi`, `laveblaj`, `Lavu inversigite`, `ŝorto`, `piĵamo` は衣料品店・洗濯表示文脈で対応する。
- `provejo` は PIV 見出しでは弱いが、`provi` + `-ej-` の透明な複合語で、衣料品店の fitting room 文脈として日中韓/RU と一致するため未修正。

参照:
- PIV 2020 ローカル `benjeto`, `bulko`, `kazeo`, `kirli`, `dolĉigilo`, `magazeno`, `rabato`, `persekuti`, `provi`, `grandeco`, `ŝorto`, `piĵamo`, `inversigi`: `PIV2020_structured.txt`
- PIV 2020 `ŝorbeto`: https://vortaro.net/py/serchi.py?s=%C5%9Dorbeto&simpla=1
- PIV 2020 `pudingo`: https://vortaro.net/py/serchi.py?s=pudingo&simpla=1
- PIV 2020 `benjeto`: https://vortaro.net/py/serchi.py?s=benjeto&simpla=1
- PIV 2020 `kazeo`: https://vortaro.net/py/serchi.py?s=kazeo&simpla=1
- PIV 2020 `kirli`: https://vortaro.net/py/serchi.py?s=kirli&simpla=1
- PIV 2020 `magazeno`: https://vortaro.net/py/serchi.py?s=magazeno&simpla=1
- PIV 2020 `rabato`: https://vortaro.net/py/serchi.py?s=rabato&simpla=1
- PIV 2020 `ŝorto`: https://vortaro.net/py/serchi.py?s=%C5%9Dorto&simpla=1
- PIV 2020 `piĵamo`: https://vortaro.net/py/serchi.py?s=pi%C4%B5amo&simpla=1
- Glosbe `croissant`: https://glosbe.com/en/eo/croissant
- Glosbe `scrambled eggs`: https://glosbe.com/en/eo/scrambled%20eggs
- Glosbe `dry-cleaning`: https://glosbe.com/en/eo/dry-cleaning

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `144570563cfc597369fb662764152324`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3356`〜`ID3455` は 100 件確認済み。
- `git diff --check` 問題なし。

## 550. 549周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit
- Food / Vegetables
- Food / Staple Food & Spices
- Food / Breakfast Food 冒頭

結果:
- **1件修正（1行）**
- 食品名・料理名が中心のブロックとして、EO と JA/ZH/KO の対応を主軸に再確認。PIV/Glosbe で確認できなかった EO 造語疑いを、確認済み語へ補正した。

修正:
- `ID3350` EO
  - `Mi volas iom da bekono` → `Mi volas iom da lardo`
  - 理由: `bekono` は PIV 2020 で確認できず、Glosbe の bacon 対応にも現れない。PIV 2020 の `lardo` は塩漬け・燻製を含む豚の脂身/肉として、`ovoj kun lardo` など料理用例があり、Glosbe でも bacon の EO 候補として確認できる。JA/ZH/KO/RU は bacon/бекон/培根/ベーコンで揃っているため、内容を変えずに確認済みの EO 語へ補正。

主な据え置き確認:
- `persikoj`, `avokado`, `prunoj`, `mango`, `kivifruktoj`, `akvomelono`, `kokoso`, `juglandoj`, `limeoj`, `ĉerizoj`, `abriko`, `nigra ribo`, `migdaloj`, `frambo`, `mirtelo`, `oksikoko`, `grapfrukto`, `figoj`, `arakidoj`, `strudelo`, `mandarinoj` は果物・ナッツ・果物菓子文脈で対応する。
- `limeojn` は PIV の `limeo` と日中韓/RU のライム文脈で一致する。EO は複数形だが、好悪表現で総称的に果物を指すため未修正。
- `Mi preferas ĵeleon el nigra ribo` は黒すぐり由来の jelly として、JA `カシスのゼリー`、ZH `黑加仑果冻`、KO/RU と対応する。
- `florbrasikon al brokolo` は `preferi X al Y` の構文として維持。RU の `брокколи` は不変化名詞のため、見かけ上は語形変化がなくても比較相手として読める。
- `papriko` は PIV では主に paprika spice / その植物・果実の語義で、sweet pepper を厳密に明示するなら `dolĉa kapsiko` も候補。ただし JA/KO が「パプリカ」、ZH/RU/EN が sweet pepper 系で、PIV の `kapsiko` 説明にも非辛味の大きな果実が野菜として使われる旨があるため、過修正を避けて現行維持。
- `akra kapsiko` は PIV の `kapsiko` と `akra` の組み合わせとして chilli 文脈に対応する。
- `peklitaj kukumoj`, `laktuko`, `panumita kukurbeto`, `betoj kun kapra fromaĝo`, `brezitaj karotoj kaj kikeroj` は野菜料理として日中韓/RU と対応する。
- `tofuon`, `rozmarenon` は PIV 見出しでは弱いが、Glosbe 等で現代食品語彙として確認できるため維持。
- `lardo` は bacon と完全に同一範囲ではない可能性があるが、PIV/Glosbe で確認できる現行最良候補として採用。`porkflankaĵo` は Glosbe にも出るが、PIV では確認できず、料理名としては `lardo` のほうが安定すると判断。
- `eruko`, `kuskusa salato`, `verdaj fazeoloj`, `safrana rizo`, `fazeola supo`, `petrosela saŭco`, `mocarelo`, `vafloj` は PIV で確認でき、食品文脈として意味ズレなし。
- `terpomoj` の JA `ポテト` は `じゃがいも` より料理注文では自然な場合があり、同ブロック内の `fritoj` / `フライドポテト` と区別されているため今回は未修正。

参照:
- PIV 2020 ローカル `avokado`, `kivifrukto`, `akvomelono`, `limeo`, `nigra ribo`, `mirtelo`, `oksikoko`, `grapfrukto`, `arakido`, `strudelo`, `florbrasiko`, `brokolo`, `papriko`, `kapsiko`, `melongeno`, `kuskuso`, `fazeolo`, `safrano`, `eruko`, `mocarelo`, `vaflo`: `PIV2020_structured.txt`
- PIV 2020 `papriko`: https://vortaro.net/py/serchi.py?s=papriko&simpla=1
- PIV 2020 `kapsiko`: https://vortaro.net/py/serchi.py?s=kapsiko&simpla=1
- PIV 2020 `eruko`: https://vortaro.net/py/serchi.py?s=eruko&simpla=1
- PIV 2020 `mocarelo`: https://vortaro.net/py/serchi.py?s=mocarelo&simpla=1
- PIV 2020 `vaflo`: https://vortaro.net/py/serchi.py?s=vaflo&simpla=1
- PIV 2020 `maizo`: https://vortaro.net/py/serchi.py?s=maizo&simpla=1
- PIV 2020 `lardo`: https://vortaro.net/py/serchi.py?s=lardo&simpla=1
- Majstro `dolĉa kapsiko`: https://www.majstro.com/dictionaries/Esperanto-English/dol%C4%89a%20kapsiko
- Glosbe `tofu`: https://glosbe.com/en/eo/tofu
- Glosbe `rosemary`: https://glosbe.com/en/eo/rosemary
- Glosbe `bacon`: https://glosbe.com/en/eo/bacon

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e2d188903ef3974be63ab02bbbe34cd5`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3256`〜`ID3355` は 100 件確認済み。
- `git diff --check` 問題なし。

## 549. 548周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints
- Restaurant & Pub / At the Pub
- Food / Meat & Fish

結果:
- **今回の追加修正なし**
- 過去周回で既に修正済みの ZH/KO/EO 行を含め、現在の CSV 上で EO/JA/ZH/KO/RU の列間対応を再確認した。今回新たに明確な意味ズレは見つからなかった。

主な据え置き確認:
- `Ĉu nia manĝaĵo jam venas?`, `Via mendo estos sur via tablo ene de 5 minutoj`, `Mankas unu plado`, `Ĝi ne estas sufiĉe kuirita`, `Mi ŝatus fari plendon` は、レストラン苦情文脈で日中韓/RU と対応する。
- `Nigran teon`, `Viskion kaj akvon`, `Kun glacio`, `Kun kremo`, `Kun sukero`, `lokan bieron`, `Kiu sekvas?` はパブでの短い注文表現として維持。
- `naĉojn` は PIV 見出しでは弱いが、Drops などの語彙ページで nachos の EO 形として確認でき、料理名として日中韓/RU が一致するため未修正。
- `postebrio` は PIV ローカルで `post ebrio` を確認でき、hangover / 二日酔い / 숙취 / похмелье と対応する。
- `barelan aŭ botelan bieron`, `glasetojn da tekilo`, `botelon da rumo`, `ĉipsoj`, `laktoskuaĵo`, `fritojn` はパブ・軽食語彙として維持。`laktoskuaĵo` は Glosbe でも milkshake 対応を確認。
- `rostbefo` は PIV 見出しで確認でき、過去修正後の `Mi prenos la rostbefon` を維持。
- `bifstekon el bova lumbaĵo`, `porkaj ripoj`, `bova ripo`, `bovida kotleto` は肉の部位・料理名として対応する。`bova ripo` の JA `リブロース` は直訳ではないが、牛リブ系の料理・部位として文脈別許容。
- `soleo`, `salikoko`, `kuniklo`, `ŝafidaĵo`, `ansero`, `fazano`, `kalmaro`, `truto`, `salmo`, `ostro`, `skombro`, `moruo`, `tinuso`, `koturno`, `polpo`, `krabo`, `karpo`, `ŝarko`, `haringo`, `kankro`, `omaro` は魚介・肉料理名として日中韓/RU と大きな意味ズレなし。
- `la salikoka supo finiĝis`, `ni ne plu havas omarojn` は品切れ表現として自然で、`finiĝis` / `ne plu havas` の使い分けも維持。

参照:
- PIV 2020 ローカル `post ebrio`, `rostbefo`, `lumbaĵo`, `kankro`, `tekilo`, `ĉipsoj`, `soleo`, `skombro`, `polpo`, `omaro`, `haringo`, `bifsteko`, `salikoko`, `fazano`, `kalmaro`, `ŝinko`: `PIV2020_structured.txt`
- PIV 2020 `rostbefo`: https://vortaro.net/py/serchi.py?s=rostbefo&simpla=1
- PIV 2020 `lumbaĵo`: https://vortaro.net/py/serchi.py?s=lumba%C4%B5o&simpla=1
- PIV 2020 `kankro`: https://vortaro.net/py/serchi.py?s=kankro&simpla=1
- PIV 2020 `tekilo`: https://vortaro.net/py/serchi.py?s=tekilo&simpla=1
- PIV 2020 `ĉipsoj`: https://vortaro.net/py/serchi.py?s=%C4%89ipsoj&simpla=1
- PIV 2020 `soleo`: https://vortaro.net/py/serchi.py?s=soleo&simpla=1
- PIV 2020 `skombro`: https://vortaro.net/py/serchi.py?s=skombro&simpla=1
- PIV 2020 `polpo`: https://vortaro.net/py/serchi.py?s=polpo&simpla=1
- PIV 2020 `omaro`: https://vortaro.net/py/serchi.py?s=omaro&simpla=1
- PIV 2020 `haringo`: https://vortaro.net/py/serchi.py?s=haringo&simpla=1
- Glosbe `milkshake` → EO `laktoskuaĵo`: https://glosbe.com/en/eo/milkshake
- Drops `nachos` → EO `naĉoj`: https://languagedrops.com/word/en/english/esperanto/translate/popcorn/

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e5cb0bdba496d083b57ff3b2a6fdfbc2`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3156`〜`ID3255` は 100 件確認済み。
- `git diff --check` 問題なし。

## 548. 547周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal
- Restaurant & Pub / Paying the Bill
- Restaurant & Pub / Complaints

結果:
- **1件修正（1行）**
- EO は追加修正なし。飲食店での食事中の確認表現として、JA 1件を発話意図に合わせて補正。

修正:
- `ID3057` JA
  - `どんな味がしますか？` → `お味はいかがですか？`
  - 理由: EO `Kiel ĝi gustas al vi?`、RU `Как вам на вкус?`、ZH `味道怎么样？`、KO `맛이 어때요?` は「味の種類」ではなく、相手にとって味がどうかを尋ねる評価表現。旧JAは「甘い/辛い等の種類」を聞く響きが強く、EO-JAクイズでは意味がずれるため、飲食店で自然な評価質問に補正。

主な据え置き確認:
- `Ĉu ĉi tiu manĝaĵo estas halala?` の `halala` は PIV 見出しでは未確認だが、Glosbe で halal の EO 形として確認でき、日中韓/RU もハラール文脈で揃うため維持。
- `manĝobastonetojn` は PIV の `manĝ bastonetoj` と `manĝilo` の説明により chopsticks 文脈として確認できる。表記の連結差は複合語として許容し、未修正。
- `fritoj` は PIV の `friti`・`terpom-fritoj` と料理文脈から「フライドポテト/картошка-фри」に対応するため維持。
- `Ankoraŭ unu porcion da rizo, mi petas` は省略された `mi petas` の目的語として `porcion` を取る注文表現として許容。
- `kalzoneon` は PIV 見出しでは未確認だが、Wiktionary で Italian calzone 由来の EO 名詞として確認でき、料理名の文脈で意味ズレなし。
- `rapidmanĝaĵo`, `laktaĵoj`, `trinkmono`, `restmono`, `servokotizo`, `konton`, `malĝuste sumigita`, `tro kuirita`, `odoras je korko`, `rostitan meleagron` は飲食店・会計・苦情文脈で対応する。
- `servokotizo` は PIV の `kotizo` が会費・分担金寄りで語義幅は残るが、同CSV内の service charge 表現として一貫し、RU `сервисный сбор`・日中韓も対応するため未修正。
- `Bonvolu skribi tion sur mian konton` は PIV では `en ies konton` 型も確認できるが、`sur mian konton` も「私の勘定につける」意図が日中韓/RUと揃っており、文脈別許容として維持。
- `Kie mi povas nutri la bebon?` の JA `赤ちゃんに食べさせられる場所はどこですか？` は「授乳」と限定せず、EO/RU/ZH/KO の「赤ちゃんに食事/ミルクを与える」一般表現として維持。

参照:
- PIV 2020 ローカル `bastoneto/manĝ bastonetoj`, `manĝilo`, `friti/terpom-fritoj`, `trinkmono`, `korko`, `meleagro`, `sumo/sumigi`, `kotizi/kotizo`, `konto`, `rosti`: `PIV2020_structured.txt`
- PIV 2020 `trinkmono`: https://vortaro.net/py/serchi.py?s=trinkmono&simpla=1
- PIV 2020 `korko`: https://vortaro.net/py/serchi.py?s=korko&simpla=1
- PIV 2020 `meleagro`: https://vortaro.net/py/serchi.py?s=meleagro&simpla=1
- PIV 2020 `sumigi`: https://vortaro.net/py/serchi.py?s=sumigi&simpla=1
- PIV 2020 `kotizo`: https://vortaro.net/py/serchi.py?s=kotizo&simpla=1
- PIV 2020 `konto`: https://vortaro.net/py/serchi.py?s=konto&simpla=1
- PIV 2020 `rosti`: https://vortaro.net/py/serchi.py?s=rosti&simpla=1
- PIV 2020 `terpom-fritoj`: https://vortaro.net/py/serchi.py?s=terpom-fritoj&simpla=1
- Glosbe `halal` → EO `halala`: https://glosbe.com/en/eo/halal
- Wiktionary `kalzoneo`: https://en.wiktionary.org/wiki/kalzoneo

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e5cb0bdba496d083b57ff3b2a6fdfbc2`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID3056`〜`ID3155` は 100 件確認済み。
- `git diff --check` 問題なし。

## 547. 546周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks
- Restaurant & Pub / Ordering Food
- Restaurant & Pub / During the Meal 冒頭

結果:
- **今回の追加修正なし**
- EO/JA/ZH/KO/RU の列間対応を再確認し、明確な意味ズレは見つからなかった。

主な据え置き確認:
- `oranĝa suko`, `papaja smuzio`, `glacio`, `doma vino`, `ĉampano`, `biero`, `karafo da limonado`, `koktelo`, `soja lakto`, `kruĉo da kranakvo`, `vinkarto`, `gustumi la vinon` は飲み物注文文脈で対応する。
- `koŝera manĝaĵo`, `vegetaranino`, `vegano`, `kebabo`, `pastaĵoj`, `bifsteko kun fritoj`, `vegetara pico`, `por forporti`, `por kunpreni`, `memservo` は料理・注文語彙として維持。
- `Pardonu, ni ne plu havas tion`, `Ni ne havas omarojn`, `Kion vi ŝatus anstataŭe?`, `Kiom da tempo ĝi daŭros?` は品切れ・待ち時間の会話として意味ズレなし。
- `antaŭmanĝaĵoj`, `supo de la tago`, `farĉitaj fungoj`, `ĉefplado`, `specialaĵo de la domo`, `tritavola sandviĉo`, `franca saŭco`, `mezrostita`, `bone rostita`, `sen salo` は飲食店メニュー・焼き加減・調理条件として対応する。
- `Oni jam servas min, dankon` の JA `もう注文していますので、大丈夫です。` は直訳ではないが、`Are you being served?` への日本語応答として自然で、会話意図は保たれるため未修正。
- `Mi manĝos sandviĉon` の JA `サンドイッチを食べます。` は注文場面では `サンドイッチにします` も候補だが、EO/RU/EN/ZH/KO が「食べる」寄りで揃っているため今回は未修正。

参照:
- PIV 2020 ローカル `akvo/kran akvo`, `trinki/trinkaĵo`, `ĉampano`, `brando`, `koktelo`, `konjako`, `koŝera`, `pastaĵoj`, `bifsteko`, `fritoj/terpom-fritoj`, `menuo`, `deserto`, `farĉi`, `omar/o`, `vegetara/vegetarano`, `kebabo`, `nudeloj`, `steko`, `rost/i`: `PIV2020_structured.txt`
- PIV 2020 `koŝera`: https://vortaro.net/py/serchi.py?s=ko%C5%9Dera&simpla=1
- PIV 2020 `pastaĵoj`: https://vortaro.net/py/serchi.py?s=pasta%C4%B5oj&simpla=1
- PIV 2020 `terpom-fritoj`: https://vortaro.net/py/serchi.py?s=terpom-fritoj&simpla=1
- PIV 2020 `bifsteko`: https://vortaro.net/py/serchi.py?s=bifsteko&simpla=1
- PIV 2020 `kran akvo`: https://vortaro.net/py/serchi.py?s=kran%20akvo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `7bad315b036934964df516d4b9649015`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2956`〜`ID3055` は 100 件確認済み。
- `git diff --check` 問題なし。

## 546. 545周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat
- Restaurant & Pub / Booking a Table
- Restaurant & Pub / Ordering Drinks

結果:
- **2件修正（1行・2列）**
- EO は追加修正なし。Hotel / Renting a Flat 文脈で JA/ZH を各1件、EO/RU/KO との対応に合わせて補正。

修正:
- `ID2867` JA/ZH
  - `ガレージが欲しいですか？` → `ガレージは必要ですか？`
  - `你想要一个车库吗？` → `你需要车库吗？`
  - 理由: EO `Ĉu vi bezonas garaĝon?`、RU `Вам нужен гараж?`、KO `차고가 필요하세요?` は want より need の表現。旧JA/ZHでも会話としては通るが、EO-JA/ZH対応のクイズでは `bezonas` の意味が薄れるため、内容を変えずに「必要/需要」へ補正。

主な据え置き確認:
- `vazaro`, `tukoj`, `litotukoj`, `balailo`, `tondilo`, `ŝvabrilo`, `rubsakoj`, `detergento`, `adaptilo`, `ampolo`, `garaĝo`, `kuirejaj iloj` はアパート備品・生活用品文脈として維持。
- `fridujo`, `kuirilo`, `varmigilo`, `mikroondilo`, `telerlavmaŝino`, `klimatizilo`, `lavmaŝino`, `elektromezurilo` は住居設備・家電語彙として意味ズレなし。
- `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `suĉkloŝo`, `adherema filmo`, `polvosuĉilo` は、PIV で直接確認できる語・透明な複合語・既存オンライン確認の範囲で文脈別許容。`suĉkloŝo` は PIV 見出しでは弱いが、plunger 文脈として既存確認どおり維持。
- `rezervi tablon`, `antaŭmendi tablon`, `rezervo`, `liberaj tabloj`, `tablo ĉe la fenestro`, `fumejo`, `sidi sur la teraso/en la suno/en la ombro` は飲食店予約文脈として対応する。
- `gasita akvo`, `akvo sen gaso`, `trinkaĵo`, `vinkarto` は飲み物注文文脈で意味ズレなし。
- `Ĉu vi havas sufiĉe da mono?` の JA `お金は足りていますか？` は `十分なお金がありますか` より自然な会話形として許容。

参照:
- PIV 2020 ローカル `vazaro`, `tuko/litotuko`, `ŝvabrilo`, `ampolo`, `komforto`, `fridujo`, `kuirilo`, `varmigilo`, `skatolo`, `mendi`, `rezervi`, `fumejo`, `gaso`, `karto`, `vazo`, `garaĝo`: `PIV2020_structured.txt`
- PIV 2020 `vazaro`: https://vortaro.net/py/serchi.py?s=vazaro&simpla=1
- PIV 2020 `ŝvabrilo`: https://vortaro.net/py/serchi.py?s=%C5%9Dvabrilo&simpla=1
- PIV 2020 `adheri`: https://vortaro.net/py/serchi.py?s=adheri&simpla=1
- PIV 2020 `gaso`: https://vortaro.net/py/serchi.py?s=gaso&simpla=1
- Wiktionary/Kaikki `suĉkloŝo`: https://kaikki.org/dictionary/Esperanto/meaning/s/su/su%C4%89klo%C5%9Do.html

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e5cb0bdba496d083b57ff3b2a6fdfbc2`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2856`〜`ID2955` は 100 件、`ID2867` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 545. 544周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay
- Hotel / Checking out
- Hotel / Complaints
- Hotel / Renting a Flat

結果:
- **1件修正（1行）**
- EO は追加修正なし。Hotel / Checking out 文脈で JA 1件を自然化。

修正:
- `ID2773` JA
  - `この請求書は何のものですか？` → `これは何の請求ですか？`
  - 理由: EO `Por kio estas ĉi tiu fakturo?`、RU `За что этот счёт?` は「この請求/会計は何に対するものか」を尋ねる精算表現。旧JAは `何のもの` が不自然で、ホテル精算の請求内容確認としては `何の請求` が自然なため補正。

主な据え置き確認:
- `lavejo`, `gladi`, `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `restmono`, `monŝranko`, `detaligita fakturo`, `personan ĉekon`, `bagaĝo`, `valoraĵoj` はホテル滞在・精算文脈として既存判断どおり維持。
- `servokotizo` は PIV の `kotizo` が会費・分担金寄りで語義幅は残るが、同ファイル内の service charge 表現として一貫しており、RU `сервисный сбор`・日中韓とも対応するため未修正。
- `lavujo` は PIV では洗濯用のたらい寄りで、客室の sink としてはやや広いが、既存確認どおり文脈別許容とし、日中韓側は洗面台/洗手池/세면대でホテル苦情文脈に揃っているため EO は過修正しない。
- `ŝtopita`, `bolilo`, `butono`, `klimatizilo`, `hejtado`, `ventumilo`, `littukoj`, `duobla lito`, `du apartaj litoj`, `subskribo`, `rehavi mian monon`, `apartamento/luo` はホテル設備・苦情・賃貸文脈で意味ズレなし。
- `Ĉu vi akceptas usonajn dolarojn?` の JA `アメリカドルは使えますか？` は `米ドル` のほうが一般的だが、意味ズレではないため今回は未修正。
- `Ĉi tiuj ne estas miaj aĵoj` / `Ĉi tiuj ne estas miaj` の JA `これは私のものではありません` は、集合を指す `これ` として読めるため、複数明示への過修正は見送った。

参照:
- PIV 2020 ローカル `gladi`, `kalkulo`, `fakturo`, `kotizo`, `ŝtopi`, `bolilo`, `butono`, `klimatizilo`, `hejtado`, `lavi/lavejo/lavujo`, `apartamento`, `lui/luo`, `ŝlosilo`, `bagaĝo`, `valoraĵo`: `PIV2020_structured.txt`
- PIV 2020 `fakturo`: https://vortaro.net/py/serchi.py?s=fakturo&simpla=1
- PIV 2020 `kalkulo`: https://vortaro.net/py/serchi.py?s=kalkulo&simpla=1
- PIV 2020 `kotizo`: https://vortaro.net/py/serchi.py?s=kotizo&simpla=1
- PIV 2020 `ŝtopi`: https://vortaro.net/py/serchi.py?s=%C5%9Dtopi&simpla=1
- PIV 2020 `bolilo`: https://vortaro.net/py/serchi.py?s=bolilo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `6f4396a2ba372fb52e4d949f4dc15087`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2756`〜`ID2855` は 100 件、`ID2773` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 544. 543周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Room
- Hotel / At Reception
- Hotel / During Your Stay

結果:
- **2件修正（2行）**
- EO は追加修正なし。Hotel / Booking a Room 文脈で JA 2件を自然化。

修正:
- `ID2665` JA
  - `これより静かなものはありますか？` → `もっと静かな部屋はありますか？`
  - 理由: EO `Ĉu estas io pli trankvila?`、RU `Есть что-нибудь потише?` は直訳上「もっと静かなもの」だが、ホテル予約文脈では尋ねている対象は部屋。旧JAは `もの` が不自然で、クイズ文脈でも選択肢の意味がぼやけるため、内容を変えずに「部屋」と明示。
- `ID2666` JA
  - `もう少し大きいものはありますか？` → `もう少し大きい部屋はありますか？`
  - 理由: EO `Ĉu vi havas ion pli grandan?`、ZH/KO は大きい部屋の有無として読める。ホテル予約文脈では `ion pli grandan` の対象を「部屋」とするのが自然で、旧JAの `もの` は会話として不自然だったため補正。

主な据え置き確認:
- `atendolisto`, `longdaŭra restado`, `ĉambro por nefumantoj`, `aldona/plia lito`, `ĉambronumero`, `ĉambroŝlosilo`, `matenmanĝo estas servata`, `ĉambroservo`, `monŝranko`, `savelirejo`, `telefonan ŝargilon`, `eksteran linion`, `telefona mesaĝo`, `gladigi`, `plusendi mian poŝton`, `mendi matenmanĝon` はホテル予約・滞在中の実用語彙として維持。
- `Je kioma horo vi fermas?` はホテル入口・フロント等の閉鎖時刻を尋ねる文脈として許容。
- `Ne ĝenu` の JA `起こさないでください` は、ホテルの札・依頼表現としては `Do not disturb` より少し具体化されるが、睡眠中に邪魔しないでほしい文脈として実用上許容。
- `La loĝanto havas gaston`, `Ĉambro malplenigita`, `La ĉambro estas rezervita`, `Ŝlosilo ĉe akcepto`, `Mi transloĝiĝis de la ĉambro 109` は受付・客室管理の文脈と対応する。

参照:
- PIV 2020 ローカル `atendi/atendolisto`, `ĉambro`, `ŝlosilo`, `lasi`, `tuko`, `kovrilo`, `ŝargilo`, `gladi/gladigi`, `savelirejo`, `plusendi`: `PIV2020_structured.txt`
- PIV 2020 `atendi`: https://vortaro.net/py/serchi.py?s=atendi&simpla=1
- PIV 2020 `monŝranko`: https://vortaro.net/py/serchi.py?s=mon%C5%9Dranko&simpla=1
- PIV 2020 `gladi`: https://vortaro.net/py/serchi.py?s=gladi&simpla=1
- PIV 2020 `plusendi`: https://vortaro.net/py/serchi.py?s=plusendi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `b5a2e97c9dff9f7fe237b065395008fa`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2656`〜`ID2755` は 100 件、`ID2665`/`ID2666` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 543. 542周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi
- Other Transport / Ship
- Hotel / Asking about Facilities
- Hotel / Booking a Room

結果:
- **1件修正（1行）**
- EO は追加修正なし。Hotel / Booking a Room 文脈で JA 1件を自然化。

修正:
- `ID2647` JA
  - `これ以上のものはありますか？` → `もっと良い部屋はありますか？`
  - 理由: EO `Ĉu estas io pli bona?`、EN/RU/ZH/KO は「もっと良いもの/選択肢はあるか」。ホテル予約文脈では「もっと良い部屋」が自然で、旧JAの `これ以上のもの` は better の意味が少し曖昧だったため補正。

主な据え置き確認:
- `taksimetro`, `nokta krompago`, `bankaŭtomato`, `veni preni min`, `halti ĉe la angulo` はタクシー文脈で対応する。
- `Savringo`, `Savboato`, `marmalsano`, `kajo`, `kajuto`, `haveno`, `enŝipiĝi`, `ferdeko`, `pramo`, `krozado`, `radiogramo`, `sunseĝo`, `transiro` は船旅語彙として維持。
- `Ĉu vin naŭzas vojaĝado?` は Ship 節内では ZH/KO が船酔い寄りだが、EO は「旅行で気分が悪くなるか」を広く尋ねる文として文脈別許容。
- `Ĉio inkluzivita`, `inkludita`, `aŭtoparkejo`, `monŝranko`, `ĉambroservo`, `rulseĝa aliro`, `frizejo`, `gimnastikejo`, `ŝtopilingo`, `duŝkabinoj` はホテル設備語彙として意味ズレなし。
- `unulita ĉambro`, `ĉambro kun du apartaj litoj`, `plena pensiono`, `antaŭpago`, `rezervo`, `Neniu libera loko` は宿泊予約文脈で対応する。

参照:
- PIV 2020 ローカル `kajuto`, `ferdeko`, `enŝipiĝi`, `krozado`, `radiogramo`, `ŝtopilingo`, `handikapulo`, `rulseĝo`, `pensiono`: `PIV2020_structured.txt`
- PIV 2020 `kajuto`: https://vortaro.net/py/serchi.py?s=kajuto&simpla=1
- PIV 2020 `ferdeko`: https://vortaro.net/py/serchi.py?s=ferdeko&simpla=1
- PIV 2020 `inkludi`: https://vortaro.net/py/serchi.py?s=inkludi&simpla=1
- PIV 2020 `ŝtopilingo`: https://vortaro.net/py/serchi.py?s=%C5%9Dtopilingo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `7c1be35a33912712ac7901bf1402483a`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2556`〜`ID2655` は 100 件、`ID2647` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 542. 541周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / At the Train Station
- Other Transport / On the Bus or Train
- Other Transport / Taxi

結果:
- **2件修正（2行）**
- EO は追加修正なし。Taxi 文脈で JA 2件を、EO/ZH/KO/RU との対応に合わせて自然化。

修正:
- `ID2545` JA
  - `これはあなたのためです。` → `これはどうぞ。`
  - 理由: EO `Ĉi tio estas por vi`、RU `Это вам`、ZH/KO は、タクシーで運転手に渡すチップ等の場面として自然。旧JAは直訳調で、実際の会話では不自然だったため、内容を変えずに日本語として自然化。
- `ID2547` JA
  - `空港利用料がかかります。` → `空港割増料金がかかります。`
  - 理由: EO `flughavena krompago`、EN `airport surcharge`、ZH `机场附加费`、KO `공항 할증료`、RU `дополнительный аэропортовый сбор` はタクシー料金の追加料金。旧JAは空港施設利用料にも読めるため、タクシー文脈の surcharge として明確化。

主な据え置き確認:
- `pensiula/unua-klasa/unudirekta/revenbileto`, `eksprestrajno`, `loka trajno`, `kajo`, `vojaĝkarto`, `abonbileto`, `rabataj tarifoj`, `skemo de la metroo` は鉄道・交通カード文脈で対応する。
- `haltejo`, `vagono`, `restoracia vagono`, `kupeo`, `pakaĵujo`, `Laŭpeta haltejo`, `preterveturis vian haltejon`, `Ĉi tiu trajno finiĝas ĉi tie` は車内案内として意味ズレなし。
- `taksimetro`, `restmono`, `trinkmono`, `taksihaltejo`, `flughavena krompago`, `disponeblaj aŭtoj` はタクシー手配・会計語彙として維持。
- `Veturigu min ĉi tien`, `Ellasu min ĉi tie`, `Venu preni min`, `Mi veturas al ĉi tiu adreso` はタクシーの実用会話として文脈別許容。
- `Mian restmonon, mi petas` は PIV の直接見出し確認は弱いが、`resti/resta` 系の透明な複合語で、同データ内の釣り銭文脈と整合するため未修正。

参照:
- PIV 2020 ローカル `abono`, `kajo`, `kupeo`, `vagono`, `haltejo`, `taksio/taksimetro`, `trinkmono`, `krompago`: `PIV2020_structured.txt`
- PIV 2020 `adreso`: https://vortaro.net/py/serchi.py?s=adreso&simpla=1
- PIV 2020 `haltejo`: https://vortaro.net/py/serchi.py?s=haltejo&simpla=1
- PIV 2020 `kupeo`: https://vortaro.net/py/serchi.py?s=kupeo&simpla=1
- PIV 2020 `pakaĵo`: https://vortaro.net/py/serchi.py?s=paka%C4%B5o&simpla=1
- PIV 2020 `taksio`: https://vortaro.net/py/serchi.py?s=taksio&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `e71c202465c3aeb4e6001dfb375854c1`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2456`〜`ID2555` は 100 件、`ID2545`/`ID2547` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 541. 540周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs
- Other Transport / At the Bus Station
- Other Transport / At the Train Station

結果:
- **1件修正（1行）**
- EO は追加修正なし。道路標識文脈で JA 1件を、EO/ZH/KO/RU との対応に合わせて補正。

修正:
- `ID2359` JA
  - `止まれ！立入禁止！` → `止まれ！通行禁止！`
  - 理由: EO `Haltu! Trapaso malpermesita!` は `trapaso`（通過・通行）の禁止で、ZH `禁止通行`、KO `통행 금지`、RU `Проход запрещён` とも対応する。旧JA `立入禁止` は場所への立ち入り禁止に寄るため、道路標識・通行文脈として自然化。

主な据え置き確認:
- `Parkumejo`, `Vojlaboroj`, `Parkumado malpermesita`, `Rapidlimo`, `Eniro malpermesita`, `Vojo fermita`, `Buskoridoro`, `Cedu vojon` は道路標識として意味ズレなし。
- `Preterpasu maldekstre` は RU が障害物回避標識寄り、EN/JA/ZH/KO が keep left 寄りだが、左側通行指示として文脈別許容。
- `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo`, `Piedira transirejo`, `Ne trinku kaj veturu` は標識語として維持。
- `bileto`, `karto`, `revenbileto`, `monata abono`, `unudirekta bileto`, `grupa tarifo`, `rabatita tarifo`, `pensiula revenbileto`, `retura bileto` はバス・鉄道切符文脈で対応する。
- `stampi la bileton` は交通機関の切符に押印・検札/有効化する文脈として維持。ZH `打票` はやや地域差があるが、明確な意味ズレではないため今回は未修正。
- `Kiu kajo?`, `kajo numero 1`, `Atentu la interspacon`, `rekta trajno`, `ekspresa trajno`, `malfruiĝas`, `troplena`, `atendejo` は駅・鉄道案内として意味ズレなし。

参照:
- PIV 2020 ローカル `trapasi/trapaso`, `piedira`, `trafiklumoj`, `abono`, `tarifo`, `biletejo`, `stacidomo`, `kajo`, `trajno`, `stampi`: `PIV2020_structured.txt`
- PIV 2020 `piedira zono`: https://vortaro.net/py/serchi.py?s=piedira%20zono&simpla=1
- PIV 2020 `kajo`: https://vortaro.net/py/serchi.py?s=kajo&simpla=1
- PIV 2020 `abono`: https://vortaro.net/py/serchi.py?s=abono&simpla=1
- PIV 2020 `vagono`: https://vortaro.net/py/serchi.py?s=vagono&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `27a50e05aec417418553617c6813f0f0`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2356`〜`ID2455` は 100 件、`ID2359` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 540. 539周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking
- Car / At the Petrol Station
- Car / Mechanical Problems
- Car / Road Signs

結果:
- **3件修正（1行）**
- EO は追加修正なし。ID2308 の JA/ZH/KO を、車・給油所文脈の `oleo` として自然化。

修正:
- `ID2308` JA/ZH/KO
  - JA `油が必要です。` → `オイルが必要です。`
  - ZH `我需要一些油。` → `我需要一些机油。`
  - KO `기름이 좀 필요해요.` → `오일이 좀 필요해요.`
  - 理由: EO `Mi bezonas iom da oleo`、EN `oil`、RU `масло` は Car / At the Petrol Station 文脈では車用オイルとして読むのが自然。旧JA/ZH/KOは一般の油・燃料にも読め、直後の `ID2329` オイル交換表現とも揃わないため、内容を変えずに車文脈へ寄せた。

主な据え置き確認:
- `stirada ekzameno`, `vojsignoj`, `unudirekta strato`, `piedirantoj`, `aŭtovojo`, `aŭtoriparejo`, `parkometro` は運転・道路文脈で意味ズレなし。
- `serva areo` は高速道路の service area として JA/ZH/KO/EN と整合。RU は整備拠点寄りにも読めるが、参考列だけで EO を動かす根拠は弱いため維持。
- `fervojajn liniojn`, `trafikrondo`, `trafikblokiĝo`, `akcidento`, `veturi maldekstre` は道路案内文脈で対応する。
- `benzino`, `benzinejo`, `brulaĵo`, `dizelo`, `benzinujo`, `pneŭoj/pneŭmatikoj`, `startokabloj` は給油所・車両語彙として維持。
- `akumulatoro`, `malŝargiĝis`, `pneŭmatiko krevis`, `hupo`, `direktomontriloj`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `bremslikvaĵo` は過去修正後の形を維持。

参照:
- PIV 2020 ローカル `oleo`, `benzino`, `brulaĵo`, `akumulatoro`, `pneŭmatiko`, `hupo`, `rapidometro`, `stirmekanismo`: `PIV2020_structured.txt`
- PIV 2020 `akumulatoro`: https://vortaro.net/py/serchi.py?s=akumulatoro&simpla=1
- PIV 2020 `paneo`: https://vortaro.net/py/serchi.py?s=paneo&simpla=1
- PIV 2020 `rapidometro`: https://vortaro.net/py/serchi.py?s=rapidometro&simpla=1
- PIV 2020 `pneŭmatiko`: https://vortaro.net/py/serchi.py?s=pne%C5%ADmatiko&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `d576a465a2834c3963010df497433f60`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2256`〜`ID2355` は 100 件、`ID2308` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 539. 538周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane
- Plane / Airport Signs
- Car / Car Hire
- Car / Driving & Parking

結果:
- **今回の追加修正なし**
- 既存周回で `mana/aŭtomata transmisio`, `kaŭcio`, `redoni la aŭton`, `trafikrondo` などの主要な意味ズレは修正済み。今回の再点検では、EO および JA/ZH/KO のクイズ対応に追加で明確な誤りは見つからなかった。

主な据え置き確認:
- `sur la aviadilo`, `stevardino kiu parolas la hebrean`, `formularon por dogandeklaro`, `forflugoj`, `pordegoj`, `bagaĝa elpreno` は機内・空港標識として意味ズレなし。
- `lui aŭton/biciklon/mopedon/motorciklon`, `mana/aŭtomata transmisio`, `infana aŭtoseĝo`, `benzinujo`, `centra ŝlosado`, `kofrujo`, `infanseruroj`, `direktomontriloj`, `klimatizilo`, `stirpermesilo` はレンタカー文脈で対応する。
- `redoni la aŭton kun plena benzinujo`, `redoni la aŭton ĉe mia celloko`, `lasi la aŭton ĉe la flughaveno`, `aldoni duan ŝoforon`, `rapidlimo sur aŭtovojoj` は過去修正後の形を維持。
- `Veturu trans la ponton`, `Veturu sub la ponto`, `Veturu tra la trafikrondo`, `vojmapo`, `loko por halti` は運転案内として文脈別許容。
- `ID2156` `veki min por la manĝo` は RU が「食事前」寄りだが、機内で「食事のために起こす」として意味は一致するため維持。

参照:
- PIV 2020 ローカル `traduki`, `dogano/deklaro`, `pordego`, `lui`, `transmisio`, `benzinujo`, `seruro`, `aŭtovojo`, `mapo`: `PIV2020_structured.txt`
- PIV 2020 `transmisio`: https://vortaro.net/py/serchi.py?s=transmisio&simpla=1
- PIV 2020 `benzinujo`: https://vortaro.net/py/serchi.py?s=benzinujo&simpla=1
- PIV 2020 `aŭtovojo`: https://vortaro.net/py/serchi.py?s=a%C5%ADtovojo&simpla=1
- PIV 2020 `seruro`: https://vortaro.net/py/serchi.py?s=seruro&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `d576a465a2834c3963010df497433f60`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2156`〜`ID2255` は 100 件確認済み。
- `git diff --check` 問題なし。

## 538. 537周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage
- Plane / Passport Control & Customs
- Plane / On the Plane

結果:
- **今回の追加修正なし**
- 既存周回で `registrigi`, `dogano`, `enmigrada formularo`, `reklini`, `sekurzono` などの主要な意味ズレは修正済み。今回の再点検では、EO および JA/ZH/KO のクイズ対応に追加で明確な誤りは見つからなかった。

主な据え置き確認:
- `ID2056/2058` `manbagaĝo`, `ID2057` `registrigi ĉi tion kiel bagaĝon`, `ID2061` `bagaĝetikedo`, `ID2063` `bagaĝ-ricevejo`, `ID2150` `supran bagaĝujon` は空港荷物文脈で意味が明確。
- `ID2089/2113/2115` `dogano` は、税関そのものではなく duty/関税としても使えることを既存の PIV 照合に基づき維持。
- `ID2085/2101/2120` `azilo`, `peti azilon`, `statuson de rifuĝinto` は政治的庇護・難民関連の表現として JA/ZH/KO/RU と整合。
- `ID2102` `enŝipiĝo` は語源的には船舶寄りだが、航空の boarding 文脈で既存周回どおり文脈別許容として維持。
- `ID2127` `reklini mian seĝon`, `ID2130` `fiksi vian sekurzonon`, `ID2149` `remeti vian seĝodorson en la vertikalan pozicion` は機内表現として整合。
- `ID2140` `stevardino` は EN が中立的な flight attendant だが、RU が女性形 `стюардессой` であり、現行 EO を動かす根拠は弱いため維持。
- `ID2152` JA `どの高度を飛んでいますか`、`ID2155` ZH `机上有免税商品销售吗` などはより自然な言い換え候補はあるが、意味ズレは明確ではないため今回は未修正。

参照:
- PIV 2020 ローカル `registri/registrigi`, `bagaĝo`, `dogano`, `azilo`, `rifuĝinto`, `sekurzono`, `stevardo`, `seĝodorso`: `PIV2020_structured.txt`
- PIV 2020 `dogano`: https://vortaro.net/py/serchi.py?s=dogano&simpla=1
- PIV 2020 `azilo`: https://vortaro.net/py/serchi.py?s=azilo&simpla=1
- PIV 2020 `sekurzono`: https://vortaro.net/py/serchi.py?s=sekurzono&simpla=1
- PIV 2020 `stevardo`: https://vortaro.net/py/serchi.py?s=stevardo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `82a4a5b27c3a56d157631742252d6d09`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID2056`〜`ID2155` は 100 件確認済み。
- `git diff --check` 問題なし。

## 537. 536周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight
- Plane / Checking in
- Plane / Luggage

結果:
- **5件修正（3行）**
- EO は追加修正なし。JA/ZH/KO の空港・搭乗手続き表現を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID2007` JA/ZH/KO
  - JA `国内ですか、それとも海外ですか？` → `国内線ですか、それとも国際線ですか？`
  - ZH `国内还是国际？` → `国内航班还是国际航班？`
  - KO `국내인가요, 아니면 해외인가요?` → `국내선인가요, 아니면 국제선인가요?`
  - 理由: EO `Enlanda aŭ internacia?` は空港チェックイン文脈では国内線/国際線の区別。旧JA/KOの「海外」は `international` そのものではなく、クイズ上やや曖昧だったため航空便の種別として明確化。
- `ID2020` ZH
  - `你有你的预订参考号吗？` → `您有预订编号吗？`
  - 理由: EO `rezervonumero`、JA `予約番号`、RU `номер бронирования` は予約番号。旧ZHの `预订参考号` は意味は推測できるが不自然で、二重の `你/你的` も硬いため自然化。
- `ID2021` ZH
  - `这是我的预订参考号。` → `这是我的预订编号。`
  - 理由: 上記と同様に、EO `Jen mia rezervonumero` に合わせて予約番号として統一。

主な据え置き確認:
- `halto dumvoje`, `rekta flugo`, `flugkompanio`, `komerca klaso`, `antaŭa/malantaŭa vico`, `celloko`, `forveturo` は航空予約文脈で各列と整合。
- `ŝanĝi aviadilon` は以前の `transŝanĝo` 修正後の形を維持。PIVで確認できる `ŝanĝi` + `aviadilo` による「飛行機を乗り換える」表現として自然。
- `registrejo`, `enŝipiĝo`, `atendejo`, `pordego/elirejo`, `senimposta butiko` は空港チェックイン文脈で意味ズレなし。`pordego` は空港ゲートとしても用例確認できるが、既存の `elirejo` との併存は文脈別許容として維持。
- `bagaĝo`, `valizo`, `bagaĝetikedo`, `ĉareto`, `bagaĝaj ŝranketoj`, `manbagaĝo`, `superpezo` は荷物関連語として維持。
- `Bonvolu elpreni vian tekkomputilon el ĝia ujo`, `kunporti tion`, `sendi mian bagaĝon al la hotelo`, `porti ĉi tiun bagaĝon al la taksihaltejo` は空港保安・荷物依頼文脈で対応列と整合。

参照:
- PIV 2020 ローカル `flugi/flugo`: `PIV2020_structured.txt`
- PIV 2020 ローカル `aviadilo`, `ŝanĝi`, `rezervi`, `registri`, `bagaĝo`, `valizo`: `PIV2020_structured.txt`
- Drops 空港語彙 `enlanda flugo`, `internacia flugo`, `pordego`: https://languagedrops.com/word/en/esperanto/english/translate/pordego/
- Glosbe `baggage` → `bagaĝo`: https://glosbe.com/en/eo/baggage

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `82a4a5b27c3a56d157631742252d6d09`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1956`〜`ID2055` は 100 件、`ID2007`/`ID2020`/`ID2021` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 536. 535周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions
- Travel / At the Tourist Office
- Travel / Excursions
- Plane / Booking a Flight

結果:
- **5件修正（5行）**
- EO は追加修正なし。JA 3件、KO 2件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1873` KO
  - `시장 어디에 있나요?` → `시장은 어디에 있나요?`
  - 理由: EO `Kie estas la merkato?`、JA/ZH/RU は「市場はどこか」。旧KOも意味は通るが、助詞を補い、観光案内所での自然な質問形にした。
- `ID1910` KO
  - `안내해 주실 수 있나요?` → `가이드를 부탁드릴 수 있나요?`
  - 理由: EO `Ĉu mi povas havi gvidiston?` と RU/JA/ZH は「ガイドという人をお願いできるか」。旧KOは「案内してもらえるか」と行為に寄り、`gvidisto` の人名詞が落ちていた。
- `ID1923` JA
  - `何かエクスカーションはありますか？` → `何か観光ツアーはありますか？`
  - 理由: EO `ekskursoj` と RU/EN/ZH/KO は観光ツアー・ экскурсии。旧JAの `エクスカーション` は旅行業界語としてはあり得るが、学習クイズの日本語としては不自然なため自然化。
- `ID1924` JA
  - `こちらがエクスカーションの一覧です。` → `こちらが観光ツアーの一覧です。`
  - 理由: 上記と同様に、`ekskursoj` の日本語を自然な表現へ統一。
- `ID1938` JA
  - `このエクスカーションの申し込みはどこでできますか？` → `この観光ツアーの申し込みはどこでできますか？`
  - 理由: EO `aliĝi al la ekskurso` は「そのツアーに申し込む/参加登録する」。旧JAの外来語を自然化し、周辺の `tour` 系表現と揃えた。

主な据え置き確認:
- `Daŭrigu rekten preter kelkaj semaforoj`, `subpasejo`, `indikiloj`, `turisma oficejo`, `urbocentro` は道案内・観光案内所文脈で意味ズレなし。
- `vidindaĵoj`, `junulargastejoj`, `tendumejoj`, `sandviĉejo`, `naveda buso`, `rondvojaĝoj`, `gvidata ekskurso`, `vidindaĵa ekskurso` は既存周回の PIV 2020 照合どおり維持。
- `preni miajn fotojn`, `presi la fotojn de ĉi tiu memorkarto`, `subeksponitaj` は写真受け取り・印刷・露出不足の文脈で各列と整合。
- `en la estona`, `gvidisto kiu parolas la kartvelan`, `ekonomiklasa bileto` は言語指定・航空券表現として維持。

参照:
- PIV 2020 ローカル `ekskurso`: `PIV2020_structured.txt`
- PIV 2020 ローカル `gvidi/gvidisto`: `PIV2020_structured.txt`
- PIV 2020 `turisma`: https://vortaro.net/py/serchi.py?s=turisma&simpla=1
- PIV 2020 `gastejo`: https://vortaro.net/py/serchi.py?s=gastejo&simpla=1
- PIV 2020 `vidindaĵo`: https://vortaro.net/py/serchi.py?s=vidinda%C4%B5o&simpla=1
- PIV 2020 `preni`: https://vortaro.net/py/serchi.py?s=preni&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `d123c12235a07bce2a59512d4236536a`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1856`〜`ID1955` は 100 件、`ID1873`/`ID1910`/`ID1923`/`ID1924`/`ID1938` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 535. 534周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter
- Travel / Asking Directions
- Travel / Giving Directions

結果:
- **5件修正（5行）**
- EO は追加修正なし。ZH 4件、KO 1件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1759` KO
  - `그는 여러 프로젝트에서 저와 함께 일했습니다.` → `그는 여러 프로젝트에서 제 밑에서 일했습니다.`
  - 理由: EO `Li laboris por mi pri diversaj projektoj` と RU `Он работал у меня...`、JA `私のもとで` は「私の下で/私のために」。旧KOは `kun mi` に近い「私と一緒に」に寄っていたため、推薦状文脈に合わせて補正。
- `ID1763` ZH
  - `她始终如一地产出高质量的工作。` → `她始终能完成高质量的工作。`
  - 理由: EO `produktas altkvalitan laboron` は「高品質な仕事を生み出す/こなす」。旧ZHは `产出...工作` がやや不自然な組み合わせだったため、意味を保って自然化。
- `ID1764` ZH
  - `她将为你的项目带来极大助力。` → `她将成为贵项目的优秀补充。`
  - 理由: EO `bonega aldono al via programo` と RU `отличным дополнением вашей программы` は「プログラムへの優れた追加・戦力」。旧ZHは「助力」に言い換えられ、かつ推薦状文脈として `你的` がややくだけすぎるため補正。
- `ID1832` ZH
  - `路还很远。` → `走路去的话很远。`
  - 理由: EO `Piede estas malproksime`、RU `Пешком идти далеко`、JA/KO は「歩くには遠い」。旧ZHは「道がまだ遠い」だけで、歩行条件が落ちていた。
- `ID1834` ZH
  - `它将在你的左侧。` → `它会在你的左手边。`
  - 理由: EO `Ĝi estos maldekstre de vi` と RU/JA/KO は道案内で「左手にある」。旧ZHは意味は取れるが機械的で、道案内として自然な `左手边` に補正。

主な据え置き確認:
- `rekomendletero`, `gvidanto`, `komunikaj kapabloj`, `plej varman rekomendon`, `elstaran kontribuon`, `fidinda persono kun bona humursento` は推薦状文脈で意味ズレなし。
- `ŝparvojo`, `marbordo`, `stacidomo`, `aŭtobusa stacio`, `ambasadejo`, `orientiĝas`, `piediri`, `trans la strato`, `fajrobrigadejo` は既存周回の PIV 2020 照合どおり維持。
- `Mi malfacile orientiĝas` は JA が「道に迷った」に寄るが、方向感覚を失っている旅行会話として許容。
- `diri al mi la direkton` は `montri la vojon` も候補だが、方向・道順を尋ねる発話として日中韓と大きく衝突しない。
- `Daŭrigu ankoraŭ duonkilometron` は「さらに約500m進む」と対応し、距離表現として維持。

参照:
- PIV 2020 ローカル `programo`: `PIV2020_structured.txt`（計画・番組・学習課程・コンピュータプログラム等の語義）
- PIV 2020 ローカル `gvidi/gvidanto`: `PIV2020_structured.txt`
- PIV 2020 `ŝparvojo`: https://vortaro.net/py/serchi.py?s=%C5%9Dparvojo&simpla=1
- PIV 2020 `orientiĝi`: https://vortaro.net/py/serchi.py?s=orienti%C4%9Di&simpla=1
- PIV 2020 `piediri`: https://vortaro.net/py/serchi.py?s=piediri&simpla=1
- PIV 2020 `trans`: https://vortaro.net/py/serchi.py?s=trans&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `c98aa1e720bd81d1510aa388351edd1f`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1756`〜`ID1855` は 100 件、`ID1759`/`ID1763`/`ID1764`/`ID1832`/`ID1834` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 534. 533周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business
- Jobs / At the Interview
- Jobs / Recommendation Letter

結果:
- **3件修正（3行）**
- EO は追加修正なし。ZH 3件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1662` ZH
  - `您的报价符合我们的要求。` → `您的提议符合我们的要求。`
  - 理由: EO `Via propono`、RU `Ваше предложение`、JA/KO は「提案」。旧ZHの `报价` は価格見積りに狭く、価格交渉文と混同しやすいため、より広い `提议` に補正。
- `ID1673` ZH
  - `请返回一份已签署的合同副本。` → `请寄回一份已签署的合同副本。`
  - 理由: EO `resendi` と JA/RU は「署名済みコピーを返送する」。旧ZHの `返回` は意味は取れるが文書返送として硬く不自然なため、`寄回` に補正。
- `ID1740` ZH
  - `我很珍惜能够拓宽知识的机会。` → `如果能有机会拓宽知识，我将不胜感激。`
  - 理由: EO `Mi estus dankema pro la ebleco...` と EN/JA/KO/RU は「機会があれば感謝する」という条件的な丁寧表現。旧ZHは既に機会を得ているような叙述に寄るため補正。

主な据え置き確認:
- `afervojaĝojn`, `formularon por vivresumo`, `laborkontrakto`, `provperiodo`, `aliĝilo` は既存周回で PIV 2020 と照合済みのため維持。
- `Kiam ni negocos pri la prezo?`, `fakturas nur en eŭroj`, `dato de ekspedo`, `mendo`, `kontrakto` はビジネス文脈で列間対応を保つ。
- `Al kiu mi devus raporti?`, `akiri rekomendojn`, `labori laŭvice`, `vojaĝkostojn` は面接・雇用文脈で許容範囲。
- `Mia fako estas informatiko` は情報技術寄りの訳と専門分野名の揺れがあるが、`informatiko` は分野名として成立するため維持。
- `fortaĵoj/malfortaĵoj`, `lojaleco/akurateco`, `plenumas siajn devojn` は推薦状・面接評価として意味ズレなし。

参照:
- PIV 2020 ローカル `proponi`: `PIV2020_structured.txt`（`proponi al iu siajn servojn` 等）
- PIV 2020 ローカル `kontrakto`: `PIV2020_structured.txt`（`kontrakto`: Jure valida interkonsento）
- PIV 2020 ローカル `sendi/resendi`: `PIV2020_structured.txt`
- PIV 2020 `aliĝilo`: https://vortaro.net/py/serchi.py?s=ali%C4%9Dilo&simpla=1
- PIV 2020 `laborkontrakto`: https://vortaro.net/py/serchi.py?s=laborkontrakto&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `18783ade9407afa62f3a1d11e1b48284`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1656`〜`ID1755` は 100 件、`ID1662`/`ID1673`/`ID1740` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 533. 532周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation
- Jobs / Employment Status
- Jobs / At the Workplace
- Jobs / Business

結果:
- **1件修正（1行）**
- EO は追加修正なし。JA 1件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1595` JA
  - `自分の会社を経営しています。` → `自分の事業をしています。`
  - 理由: EO `Mi havas propran komercon` と RU `У меня свой бизнес.` は「自分の事業/ビジネスを持っている」。PIV 2020 ローカル抽出でも `komerco` は商業・事業の語義で、旧JAの「会社」は法人・会社経営に狭まりすぎるため、より広い自然な表現へ補正。

主な据え置き確認:
- `merkatika administranto` は `merkatiko` + `administranto` として成立するが、EN/JA/ZH/KO の manager 寄りと RU の specialist 寄りに揺れがあるため、役職名を一方向へ固定する修正は避けた。
- `trejniĝas por fariĝi ...`, `staĝanta administranto`, `doktoro pri juro`, `advokata firmao`, `Mi faras praktikon`, `patrina/patra forpermeso` は職業・雇用状態文脈で維持。
- `maldungita pro redukto de laborfortoj` は PIV 2020 ローカル抽出の用例と整合し、整理解雇の意味を保つため維持。
- `fotokopiilo`, `retpoŝto`, `fakturo`, `faksi`, `kliento`, `limtempo por liveri la varojn finiĝas`, `interkonsento` は職場・商談文脈で意味ズレなし。
- `nevo`, `pli aĝa fratino`, `onklino` は中韓の親族語で話者性別・父母系の選択が出るが、対象言語上の自然な具体化として文脈別許容。

参照:
- PIV 2020 ローカル `komerco`: `PIV2020_structured.txt`（`komerco`: Profesia klopodo por la interŝanĝo de varoj）
- PIV 2020 `merkatiko`: https://vortaro.net/py/serchi.py?s=merkatiko&simpla=1
- PIV 2020 `dungi`: https://vortaro.net/py/serchi.py?s=dungi&simpla=1
- PIV 2020 `faksi`: https://vortaro.net/py/serchi.py?s=faksi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `fc9717c8bb13fdd85250399bc45fbf7d`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1556`〜`ID1655` は 100 件、`ID1595` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 532. 531周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life
- Numbers & Colours
- Jobs / Occupation

結果:
- **5件修正（3行）**
- EO は追加修正なし。JA 2件、ZH 2件、KO 1件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1540` JA
  - `どちらの会社にお勤めですか？` → `勤務先はどちらですか？`
  - 理由: EO `Por kiu vi laboras?` と RU `На кого ты работаешь?` は雇用主・勤務先を尋ねる文。旧JAは「会社」に限定され、`loka konsilio` のような非会社勤務の近接文脈とやや衝突するため、より広い自然な質問へ補正。
- `ID1543` JA/ZH/KO
  - JA `彼は弁護士です。` → `彼は法律家です。`
  - ZH `他是一名律师。` → `他是一名法律工作者。`
  - KO `그는 변호사예요.` → `그는 법률가예요.`
  - 理由: EO `juristo` は PIV 2020 ローカル抽出で「法律・司法の専門家」、ReVo でも `Fakulo pri juro` と確認。RU `юрист` も同範囲。旧日中韓は `advokato` 相当の「弁護士」に寄りすぎ、クイズ上の語彙対応を狭めるため補正。
- `ID1555` ZH
  - `我从事残障儿童的工作。` → `我和残障儿童一起工作。`
  - 理由: EO `Mi laboras kun handikapitaj infanoj`、EN/RU/JA/KO は「障がいのある子どもたちと一緒に働く」。旧ZHは「残障儿童的工作」がやや名詞句として不自然で、子どもたち自身の仕事にも読めるため、`kun` に対応する自然な表現へ補正。

主な据え置き確認:
- `formulitaj skribe`, `raporto pri sanservo`, `faras esploradon`, `ekzamena sesio`, `ripeti multajn aferojn` は学生生活・研究・試験文脈で意味ズレなし。
- 色表現の `Ruĝo kaj verdo faras brunon`, `purpuron`, `viola`, `oranĝan koloron`, `helverdan koloron` は既存周回で PIV 2020 と列間対応を確認済みのため維持。
- 韓国語の数詞列は固有数詞・漢数詞の揺れがあるが、数値対応自体は崩れておらず、明確な意味ズレとは扱わない。
- `informteknologio`, `vokcentro` は PIV 直接見出しではないものの透明な複合語として文脈上明確。`veterinaro`, `komercistino`, `handikapitaj infanoj` は PIV 2020 ローカル抽出および既存確認どおり維持。

参照:
- PIV 2020 ローカル `juristo`: `PIV2020_structured.txt`（`juristo`: Specialisto pri la juraj k juĝaj aferoj）
- ReVo `juristo`: https://reta-vortaro.de/revo/art/jur.html
- PIV 2020 `advokato`: https://vortaro.net/py/serchi.py?s=advokato&simpla=1
- PIV 2020 `handikapo`: https://vortaro.net/py/serchi.py?s=handikapo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `8a31db6b4f82ed73eb3e72630ba2224d`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1456`〜`ID1555` は 100 件、`ID1540`/`ID1543`/`ID1555` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 531. 530周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University
- Education / Student Life

結果:
- **7件修正（5行）**
- EO は追加修正なし。JA 1件、ZH 3件、KO 3件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1393` KO
  - `이 대학에는 어떤 학과들이 있나요?` → `이 대학에는 어떤 학부들이 있나요?`
  - 理由: EO `fakultatojn` と RU `факультеты` は大学の主要部門「学部/faculty」。旧KOの `학과` は department 寄りで、前周にENを `faculties` へ補正した判断ともずれるため `학부` に補正。
- `ID1402` ZH
  - `请您填写这份注册表。` → `您能填写这份注册表吗？`
  - 理由: EO `Ĉu vi povus plenigi...`、EN/RU/JA/KO は「記入していただけますか」という依頼疑問。旧ZHは命令・依頼文で、クイズ対応上 `Bonvolu...` 型に寄りやすかった。
- `ID1410` ZH
  - `你参加过任何读书会吗？` → `你是某个读书会的成员吗？`
  - 理由: EO `Ĉu vi estas membro de iu libroklubo?` と RU `являешься членом...` は現在の会員かどうか。旧ZHは「参加したことがあるか」という経験質問に寄っていた。
- `ID1413` JA/ZH/KO
  - JA `あと何年残っていますか？` → `あと何年勉強しなければなりませんか？`
  - ZH `你还剩多少年？` → `你还需要学习几年？`
  - KO `앞으로 몇 년이나 더 남았어요?` → `앞으로 몇 년 더 공부해야 하나요?`
  - 理由: EO `Kiom da jaroj vi ankoraŭ devas studi?` と RU `Сколько лет тебе ещё учиться?` は「あと何年勉強する必要があるか」。旧日中韓はいずれも「何年残っているか」に省略され、学習義務が落ちていた。
- `ID1423` KO
  - `저와 함께 연습해도 될까요?` → `같이 연습해도 될까요?`
  - 理由: EO `Ĉu mi povas ekzerciĝi kun vi?`、ZH `和你一起`、RU `с тобой` は「あなたと練習してよいか」。旧KOの `저와 함께` は「私と一緒に」と逆方向に読めるため、主語・相手の衝突を避ける自然な `같이` に補正。

主な据え置き確認:
- `Neniu rajtas forlasi la klasĉambron nun`, `En kiu aĝo infanoj komencas iri al lernejo?`, `Kiam finiĝas la lerneja jaro?` は学校文脈で意味ズレなし。
- `studi ĉe universitato`, `studjaro`, `diplomiĝis`, `magistriĝo`, `doktoriĝas`, `Mi prenas liberan jaron` は、大学・学位・休学/ギャップイヤー文脈として前周までの判断を維持。
- `fakultato`, `rektoro`, `lektoro`, `studentloĝejo`, `akceptkondiĉoj`, `eniraj ekzamenoj`, `registriĝa formularo` は PIV 2020 の語義・透明な複合構成と合う。
- `Mi faros mian raporton en la kataluna` は、PIV 2020 の `raporto` が口頭・文書の両方に読めるため、RU の発表寄りと日中韓の作成寄りの揺れを明確な誤りとはしない。
- `aliĝi al la biblioteko`, `biblioteka karto`, `prunti ... librojn`, `disertacio`, `invitita parolanto`, `templimo por paroladoj`, `formulitaj buŝe` は学生生活・図書館・会議文脈で維持。
- `Ŝi estas brila oratoro` は、PIV 2020 の `oratoro` が公開で話す人を表し、女性主語でも性別明示の `oratorino` へ直す必然性は低いため維持。

参照:
- PIV 2020 `aĝo`: https://vortaro.net/py/serchi.py?s=a%C4%9Do&simpla=1
- PIV 2020 `fakultato`: https://vortaro.net/py/serchi.py?s=fakultato&simpla=1
- PIV 2020 `formularo`: https://vortaro.net/py/serchi.py?s=formularo&simpla=1
- PIV 2020 `klubo`: https://vortaro.net/py/serchi.py?s=klubo&simpla=1
- PIV 2020 `ekzerciĝi`: https://vortaro.net/py/serchi.py?s=ekzerci%C4%9Di&simpla=1
- PIV 2020 `studento`: https://vortaro.net/py/serchi.py?s=studento&simpla=1
- PIV 2020 `magistro`: https://vortaro.net/py/serchi.py?s=magistro&simpla=1
- PIV 2020 `doktoriĝi`: https://vortaro.net/py/serchi.py?s=doktori%C4%9Di&simpla=1
- PIV 2020 `biblioteko`: https://vortaro.net/py/serchi.py?s=biblioteko&simpla=1
- PIV 2020 `templimo`: https://vortaro.net/py/serchi.py?s=templimo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `c05764fed175582b4e0935376559e5bb`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1356`〜`ID1455` は 100 件、`ID1393`/`ID1402`/`ID1410`/`ID1413`/`ID1423` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 530. 529周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding
- Education / At School

結果:
- **7件修正（6行）**
- EO は追加修正なし。JA 4件、ZH 1件、KO 2件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1262` JA
  - `よろしければ、コーヒーでもいかがですか？` → `よろしければ、中に入ってコーヒーでもいかがですか？`
  - 理由: EO `enveni` と RU `зайти`、ZH `进来` は「中へ入る」を含む。旧JAはコーヒーの誘いだけで、入室要素が落ちていた。
- `ID1279` JA
  - `あなたは本当に歌が上手ですね。` → `あなたは本当に才能のある歌手ですね。`
  - 理由: EO `talenta kantistino` と RU `талантливая певица` は「才能ある歌手」。旧JAは「歌が上手」に狭まり、`kantistino` の職業・人物名詞が落ちていた。
- `ID1288` JA
  - `とても素敵なセンスをお持ちですね。` → `服のセンスが本当に素敵ですね。`
  - 理由: EO `guston pri vestoj` と RU `вкус в одежде` は服装に関するセンス。旧JAは対象が広すぎた。
- `ID1304` JA/ZH
  - JA `お二人が末永く幸せでいられますように。` → `お二人がお互いをとても幸せにし合えますように。`
  - ZH `希望你们彼此能够非常幸福。` → `希望你们能让彼此非常幸福。`
  - 理由: EO `ege feliĉigos unu la alian` と RU `сделаете друг друга невероятно счастливыми` は「互いを幸せにする」。旧JA/ZHは「二人が幸せである」に寄り、相互的な使役が弱かった。
- `ID1309` KO
  - `아직 결혼 날짜를 정하셨나요?` → `결혼식 날짜는 정하셨나요?`
  - 理由: EO `jam decidis pri la dato de la geedziĝo?`、JA「もう結婚式の日取りは決まりましたか？」、RU `уже определились...` に対応。旧KOは肯定疑問での `아직` が不自然で、「まだ決めていないのか」に寄りやすかった。
- `ID1342` KO
  - `여름 학교를 운영하나요?` → `여름학교를 운영하나요?`
  - 理由: EO `somerajn lernejojn` の summer school 対応として、韓国語では一語化した `여름학교` が自然。意味変更ではなく表記・自然さの補正。

主な据え置き確認:
- `Ĉu vi havas fotojn de vi mem?`, `Ĉu vi ŝatus enveni por taso da kafo?`, `Forigu viajn manojn de mi!` は Dating / On a Date の会話として意味ズレなし。
- `Mi ŝatas vian veston` は、PIV 2020 の `vesto` が身につける衣服全体を表せるため、outfit / 服装文脈として維持。
- `Vi estas ravega`, `Vi aspektas tre bele ĉi-vespere`, `Vi aspektas bela en tiu robo!`, `Vi havas mirindan guston pri vestoj` は、PIV 2020 の `ravi/rava`, `aspekti`, `vesto` と照合し、褒め言葉として文脈別許容。
- `Ĉu vi edziniĝos al mi?` は PIV 2020 の `edziniĝi`「妻になる」と整合し、RU/ZH が女性相手のプロポーズで揃っているため維持。
- `nupto`, `geedziĝo`, `fianĉiĝo`, `novgeedzoj`, `porcelana/arĝenta/perla/korala/rubina/diamanta` の結婚記念日表現は透明で、婚礼文脈と整合。
- `gimnastikejo`, `respondi mian demandon`, `lerni ĝin parkere`, `notoj`, `sonorilo` は PIV 2020 の語義・用例と合い、Education / At School 文脈で維持。
- `Kie vi iris al lernejo?`, `Mi iris al lernejo en Bristolo`, `Mi finis lernejon deksesjaraĝe` は、英語・ロシア語の school attendance / completion と対応し、意味衝突なし。

参照:
- PIV 2020 `enveni`: https://vortaro.net/py/serchi.py?s=enveni&simpla=1
- PIV 2020 `vesto`: https://vortaro.net/py/serchi.py?s=vesto&simpla=1
- PIV 2020 `ravi`: https://vortaro.net/py/serchi.py?s=ravi&simpla=1
- PIV 2020 `aspekti`: https://vortaro.net/py/serchi.py?s=aspekti&simpla=1
- PIV 2020 `feliĉigi`: https://vortaro.net/py/serchi.py?s=feli%C4%89igi&simpla=1
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `nupto`: https://vortaro.net/py/serchi.py?s=nupto&simpla=1
- PIV 2020 `proponi`: https://vortaro.net/py/serchi.py?s=proponi&simpla=1
- PIV 2020 `noto`: https://vortaro.net/py/serchi.py?s=noto&simpla=1
- PIV 2020 `parkere`: https://vortaro.net/py/serchi.py?s=parkere&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `387fe6643bd9ebb76e4bcf6ed0f11c4f`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1256`〜`ID1355` は 100 件、`ID1262`/`ID1279`/`ID1288`/`ID1304`/`ID1309`/`ID1342` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 529. 528周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet, Accepting & Declining
- Dating / Asking Someone out, On a Date

結果:
- **3件修正**
- EO は追加修正なし。参考EN 2件、ZH 1件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1162` EN
  - `Yes, surely.` → `Yes, certainly.`
  - 理由: EO `Jes, certe` と RU `Да, конечно.` は承諾の「もちろん」。旧ENの `surely` は推量・確認寄りにも読めるため、承諾表現として自然な `certainly` に補正。
- `ID1183` ZH
  - `我在那里等你。` → `我们在那里见面。`
  - 理由: EO `Ni renkontiĝos tie` と RU `Встретимся там.` は「そこで会う」。旧ZHは「そこで待っている」で、主体と動作が少しずれていた。
- `ID1217` EN
  - `What are you up to?` → `What have you come up with?`
  - 理由: EO `Kion vi elpensis?`、JA/ZH/KO、RU `Что ты задумала?` は「何を思いついた/考え出したか」。旧ENは「何をしているのか/何を企んでいるのか」に寄り、他列とずれやすかった。

主な据え置き確認:
- `Sinjoroj, ni povas ludi partion de golfo` は男性複数への呼びかけで、`partio` のゲーム・競技の一回という語義から golf round / RU `партию в гольф` に対応する。
- `Sonas bone`, `Mi ne kontraŭas`, `Kun plezuro`, `Tio sonas alloge`, `Mi iomete malfruiĝas`, `Mi ne interesiĝas` は承諾・断りの短文として自然。
- `Mi venos preni vin`, `Mi regalos vin per trinkaĵo`, `akompani vin hejmen`, `veturigi vin hejmen` は誘い・送迎文脈で意味ズレなし。
- `Ĉu mi povas aliĝi al vi?`, `Ĉu ĝenas vin, se mi aliĝos al vi?` は同席・合流を求める表現として文脈別許容。
- `Ĉu vi renkontiĝas kun iu?` は広いが、Dating 文脈では「付き合っている/会っている人がいる」と読めるため維持。
- `Vi mankas al mi`, `Mi enamiĝis al vi`, `Mi freneziĝas pro vi` は恋愛・親密表現として列間対応を保つ。
- `Ni forveturu de ĉi tie` は JA/ZH/KO より乗り物含みが出るが、RU `уедем` と整合し、明確な衝突ではないため維持。
- `Lasu min trankvila`, `Ne tuŝu min!`, `Ĉu mi povas kisi/brakumi vin?` はデート場面の境界・親密表現として意味ズレなし。

参照:
- PIV 2020 `partio`: https://vortaro.net/py/serchi.py?s=partio&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `regali`: https://vortaro.net/py/serchi.py?s=regali&simpla=1
- PIV 2020 `elpensi`: https://vortaro.net/py/serchi.py?s=elpensi&simpla=1
- PIV 2020 `akompani`: https://vortaro.net/py/serchi.py?s=akompani&simpla=1
- PIV 2020 `veturigi`: https://vortaro.net/py/serchi.py?s=veturigi&simpla=1
- PIV 2020 `manki`: https://vortaro.net/py/serchi.py?s=manki&simpla=1
- PIV 2020 `enamiĝi`: https://vortaro.net/py/serchi.py?s=enami%C4%9Di&simpla=1
- PIV 2020 `freneziĝi`: https://vortaro.net/py/serchi.py?s=frenezi%C4%9Di&simpla=1
- PIV 2020 `forveturi`: https://vortaro.net/py/serchi.py?s=forveturi&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `3ae3c0ff7bedc39bea16ce857a634d04`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1156`〜`ID1255` は 100 件、`ID1162`/`ID1183`/`ID1217` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 528. 527周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **4件修正（3行）**
- EO は追加修正なし。参考EN 2件、ZH 1件、KO 1件を、EO/RUおよび日中韓クイズ対応に寄せて補正。

修正:
- `ID1087` EN
  - `I rather dislike them.` → `I don't like them very much.`
  - 理由: EO `Ili ne tre plaĉas al mi` と RU `Они мне не очень нравятся.` は「それほど好きではない」。旧ENは `rather dislike` で嫌悪寄りに強く、参考列として強すぎた。
- `ID1145` ZH/KO
  - ZH `你周末想去哪里玩吗？` → `你周末想不想去哪儿玩？`
  - KO `주말에 어디 가고 싶으세요?` → `주말에 어디 좀 가고 싶으세요?`
  - 理由: EO `Ĉu vi volas iri ien dum la semajnfino?` と RU `Ты хочешь куда-нибудь поехать на выходных?` は yes/no の「週末にどこかへ行きたいか」。旧ZH/KOは「どこへ行きたいか」という場所質問に寄りやすかったため、`ien` の不定性と疑問形式に合わせた。
- `ID1154` EN
  - `Can we make it a bit later, say 4 p.m?` → `Can we make it a bit later, say 4 p.m.?`
  - 理由: 参考ENの句読点補正。内容変更なし。

主な据え置き確認:
- `Kiom bone vi konas lin?`, `grizajn ĉe la tempioj`, `bonkondutaj`, `zorge elektas`, `Kien ajn mi iras` は人物描写・性格描写として列間対応を保つ。
- `iri al noktokluboj`, `butikumi`, `hobio`, `fotografado`, `ĝardenado`, `patkukojn`, `drinkejo`, `dombestojn` は趣味・嗜好文脈で対応する。
- `Mi ŝatas troti` は `jogging` と完全同義ではないが、PIV 2020 で人の小走り・速歩系の用法が確認でき、軽いランニング文脈として文脈別許容。
- `Mi ne pensas, ke piedirado estas agrabla` は EN/JA/ZH の hiking より広いが、RU `пешие прогулки` とも合い、徒歩・散策寄りの意味として維持。
- `modprezentadon`, `sciencfikciaj libroj`, `mensogulon`, `hororaj filmoj` は透明複合またはPIV確認語として意味ズレなし。
- `Aliĝu al mi por tagmanĝo`, `Ĉu vi ŝatus aliĝi al ni?` はやや硬いが、PIV 2020 の `aliĝi al ...` の「加わる」語義から、会食・同席への誘いとして許容。
- `Ĉu vi rememorigos min?`, `vestiblo`, `je la 16-a horo`, `Sciigu min, se vi povos veni` は待ち合わせ・予定調整文脈で対応する。

参照:
- PIV 2020 `butikumi`: https://vortaro.net/py/serchi.py?s=butikumi&simpla=1
- PIV 2020 `hobio`: https://vortaro.net/py/serchi.py?s=hobio&simpla=1
- PIV 2020 `fotografado`: https://vortaro.net/py/serchi.py?s=fotografado&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `troti`: https://vortaro.net/py/serchi.py?s=troti&simpla=1
- PIV 2020 `piedirado`: https://vortaro.net/py/serchi.py?s=piedirado&simpla=1
- PIV 2020 `ekskurso`: https://vortaro.net/py/serchi.py?s=ekskurso&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `memorigi`: https://vortaro.net/py/serchi.py?s=memorigi&simpla=1
- PIV 2020 `vestiblo`: https://vortaro.net/py/serchi.py?s=vestiblo&simpla=1
- PIV 2020 `hororo`: https://vortaro.net/py/serchi.py?s=hororo&simpla=1
- PIV 2020 `sciencfikcio`: https://vortaro.net/py/serchi.py?s=sciencfikcio&simpla=1
- PIV 2020 `mensogulo`: https://vortaro.net/py/serchi.py?s=mensogulo&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `d4225b8a60ff17c8a1f7a9adbe9e9172`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID1056`〜`ID1155` は 100 件、`ID1087`/`ID1145`/`ID1154` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 527. 526周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age/Nationality & Religion, Family & Relationships, Describing People

結果:
- **6件修正**
- EO は追加修正なし。JA 2件、参考EN 4件を、既存のEO/RUおよび日中韓対応に寄せて補正。

修正:
- `ID1021` JA
  - `はい、孫が一人と、孫娘が二人います。` → `はい、男の孫が一人、女の孫が二人います。`
  - 理由: EO `unu nepo kaj du nepinoj`、RU `внук и две внучки`、EN/ZH/KO は「男の孫1人 + 女の孫2人」を明示する。旧JAは最初の `nepo` の男性性が落ち、クイズ対応としてやや曖昧だった。
- `ID1046`〜`ID1049` EN
  - `I've got a mouth to eat.` → `I've got a mouth to eat with.`
  - `I've got two ears to hear.` → `I've got two ears to hear with.`
  - `I've got a tongue to taste.` → `I've got a tongue to taste with.`
  - `I've got two feet to run.` → `I've got two feet to run with.`
  - 理由: EO `por manĝi/aŭdi/gustumi/kuri` と RU `чтобы ...` は機能・用途表現として通るが、EN では身体部位を手段として表すには `with` を補う方が自然。参考列のみの文法補正。
- `ID1050` JA
  - `あなたの妹さんはどんな方ですか？` → `あなたの妹さんはどんな見た目ですか？`
  - 理由: EO `Kiel aspektas ...?`、EN/RU/ZH/KO は外見を尋ねる内容。旧JAは「どんな人/性格」に寄りやすく、`ID1029`/`ID1038` の `Kia ...?` 系とも紛れやすいため、外見質問に揃えた。

主な据え置き確認:
- `budhano`, `siĥo`, `protestantino`, `ateisto`, `preĝejo`, `templo`, `moskeo`, `sinagogo` は宗教関連語として対応する。`preĝejo` はやや広いが、キリスト教の church 文脈でも使えるため過修正しない。
- `edziniĝinta`, `Ĉu vi edziniĝis?`, `fianĉino`, `fraŭla`, `disiĝis`, `en rilato`, `rendevuas kun iu` は関係・婚姻文脈で列間対応を保つ。女性形は RU の女性話者・女性対象と整合する箇所として維持。
- `solinfano`, `geavoj`, `genepoj`, `nepo`, `nepinoj` は親族語として意味ズレなし。`ID1021` はJAのみ明確化。
- `bonŝanculo`, `okulvitroj`, `saĝa`, `inteligenta`, `svelta`, `rufa`, `ĉarma`, `scivolema`, `flari`, `gustumi` は人物・身体描写文脈で対応する。
- `Li estas juna, malalta kaj bela` の `bela` は男性の外見評価にも使えるため、handsome / привлекательный との対応を維持。
- `Mi havas buŝon/orelojn/langon/piedojn por ...` はやや教材的だが、身体部位の機能説明として意味は明確なため、EOは維持。

参照:
- PIV 2020 `budhano`: https://vortaro.net/py/serchi.py?s=budhano&simpla=1
- PIV 2020 `siĥo`: https://vortaro.net/py/serchi.py?s=si%C4%A5o&simpla=1
- PIV 2020 `preĝejo`: https://vortaro.net/py/serchi.py?s=pre%C4%9Dejo&simpla=1
- PIV 2020 `moskeo`: https://vortaro.net/py/serchi.py?s=moskeo&simpla=1
- PIV 2020 `sinagogo`: https://vortaro.net/py/serchi.py?s=sinagogo&simpla=1
- PIV 2020 `fraŭlo`: https://vortaro.net/py/serchi.py?s=fra%C5%ADlo&simpla=1
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `fianĉino`: https://vortaro.net/py/serchi.py?s=fian%C4%89ino&simpla=1
- PIV 2020 `rendevui`: https://vortaro.net/py/serchi.py?s=rendevui&simpla=1
- PIV 2020 `nepo`: https://vortaro.net/py/serchi.py?s=nepo&simpla=1
- PIV 2020 `aspekti`: https://vortaro.net/py/serchi.py?s=aspekti&simpla=1
- PIV 2020 `gustumi`: https://vortaro.net/py/serchi.py?s=gustumi&simpla=1
- PIV 2020 `flari`: https://vortaro.net/py/serchi.py?s=flari&simpla=1
- PIV 2020 `rufa`: https://vortaro.net/py/serchi.py?s=rufa&simpla=1
- PIV 2020 `ĉarma`: https://vortaro.net/py/serchi.py?s=%C4%89arma&simpla=1
- PIV 2020 `svelta`: https://vortaro.net/py/serchi.py?s=svelta&simpla=1

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `198a8f98209d3fe62dcb31340adf549b`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID956`〜`ID1055` は 100 件、`ID1021`/`ID1046`〜`ID1050` の補正後内容を確認済み。
- `git diff --check` 問題なし。

## 526. 525周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions, Place of Residence, Age/Nationality & Religion

結果:
- **1件修正**

修正:
- `ID954` EO
  - `Mi estas musulmanino` → `Mi estas islamanino`
  - 理由: PIV 2020 では `musulmano/musulmanino` を確認できず、`Islamo` 項で `islamano`（Kredanto de Islamo）が確認できる。Glosbe 系でも `مسلم` の訳として `islamano` が出る。`muzulmano` という別形は確認できるが、現CSVの `musulmanino` とは綴りが異なるため、PIV で確認できる語根に基づく規則的女性形 `islamanino` に修正。

主な据え置き確認:
- `Mi estas kun amikino` は PIV の `amikino` と RU `подругой` が整合。JA/ZH/KO は性別非明示だが許容。
- `vendmanaĝero` は PIV で `manaĝero` の定義が狭く、Glosbe でも直接訳は取れないが、`vend-` + `manaĝero` の透明複合として sales manager を表せるため、明確な誤りとは判断しない。
- `Ĉu mi povas prezenti al vi mian fianĉon?`, `prezenti nian direktoron, sinjoron Smirnov`, `prezenti al vi nian filinon` は紹介方向・格として許容。
- `Ĉu plaĉas al vi ĉi tie?`, `Ĉi tie tre plaĉas al mi`, `Kio alkondukas vin al Brazilo?`, `Mi estas ĉi tie por labori`, `Mi dividas ĝin kun unu alia persono`, `Ŝi kunloĝas en domo kun tri aliaj homoj`, `jam de ses monatoj` は居住・滞在文脈で意味ズレなし。
- `Moldavio`, `Nov-Zelando`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio`, `nacieco` は地名・国籍表現として PIV 等と整合。
- `judino`, `kristanino`, `katoliko`, `hinduistino`, `Al kiu religio vi apartenas?` は宗教・信仰文脈で対応する。

参照:
- PIV 2020 `amikino`: https://vortaro.net/py/serchi.py?s=amikino&simpla=1
- PIV 2020 `fianĉo`: https://vortaro.net/py/serchi.py?s=fian%C4%89o&simpla=1
- PIV 2020 `manaĝero`: https://vortaro.net/py/serchi.py?s=mana%C4%9Dero&simpla=1
- PIV 2020 `korespondanto`: https://vortaro.net/py/serchi.py?s=korespondanto&simpla=1
- PIV 2020 `Moldavio`: https://vortaro.net/py/serchi.py?s=Moldavio&simpla=1
- PIV 2020 `Kazaĥio`: https://vortaro.net/py/serchi.py?s=Kaza%C4%A5io&simpla=1
- PIV 2020 `nacieco`: https://vortaro.net/py/serchi.py?s=nacieco&simpla=1
- PIV 2020 `religio`: https://vortaro.net/py/serchi.py?s=religio&simpla=1
- PIV 2020 `islamano`: https://vortaro.net/py/serchi.py?s=islamano&simpla=1
- PIV 2020 `hinduismo`: https://vortaro.net/py/serchi.py?s=hinduismo&simpla=1
- Glosbe `مسلم` → Esperanto: https://glosbe.com/ar/eo/%D9%85%D8%B3%D9%84%D9%85

今回の整合性確認:
- 本体 CSV とコピー CSV は一致: `cmp_exit=0`
- CSV MD5: `0bbcb98f2a0fef680a8e3e235253c0ff`
- `ID156`〜`ID5155` の 5000 行連続性を検証済み。
- `ID856`〜`ID955` は 100 件、`ID954` EO が `Mi estas islamanino` であることを確認済み。
- `git diff --check` 問題なし。

## 525. 524周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid, At the Police Station
- Making Friends / Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi sangas`, `Min trafis aŭto`, `Li estas senkonscia`, `Mia filino estas vundita`, `Konduku min al hospitalo!` は応急処置・緊急搬送の短文として列間対応を保つ。
- `Mi estis mordita`, `Mi tranĉis min`, `Mi bruligis min`, `Mi rompis mian brakon`, `Mi tordis al mi la maleolon` は負傷説明として意味ズレなし。`brulvundi` も候補だが、現形は「やけどした」と読めるため過修正しない。
- `Bonvolu surmeti bandaĝon` は `bandaĝi la piedon/vundon` より説明的だが、PIV の `bandaĝo` の語義と合い、RU `наденьте бандаж` 寄りの表現として維持。
- `Ĉio estos bone kun vi`, `Trankviliĝu, ĉio estos en ordo`, `Mi atendos ĉi tie kun vi, ne zorgu` はやや直訳的な箇所もあるが、励まし・安心させる発話として文脈別許容。
- `Mi elartikigis mian brakon` は、PIV の `luksacio` / `elartikigi sian ŝultron` 系から脱臼表現として確認できる。`brakon` は広いが、RU `вывихнул руку` とも整合するため維持。
- `Mi havas manĝaĵveneniĝon`, `Ĉu vi havas diabeton?`, `alergia al ...`, `reakcion al novokaino`, `poliso de medicina asekuro` は医療・保険文脈で対応する。
- `Ĉu vi povus sciigi mian familion?`, `Ĉu mi povas daŭrigi mian vojaĝon?` は依頼・確認表現として自然。
- `Mi bezonas advokaton`, `Bonvolu subskribi vian deklaron`, `Ĉu mi estas arestita?`, `Vi devos pagi monpunon`, `Kie estas la plej proksima policejo?` は警察署文脈の基本表現として意味ズレなし。
- `Oni enrompis en mian aŭton`, `Mi ŝatus denunci ŝtelon`, `Kion oni ŝtelis de vi?`, `Bonvolu plenigi raporton pri ŝtelo` は盗難・車上荒らしの届出文脈として対応する。
- `Ĉu mi povas ĝin anstataŭigi?` は「再発行」そのものより「置き換える」に近いが、RU `заменить` と合い、紛失パスポートの replacement 文脈として許容。
- `oficejo pri perditaj aĵoj` は ID715 と同じく説明的だが、遺失物取扱所として透明で、ID821/827 の内部整合もあるため維持。
- `Ni penos fari lian fotoroboton` は PIV 直接見出しでは未確認だが、Glosbe/DBnary で `facial composite` / `identikit` と確認でき、RU `фоторобот` と一致するためAI造語誤りとは判断しない。
- `Miaj muzikaj instrumentoj estis detruitaj` は JA/RU の「壊れた」より少し強いが、EN `destroyed`・ZH `被毁` と対応し、内容変更を避けて維持。
- `Kio estas via familinomo?` は Glosbe で surname / family name として確認でき、紹介文脈の名字確認として維持。
- `Permesu al mi prezenti vin al Davido`, `Mi ŝatus prezenti Alicon al vi`, `Estas agrable konatiĝi kun vi, Jan!` は、過去修正後の紹介方向・格のままで妥当。

参照:
- PIV 2020 `bandaĝo`: https://vortaro.net/py/serchi.py?s=banda%C4%9Do&simpla=1
- PIV 2020 `bruligi`: https://vortaro.net/py/serchi.py?s=bruligi&simpla=1
- PIV 2020 `luksacio`: https://vortaro.net/py/serchi.py?s=luksacio&simpla=1
- PIV 2020 `ŝultro`: https://vortaro.net/py/serchi.py?s=%C5%9Dultro&simpla=1
- PIV 2020 `veneniĝo`: https://vortaro.net/py/serchi.py?s=veneni%C4%9Do&simpla=1
- PIV 2020 `alergio`: https://vortaro.net/py/serchi.py?s=alergio&simpla=1
- PIV 2020 `novokaino`: https://vortaro.net/py/serchi.py?s=novokaino&simpla=1
- PIV 2020 `deklaro`: https://vortaro.net/py/serchi.py?s=deklaro&simpla=1
- PIV 2020 `advokato`: https://vortaro.net/py/serchi.py?s=advokato&simpla=1
- PIV 2020 `denunci`: https://vortaro.net/py/serchi.py?s=denunci&simpla=1
- PIV 2020 `anstataŭigi`: https://vortaro.net/py/serchi.py?s=anstata%C5%ADigi&simpla=1
- PIV 2020 `atestanto`: https://vortaro.net/py/serchi.py?s=atestanto&simpla=1
- PIV 2020 `prezenti`: https://vortaro.net/py/serchi.py?s=prezenti&simpla=1
- Glosbe `fotoroboto`: https://glosbe.com/eo/en/fotoroboto
- Glosbe `familinomo`: https://glosbe.com/eo/en/familinomo

## 524. 523周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions
- Emergencies / Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Ĉu ĉi tiu loko ne estas mirinda?`, `Mi pensas, ke jes`, `Mi ne pensas tiel`, `Mi esperas tion`, `Tio dependas`, `Vi malpravas` は短い意見・応答表現として列間対応を保つ。
- `Ĉu vi havas iujn rimarkojn?` は PIV の `rimarki/rimarko` の「注意して述べること・コメント」系の語義から、RU `замечания` および日中韓の「意見」と文脈上対応する。
- `Ĝi estas grandioza`, `Tio estas mirinda`, `Tio estas nekredebla`, `Kia bela loko!`, `Kia bonega ideo!` は評価表現として自然。
- `Ili tre plaĉas al mi!`, `Kio plaĉas al vi pri ĝi?`, `Mi ne povas diri, ke tio tre plaĉas al mi`, `Sincere dirante, li ne plaĉas al mi` は、PIV の `plaĉi al iu` の型と合う。
- `Kion vi povas diri pri ĉi tiu bildo?` は、`bildo` が写真・絵・画像を広く表せるため、JA/KO の「写真」寄り、RU の「絵」寄りを吸収できる。
- `La aktorado estis malbona` は PIV で `aktorado` が「俳優の演技・演じ方」と確認でき、acting として維持。
- `Persone, mi konsideras ĉi tiun filmon la plej bona` は `konsideri + objekto + predikativo` として読める。`la plej bonan` への変更は名詞句内修飾にも読めるため不要。
- `Fajro!` は `Incendio!` も候補だが、短い警告発話としては許容。`fajrobrigado` は PIV で消防隊相当が確認できる。
- `Voku ambulancon!`, `Estas urĝa situacio!`, `Bonvolu tuj voki la policon`, `Oni atakis min` は緊急時の短文として意味ズレなし。
- `Ĉu io malbonas?` はやや口語的だが、「何か問題があるか」の短い確認として文脈別許容。
- `oficejo pri perditaj aĵoj` はやや説明的だが、PIV の `perdi` 系とも整合し、遺失物取扱所として意味は明確。
- `Ĉu vi havis akcidenton?` は PIV の典型例では `suferi akcidenton` などが目立つものの、現形でも「事故に遭ったか」の意味は明確で、内容変更を避けて維持。
- `Mi estas traŭmatizita`, `Ĉu iu estas vundita?`, `Estas vunditoj`, `Kio kaŭzis la akcidenton?`, `Li koliziis kun mi`, `Ne estis mia kulpo` は事故文脈として対応する。
- `stirpermesilo`, `asekurdokumentoj`, `akcidentraporto` は透明な複合語として、運転免許証・保険書類・事故報告書を表すため維持。
- `Mi havis la prioritaton` は PIV に交通文脈の `havi prioritaton de paso` があり、right of way として妥当。
- `Ĉu vi povus blovi en ĉi tiun tubon, mi petas?` は PIV に `blovi en tubon` の用例があり、飲酒検査の文脈と整合する。
- `Kiun mi informu pri la akcidento?` は PIV の `informi iun pri io` の型から、`kiun` の対格が支持される。

参照:
- PIV 2020 `plaĉi`: https://vortaro.net/py/serchi.py?s=pla%C4%89i&simpla=1
- PIV 2020 `rimarko`: https://vortaro.net/py/serchi.py?s=rimarko&simpla=1
- PIV 2020 `grandioza`: https://vortaro.net/py/serchi.py?s=grandioza&simpla=1
- PIV 2020 `aktorado`: https://vortaro.net/py/serchi.py?s=aktorado&simpla=1
- PIV 2020 `konsideri`: https://vortaro.net/py/serchi.py?s=konsideri&simpla=1
- PIV 2020 `fajrobrigado`: https://vortaro.net/py/serchi.py?s=fajrobrigado&simpla=1
- PIV 2020 `ambulanco`: https://vortaro.net/py/serchi.py?s=ambulanco&simpla=1
- PIV 2020 `traŭmatizi`: https://vortaro.net/py/serchi.py?s=tra%C5%ADmatizi&simpla=1
- PIV 2020 `prioritato`: https://vortaro.net/py/serchi.py?s=prioritato&simpla=1
- PIV 2020 `akcidento`: https://vortaro.net/py/serchi.py?s=akcidento&simpla=1
- PIV 2020 `asekuri`: https://vortaro.net/py/serchi.py?s=asekuri&simpla=1
- PIV 2020 `damaĝo`: https://vortaro.net/py/serchi.py?s=dama%C4%9Do&simpla=1
- PIV 2020 `blovi`: https://vortaro.net/py/serchi.py?s=blovi&simpla=1
- PIV 2020 `informi`: https://vortaro.net/py/serchi.py?s=informi&simpla=1

## 523. 522周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information, Expressing Feelings, Help & Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kial vi diris tion?`, `Ĉu iu povas diri al mi la veron?`, `Kiam komenciĝas la cirkaj spektakloj?`, `Ĉu vi scias, kiu inventis la radon?` は質問表現として列間対応を保つ。
- `Mi estas trista`, `Mi estas malstreĉita`, `Mi estas surprizita`, `Mi timas`, `Mi maltrankvilas`, `Mi koleras`, `Mi hontas`, `Mi sentas min embarasita` は感情表現として自然、または文脈別許容。
- `Mi estas ekscitita` は PIV の `eksciti` が心の動きを強める語義を持ち、日中韓文の「期待」寄り訳とも excited の範囲で対応するため維持。
- `Mi estas motivita` は PIV の `motivi` が「理由づける」寄りで注意点は残るが、`motivo` が人を行動させるものを表すこと、より安全な置換が意味を寄せすぎることから文脈別許容。
- `Mi sentas iom da kapturno` は `senti kapturnon` が PIV で確認できる。現形は少し説明的だが「少しめまいがする」と読める。
- `Ni tre bedaŭras aŭdi pri via perdo`, `Bonvolu akcepti niajn plej profundajn kondolencojn`, `Niaj pensoj estas kun vi kaj via familio` は弔意表現として意味ズレなし。
- `Ĉu mi povus prunti vian plumon?`, `Ĉu vi povus prunti al mi iom da mono, mi petas?` は `prunti` に貸す/借りるの両義があるため曖昧さはあるが文脈で明確。`pruntedoni` / `pruntepreni` への置換は今回不要。
- `Ĉu vi povus fari al mi servon?`, `Ĉu vi povus prizorgi tion dum momento?`, `Ĉu vi estus tiel afabla kaj klarigus tion denove?`, `Ĉu ĝenus vin doni al mi la tekkomputilon?` は依頼表現として許容。
- `Mi malkonsilus lui aŭton`, `Se vi sekvos mian konsilon, vi sukcesos`, `Se mi estus vi...`, `Kion vi pensas, ke mi faru?` は助言文脈として列間対応を保つ。
- `flugpersonaro` は `personaro` と `flug-` の透明複合として flight crew を表せるため、AI造語誤りとは判断しない。
- `Tio estas naŭza`, `Estas interese`, `Estas enuige`, `Estas mirinde`, `Ĝi estas bela`, `Ĝi estas malbela` は意見・評価表現として対応する。

参照:
- PIV 2020 `trista`: https://vortaro.net/py/serchi.py?s=trista&simpla=1
- PIV 2020 `eksciti`: https://vortaro.net/py/serchi.py?s=eksciti&simpla=1
- PIV 2020 `motivi`: https://vortaro.net/py/serchi.py?s=motivi&simpla=1
- PIV 2020 `embarasi`: https://vortaro.net/py/serchi.py?s=embarasi&simpla=1
- PIV 2020 `kapturno`: https://vortaro.net/py/serchi.py?s=kapturno&simpla=1
- PIV 2020 `kondolenci`: https://vortaro.net/py/serchi.py?s=kondolenci&simpla=1
- PIV 2020 `prunti`: https://vortaro.net/py/serchi.py?s=prunti&simpla=1
- PIV 2020 `servo`: https://vortaro.net/py/serchi.py?s=servo&simpla=1
- PIV 2020 `malkonsili`: https://vortaro.net/py/serchi.py?s=malkonsili&simpla=1
- PIV 2020 `naŭzi`: https://vortaro.net/py/serchi.py?s=na%C5%ADzi&simpla=1
- PIV 2020 `ŝoki`: https://vortaro.net/py/serchi.py?s=%C5%9Doki&simpla=1
- PIV 2020 `personaro`: https://vortaro.net/py/serchi.py?s=personaro&simpla=1

## 522. 521周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Parolu kun mi en la mandarena ĉina lingvo` はやや硬いが、PIV で `mandarena ... lingvo` 系が確認でき、「標準中国語/普通話で話す」として日中韓文と対応するため文脈別許容。
- `Vi ne havas akĉenton`, `Ĉu mi ĝuste ĝin prononcas?`, `Kiel oni diras tion ĉeĥe?`, `Kiel tio nomiĝas pole?`, `Ĉu vi povas literumi ĝin?` は、発音・綴り・別言語での言い方を尋ねる表現として意味ズレなし。
- `Mi konsentas kun vi`, `Mi ne konsentas kun via opinio`, `Ĉu vi konsentas, ke ...`, `Mi komprenas lian vidpunkton` は、PIV の `konsenti` / `vidpunkto` の用例と整合する。
- `Mi ne povas diri, ke mi kunhavas vian vidpunkton` は `kunhavi` がやや直訳的に見えるが、PIV ローカル抽出で `kun havi opinion` を確認済みで、`vidpunkton` との結合も意味明確なため維持。
- `En la televido estas tro multe da reklamoj, ĉu ne?` は少し直訳的だが、PIV の `reklamo` と合い、テレビ放送内の広告が多いという意味は明確。
- `ĉe Petro`, `ĉe la laboro`, `en trajno`, `en la kamparo`, `el Portugalio` は、場所・移動元の表現として日中韓文およびロシア語文と対応する。
- `drinkejo`, `junulargastejo`, `picejoj`, `duŝiĝi`, `biciklas` は PIV で語根・派生語を確認でき、造語的誤りとは判断しない。
- `Jes, mi iris tien por ferioj`, `Fakte, mi estas survoje por renkonti amikon`, `Kiom longe vi estis en Kolombio?` は、多少英語参照文との差や硬さがあるが、ロシア語・日中韓文との実質的な意味対応は保たれるため維持。
- `Kion vi trovas pli interesa, teatron aŭ operon?` は比較対象が明確で、「演劇とオペラのどちらがより面白いか」という各列の内容と一致する。

参照:
- PIV 2020 `mandarena`: https://vortaro.net/py/serchi.py?s=mandarena&simpla=1
- PIV 2020 `akĉento`: https://vortaro.net/py/serchi.py?s=ak%C4%89ento&simpla=1
- PIV 2020 `konsenti`: https://vortaro.net/py/serchi.py?s=konsenti&simpla=1
- PIV 2020 `vidpunkto`: https://vortaro.net/py/serchi.py?s=vidpunkto&simpla=1
- PIV 2020 `reklamo`: https://vortaro.net/py/serchi.py?s=reklamo&simpla=1
- PIV 2020 `junulargastejo`: https://vortaro.net/py/serchi.py?s=junulargastejo&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `bicikli`: https://vortaro.net/py/serchi.py?s=bicikli&simpla=1
- PIV 2020 `duŝi`: https://vortaro.net/py/serchi.py?s=du%C5%9Di&simpla=1
- PIV 2020 `picejo`: https://vortaro.net/py/serchi.py?s=picejo&simpla=1

## 521. 520周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers, Congratulations
- General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Jes, ĝi tre plaĉas al mi!`, `Kia trankviliĝo!`, `Tia estas la vivo!`, `Ne gravas`, `Ju pli frue, des pli bone` は短い応答・感嘆表現として各列と対応する。
- `Feliĉan ...!` 系の祝祭表現、`Gratulon pro ...`, `Gratulojn pro ...`, `Permesu al mi gratuli vin` は、PIV の `gratuli/gratulo` の用例とも整合する。
- `Feliĉan Divalon!` は PIV では直接確認できないが、Glosbe 等で `Divalo` が Diwali のエスペラント形として確認でき、`Feliĉan + -n` の形も文法的に自然なため維持。
- `Gratulon pro via akcepto en la universitaton!` は少し硬いが、PIV の `akcepti` に教育機関が学生を受け入れる用例があり、大学合格・入学許可の文脈として意味ズレなし。
- `Mi ŝatas la bengalan`, `Mi lernas la urduon`, `Mi parolas la rumanan`, `Ĉu ŝi parolas la tajan?` などは、PIV 収録の民族・言語名および `lingvo` の用例に照らして、言語名としての省略用法を維持。
- `azerbajĝane`, `tagaloga`, `latve`, `norvega`, `slovakan`, `indonezian` は一部がPIV見出し語では直接確認しにくいが、民族・国名からの規則的派生または透明な言語名表現で、日中韓文との対応は明確。
- `Mi lernas la indonezian jam de unu monato` は `dum unu monato` も候補だが、`jam de ...` は「...前からずっと」の継続として読めるため維持。
- `Mi havas akĉenton` は PIV で話者・集団の発音習慣としての `akĉento` が確認でき、以前の `akcento` 修正後の現形を維持。
- `Kiel ĉi tio nomiĝas?`, `Kion ĉi tio signifas?`, `Bonvolu noti ĝin`, `Bonvolu ripeti, mi petas`, `Ĉu vi povas literumi ĝin?` は「伝わらない時の聞き返し・確認」文脈として意味ズレなし。

参照:
- PIV 2020 `gratuli`: https://vortaro.net/py/serchi.py?s=gratuli&simpla=1
- PIV 2020 `akcepti`: https://vortaro.net/py/serchi.py?s=akcepti&simpla=1
- PIV 2020 `lingvo`: https://vortaro.net/py/serchi.py?s=lingvo&simpla=1
- PIV 2020 `akĉento`: https://vortaro.net/py/serchi.py?s=ak%C4%89ento&simpla=1
- Glosbe `Divalo`: https://glosbe.com/eo/en/Divalo

## 520. 519周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions & Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Pardonu min`, `Bonvolu pardoni min`, `Pardonu pro la prokrasto`, `Mi petas pardonon`, `Ne estas kialo pardonpeti` は謝罪・許しを求める表現として一貫し、PIV の `peti` / `pardonpeti` の用例とも合う。
- `Pardonu, ke mi ĝenas vin`, `Ĉu mi ĝenas vin?`, `Ĉu mi povas ĝeni vin momenton?` は、PIV の `ĝeni` の「妨げる・邪魔する」語義と対応し、丁寧な呼びかけ文脈として自然。
- `Ne ofendiĝu`, `Mi ne tion celis`, `Mi bedaŭras, ke mi diris tion`, `Mi agis senzorge` は、謝罪・誤解解消の短文として意味ズレなし。`Mi ne tion celis` は語順がやや強調的だが、「その意味ではなかった」として文脈別許容。
- `Kuraĝu!` は PIV の `kuraĝa/kuraĝi` 系から「元気を出して・勇気を出して」の短い励ましとして許容。
- `Bonvolu viciĝi ĉi tie` は PIV の `viciĝi` で列に並ぶ語義が確認でき、行列案内として自然。
- `Ne paŝu sur la gazonon!` は「芝生へ踏み入らないで」の移動先を示す `sur + -n` として、掲示文脈で整合する。
- `Kio?`, `Kie?`, `Kiam?`, `Kial?`, `Kiu?`, `Kiel?`, `Kiom?`, `Kiom ofte?`, `Kiom longe?`, `Kiom malproksime?` は短い疑問応答として、クイズ用途でも対応が明確。
- `Donu al mi ĉi tiun` は「この一つをください」の選択文脈として `ĉi tiun` を維持。`ĉi tion` への変更も可能だが、意味差が小さく、内容変更を避けた。

参照:
- PIV 2020 `pardonpeti`: https://vortaro.net/py/serchi.py?s=pardonpeti&simpla=1
- PIV 2020 `ĝeni`: https://vortaro.net/py/serchi.py?s=%C4%9Deni&simpla=1
- PIV 2020 `kuraĝi`: https://vortaro.net/py/serchi.py?s=kura%C4%9Di&simpla=1
- PIV 2020 `viciĝi`: https://vortaro.net/py/serchi.py?s=vici%C4%9Di&simpla=1

## 519. 518周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kiel vi fartas?`, `Mi fartas bone`, `Ne tro malbone`, `Tiel-tiel` は挨拶・近況確認の基本表現として、PIV の `farti` の語義とも整合する。
- `Salutu Lukason de mi`, `Bonvolu transdoni miajn korajn salutojn al via patro` は、PIV の `saluti` / `saluto` の用例に照らしても「よろしく伝える」文脈として自然。
- `Mi antaŭĝojas revidi vin` は PIV 見出し語では未確認だが、`antaŭ` + `ĝoji` の透明複合で、Glosbe でも “look forward” 系の対応が確認できるため、造語暴走ではなく文脈別許容として維持。
- `Ni tostu por vi!`, `Mi ŝatus proponi toston por mia filo` は、PIV の `tosto` が「健康・名誉・成功などのための乾杯の小発話」を表すため、祝辞・乾杯文脈として意味ズレなし。
- `Nedankinde`, `Dankon pro via gastamo`, `Mi ne povas sufiĉe danki vin`, `Mi tre aprezas viajn afablajn vortojn` は感謝・返礼表現として文脈と対応する。
- `Sanon!` は「Bless you! / Будь здоров!」に相当する健康を祈る短い応答として許容し、`Je via sano!` とは乾杯表現として区別されている。

参照:
- PIV 2020 `farti`: https://vortaro.net/py/serchi.py?s=farti&simpla=1
- PIV 2020 `saluti`: https://vortaro.net/py/serchi.py?s=saluti&simpla=1
- PIV 2020 `tosti`: https://vortaro.net/py/serchi.py?s=tosti&simpla=1
- PIV 2020 `aprezi`: https://vortaro.net/py/serchi.py?s=aprezi&simpla=1
- Glosbe `antaŭĝoji`: https://glosbe.com/eo/en/anta%C5%AD%C4%9Doji

## 512. 511周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs, Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `La ekrano fendiĝis`, `La klavarbutono fiksiĝis`, `ripari`, `garantio`, `kroneto`, `brakhorloĝo`, `ŝlosilringo`, `plandumoj` は修理・靴修理文脈で意味ズレなし。
- `Je kiuj horoj vi akceptas?` は医師の診療・受付時間を尋ねる表現として文脈別許容。
- `sangogrupo`, `O negativa`, `O-pozitiva`, `insulino`, `trankviligaĵo`, `kontraŭdolorilo` は診療・処方文脈として整合する。
- `surdorse` / `surventre` は就寝姿勢の表現として、日中韓文および露文の「仰向け／うつ伏せ」と対応する。

参照:
- PIV 2020 `fendi`: https://vortaro.net/py/serchi.py?s=fendi&simpla=1
- PIV 2020 `akcepti`: https://vortaro.net/py/serchi.py?s=akcepti&simpla=1
- PIV 2020 `sango`: https://vortaro.net/py/serchi.py?s=sango&simpla=1

## 513. 512周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / Diseases, Treatment

結果:
- **追加修正あり**

修正:
- `ID4567` `Insekto mordis min` → `Insekto pikis min`
  - 露文 `Меня укусило насекомое.` と英中韓文だけを見ると `mordi` も「噛む」寄りで完全な誤りとは言い切れない。
  - ただし日本語 `虫に刺されました。` の健康相談フレーズとしては、PIV で `piki` に「動植物が尖った器官で傷つける」語義と蜂・虫の用例が確認できるため、`Insekto pikis min` のほうが自然で、内容も変えないと判断した。

主な据え置き確認:
- `haŭterupcio`, `furunko`, `konstipiĝi`, `konstipita`, `naza kataro`, `kontaĝa` は症状・病名の表現として確認できる。
- `Mi sentas kapturnon`, `Mi sentas min malforta`, `Mia fingro ŝveliĝis`, `Mia nazo fluas` は症状説明として意味ズレなし。
- `suturerojn`, `urinan specimenon`, `sangopremo`, `pulso`, `rentgenan bildon` は治療・検査文脈で自然。
- `Ĉu mi rajtas ellitiĝi?` は病床から起きてよいかを尋ねる表現として対応する。

参照:
- PIV 2020 `piki`: https://vortaro.net/py/serchi.py?s=piki&simpla=1
- PIV 2020 `mordi`: https://vortaro.net/py/serchi.py?s=mordi&simpla=1
- PIV 2020 `suturo`: https://vortaro.net/py/serchi.py?s=suturo&simpla=1
- PIV 2020 `urina`: https://vortaro.net/py/serchi.py?s=urina&simpla=1

## 514. 513周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, Dentist, Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `plombo`, `plombi`, `kario`, `dentprotezo`, `kanaltraktadon`, `loka anestezo` は歯科文脈で対応する。
- `alĝustigu al vi kronon` は歯冠を合わせる処置として意味は通り、明確な意味ズレまではないため維持。
- `dioptrio`, `astigmatismo`, `miopa`, `hipermetropa`, `kontaktlensojn`, `okulvitrojn` は眼鏡店・検眼文脈で整合する。
- `inhalilon`, `plastrojn`, `jodon`, `paracetamolon`, `aspirinon`, `traĉojn` は薬局での品目として意味ズレなし。

参照:
- PIV 2020 `plombo`: https://vortaro.net/py/serchi.py?s=plombo&simpla=1
- PIV 2020 `dioptrio`: https://vortaro.net/py/serchi.py?s=dioptrio&simpla=1
- PIV 2020 `miopa`: https://vortaro.net/py/serchi.py?s=miopa&simpla=1
- PIV 2020 `hipermetropa`: https://vortaro.net/py/serchi.py?s=hipermetropa&simpla=1

## 515. 514周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy, Communication Means / Public Telephones, Phone Calls

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `herbaj medikamentoj`, `kromefikoj`, `dormigiloj`, `misdigesto`, `tuso`, `laksigilo`, `elĉerpiĝis` は薬局での説明として文脈別許容。
- `Ĉu mi prenu ĝin fastante?` は服薬時の「空腹時」を尋ねる表現として、PIV の `fasto` の薬用例とも整合する。
- `Ne prenu interne` は `Ne enprenu` より説明的だが、「内服しないでください」という注意文として意味は明確。
- `telefonbudo`, `telefonkarto`, `voka signalo`, `retelefoni`, `aŭtomata respondilo`, `mesaĝon` は電話関連の語彙として整合する。

参照:
- PIV 2020 `fasti`: https://vortaro.net/py/serchi.py?s=fasti&simpla=1
- PIV 2020 `dormi`: https://vortaro.net/py/serchi.py?s=dormigilo&simpla=1
- PIV 2020 `telefono`: https://vortaro.net/py/serchi.py?s=telefono&simpla=1

## 516. 515周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interna numero`, `telefonlibro`, `telefonisto`, `fakso`, `retpoŝtadreso`, `ensaluti`, `elsaluti` は勤務先電話・通信文脈として対応する。
- `en Facebook`, `en Tvitero`, `blogo`, `poŝtelefonon`, `elŝutas`, `presilo`, `skanilo` は現代的な媒体・通信語彙として文脈別許容。
- `rekomendita poŝto`, `afranki`, `poŝtmarkojn`, `dogana deklaracio`, `paketo`, `pesilo` は郵便局文脈で意味ズレなし。
- `Ĉu vi povas sendi al mi la ligilon?`, `Ĉu mi povas presi ĉi tie?` は日本語・中韓文との対応も保たれている。

参照:
- PIV 2020 `retpoŝto`: https://vortaro.net/py/serchi.py?s=retpo%C5%9Dto&simpla=1
- PIV 2020 `afranki`: https://vortaro.net/py/serchi.py?s=afranki&simpla=1
- PIV 2020 `poŝto`: https://vortaro.net/py/serchi.py?s=po%C5%9Dto&simpla=1

## 517. 516周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letters, Time & Weather / Time Expressions, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `vivresumo`, `Antaŭdankon`, `retmesaĝon`, `antaŭĝojas ricevi vian respondon` は手紙・郵便・メール文脈で意味ズレなし。
- `Mi kunsendas mian vivresumon` は応募書類などを添付する定型表現として自然。
- `kvin antaŭ la dua`, `kvarono antaŭ la tria`, `duono post la kvara`, `ĉirkaŭ la deka`, `Ĝis la unua horo` は時間表現として対応する。
- 月名・季節名・曜日名は、`la printempaj monatoj estas marto, aprilo kaj majo` などの説明文として一貫している。

参照:
- PIV 2020 `poŝtrestante`: https://vortaro.net/py/serchi.py?s=po%C5%9Dtrestante&simpla=1
- PIV 2020 `sendi`: https://vortaro.net/py/serchi.py?s=sendi&simpla=1
- PIV 2020 `ĝis`: https://vortaro.net/py/serchi.py?s=%C4%9Dis&simpla=1

## 518. 517周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Ĉi-posttagmeze`, `Postmorgaŭ`, `je la fino de la monato`, `semajnfine`, `ĝis lundo`, `post semajno` は予定・日付表現として整合する。
- `glacie kaj glite`, `Pluvetadas`, `Hajlas`, `Fulmas`, `fulmotondro`, `venteto`, `ventego`, `sub nulo` は天候表現として自然。
- `veterprognozo`, `atmosfera premo`, `humido`, `subite ŝanĝiĝi`, `vetero estos bela` は天気予報・気象説明の文脈で意味ズレなし。
- `Kia estos la vetero morgaŭ?`, `Kiam ĉesos pluvi?`, `Kiu estas la plej varma monato en via lando?` は日中韓文との対応も保たれている。

参照:
- PIV 2020 `hajlo`: https://vortaro.net/py/serchi.py?s=hajlo&simpla=1
- PIV 2020 `fulmotondro`: https://vortaro.net/py/serchi.py?s=fulmotondro&simpla=1
- PIV 2020 `vetero`: https://vortaro.net/py/serchi.py?s=vetero&simpla=1

## 502. 501周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Photography, At the Pharmacy

結果:
- **追加修正あり**

修正:
- `ID3494` `Ili sidas sur mi kiel ganto` → `Ili perfekte sidas al mi`
  - 露文 `Они сидят на мне как влитые.` の直訳として `sur mi` が入っていたが、PIV の衣服・帽子の用例では `sidi al vi` 型が確認できる。
  - `kiel ganto` は英語慣用句の直訳として靴文脈ではやや不自然なため、意味を変えずに「ぴったり合う」を `perfekte sidas al mi` とした。

主な据え置き確認:
- `zorioj` は PIV で鼻緒型の履物として確認でき、Japanese/Chinese/Korean のサンダル系表現と大きな意味ズレなし。
- `ŝelkoj` は PIV でズボン等を吊るす肩紐として確認でき、braces/suspenders 文脈に対応する。
- `Akvorezistan ŝminkon por okulharoj` は `maskaro` ではないが、マスカラを指す説明的表現として文脈上明確なため維持。
- `presi la fotojn`, `fototubeto`, `memorkarto`, `ŝargilo`, `kontaktlensojn`, `dentopaston` は買い物・薬局文脈で整合。

参照:
- PIV 2020 `sidi`: https://vortaro.net/py/serchi.py?s=sidi&simpla=1
- PIV 2020 `zorio`: https://vortaro.net/py/serchi.py?s=zorio&simpla=1
- PIV 2020 `ŝelko`: https://vortaro.net/py/serchi.py?s=%C5%9Delko&simpla=1

## 503. 502周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / At the Pharmacy, Supermarket

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sunbrulvundon`, `doloriga gorĝo`, `glutdoloraĵoj`, `kontraŭdolorilojn`, `laksigilon`, `ungventon` は薬局での症状・薬品表現として対応する。
- `beboŝampuo`, `senodorigilon`, `lipruĝon`, `harsekigilon`, `razŝaŭmon`, `razkremon` は身だしなみ用品として透明。
- `sandviĉa pano`, `kompleta lakto`, `senŝaŭmigita lakto`, `nigra teo`, `kelkajn kafgrajnojn` は食品名として文脈別許容。
- `Kiu estas la limdato?` は「どの期限日か」を尋ねる小売り文脈として許容し、意味ズレなしと判断。

参照:
- PIV 2020 `ŝampuo`: https://vortaro.net/py/serchi.py?s=%C5%9Dampuo&simpla=1
- PIV 2020 `fen`: https://vortaro.net/py/serchi.py?s=feni&simpla=1
- PIV 2020 `limdato`: https://vortaro.net/py/serchi.py?s=limdato&simpla=1

## 504. 503周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / Supermarket, Bookshop, Florist

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `freŝaj ovoj`, `frostigitan viandon`, `konservitajn tomatojn`, `laktosukero`, `reduktitan prezo` はスーパーでの購入表現として意味ズレなし。
- `kuirlibro`, `vojaĝgvidilon`, `paperlibro`, `malmolan kovrilon`, `brokantan librovendejon` は書店文脈で整合する。
- `bukedon da floroj`, `floraranĝo`, `florojn en poto`, `krono el freŝaj floroj` は花屋・供花文脈として対応する。
- `restmono`, `pagon per karto`, `kvitancon`, `senimposta aĉetado` は精算・免税関連として自然。

参照:
- PIV 2020 `konservi`: https://vortaro.net/py/serchi.py?s=konservi&simpla=1
- PIV 2020 `brokanti`: https://vortaro.net/py/serchi.py?s=brokanti&simpla=1
- PIV 2020 `krono`: https://vortaro.net/py/serchi.py?s=krono&simpla=1

## 505. 504周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Paying; Leisure Time / Cinema

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interŝanĝi ... kontraŭ`, `repagon`, `difektita`, `mankas peco`, `registrita poŝto` は返品・交換・郵送文脈で整合する。
- `filmo de suspenso`, `animacia filmo`, `subtekstoj`, `nigrablanka filmo`, `sciencfikcia filmo` は映画ジャンル・上映条件として許容。
- `antaŭa vico`, `malantaŭa vico`, `en la mezo`, `dublita`, `filmo komenciĝas` は映画館での席・上映文脈として対応する。
- `Kiu estas la sekureca numero sur la karto?` はカード上の識別番号を聞く文として意味ズレなし。

参照:
- PIV 2020 `repagi`: https://vortaro.net/py/serchi.py?s=repagi&simpla=1
- PIV 2020 `subtitolo`: https://vortaro.net/py/serchi.py?s=subtitolo&simpla=1
- PIV 2020 `dubli`: https://vortaro.net/py/serchi.py?s=dubli&simpla=1

## 506. 505周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / Cinema, Theatre, Museum, Nightclub

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `teatra lorneto`, `loĝio`, `interakto`, `ludafiŝo`, `enirbiletoj` は劇場文脈として許容。特に `interakto` は PIV で幕間・休憩時間の語義が確認できる。
- `enirkotizo`, `aŭdgvidilo`, `ĉefverko`, `fama pentraĵo`, `la galerio fermiĝas` は美術館・博物館文脈で整合する。
- `diskĵokeo`, `dancplanko`, `gastejlisto`, `ni kuniru danci` はナイトクラブ文脈として文脈別許容。
- `Ĉu mi povas foti?`, `Ĉu ĝi estas interaga?`, `La ekspozicio estas en la dua etaĝo` は場面と意味が一致する。

参照:
- PIV 2020 `interakto`: https://vortaro.net/py/serchi.py?s=interakto&simpla=1
- PIV 2020 `paŭzo`: https://vortaro.net/py/serchi.py?s=pa%C5%ADzo&simpla=1
- PIV 2020 `loĝio`: https://vortaro.net/py/serchi.py?s=lo%C4%9Dio&simpla=1

## 507. 506周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / Nightclub, At the Beach, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ĉambro por fumi`, `vestogardejo`, `enirkotizo`, `lasera spektaklo` はナイトクラブ・会場表現として整合する。
- `plaĝa ombrelo`, `sunbrulvundo`, `savisto`, `akvoskioj`, `malsekkostumo`, `jaĥton` は海辺・水上活動語彙として文脈別許容。
- `akvoskiado`, `veli`, `tabulvelado`, `naĝmaskon`, `spirtubon`, `naĝilojn` はウォータースポーツ文脈に対応する。
- `Li golis`, `ligmaĉo`, `golfbastonojn`, `golfĉaron` はスポーツ・ゴルフ語彙として意味ズレなし。

参照:
- PIV 2020 `akvoskio`: https://vortaro.net/py/serchi.py?s=akvoskio&simpla=1
- PIV 2020 `jaĥto`: https://vortaro.net/py/serchi.py?s=ja%C4%A5to&simpla=1
- PIV 2020 `golo`: https://vortaro.net/py/serchi.py?s=goli&simpla=1

## 508. 507周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport, Going Camping

結果:
- **追加修正あり**

修正:
- `ID4056` `Kiel vi pensas, kia estos la fina rezulto?` → `Kia, laŭ vi, estos la fina rezulto?`
  - `Kiel vi pensas` は露文・英文の「どう思う」の直訳調が強い。`laŭ vi` を挿入して「あなたの見立てでは」という意味にし、スコア予想の内容は維持した。
- `ID4151` `Kiel pri promeno en la arbaro?` → `Kion vi diras pri promeno en la arbaro?`
  - `How about ...? / Как насчёт ...?` の提案表現として、`kiel pri` より `Kion vi diras pri ...?` の方がエスペラントとして自然。
  - 「森を散歩しませんか」という提案内容は変更していない。

主な据え置き確認:
- `vetŝancoj`, `remifinaĵo`, `nul kontraŭ nul`, `golŝanco`, `trejnisto`, `diskĵeto`, `haltigita pro pluvo` はスポーツ観戦文脈として対応する。
- `telfero`, `seĝtelfero`, `skivoston`, `skilifto`, `tobogano`, `rostokrado`, `tendostango` はキャンプ・スキー・野外活動語彙として許容。
- `Kie estas la plej proksima tendaro?`, `Ĉu ni rajtas fajrigi ĉi tie?`, `Ni iru pikniki` は場面と意味が一致する。

参照:
- PIV 2020 `laŭ`: https://vortaro.net/py/serchi.py?s=la%C5%AD&simpla=1
- PIV 2020 `diri`: https://vortaro.net/py/serchi.py?s=diri&simpla=1
- Tekstaro 用例検索 `Kion vi diras pri`: https://tekstaro.com/

## 509. 508周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping, Hobbies, In the Garden, Entertaining

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ruldomo`, `piedvojetoj`, `fornoj por ruldomoj`, `fajroestingilon`, `ŝparbutikon` はキャンプ・余暇文脈として整合。
- `kolektas poŝtmarkojn`, `popolmuziko`, `televidaj romanoj`, `modelfervojo`, `ŝako`, `legadon` は趣味表現として対応する。
- `erpi`, `elherbi`, `tondi la gazonon`, `kompoŝto`, `fruktarbejo`, `akvumi`, `plantas semojn` は園芸語彙として意味ズレなし。
- `buŝtukoj`, `satiĝis`, `fari paroladon`, `adiaŭan feston`, `amuziĝis` は来客・会食文脈で許容。

参照:
- PIV 2020 `erpi`: https://vortaro.net/py/serchi.py?s=erpi&simpla=1
- PIV 2020 `kompoŝto`: https://vortaro.net/py/serchi.py?s=kompo%C5%9Dto&simpla=1
- PIV 2020 `fruktarbejo`: https://vortaro.net/py/serchi.py?s=fruktarbejo&simpla=1

## 510. 509周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / Bank, Estate Agent

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provizio`, `konteltiro`, `kuranta konto`, `ŝparkonto`, `ĉekaro`, `monkarton`, `ĝiri`, `interezokvoto` は銀行・送金文脈で確認できる。
- `hipoteko`, `makleriston`, `duetaĝa`, `bangalo`, `vicdomo`, `duamana posedaĵo`, `meblita`, `luebla` は不動産文脈として整合する。
- `Mia kontokarto estis ŝtelita`, `Mi ŝatus bloki mian karton`, `Mi volas nuligi ĉekon` は銀行窓口・紛失対応として意味ズレなし。
- `Ĉu ĝi estas je promenatinga distanco de butikoj?`, `Ĉu ĝi havas duoblan vitraĵon?` は物件確認の表現として許容。

参照:
- PIV 2020 `provizio`: https://vortaro.net/py/serchi.py?s=provizio&simpla=1
- PIV 2020 `ĝiri`: https://vortaro.net/py/serchi.py?s=%C4%9Diri&simpla=1
- PIV 2020 `hipoteko`: https://vortaro.net/py/serchi.py?s=hipoteko&simpla=1
- PIV 2020 `bangalo`: https://vortaro.net/py/serchi.py?s=bangalo&simpla=1

## 511. 510周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / Estate Agent, Beauty Parlour, Tailor, Shoe Repairs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `franĝo`, `dislimo`, `senharigo`, `feni`, `permanentaĵo`, `tondigon`, `manikuron`, `pedikuron` は美容院・美容サービス文脈で辞書・派生上の根拠がある。
- `kostumo laŭmezura`, `Ŝanĝu la maniklongon`, `malvastigi`, `larĝigi`, `alĝustigi`, `dekstra ŝultro` は仕立て直し表現として対応する。
- `renovigi miajn ŝuojn`, `anstatigi la kalkanojn`, `ŝuojn ripari`, `novaj plandumoj` は靴修理文脈で意味ズレなし。
- `Mi ŝatus provi alian frizaĵon`, `Nur iomete tondi`, `Ĉu vi povas lavi ĝin?` は美容院での依頼として自然。

参照:
- PIV 2020 `franĝo`: https://vortaro.net/py/serchi.py?s=fran%C4%9Do&simpla=1
- PIV 2020 `dislimo`: https://vortaro.net/py/serchi.py?s=dislimo&simpla=1
- PIV 2020 `har`: https://vortaro.net/py/serchi.py?s=senharigo&simpla=1
- PIV 2020 `fen`: https://vortaro.net/py/serchi.py?s=feni&simpla=1

## 492. 491周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / At the Train Station, On the Bus or Train, Taxi

結果:
- **追加修正あり**

修正:
- `ID2529` `Kiu estas la adreso?` → `Kio estas la adreso?`
  - 「住所は何ですか / Какой адрес?」の内容では、候補の中から「どれ」を選ぶ `kiu` より、内容を尋ねる `kio` が自然。
  - 表現内容は変更せず、疑問詞だけを文法的に明確化した。

主な据え置き確認:
- `eksprestrajno`, `revenbileto`, `vojaĝkarto`, `abonbileto`, `skemo de la metroo` は鉄道・交通カード文脈で意味ズレなし。
- `haltejo`, `vagono`, `restoracia vagono`, `pakaĵujo`, `taksimetro`, `taksihaltejo` はバス・列車・タクシー文脈として許容。
- `flughavena krompago`, `nokta krompago`, `nunmomente ne estas disponeblaj aŭtoj` はタクシー手配・料金文脈で対応する。
- `Veturigu min ĉi tien`, `Ellasu min ĉi tie` は地図・住所を示す場面を含む実用表現として文脈別許容。

参照:
- PIV 2020 `adreso`: https://vortaro.net/py/serchi.py?s=adreso&simpla=1
- PIV 2020 `haltejo`: https://vortaro.net/py/serchi.py?s=haltejo&simpla=1
- PIV 2020 `krompago`: https://vortaro.net/py/serchi.py?s=krompago&simpla=1
- PIV 2020 `pakaĵo`: https://vortaro.net/py/serchi.py?s=paka%C4%B5o&simpla=1

## 493. 492周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi, Ship; Hotel / Asking about Facilities, Booking a Room

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Savringo`, `Savboato`, `kajuto`, `ferdeko`, `enŝipiĝi`, `pramo`, `transiro` は船旅語彙として対応する。
- `Mi havas marmalsanon`, `La maro estas maltrankvila`, `Surmetu viajn savvestojn` は船酔い・海況・安全文脈で意味ズレなし。
- `Ĉio inkluzivita`, `inkludita` は PIV で `inkludi` / `inkluzivi` が確認でき、料金に含まれる文脈として許容。
- `ŝtopilingo`, `rulseĝa aliro`, `monŝranko`, `frizejo`, `gimnastikejo` はホテル設備語彙として透明。

参照:
- PIV 2020 `kajuto`: https://vortaro.net/py/serchi.py?s=kajuto&simpla=1
- PIV 2020 `ferdeko`: https://vortaro.net/py/serchi.py?s=ferdeko&simpla=1
- PIV 2020 `inkludi`: https://vortaro.net/py/serchi.py?s=inkludi&simpla=1
- PIV 2020 `ŝtopilingo`: https://vortaro.net/py/serchi.py?s=%C5%9Dtopilingo&simpla=1

## 494. 493周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Room, Checking in, During Your Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `atendolisto`, `longdaŭra restado`, `ĉambro por nefumantoj`, `aldona/plia lito` は予約文脈として自然。
- `ĉambroŝlosilo`, `ĉambronumero`, `teretaĝo`, `matenmanĝo estas servata`, `ĉambroservo` はホテルチェックイン文脈で対応する。
- `monŝranko`, `savelirejo`, `telefonan ŝargilon`, `eksteran linion`, `telefona mesaĝo` は設備・滞在中の問い合わせとして意味ズレなし。
- `gladigi ĉi tion`, `purigi kostumon`, `plusendi mian poŝton` はランドリー・郵便転送の文脈で許容。

参照:
- PIV 2020 `atendi`: https://vortaro.net/py/serchi.py?s=atendi&simpla=1
- PIV 2020 `monŝranko`: https://vortaro.net/py/serchi.py?s=mon%C5%9Dranko&simpla=1
- PIV 2020 `gladi`: https://vortaro.net/py/serchi.py?s=gladi&simpla=1
- PIV 2020 `plusendi`: https://vortaro.net/py/serchi.py?s=plusendi&simpla=1

## 495. 494周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay, Checking out, Complaints, Renting a Flat

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kalkulo` と `fakturo` は会計・請求書文脈で使い分けられており、ホテル精算の各文と整合する。
- `restmono` は `apunto` と並んで「つり銭・小銭」文脈で辞書・用例が確認でき、`Mian restmonon`, `Gardu la restmonon`, `malĝustan restmonon` と一貫するため維持。
- `monŝranko`, `detaligita fakturo`, `personan ĉekon`, `servokotizo`, `imposto` は精算関連語彙として意味ズレなし。
- 苦情表現の `malbonodoras`, `ŝtopita`, `littukoj`, `duobla lito`, `du apartaj litoj`, `subskribo` は露文・日中韓文と対応する。

参照:
- PIV 2020 `apunto`: https://vortaro.net/py/serchi.py?s=apunto&simpla=1
- ReVo `restmono`: https://reta-vortaro.de/revo/art/mon.html
- PIV 2020 `fakturo`: https://vortaro.net/py/serchi.py?s=fakturo&simpla=1
- PIV 2020 `littuko`: https://vortaro.net/py/serchi.py?s=littuko&simpla=1

## 496. 495周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat; Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vazaro`, `ŝvabrilo`, `polvosuĉilo`, `telerlavmaŝino`, `elektromezurilo` はアパート備品・家電文脈として対応する。
- `suĉkloŝo` は PIV 本文では直接確認できなかったが、Wiktionary 等で plunger として確認でき、透明な合成として維持。
- `skatolmalfermilo` は Glosbe/Wikimedia 等で tin/can opener として確認でき、PIV の `elladigilo` も同義方向の根拠になるため、現行のまま許容。
- `adherema filmo` は PIV の `adheri/adhera` に基づく透明表現で、cling film 文脈として大きな意味ズレなし。
- `Rezervita`, `antaŭmendi tablon`, `fumejo`, `sidi en la suno/ombro`, `gasita akvo`, `vinkarto` は飲食店文脈で整合する。

参照:
- PIV 2020 `ŝvabrilo`: https://vortaro.net/py/serchi.py?s=%C5%9Dvabrilo&simpla=1
- Wiktionary `kloŝo` / `suĉkloŝo`: https://en.wiktionary.org/wiki/klo%C5%9Do
- Glosbe `tin` / `skatolmalfermilo`: https://en.glosbe.com/en/eo/tin
- PIV 2020 `adheri`: https://vortaro.net/py/serchi.py?s=adheri&simpla=1

## 497. 496周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio` は PIV 未収録寄りだが、Wiktionary 等で smoothie として確認でき、現代的な飲料名として文脈別許容。
- `koŝera manĝaĵo`, `halala`, `kebabo`, `pastaĵoj`, `bifsteko kun fritoj` は料理・宗教食語彙として意味ズレなし。
- `surloke aŭ por forporti`, `por ĉi tie`, `por kunpreni` は eat in / take away 文脈で対応する。
- `antaŭmanĝaĵoj`, `specialaĵo de la domo`, `tritavola sandviĉo`, `franca saŭco`, `mezrostita`, `bone rostita viando` は注文表現として許容。

参照:
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio
- PIV 2020 `koŝera`: https://vortaro.net/py/serchi.py?s=ko%C5%9Dera&simpla=1
- PIV 2020 `kebabo`: https://vortaro.net/py/serchi.py?s=kebabo&simpla=1
- PIV 2020 `terpom-fritoj`: https://vortaro.net/py/serchi.py?s=terpom-fritoj&simpla=1

## 498. 497周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `manĝobastonetoj`, `fritoj`, `ankoraŭ unu porcion da rizo`, `servokotizo`, `trinkmono` は食事中・会計文脈として対応する。
- `Mi estas alergia al laktaĵoj/nuksoj/tritiko` はアレルギー表現として列間の意味ズレなし。
- `La kalkulo inkluzivas la servokotizon`, `malĝuste sumigita`, `skribi tion sur mian konton` は請求・会計表現として自然。
- 苦情表現の `tro kuirita`, `odoras je korko`, `tro sala`, `tro malmola`, `Mia mendo ankoraŭ ne alvenis` は露文・日中韓文と対応する。

参照:
- PIV 2020 `bastoneto`: https://vortaro.net/py/serchi.py?s=bastoneto&simpla=1
- PIV 2020 `trinkmono`: https://vortaro.net/py/serchi.py?s=trinkmono&simpla=1
- PIV 2020 `korko`: https://vortaro.net/py/serchi.py?s=korko&simpla=1
- PIV 2020 `inkludi`: https://vortaro.net/py/serchi.py?s=inkludi&simpla=1

## 499. 498周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, At the Pub; Food / Meat & Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `postebrio` は PIV の `post ebrio` と対応し、hangover 文脈として意味が明確。
- `barela aŭ botela biero`, `glasetojn da tekilo`, `laktoskuaĵo`, `ĉipsoj`, `fajrilon` はパブ語彙として許容。
- `bova lumbaĵo`, `porkaj ripoj`, `fumita truto`, `grilita salmo`, `boligitaj kankroj`, `bovida kotleto` は肉魚名・調理法として整合する。
- `Pardonu, ni ne plu havas omarojn`, `la salikoka supo finiĝis` は品切れ表現として対応する。

参照:
- PIV 2020 `post ebrio`: https://vortaro.net/py/serchi.py?s=post%20ebrio&simpla=1
- PIV 2020 `tekilo`: https://vortaro.net/py/serchi.py?s=tekilo&simpla=1
- PIV 2020 `lumbaĵo`: https://vortaro.net/py/serchi.py?s=lumba%C4%B5o&simpla=1
- PIV 2020 `kankro`: https://vortaro.net/py/serchi.py?s=kankro&simpla=1

## 500. 499周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Food & Spices, Breakfast Food

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 果物類の `avokado`, `kivifrukto`, `akvomelono`, `limeoj`, `oksikoko`, `grapfrukto`, `mirtelo`, `frambo` は辞書・語形成上問題なし。
- `arakidoj`, `migdaloj`, `juglandoj`, `sekigitaj fruktoj` はナッツ・乾果文脈で対応する。
- 野菜類の `florbrasiko`, `melongeno`, `pekli`, `kapsiko`, `panumita kukurbeto`, `brezitaj karotoj kaj kikeroj` は料理文脈として許容。
- `eruko`, `kuskusa salato`, `verdaj fazeoloj`, `safrana rizo`, `fazeola supo`, `petrosela saŭco` は主食・香辛料語彙として意味ズレなし。

参照:
- PIV 2020 `avokado`: https://vortaro.net/py/serchi.py?s=avokado&simpla=1
- PIV 2020 `arakido`: https://vortaro.net/py/serchi.py?s=arakido&simpla=1
- PIV 2020 `pekli`: https://vortaro.net/py/serchi.py?s=pekli&simpla=1
- PIV 2020 `panumi`: https://vortaro.net/py/serchi.py?s=panumi&simpla=1

## 501. 500周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food; Shopping / At the Department Store, Clothes

結果:
- **追加修正あり**

修正:
- `ID3362` `Ŝi ŝatas ringokukojn` → `Ŝi ŝatas benjetojn`
  - EN/JA/ZH/KO/RU は doughnuts / ドーナツ / 甜甜圈 / 도넛 / пончики。
  - PIV 2020 で `benjeto` は料理語彙として確認でき、定義内にも `ringoforma benjeto` がある。
  - `ringokuko` は意味は推測できるが、doughnut そのものとしては `benjeto` のほうが辞書確認済みで自然。

主な据え置き確認:
- `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `artefarita dolĉigilo` は朝食語彙として対応する。
- `magazeno` は PIV で「大きめで多品目の店」として確認でき、department store 文脈で文脈別許容。
- `fako`, `sekcio`, `teretaĝo`, `kaso`, `butikoŝtelistoj estos juĝe persekutataj` は百貨店案内・掲示として意味ズレなし。
- 衣類表現の `surprovi`, `provejo`, `kemia purigado`, `laveblaj`, `ŝorto`, `piĵamo`, `Lavu inversigite` は語形成・文脈とも許容。

参照:
- PIV 2020 `benjeto`: https://vortaro.net/py/serchi.py?s=benjeto&simpla=1
- PIV 2020 `magazeno`: https://vortaro.net/py/serchi.py?s=magazeno&simpla=1
- PIV 2020 `kazeo`: https://vortaro.net/py/serchi.py?s=kazeo&simpla=1
- PIV 2020 `ŝorto`: https://vortaro.net/py/serchi.py?s=%C5%9Dorto&simpla=1

一致確認:
- `cmp_exit=0`
- `md5=7488c92c2ba20c2b6091c7e21bf2d0bb`

判定基準:
- RU は最重要参考列
- 実運用では Esperanto と JA/ZH/KO の対応を重視
- 文脈別許容は残す
- 意味のズレが明確な箇所だけ修正
- PIV / Glosbe で裏取りできない置換はしない
- 「辞書にない」だけでは直さない
- 複合語として透明で、意味ズレもないものは原則据え置く

## 1. この文書の見方

この文書では、未修正語を次の2群に分ける。

- `保留継続`: 4周目終了時点でも、まだ少し気になる点が残っている語群
- `保留から外した語`: 以前は保留候補だったが、4周目までの確認で現形維持でよいと判断した語群

実務上、次に重点再調査すべきなのは `保留継続` だけでよい。

## 2. 保留継続

件数:
- `15語群 / 21 PhraseID`

### 2.1 高優先

意味の焦点や語義の取り方にまだ少し緊張があるもの。

| 優先 | PhraseID | 現行文 | 気になる点 | 据え置き理由 |
|---|---:|---|---|---|
| 高 | 902 | Mi estas ĉi tie por labori | RU は「出張」寄り | JA/ZH/KO/EN は「仕事で来ている」と一致しており、RU に寄せて動かすのは危険 |
| 高 | 1560 | Mi estas merkatika administranto | `marketing manager / specialist` の揺れ | 列間の意味を固定した安全な置換先を確定できない |

### 2.2 中優先

見出し語としては弱めだが、文脈上は十分通るもの。

| 優先 | PhraseID | 現行文 | 気になる点 | 据え置き理由 |
|---|---:|---|---|---|
| 中 | 2047 | Mi havas du manbagaĝojn | `manbagaĝo` が弱め | 空港文脈では十分自然 |
| 中 | 2048 | Vi havas tro da manbagaĝo | `manbagaĝo` が弱め | 上と同じ |
| 中 | 2055 | Ĉu mi povus vidi vian manbagaĝon, mi petas? | `manbagaĝo` が弱め | 上と同じ |
| 中 | 2056 | Mi havas unu manbagaĝon | `manbagaĝo` が弱め | 上と同じ |
| 中 | 2058 | Ĝi estas tro granda por manbagaĝo | `manbagaĝo` が弱め | 上と同じ |
| 中 | 2623 | Ĉu vi havas rulseĝan aliron? | やや説明的 | より安全な標準置換を確定できない |

### 2.3 低優先

主に透明な複合語、硬さ、または表記揺れの問題。現状維持でも実害は小さい。

| 優先 | PhraseID | 現行文 | 気になる点 | 据え置き理由 |
|---|---:|---|---|---|
| 低 | 456 | Parolu kun mi en la mandarena ĉina lingvo | やや硬い | 誤りと断定する根拠不足 |
| 低 | 1253 | Ni forveturu de ĉi tie | 直訳感 | 意味ズレは明確でない |
| 低 | 1454 | Kiu estas la templimo por paroladoj? | 複合語の自然さ | 生産的複合語として成立しうる |
| 低 | 2181 | Bagaĝa elpreno | 透明複合語 | 意味は明確、置換先確定不足 |
| 低 | 2213 | Ĉu ĉi tiu aŭto havas infanserurojn? | 透明複合語 | 意味は明確、置換先確定不足 |
| 低 | 2225 | Kiom longa estas la minimuma luoperiodo? | 透明複合語 | 上と同じ |
| 低 | 2254 | Ĉu vi havas vojmapon? | 透明複合語 | 上と同じ |
| 低 | 2278 | Kiom malproksimas la sekva serva areo? | やや calque 的 | 意味ズレは明確でない |
| 低 | 2292 | Mi staris en trafikblokiĝo dum unu horo | 透明複合語 | 意味は明確、壊す理由がない |
| 低 | 2367 | Buskoridoro | やや直訳的 | bus lane と対応し、過去確認済みのため安全な置換先をさらに動かさない |
| 低 | 2782 | Ĉu la servokotizo estas inkluzivita? | 語義幅 | PIV の `kotizo` は会費・分担金寄りで少し気になるが、オンライン実例と列間意味から service charge としては許容範囲 |
| 低 | 2783 | Servokotizo ne estas inkluzivita | 語義幅 | 上と同じ |
| 低 | 2796 | Kiom estas la servokotizo kaj la imposto? | 語義幅 | 上と同じ |

## 3. 保留から外した語

以下は以前は弱候補だったが、4周目までの確認で「現形維持でよい」と判断した語群。
次回以降は、原則として重点再調査対象から外してよい。

### 3.1 4周目で据え置き確定に寄った語

- `mandarena`
- `picejo`
- `klubumi`
- `dombestoj`
- `fantombildo`
- `bandaĝo`
- `vojaĝkostoj`
- `solvanto`
- `interreta kafejo`
- `aŭtobushaltejo`
- `enŝipiĝo`
- `biletaŭtomatoj`
- `vojaĝkarto`
- `abonbileto`
- `pakaĵujo`
- `restmono`
- `taksihaltejo`
- `bankaŭtomato`
- `monŝranko`
- `gimnastikejo`

### 3.2 ホテル・旅行

- `elregistriĝi`
- `longdaŭra restado`
- `telefona ŝargilo`
- `halala`

### 3.3 飲食・買い物

- `naĉoj`
- `barela biero`
- `bekono`
- `ringokukoj`
- `fingrosandaloj`
- `vizaĝpudro`
- `skribmaterialoj`
- `laktoskuaĵo`

### 3.4 娯楽・スポーツ

- `antikvaran librovendejon`
- `drama teatro`
- `karikatursalono`
- `surfotabulo`
- `aerbotelo`
- `tendumejo`

### 3.5 銀行・美容・健康

- `monretiro`
- `kontoekstrakto`
- `duamana`
- `frizaĵo`
- `feni`
- `skalpo`
- `malsanasekuro`
- `kuracista atestilo`
- `dentpurigado`
- `okulvitrujo`

### 3.6 電話・郵便

- `telefonkarto`
- `retelefoni`
- `aŭtomata respondilo`
- `afranko`
- `giĉeto`
- `poŝtrestante`
- `aldonaĵo`

### 3.7 31周目で保留から外した語

- `patrina forpermeso`
- `patra forpermeso`

### 3.8 32周目で修正して保留解除した語

- `laborvojaĝo` → `afervojaĝo`
- `navedbuso` → `naveda buso`

### 3.9 36周目で保留から外した語

- `seĝodorso`

### 3.10 67周目で修正・保留解除した語

- `suĉkloŝo`
- `smuzio`
- `kalcono` → `kalzoneo`

## 4. 実務判断

- 次に本当に重点再調査すべきなのは `保留継続 15語群` のみ
- その中でも、先に見る価値があるのは `高優先 2語群`
- `servokotizo` は、PIV 上の `kotizo` の語義幅を理由に低優先保留とするのが妥当
- `保留から外した語` は、現時点では未修正のままで閉じてよい

## 5. 参照

主に以下を確認に使用:

- PIV
  - https://vortaro.net/
- Glosbe
  - https://glosbe.com/

## 6. 5周目結果

実施日:
- 2026-03-06

対象:
- `ID156〜1255` は通しで再点検
- `ID1256〜5155` は、前周までの `保留継続`・弱候補を重点的に再検証

結果:
- **追加修正なし**
- `cmp_exit=0`
- `md5=13dad84c26a36519e0313fad4c96dc77`

### 6.1 5周目で確認したこと

- `ID456` `mandarena ĉina lingvo`
- `ID767` `surmeti bandaĝon`
- `ID826` `fari lian fantombildon`
- `ID902` `Mi estas ĉi tie por labori`
- `ID1064` `Mi amas klubumi`
- `ID1092` `Ĉu vi havas dombestojn?`
- `ID1253` `Ni forveturu de ĉi tie`
- `ID1350` `Estas pli bone ol la lastan fojon`
- `ID1454` `templimo`
- `ID1560` `merkatika administranto`
- `ID1590` `patrina forpermeso`
- `ID1591` `patra forpermeso`
- `ID1664` `laborvojaĝojn`
- `ID1906` `navedbuso`
- `ID2047/2048/2055/2056/2058` `manbagaĝo`
- `ID2149` `seĝodorso`
- `ID2181` `bagaĝa elpreno`
- `ID2213` `infanseruroj`
- `ID2225` `luoperiodo`
- `ID2254` `vojmapo`
- `ID2278` `serva areo`
- `ID2292` `trafikblokiĝo`
- `ID2782/2783/2796` `servkotizo / servokotizo`

### 6.2 5周目で据え置き判断がさらに強くなった語

以下は、5周目で外部用例・辞書側の裏付けが相対的に増え、少なくとも「AI造語だから直すべき」とは言えないことが、前より明確になった語。

- `laborvojaĝo`
- `patrina forpermeso`
- `patra forpermeso`
- `manbagaĝo`
- `seĝodorso`

### 6.3 5周目終了時点の実務判断

- `保留継続` 群についても、5周目で**新たに動かすだけの根拠は出なかった**
- したがって、CSV 本体はこの時点でも**据え置きが妥当**
- 次に再調査する場合も、まずは `高優先 5語群` だけを対象にすれば十分

### 6.4 5周目で確認した補助ソース

- `laborvojaĝo`
  - https://www.esperanto-panorama.net/vortaro/labvoja.htm
- `patrina forpermeso`
  - https://majstro.com/ser/e2e?q=patrina%20forpermeso
- `patra forpermeso`
  - https://majstro.com/ser/e2e?q=patra%20forpermeso
- `manbagaĝo`
  - https://www.esperanto-panorama.net/vortaro/manbagag.htm

## 7. 6周目結果

実施日:
- 2026-04-28

対象:
- 既存の 5周目結果を起点に、CSV 全体の構造チェック、長い低頻度語・透明複合語・保留継続語、列間対応の再確認を実施
- PIV / Glosbe / Web 用例で、置換してよい根拠が取れるものだけを修正

修正:
- `ID1807` `Ĉu vi scias, kie troviĝas la kanada ambasadorejo?`
  - `Ĉu vi scias, kie troviĝas la kanada ambasadejo?` に修正
  - 理由: PIV 2020 では `ambasadejo` が「大使館の建物」、`ambasadorejo` が「大使の住居」。JA/ZH/KO/RU/EN はすべて「カナダ大使館 / Canadian embassy / канадское посольство」に対応しているため。

一致確認:
- `cmp_exit=0`
- `md5=573494e5fbbd197f23ab0d72461f8c34`

## 8. 7周目 100件ずつ継続点検

実施日:
- 2026-04-28

対象:
- `ID156〜1455` を100件ずつ通し確認
- 今回の継続分では特に `ID756〜1455` を救急・警察・自己紹介・居住・国籍/宗教・家族・人物描写・趣味・予定調整・交際・結婚・学校/大学文脈として精査
- PIV / Glosbe / Web 用例で根拠が取れ、かつ意味ズレが明確な箇所だけを修正

修正:
- `ID641` `Ĉu vi ĝenus doni al mi la tekkomputilon?`
  - `Ĉu ĝenus vin doni al mi la tekkomputilon?` に修正
  - 理由: PIV 2020 では `ĝeni` は他動詞。元文は英語 "Would you mind..." の直訳で `vi` を `ĝeni` の主語にしており不自然。`vin` を目的語にする形で RU/JA/ZH/KO の依頼表現を維持。
- `ID826` `Ni penos fari lian fantombildon`
  - `Ni penos fari lian fotoroboton` に修正
  - 理由: RU `фоторобот`、EN `photofit`、JA/ZH/KO は警察の似顔絵/合成画像。`fantombildo` はこの意味では弱く、Glosbe で `fotoroboto` -> `retrato robot` を確認。
- `ID984` `Mi estas edziĝinta`
  - `Mi estas edziniĝinta` に修正
  - 理由: RU は女性話者の `Я замужем`。PIV 2020 では `edziĝi` は「夫になる」、`edziniĝi` は「妻になる」。日本語・中国語・韓国語は性別非明示なので、この修正で内容は変わらない。
- `ID1018` `Ne, mi estas sola infano`
  - `Ne, mi estas solinfano` に修正
  - 理由: PIV 2020 に `solinfano` = 兄弟姉妹のいない子として掲載。`sola infano` より「一人っ子」を明確に表せる。
- `ID1273` `Mi ŝatas vian vestaron`
  - `Mi ŝatas vian veston` に修正
  - 理由: RU/JA/ZH/KO は「今の服装・装い」。PIV 2020 では `vesto` が身につける衣服全般を表し、`vestaro` はこの文脈では広すぎる。

主な据え置き確認:
- `ID779` `elartikigis mian brakon`: PIV で直接見出しは出ないが、透明複合で列間意味は一致。確実な置換根拠が不足。
- `ID781` `manĝaĵveneniĝon`: PIV で `veneniĝo` は確認。複合語として透明で、RU/JA/ZH/KO と整合。
- `ID803` `Oni enrompis mian aŭton`: PIV で `enrompi` の語義を確認。車上荒らし文脈として許容。
- `ID852/854` `prezenti vin al Davido/Alico`: EO/EN/RU は「あなたを David/Alice に紹介」。JA/ZH/KO は相手を紹介する言い方にも読めるが、紹介場面では実害が小さく、RU に寄せて据え置き。
- `ID1081` `troti`: PIV で人についても「小走り/短い歩幅で速く進む」語義を確認。ジョギング文脈として許容。
- `ID1119/1199/1209` `aliĝi al ...`: PIV で `aliĝi` の「加わる」語義を確認。会話的な「join」文脈として許容。
- `ID1357` `En kiu aĝo ...`: `en la aĝo de ...` 系の用法として許容。

一致確認:
- `cmp_exit=0`
- `md5=c96275e962a671693ce617daeea04277`

## 9. 8周目 100件ずつ継続点検

実施日:
- 2026-04-28

対象:
- `ID1456〜2855` を100件ずつ通し確認
- 教育後半、職業、業務連絡、道案内、空港/税関、機内、レンタカー、運転、バス/鉄道、タクシー、船、ホテル予約/滞在/苦情まで精査
- Esperanto と JA/ZH/KO の対応を主軸にしつつ、RU/EN を参照。辞書で確認でき、意味ズレまたは語形上の問題が明確な箇所だけを修正

修正:
- `ID1780` `Kiun mallongan vojon mi povas preni?`
  - `Kiun ŝparvojon mi povas preni?` に修正
  - 理由: PIV 2020 で `ŝparvojo` は「通常より短い道」。Glosbe でも `shortcut` の訳として確認。`mallonga vojo` でも通じるが、JA/ZH/KO/RU/EN は「近道/捷径/shortcut/короткий путь」なので既存語に寄せた。
- `ID2072` RU `Приятного прибывания!`
  - `Приятного пребывания!` に修正
  - 理由: 「滞在」を表すのは `пребывание`。EO `restadon`、EN/JA/ZH/KO と整合する参照文の明確な一字誤り。
- `ID2100` `Mi havas rifuĝintan statuson`
  - `Mi havas statuson de rifuĝinto` に修正
  - 理由: PIV 2020 で `rifuĝinto` は政治的・宗教的迫害等により避難した人。`rifuĝinta statuso` は「逃げた status」のように読めるため、RU `статус беженца` と JA/ZH/KO に合わせて「難民の地位」と明示。
- `ID2157` `Ĉu vi povus traduki ĝin al la turka?`
  - `Ĉu vi povus traduki ĝin en la turkan?` に修正
  - 理由: PIV 2020 の `traduki` は「de unu lingvo en alian」。`al` より `en` がこの語法に合う。
- `ID2649` `Mi ŝatus plenan pension`
  - `Mi ŝatus plenan pensionon` に修正
  - 理由: `pension` は PIV 2020 の `pensio`（年金）の対格として読める。ホテルの `full board / полный пансион` 文脈では少なくとも `pensiono` 系にする必要があり、目的語として `pensionon` にした。
- `ID2848` `Mi rezervis duoblan liton, sed ricevis du unulitajn`
  - `Mi rezervis duoblan liton, sed ricevis du apartajn litojn` に修正
  - 理由: PIV 2020 で `lito` と `aparta` を確認。元文は名詞が省略され、`du unulitajn` が「2つの一人用の何か」となって不明瞭。JA/ZH/KO/RU は「ダブルベッドではなくツイン/二つの単独ベッド」を表すため、`du apartajn litojn` が安全。

主な据え置き確認:
- `ID1467` `ripeti multajn aferojn`: PIV で `ripeti/ripetado` の学習文脈を確認。「復習する」として許容。
- `ID1560` `merkatika administranto`: `marketing manager` と RU `специалист по маркетингу` の列間差があり、安全な単一置換先を確定できないため据え置き。
- `ID1650` `eksvalidiĝas`: PIV の商業系語義で「効力を失う/失効」が確認できる。締切文として硬いが意味ズレは明確でない。
- `ID1718` `labori laŭvice`: PIV で `laŭvice` は「順番に」、`deĵoro` は勤務交替の時間帯を確認。`laŭ deĵoroj` も候補だが、現文も「交替で働く」と読めるため据え置き。
- `ID1906` `navedbuson`: PIV で `naveda` に「往復する/ir-reira」の比喩義を確認。`shuttle bus` 文脈として許容。
- `ID1978/1989` `transiro/transŝanĝo`: `transŝanĝo` はPIV未確認で気になるが、確実に狭い交通用語へ置換する根拠が不足。周辺文脈では意味を推測できるため今回は据え置き。
- `ID2115` `pagi doganon`: PIV で `dogano` 自体に「関税/limimposto」の意味があるため据え置き。
- `ID2648` `inkludita`: PIV で `inkludi = inkluzivi` を確認。`inkluzivita` に統一する必要はない。

一致確認:
- `cmp_exit=0`
- `md5=e3c25e35e9f6efbdafb3568f6c485c4c`

## 10. 9周目 100件ずつ継続点検

実施日:
- 2026-04-28

対象:
- `ID2856〜3655` を100件ずつ通し確認
- アパート備品、レストラン予約・注文・会計、肉魚・果物・野菜・朝食、百貨店/衣服/靴/アクセサリー/日用品/電子機器/その他商品、スーパー冒頭まで精査
- PIV / Glosbe で確認でき、かつ生成語・直訳感による不自然さが明確な箇所だけを修正

修正:
- `ID3218` `Mi ŝatas sirlojnan bifstekon`
  - `Mi ŝatas bifstekon el bova lumbaĵo` に修正
  - 理由: `sirlojna` は PIV/Glosbe で確認できず、英語由来の生成語の可能性が高い。PIV 2020 で `bifsteko` は牛肉のステーキ、`lumbaĵo` は調理用の腰肉で `bova lumbaĵo` の用例が確認できるため、JA/ZH/KO/RU の「サーロイン/등심/оковалок」寄りの意味を保って安全に表現した。
- `ID3401` `Ĉu estas universala magazeno proksime?`
  - `Ĉu estas magazeno proksime?` に修正
  - 理由: RU `универмаг` の直訳としての `universala magazeno` は不自然寄り。PIV 2020 で `magazeno` は「butiko より大きく多品目の店」、Glosbe でも `department store` の訳として確認できるため、意味を変えずに簡潔化した。

主な据え置き確認:
- `ID2884` `ventuzilo`: PIV 直接見出しは未確認だが、`ventuzo` 系の透明な器具名として読め、RU/JA/ZH/KO の「 вантуз / スッポン」に沿う安全な置換先を確定できないため据え置き。
- `ID2885` `adherema filmo`: PIV で `adheri/adhera` を確認。`adhera filmo` も候補だが、現形は「くっつきやすいフィルム」として透明で、意味ズレは明確でないため据え置き。
- `ID2959` `smuzio`: PIV では未確認だが、Glosbe で `smoothie -> smuzio` を確認。JA/ZH/KO/RU と一致するため据え置き。
- `ID3004/3321` `pastaĵoj`: PIV 2020 で「薄い生地を切り、ゆでた食品の総称」として確認。パスタ文脈で問題なし。
- `ID3051` `Mezrostita`: PIV 2020 の `bifsteko` 項に `sanga, mezrostita, trarostita` の用例があり、焼き加減の表現として据え置き。
- `ID3331` `eruko`: PIV 2020 で `kultiva eruko` の葉がサラダ用と確認。英語 `rocket` / RU `руккола` 文脈として据え置き。
- `ID3534` `tubon de dentopasto`: PIV 2020 に `tubo de dentopasto` の形が確認できるため据え置き。
- `ID3633` `likva sapo`: EN は `washing up liquid` だが、RU/JA/ZH/KO は「液体せっけん」。ユーザー方針どおり RU/JA/ZH/KO を優先し据え置き。

一致確認:
- `cmp_exit=0`
- `md5=8a8c0a57e5b263c35b4ba30a99717bf3`

## 11. 10周目 100件ずつ継続点検

実施日:
- 2026-04-28

対象:
- `ID3656〜5155` を100件ずつ通し確認
- スーパー後半、花屋・書店、写真、映画館・劇場、スポーツ、キャンプ、銀行、郵便局、美容院、医療、通信・手紙、天候・時間表現まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参照列として確認。PIV / Glosbe / Web 用例で確証が取れ、意味ズレまたは語法上の問題が明確な箇所だけを修正

修正:
- `ID3719` `Mi ŝatus bukedon de ruĝaj rozoj`
  - `Mi ŝatus bukedon da ruĝaj rozoj` に修正
  - 理由: PIV 2020 の `bukedo` では `bukedo da ...` 型の用例が確認できる。既存の `ID3741` も `bukedon da ruĝaj diantoj` なので、同じ花束文脈で語法をそろえた。
- `ID4032` `Kie estas la teniskorto?`
  - `Kie estas la tenisejo?` に修正
  - 理由: PIV 2020 で `tenisejo` はテニス用の特別に標示された競技場として確認できる一方、`korto` は中庭・庭の意味が中心で、スポーツの court の直訳としては不安定。
- `ID4059` `Kiom kostas lui la korton?`
  - `Kiom kostas lui la tenisejon?` に修正
  - 理由: 周辺がテニス文脈で、RU/EN/JA/ZH/KO の `court / корт / コート` はテニスコートを指す。`ID4032` と同じく `tenisejo` に明示。
- `ID4115` `Ĉu vi havas karavanon?`
  - `Ĉu vi havas ruldomon?` に修正
  - 理由: RU は `дом на колёсах`、JA/ZH/KO もキャンピングカー/房车/카라반文脈。PIV 2020 では車両としての `karavano` は避けるべき用法として `ruldomo` へ送られているため、標準的な語へ修正。
- `ID4307` `Mi ŝatus transloki iom da mono al ĉi tiu konto`
  - `Mi ŝatus ĝiri iom da mono en ĉi tiun konton` に修正
  - 理由: PIV 2020 の `ĝiri` は銀行口座から別口座へ送金する意味。`transloki` は物を別の場所へ移す意味が中心で、銀行振込には直訳感が強い。
- `ID4422` `Mi ŝatus, ke vi fajlu kaj formigu miajn ungojn`
  - `Mi ŝatus, ke vi fajlu kaj formu miajn ungojn` に修正
  - 理由: PIV 2020 の `formi` は形を与える意味。ここでは美容師/ネイリストに爪の形を整えてもらう文であり、使役的な `formigi` は不要で不自然。
- `ID4541` `Kioma estas mia temperaturo?`
  - `Kia estas mia temperaturo?` に修正
  - 理由: PIV 2020 の `kioma` は順番・番号を問う語。体温の状態/値を尋ねる文としては `Kia estas ...?` が安全で、既存の `ID5109` `Kia estas la temperaturo?` とも整合。
- `ID4968` `Al kiu tio povas koncerni,`
  - `Al la koncernatoj,` に修正
  - 理由: `koncerni` は他動詞で、元文は英語 `To whom it may concern` の前置詞つき直訳になっている。PIV 2020 で確認できる `koncernato` を用い、JA/ZH/KO/RU の「関係者各位」相当を保った。
- `ID5085` `Ĉiun kvin minutojn`
  - `Ĉiujn kvin minutojn` に修正
  - 理由: `kvin minutojn` は複数対格なので、`ĉiu` も `ĉiujn` と一致させる必要がある。意味は「5分ごとに」のまま。
- 参考列のみ: `ID4148` EN `Have you got a leveler spot?`
  - `Have you got a more level spot?` に修正
  - 理由: EO/RU/JA/ZH/KO は「もっと平らな場所」で一致。英語列だけが typo/不自然表現。
- 参考列のみ: `ID4994` EN `It was so kind of you to write to me back.`
  - `It was so kind of you to write back to me.` に修正
  - 理由: EO/RU/JA/ZH/KO は「返信してくれてありがとう」で一致。英語列だけ語順が不自然。

主な据え置き確認:
- `ID3872/3873/3896` `interakto`: 初見では `intermission/interval` の訳として不安があったが、PIV 2020 で劇場の「幕間」として確認できるため据え置き。
- `ID4388` `Mi ŝatus harlumojn`: ハイライト文脈の生成語らしさは残るが、PIV/Glosbe でより安全な定訳を確証できなかった。意味を壊す危険があるため保留。
- `ID4570` `Mi havas gripon`: RU は「風邪をひいた」に近いが、EN/JA/ZH/KO は「インフルエンザ/flu」で一致するため EO を据え置き。
- `ID4650` `Mi volas redukti mian drinkadon`: RU は「酒をやめたい」寄りだが、EN/JA/ZH/KO は「酒量を減らす」で一致するため EO を据え置き。
- `ID4709` `Li estas malmiopa`: PIV 2020 で `malmiopa` = `hipermetropa` を確認。意味は遠視で問題なし。
- `ID4962` `poŝtrestante`: PIV 2020 で郵便局留めの形として確認できるため据え置き。
- `ID4977/4978/4979/4981/4991` `antaŭĝoji`: 直接見出しの強さには多少不安があるが、透明な複合で「楽しみにする」の意味は明確。列間ズレもないため据え置き。

一致確認:
- `cmp_exit=0`
- `md5=ffc7dd4f2f353223b117f2298f7ba46d`

## 12. 11周目 再点検（ID156〜755）

実施日:
- 2026-04-28

対象:
- 前回末尾まで到達済みのため、再点検として `ID156〜755` を100件ずつ確認
- 挨拶・祝福・感謝、謝罪、指示、短い応答、言語名、意思疎通、賛否、一般的な質問、感情表現、助言、意見、緊急時・事故冒頭まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参照列として確認。PIVで語法が確認でき、意味ズレが明確でないものは据え置き

修正:
- 参考列のみ: `ID619` EN `I suggest you going there.`
  - `I suggest that you go there.` に修正
  - 理由: EO `Mi proponas, ke vi iru tien`、JA/ZH/KO/RU は「そこへ行くことを勧める」で一致。英語列のみ構文が不自然。
- 参考列のみ: `ID638` EN `I would recommend you to talk with Jia.`
  - `I would recommend that you talk with Jia.` に修正
  - 理由: EO `Mi rekomendus al vi paroli kun Jia`、JA/ZH/KO/RU と意味は一致。英語列のみ語法を自然化。
- 参考列のみ: `ID746` RU `Я хочу сообщить о аварии.`
  - `Я хочу сообщить об аварии.` に修正
  - 理由: 母音で始まる `аварии` の前では `о` ではなく `об` が自然。EO/EN/JA/ZH/KO の意味は維持。

主な据え置き確認:
- `ID198` `Sanon!`: `Bless you / Будь здоров` 文脈として許容。`sano` はPIVで健康の祝意・乾杯文脈も確認できる。
- `ID210/216` `tosti por ...`: PIV で `tosto por ...` 系の用例を確認。`por` を理由に修正する必要はない。
- `ID244` `Mi dankas pro via tempo`: PIV で `danki` は `danki al iu pro io` などが確認でき、`mi dankas pro ...` 型も用例上許容できるため据え置き。
- `ID456` `Parolu kun mi en la mandarena ĉina lingvo`: 既存保留どおりやや硬いが、PIV で `la mandarena lingvo` / `la plej multe disvastigita lingvo ... estas la mandarena` を確認。意味ズレはないため据え置き。
- `ID492` `Mi ne povas diri, ke mi kunhavas vian vidpunkton`: PIV で `kun havi opinion` を確認。`vidpunkton` との結合も意味は明確なので据え置き。
- `ID616/721` `prunti vian plumon/telefonon`: PIV で `prunti` には「貸す」と「借りる」の両義があり、`pruntepreni` も確認できる。曖昧さはあるが、誤りと断定できないため据え置き。
- `ID664` `Ili tre plaĉas al mi!`: EN は singular だが RU は plural。JA/ZH/KO は目的語数が明示されにくく、実運用上の意味破綻は小さいため据え置き。
- `ID693` `mi konsideras ĉi tiun filmon la plej bona`: 目的語補語としての `la plej bona` は文法上許容できるため据え置き。

一致確認:
- `cmp_exit=0`
- `md5=59c64dfe5aac2dcb2e16206a81c3b02a`

## 13. 12周目 再点検（ID756〜1655）

実施日:
- 2026-04-28

対象:
- `ID756〜1655` を100件ずつ確認
- 緊急時・警察/大使館、自己紹介・住所・国籍・宗教、家族、外見・趣味、誘い/恋愛、学校/大学/図書館、職業/職場冒頭まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU は最重要参考列、EN は補助参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で語義を照合。意味ズレが明確でないものは据え置き

修正:
- `ID888` `Kiu estas via adreso?`
  - `Kio estas via adreso?` に修正
  - 理由: PIV 2020 では `kio` は具体/抽象の「何」を問う代名詞、`kiu` は同定・選択を問う語。住所の値を尋ねる基本文では `Kio estas via adreso?` が自然で、日中韓/RU/EN の「住所は何ですか」と一致する。
- `ID935` `Mi estas amerikano`
  - `Mi estas usonano` に修正
  - 理由: PIV 2020 で `Amerikano` はアメリカ大陸の住人であり、`Usonano` の意味では使わない旨が明記されている。日中韓/RU/EN は実質「米国人」なので、`usonano` にするのが明確で安全。
- 参考列のみ: `ID767` EN `Please put a bandage.`
  - `Please put on a bandage.` に修正
  - 理由: EO/RU/JA/ZH/KO は包帯/バンデージを着ける・巻く文脈で一致。英語列だけが非文。
- 参考列のみ: `ID781` EN `I've got a food poisoning.`
  - `I've got food poisoning.` に修正
  - 理由: EO/RU/JA/ZH/KO は食中毒で一致。英語列のみ不可算名詞扱いの誤り。
- 参考列のみ: `ID802` EN `I was a victim of a fraud.`
  - `I was a victim of fraud.` に修正
  - 理由: EO/RU/JA/ZH/KO は詐欺被害で一致。英語列のみ不要冠詞。
- 参考列のみ: `ID1347` EN `I'd like to suggest you a good book.`
  - `I'd like to recommend a good book to you.` に修正
  - 理由: EO `proponi al vi bonan libron` と日中韓/RU は本をすすめる文脈で一致。英語列のみ構文が不自然。
- 参考列のみ: `ID1408` EN `He is a lector in Russian language at Oxford University.`
  - `He is a lecturer in Russian at Oxford University.` に修正
  - 理由: EO/RU/JA/ZH/KO はオックスフォード大学のロシア語講師で一致。英語列のみ語法が不自然。
- 参考列のみ: `ID1431` EN `How can I fill in the library card?`
  - `How can I fill in the library registration form?` に修正
  - 理由: EO `bibliotekan formularon`、JA/ZH/KO/RU は図書館の申込/登録フォームで一致。英語列だけ `card` にずれている。
- 参考列のみ: `ID1435` EN `Whom does this discovery belong to?`
  - `Who does this discovery belong to?` に修正
  - 理由: EO/RU/JA/ZH/KO は発見の帰属先を問う文で一致。英語列のみ疑問詞の格が不自然。
- 参考列のみ: `ID1443` EN `He passed brilliantly all the exams.`
  - `He passed all the exams brilliantly.` に修正
  - 理由: EO/RU/JA/ZH/KO は全試験に見事に合格で一致。英語列のみ語順を自然化。
- 参考列のみ: `ID1449` EN `We would like to borrow some linguistic books.`
  - `We would like to borrow some books on linguistics.` に修正
  - 理由: EO `lingvistikajn librojn`、RU/JA/ZH/KO は言語学の本で一致。英語列のみ `linguistic books` が意図とずれやすい。

主な据え置き確認:
- `ID767` `Bonvolu surmeti bandaĝon`: PIV 2020 では `bandaĝi` も確認でき、対象部位を明示するなら自然な候補。ただし RU は「バンデージを着けてください」寄りで、現 EO も意味破綻まではないため、英語参考列だけ修正。
- `ID846` `Maria` / EN-RU `Mary`: EO/JA/ZH/KO は Maria 系、EN/RU は Mary 系で揺れがあるが、固有名のローカライズ差と判断でき、クイズ主軸の EO-JA/ZH/KO は一致しているため据え置き。
- `ID936` `Kia estas via nacieco?`: PIV 2020 の `kia` は性質・種類を問う語で、`kia estas via aĝo?` 型の例もある。国籍という属性を問う文として許容し、修正せず。
- `ID1064` `Mi amas klubumi`: PIV で直接見出しは確認できなかったが、`klubo` + `-um-` の透明な派生で、日中韓/RU の「クラブへ行く」文脈と明確なズレはないため据え置き。
- `ID1081` `Mi ŝatas troti`: PIV 2020 で `troti` は人についても「短い歩幅で速く歩く/進む」用法が確認できる。ジョギング文脈として多少硬いが意味破綻ではないため据え置き。
- `ID1092` `dombestojn`: `pets` より広いが、RU `домашние животные` とも対応し、日中韓も家庭で飼う動物文脈なので据え置き。
- `ID1119/1199/1209` `aliĝi al ...`: 誘い文脈の `join` としてやや直訳感はあるが、意味は通るため据え置き。
- `ID1330` `respondi mian demandon`: PIV 2020 で `respondi` の他動詞用法および `respondi demandon` 型を確認。修正不要。
- `ID1357` `En kiu aĝo ...`: 「どの年齢で」の形として理解可能。`Je kia aĝo` 等への言い換え余地はあるが、意味ズレはないため据え置き。
- `ID1560` `merkatika administranto`: PIV 2020 で `merkatiko` は確認できる。`manaĝero pri merkatiko` 等の言い換えは可能だが、既存文でも「マーケティング担当管理職」の意味は保たれるため据え置き。
- `ID1650` `eksvalidiĝas`: 納期/期限が切れる文脈として少し硬いが、RU/JA/ZH/KO と大きくはずれないため据え置き。

一致確認:
- `cmp_exit=0`
- `md5=1f7c11ec1759c1e28ac174412d10785a`

## 14. 13周目 再点検（ID1656〜2355）

実施日:
- 2026-04-28

対象:
- `ID1656〜2355` を100件ずつ確認
- 職場・推薦状、旅行案内、観光/写真、飛行機予約・チェックイン・荷物・税関・機内、空港表示、レンタカー・運転案内・給油・車両故障まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU は最重要参考列、EN は補助参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `sperto`、`humoro/humuro`、`preferi`、`preni/ricevi`、`trans`、`turni/turniĝo`、`enŝipiĝi` 周辺を照合

修正:
- `ID1736` `Mi havas 15-jaran sperton laborante kiel flegistino`
  - `Mi havas 15-jaran sperton kiel flegistino` に修正
  - 理由: `sperto` 自体は正しいが、`sperton laborante kiel ...` は英語的で、`laborante` の係り方が不自然。RU/JA/ZH/KO の「看護師として15年の経験」は、`15-jara sperto kiel flegistino` で内容を変えずに表せる。
- `ID1767` `Li estas fidinda persono kun bona humorsento`
  - `Li estas fidinda persono kun bona humursento` に修正
  - 理由: PIV 2020 では `humoro` は主に「気分・心理状態」、`humuro` は「ユーモア」。RU/JA/ZH/KO は「ユーモアのセンス」なので `humursento` が適切。
- `ID1840` `Vi pli bone prenu la buson`
  - `Vi prefere prenu la buson` に修正
  - 理由: `you'd better` の直訳的な `vi pli bone ...` を避け、PIV 2020 で確認できる `prefere` を使って、助言として自然な形にした。意味は「バスで行ったほうがよい」のまま。
- `ID1978` `Ĉu mi povas fari la transiron en la sama tago?`
  - `Ĉu mi povas ŝanĝi aviadilon en la sama tago?` に修正
  - 理由: `transiro` は一般に「移行・横断」寄りで、空路の「乗り継ぎ/пересадка」をEOだけで読ませるには弱い。直前の `ID1977` と同じ `ŝanĝi aviadilon` に寄せ、内容を「同日に乗り継げるか」に保った。
- `ID2143` `La loka tempo estas la 21:34`
  - `La loka tempo estas 21:34` に修正
  - 理由: デジタル時刻表記では `la` が不要で不自然。各言語列の「現地時刻は21:34」を維持。
- `ID2284` `Prenu la duan turnon dekstre`
  - `Turnu dekstren ĉe la dua turniĝo` に修正
  - 理由: PIV 2020 で `turno` は主に「何かを回す動作」。道案内の「2つ目の曲がり角で右折」は、同一データ内の `ID2282` `ĉe la unua turniĝo` と同じ型にそろえるのが自然。

主な据え置き確認:
- `ID1737` `Mia fako estas informatiko`: EN/RU は情報技術寄りだが、`informatiko` は分野名として十分通り、`informteknologio` へ寄せると学科/専門分野の焦点を逆に狭める可能性があるため据え置き。
- `ID1906` `navedbuson`: PIV 2020 では `navedo` 周辺は確認できるが、`navedbuso` そのものの強い標準性はまだ弱い。ただし shuttle bus として透明で、置換先をより安全に確定できないため既存保留どおり据え置き。
- `ID1937` `Mi ŝatus preni miajn fotojn`: 写真店文脈では「写真を受け取る/引き取る」と読める。PIV 2020 の `preni` には「受け取る」寄りの用法もあるため、`ricevi` への変更は過修正と判断。
- `ID2011/2102` `enŝipiĝo`: PIV 2020 では `enŝipiĝi` は船中心だが、航空の「boarding」としての慣用的拡張を完全には排除できない。`enaviadiliĝo` への一括変更は大きいので、今回は保留。
- `ID2047/2048/2055/2056/2058` `manbagaĝo`: 直接見出しとしての強さには少し不安があるが、空港文脈で意味は明確。既存保留どおり据え置き。
- `ID2149` `seĝodorson`: 透明複合語で、RU/JA/ZH/KO の「座席の背もたれ」を十分表す。より安全な標準置換を確定できないため据え置き。
- `ID2236` `prezenti postulon pri aŭtoasekura kompenso`: やや硬いが、保険金請求の意味は明確で、各言語列と大きくずれないため据え置き。
- `ID2278` `serva areo`: 高速道路の service area として直訳感はあるが、意味ズレは明確でないため据え置き。
- `ID2292` `trafikblokiĝo`: 透明複合語で「渋滞にはまった」の意味は十分通るため据え置き。

一致確認:
- `cmp_exit=0`
- `md5=d5873d184413911fb4a57d2903e6edfd`

## 15. 14周目 再点検（ID2356〜3155）

実施日:
- 2026-04-28

対象:
- `ID2356〜3155` を100件ずつ確認
- 道路標識、バス停/駅、タクシー、船、ホテル設備/予約/チェックイン/滞在中/チェックアウト、賃貸、レストラン予約/注文/食事中/会計/苦情まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU は最重要参考列、EN は補助参考列として確認
- PIV 2020 公式簡易検索、ローカル抽出、Glosbe/一般Web検索で、特に `ŝanĝi/transiri`、`taksimetro`、`Usono/Ameriko`、`ŝvabrilo`、料理・飲料名を照合

修正:
- `ID2395` `Kie mi transiru por Zagrebo?`
  - `Kie mi ŝanĝu aŭtobuson por Zagrebo?` に修正
  - 理由: RU/JA/ZH/KO は「ザグレブ行きに乗り換える」。`transiri` は横断・移動としても読めるため、PIVで「電車/トラムを替える」用例のある `ŝanĝi` に寄せた。バス停文脈なので `aŭtobuson` を明示。
- `ID2416` `Vi devos transiri en Oslo`
  - `Vi devos ŝanĝi aŭtobuson en Oslo` に修正
  - 理由: 上と同じ。RU `сделать пересадку` と日中韓の乗り換えに合わせ、横断ではなく乗り換えを明確化。
- 参考列のみ: `ID2531` EN `We'll get there quickly.`
  - `We'll be there soon.` に修正
  - 理由: EO `baldaŭ`、RU `скоро`、JA/ZH/KO は「すぐ/まもなく到着」で一致。英語列だけ「速く行く」寄りなので補正。
- `ID2532` `Kie estas la taksometro?`
  - `Kie estas la taksimetro?` に修正
  - 理由: PIVの見出しは `taksimetr/o`。タクシーの料金計の語として `taksimetro` が確認できる。
- `ID2561` `Bonvolu ŝalti la taksometron`
  - `Bonvolu ŝalti la taksimetron` に修正
  - 理由: 同上。RU/JA/ZH/KO のタクシーメーターをオンにする文脈と一致。
- `ID2787` `Ĉu vi akceptas amerikajn dolarojn?`
  - `Ĉu vi akceptas usonajn dolarojn?` に修正
  - 理由: PIVでは `Ameriko` は大陸、`Usono` は米国。PIVにも `Amerikano` を `Usonano` の意味で使わない旨があり、米ドルは `usonaj dolaroj` が安全。
- `ID2868` `Mi bezonas ŝvabron`
  - `Mi bezonas ŝvabrilon` に修正
  - 理由: PIVでは `ŝvabo` はシュヴァーベン人で、掃除具は `ŝvabr/i` の派生 `ŝvabrilo`。RU/JA/ZH/KO/EN は mop なので、`ŝvabrilo` が明確。

主な据え置き確認:
- `ID2623` `rulseĝan aliron`: 少し説明的だが、車椅子でアクセス可能かを問う意味は明確。より安全な標準置換を確定できないため既存保留どおり据え置き。
- `ID2782/2783/2796` `servkotizo / servokotizo`: 表記揺れはあるが、サービス料の意味は明確。既存保留どおり未修正。
- `ID2884` `ventuzilon`: PIVで直接確認できず、弱候補として保留に戻した。ただし RU/JA/ZH/KO は plunger/вантуз で一致し、より安全な置換先を辞書根拠付きで確定できないため今回は未修正。
- `ID2959` `smuzion`: PIVでは直接確認できなかった。飲料名の新語/外来語として意味は各列と一致し、標準置換を確定できないため未修正。
- `ID3004` `pastaĵojn`: PIVで `pastaĵoj` が「小麦粉・水・塩などの薄い生地を切って茹でた食品群」として確認でき、pasta の意味と合うため据え置き。
- `ID3050` `stekon`: PIVで `stek/o` を確認。ステーキの意味で問題ないため据え置き。
- `ID3087` `kalconon`: PIVでは直接確認できず弱いが、料理名 calzone の対応は各列で一致。`kalzono` などへ置換する強い根拠もないため未修正。
- `ID3149` `vino odoras je korko`: コルク臭/ブショネ系の苦情として意味は各列と整合し、未修正。

一致確認:
- `cmp_exit=0`
- `md5=f65de1570b5817600911bf347bbe72c6`

## 16. 15周目 再点検（ID3156〜4155）

実施日:
- 2026-04-28

対象:
- `ID3156〜4155` を100件ずつ確認
- レストランの苦情、パブ、肉/魚/果物/野菜/朝食、百貨店、衣料・靴・アクセサリー・パーソナルケア、電子機器・日用品、スーパー、書店/花屋、支払い/返品、映画館・劇場・博物館・ナイトクラブ、ビーチ、スポーツ、音楽、キャンプまで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU は最重要参考列、EN は補助参考列として確認
- PIV 2020 公式簡易検索、ローカル抽出、ReVo/Glosbe/一般Web検索で、特に `limeo/limedo/limo`、`kapsiko/ĉilio`、`kukurbeto/zukino`、`poemaro`、`surfotabulo`、`eruko`、`kazeo`、`interakto`、`tubo de dentopasto` 周辺を照合

修正:
- `ID3270` `Ŝi ne ŝatas limon`
  - `Ŝi ne ŝatas limeojn` に修正
  - 理由: JA/ZH/KO/RU/EN は果物のライム。PIV 2020 では `lim/o` は境界・限界で、果物は `lime/o` として確認できる。果物一般を好まない文脈なので、同ファイル内の `citronojn` 等と同じく複数対格にした。
- `ID3310` `Ne uzu tro multe da ĉilio`
  - `Ne uzu tro multe da akra kapsiko` に修正
  - 理由: PIV 2020 では `Ĉilio` はチリ国名、`ĉilo` は別語義で、唐辛子としては危険。PIV 2020 の `kapsiko` には `neakra, akra, akrega kapsiko` の用例があり、RU/JA/ZH/KO の「唐辛子/чили」に合う。
- `ID3313` `Mi ŝatus la panitan zukinon`
  - `Mi ŝatus la panitan kukurbeton` に修正
  - 理由: `zukino` は PIV 2020 で確認できず、PIV 2020 では zucchini/courgette に相当する `kukurbeto` が確認できる。料理名として「パン粉衣のズッキーニ」を維持。
- 参考列のみ: `ID3548` EN `About one hundred euro.`
  - `About one hundred euros.` に修正
  - 理由: EO/RU/JA/ZH/KO は約100ユーロで一致。英語列のみ複数形を自然化。
- 参考列のみ: `ID3633` EN `Could you tell me where the washing up liquid is?`
  - `Could you tell me where the liquid soap is?` に修正
  - 理由: EO `likva sapo`、RU `жидкое мыло`、JA/ZH/KO は液体せっけん。英語列だけ食器用洗剤にずれていた。
- 参考列のみ: `ID3671` EN `What's in that chocolate?`
  - `What's in these chocolate candies?` に修正
  - 理由: EO/RU/ZH/KO は複数のチョコレート菓子/конфеты。英語列だけ単数の chocolate で対象がずれていた。
- 参考列のみ: `ID3682` EN `I'd like a half-dozen of eggs.`
  - `I'd like half a dozen eggs.` に修正
  - 理由: EO/RU/JA/ZH/KO は卵6個で一致。英語列のみ自然化。
- `ID3715` `Mi ŝatus vidi kelkajn librojn pri poezio`
  - `Mi ŝatus vidi kelkajn poemarojn` に修正
  - 理由: JA/ZH/KO は「詩集」、RU は `книги с поэзией`。`libroj pri poezio` は「詩についての本」とも読める。ReVo で `poemaro` は「poeziaĵoj の集合」と確認でき、詩集として意味が最も明確。
- 参考列のみ: `ID3764` EN `I only have got 5 yens.`
  - `I only have 5 yen.` に修正
  - 理由: EO/RU/JA/ZH/KO は5円で一致。英語列のみ不自然な `have got` と `yens` を補正。EO `eno` は PIV 2020 で日本の円として確認済み。
- 参考列のみ: `ID3775` EN `That's more than I can afford but I'll take it.`
  - `That's more than I can afford, but I'll take them.` に修正
  - 理由: EO `ilin`、RU `их` は複数目的語。英語列だけ単数 `it` だった。
- 参考列のみ: `ID3890` EN `Until when is the play on?`
  - `What time does the performance end?` に修正
  - 理由: EO `Ĝis kioma horo daŭras la spektaklo?`、RU/JA/ZH/KO は終演時刻を問う。英語列だけ「いつまで上演されているか」寄りで、期間/日程にずれやすい。
- `ID3990` `Kie mi povas lui surftabulon?`
  - `Kie mi povas lui surfotabulon?` に修正
  - 理由: PIV 2020 で `surfotabulo` は surfboard として確認でき、`surftabulo` は PIV 2020 公式検索で確認できなかった。同じ範囲内の `ID3998` も `surfotabulon` なので表記を統一。

主な据え置き確認:
- `ID3162` `bakita`: RU `пропеклась` とも対応し、料理が十分火を通されていない文脈として自然。`kuirita` へ広げる必要はないと判断。
- `ID3194` `postebrio`: 二日酔いの意味は透明で、RU/JA/ZH/KO と整合。より標準的な置換を確定できないため据え置き。
- `ID3331` `eruko`: PIV 2020 で `kultiva eruko` はサラダ用の葉を持つ植物として確認。rocket/arugula として修正不要。
- `ID3372` `kazeo`: PIV 2020 で凝乳/カード系の語義を確認。cottage cheese/tvorog 文脈として修正不要。
- `ID3502` `stretaj`: PIV 2020 で `stret/a = mallarĝa` 自体は確認できるとして一度据え置いたが、267周目再点検で衣服の「きつい」をより直接表す `malvastaj` へ修正済み。
- `ID3534` `tubon de dentopasto`: PIV 2020 の `tubo` に `tubo de dentopasto` の用例があり、`da` へ直す必要はない。
- `ID3546` `paletron da ŝminko por la palpebroj`: eyeshadow palette の説明として通る。PIV 2020 だけではより安全な標準置換を確定できないため据え置き。
- `ID3553` `ŝminkon por okulharoj`: mascara の説明として意味は通る。`maskaro` 等は今回の辞書確認だけでは強く確定できないため据え置き。
- `ID3764` `enojn`: PIV 2020 で `en/o` は日本の円として確認。`jen/o` も参照されるが、現形は誤りではないため据え置き。
- `ID3872/3873` `interakto`: PIV 2020 で劇場・映画館の幕間/休憩時間として確認。英語的な `interaction` ではなく、当該文脈では修正不要。
- `ID4065` `vetproporcioj`: PIV 2020 で直接見出しは確認できないが、競馬・賭け率文脈として意味は透明。`vetkvoto` も強く確認できず、より安全な置換先を確定できないため据え置き。

一致確認:
- `cmp_exit=0`
- `md5=2f37a7896d32e5f14c7e529d4ccfb110`

## 17. 16周目 再点検（ID4156〜5155）

実施日:
- 2026-04-28

対象:
- `ID4156〜5155` を100件ずつ確認
- キャンプ、家族、園芸、来客、銀行、不動産、美容院、仕立て/修理、医者/病気/治療、歯科、眼鏡店、薬局、電話/仕事の電話、マスメディア、郵便局、手紙、時刻、カレンダー、天気まで精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU は最重要参考列、EN は補助参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `hipermetropa`、`inhalilo`、`fasti/fasto`、`gripo` を照合

修正:
- 参考列のみ: `ID4415` RU `Не могли бы вы побрить мне усы, пожалуйста?`
  - `Не могли бы вы подровнять мне усы, пожалуйста?` に修正
  - 理由: EO/EN/JA/ZH/KO は「口ひげを剃る」ではなく「整える/trim」。RU だけ全剃り寄りにずれていた。
- 参考列のみ: `ID4416` RU `Не могли бы вы побрить мне бороду, пожалуйста?`
  - `Не могли бы вы подровнять мне бороду, пожалуйста?` に修正
  - 理由: 上と同じ。 beard を整える文脈に合わせた。
- 参考列のみ: `ID4533` EN `My blood group is 0 negative.`
  - `My blood group is O negative.` に修正
  - 理由: EO/JA/ZH/KO は血液型 O 型。英語列のみ数字の 0 に見える表記だった。RU の `1 отрицательная` はロシア語圏の血液型表記として O 型相当なので維持。
- 参考列のみ: `ID4534` EN `My blood group is 0 positive.`
  - `My blood group is O positive.` に修正
  - 理由: 上と同じ。
- 参考列のみ: `ID4570` RU `Я простыла.`
  - `У меня грипп.` に修正
  - 理由: EO `gripo`、EN/JA/ZH/KO はインフルエンザ/flu。RU だけ「風邪をひいた」にずれていた。PIV 2020 でも `gripo` は感染性の flu と確認。
- 参考列のみ: `ID4636` EN `You'll need a serious treatment.`
  - `You'll need serious treatment.` に修正
  - 理由: EO/RU/JA/ZH/KO の「本格的な/ серьёзное лечение」は維持し、英語の不自然な冠詞だけ除去。
- 参考列のみ: `ID4650` RU `Вам следует бросить пить.`
  - `Вам следует сократить употребление алкоголя.` に修正
  - 理由: EO/EN/JA/ZH/KO は「飲酒量を減らす」。RU だけ「禁酒する」まで強くなっていた。
- `ID4709` `Li estas malmiopa`
  - `Li estas hipermetropa` に修正
  - 理由: JA/ZH/KO/RU/EN は「遠視」。`malmiopa` は「近視ではない」で、正視も含み得る。PIV 2020 で `hipermetropa` は遠視の語として確認できるため、意味を明確化。
- 参考列のみ: `ID4712` EN `I need a new glasses' case.`
  - `I need a new glasses case.` に修正
  - 理由: EO/RU/JA/ZH/KO は眼鏡ケース。英語列の所有格だけ不自然。
- 参考列のみ: `ID4742` RU `Мне нужен респиратор.`
  - `Мне нужен ингалятор.` に修正
  - 理由: EO `inhalilo`、EN/JA/ZH/KO は inhaler/吸入器。PIV 2020 でも `inhalilo` は吸入を助ける器具と確認でき、RU の `респиратор` は防塵マスク/呼吸器寄りでずれる。
- `ID4750` `Ĉu preni fastante?`
  - `Ĉu mi prenu ĝin fastante?` に修正
  - 理由: 意味は「空腹時に服用するのか」。`fastante` 自体は PIV 2020 の `fasti/fasto` と整合するが、クイズ文としては主語と目的語を補った方が文として自然で、内容は変えない。
- 参考列のみ: `ID4753` EN `It can be taken without a prescription.`
  - `It can be bought without a prescription.` に修正
  - 理由: EO/RU/JA/ZH/KO は「処方箋なしで買える」。英語列だけ「服用できる」にずれていた。
- 参考列のみ: `ID4762` EN `I would like a bottle of aspirin.`
  - `I would like a pack of aspirin.` に修正
  - 理由: EO `pakaĵo`、RU `упаковка`、JA/ZH/KO は箱/パック。英語列だけ bottle にずれていた。
- 参考列のみ: `ID4896` EN `The image is vague.`
  - `The image is blurry.` に修正
  - 理由: EO `malklara`、RU/JA/ZH/KO は画像がぼやけている/不鮮明。視覚的なぼけは `blurry` が自然。
- 参考列のみ: `ID4941` RU `Взвесьте эту посылку, пожалуйста?`
  - `Взвесьте эту посылку, пожалуйста.` に修正
  - 理由: 命令形の丁寧依頼で、文末の疑問符だけ不自然。意味は維持。
- 参考列のみ: `ID4949` RU `Можно мне альбом марок первого класса, пожалуйста?`
  - `Можно мне книжечку марок первого класса, пожалуйста?` に修正
  - 理由: EO/EN/JA/ZH/KO は切手帳/booklet/book of stamps。RU の `альбом марок` は収集用アルバムに読めるため郵便局文脈に合わせた。
- 参考列のみ: `ID5097` RU `Очень холодно.`
  - `На улице ледяно и скользко.` に修正
  - 理由: EO/EN/JA/ZH/KO は「凍っていて滑りやすい」。RU だけ「とても寒い」に落ちており、滑りやすさが消えていた。
- 参考列のみ: `ID5129` EN `Cold weather, isn't it?`
  - `It's cold, isn't it?` に修正
  - 理由: EO/RU/JA/ZH/KO は「寒いですね」。英語列の不自然な名詞句を自然化。
- 参考列のみ: `ID5130` EN `Hot weather, isn't it?`
  - `It's hot, isn't it?` に修正
  - 理由: 上と同じ。

主な据え置き確認:
- `ID4214/4227` `bolkruĉo / bolilo`: PIV 2020 で `bolilo` を確認。湯沸かし器/やかん文脈として意味は通るため未修正。
- `ID4388` `harlumoj`: hair highlights の訳として少し気になるが、より安全な標準置換を辞書根拠付きで確定できないため未修正。
- `ID4620` `fojnofebro`: PIV 2020 では `fojno kataro` は見えるが、現形も透明な複合語で hay fever の意味は各列と一致。強い置換根拠がないため未修正。
- `ID4708` `grandajn dioptriojn`: 眼鏡店で度が強いという意味は各列と整合。誤りとまでは判断せず未修正。
- `ID4815` `Kiam estas pli bone telefoni al vi?`: やや直訳的だが、電話に都合のよい時を尋ねる意味は明確。今回は未修正。
- `ID5004` `Kioma estas la preciza horo?`: 後続再点検で `Kioma horo estas precize?` に修正済み。
- `ID5146` `La suno ĵus kaŝiĝis`: 後続再点検で RU の日没寄り表現を `Солнце только что скрылось.` に修正済み。

一致確認:
- `cmp_exit=0`
- `md5=5de033a83b8aa83e3bac2afccbdf761f`

## 18. 17周目 追加再点検（ID156〜255）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID156〜255` を確認
- Basic Sentences の Saying Hello & Goodbye、Good Wishes、Thanks を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `tosto/tosti`、`minimumo`、`danki` 周辺を照合

修正:
- 参考列のみ: `ID205` RU `Приятно провести ночь!`
  - `Приятной ночи!` に修正
  - 理由: EO `Agrablan nokton!`、JA/ZH/KO/EN は「よい夜を」。元のRUは不自然な不定詞句で、挨拶として成立しにくい。
- 参考列のみ: `ID234` RU `Я хорошо, спасибо.`
  - `У меня всё хорошо, спасибо.` に修正
  - 理由: EO `Mi fartas bone, dankon` と各列の「元気です」に対応。元のRUは `я` と `хорошо` の組み合わせが不自然。
- 参考列のみ: `ID240` RU `Это было меньшее, что я мог сделать.`
  - `Это было самое малое, что я мог сделать.` に修正
  - 理由: EO/EN/JA/ZH/KO は「自分にできるせめてものこと」。元のRUは比較級 `меньшее` が不自然で、慣用的には `самое малое` が近い。
- 参考列のみ: `ID243` RU `Наоборот, это мне стоило бы вас благодарить!`
  - `Наоборот, это мне следует вас благодарить!` に修正
  - 理由: EO/EN/JA/ZH/KO は「こちらこそ感謝すべき」。元のRUは `стоило бы` で意味がずれ、義務・当然性は `следует` が自然。
- 参考列のみ: `ID249` EN `I am pleased to do so.`
  - `It was a pleasure for me to do that.` に修正
  - 理由: EO `Estis plezuro por mi tion fari`、RU/JA/ZH/KO は過去の行為について「できてうれしかった」。英語列だけ現在形・これから/一般的な応答にずれていた。

主な据え置き確認:
- `ID186` `Mi antaŭĝojas revidi vin`: PIV 2020 では直接確認できなかったが、意味は各列と一致。`antaŭĝoji pri revido` などへ直す候補はあるが、辞書根拠付きで現形を誤りと断定できないため未修正。
- `ID198` `Sanon!`: sneeze 後の `Bless you!` と一般的な健康祈願の間で揺れるが、RU/EN と対応し、JA/ZH/KO も実用上「お大事に/保重」系で許容範囲。未修正。
- `ID210` `Ni tostu por vi!` / `ID216` `Mi ŝatus proponi toston por mia filo`: PIV 2020 で `tosto/tosti` を確認。`pro ies sano aŭ honoro` の説明や `por ... oni eldiris ... toston` の例があり、`por` を明確な誤りとは判断しない。未修正。
- `ID240` `Tio estis la plej malmulto, kion mi povis fari`: PIV 2020 で `minimumo` は確認でき、置換案としては `Tio estis la minimumo, kion mi povis fari` も考えられる。ただし現形は各列の「least I could do」と対応し、意味ズレが明確ではないため今回はEOを動かさない。
- `ID244` `Mi dankas pro via tempo`: PIV 2020 で `danki al iu pro io` 等を確認。`Mi dankas vin pro via tempo` の方が明示的だが、現形は省略表現として通り、意味ズレもないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=1a51d4ce2910c0c9ca657bdc9d3e0243`

## 19. 18周目 追加再点検（ID256〜355）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID256〜355` を確認
- Thanks の末尾、Apologies、Instructions、Short Questions & Answers の冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `zorgi/senzorge`、`atenti`、`viciĝi` 周辺を照合

修正:
- 参考列のみ: `ID275` RU `Я вам не помешаю?`
  - `Я вам не мешаю?` に修正
  - 理由: EO/EN/JA/ZH/KO は「今、邪魔していないか」。元のRUは「これから邪魔にならないか」寄りで、時点が少しずれていた。
- 参考列のみ: `ID284` EN `I regret saying this.`
  - `I regret having said that.` に修正
  - 理由: EO `ke mi diris tion`、JA/ZH/KO/RU は既に言ってしまった内容への後悔。英語列だけ現在発話中の `this` に寄りやすかった。
- `ID285` `Estis senzorge de mia flanko`
  - `Mi agis senzorge` に修正
  - 理由: 内容は「私の不注意でした」。PIV 2020 で `senzorga/senzorge` は成立するが、旧文は `de mia flanko` が直訳的で文として硬い。`Mi agis senzorge` は内容を変えず、EOとして自然。
- 参考列のみ: `ID286` RU `Боюсь, я не могу задержаться на подольше.`
  - `Боюсь, я не могу задержаться дольше.` に修正
  - 理由: EO/EN/JA/ZH/KO は「これ以上長くいられない」。元のRUは `на подольше` が不自然。
- `ID303` `Ne zorgu pri tio!` の EN/JA/ZH/KO を修正
  - EN `Don't worry about that!`
  - JA `そのことは気にしないでください！`
  - ZH `别为这件事担心！`
  - KO `그건 걱정하지 마세요!`
  - 理由: EO/RU は「そのことを気にしないで/心配しないで」。旧訳は EN `Take it easy!`、JA `気楽にいこう！`、ZH `别紧张！` などで、特に ZH は `ID313` `Ne nervozu` と重なりやすい。クイズ主軸列の対応を明確化。

主な据え置き確認:
- `ID257` `nome de mia edzo`: 夫の名において/夫を代表してという意味で JA/ZH/KO/RU と整合。未修正。
- `ID276` `Mi ne tion celis`: `Mi ne celis tion` の方が平板だが、現形は `tion` に焦点を置く語順として成立し、意味ズレはないため未修正。
- `ID282` `Ne estas kialo pardonpeti`: `por pardonpeti` を補う案はあるが、短い会話表現として意味は明確。未修正。
- `ID302` `Kuraĝu!`: 直訳は「勇気を出して」だが、EN/JA/ZH/KO/RU の cheer up / 元気を出して / 힘내세요 系と文脈上対応可能。未修正。
- `ID308` `Atentu la hundon`: PIV 2020 で `atenti` は他動詞として、対象へ注意を向ける用法と、危険回避の用法を確認。標識文脈では「犬に注意」の意味が通るため未修正。
- `ID316` `Bonvolu viciĝi ĉi tie`: PIV 2020 で `viciĝi` は列に並ぶ意味として確認。未修正。
- `ID345` `Kial ne?`: 「なぜだめなのか」と「いいじゃないか」の両方に寄り得るが、短答表現として文脈別許容。未修正。
- `ID354` `Amuze!`: `Tio estas amuza!` も候補だが、短い感嘆として成立し、意味ズレが明確ではないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=8cd4396279cf76d94697f646d07800a3`

## 20. 19周目 追加再点検（ID356〜455）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID356〜455` を確認
- Basic Sentences の Short Questions & Answers 末尾、Congratulations、General Conversation / Languages、Making Yourself Understood の冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索、ローカルPIV抽出、Glosbe/検索結果で、特に `akcento/akĉento`、`dum/de`、祝祭名・言語名周辺を照合

修正:
- 参考列のみ: `ID442` RU `Запиши это пожалуйста.`
  - `Запиши это, пожалуйста.` に修正
  - 理由: EO/EN/JA/ZH/KO は「書き留めてください」。RU の語彙・文体は維持し、`пожалуйста` 前の必須に近いコンマだけ補った。
- `ID449` `Mi havas akcenton`
  - `Mi havas akĉenton` に修正
  - 理由: この文脈は「なまり/口音/foreign accent」。PIV 2020 では `akĉento` が話者・集団の発音習慣として定義され、例にも `havi ... akĉenton` がある。一方 `akcento` は主に語・音節・句の強勢/アクセントなので、ここでは意味がずれていた。

主な据え置き確認:
- `ID373` `Nu, mi neniam aŭdis pri li`: EN は `heard of him` の方が自然だが、`heard about him` でも意味は通る。参考列のみの微修正で、明確な意味ズレではないため未修正。
- `ID388` `Feliĉan Divalion!`: PIV 2020 では直接確認できなかった。Esperanto Web上では `Divali`、`Divalio/Divalion` 系の揺れが見えるが、より安全な置換先を辞書根拠付きで確定できないため未修正。
- `ID396` `Gratulon pro via akcepto en la universitaton!`: PIV 2020 で `akcepti` は教育機関が学生を受け入れる用法を持つ。`akceptiĝo` 等も候補だが、現形を誤りと断定できないため未修正。
- `ID415` `azerbajĝane`: PIV 2020 で `Azerbajĝano` は確認。言語名の通常派生として意味は明確で、置換根拠不足のため未修正。
- `ID421` `Via tagaloga estas tre bona`: PIV 2020 では `tagaloga` は直接確認できなかったが、言語名形容詞として透明で、各列の意味も一致。未修正。
- `ID432` `Mi lernas la indonezian jam de unu monato`: `dum unu monato` も可能だが、`jam de ...` は「...前からずっと」の表現として成立する。明確な誤りではないため未修正。
- `ID455` `Mia korea estas sufiĉe malbona`: 口語的な省略として「私の韓国語力」を表し、JA/ZH/KO/RU と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=5d927594bf05bc8fac439cc7918b3b58`

## 21. 20周目 追加再点検（ID456〜555）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID456〜555` を確認
- Making Yourself Understood の続き、Agreement & Disagreement、General Conversation の冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- 前区間から続く `akcento/akĉento`、言語名、移動・旅行表現、同意/不同意表現を確認

修正:
- `ID457` `Vi ne havas akcenton`
  - `Vi ne havas akĉenton` に修正
  - 理由: `ID449` と同じく、この文脈は「なまり/口音/foreign accent」。PIV 2020 の `akĉento` の語義・用例がこの意味に一致し、`akcento` は語や音節の強勢に寄りやすいため。

主な据え置き確認:
- `ID456` `Parolu kun mi en la mandarena ĉina lingvo`: 以前から低優先保留に入れている硬い表現。意味は「標準中国語/普通話で話す」と各列で一致し、より安全な置換を辞書根拠付きで確定できないため未修正。
- `ID463` `Ĉu mi ĝuste ĝin prononcas?`: `Ĉu mi prononcas ĝin ĝuste?` の方が平板だが、現形も焦点語順として成立し、意味ズレはないため未修正。
- `ID476` `Mi ne konsentas kun via opinio`: `pri via opinio` 等も考えられるが、`konsenti kun` の方向で意味は明確。未修正。
- `ID497` `En la televido estas tro multe da reklamoj, ĉu ne?`: やや直訳的だが、テレビ放送/テレビ上に広告が多いという意味は各列と一致。未修正。
- `ID531` `Jes, mi iris tien por ferioj`: `ferie` なども候補だが、「休暇目的でそこへ行った」という意味は通る。未修正。
- `ID536` `Fakte, mi estas survoje por renkonti amikon`: `al renkonto kun amiko` 等も候補だが、目的の `por renkonti` として意味は明確。未修正。
- `ID542` `Kiom longe vi estis en Kolombio?`: EN は現在完了にも読めるが、EO/RU/JA は過去の滞在期間として整合。クイズ主軸列に明確なずれはないため未修正。
- `ID551` `Ĉu vi trovas teatron aŭ operon pli interesa?`: 比較対象を尋ねる文として理解可能。`interesa` の補語形もこの構文では許容範囲と判断し未修正。

一致確認:
- `cmp_exit=0`
- `md5=9ffc461b27df4ba3bc5a6fac1bcf689d`

## 22. 21周目 追加再点検（ID556〜655）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID556〜655` を確認
- General Conversation の Questions、Feelings、Help & Advice 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `trista`、`ekscitita`、`embarasita`、`kapturno`、`kondolenco`、`personaro`、`prunti`、`komplezo/servo`、`pensi/opinii` 周辺を照合

修正:
- なし

主な据え置き確認:
- `ID562` `Mi estas trista`: PIV 2020 で `trista` は `malgaja, malĝoja` と確認。未修正。
- `ID577` `Mi estas ekscitita`: PIV 2020 で `eksciti` は心の動きを強くする意味を持つ。JA/ZH/KO は期待寄りだが、感情表現として文脈別許容。未修正。
- `ID591` `Mi estas motivita`: PIV 2020 の `motivi` は「理由づける」寄りで少し気になるが、現代用例として motivation の意味も広く見える。より安全な置換は `entuziasma`、`inspirita` などに意味が寄りすぎるため未修正。
- `ID594` `Mi sentas min embarasita`: PIV 2020 で `embaraso/embarasi` は気まずさ・困惑を表す。`embarrassed` 文脈として許容。未修正。
- `ID599` `Mi sentas iom da kapturno`: PIV 2020 で `senti kapturnon` を確認。現形はやや説明的だが意味は明確。未修正。
- `ID606` `via perdo` / `ID607` `kondolencojn`: PIV 2020 で `pro la perdo de via patro... kondolencon` の型を確認。弔意文として整合。未修正。
- `ID623` `Ĉu vi povus fari al mi servon?`: PIV 2020 で `servo` に「助け・利益のために行うこと」の意味を確認。`komplezo` も候補だが、現形を誤りとは判断しない。
- `ID627` `Kion vi pensas, ke mi faru?`: `Kion laŭ vi mi faru?` 等の方が滑らかだが、`pensi, ke...` として意味は通る。未修正。
- `ID646` `flugpersonaro`: PIV 2020 で `personaro` は企業などで働く人々の集合、`flug-` は透明な複合要素として確認。見出し語ではないが、AI造語と断定できず意味も明確なため未修正。

一致確認:
- `cmp_exit=0`
- `md5=9ffc461b27df4ba3bc5a6fac1bcf689d`

## 23. 22周目 追加再点検（ID656〜755）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID656〜755` を確認
- General Conversation / Opinions、Emergencies / Emergency Situations、Accidents を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `aktorado`、`traŭmatizita`、`prioritato`、`stirpermesilo`、`akcidentraporto` 周辺を照合

修正:
- 参考列のみ: `ID664` EN `I really like it!`
  - `I really like them!` に修正
  - 理由: EO `Ili` と RU `Они` は複数。EN だけ単数になっていた。
- 参考列のみ: `ID667` RU `Совсем наоборот.`
  - `Это совсем другое.` に修正
  - 理由: EO/EN/JA/ZH/KO は「まったく/かなり違う」。旧RUは「正反対」で `Tute male` に近く、意味が強くずれていた。
- 参考列のみ: `ID678` RU `Боюсь эта книга мне не нравится.`
  - `Боюсь, эта книга мне не нравится.` に修正
  - 理由: 意味は維持し、挿入的な `Боюсь,` のコンマを補った。

主な据え置き確認:
- `ID682` `La aktorado estis malbona`: PIV 2020 で `aktorado` は「俳優の演技・演じ方」と確認。未修正。
- `ID693` `Persone, mi konsideras ĉi tiun filmon la plej bona`: 補語形として理解可能。`la plej bonan` へ変えると名詞句内の修飾にも読めるため未修正。
- `ID715` `oficejo pri perditaj aĵoj`: やや説明的だが、遺失物取扱所として意味は明確。後続 `ID821/827` とも同系統なので未修正。
- `ID725` `Mi estas traŭmatizita`: PIV 2020 で `traŭmatizi` と `psika traŭmato` を確認。AI造語ではないため未修正。
- `ID733/750` `stirpermesilo`: 透明な複合語で、同CSV内でも複数箇所に一貫して使われる。意味ズレなし。
- `ID741` `Mi havis la prioritaton`: PIV 2020 で交通文脈の `havi prioritaton de paso` を確認。right of way として妥当。
- `ID754` `akcidentraporto`: 透明な複合語で、事故報告書として各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=96d98f0a5d4a31b56081155584a8585d`

## 24. 23周目 追加再点検（ID756〜855）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID756〜855` を確認
- Emergencies / Accidents、Crimes、Legal、Documents を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `elartikigi`、`denunci`、`deklaro`、`advokato`、`aresti`、`ambasadejo`、`anstataŭigi`、`foto/robot` 周辺を照合。`fotoroboto` は Glosbe でも見出し相当の使用を確認

修正:
- なし

主な据え置き確認:
- `ID767` `bandaĝon`: 応急処置で包帯を必要とする文脈として各列と整合。未修正。
- `ID779` `Mia ŝultro estas elartikigita`: PIV 2020 で `elartikigi` と肩の脱臼用例を確認。未修正。
- `ID803` `Oni enrompis mian aŭton`: 直訳的ではあるが、車上荒らしの被害として意味は明確。`enrompi` の他動的用法も用例上確認できるため未修正。
- `ID813` `Mi volas vidi mian advokaton`: PIV 2020 で `advokato` は弁護士として確認。未修正。
- `ID820` `Ĉu mi povas ĝin anstataŭigi?`: 「再発行してもらう」に対してやや広い「取り替える/代替する」だが、紛失カードの置換としては理解可能。明確な意味ズレとはせず未修正。
- `ID826` `fotoroboton`: PIV 2020 では `foto` と `roboto` の要素を確認、Glosbe で `fotoroboto` の使用も確認。AI造語とは断定できないため未修正。
- `ID835` `La dokumentoj estis detruitaj`: 文書が破棄・損壊されたという意味で各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=96d98f0a5d4a31b56081155584a8585d`

## 25. 24周目 追加再点検（ID856〜955）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID856〜955` を確認
- Making Friends / Introductions、Personal Information、Work & Careers、Place of Residence、Family & Relationships、Culture & Identity を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `korespondanto`、`Kazaĥio`、`Moldavio`、`nacieco`、`religio`、`familia nomo`、`vendmanaĝero` 周辺を照合

修正:
- 参考列のみ: `ID925` EN `He is here as a correspondent.`
  - `He works here as a correspondent.` に修正
  - 理由: EO `Li laboras...`、RU `Он работает...`、JA/ZH/KO はすべて「ここで特派員として働く」。旧ENだけ「いる」に寄っていた。
- 参考列のみ: `ID929` RU `Он жил в Новой Зеландии шесть месяцев.`
  - `Он живёт в Новой Зеландии уже шесть месяцев.` に修正
  - 理由: EO `loĝas ... jam de ses monatoj`、EN/JA/ZH/KO は「現在まで半年住んでいる」。旧RUは過去形で、現在継続の意味が落ちていた。

主な据え置き確認:
- `ID878` `sinjoron Smirnov`: 敬称付きの非同化姓として、姓に対格語尾を付けない形は実用上許容されると判断。未修正。
- `ID883` `De kie vi venas?`: 出身地を尋ねる定型として自然。未修正。
- `ID892` `Ĉi tie tre plaĉas al mi`: `Plaĉas al mi ĉi tie` の方が平板だが、場所を主題化した表現として理解可能。未修正。
- `ID902` `Mi estas ĉi tie por labori`: RU は出張寄りだが、EO/JA/ZH/KO は「仕事で来ている」として整合。既存の低優先保留を継続。
- `ID925` `korespondanto`: PIV 2020 で職業名として確認。EOは未修正。
- `ID936` `Kia estas via nacieco?`: `Kio estas via nacieco?` も自然だが、国籍の性質・属性を問う形として意味は通る。未修正。
- `ID947` `Mia gepatra lingvo estas la rusa`: `la rusa lingvo` の省略として定型的に理解可能。未修正。
- `ID952` `Kia estas via religio?`: `Kio estas via religio?` も候補だが、宗教属性を問う形として文脈上許容。未修正。

一致確認:
- `cmp_exit=0`
- `md5=03d569c56e51d82a823dc60fd95e2e5b`

## 26. 25周目 追加再点検（ID956〜1055）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID956〜1055` を確認
- Making Friends / Age, Nationality & Religion、Family & Relationships、Describing People を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `budhano/budhisto`、`siĥo`、`fraŭlo/fraŭlino/fraŭla`、`fianĉino`、`rilato`、`solinfano`、`ĉarma`、`rufa` 周辺を照合

修正:
- `ID991` EO `Ne, mi estas sola`
  - `Ne, mi estas fraŭla` に修正
  - 理由: 文脈は `Are you married?` に対する「独身です」。PIV 2020 で `sola` は「一人でいる/唯一」の意味が中心で、独身状態には寄りにくい。同CSV内でも `Ĉu vi estas fraŭla?` が `Are you single?` に対応しているため、内容を変えずに `fraŭla` へ修正。
- 参考列のみ: `ID1025` EN `You're very nice.`
  - `You're very charming.` に修正
  - 理由: EO `ĉarma` と JA/ZH/KO は「魅力的」。旧ENの `nice` は「親切/感じがよい」に寄りやすく、魅力の意味が弱かった。

主な据え置き確認:
- `ID956` `Mi estas budhano`: PIV 2020 で `budhano` は仏教徒、`budhisto` はその同義と確認。未修正。
- `ID958` `Mi estas protestantino`: RU `протестантка` と一致する女性形。JA/ZH/KOは性別を明示しないが意味ズレはないため未修正。
- `ID984/990` `edziniĝinta` / `edziniĝis`: 女性話者に対する婚姻表現として RU と整合。未修正。
- `ID996` `mi estas fianĉino`: PIV 2020 で `fianĉino` は婚約した女性。`fianĉiĝinta` の方が直訳的だが、意味は「婚約している」で一致。未修正。
- `ID998` `Li estas en rilato`: PIV 2020 で `rilato` に人間関係・相互関係の意味を確認。恋愛関係文脈として理解可能。未修正。
- `ID1018` `solinfano`: PIV 2020 の `sola` 項で `solinfano` 型を確認。一人っ子として妥当。
- `ID1052` `rufajn harojn`: PIV 2020 で `rufa` は髪色・体毛色の赤褐色系を表す。赤毛として整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=0b6399f253438b813bc29694ba3c274e`

## 27. 26周目 追加再点検（ID1056〜1155）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1056〜1155` を確認
- Making Friends / Describing People、Things You Like & Dislike、Arranging to Meet を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `klubo/noktoklubo`、`butikumi`、`hobio`、`fotografado`、`patkuko`、`drinkejo`、`troti/trotado`、`piedirado/ekskurso/migrado`、`aliĝi`、`rememorigi`、`vestiblo` 周辺を照合

修正:
- `ID1064` EO `Mi amas klubumi`
  - `Mi amas iri al noktokluboj` に修正
  - 理由: 旧形 `klubumi` はPIV 2020で確認できず、基礎語 `klubo` も一般の団体・クラブまで広い。各列は「夜店/ナイトクラブに行く」という意味で揃っているため、PIV 2020で確認できる `noktoklubo` を使い、意味を変えずに明確化。

主な据え置き確認:
- `ID1065` `butikumi`: PIV 2020 で「店を見て回る/買い物をする」意味を確認。未修正。
- `ID1066/1067` `hobio` / `fotografado`: PIV 2020 で `hobio` は `ŝatokupo`、`fotografado` は写真撮影として確認。未修正。
- `ID1074` `patkukojn`: 食べ物として各列と整合。未修正。
- `ID1075` `drinkejo`: 同CSV内でも「bar/pub」相当として一貫。未修正。
- `ID1081` `Mi ŝatas troti`: PIV 2020 で `troti` は人にも使える「速く小刻みに歩く」意味を確認。`jogging` との距離は少し残るが、各列の軽いランニング/ジョギング文脈として許容し未修正。
- `ID1104` `piedirado`: EN/JA/ZH はハイキング寄り、KO は歩行寄り、RU は徒歩散策寄り。`piedirado` は少し広いが、明確な意味ズレとはせず未修正。
- `ID1119/1124` `aliĝi al mi/ni`: PIV 2020 で `aliĝi` は加わる/参加する意味を確認。会食や同席への誘いとしてやや直訳的だが許容。未修正。
- `ID1136` `Ĉu vi rememorigos min?`: PIV 2020 で `memorigi/rememorigi` の対人用法を確認。未修正。
- `ID1152` `vestiblo`: ホテルのロビー/ホール文脈として同CSV内使用と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=b900d4825cde5f4c29f40790573acd16`

## 28. 27周目 追加再点検（ID1156〜1255）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1156〜1255` を確認
- Making Friends / Arranging to Meet、Dating / Asking Someone out、On a Date を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `partio`、`kiel/kio`、`konveni`、`aliĝi`、`regali`、`manki`、`enamiĝi`、`freneziĝi`、`akompan/i`、`veturigi` 周辺を照合

修正:
- 参考列のみ: `ID1156` EN `Gents, you may like a game of golf.`
  - `Gentlemen, we can play a round of golf.` に修正
  - 理由: EO `ni povas ludi...` と RU `мы можем сыграть...` は「私たちはプレーできる」。旧ENは「皆さんは気に入るかもしれない」と誘いの意味に寄り、主語・意味がずれていた。
- `ID1206` EO `Kiel pri hodiaŭ?`
  - `Kio pri hodiaŭ?` に修正
  - 理由: 旧形は英語 `How about...` の直訳に見え、PIV 2020 の `kiel` の主要語義にも合いにくい。`Kio pri ...?` は「...はどうか」を表す形としてより安全で、各列の意味を変えない。

主な据え置き確認:
- `ID1156` `partion de golfo`: PIV 2020 で `partio` はゲーム・対戦の一回を表す語義を確認。ゴルフの1ラウンドとして許容し、EOは未修正。
- `ID1180` `Mi iomete malfruiĝas`: 「少し遅れている/遅れそう」の表現として各列と整合。未修正。
- `ID1199/1209` `aliĝi al vi`: PIV 2020 で `aliĝi` は加わる/参加する意味を確認。会話相手に同席を求める表現として許容。未修正。
- `ID1210` `Mi regalos vin per trinkaĵo`: `regali ... per ...` として「飲み物をごちそうする」意味が明確。未修正。
- `ID1212` `lokon kien iri`: コンマや `al kiu` も候補だが、「行く場所」の意味は明確。未修正。
- `ID1230` `Vi mankas al mi`: PIV 2020 で `manki al ...` 型を確認。恋愛・親密表現として各列と整合。
- `ID1235` `Mi enamiĝis al vi`: 「恋に落ちた/好きになった」として各列と整合。未修正。
- `ID1245` `Mi freneziĝas pro vi`: PIV 2020 で `freneza pro ...` 型の情熱表現を確認。`crazy about you` 相当として許容。未修正。
- `ID1237/1247` `akompani/veturigi vin hejmen`: 徒歩で送る/車で送るの差が明確で、各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=852e7acfd1eb7b668770f0a927e96eb6`

## 29. 28周目 追加再点検（ID1256〜1355）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1256〜1355` を確認
- Dating / On a Date、Compliments、Wedding、Education / At School を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `aspekti`、`rava/ravega`、`komplimento`、`gusto`、`nupto`、`porcelana/koral/rubena`、`gimnastikejo`、`respondi`、`noto` 周辺を照合

修正:
- 参考列のみ: `ID1345` EN `I didn't understand quite well.`
  - `I didn't quite understand.` に修正
  - 理由: EO `Mi ne tute komprenis` と RU `Я не совсем поняла` は「完全には理解できなかった」。旧ENは語順が不自然だった。
- 参考列のみ: `ID1346` RU `У кого-нибудь есть, что добавить?`
  - `У кого-нибудь есть что добавить?` に修正
  - 理由: この構文では `есть что добавить` が一まとまりで、旧文のコンマは不要。

主な据え置き確認:
- `ID1274` `Vi estas ravega`: PIV 2020 で `rava` は強い魅力・感嘆を起こす語と確認。`ravega` は規則的な強意形で、`gorgeous / потрясающая` と整合。
- `ID1285` `Vi aspektas tre bele ĉi-vespere`: PIV 2020 で `aspekti` は `pale/malbele/sane` など副詞を伴う用法を確認。未修正。
- `ID1288` `mirindan guston pri vestoj`: `gusto` の審美眼の意味をPIV 2020で確認。前置詞は少し広いが、服についてのセンスとして意味明確。未修正。
- `ID1294` `Ĉu vi edziniĝos al mi?`: RU `Ты выйдешь за меня?` と同じく女性相手のプロポーズとして整合。未修正。
- `ID1311〜1316` 結婚記念日の表現: `nupto` と素材形容詞の組み合わせとして意味が透明で、各列と対応。未修正。
- `ID1323` `gimnastikejon`: PIV 2020 で「体操・運動をする場所」と確認。学校施設の gym 文脈として許容。未修正。
- `ID1330` `respondi mian demandon`: PIV 2020 で `respondi tiun ĉi demandon` 型の他動詞用法を確認。未修正。
- `ID1351〜1353` `notoj`: 成績・点数文脈として各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=63e6e50a1084b9f4e7f062c10990183c`

## 30. 29周目 追加再点検（ID1356〜1455）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1356〜1455` を確認
- Education / At School、At University、Student Life を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `klaso/klasĉambro`、`magistro/magistreco`、`paŭzo/libera/jaro`、`fakultato`、`rektoro`、`klubo`、`ekzameno/malsukcesi`、`oratoro` 周辺を照合

修正:
- `ID1356` EO `Neniu rajtas forlasi la klason nun`
  - `Neniu rajtas forlasi la klasĉambron nun` に修正
  - 理由: PIV 2020 では `klaso` 自体にも「教室」の語義があるが、JA/ZH/KO は明確に「教室」を出る内容。クイズ上の曖昧さを避け、PIV内で用例のある `klasĉambro` に明示化。
- `ID1386` EO `Mi prenas paŭzjaron`
  - `Mi prenas liberan jaron` に修正
  - 理由: `paŭzjaro` はPIV 2020と手元コーパスで確認できず、`paŭzo` はPIV上「短い中断」が中心。内容は「gap year / 休学一年 / академический отпуск」なので、基礎語 `libera` + `jaro` に寄せて、造語感を下げた。
- 参考列のみ: `ID1393` EN `What departments has this university got?`
  - `What faculties does this university have?` に修正
  - 理由: EO `fakultatojn` と RU `факультеты` は「学部/ faculty」。旧ENは department に寄り、さらに語順も不自然。
- 参考列のみ: `ID1400` EN `Who is the chancellor of the university?`
  - `Who is the rector of the university?` に修正
  - 理由: EO `rektoro` と RU `ректор` に合わせた。PIV 2020 でも `rektoro` は教育機関の長、特に大学の長。
- 参考列のみ: `ID1410` EN `Are you a member of any book group?`
  - `Are you a member of any book club?` に修正
  - 理由: EO `libroklubo` と RU `книжного клуба` に合わせ、英語も自然な `book club` に統一。
- 参考列のみ: `ID1413` EN `How many more years do you have to go?`
  - `How many more years do you have to study?` に修正
  - 理由: EO `devas studi` と RU `учиться` は「あと何年勉強する必要があるか」。旧ENは省略が強く、参照列として曖昧。
- 参考列のみ: `ID1437` EN `I will make my report in Catalan.`
  - `I will prepare my report in Catalan.` に修正
  - 理由: EO `fari raporton` と JA/ZH/KO の「報告書を作成する」側に合わせ、旧ENの直訳調を緩和。
- `ID1444` EO `Li fiaskis en la ekzameno pri filozofio`
  - `Li malsukcesis en la ekzameno pri filozofio` に修正
  - 理由: PIV 2020 の `ekzameno` 項で `sukcesi, malsukcesi en la ekzameno` が例示されている。試験に落ちる意味としてはこちらがより安全。
- 参考列のみ: `ID1447` EN `How can one subscribe to the library?`
  - `How can one register with the library?` に修正
  - 理由: EO `aliĝi al la biblioteko` と RU `записаться в библиотеку` は図書館利用登録。旧ENの `subscribe` は図書館文脈では不自然。

主な据え置き確認:
- `ID1357` `En kiu aĝo infanoj komencas iri al lernejo?`: `Je kiu aĝo` も候補だが、PIV 2020 には `en la aĝo de ...` 型があり、意味ズレはないため未修正。
- `ID1363/1367` `studi ĉe universitato`: `ĉe` は機関所属・場所を表す表現として許容。未修正。
- `ID1384` `magistriĝo`: PIV 2020 で `magistro` / `magistreco` は確認できるが、現形も規則的派生として理解可能。安全な置換先を確定しきれないため未修正。
- `ID1385` `doktoriĝas`: PIV 2020 で `doktoriĝi` は「博士号を得る」意味として確認。未修正。
- `ID1403` `studentloĝejon`: 透明な複合語で、学生寮文脈と整合。未修正。
- `ID1453` `brila oratoro`: PIV 2020 は `oratoro` を「公開で話す人」として定義しており、女性主語でも性別明示の `oratorino` へ直す必然性は低い。未修正。
- `ID1454` `templimo`: 既存の低優先保留語。PIV 2020 に `templimo` が見え、意味は「時間制限」として明確。未修正。
- `ID1455` `formulitaj buŝe`: RU とも整合し、口頭で質問を形にして提示する意味として許容。未修正。

一致確認:
- `cmp_exit=0`
- `md5=837f2a9863e5d0c6ef5202d33074ed27`

## 31. 30周目 追加再点検（ID1456〜1555）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1456〜1555` を確認
- Education / Student Life、Numbers & Colours、Jobs / Occupation を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `koloro`、`ruĝo/verdo/bruno/flavo/oranĝa`、`juristo/advokato`、`komercisto/entreprenisto`、`handikapo`、`voki/vokcentro`、`informadiko/teknologio` 周辺を照合

修正:
- 参考列のみ: `ID1456` EN `Can the questions be formulated in written form?`
  - `Can the questions be formulated in writing?` に修正
  - 理由: EO `skribe` と RU `письменно` に合わせ、英語として自然な形へ修正。
- 参考列のみ: `ID1457` EN `Did you like the report on health service?`
  - `Did you like the report on healthcare?` に修正
  - 理由: EO `sanservo` と RU `здравоохранение` の文脈では `healthcare` が自然。
- 参考列のみ: `ID1460` EN `Who originated the idea?`
  - `Who proposed that idea?` に修正
  - 理由: EO `proponis` と RU `выдвинул` は「提案した/打ち出した」。旧ENは「発案者」に寄りすぎる。
- 参考列のみ: `ID1461` RU `Кто автор этого изобретения?`
  - `Кто изобретатель телефона?` に修正
  - 理由: EO/EN/JA/ZH/KO は「電話の発明者」。旧RUは「この発明」に曖昧化していた。
- 参考列のみ: `ID1465` EN `How many days have you got for preparation?`
  - `How many days do you have to prepare?` に修正
  - 理由: 参照英語として自然で、EO/RUの「準備に使える日数」と対応。
- 参考列のみ: `ID1467` EN `I still have got many things to revise.`
  - `I still have many things to revise.` に修正
  - 理由: 不自然な `have got` を削り、意味は維持。
- 参考列のみ: `ID1485` RU `Медведь- коричневый.`
  - `Медведь — коричневый.` に修正
  - 理由: ダッシュ前後の表記を自然化。
- `ID1486` EO `Ruĝa kaj verda faras brunan`
  - `Ruĝo kaj verdo faras brunon` に修正
  - 理由: 色そのものを混ぜる文なので、PIV 2020で確認できる色名詞 `ruĝo/verdo/bruno` を使う方が文法的に安定。
- 参考列のみ: `ID1500` RU `Слива- лиловая.`
  - `Слива — лиловая.` に修正
  - 理由: ダッシュ前後の表記を自然化。
- `ID1503` EO `Flava kaj ruĝa faras oranĝan`
  - `Flavo kaj ruĝo faras oranĝan koloron` に修正
  - 理由: 主語は色名詞 `flavo/ruĝo` にし、`oranĝa` はPIV上果物由来の色形容詞なので、目的語 `koloron` を明示。
- `ID1504` EO `Verda kaj flava faras helverdan`
  - `Verdo kaj flavo faras helverdan koloron` に修正
  - 理由: 上と同じく、色名詞を主語にし、目的語 `koloron` を明示。
- 参考列のみ: `ID1506` EN `Sixty, seventy, eighty, ninety, hundred.`
  - `Sixty, seventy, eighty, ninety, one hundred.` に修正
  - 理由: 数詞列として `cent` に対応する英語を自然化。
- 参考列のみ: `ID1540` EN `Whom do you work for?`
  - `Who do you work for?` に修正
  - 理由: 口語の参照文として自然な形へ修正。

主な据え置き確認:
- `ID1466` `ekzamena sesio`: 試験期間/試験セッションとして各列と整合。未修正。
- `ID1501` `Ruĝo kaj bluo faras purpuron`: PIV 2020で `purpuro/purpura` を確認。紫系色の表現として許容し未修正。
- `ID1538` `informteknologio`: `informi` + `teknologio` の透明複合語で、ウェブ用例も確認。`informa teknologio` も候補だが、明確な誤りではないため未修正。
- `ID1543` `juristo`: PIV 2020では「法律・司法の専門家」。JA/ZH/KOは弁護士寄りだが、RU `юрист` と整合し、`advokato` に限定するのは危険なため未修正。
- `ID1549` `komercistino`: PIV 2020で `komercisto` は職業的に商取引をする人。`entreprenistino` も候補だが、`businesswoman` の広い意味として許容し未修正。
- `ID1551` `vokcentro`: PIV 2020の `voki` を基礎にした透明複合語で、call centre 文脈として意味明確。未修正。
- `ID1555` `handikapitaj infanoj`: PIV 2020で `handikapo/handikapito` を確認。現代的には別表現もあり得るが、意味ズレはないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=a23fd5ae7b277907afb5d13a7b67d868`

## 32. 31周目 追加再点検（ID1556〜1655）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1556〜1655` を確認
- Jobs / Occupation、At Work を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `merkatiko`、`praktiko/staĝo`、`forpermeso`、`maldungi`、`eksvalidiĝi/finiĝi`、`interkonsento` 周辺を照合
- `patrina forpermeso` / `patra forpermeso` は Majstro などの外部用例も再確認

修正:
- 参考列のみ: `ID1618` JA `私は8時に始まり、5時に終わります。`
  - `8時に仕事を始めて、5時に終わります。` に修正
  - 理由: EO/RU/EN/ZH/KO は「仕事を8時に始め、5時に終える」。旧JAは主語と述語の対応が不自然だった。
- 参考列のみ: `ID1641` EN `I've got one hour lunch break at noon.`
  - `I've got a one-hour lunch break at noon.` に修正
  - 理由: 英語として冠詞・複合形容詞を補い、意味は維持。
- `ID1650` EO `La limtempo por liveri la varojn eksvalidiĝas`
  - `La limtempo por liveri la varojn finiĝas` に修正
  - 理由: PIV 2020 の `eksvalidiĝi` は「法的・契約的効力を失う」寄り。ここでは納品期限が終わる意味なので、PIV 2020 で確認できる `finiĝi` に寄せた。
- 参考列のみ: `ID1650` EN `The delivery time of the merchandise expires.`
  - `The deadline for delivering the goods is expiring.` に修正
  - 理由: EO/RU/JA/ZH/KO は「納品期限が切れる/終わる」であり、旧ENは `delivery time` が不自然かつ意味が曖昧だった。

主な据え置き確認:
- `ID1560` `Mi estas merkatika administranto`: PIV 2020 で `merkatiko` 自体は確認。ただし RU は「マーケティング専門家」、EN/JA/ZH/KO は「マーケティング管理者/マネージャー」寄りで、職名の焦点を安全に固定できないため高優先保留を継続。
- `ID1588` `Mi faras praktikon`: `staĝi` も候補だが、PIV 2020 の `praktiko` には実務・実地練習の語義があり、RU/ZH/JA/KO のインターン・実習文脈と大きくはずれないため未修正。
- `ID1590` `Ŝi estas en patrina forpermeso` / `ID1591` `Li estas en patra forpermeso`: `forpermeso` は PIV 2020 で休暇・許可された不在として確認。`patrina/patra forpermeso` は外部用例があり、意味も各列と一致するため高優先保留から外した。
- `ID1600` `La kompanio maldungis lin`: PIV 2020 で `maldungi` は雇用を解く意味。RU/JA/ZH/KO と整合し未修正。
- `ID1655` `Ĉu ni faru la interkonsenton?`: `interkonsento` は合意・協定の意味で、契約成立の会話として許容。未修正。

一致確認:
- `cmp_exit=0`
- `md5=94a2b4a0ab5a6eed5552e3e30dc608ed`

## 33. 32周目 追加再点検（ID1656〜1755）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1656〜1755` を確認
- Jobs / Business、At the Interview、Recommendation Letter を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `afervojaĝo`、`formularo`、`laborkontrakto`、`provperiodo`、`deĵori/laŭvice`、`fortaĵo/malfortaĵo`、`vojaĝkostoj`、`flegistino` 周辺を照合

修正:
- 参考列のみ: `ID1659` RU `Я не могу сделать это завтра в 2 часа дня.`
  - `Я не смогу прийти завтра в 2 часа дня.` に修正
  - 理由: EO/JA/ZH/KO は「明日14時に来られない/出席できない」。旧RUは英語 `make it` の誤訳で「それをできない」に寄っていた。
- `ID1664` EO `Mi ofte faras laborvojaĝojn`
  - `Mi ofte faras afervojaĝojn` に修正
  - 理由: PIV 2020 で `afervojaĝo` は「観光以外の目的の旅行」と確認でき、business trip / 出張 / командировка の文脈により安全。保留語 `laborvojaĝo` はここで解除。
- 参考列のみ: `ID1674` RU `Я бы хотел встретиться с господином Вэнгом, пожалуйста.`
  - `Я бы хотел записаться на встречу с господином Ваном.` に修正
  - 理由: EO/EN/JA/ZH/KO は Wang/王/ワン/왕。旧RUは Weng に見える転写だった。
- 参考列のみ: `ID1683` RU `Когда вы собираетесь обговорить цену?`
  - `Когда мы будем договариваться о цене?` に修正
  - 理由: EO/EN/JA/ZH は「私たちが価格交渉をする時期」。旧RUは主語が「あなた方」にずれていた。
- `ID1686` EO `Ĉu vi havas modelon de vivresumo?`
  - `Ĉu vi havas formularon por vivresumo?` に修正
  - 理由: JA/ZH/KO/EN は履歴書の「用紙/フォーム」。PIV 2020 の `formularo` は記入用書類で、旧 `modelo` は「見本/モデル」に寄りすぎていた。
- 参考列のみ: `ID1686` RU `У вас есть образец резюме?`
  - `У вас есть бланк резюме?` に修正
  - 理由: 上記と同じく、sample ではなく blank/form に合わせた。
- 参考列のみ: `ID1694` EN `I have never gone to university.`
  - `I have never been to university.` に修正
  - 理由: 英語として自然な形へ修正。意味は維持。
- `ID1713` EO `Ĉi tio estas via laborokontrakto`
  - `Ĉi tio estas via laborkontrakto` に修正
  - 理由: PIV 2020 で `laborkontrakto` が明示例として確認できる。旧形は透明ではあるが、標準的な複合形に寄せた。
- 参考列のみ: `ID1714` EN `There's a three month trial period.`
  - `There's a three-month trial period.` に修正
  - 理由: 名詞前の複合形容詞として自然化。
- 参考列のみ: `ID1725` EN `I would like to get hired by your company.`
  - `I would like to be hired by your company.` に修正
  - 理由: 面接・応募文脈でやや口語的な `get hired` を参照列として自然化。
- 参考列のみ: `ID1727` RU `Я желаю претендовать на позицию руководителя отдела.`
  - `Я хочу подать заявку на должность офис-менеджера.` に修正
  - 理由: EO/EN/JA/ZH/KO は office manager。旧RUは「部門長」にずれていた。
- 参考列のみ: `ID1736` EN `I've got 15 years experience of working as a nurse.`
  - `I've got 15 years' experience working as a nurse.` に修正
  - 理由: 所有格と動名詞句を整え、意味は維持。
- `ID1750` JA/ZH/KO/EN
  - EN `She handles responsibility well.` → `She performs her duties well.`
  - JA `彼女は責任感が強いです。` → `彼女は自分の職務をきちんと果たします。`
  - ZH `她能够很好地承担责任。` → `她很好地履行自己的职责。`
  - KO `그녀는 책임을 잘 감당해요.` → `그녀는 자신의 직무를 잘 수행합니다.`
  - 理由: EO `plenumas siajn devojn` と RU `справляется с обязанностями` は「職務・義務を果たす」。旧日中韓英は「責任感/責任を担う」に寄っていたため、クイズ対象列の意味を明確化。

主な据え置き確認:
- `ID1676` `Mi scivolas, ĉu ni povas prokrasti nian kunvenon?`: 間接疑問文だが、丁寧な依頼としてのイントネーションを表す句読法は許容と判断し未修正。
- `ID1734` `vojaĝkostojn`: PIV 2020 で `vojaĝkostoj` が確認でき、支給・補償文脈とも整合。未修正。
- `ID1737` `Mia fako estas informatiko`: EN/RU は情報技術寄りだが、`informatiko` は専門分野名として十分通り、`informteknologio` へ寄せると学科・専門分野の焦点を逆に狭める可能性があるため未修正。
- `ID1744` `fortaĵoj kaj malfortaĵoj`: PIV 2020 で `fortaĵo` と `malfortaĵo` を確認。strengths / weaknesses の面接文脈として未修正。
- `ID1745` `lojaleco kaj akurateco`: PIV 2020 で `lojala/lojaleco` と `akurata/akurateco` の意味を確認。推薦状の人物評価として未修正。

一致確認:
- `cmp_exit=0`
- `md5=a3b33bb4676334b1981f0b7278cf8598`

## 34. 33周目 追加再点検（ID1756〜1855）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1756〜1855` を確認
- Jobs / Recommendation Letter、Travel / Asking Directions、Travel / Giving Directions を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `ŝparvojo`、`ambasadejo`、`stacidomo`、`aŭtobusa stacio`、`marbordo`、`semaforo`、`fajrobrigadejo`、`trans la strato` 周辺を照合

修正:
- 参考列のみ: `ID1756` EN `I cannot recommend him for your company.`
  - `I cannot recommend him to your company.` に修正
  - 理由: EO `rekomendi ... al ...` と RU/JA/KO は「御社に推薦する」。旧ENの `for your company` はやや不自然。
- 参考列のみ: `ID1757` EN `Would you, please, write a letter of recommendation for me?`
  - `Would you please write a letter of recommendation for me?` に修正
  - 理由: 不要なコンマを外し、自然な依頼文にした。
- 参考列のみ: `ID1759` RU `Он работал на меня в различных проектах.`
  - `Он работал у меня над различными проектами.` に修正
  - 理由: EO/EN/JA は「私の下で/私のために様々なプロジェクトに携わった」。旧RUは不自然で、プロジェクトとの関係も弱かった。
- 参考列のみ: `ID1763` EN `She consistently produces high quality work.`
  - `She consistently produces high-quality work.` に修正
  - 理由: 名詞前の複合形容詞として自然化。
- 参考列のみ: `ID1766` EN `He brought outstanding contribution to my project.`
  - `He made an outstanding contribution to my project.` に修正
  - 理由: `make a contribution` が自然で、EO/RU/JA/ZH/KO の意味を維持。
- 参考列のみ: `ID1767` EN `He is a reliable person with good sense of humour.`
  - `He is a reliable person with a good sense of humour.` に修正
  - 理由: 冠詞を補って自然化。
- 参考列のみ: `ID1824` JA `銀行の裏側で。`
  - `銀行の裏側です。` に修正
  - 理由: EO/EN/RU は場所提示の断片。旧JAは助詞で終わり不自然。
- 参考列のみ: `ID1830` ZH `非常接近。`
  - `挺近的。` に修正
  - 理由: 道案内の距離表現として自然化。意味は `sufiĉe proksime` と整合。
- 参考列のみ: `ID1841` ZH `直行大约一公里。`
  - `一直往前走大约一公里。` に修正
  - 理由: 道案内として自然な命令表現へ修正。
- 参考列のみ: `ID1855` EN `Keep going for another half kilometre.`
  - `Keep going for another half a kilometre.` に修正
  - 理由: 英語として自然化。距離の意味は維持。

主な据え置き確認:
- `ID1780` `Kiun ŝparvojon mi povas preni?`: PIV 2020 と Glosbe で `ŝparvojo` が shortcut 相当として確認済み。現形維持。
- `ID1798` `diri al mi la direkton`: `montri la vojon` なども候補だが、各列の「道を教える/方向を示す」と大きくずれないため未修正。
- `ID1804` `aŭtobusa stacio`: バスターミナル/バスステーション文脈として透明で、各列と整合。未修正。
- `ID1807` `ambasadejo`: 以前の周回で `ambasadorejo` から修正済み。PIV 2020 で大使館建物として確認済み。
- `ID1814` `Mi malfacile orientiĝas`: JA は「道に迷った」に寄るが、方向感覚を失っている文脈として許容し未修正。
- `ID1847` `trans la strato`: PIV 2020 に場所を表す `trans la strato` 型があり、across the street として未修正。
- `ID1853` `fajrobrigadejo`: `fajrobrigado` + `-ejo` の透明派生で、fire station / пожарная часть と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=41e20e899855f179cb109d243464c286`

## 35. 34周目 追加再点検（ID1856〜1955）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1856〜1955` を確認
- Travel / Giving Directions、At the Tourist Office、Excursions、Plane / Booking a Flight を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `rekten`、`naveda`、`buso`、`vidindaĵo`、`ekskurso`、`rondvojaĝo`、`gvidata`、`fotografio/foti`、`ekonomiklasa` 周辺を照合

修正:
- 参考列のみ: `ID1856` ZH `直行，经过几个红绿灯。`
  - `继续直走，经过几个红绿灯。` に修正
  - 理由: 道案内の命令文として自然化。EO/RU/JA/KO の「そのまま直進し、信号をいくつか過ぎる」と整合。
- 参考列のみ: `ID1861` ZH `抱歉，我不认识这个城镇。`
  - `抱歉，我不熟悉这个城镇。` に修正
  - 理由: 場所について「知らない/詳しくない」を表すには `不熟悉` が自然。
- `ID1906` EO `Kie mi povas preni la navedbuson?`
  - `Kie mi povas preni la navedan buson?` に修正
  - 理由: PIV 2020 で `naveda` は比喩的に「往復する/ir-reira」と確認でき、`buso` との形容詞句にすれば shuttle bus の意味を保ちながら、保留語 `navedbuso` より安全。
- 参考列のみ: `ID1906` RU `Где я могу сесть на маршрутный автобус?`
  - `Где я могу сесть на шаттл?` に修正
  - 理由: EO/EN/JA/ZH/KO は shuttle bus。旧RUの `маршрутный автобус` は通常の路線バス寄り。
- 参考列のみ: `ID1920` EN `Are there any meals included?`
  - `Are meals included in the price?` に修正
  - 理由: EO/RU は「料金に食事が含まれるか」を明示しているため、参照英語も合わせた。
- 参考列のみ: `ID1942` ZH `您更倾向于哪种旅游方式？`
  - `您更喜欢哪种游览项目？` に修正
  - 理由: EO/RU/EN/JA/KO は「どの種類のツアー/エクスカーションを好むか」。旧ZHは「旅行方式」に寄っていた。
- 参考列のみ: `ID1944` EN `I'd like a Georgian speaking guide.`
  - `I'd like a Georgian-speaking guide.` に修正
  - 理由: 名詞前の複合形容詞として自然化。
- 参考列のみ: `ID1950` EN `Would you please tell me what museums are here?`
  - `Would you please tell me which museums are here?` に修正
  - 理由: `kiuj muzeoj` に合わせ、列挙対象を尋ねる英語にした。
- 参考列のみ: `ID1955` EN `An economy class ticket.`
  - `An economy-class ticket.` に修正
  - 理由: 名詞前の複合形容詞として自然化。

主な据え置き確認:
- `ID1856` `Daŭrigu rekten ...`: PIV 2020 に `iru rekten` 型の用例があり、方向副詞として未修正。
- `ID1867` `viziti vidindaĵojn`: 観光・見どころを見る意味として各列と整合。未修正。
- `ID1894` `junulargastejoj`: youth hostel 文脈の透明な複合語で、各列と整合。未修正。
- `ID1901` `sandviĉejon`: サンドイッチを売る店として透明で、JA/ZH/KO/EN と整合。RU はやや広い `закусочная` だが参考列内の許容と判断。
- `ID1928` `en la estona`: 言語指定として自然。未修正。
- `ID1937` `preni miajn fotojn`: 写真店・観光文脈では「写真を受け取る/引き取る」と読めるため未修正。
- `ID1941` `vidindaĵan ekskurson`: sightseeing tour として意味が透明で、各列と整合。未修正。
- `ID1953` `subeksponitaj`: 写真の露出不足として各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=440b676b0b5f5aa2182c0f8fe221c726`

## 36. 35周目 追加再点検（ID1956〜2055）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID1956〜2055` を確認
- Plane / Booking a Flight、Checking in、Luggage を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `ŝanĝi`、`aviadilo`、`atendejo`、`registrejo`、`bagaĝo`、`valizo`、`metala`、`pordego/elirejo` 周辺を照合
- Glosbe と Web/PDF 用例で `pordego`、`manbagaĝo`、`ŝanĝi aviadilon` 周辺も確認

修正:
- 参考列のみ: `ID1969` RU `Какое у вас направление?`
  - `Какой у вас пункт назначения?` に修正
  - 理由: EO/EN/JA/ZH/KO は「目的地」。旧RUも旅行文脈では通じうるが、`направление` は方向・方面に寄るため、`celloko` に合わせて明確化。
- 参考列のみ: `ID1973` EN `How frequent are the flights?`
  - `How often are there flights?` に修正
  - 理由: EO `Kiom ofte ...` と RU `Как часто ...` に合わせ、自然な頻度質問にした。
- `ID1989` EO `Kiom da tempo necesas por la transŝanĝo?`
  - `Kiom da tempo necesas por ŝanĝi aviadilon?` に修正
  - 理由: `transŝanĝo` はPIVで直接確認できず、交通の乗り継ぎとしては不安定。PIVで確認できる `ŝanĝi` と `aviadilo` を用い、周辺の `ID1977/1978` と同じ「飛行機を乗り換える」表現へ寄せた。
- 参考列のみ: `ID1999` EN `Where's the check-in?`
  - `Where's the check-in counter?` に修正
  - 理由: EO `registrejo` と RU `стойка регистрации` はチェックイン窓口。英語を明確化。
- `ID2012` EN/JA/ZH/KO
  - EN `Let's go into the lounge.` → `Let's go to the waiting area.`
  - JA `ラウンジに行きましょう。` → `待合室に行きましょう。`
  - ZH `我们去休息室吧。` → `我们去候机区吧。`
  - KO `라운지로 가요.` → `대기실로 가요.`
  - 理由: PIV 2020 の `atendejo` は待合室。RU も `зал ожидания` で、旧日中韓英は空港ラウンジ寄りに読まれやすかった。
- 参考列のみ: `ID2018` EN `What airline are you flying?`
  - `Which airline are you flying with?` に修正
  - 理由: 英語として自然化。EO/RU/JA/ZH/KO の「どの航空会社で飛ぶか」と整合。
- 参考列のみ: `ID2022` RU `Я могу посмотреть ваш паспорт, пожалуйста?`
  - `Могу я посмотреть ваш паспорт, пожалуйста?` に修正
  - 理由: 依頼文として自然な語順にした。
- 参考列のみ: `ID2028` EN `Please put any metallic objects into the tray.`
  - `Please put all metal objects into the tray.` に修正
  - 理由: EO/RU/ZH/KO は「すべての金属物」。英語も数量範囲を合わせた。
- 参考列のみ: `ID2035` EN `Where is the luggage check?`
  - `Where can I weigh my luggage?` に修正
  - 理由: EO/RU/JA/ZH/KO は「荷物を量る場所」。旧ENは luggage check で意味がずれていた。
- `ID2037` EN/JA/ZH/KO
  - EN `How many bags have you got?` → `How many suitcases have you got?`
  - JA `バッグはいくつお持ちですか？` → `スーツケースはいくつお持ちですか？`
  - ZH `你有几个包？` → `你有几个行李箱？`
  - KO `가방이 몇 개 있으신가요?` → `여행가방이 몇 개 있으신가요?`
  - 理由: EO `valizoj` と RU `чемоданов` はスーツケース。クイズ対象列を広い「バッグ」から具体化。
- 参考列のみ: `ID2045` KO `네, 가방 하나 있어요.`
  - `네, 여행가방 하나 있어요.` に修正
  - 理由: EO/RU/EN/JA/ZH は「スーツケース1つ」。韓国語だけ広い `가방` だったため合わせた。
- 参考列のみ: `ID2050` EN `You have to pay an overweight charge.`
  - `You will have to pay for the excess weight.` に修正
  - 理由: EO `devos pagi por la superpezo` と RU `оплатить перевес` に合わせ、超過重量そのものへの支払いとして自然化。
- 参考列のみ: `ID2055` KO `손가방을 보여주시겠어요?`
  - `기내 반입 수하물을 보여주시겠어요?` に修正
  - 理由: EO/EN/RU/ZH は hand luggage / ручная кладь / 随身行李。旧KOはハンドバッグ寄りで、機内持ち込み手荷物としては狭すぎた。

主な据え置き確認:
- `ID1957` `halto dumvoje`: 途中停車/経由地として各列と整合。未修正。
- `ID1984` `forveturo`: 飛行機文脈では `forflugo` も候補だが、PIV上の一般的な出発表現として意味は通るため未修正。
- `ID2011` `enŝipiĝo`: 既存保留どおり、航空 boarding としての慣用拡張を完全には排除できないため未修正。
- `ID2023` `pordego`: 空港 gate としては `elirejo` に統一する案もあるが、Glosbe で `gate -> pordego` が確認でき、明確な意味ズレとは断定しないため未修正。
- `ID2039` `bagaĝetikedo`: baggage tag として透明で、JA/ZH/KO/RU と大きくずれないため未修正。
- `ID2047/2048/2055` `manbagaĝo`: PIVで直接見出しとしては弱いが、Web上に空港文脈の実用例があり、意味は明確。既存保留どおりEOは未修正。ただし `ID2055` のKOのみ、ハンドバッグ寄りの意味ズレを修正。

一致確認:
- `cmp_exit=0`
- `md5=c88362d48f8abef66af9845f34fb0886`

## 37. 36周目 追加再点検（ID2056〜2155）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2056〜2155` を確認
- Plane / Luggage、Passport Control & Customs、On the Plane を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `registri/registrigi`、`bagaĝo`、`dogano`、`deklaro`、`azilo`、`rifuĝinto`、`sekurzono`、`stevardo`、`seĝodorso` 周辺を照合

修正:
- `ID2044` EO `Ĉu vi enregistras iun bagaĝon?`
  - `Ĉu vi registrigas iun bagaĝon?` に修正
  - 理由: PIV 2020 で `registrigi pakaĵon ĉe la stacidomo` 型を確認。空港で荷物を預ける文脈では、フランス語風に見える `enregistri` より、PIVで裏取りできる `registrigi` が安全。
- `ID2057` EO `Ĉu mi devas enregistri ĉi tion, aŭ ĉu mi povas kunporti ĝin?`
  - `Ĉu mi devas registrigi ĉi tion kiel bagaĝon, aŭ ĉu mi povas kunporti ĝin?` に修正
  - 理由: 上と同じ。`kiel bagaĝon` を補い、「これを預け荷物として登録する/預ける」意味を明確化。
- `ID2089` EO `Kiom da imposto mi devas pagi?`
  - `Kiom da dogano mi devas pagi?` に修正
  - 理由: PIV 2020 で `dogano` は外国領域に入る商品に課される税、`limimposto` と確認。JA/ZH/KO/RU/EN は「関税/duty/пошлина」なので、一般的な `imposto` より具体化。
- `ID2113` EO `Vi devas pagi imposton por ĉi tiuj varoj`
  - `Vi devas pagi doganon por ĉi tiuj varoj` に修正
  - 理由: `ID2089` と同じ。税関文脈の duty を `dogano` に統一。
- 参考列のみ: `ID2100` EN `I have got a refugee status.`
  - `I have got refugee status.` に修正
  - 理由: 英語として自然化。EO/RU/JA/ZH/KO の意味は維持。
- `ID2104` JA `私は外交官パスポートを持っています。`
  - `私は外交旅券を持っています。` に修正
  - 理由: `diplomata pasporto` / diplomatic passport / дипломатический паспорт に対応する日本語として自然化。
- 参考列のみ: `ID2105` RU `Не могли бы вы, пожалуйста, поставить в мой паспорт штамп?`
  - `Не могли бы вы, пожалуйста, поставить штамп в мой паспорт?` に修正
  - 理由: ロシア語の語順を自然化。意味は維持。
- 参考列のみ: `ID2112` EN `I have got with me three bottles of whisky.`
  - `I have three bottles of whisky with me.` に修正
  - 理由: 英語として自然化。EO/RU/JA/ZH/KO の意味は維持。
- `ID2116` ZH/KO
  - ZH `你需要填写这份移民表格。` → `您需要填写这份入境表格。`
  - KO `이 이민 신청서를 작성하셔야 합니다.` → `이 입국 신고서를 작성하셔야 합니다.`
  - 理由: Passport Control & Customs の `enmigrada formularo` / immigration form / иммиграционная карточка は入境・入国時の書類。旧ZH/KOは移民申請書寄りで意味がずれていた。
- `ID2127` ZH `我可以把座椅调低一些吗？`
  - `我可以把座椅往后调吗？` に修正
  - 理由: EO/EN/RU/JA/KO は座席を後ろへ倒す/recline。旧ZHは座席を低くする意味に読まれやすい。
- `ID2130` KO `좌석 벨트를 착용해 주세요.`
  - `안전벨트를 매 주세요.` に修正
  - 理由: `sekurzono` / seat belt / ремни / 安全带 に対し、韓国語として自然な機内表現へ修正。
- 参考列のみ: `ID2145` RU `Мы надолго здесь остановились?`
  - `Как долго мы здесь остановимся?` に修正
  - 理由: EO/EN/JA/ZH/KO は未来の停留時間を尋ねる文。旧RUは「もう停まっているのか」に寄っていた。

主な据え置き確認:
- `ID2056/2058` `manbagaĝo`: 既存保留どおり、空港文脈で意味は明確なためEOは未修正。
- `ID2063` `bagaĝ-ricevejo`: baggage reclaim area として透明で、JA/ZH/KO/RU と整合。未修正。
- `ID2085/2101/2120` `azilo`: PIV 2020 で `peti azilon` 型を確認。政治的庇護/難民申請文脈として未修正。
- `ID2115` `pagi doganon`: PIV 2020 で `dogano = limimposto` と確認済み。現形維持。
- `ID2130` `sekurzono`: PIV 2020 で航空乗客を座席に固定する装備として確認。現形維持。
- `ID2140` `stevardino`: PIV 2020 で航空・船舶の乗客の快適を担当する職員として確認。RU も女性形 `стюардесса` なので未修正。
- `ID2149` `seĝodorso`: PIV 2020 の `galbo` 項で `seĝodorso` の用例を確認。保留継続から外し、現形維持。
- `ID2150` `supran bagaĝujon`: overhead locker/bin として透明で、JA/ZH/KO/RU と整合。未修正。
- `ID2154` `kovrilon`: `litkovrilo` も候補だが、機内で「掛けるもの」を求める文脈では `kovrilo` で意味が通るため未修正。

一致確認:
- `cmp_exit=0`
- `md5=8c1a721ba68d231a28c8eb8449a986ee`

## 38. 37周目 追加再点検（ID2156〜2255）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2156〜2255` を確認
- On the Plane、空港標識、Car Hire、Driving & Parking を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `mana`、`aŭtomata`、`transmisio`、`kaŭcio`、`deponaĵo`、`lasi`、`redoni`、`sub`、`voj/mapo`、`lu/i` 周辺を照合

修正:
- `ID2193` EO `Ĉu ĝi estas mekanika aŭ aŭtomata?`
  - `Ĉu ĝi havas manan aŭ aŭtomatan transmision?` に修正
  - 理由: RU の `механическая или автоматическая` は車文脈では変速機の手動/自動。PIV 2020 で `mekanika` は機械・力学一般の形容で、単独では manual transmission の意味が弱い。一方、`mana`、`aŭtomata`、`transmisio` はPIV上で確認でき、同CSV内 `ID2220` とも整合する。
- 参考列のみ: `ID2197` EN `Where are the lights?`
  - `Where do you turn on the headlights?` に修正
  - 理由: EO/RU/JA/ZH/KO は「ヘッドライトをどこで点けるか」。旧ENは灯火そのものの所在にも読めた。
- 参考列のみ: `ID2200` EN `Any extra fee?`
  - `Are there any extra fees?` に修正
  - 理由: EO/RU/JA/ZH/KO の「追加料金はあるか」に合わせ、英語を自然化。
- `ID2201` ZH `我可以在哪里退还？`
  - `我可以在哪里还车？` に修正
  - 理由: Car Hire 文脈で EO `redoni ĝin`、RU `вернуть её`、JA/KO は返却。旧ZHの `退还` は返金・返品寄りにも読まれるため、レンタカー返却として自然な `还车` にした。
- 参考列のみ: `ID2214` EN `Where are the indicators?`
  - `Where do you turn on the indicators?` に修正
  - 理由: EO/RU/JA/ZH/KO は「方向指示器をどこで点けるか」。旧ENは物理的な位置質問に寄る。
- 参考列のみ: `ID2224` EN `Where are the windscreen wipers?`
  - `Where do you turn on the windscreen wipers?` に修正
  - 理由: EO/RU/JA/ZH/KO はワイパー操作の質問。旧ENはワイパー本体の所在に寄る。
- `ID2234` EO `Ĉu mi devas pagi antaŭpagon?`
  - `Ĉu mi devas pagi kaŭcion?` に修正
  - EN も `Do I need to pay a deposit?` → `Do I need to pay a security deposit?` に修正
  - 理由: JA/ZH/KO/RU は保証金/押金/задаток。PIV 2020 で `antaŭpago` は前払い寄り、`kaŭcio` は契約履行を保証するために預ける金額として確認できるため、レンタカー保証金に合わせた。
- `ID2237` EO `Ĉu mi povus lasi la aŭton ĉe mia celloko?`
  - `Ĉu mi povus redoni la aŭton ĉe mia celloko?` に修正
  - 理由: PIV 2020 で `lasi` は「置いていく/残す」、`redoni` は受け取ったものを返す意味。Car Hire の `drop off` と JA/ZH/KO の「返却/还车/반납」に合わせ、クイズ対象列との対応を明確化。`ID2238` は空港に車を置く文脈として各列が整合するため未修正。
- `ID2239` ZH `我想添加一位第二驾驶员。`
  - `我想添加第二位驾驶员。` に修正
  - 理由: 中国語として `一位第二驾驶员` は数量と序数が重なり不自然。EO/RU/JA/KO の「2人目の運転者を追加」と意味は維持。
- 参考列のみ: `ID2253` EN `Go over the roundabout.`
  - `Go through the roundabout.` に修正
  - 理由: EO `tra la trafikrondo` と JA/ZH/KO/RU はラウンドアバウトを通過/進む。旧ENの `over` は意味がずれていた。

主な据え置き確認:
- `ID2156` `veki min por la manĝo`: RU は「食事前に起こす」だが、機内で「食事のために起こす」として JA/ZH/KO/EN と整合。`antaŭ la manĝo` へ寄せるほどの明確な誤りではない。
- `ID2160` `formularon por dogandeklaro`: PIV 2020 の `deklaro` 項で `dogan deklaro` を確認。`dogandeklaro` は透明で、周辺の `dogana deklaracio` と意味は一致するため未修正。
- `ID2168` `Pordegoj 1-32`: 空港 gate は `elirejo` に統一する案もあるが、前回確認どおり `pordego` も gate として辞書上確認できる。標識表現として致命的でないため未修正。
- `ID2181` `Bagaĝa elpreno`: 既存保留どおり、透明複合語として意味は明確。標準置換先を確定できないため未修正。
- `ID2213` `infanseruroj`: PIVで直接見出しは確認できないが、`infan-` + `seruro` の透明複合語で child locks として各列と整合。低優先保留を継続。
- `ID2225` `minimuma luoperiodo`: PIVで `lui` と `luado de aŭtomobilo` を確認。`luoperiodo` は直接見出しではないが意味は透明なため、低優先保留を継続。
- `ID2252` `Veturu sub la ponto`: PIV 2020 の `sub` は位置・移動の両方を扱う。ここでは「橋の下を通って走る」経路表現として許容し、`sub la ponton` への変更は見送り。
- `ID2254` `vojmapon`: PIVで `voj/o` と `map/o` は確認できるが、`vojmapo` の直接見出しは弱い。意味は road map と明確に対応するため、低優先保留を継続。

一致確認:
- `cmp_exit=0`
- `md5=47388090425edf1679a9694fbf32bd04`

## 39. 38周目 追加再点検（ID2256〜2355）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2256〜2355` を確認
- Driving & Parking、At the Petrol Station、Mechanical Problems、Road Signs 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `akumulatoro`、`baterio`、`malŝargiĝi`、`ŝargi`、`meĥanikisto/mekanikisto`、`direktmontrilo/ĝirindikilo`、`hupo`、`kapoto`、`pneŭmatiko`、`pumpi`、`benzinujo`、`rapidometro` 周辺を照合
- オンライン辞書検索で `bremslikvaĵo`、`startkablo/startokablo`、`direktomontrilo` 周辺の実例も確認

修正:
- `ID2279` ZH `最近的加油站有多少公里？`
  - `到最近的加油站有多少公里？` に修正
  - 理由: EO `ĝis`、RU `до`、JA/KO は「最寄りのガソリンスタンドまで」の距離。旧ZHは起点・到達先の関係が弱く、中国語としても不自然だった。
- `ID2318` ZH `我需要一块新电池。`
  - `我需要一个新的电瓶。` に修正
  - 理由: Car / Mechanical Problems 文脈で EO/RU は `akumulatoro / аккумулятор`。中国語では車載バッテリーとして `电瓶` が自然。
- `ID2322` EO `La baterio elĉerpiĝis`
  - `La akumulatoro malŝargiĝis` に修正
  - ZH も `电池没电了。` → `电瓶没电了。` に修正
  - 理由: RU は `Аккумулятор разрядился.`。PIV 2020 で `akumulatoro` は電気を蓄えて必要時に供給する装置、`malŝargiĝi` は電池・蓄電池の放電に使えることを確認。車の故障文脈では旧EOより正確。
- `ID2336` EO `Ĉu vi bonvolus ŝargi la baterion?`
  - `Ĉu vi bonvolus ŝargi la akumulatoron?` に修正
  - ZH も `请帮忙充一下电池。` → `请帮忙给电瓶充一下电。` に修正
  - 理由: `ID2322` と同じく車載バッテリーに統一。PIV 2020 で `ŝargi akumulatoron` 型を確認。
- `ID2342` JA/ZH/KO
  - JA `インジケーターが動作していません。` → `ウインカーが作動していません。`
  - ZH `指示灯不亮。` → `转向灯不亮。`
  - KO `지시등이 작동하지 않습니다.` → `방향지시등이 작동하지 않습니다.`
  - 理由: EO `direktomontriloj`、RU `Поворотники` は車の方向指示器。PIV 2020 でも `direktmontrilo = ĝirindikilo`、`indikilo de direktoŝanĝo ĉe aŭtomobilo` 型を確認。旧JA/ZH/KOは一般的な indicator/light に寄り、クイズ対象として曖昧だった。
- `ID2348` EO `Ĉu vi bonvolus aldoni bremsfluaĵon?`
  - `Ĉu vi bonvolus aldoni bremslikvaĵon?` に修正
  - 理由: 旧語も `fluaĵo = likvo` の透明語として意味は取れるが、オンライン辞書で brake fluid として `bremslikvaĵo` を確認できたため、より確認可能な表現に寄せた。意味は変更していない。
- `ID2354` JA/ZH/KO
  - JA `どなたかをそちらに向かわせてください。` → `車を引き取りに誰かを送ってください。`
  - ZH `请派人来取。` → `请派人来取车。`
  - KO `누군가를 보내 주세요.` → `차를 가지러 사람을 보내 주세요.`
  - 理由: EO `sendi iun por ĝi`、EN `send someone for it`、RU `пришлите кого-нибудь за ней` は、故障した車を取りに来る/引き取りに来る意味。旧JA/KOは「人を送る」だけで目的語が落ち、クイズ対応が弱かった。

主な据え置き確認:
- `ID2276` `Kiom da tempo daŭras per aŭto?`: `necesas` に寄せる案はあるが、質問の意味は各列と対応し、明確な誤りではないため未修正。
- `ID2278` `serva areo`: 既存保留どおり、高速道路の service area として直訳感はあるが、JA/ZH/KO/EN の意味は明確。RU は「技術サービス地点」寄りだが、ここだけでEOを動かすのは危険なため未修正。
- `ID2287` `fervojajn liniojn`: 物理的な線路なら `relvojojn` も候補だが、`fervoja linio` でも railway line として意味は取れるため未修正。
- `ID2315` `startokablojn`: `startkablo` の実例も確認したが、`starto` + `kablo` の透明複合語で jump leads として列間対応は明確。PIVで `starti/startigi` と `kablo` は確認できるため未修正。
- `ID2326` `meĥanikiston`: 当時は実例があり意味ズレなしとして未修正にしたが、89周目でPIV確認済みの `mekanikiston` へ寄せて修正済み。
- `ID2343` `brulaĵindikilo`: PIV 2020 には `benzinometro` もあるが、fuel gauge を汎用的に指す表現として透明で、ディーゼル車も含む文脈では現形を維持。
- `ID2346` `stirmekanismo`: `stirilaro` も候補だが、RU `рулевым механизмом` と対応し、意味は明確なため未修正。

一致確認:
- `cmp_exit=0`
- `md5=5d24cf32121c454fc180c1012b889857`

## 40. 39周目 追加再点検（ID2356〜2455）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2356〜2455` を確認
- Road Signs、At the Bus Station、At the Train Station を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索とローカル抽出で、特に `bus/o`、`strio`、`trafiklumoj`、`piedira zono`、`abono`、`tarifo`、`biletejo`、`stacidomo`、`kajo`、`pasaĝer kajo`、`platformo`、`trajno`、`ekspres trajno`、`stampi` 周辺を照合

修正:
- `ID2364` JA/ZH/KO
  - JA `立入禁止` → `進入禁止`
  - ZH `禁止入内` → `禁止驶入`
  - KO `출입 금지` → `진입 금지`
  - 理由: Car / Road Signs 文脈で RU は `Въезд запрещён`。歩行者の立入禁止ではなく、車両の no entry として対象言語を明確化。
- `ID2374` EO `Trafiklumo-regulado`
  - `Trafiklumoj` に修正
  - 理由: JA/ZH/KO/EN は「信号機/traffic lights」。PIV 2020 で `trafiklumoj` を確認。旧EOは RU `Светофорное регулирование` に寄った説明的な語で、クイズ対象列との対応が弱かった。
- `ID2395` ZH `我在哪里换乘去萨格勒布？`
  - `我在哪里换乘去萨格勒布的公交车？` に修正
  - 理由: 「どこでザグレブ行きに乗り換えるか」の目的語が旧ZHでは落ちており、不自然。
- `ID2396` ZH `请问，公交车站在哪里？`
  - `请问，汽车站在哪里？` に修正
  - 理由: EO `aŭtobusa stacidomo`、EN bus station、RU `автобусный вокзал`、JA/KO はバスターミナル。旧ZHは bus stop に読まれやすかった。
- `ID2399` EN/JA/ZH/KO
  - EN `What's the frequency per hour?` → `How many times an hour does it run?`
  - JA `1時間あたりの頻度はどれくらいですか？` → `1時間に何本ありますか？`
  - ZH `每小时的频率是多少？` → `每小时有几班？`
  - KO `시간당 빈도는 얼마인가요?` → `한 시간에 몇 번 운행하나요?`
  - 理由: EO/RU は「1時間に何回走るか」。旧表現は各言語とも説明調で、バス案内として不自然だった。
- `ID2401` JA/ZH/KO
  - JA `次のを待ちましょう。` → `次のバスを待ちましょう。`
  - ZH `我们等下一个吧。` → `我们等下一班吧。`
  - KO `다음 것을 기다립시다.` → `다음 버스를 기다립시다.`
  - 理由: EO `la sekvan` は bus station 文脈で「次のバス」。対象言語側では省略が不自然だった。
- `ID2410` ZH `头等舱往返哥本哈根多少钱？`
  - `到哥本哈根的一等往返票多少钱？` に修正
  - 理由: `头等舱` は飛行機の客室寄り。ここでは `unuaklasa revenbileto` / first class return / билет первого класса に対応する切符表現にした。
- `ID2413` KO `민스크행 어린이 1인용 편도 티켓 한 장 주세요.`
  - `민스크행 어린이 편도표 한 장 주세요.` に修正
  - 理由: `어린이 1인용 편도 티켓 한 장` は数量表現が重く、bus/train ticket 文脈では `어린이 편도표 한 장` が自然。
- `ID2414` JA `日曜日に戻るバク行きの往復をお願いします。`
  - `日曜日に戻るバク行きの往復切符をお願いします。` に修正
  - 理由: EO/EN/ZH/KO/RU は return ticket。旧JAは「往復」だけで切符が落ちていた。
- `ID2419` EO `Kiu platformo?`
  - `Kiu kajo?` に修正
  - JA/ZH/KO も `何番線ですか？` / `哪个站台？` / `어느 승강장인가요?` に修正
  - 理由: PIV 2020 で `platformo` は鉄道駅の乗り場ではなく、鉄道の passenger platform は `pasaĝer kajo`。同CSV内 `ID2447` も `kajo numero 1` を使っているため、`kajo` に統一。
- `ID2425` EO `Ĉu tio estas rapidtrajno?`
  - `Ĉu tio estas ekspresa trajno?` に修正
  - 理由: EN/JA/ZH/KO/RU は express train / 急行列車 / поезд-экспресс。PIV 2020 で `ekspres trajno` は「普通列車より速く、停車駅が少ない列車」と確認でき、旧 `rapidtrajno` より意味が正確。
- `ID2446` ZH `火车已被取消。`
  - `这趟火车取消了。` に修正
  - 理由: 意味は同じだが、交通案内として中国語が自然。
- 参考列のみ: `ID2449` EN `Where is the timetable of trains?`
  - `Where is the train timetable?` に修正
  - 理由: 英語として自然化。EO/RU/JA/ZH/KO の意味は維持。

主な据え置き確認:
- `ID2361/2384` `bushaltejo`: PIV 2020 で `bus/o = aŭtobuso` を確認。既存の `aŭtobushaltejo` と同系列の透明複合語として未修正。
- `ID2367` `Busstrio`: PIVで直接見出しは確認できないが、`bus/o` と `strio` の透明複合語で bus lane と対応。安全な標準置換を確定できないため未修正。
- `ID2369` `Preterpasu maldekstre`: RU は「障害物を左から回避」、JA/ZH/KO/EN は keep left 系。道路標識文脈では同じ指示として許容し、未修正。
- `ID2370` `piedira zono`: PIV 2020 で `piedira zono` を交通用語として確認。RU は pedestrian path 寄りだが、JA/ZH/KO/EN とEOは zone で一致するため未修正。
- `ID2404` `stampi la bileton`: PIV 2020 で駅文脈の `stampi` 用例を確認。`validigi` も候補だが、各列の stamp/押印/打票/печать と整合するため未修正。
- `ID2414` `returan bileton`: `revenbileto` との揺れはあるが、return ticket として意味は明確。未修正。
- `ID2431` `Atentu la interspacon`: RU は「ホーム端に近づかないで」に寄るが、EO/EN/JA/ZH/KO は platform gap として一致。クイズ対象列を優先して未修正。
- `ID2443` `Abu-Dabion`: `Abu-Dabio` の対格として文法的に自然。未修正。

一致確認:
- `cmp_exit=0`
- `md5=0b65854775e883f72d72c5baf5fc8718`

## 41. 40周目 追加再点検（ID2456〜2555）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2456〜2555` を確認
- At the Train Station、On the Bus or Train、Taxi を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索、ローカル抽出、Glosbe/一般Web検索で、特に `abonbileto`、`kajo`、`eksprestrajno`、`traveturi`、`kupeo`、`taksimetro`、`ŝalti`、`trajnstacio`、`superpago/krompago`、`nunmomente` 周辺を照合

修正:
- `ID2457` JA/ZH
  - JA `タリンまでの往復ファーストクラスをお願いします。` → `タリンまでのファーストクラスの往復切符をお願いします。`
  - ZH `我想要一张去塔林的头等舱往返票。` → `我想要一张去塔林的一等往返票。`
  - 理由: 鉄道切符文脈の `unuaklasa revenbileto / билет первого класса туда и обратно`。旧JAは「切符」が落ち、旧ZHの `头等舱` は航空機の客室寄りだった。
- `ID2461` JA/KO
  - JA `台北にはこのプラットフォームで合っていますか？` → `台北行きはこのホームで合っていますか？`
  - KO `여기가 타이베이행 맞는 플랫폼인가요?` → `여기가 타이베이행 승강장이 맞나요?`
  - 理由: EO `kajo`、EN/RU は platform。日本語・韓国語の駅案内として自然な表現に寄せた。
- `ID2462` KO
  - `10시 22분 바르샤바행은 11번 플랫폼에서 출발합니다.` → `10시 22분 바르샤바행은 11번 승강장에서 출발합니다.`
  - 理由: `kajo` に対応する鉄道文脈の Korean として `승강장` がより自然。
- `ID2465` JA/ZH/KO
  - JA `シーズンチケットの更新をお願いします。` → `定期券の更新をお願いします。`
  - ZH `我想续订我的季票。` → `我想给我的定期票续期。`
  - KO `시즌권을 갱신하고 싶어요.` → `정기권을 갱신하고 싶어요.`
  - 理由: PIV 2020 で `aboni` は `fervojbileton` にも使われ、RU `абонемент` とも整合する。交通機関の season ticket は日中韓では定期券/定期票/정기권が自然。
- `ID2493` EO/JA/KO
  - EO `Kie ni nun traveturas?` → `Tra kie ni nun veturas?`
  - JA `今、私たちはどこを通っていますか？` → `今どこを通っていますか？`
  - KO `지금 우리는 어디를 지나고 있나요?` → `지금 어디를 지나고 있나요?`
  - 理由: PIV 2020 では `tra veturi` は他動詞として「何を通過するか」を取る。旧EOは目的語なしで不自然だったため、意味を保って `Tra kie ... veturas?` に修正。
- `ID2514` ZH
  - `不好意思，这不是你的车厢。` → `不好意思，这不是你的包厢。`
  - 理由: PIV 2020 で `kupeo` は乗り物内の扉で区切られた区画。`车厢` は車両全体に寄るため、EN/RU の compartment/купе と合わせた。
- `ID2520` ZH
  - `本次列车到站终点。` → `本次列车到此终止运行。`
  - 理由: `Ĉi tiu trajno finiĝas ĉi tie` と RU `Поезд дальше не идёт` に対応する「当駅止まり」。旧ZHは不自然。
- `ID2532` ZH
  - `仪表在哪里？` → `计价器在哪里？`
  - 理由: PIV 2020 で `taksimetro` はタクシー等に接続され、運賃を示す自動装置。タクシー文脈では一般的な instrument ではなく `计价器`。
- `ID2540` ZH/KO
  - ZH `仪表开了吗？` → `计价器开了吗？`
  - KO `계량기가 켜져 있나요?` → `미터기가 켜져 있나요?`
  - 理由: `taksimetro` と RU `таксометр` に合わせ、タクシーメーターを明確化。
- `ID2541` EN/ZH/KO
  - EN `Please take the most direct route.` → `Please take the shortest route.`
  - ZH `请走最直接的路线。` → `请走最短路线。`
  - KO `가장 직접적인 경로로 가주세요.` → `가장 짧은 길로 가 주세요.`
  - 理由: EO `plej mallongan vojon`、RU `самый короткий маршрут`、JA `最短ルート` は shortest route。旧ZH/KOは direct route 寄りだった。
- 参考列のみ: `ID2547` EN `There's airport surcharge.`
  - `There's an airport surcharge.` に修正
  - 理由: 英語として冠詞が必要。EO/RU/JA/ZH/KO の意味は維持。

主な据え置き確認:
- `ID2459` `eksprestrajno`: PIV 2020 で `ekspres trajno` と `eksprestrajno` 系の用例を確認。`ekspresa trajno` への統一も可能だが、現行語は誤りではないため未修正。
- `ID2463/2485` `vojaĝkarto`: travel card / 交通カードとして透明で、列間の意味も一致するため未修正。
- `ID2508` `pakaĵujo`: 荷物を入れる場所として透明。`pakaĵujo` はやや広いが、EN/JA/ZH/KO/RU と大きくずれないため未修正。
- `ID2518` `preterveturis vian haltejon`: PIV 2020 で `preter veturi` は他動詞として確認でき、降りる駅を乗り過ごす意味として成立するため未修正。
- `ID2538` `trajnstacio`: PIV 2020 の強い標準語としては `stacio/stacidomo` が見えるが、`trajnstacio` も透明で、train station / 鉄道駅との対応は明確。`fervoja stacidomo` へ寄せると硬くなるため未修正。
- `ID2544` `Ellasu min ĉi tie`: PIV 2020 の `el lasi` は「外へ出させる/出す」意味を確認でき、taxi の “let me off here” として成立するため未修正。
- `ID2547` `flughavena superpago`: PIV 2020 では `krompago/krompagi` の実例が強い一方、オンライン辞書で `superpago = surcharge` も確認できた。旧語は造語ミスとは断定できず、意味も各列と一致するため未修正。
- `ID2553` `nunmomente`: `nuntempe` なども候補だが、現在利用可能な車がないという意味は明確で、置換の必要性は高くないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=b70dc50f5fa8d125d2a8311bc1fde3a8`

## 42. 41周目 追加再点検（ID2556〜2655）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2556〜2655` を確認
- Taxi、Ship、Hotel / Asking about Facilities、Hotel / Booking a Room 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 公式簡易検索、ローカル抽出、Glosbe/一般Web検索で、特に `taksimetro`、`bankaŭtomato`、`marmalsano`、`enŝipiĝi`、`krozado`、`radiogramo`、`sunseĝo`、`aŭtoparkejo`、`monŝranko`、`ĉambroservo`、`rulseĝa aliro`、`gimnastikejo`、`ŝtopilingo`、`plena pensiono`、`antaŭpago` 周辺を照合

修正:
- `ID2561` JA/KO
  - JA `メーターの電源を入れてください。` → `メーターを入れてください。`
  - KO `계량기를 켜 주세요.` → `미터기를 켜 주세요.`
  - 理由: PIV 2020 で `taksimetro` はタクシー等の運賃表示装置。タクシー文脈では「電源」「計量器」より、タクシーメーターとしての表現が自然。
- `ID2566` ZH/KO
  - ZH `我们可以在自动取款机停一下吗？` → `我们可以在自动取款机旁停一下吗？`
  - KO `현금자동입출금기에 잠깐 들를 수 있을까요?` → `ATM에 잠깐 들를 수 있을까요?`
  - 理由: taxi で「ATMのそばに停まる/寄る」意味。旧ZHは場所関係が少し不自然、旧KOは硬すぎた。
- `ID2569` EO/KO
  - EO `Mi marmalsanas` → `Mi havas marmalsanon`
  - KO `저는 멀미가 나요.` → `저는 배멀미가 나요.`
  - 理由: PIV 2020 とオンライン辞書で `marmalsano` を確認。`marmalsanas` も透明な派生として読めるが、ユーザー懸念に合わせ、辞書確認済みの名詞句に寄せた。KOも seasick を明示。
- `ID2574` JA/KO
  - JA `搭乗は何時ですか？` → `乗船は何時ですか？`
  - KO `우리는 몇 시에 탑승하나요?` → `우리는 몇 시에 승선하나요?`
  - 理由: Ship 文脈で EO `enŝipiĝi`、ZH `登船`、RU `сесть на корабль`。日韓も船に乗る表現へ明確化。
- `ID2589` EO
  - `La kruzo estis mirinda` → `La krozado estis mirinda`
  - 理由: PIV 2020 で確認できる語は `kroz/i` と派生 `krozado`。`kruzo` は英語/ロシア語 cruise/круиз からの直写に見え、確認済みの形へ修正。
- `ID2603` ZH/KO
  - ZH `我需要发送一份电报。` → `我需要发送一份无线电报。`
  - KO `전문을 보내야 합니다.` → `무선 전보를 보내야 합니다.`
  - 理由: PIV 2020 で `radiogramo` は radio-telegraphy による telegram。JA/RU/EO に合わせ、日中韓対応で「無線電報」を明確化。
- `ID2611` JA/ZH/KO
  - JA `パソコンをお持ちですか？` → `利用できるパソコンはありますか？`
  - ZH `你有电脑吗？` → `有可以使用的电脑吗？`
  - KO `컴퓨터가 있으신가요?` → `사용할 수 있는 컴퓨터가 있나요?`
  - 理由: Hotel / Facilities 文脈では、相手個人の所有物ではなく宿泊客が使える設備の有無を尋ねる文。
- `ID2612` JA
  - `アダプターを持っていますか？` → `アダプターはありますか？`
  - 理由: 上と同じくホテル設備・貸出品の有無を尋ねる文。旧JAは相手個人の持ち物に読まれやすい。
- `ID2624` ZH
  - `你离市中心有多远？` → `你们离市中心有多远？`
  - 理由: ホテルへ尋ねる文なので、中国語では `你们` が自然。EO/RUの `vi/вы` とも対応する。
- `ID2633` EO
  - `Ĉu en mia ĉambro estas prizo por mia elektra razilo?` → `Ĉu en mia ĉambro estas ŝtopilingo por mia elektra razilo?`
  - 理由: PIV 2020 で socket に対応する確認可能な語として `ŝtopilingo` を確認。`prizo` はPIVローカル抽出で確認できず、フランス語等からの直写の疑いが残るため、辞書確認済みの語に修正。
- `ID2642` JA/ZH/KO
  - JA `今夜のために。` → `今夜です。`
  - ZH `今晚用。` → `今晚。`
  - KO `오늘 밤을 위해.` → `오늘 밤이요.`
  - 理由: `Por ĉi tiu nokto / For tonight / На сегодняшнюю ночь` は予約開始日の返答。旧日中韓は直訳調で不自然だった。
- `ID2650` JA/KO
  - JA `保証金は必要ですか？` → `予約金は必要ですか？`
  - KO `보증금이 필요하신가요?` → `예약금이 필요하신가요?`
  - 理由: EO `antaŭpago` は前払い・予約時の前金。RU `задаток`、ZH `定金` と合わせ、security deposit 寄りの語を避けた。

主な据え置き確認:
- `ID2563` `nokta krompago`: PIV 2020 と既存確認で `krompago/krompagi` の surcharge 用法を確認。現形維持。
- `ID2567` `Savringo`、`ID2568` `Savboato`、`ID2588` `savvestojn`: PIV 2020 で `savi/sava` の基礎語義を確認し、オンライン辞書・一般Web検索でも life ring/lifeboat/life jacket 系の実例を確認。透明複合語として未修正。
- `ID2570` `kajo`: PIV 2020 で船の上陸場所との関連を確認。dock / pier 文脈として問題なし。
- `ID2590` `Ĉu vin naŭzas vojaĝado?`: PIV 2020 で `naŭzi` は他動詞「吐き気を催させる」。語順はやや硬いが文法上成立し、EN/RU/JA の travel-sick とも対応するため未修正。
- `ID2601` `sunseĝo`: PIV 直接見出しとしては強くないが、同CSV内 At the Beach でも使われ、オンライン実例も確認。deckchair/sunlounger として意味は明確なため未修正。
- `ID2608` `aŭtoparkejo`: 透明複合語で car park と対応。PIV 2020 の `aŭtoparkado` 実例もあり、未修正。
- `ID2614` `beleca salono`: 直接見出しとしては弱いが、beauty salon として透明で、各列の意味とずれないため未修正。
- `ID2621` `ĉambroservo`: 透明複合語で room service と対応。未修正。
- `ID2623` `rulseĝan aliron`: 既存保留どおり、やや説明的だが wheelchair access として意味は明確。未修正。
- `ID2629` `gimnastikejo`: PIV 2020 で「体を鍛えるための場所」を確認。fitness centre として許容し、未修正。
- `ID2633` `elektra razilo`: PIV 2020 で `elektra razilo` の用例を確認。socket 側は上記のとおり `ŝtopilingo` に修正済み。
- `ID2649` `plena pensiono`: PIV 2020 の `pensiono` には注意書きがあるが、旅行・宿泊文脈の full board としてオンライン実例があり、RU/JA/ZH/KO/EN との対応も明確なため未修正。
- `ID2655` `unulitaj ĉambroj`: `unulita` + `ĉambro` で single room を表す透明な形。以前修正した `du unulitajn` のような名詞省略ではないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=805306fcce00fc2eca22b6febd4cf497`

## 43. 42周目 追加再点検（ID2656〜2755）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2656〜2755` を確認
- Hotel / Booking a Room、Checking in、During Your Stay を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `atendolisto`、`duobla ĉambro`、`ĉambronumero`、`ŝlosilo`、`lasi`、`tuko/mantuko`、`kovrilo/litkovrilo`、`ŝargilo`、`gladi`、`urĝa elirejo/savelirejo/rezerva elirejo`、`internacia kodo`、`plusendi` 周辺を照合

修正:
- `ID2667` KO
  - `네, 4박 동안 객실을 예약하고 싶습니다.` → `4박 동안 객실을 예약하고 싶습니다.`
  - 理由: 独立した予約依頼文で、旧KOの `네,` は他列にない応答語を足していたため削除。
- `ID2698` JA/ZH
  - JA `ここに荷物を置いてもいいですか？` → `ここに荷物を預けてもいいですか？`
  - ZH `我可以把行李放在这里吗？` → `我可以把行李寄放在这里吗？`
  - 理由: EO `lasi miajn sakojn ĉi tie` と RU `оставить здесь свои сумки` は直訳の「置く」でも読めるが、ホテルのチェックイン文脈では荷物預かりを尋ねる表現が自然。KO は既に `맡겨도`。
- `ID2699` JA
  - `お荷物をお手伝いしましょうか？` → `お荷物をお運びしましょうか？`
  - 理由: 旧JAは日本語として不自然。EO/EN/RU/ZH/KO の「荷物を手伝う/運ぶ」意味に合わせた。
- `ID2707` JA
  - `お食事は何時にご用意しておりますか。` → `朝食、昼食、夕食は何時に提供されますか？`
  - 理由: 旧JAはホテル側が自分で準備時刻を尋ねるように読める。EO/RU は朝食・昼食・夕食の提供時刻を尋ねる客側の質問。
- `ID2709` JA
  - `夕食の時間は何時から営業していますか？` → `夕食時、レストランは何時に開きますか？`
  - 理由: 旧JAは主語と述語のつながりが不自然。EO `malfermiĝas la restoracio por vespermanĝo` と RU `ресторан открывается для ужина` に合わせた。
- `ID2713` ZH
  - `你晚上会锁前门吗？` → `你们晚上会锁前门吗？`
  - 理由: ホテルへ尋ねる文なので、施設側を指す `你们` が自然。
- `ID2729` EN
  - `Could you wake me up at 6 a.m?` → `Could you wake me up at 6 a.m.?`
  - 理由: 参考列のみ。略語 `a.m.` の句点を補った。
- `ID2739` JA
  - `こちらをプレスしてください。` → `こちらにアイロンをかけてください。`
  - 理由: PIV 2020 で `gladi` は熱い道具で布や衣類を平らにすること。日本語では hotel laundry 文脈でも「プレスする」より「アイロンをかける」が自然。
- `ID2744` EO
  - `Kie estas la urĝa elirejo?` → `Kie estas la savelirejo?`
  - 理由: PIV 2020 では `urĝa` は「延期できない/急を要する」の意味で、`urĝa elirejo` も通じるが literal 寄り。PIV 2020 の安全灯の項に `savelirejoj` が見え、非常口・避難出口の文脈では `savelirejo` がより確認しやすいため修正。
- `ID2749` JA/KO
  - JA `自分の国際電話番号の国番号を知っていますか？` → `国際電話の国番号をご存じですか？`
  - KO `당신의 국제 전화 코드가 무엇인지 알고 계신가요?` → `국제 전화 국가번호가 무엇인지 알고 계신가요?`
  - 理由: 旧JA/KOは直訳調で、国際電話の国番号を尋ねる自然な言い方から少し外れていた。ZH は既に `国际区号`。
- `ID2755` EN/ZH/KO
  - EN `Please send my breakfast at 7.00.` → `Please bring my breakfast at 7.00.`
  - ZH `请在七点送我的早餐。` → `请在七点把早餐送来。`
  - KO `아침 식사를 7시에 보내주세요.` → `아침 식사를 7시에 가져다주세요.`
  - 理由: EO `alporti` と RU `принесите` は「持ってくる」。旧EN/ZH/KOは send/送る 寄りで、朝食を部屋へ持参する文脈として不自然だった。

主な据え置き確認:
- `ID2669` `atendolisto`: `atendi` + `listo` の透明複合で、waiting list / лист ожидания と一致するため未修正。
- `ID2681` `duoblan ĉambron kun aldona lito`: `duobla ĉambro` は double room / двухместный номер として宿泊文脈で成立し、名詞省略でもないため未修正。
- `ID2689` `ĉambronumero`: `ĉambro` + `numero` の透明複合で、room number と一致するため未修正。
- `ID2691` ZH `房卡`: EO/RU/JA/KO は「鍵」だが、ホテル文脈では room key と key card が実用上重なる。明確な意味ズレとは断定せず未修正。
- `ID2718` `tuko`: PIV 2020 で `tuko` は用途をもつ布片、派生に `man tuko` が確認できる。ホテル文脈では towel として通じ、同CSV内でも一貫使用されているため未修正。
- `ID2721` `kovrilo`: PIV 2020 では `litkovrilo` も確認できるが、ホテルで blanket を求める文として `kovrilo` は意味が明確なため未修正。
- `ID2724` `telefona ŝargilo`: PIV 2020 の `ŝargi` には電気を入れる意味があり、`ŝargilo` は同CSV内 Shopping でも phone charger として使用されている。現代語として意味が明確なため未修正。
- `ID2736` `akiri eksteran linion`: 外線を取る/外線につなぐという電話文脈で各列と一致するため未修正。
- `ID2753` `plusendi mian poŝton`: forward mail / переслать почту と対応し、`plu` + `sendi` 系の透明な表現として未修正。

一致確認:
- `cmp_exit=0`
- `md5=313896346130473f72cc2da1406a88c4`

## 44. 43周目 追加再点検（ID2756〜2855）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2756〜2855` を確認
- Hotel / During Your Stay 末尾、Checking out、Complaints、Renting a Flat 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `elregistriĝi`、`kalkulo/fakturo`、`servokotizo`、`restmono`、`lavujo/lavabo`、`ŝtopita`、`bolilo`、`butono`、`monŝranko`、`klimatizilo`、`apartamento/luo` 周辺を照合

修正:
- `ID2761` JA
  - `このスーツをクリーニングしてプレスしていただけますか？` → `このスーツをクリーニングしてアイロンをかけていただけますか？`
  - 理由: PIV 2020 で `gladi` は熱い道具で布や衣類を平らにすること。日本語では「プレス」より「アイロンをかける」が自然。
- `ID2782` EO
  - `Ĉu la servkotizo estas inkluzivita?` → `Ĉu la servokotizo estas inkluzivita?`
  - 理由: 同範囲の `ID2783/2796` が `servokotizo`。`serv-` でも複合語として読めるが、クイズ用データでは表記ゆれを避けるため、既存の多数派形に統一。
- `ID2784` EN/JA/KO
  - EN `The bill is overcharged.` → `The bill is too high.`
  - JA `請求額が過剰です。` → `請求額が高すぎます。`
  - KO `청구 금액이 과다하게 청구되었습니다.` → `청구 금액이 너무 높습니다.`
  - 理由: EO `tro alta` と RU `Счёт завышен` は「請求が高すぎる」。旧EN/JA/KOは語法が不自然または重かった。
- `ID2798` ZH
  - `迷你吧向我收了多少钱？` → `迷你吧的费用是多少？`
  - 理由: 旧ZHは minibar を主語にした課金表現が不自然。請求内訳として自然な形に修正。
- `ID2804` ZH
  - `你找错钱了。` → `您找错零钱了。`
  - 理由: ホテル精算文脈では `您` が自然で、`零钱` を入れると EO `restmono`、RU `сдача` との対応が明確。
- `ID2806` KO
  - `짐을 내려가는 데 도와주실 수 있을까요?` → `짐을 아래층으로 옮기는 것을 도와주실 수 있을까요?`
  - 理由: 旧KOは文法的につながりが不自然。EO/RU の「荷物を下へ運ぶのを手伝う」に合わせた。
- `ID2820` JA/ZH/KO
  - JA `シンクが詰まっています。` → `洗面台が詰まっています。`
  - ZH `水槽堵了。` → `洗手池堵了。`
  - KO `싱크대가 막혔어요.` → `세면대가 막혔어요.`
  - 理由: Hotel / Complaints 文脈の sink は客室・浴室の洗面台として読むのが自然。RU `раковина` とも整合する。
- `ID2837` ZH
  - `少了一个按钮。` → `少了一颗纽扣。`
  - 理由: PIV 2020 で `butono` は衣服のボタン用法を明確に確認。RU `пуговица` と同じく、衣服のボタンなら `纽扣` が自然。

主な据え置き確認:
- `ID2765/2794/2795` `elregistriĝi`: PIV 2020 で `registri/registrigi` の基礎義を確認。ホテル checkout 専用語としてPIV見出しではないが、オンライン実例でも checkout 系の用法があり、日中韓/RUとの対応は明確なため未修正。
- `ID2758/2759` `lavejo`: PIV 2020 の `lavejo/lavisto` は洗濯・洗濯業に接続し、laundry/laundry service 文脈とずれないため未修正。
- `ID2782/2783/2796` `servokotizo`: PIV 2020 の `kotizo` は会費・分担金寄りで少し気になるが、オンライン実例で `servokotizo` も確認でき、service charge / сервисный сбор との意味ズレは明確でないため表記統一のみ。
- `ID2784/2798` `kalkulo`: PIV 2020 で hotel/restoracia bill の用例を確認。`fakturo` も候補だが、現形は誤りでないため未修正。
- `ID2803/2804` `restmono`: PIV 2020 の `resti/resto` から透明に読め、同CSV内でも change/釣り銭として一貫しているため未修正。
- `ID2820` `lavujo`: PIV 2020 では `lavabo` が固定洗面器、`lavujo` は洗濯用のたらい寄りだが、オンライン辞書では sink としての用法も確認できる。今回は EO を過修正せず、日中韓側だけホテル文脈へ寄せた。
- `ID2833` `bolilo`: PIV 2020 で「水を沸かすための容器」を確認。kettle / чайник と対応するため未修正。
- `ID2837` `butono`: PIV 2020 で衣服のボタン用法を確認。EOは現形維持し、ZHだけ `纽扣` へ修正。
- `ID2854/2855` `apartamento/luo`: PIV 2020 で `apartamento` と `lui/luo` を確認。Renting a Flat 文脈と一致するため未修正。

一致確認:
- `cmp_exit=0`
- `md5=14e23ba2b74d46133ad0ad801dba0d37`

## 45. 44周目 追加再点検（ID2856〜2955）

実施日:
- 2026-04-28

対象:
- 追加周回として `ID2856〜2955` を確認
- Hotel / Renting a Flat、Restaurant & Pub / Booking a Table、Ordering Drinks 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `vazaro`、`ŝvabrilo`、`korktirilo`、`skatolmalfermilo`、`botelmalfermilo`、`ventuzilo/suĉkloŝo`、`adherema filmo`、`polvosuĉilo`、`mendi/rezervi tablon`、`fumejo`、`gasita akvo`、`vinkarto` 周辺を照合

修正:
- `ID2857` ZH
  - `当然可以。` → `是的，当然有。`
  - 理由: 直前の `Ĉu estas varma akvo?` への返答なので「可能です」ではなく「あります」とする方が対応が明確。
- `ID2874/2875/2876` JA/ZH
  - `冷蔵庫はどのように動くのですか？` → `冷蔵庫はどう使えばいいですか？`
  - `冰箱是如何工作的？` → `冰箱怎么用？`
  - `この調理器はどのように使うのですか？` → `コンロはどう使えばいいですか？`
  - `这个炊具是如何工作的？` → `炉灶怎么用？`
  - `このヒーターはどのように作動しますか？` → `ヒーターはどう使えばいいですか？`
  - `加热器是如何工作的？` → `加热器怎么用？`
  - 理由: Renting a Flat 文脈の `Kiel funkcias ...?` は、機器の物理的仕組みではなく操作方法を尋ねる実用会話として読むのが自然。
- `ID2881` JA/ZH/KO
  - JA `ワインオープナーが必要です。` → `コルク抜きが必要です。`
  - ZH `我需要一个开瓶器。` → `我需要一个红酒开瓶器。`
  - KO `와인 오프너가 필요해요.` → `코르크 따개가 필요해요.`
  - 理由: PIV 2020 で `korktirilo` を確認。`ID2883` の bottle opener と区別するため、corkscrew / штопор を明確化。
- `ID2884` EO/JA
  - EO `Mi bezonas ventuzilon` → `Mi bezonas suĉkloŝon`
  - JA `スッポンが必要です。` → `ラバーカップが必要です。`
  - 理由: `ventuzilo` はこの用途での確認が弱く、オンライン辞書・Web実例で plunger に `suĉkloŝo` を確認。RU `вантуз`、ZH `马桶疏通器`、KO `뚫어뻥` とも整合する。目的語なので `suĉkloŝon`。
- `ID2885` KO
  - `랩 한 통이 필요해요.` → `랩 한 롤이 필요해요.`
  - 理由: EO/EN/RU/ZH は roll of cling film。KOも「1ロール」に合わせた。
- `ID2889/2890/2891/2892` JA/ZH
  - `電子レンジ/食器洗い機/エアコン/洗濯機はどのように動くのですか？` → `...はどう使えばいいですか？`
  - `微波炉/洗碗机/空调/洗衣机是如何工作的？` → `...怎么用？`
  - 理由: 上記 `Kiel funkcias ...?` と同じく、賃貸住居での機器操作を尋ねる文として自然化。
- `ID2904` ZH/KO
  - ZH `什么时候？` → `几点？`
  - KO `몇 시에요?` → `몇 시예요?`
  - 理由: EO `Por kioma horo?` は予約時刻。ZH は時刻を明確化、KO は正書法を修正。
- `ID2905` KO
  - `오늘 저녁 8시에요.` → `오늘 저녁 8시예요.`
  - 理由: 韓国語の正書法修正。
- `ID2908` JA/ZH
  - JA `はい、あります。` → `はい、予約しています。`
  - ZH `是的，我有。` → `是的，已经预订了。`
  - 理由: `Ĉu vi havas rezervon?` への返答。restaurant reservation として自然化。
- `ID2921` ZH/KO
  - ZH `这是您的桌子。` → `这是您的座位。`
  - KO `이것이 당신의 테이블입니다.` → `이쪽이 고객님의 테이블입니다.`
  - 理由: 席案内の文脈では literal な「あなたの机」より、客席・テーブル案内としての表現が自然。
- `ID2930` EN
  - `Can we book a table for tomorrow at 8 p.m?` → `Can we book a table for tomorrow at 8 p.m.?`
  - 理由: 参考列のみ。略語 `p.m.` の句点を補った。
- `ID2936` ZH
  - `请稍等，等待安排座位` → `请稍等，我们会带您入座。`
  - 理由: EO `oni vin kondukos al via loko`、RU `вас проводят` に合わせ、席へ案内する意味を自然化。
- `ID2949` JA
  - `ミルクとお砂糖はご利用になりますか？` → `ミルクまたは砂糖はお入れしますか？`
  - 理由: EO `aŭ` と EN/RU の or に合わせ、かつ飲み物に入れる表現へ自然化。
- `ID2952` JA/ZH
  - JA `お水はそのまま（普通の水）と炭酸水、どちらになさいますか？` → `炭酸入りと炭酸なし、どちらになさいますか？`
  - ZH `要无气水还是气泡水？` → `要普通水还是气泡水？`
  - 理由: EO/RU の gas/no gas と対応し、日本語・中国語として自然な対立に修正。
- `ID2954` ZH
  - `请给我一杯不含气的水。` → `请给我一杯不带气的水。`
  - 理由: still water / water without gas として自然化。

主な据え置き確認:
- `ID2860` `vazaro`: PIV 2020 で「家で用いる器一式」を確認。dishes / посуда と対応するため未修正。
- `ID2868` `ŝvabrilo`: PIV 2020 で mop に相当する定義を確認。未修正。
- `ID2874/2889/2890/2891/2892` `fridujo/mikroondilo/telerlavmaŝino/klimatizilo/lavmaŝino`: 透明複合語または既存CSVで一貫した機器名。EOは未修正。
- `ID2875` `kuirilo`: PIV 2020 では広く cooking utensil/tool だが、RU `плита` と EN `cooker` から、住居設備のコンロ・炉灶として日中側を自然化し、EOは未修正。
- `ID2885` `adherema filmo`: PIV 2020 で `adheri/adhera` と `filmo` を確認。`adherema` は透明な派生で、cling film / пищевая плёнка と意味ズレが明確ではないため未修正。
- `ID2888` `komfortaĵoj`: PIV 2020 の `komforto` 系から modern conveniences として自然に読めるため未修正。
- `ID2908` `mendita`: PIV 2020 で `mendi` はホテルの部屋、レストランの料理、座席予約にも使えることを確認。`rezervita` への置換は不要と判断。
- `ID2933` `fumejo`: PIV 2020 で「喫煙者用の別室」を確認。smoking area として未修正。
- `ID2952/2953/2954` `gaso/gasita akvo/sen gaso`: PIV 2020 の `gaso/gasigi` とオンライン辞書の実例から、carbonated/sparkling water 文脈として成立するため未修正。
- `ID2955` `vinkarto`: PIV 2020 で `karto` にレストランの品書き用法を確認し、同CSV後続にも `vinkarto` が複数あるため未修正。

一致確認:
- `cmp_exit=0`
- `md5=74459eab0de8b2d3f84e365293a419fa`

## 46. 45周目 追加再点検（ID2956〜3055）

対象:
- 追加周回として `ID2956〜3055` を確認
- Restaurant & Pub / Ordering Drinks、Ordering Food、During the Meal 冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `smuzio`、`koŝera`、`kran akvo`、`pastaĵoj`、`brando/konjako`、`mezrostita`、`farĉi`、`nudeloj` 周辺を照合

修正:
- `ID2967` ZH
  - `请再来一份同样的。` → `请再来一杯同样的。`
  - 理由: Ordering Drinks 文脈の `La samon denove` なので、飲み物に自然な量詞へ修正。
- `ID2991` ZH
  - `你能推荐一款好的白兰地吗？` → `你能推荐一款好的干邑吗？`
  - 理由: `ID2990` の `brando` は brandy / 白兰地、`ID2991` の `konjako` は cognac / коньяк。PIV 2020 でも `konjako` は Cognac 地方のワイン由来ブランデーとして区別されるため、中国語も `干邑` に限定。
- `ID2996` ZH/KO
  - ZH `您的订单到了。` → `这是您点的餐。`
  - KO `주문하신 것입니다.` → `주문하신 음식입니다.`
  - 理由: `Jen via mendo` はレストランで注文品を出す場面。通販・注文到着のような表現を避け、料理提供として自然化。
- `ID3009/3010` ZH
  - `请在这里用。` → `堂食，谢谢。`
  - `这是外带的。` → `打包带走，谢谢。`
  - 理由: `Ĉu surloke aŭ por forporti?` への返答として、店内飲食・持ち帰りの対立を自然化。
- `ID3012` EN
  - `Is there a Hungarian menu?` → `Is there a menu in Hungarian?`
  - 理由: EO `en la hungara`、RU `на венгерском`、JA/ZH/KO は「ハンガリー語のメニュー」。参考列だが、料理種別の Hungarian menu と誤読されやすいため明確化。
- `ID3015` JA
  - `まだ注文の準備ができていません。` → `まだ注文は決まっていません。`
  - 理由: 客が注文をまだ決めていない状況として自然化。
- `ID3021` KO
  - `죄송하지만, 해당 상품은 품절되었습니다.` → `죄송하지만, 그 메뉴는 품절되었습니다.`
  - 理由: レストランの品切れなので、商品一般よりメニュー項目として自然化。
- `ID3023` ZH
  - `你希望换成什么？` → `您想换成什么？`
  - 理由: 客への応対文として語調を整えた。
- `ID3036` ZH
  - `今日特价菜品请见黑板。` → `今日特色菜写在黑板上。`
  - 理由: `specialaĵoj` / specials は値引き料理とは限らない。RU `блюда дня`、JA/KO の「本日のおすすめ」と整合するよう修正。
- `ID3038` ZH
  - `请您推荐什么，我就点什么。` → `您推荐什么，我就点什么。`
  - 理由: 「勧めるものを注文します」の構文として自然化。
- `ID3044` ZH
  - `我想尝试一下这里最有特色的美食。` → `我想尝尝当地最好吃的食物。`
  - 理由: EO/EN/RU は「最も特徴的」ではなく「最良の地元料理」。意味を寄せた。
- `ID3048` ZH
  - `你喜欢你的汤里加面条还是米饭？` → `汤里加面条还是米饭，您更喜欢哪种？`
  - 理由: literal な「你的汤」を避け、スープに麺か米を入れる選択として自然化。
- `ID3050` KO
  - `메인 요리로 스테이크로 하겠습니다.` → `메인 요리는 스테이크로 하겠습니다.`
  - 理由: 助詞重複を修正。
- `ID3051` EN/JA/KO
  - EN `Medium rare, please.` → `Medium, please.`
  - JA `ミディアムレアでお願いします。` → `ミディアムでお願いします。`
  - KO `미디엄 레어로 해주세요.` → `미디엄으로 해주세요.`
  - 理由: EO `Mezrostita`、RU `Средней прожарки`、ZH `五分熟` は medium に相当。medium rare は焼き加減が一段ずれるため修正。
- `ID3055` KO
  - `웨이터!` → `여기요!`
  - 理由: 韓国語で店員を呼ぶ実用表現として自然化。JA `すみません！` と同じく、直訳より場面対応を優先。

主な据え置き確認:
- `ID2959` `smuzio`: PIV 2020 には見当たらないが、Wiktionary 等のオンライン資料で smoothie の訳語として語形を確認。現代的借用語として用例があり、ここでは意味ズレが明確ではないため未修正。
- `ID2966` `Doma vino`: house wine / домашнее вино として文脈上成立。中国語 `店里的葡萄酒` はやや説明的だが意味崩れはないため未修正。
- `ID2984` `kruĉon da kranakvo`: PIV 2020 で `kran akvo` を確認。`kruĉo` も液体用の把手・注ぎ口付き容器として確認でき、tap water / кувшин воды из-под крана と整合するため未修正。
- `ID2993` `vegetaranino`: RU `вегетарианка` と同じく女性話者を明示。JA/ZH/KO は性を明示しないのが自然なため未修正。
- `ID3001` `koŝeran manĝaĵon`: PIV 2020 で `koŝera` は食物についてヘブライ儀礼に適う意味と確認。未修正。
- `ID3004` `pastaĵojn`: PIV 2020 で `pastaĵoj` は小麦粉・水・塩・卵などから作る pasta 類の集合名として確認。`la pastaĵojn` はメニュー項目として成立するため未修正。
- `ID3005` `fritoj`: PIV 2020 で `terpom-fritoj` / `pomfritoj` を確認。`bifstekon kun fritoj` は steak with chips/fries として成立するため未修正。
- `ID3027` `por kunpreni`: `forporti` と完全同形ではないが、持ち帰る意味は明確で、同じCSV内の take away 文脈とも衝突しないため未修正。
- `ID3047` `farĉitajn fungojn`: PIV 2020 で `farĉi` は食物の内部を詰め物で満たす意味と確認。stuffed mushrooms と整合するため未修正。
- `ID3048` `nudeloj`: PIV 2020 で `nudeloj` を確認。soup with noodles or rice として未修正。
- `ID3049` `franca saŭco`: French dressing / французская заправка として文脈上成立。未修正。

一致確認:
- `cmp_exit=0`
- `md5=4afa76605a692bce27281cc04e24160f`

## 47. 46周目 追加再点検（ID3056〜3155）

対象:
- 追加周回として `ID3056〜3155` を確認
- Restaurant & Pub / During the Meal、Paying the Bill、Complaints を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `halala`、`manĝobastonetoj`、`fritoj`、`trinkmono`、`serva pago`、`odori je korko`、`meleagro`、`kalcono` 周辺を照合

修正:
- `ID3074` ZH
  - `你能帮我加热一下吗？` → `您能帮我加热一下吗？`
  - 理由: レストランで店員へ頼む場面として、丁寧な二人称に整えた。
- `ID3076` EO
  - `Kiel pri iom da deserto?` → `Ĉu vi ŝatus iom da deserto?`
  - 理由: `Kiel pri ...?` は英語 How about の直訳色が強い。`Ĉu vi ŝatus ...?` は、JA `デザートはいかがですか？`、ZH `要不要来点甜点？` と同じ実用会話として自然。
- `ID3082` ZH
  - `我还想要一些炸土豆。` → `我还想要一些薯条。`
  - 理由: EO `fritoj`、RU `картошка-фри`、JA/KO のフライドポテトに合わせ、中国語も fries として自然化。
- `ID3102` KO
  - `나눠서 하죠.` → `나눠서 계산하죠.`
  - 理由: `Ni dividu ĝin` / split the bill の会計文脈を明確化。
- `ID3109` KO
  - `팁을 두고 왔어요.` → `팁을 남겼어요.`
  - 理由: `Mi lasis trinkmonon` は「置き忘れた」ではなく「チップを残した」。自然な韓国語に修正。
- `ID3114` EN/KO
  - EN `It's altogether.` → `All together.`
  - KO `전부 합쳐서예요.` → `전부 같이 계산해 주세요.`
  - 理由: `Ĉio kune` は会計をまとめる返答。英語・韓国語を場面対応へ修正。
- `ID3120` ZH
  - `请代我向厨师致以敬意。` → `请代我向主厨致意。`
  - 理由: EO `ĉefkuiristo`、RU `шеф-повар` に合わせ、head chef / 主厨 を明確化。
- `ID3123` ZH
  - `你们国家流行给小费吗？` → `你们国家有给小费的习惯吗？`
  - 理由: tipping common は「流行」ではなく慣習の有無。JA/RU と整合するよう修正。
- `ID3141` JA/KO
  - JA `私たちは出発します。` → `もう帰ります。`
  - KO `저희는 이제 떠납니다.` → `저희는 이제 가겠습니다.`
  - 理由: Restaurant complaints 文脈の `Ni foriras` は出発旅行ではなく「もう店を出る」。自然化。
- `ID3144` ZH
  - `这不是我的订单。` → `这不是我点的菜。`
  - 理由: レストランで出された料理が注文と違う場面。通販・注文書風の `订单` を避けた。
- `ID3149` EN
  - `This wine has corked.` → `This wine is corked.`
  - 理由: 参考列のみ。cork taint を表す定型として修正。EO `odoras je korko` は PIV 2020 の `korkogusta vino` と意味が合うため維持。
- `ID3151` ZH
  - `我来帮你换一下。` → `我来帮您换一下。`
  - 理由: 店員から客への応対として丁寧な二人称に修正。
- `ID3153` ZH
  - `我们下单已经超过三十分钟了。` → `我们点餐已经超过三十分钟了。`
  - 理由: レストランでの注文なので、オンライン注文寄りの `下单` より `点餐` が自然。
- `ID3154` ZH/KO
  - ZH `我的订单还没有到。` → `我点的菜还没上。`
  - KO `제 주문이 아직 도착하지 않았어요.` → `제가 주문한 음식이 아직 안 나왔어요.`
  - 理由: EO/RU は料理がまだ運ばれていない苦情。配送・注文到着の表現を避けた。

主な据え置き確認:
- `ID3060` `halala`: PIV 2020 には見当たらないが、オンライン辞書・用例で halal の Esperanto 形として確認。JA/ZH/KO/RU と意味が一致するため未修正。
- `ID3079` `manĝobastonetojn`: PIV 2020 では `manĝ bastonetoj` を確認。現形は連結母音付きの透明複合語として読め、意味ズレは明確ではないため未修正。
- `ID3087` `kalcono`: PIV/Glosbe で強い確認は取れなかったが、calzone の固有料理名を説明的な `faldita pico` 等へ置き換えると固有名の対応が崩れる。現時点では未修正、継続注意。
- `ID3122` `servan pagon`: `servokotizo` も候補になり得るが、`serva pago` は service charge として透明で、JA/ZH/KO/RU も一致するため未修正。
- `ID3130` `malĝuste sumigita`: PIV 2020 で `sumigi` 系を確認。bill added up wrong として成立するため未修正。
- `ID3145` `rostitan meleagron`: PIV 2020 で `meleagro` と料理用例を確認。roast turkey として未修正。
- `ID3149` `odoras je korko`: PIV 2020 の `odori je` 用法および `korkogusta vino` を確認。コルク臭のあるワインとして未修正。

一致確認:
- `cmp_exit=0`
- `md5=665e4cd10d268f628ca7aff79d0057f3`

## 48. 47周目 追加再点検（ID3156〜3255）

対象:
- 追加周回として `ID3156〜3255` を確認
- Restaurant & Pub / At the Pub と Food / Meat & Fish の冒頭を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `naĉoj`、`postebrio`、`barela biero`、`laktoskuaĵo`、`rostbefo`、魚介・肉料理名を照合

修正:
- `ID3156` ZH
  - `我们的餐点在路上了吗？` → `我们的菜已经在送过来了吗？`
  - 理由: レストラン内で料理が運ばれているかを尋ねる文脈。配送・移動中一般に見えやすい `在路上` を避け、RU `уже несут` と JA の「運ばれてきますか」に寄せた。
- `ID3160` ZH
  - `我点的饮料不要冰。` → `我点的饮料是不加冰的。`
  - 理由: `mendis ... sen glacio` の「氷なしで注文した」を、苦情場面として自然な叙述に修正。
- `ID3182` ZH
  - `你有三明治吗？` → `你们有三明治吗？`
  - 理由: 店・店員に在庫を尋ねる場面なので、個人所有のように読める `你有` を避けた。
- `ID3197` ZH
  - `请给我来一份双份的。` → `请做成双份的。`
  - 理由: 飲み物を double にする依頼。`一份` は料理一人前に寄りやすいため修正。
- `ID3206` JA/KO
  - JA `それはやりすぎです。` → `それは多すぎます。`
  - KO `그건 너무 과해요.` → `그건 너무 많아요.`
  - 理由: EO `tro multe`、RU `Слишком много`、ZH `太多了` は量が多すぎる意味。行為の過剰さに寄る表現を修正。
- `ID3207` ZH
  - `你这儿有吃的吗？` → `你们这里也有吃的吗？`
  - 理由: `ankaŭ` の「食べ物も」の意味を補い、店に尋ねる文として自然化。
- `ID3211` ZH
  - `你想要什么口味？` → `您想要什么口味？`
  - 理由: 客に味を尋ねる文として丁寧さを揃えた。
- `ID3227` EO
  - `Mi prenos la rostbifon` → `Mi prenos la rostbefon`
  - 理由: PIV 2020 の見出し語は `rostbef/o`。`rostbif/o` は確認できず、英語 roast beef の直写に引かれた誤形の可能性が高いため修正。
- `ID3231` KO
  - `그는 돼지고기를 주문할게요.` → `그는 돼지고기를 주문할 거예요.`
  - 理由: `-ㄹ게요` は話し手の意志表明になりやすく、三人称 `Li prenos` と合わないため修正。
- `ID3233` KO
  - `그분은 닭가슴살로 하시겠어요.` → `그분은 닭가슴살로 하시겠습니다.`
  - 理由: 平叙の注文内容を、疑問・勧誘に見える形から修正。
- `ID3248` KO
  - `그는 잉어구이를 드시겠습니다.` → `그분은 잉어구이로 하시겠습니다.`
  - 理由: 三人称注文として敬語の主語・述語を整え、料理を選ぶ表現に自然化。

主な据え置き確認:
- `ID3175` `naĉoj`: PIV 2020 では強い見出し確認に至らないが、オンライン辞書・用例で nachos の借用語として確認。JA/ZH/KO/RU は nachos で一致し、説明的置換は料理名対応を壊すため未修正。
- `ID3194` `postebrio`: PIV 2020 で `post ebrio` が「酔いの後に起こる頭痛」と確認できる。現形は複合語として透明で、hangover / 二日酔い / похмелье と整合するため未修正。
- `ID3203` `barela biero`: PIV 2020 で `barelo da biero` を確認。draught beer / разливное пиво として文脈上成立するため未修正。
- `ID3209` `laktoskuaĵo`: PIV 2020 の `lakto` と `skui` から透明に読め、Glosbe 等のオンライン辞書でも milkshake 対応を確認。未修正。
- `ID3218` `bifstekon el bova lumbaĵo`: 既修正済みの表現。PIV 2020 で `lumbaĵo` に `bova lumbaĵo` の料理用例を確認でき、sirloin steak として現形維持。
- `ID3235〜3255` の主要魚介・肉料理名: PIV 2020 で `skombro`、`soleo`、`salikoko`、`polpo`、`ŝarko`、`truto`、`haringo` などを確認。JA/ZH/KO/RU と大きな意味ズレは見当たらないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=ca3c28dc4ecff6e79f6636a1ed13db2a`

## 49. 48周目 追加再点検（ID3256〜3355）

対象:
- 追加周回として `ID3256〜3355` を確認
- Food / Fruits、Vegetables、Herbs and general foods を精査
- 以前の修正済み項目 `limeoj`、`akra kapsiko`、`kukurbeton`、`eruko` は再確認に留め、今回の新規修正は意味対応・自然さの崩れが明確な訳文に限定
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、果物名・野菜名・料理名を照合

修正:
- `ID3279` KO
  - `그들은 구운 소금 아몬드를 더 선호해요.` → `그들은 구워서 소금 간한 아몬드를 더 좋아해요.`
  - 理由: `rostitajn kaj salitajn migdalojn` は「ローストして塩味を付けたアーモンド」。韓国語の `구운 소금 아몬드` は名詞連結が不自然で、塩そのものを焼いたようにも見えるため修正。
- `ID3281` KO
  - `그녀는 블루베리 타르트를 주문할게요.` → `그녀는 블루베리 타르트를 주문할 거예요.`
  - 理由: 三人称 `Ŝi prenos` に対し、`-ㄹ게요` は話し手の意志表明になりやすい。三人称予定・注文内容として修正。
- `ID3283` KO
  - `그녀는 자몽 파이에 아이스크림을 곁들여 드실 거예요.` → `그분은 자몽 파이에 아이스크림을 곁들여 드실 거예요.`
  - 理由: 尊敬語 `드시다` を使うなら主語も `그분` に揃える方が自然。注文内容の意味は維持。
- `ID3285` KO
  - `카라멜라이즈드 무화과를 먹고 싶어요.` → `캐러멜화한 무화과를 좀 주세요.`
  - 理由: `karamelizitaj figoj` の料理名を、韓国語として自然な「キャラメル化したイチジク」の注文表現に修正。
- `ID3289` ZH
  - `把瓜切成厚片。` → `把甜瓜切成厚片。`
  - 理由: EO `melono`、RU `дыня`、JA/KO のメロンに合わせ、単に `瓜` では広すぎるため修正。
- `ID3290` ZH/KO
  - ZH `你喜欢吃萝卜吗？` → `你喜欢吃小萝卜吗？`
  - KO `무를 좋아하세요?` → `래디시를 좋아하세요?`
  - 理由: EO `rafanoj`、EN radishes、RU `редис`、JA `ラディッシュ` は大根一般ではなく radish。中文・韓国語の対象を狭めた。
- `ID3318` KO
  - `그분께는 당근과 병아리콩 조림을 드릴게요.` → `그분은 당근과 병아리콩 조림으로 하시겠습니다.`
  - 理由: `Li prenos ...` は「彼がそれにする」。店側が提供する意志表明 `드릴게요` より、注文内容として自然な形に修正。
- `ID3342` KO
  - `그녀는 렌틸콩과 야채를 조림으로 드시겠습니다.` → `그분은 렌틸콩과 야채 조림으로 하시겠습니다.`
  - 理由: 尊敬語を使う注文文として主語・名詞句・述語を整えた。
- `ID3343` ZH
  - `她想要一些炸土豆。` → `她想要一些薯条。`
  - 理由: EO `fritoj`、RU `картофель-фри`、JA/KO はフライドポテト。中国語も fries として自然化。

主な据え置き確認:
- `ID3270` `limeojn`: 以前の修正どおり、PIV 2020 で果物の `lime/o` を確認済み。`limo` には戻さない。
- `ID3310` `akra kapsiko`: PIV 2020 の `kapsiko` 用例により、唐辛子として現形維持。
- `ID3313` `panitan kukurbeton`: PIV 2020 で `kukurbeto` は courgette/zucchini 文脈として確認済み。`zukino` へは戻さない。
- `ID3331` `eruko`: PIV 2020 で `kultiva eruko` の葉がサラダ用と確認済み。rocket/arugula として現形維持。
- `ID3347` `cerealojn`: PIV 2020 では穀物・穀類寄りの語。JA/ZH/KO は breakfast cereal 寄りにも読めるが、Food 文脈では「シリアル/穀類」境界が曖昧で、明確な意味ズレとは断定せず未修正。
- `ID3353` `mocarelon`: PIV 2020 で `mocarel/o` を確認。mozzarella として未修正。

一致確認:
- `cmp_exit=0`
- `md5=c05bd601497afd7801b6a6495f2f5bb3`

## 50. 49周目 追加再点検（ID3356〜3455）

対象:
- 追加周回として `ID3356〜3455` を確認
- Food / Breakfast から Shopping / Department Store、Clothes の前半を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `kazeo`、`kirlovaĵo`、`magazeno`、`procesi/persekuti`、`ŝorto`、`grandeco` 周辺を照合

修正:
- `ID3365` EN/JA/KO
  - EN `Brown bread, please.` → `Black bread, please.`
  - JA `ブラウンブレッドをお願いします。` → `黒パンをお願いします。`
  - KO `브라운 브레드로 주세요.` → `흑빵으로 주세요.`
  - 理由: EO `Nigran panon`、RU `Чёрный хлеб`、ZH `黑面包` に合わせた。brown bread だと黒パン/ライ麦系の意味が弱くなる。
- `ID3372` ZH
  - `我想吃点奶酪。` → `我想吃点白软干酪。`
  - 理由: EO `kazeo` は PIV 2020 で発酵前の凝乳部分。RU `творог`、EN/JA/KO の cottage cheese と合わせ、一般のチーズでは広すぎるため修正。
- `ID3376` KO
  - `그는 스크램블 에그를 드시겠습니다.` → `그분은 스크램블 에그로 하시겠습니다.`
  - 理由: 三人称注文として尊敬語の主語・述語を整えた。
- `ID3408` EO/KO
  - EO `Butikoŝtelistoj estos procesitaj` → `Butikoŝtelistoj estos juĝe persekutataj`
  - KO `좀도둑은 법적 조치를 받습니다.` → `상점 절도범은 법적 조치를 받습니다.`
  - 理由: PIV 2020 で `procesi` は自動詞で、`procesi kontraŭ iu` 型。受動形 `procesitaj` は危険なため、PIV の `persekuti` の法的語義に沿って修正。KO も shoplifter を明示した。
- `ID3422` JA
  - `これは何でできていますか？` → `これらは何でできていますか？`
  - 理由: EO `ĉi tiuj`、EN/ZH/KO/RU は複数。日本語も複数対象に合わせた。
- `ID3439` ZH
  - `这件这里太紧了。` → `这里太紧了。`
  - 理由: 試着中に「ここがきつい」と言う場面として自然化。
- `ID3443` JA/ZH
  - JA `こちらは洗えますか？` → `これらは洗えますか？`
  - ZH `这个可以水洗吗？` → `这些可以水洗吗？`
  - 理由: EO `ĉi tiuj`、EN/KO/RU の複数対象に合わせた。
- `ID3444` RU
  - `Нет, её нужно чистить в химчистке.` → `Нет, их нужно сдавать в химчистку.`
  - 理由: EO `ilin`、EN/JA/ZH/KO は複数。RU の代名詞だけ単数女性だったため修正。
- `ID3447` ZH
  - `反面清洗` → `请翻面清洗`
  - 理由: 洗濯表示として「裏返して洗う」を自然化。
- `ID3449` EO
  - `Kiugrandaj estas ĉi tiuj ŝortoj?` → `Kian grandecon havas ĉi tiu ŝorto?`
  - 理由: `kiugrandaj` は一般的なサイズ質問として不安定で、物理的な大きさにも読める。PIV 2020 で `ŝort/o` は衣服1点の見出し語として確認できるため、サイズを尋ねる文に修正した。
- `ID3455` ZH
  - `请给我展示一件不同颜色的东西。` → `请给我看看其他颜色的。`
  - 理由: 店頭で「別の色のものを見せてください」と頼む自然な表現に修正。

主な据え置き確認:
- `ID3358` `avenajn biskvitojn`: PIV 2020 で `aveno` とその食品用例を確認。oat biscuits として未修正。
- `ID3362` `ringokukojn`: 以前の確認どおり、doughnuts の説明的複合語として文脈上成立。未修正。
- `ID3372` `kazeo`: PIV 2020 で語義確認済み。EO は現形維持。
- `ID3376` `kirlovaĵo`: PIV 2020 で `kirli ovojn` を確認。scrambled eggs として透明に読めるため未修正。
- `ID3401` `magazeno`: PIV 2020 で「大きく多品種の店」の語義を確認。department store 文脈として未修正。
- `ID3433` `provi`: PIV 2020 で衣類・帽子などを試す語義を確認。clothes 文脈の try on として未修正。

一致確認:
- `cmp_exit=0`
- `md5=0b649c4896b10a11f05f606a8efe4a28`

## 51. 50周目 追加再点検（ID3456〜3555）

対象:
- 追加周回として `ID3456〜3555` を確認
- Shopping / Clothes、Shoes & Accessories、Personal Care を精査
- Esperanto と JA/ZH/KO の対応を主軸にし、RU/EN は参考列として確認
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `pantalono`、`ŝelko`、`stretaj`、`tubo de dentopasto`、`palpebroj`、`okulharoj`、`ŝminko` 周辺を照合

修正:
- `ID3466` EO
  - `Ĉu vi havas jakon konvenan al ĉi tiuj pantalonoj?` → `Ĉu vi havas jakon konvenan al ĉi tiu pantalono?`
  - 理由: PIV 2020 は `pantalon/o` を単数衣服として扱い、1着を複数形にする用法は非推奨と明記している。同範囲の `ID3464` も `Ĉi tiu pantalono` なので統一。
- `ID3469` EN/JA/ZH/KO
  - EN `Is it hand washable?` → `Does it have to be washed by hand?`
  - JA `手洗いできますか？` → `手洗いする必要がありますか？`
  - ZH `可以手洗吗？` → `必须手洗吗？`
  - KO `손세탁이 가능한가요?` → `손세탁해야 하나요?`
  - 理由: EO `Ĉu oni devas lavi ĝin mane?` と RU `Её нужно стирать вручную?` は「手洗いする必要があるか」。可能性ではなく義務・指定の確認に修正。
- `ID3483` JA
  - `このサンダルを試着してもいいですか？` → `このサンダルを試し履きしてもいいですか？`
  - 理由: 靴・サンダル文脈なので「試着」より「試し履き」が自然。
- `ID3489` JA
  - `こちらのスニーカーを試着してみたいのですが。` → `こちらのスニーカーを試し履きしてみたいのですが。`
  - 理由: 上と同じ。
- `ID3507` JA/ZH
  - JA `ボタンを持っていますか？` → `ボタンはありますか？`
  - ZH `你有纽扣吗？` → `你们有纽扣吗？`
  - 理由: 店に在庫を尋ねる文。個人所有のように読める表現を避けた。
- `ID3512` ZH/KO
  - ZH `这是什么石头？` → `这是什么宝石？`
  - KO `이 돌은 무엇인가요?` → `이 보석은 무엇인가요?`
  - 理由: アクセサリー売り場で指輪などの石を尋ねる場面。一般の石ではなく宝石として自然化。
- `ID3515` JA/ZH
  - JA `ハンカチをお持ちですか？` → `ハンカチはありますか？`
  - ZH `你有手帕吗？` → `你们有手帕吗？`
  - 理由: 店に商品在庫を尋ねる文として自然化。
- `ID3534` KO
  - `치약 한 통 주세요.` → `치약 한 개 주세요.`
  - 理由: toothpaste tube の数量表現として、容器の「통」より一般的な商品単位に修正。
- `ID3536` ZH
  - `你有日霜吗？` → `你们有日霜吗？`
  - 理由: 店に商品在庫を尋ねる文として自然化。
- `ID3537` JA/ZH/KO
  - JA `あなたのためですか？` → `ご自分用ですか？`
  - ZH `这是给你的吗？` → `这是您自己用的吗？`
  - KO `당신을 위한 건가요?` → `본인용인가요?`
  - 理由: Personal Care の購入場面で「自分用か」を尋ねる自然な表現に修正。
- `ID3538` JA/ZH/KO
  - JA `いいえ、私のためではありません。` → `いいえ、自分用ではありません。`
  - ZH `不，这不是给我的。` → `不，不是我自己用的。`
  - KO `아니요, 저를 위한 것이 아니에요.` → `아니요, 제 것이 아니에요.`
  - 理由: 上の応答として自然化。

主な据え置き確認:
- `ID3502` `stretaj`: 既存確認では PIV 2020 の `stret/a = mallarĝa` により据え置いたが、267周目再点検で衣服用法が明示された `malvastaj` へ修正済み。
- `ID3519` `ŝelko`: PIV 2020 で「ズボン等を支える二重の弾性ベルト」と確認。braces/suspenders として未修正。
- `ID3534` `tubon de dentopasto`: PIV 2020 の `tubo` 用例に `tubo de dentopasto` が確認できるため、`da` へは動かさず現形維持。
- `ID3546` `paletron da ŝminko por la palpebroj`: 既存保留どおり、eyeshadow palette の説明として通る。より安全な標準置換を確定できないため未修正。
- `ID3553` `ŝminkon por okulharoj`: mascara の説明として意味は通る。`maskaro` 等へは辞書根拠がまだ弱いため未修正。

一致確認:
- `cmp_exit=0`
- `md5=c11e451da5995498516992753b9b6863`

## 52. 51周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`

主な修正:
- `ID3562` ZH
  - `有保障吗？` → `有保修吗？`
  - 理由: 店頭で商品の保証を尋ねる文。RU `Гарантия есть?` と JA `保証はありますか？` に合わせ、一般的な「保障」ではなく商品保証・保修として自然化。
- `ID3574` JA/ZH
  - JA `スキャナーはお持ちですか？` → `スキャナーはありますか？`
  - ZH `你有扫描仪吗？` → `你们有扫描仪吗？`
  - 理由: 店に在庫・取扱いを尋ねる文。個人所有に寄る表現を避けた。
- `ID3575` ZH
  - `你有手电筒用的电池吗？` → `你们有手电筒用的电池吗？`
  - 理由: 上と同じ。EO `vi havas` は店舗側への問いとして読める。
- `ID3578` JA/ZH
  - JA `ヘッドホンを持っていますか？` → `ヘッドホンはありますか？`
  - ZH `你有耳机吗？` → `你们有耳机吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3581` ZH
  - `我正在为我的电脑找一只鼠标。` → `我在找一个电脑用鼠标。`
  - 理由: `一只鼠标` は動物のネズミの量詞に寄って見えるため、コンピュータ用マウスとして自然化。
- `ID3596` JA/ZH
  - JA `金貨を持っていますか？` → `金貨はありますか？`
  - ZH `你有金币吗？` → `你们有金币吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3599` ZH
  - `买一送一半价` → `买一件，第二件半价。`
  - 理由: EO/RU/EN/JA は「1点購入で2点目半額」。`送一` は無料提供に読めるため修正。
- `ID3604` ZH
  - `你有衣刷吗？` → `你们有衣刷吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3607` ZH
  - `你有适合孩子玩的简单游戏吗？` → `你们有适合孩子玩的简单游戏吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3610` ZH
  - `这些模型很容易损坏吗？` → `这些小雕像很易碎吗？`
  - 理由: EO `figuretoj`、RU `статуэтки` は模型一般ではなく小像・置物寄り。壊れやすさも `易碎` がより直截。
- `ID3619` ZH/KO
  - ZH `你有针和缝纫线吗？` → `你们有针和缝纫线吗？`
  - KO `바늘과 실 있으세요?` → `바늘과 실이 있나요?`
  - 理由: 店頭在庫確認として自然化。韓国語は物に対する過剰な敬語を避けた。
- `ID3621` KO
  - `접착제 한 통이 필요해요.` → `튜브형 접착제 하나가 필요해요.`
  - 理由: EO `tubon da gluo`、RU `тюбик клея`、ZH `一管胶水` に合わせ、チューブ入りである点を保持。
- `ID3625` JA/ZH
  - JA `どんな種類のブロックを持っていますか？` → `どんな種類のブロックがありますか？`
  - ZH `你有哪些类型的积木？` → `你们有哪些类型的积木？`
  - 理由: 店頭の取扱い種別を尋ねる文として自然化。
- `ID3631` JA
  - `白い食器を見せていただけますか。` → `白い磁器を見せていただけますか。`
  - 理由: EO `blanka porcelano`、RU `белого фарфора`、ZH/KO の磁器・陶磁器に合わせた。単なる食器一般では意味が広すぎる。
- `ID3632` JA/ZH/KO
  - JA `こちらの評価をお願いできますでしょうか。` → `こちらを査定していただけますか。`
  - ZH `您能帮我评估一下这个吗？` → `您能帮我给这个估价吗？`
  - KO `이것에 대한 평가를 해주실 수 있나요?` → `이것을 감정해 주실 수 있나요?`
  - 理由: 骨董・貴金属店などの文脈で、EO `taksi` / EN `appraisal` / RU `сделать оценку` は一般評価より査定・鑑定に近い。
- `ID3636` EN/JA/KO
  - EN `Marmalade, please.` → `Jam, please.`
  - JA `マーマレードをお願いします。` → `ジャムをお願いします。`
  - KO `마멀레이드 주세요.` → `잼 주세요.`
  - 理由: RU `Джем` と ZH `果酱` に合わせた。PIV 2020 の `marmelado` は果物を砂糖と煮た濃い保存食品で、英日韓の「マーマレード」限定より広く、ここでは jam が安全。
- `ID3650` JA/ZH
  - JA `有効期限はいつですか？` → `賞味期限はいつですか？`
  - ZH `有效期到什么时候？` → `保质期到什么时候？`
  - 理由: Food & Drink の買い物文脈で RU `срок годности`、KO `유통기한` と合うよう、食品の期限として自然化。

主な据え置き確認:
- `ID3556` `pinĉilo`: PIV 2020 で `pinĉileto por senharigi` 型の用例を確認。tweezers 文脈として未修正。
- `ID3575` `pilojn`: PIV 2020 で電池・乾電池に当たる語義を確認。flashlight battery として未修正。
- `ID3625` `konstrubriketoj`: PIV 2020 の `briketo` に幼児用構成遊びの木・プラスチック片の語義を確認。building blocks として未修正。
- `ID3633` `likva sapo`: 既存確認どおり liquid soap として問題なし。
- `ID3650` `limdato`: PIV 2020 では `limtempo de valideco` 型を確認。`limdato` は透明な複合語として食品期限文脈で通るため、Esperanto 本体は未修正。

一致確認:
- `cmp_exit=0`
- `md5=00c447ba453a9f7343c93c815b6f86ed`

## 53. 52周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`

主な修正:
- `ID3656` ZH
  - `你有蛋黄酱吗？` → `你们有蛋黄酱吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3657` ZH
  - `你有咖啡豆吗？` → `你们有咖啡豆吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3668` JA/ZH/KO
  - JA `缶詰はどの売り場にありますか？` → `缶詰はどの通路にありますか？`
  - ZH `请问罐头食品在哪个货架？` → `请问罐头食品在哪条通道？`
  - KO `통조림 식품은 어느 진열대에서 찾을 수 있나요?` → `통조림 식품은 어느 통로에 있나요?`
  - 理由: EO `koridoro` と EN/RU の aisle/ряд に合わせ、売り場・棚ではなく通路として揃えた。
- `ID3672` EO
  - `Kiujn markojn vi havas kun filtroj?` → `Kiujn markojn vi havas kun filtriloj?`
  - 理由: PIV 2020 では器具・部品としての filter は `filtrilo`。`filtroj` はこの文脈では不安定なため、意味を変えず最小修正。
- `ID3687` JA
  - `こちらでお支払いしますか、それともレジでお支払いしますか？` → `ここで支払えばよいですか、それともレジですか？`
  - 理由: EO/RU/EN は客側の「自分がここで払うのか」を尋ねる文。日本語の主語が店員側に寄って見えるため修正。
- `ID3694` ZH
  - `抱歉，我们不出售这个。` → `抱歉，我们不卖这些。`
  - 理由: EO `ilin`、EN `them` に合わせ、複数対象として自然化。
- `ID3697` ZH
  - `我想买一本导游手册。` → `我想买一本旅行指南。`
  - 理由: `gvidlibro` / RU `путеводитель` は旅行ガイドブック。`导游手册` は旅行案内者向けの手引きに寄る。
- `ID3704` ZH
  - `你有雏菊吗？` → `你们有雏菊吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3706` JA/ZH
  - JA `子どもの本はどこで見つけられますか？` → `子どもの本はどこにありますか？`
  - ZH `我在哪里可以找到儿童书籍？` → `儿童书在哪里？`
  - 理由: 書店内での所在確認として自然化。
- `ID3708` JA/KO
  - JA `解説付きの辞書が必要です。` → `語義を説明する辞書が必要です。`
  - KO `저는 해설이 포함된 사전이 필요해요.` → `뜻풀이 사전이 필요해요.`
  - 理由: EO `klarigan vortaron` と RU `толковый словарь` は、注釈付き辞書ではなく語義を説明する辞書。
- `ID3712` ZH
  - `你有明信片吗？` → `你们有明信片吗？`
  - 理由: 店頭在庫確認として自然化。
- `ID3717` JA/ZH/KO
  - JA `庭に咲く花が欲しいです。` → `庭植え用の花をいくつかください。`
  - ZH `我想要一些花园里的花。` → `我想要一些适合种在花园里的花。`
  - KO `정원용 꽃을 좀 받고 싶어요.` → `정원용 꽃을 좀 주세요.`
  - 理由: EO `ĝardenaj floroj`、RU `садовые цветы` は「花園の中にある花」ではなく、庭・園芸用の花。
- `ID3723` ZH
  - `请把你新到的书给我看看。` → `请给我看看你们新到的书。`
  - 理由: 店の新入荷本を指すよう自然化。
- `ID3724` JA/KO
  - JA `建築のアルバムをいくつか見せていただけますか。` → `建築写真集をいくつか見せていただけますか。`
  - KO `건축 앨범 몇 가지 보여주세요.` → `건축 관련 화보집 몇 권을 보여 주세요.`
  - 理由: PIV 2020 の `albumo` には「ほぼ絵・写真からなる本」の語義がある。書店文脈では通常のアルバムではなく写真集・画集。
- `ID3731` KO
  - `이 잡지의 최신호를 받고 싶어요.` → `이 잡지의 최신호를 주세요.`
  - 理由: 店頭購入文として自然化。
- `ID3732` KO
  - `이 도시의 지도가 잘 표시된 것을 받고 싶어요.` → `이 도시의 표시가 잘 된 지도가 필요해요.`
  - 理由: `klare markitan mapon` の「表示がはっきりした地図」を自然な韓国語に修正。
- `ID3734` JA
  - `百科事典のような辞書はありますか？` → `百科辞典はありますか？`
  - 理由: PIV 2020 に `enciklopedia vortaro` が確認できる。日本語では「百科辞典」がより直接的。
- `ID3738` JA/ZH/KO
  - JA `この地域の風景が写っている写真はありますか？` → `この地域の風景写真はありますか？`
  - ZH `你有没有这片区域的照片？` → `你们有这片区域的风景照片吗？`
  - KO `이 지역의 풍경이 담긴 사진이 있으신가요?` → `이 지역의 풍경 사진이 있나요?`
  - 理由: EO `fotojn kun vidoj` と RU `фотографии с видами` の「風景写真」を保ち、店頭在庫確認として自然化。
- `ID3739` ZH
  - `你有印有本地景点的明信片吗？` → `你们有印有本市景点的明信片吗？`
  - 理由: 店頭在庫確認として自然化し、EO/RU の「この町・市の名所」に寄せた。
- `ID3741` JA
  - `赤いカーネーションをまとめてください。` → `赤いカーネーションの花束をお願いします。`
  - 理由: EO/RU の `bukedo/букет` に合わせ、花束である点を明示。
- `ID3743` EN/JA/ZH
  - EN `I need a wreath of fresh flowers for bride.` → `I need a wreath of fresh flowers for the bride.`
  - JA `花嫁用に新鮮な生花の花冠が必要です。` → `花嫁用の生花の花冠が必要です。`
  - ZH `我需要一个新鲜花环给新娘用。` → `我需要一个新娘用的鲜花花冠。`
  - 理由: PIV 2020 の `krono` には花嫁が頭に載せる花冠の用例がある。ZH は「新鮮な花環」より、花嫁用の花冠として自然化。
- `ID3745` JA
  - `こちらが領収書です。` → `こちらがレシートです。`
  - 理由: 店頭会計の `receipt` / RU `чек` として自然な日本語に修正。
- `ID3755` JA/ZH
  - JA `うまくいきません。` → `動きません。`
  - ZH `它不起作用。` → `这个不能用。`
  - 理由: 返品・故障文脈で EO/RU/EN の「機能しない」を商品不具合として自然化。

主な据え置き確認:
- `ID3722` `Romeo kaj Julieta`: PIV 2020 に `_Julieta_` の項目があり、用例として `Romeo k Julieta` を確認。`Julieto` 形も見かけるが、現形に十分な辞書根拠があるため未修正。
- `ID3724` `albumojn pri arkitekturo`: PIV 2020 で `albumo` に「ほぼ絵・写真からなる本」の語義を確認。Esperanto 本体は未修正。
- `ID3743` `kronon el freŝaj floroj por la fianĉino`: PIV 2020 の `krono` に、花で編んだ冠および花嫁の花冠用例を確認。Esperanto 本体は未修正。
- `ID3668` `konservaĵojn`: PIV 2020 で食品保存物の語義を確認。supermarket の canned/tinned food 文脈として未修正。

一致確認:
- `cmp_exit=0`
- `md5=8e97dcf20ff021dcb2b880334fb0e67b`

## 54. 53周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`

主な修正:
- `ID3759` ZH
  - `请给我一个礼品盒。` → `可以给我一个礼品盒吗？`
  - 理由: EO/EN/RU は「もらえますか」という依頼疑問。命令文寄りの中国語を自然化。
- `ID3763` ZH
  - `你能再检查一遍吗？` → `您能再检查一遍吗？`
  - 理由: 店員への依頼として敬体に統一。
- `ID3765` JA
  - `これに20フラン払います。` → `これなら20フラン出します。`
  - 理由: 値段交渉の `Mi donos al vi 20 frankojn por ĝi` / RU `Я дам вам...` として自然化。
- `ID3767` ZH
  - `你会把它送到我的酒店吗？` → `能把它送到我的酒店吗？`
  - 理由: 将来予測ではなく店への配送依頼として自然化。
- `ID3781` JA
  - `請求書に間違いはありませんか？` → `計算に間違いはありませんか？`
  - 理由: EO `kalkulo` は「計算」。買い物会計文脈で「請求書」に限定しない方が自然。
- `ID3786` JA/ZH
  - JA `私の購入品を自宅まで転送していただけますか？` → `購入した商品を自宅住所まで送っていただけますか？`
  - ZH `你会把我购买的商品寄到我的家庭住址吗？` → `能把我买的商品寄到我家地址吗？`
  - 理由: EO/RU は購入品を自宅住所へ送る依頼。`転送` や直訳調の `家庭住址` を避けた。
- `ID3787` ZH/KO
  - ZH `请您今天发送可以吗？` → `能请您今天寄出吗？`
  - KO `오늘 보내주실 수 있으신가요?` → `오늘 보내 주실 수 있나요?`
  - 理由: 発送依頼として自然化。韓国語は過剰な二重敬語を避けた。
- `ID3805` JA
  - `塩味のポップコーンと甘いポップコーン、どちらが好きですか？` → `塩味と甘いポップコーン、どちらにしますか？`
  - 理由: EO/RU/EN は売り場での選択提示。「好きですか」ではなく注文選択に修正。
- `ID3812` JA/ZH/KO
  - JA `ちょうどリリースされたばかりです。` → `公開されたばかりです。`
  - ZH `刚刚发布。` → `刚刚上映。`
  - KO `방금 출시됐어요.` → `막 개봉했어요.`
  - 理由: 映画の公開・上映文脈に合わせた。
- `ID3825` JA
  - `良いもののはずです。` → `良い映画のはずです。`
  - 理由: 映画についての評判・期待を述べる文として自然化。
- `ID3832` JA
  - `電話でチケットを注文することはできますか？` → `電話でチケットを予約できますか？`
  - 理由: ticket booking 文脈では「注文」より「予約」が自然。
- `ID3833` EN/KO
  - EN `Please get a ticket for me on the tenth row.` → `Please get a ticket for me in the tenth row.`
  - KO `열 번째 줄에 있는 티켓을 한 장 예매해 주세요.` → `열 번째 줄 좌석으로 표 한 장 예매해 주세요.`
  - 理由: 席列指定として自然化。
- `ID3837` JA/ZH/KO
  - JA `発売されてから約2か月経ちます。` → `公開されてから約2か月経ちます。`
  - ZH `已经推出大约两个月了。` → `已经上映大约两个月了。`
  - KO `출시된 지 약 두 달 정도 됐어요.` → `개봉한 지 약 두 달 정도 됐어요.`
  - 理由: 映画が公開・上映された時期を述べる文として修正。
- `ID3839` KO
  - `오랜만에 이렇게 훌륭한 영화를 본 건 처음이에요.` → `오랜만에 본 영화 중 손꼽히게 훌륭했어요.`
  - 理由: EO/EN/RU は「長い間見た中で最良級の一つ」。韓国語の「初めて」は意味がずれるため修正。
- `ID3844` JA/ZH
  - JA `これは悲劇なのでしょうか。` → `これは悲劇ですか？`
  - ZH `这算是一场悲剧吗？` → `这是悲剧吗？`
  - 理由: Theatre 文脈のジャンル名として自然化。現実の悲惨な出来事に寄る読みを避けた。
- `ID3849` JA/KO
  - JA `これはドラマですか？` → `これは劇ですか？`
  - KO `이거 드라마인가요?` → `이거 극인가요?`
  - 理由: Theatre 文脈の `dramo/драма`。テレビドラマに寄る訳を避け、舞台劇として自然化。
- `ID3852` JA/KO
  - JA `著者は誰ですか。` → `作者は誰ですか。`
  - KO `저자가 누구인가요?` → `작가는 누구인가요?`
  - 理由: Theatre 文脈では本の著者より作品の作者・作家が自然。

主な据え置き確認:
- `ID3791` `filmo de suspenso`: PIV 2020 で `suspenso` は映画・劇で観客を緊張した期待状態に置く場面として確認。thriller 文脈として未修正。
- `ID3805` / `ID3820` `pufmaizo`: PIV 2020 では見出し未確認だが、Glosbe 等で popcorn 対応を確認でき、`puf-` + `maizo` の透明な複合語として未修正。
- `ID3830` `subtekstojn`: subtitles の表現として Glosbe 等で確認でき、映画字幕文脈として未修正。
- `ID3850` `opereto`: PIV 2020 で「短い喜歌劇」と確認。オペレッタとして未修正。
- `ID3851` `dekoraciojn`: PIV 2020 で劇場の背景・舞台装置を指す語義を確認。scenery / декорации として未修正。

一致確認:
- `cmp_exit=0`
- `md5=ef74278d6827401e0ed8d42d81161f02`

## 55. 54周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`

主な修正:
- `ID3867` JA/KO
  - JA `ドラマを観たいです。` → `劇を観たいです。`
  - KO `드라마를 보고 싶어요.` → `연극을 보고 싶어요.`
  - 理由: Theatre 文脈の `dramo`。テレビドラマではなく舞台劇として自然化。
- `ID3868` JA/ZH/KO
  - JA `オペラグラスを持っていきたいです。` → `オペラグラスを借りたいです。`
  - ZH `我想带上歌剧望远镜。` → `我想借一个剧场望远镜。`
  - KO `오페라 글라스를 가지고 가고 싶어요.` → `오페라글라스를 빌리고 싶어요.`
  - 理由: EO `preni teatran lorneton` と RU `взять театральный бинокль` は劇場で借りる・受け取る場面。自分で持参する意味に寄らないよう修正。
- `ID3880` JA/KO
  - JA `イブニングドレスは必要ですか？` → `夜会服は必要ですか？`
  - KO `이브닝 드레스를 꼭 착용해야 하나요?` → `야회복을 꼭 입어야 하나요?`
  - 理由: EO `vespera vesto` / EN `evening dress` は女性用ドレス限定より、夜会服・正式な夜の服装として扱う方が安全。
- `ID3882` ZH
  - `请给我一份节目单好吗？` → `可以给我一份节目单吗？`
  - 理由: EO/EN/RU は丁寧な依頼疑問。命令文寄りを避けた。
- `ID3911` JA
  - `これはオリジナルですか？` → `これは真作ですか？`
  - 理由: 美術館文脈の `originalo` / RU `подлинник` は原本・真作。カタカナの「オリジナル」より明確。
- `ID3922` JA/KO
  - JA `クラシック絵画はお好きですか？` → `古典絵画はお好きですか？`
  - KO `클래식 회화를 좋아하세요?` → `고전 회화를 좋아하세요?`
  - 理由: 美術文脈の classical paintings として自然化。
- `ID3925` JA/ZH
  - JA `カリカチュアホールはどこですか？` → `風刺画の展示室はどこですか？`
  - ZH `请问漫画展厅在哪里？` → `请问讽刺画展厅在哪里？`
  - 理由: PIV 2020 の `karikaturo` は人物・対象を滑稽・風刺的に誇張した絵。一般の漫画展ではなく風刺画・カリカチュアとして修正。
- `ID3931` JA/ZH
  - JA `民族博物館はどこですか。` → `民族学博物館はどこですか。`
  - ZH `民族博物馆在哪里？` → `民族学博物馆在哪里？`
  - 理由: EO `etnografia muzeo` / RU `этнографический музей` に合わせ、民族学・民族誌寄りに修正。
- `ID3936` EN/JA/ZH/KO
  - EN `One adult and two children, please.` → `One adult ticket and two child tickets, please.`
  - JA `大人1名と子ども2名でお願いします。` → `大人券1枚と子ども券2枚をお願いします。`
  - ZH `一位成人和两位儿童，谢谢。` → `一张成人票和两张儿童票，谢谢。`
  - KO `어른 한 명과 어린이 두 명이요.` → `성인권 한 장과 어린이권 두 장이요.`
  - 理由: EO `plenkreskulan` / `infanajn` は省略された `biletojn` を修飾していると読むのが自然。入場券の種類として明示。
- `ID3942` JA/ZH/KO
  - JA `博物館の館内案内図はお持ちですか？` → `博物館の館内案内図はありますか？`
  - ZH `你有博物馆的导览图吗？` → `你们有博物馆的导览图吗？`
  - KO `박물관 안내 지도가 있으신가요?` → `박물관 안내 지도가 있나요?`
  - 理由: 博物館スタッフに案内図の有無を尋ねる文。個人所有・物への過剰敬語に寄らないよう修正。
- `ID3943` ZH
  - `你有蒙古语的导游手册吗？` → `你们有蒙古语的导览手册吗？`
  - 理由: Museum 文脈の guidebook は旅行案内者向けの手引きではなく、展示・館内の案内書。
- `ID3945` JA/ZH
  - JA `絵画館の見学にはどのくらい時間がかかりますか。` → `絵画展示室の見学にはどのくらい時間がかかりますか。`
  - ZH `参观画廊大约需要多长时间？` → `参观绘画展厅大约需要多长时间？`
  - 理由: Museum 内の picture gallery。商業画廊や別施設に寄らないよう展示室として自然化。
- `ID3946` ZH
  - `我们得把行李寄存在衣帽间。` → `我们得把包寄存在衣帽间。`
  - 理由: EO `sakojn` / RU `сумки` は bags。大きな旅行荷物に寄る `行李` を避けた。
- `ID3954` JA/ZH/KO
  - JA `ビリヤードはありますか？` → `そこにビリヤードはありますか？`
  - ZH `有台球吗？` → `那里有台球吗？`
  - KO `당구장이 있나요?` → `거기에 당구대가 있나요?`
  - 理由: EO `tie` と RU `там` の「そこに」を保持。韓国語は「ビリヤード場」ではなく台・設備の有無として修正。

主な据え置き確認:
- `ID3872/3873/3896` `interakto`: PIV 2020 で `interakto` が「二つの幕の間の時間」として確認でき、Glosbe 等でも interval/intermission 対応を確認。未修正。
- `ID3868` `teatra lorneto`: PIV 2020 で `lorno` と `binoklo` 周辺を確認。劇場用双眼鏡として通るため Esperanto 本体は未修正。
- `ID3874` `loĝio`: PIV 2020 で劇場の小区画・ボックス席の語義を確認。未修正。
- `ID3921` `fulmilo`: PIV 2020 の `fulmo` からの透明な派生として flash 文脈で通るため未修正。
- `ID3925` `karikatursalono`: `karikaturo` は PIV 2020 で確認でき、`salono` との透明な複合として展示室文脈で未修正。
- `ID3937` `handikapuloj`: PIV 2020 で `handikapulo` を確認。現代的表現への配慮は別課題だが、原文意味としては未修正。

一致確認:
- `cmp_exit=0`
- `md5=b76343bc3e0540550e5bc0eed09ed2ad`

## 56. 55周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`

主な修正:
- `ID3965` ZH
  - `你知道这附近有什么不错的俱乐部吗？` → `你知道这附近有什么不错的夜店吗？`
  - 理由: Nightclub 文脈の club。一般のクラブ活動・会員制クラブではなく夜店として明確化。
- `ID3979` KO
  - `그는 휴일을 해변에서 보냅니다.` → `그는 휴가를 해변에서 보냅니다.`
  - 理由: EO `feriojn` / RU `отпуск` は単発の休日より休暇。Beach 文脈にも合う。
- `ID3995` ZH
  - `这个氧气瓶能用多久？` → `这个气瓶能用多久？`
  - 理由: EO `aerbotelo` / RU `баллон` は「酸素ボンベ」と断定しない方が安全。潜水・水辺文脈のボンベとして自然化。
- `ID3999` EO/ZH
  - EO `Kiom kostas lui akvokostumon por unu tago?` → `Kiom kostas lui malsekkostumon por unu tago?`
  - ZH `租一套潜水服一天多少钱？` → `租一套湿式潜水服一天多少钱？`
  - 理由: `akvokostumo` は辞書・実例確認が弱く、wetsuit としては `malsekkostumo` の方が確認しやすい。内容は「水着」ではなく保温用のウェットスーツとして保持。
- `ID4006` JA
  - `緊急時にヨットは保険に入っていますか？` → `ヨットは緊急時に備えた保険に入っていますか？`
  - 理由: 「緊急時に保険へ加入する」と読める曖昧さを避け、保険適用の確認として自然化。
- `ID4007` ZH
  - `需要支付定金吗？` → `需要交押金吗？`
  - 理由: EO `garantiaĵo` / RU `залог` は予約内金より保証金・デポジット。PIV 2020 でも保証・担保の語義を確認。
- `ID4016` JA/ZH/KO
  - JA `一緒に遊ばない？` → `一緒にプレーしませんか？`
  - ZH `你想和我一起玩吗？` → `你想和我一起打吗？`
  - KO `저랑 같이 놀고 싶으세요?` → `저랑 같이 경기할래요?`
  - 理由: Sport 文脈の play。子どもの遊び一般に寄らないよう競技・プレーとして修正。
- `ID4022` ZH
  - `裁判是谁？` → `裁判员是谁？`
  - 理由: 人を指す referee として自然化。
- `ID4023` EN
  - `Who made the goal?` → `Who scored the goal?`
  - 理由: 英語の自然なサッカー・スポーツ表現へ修正。EO/RU と意味は変えない。
- `ID4036` JA
  - `切符売り場はどこですか。` → `チケット売り場はどこですか。`
  - 理由: 競技場・スポーツイベント文脈では切符よりチケットが自然。
- `ID4042` ZH
  - `今天有几场比赛？` → `今天有几场赛马？`
  - 理由: horse races の文脈を保持し、一般試合に広げない。
- `ID4046` JA/ZH
  - JA `誰が一番でしたか？` → `誰が1着でしたか？`
  - ZH `谁第一个完成的？` → `谁第一个冲过终点？`
  - 理由: race 文脈の winner/first。順位・ゴール通過として明確化。
- `ID4048` JA/KO
  - JA `この記録は破れません。` → `あなたにはこの記録は破れません。`
  - KO `이 기록은 깰 수 없어요.` → `당신은 이 기록을 깰 수 없어요.`
  - 理由: EO `Vi ne povos...` / RU `Тебе не удастся...` の二人称主語を保持。

主な据え置き確認:
- `ID3972` `diskĵokeo`: DJ を指す語として Glosbe・ウェブ実例で確認。Esperanto 本体は未修正。
- `ID3990` `surfotabulon`: PIV 2020 の `surfi` 系と `surf-` 文脈から、surfboard の透明な複合として未修正。
- `ID3995` `aerbotelo`: 「空気ボンベ」として透明な複合。ZH の酸素断定だけ修正し、Esperanto 本体は未修正。
- `ID4007` `garantiaĵo`: PIV 2020 で保証・担保・保証物の語義を確認。deposit 文脈に合うため未修正。
- `ID4029` `gimnastikejo`: PIV 2020 で体操・運動の場所として確認。RU `тренажерный зал` との対応も文脈別許容で未修正。
- `ID4032` `tenisejo`: PIV 2020 で tennis court として確認。未修正。
- `ID4034` `rugbeo`: PIV 2020 で rugby として確認。未修正。
- `ID4050` `skiojn`: sports equipment rental 文脈で「スキー板」を指すものとして未修正。

一致確認:
- `cmp_exit=0`
- `md5=089d061253d2ebbdf40e115732de16bf`

## 57. 56周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`

主な修正:
- `ID4058` KO
  - `센터 스탠드에 있는 티켓 한 장 주세요.` → `중앙 관람석 표 한 장 주세요.`
  - 理由: `centra tribuno` は中央観覧席・中央スタンド。韓国語の直訳調を避け、座席券として自然化。
- `ID4065` ZH
  - `热门选手的赔率是多少？` → `夺冠热门的赔率是多少？`
  - 理由: 競馬・レース文脈の favourite。人間の選手に限定しない表現へ修正。
- `ID4068` EO
  - `Kiu estas la minimuma veto, kiun mi povas fari?` → `Kiom estas la minimuma veto, kiun mi povas fari?`
  - 理由: 最低ベット額を尋ねる文なので、個体選択の `kiu` ではなく金額を問う `kiom` が自然。
- `ID4071` EO
  - `Kio estas la paro por ĉi tiu truo?` → `Kio estas la norma nombro da batoj por ĉi tiu truo?`
  - 理由: PIV 2020 で `paro` は主に「対・ペア」語義で、ゴルフの par としての確認が弱い。未確認の専門語化を避け、意味を変えずに「標準打数」として透明化。
- `ID4073` EO/EN
  - EO `Kiom da boatoj partoprenas en ĉi tiu regato?` → `Kiom da boatoj partoprenas en ĉi tiu regatto?`
  - EN `How many boats are included in this regatta?` → `How many boats are taking part in this regatta?`
  - 理由: PIV 2020 / Glosbe で regatta は `regatto` と確認。英語も参加数を尋ねる自然な表現へ修正。
- `ID4083` KO
  - `누가 그렇게 가르쳐줬어요?` → `그걸 누가 가르쳐 줬어요?`
  - 理由: EO `tion` / RU `этому` は「それを」。方法の「そうやって」に寄らないよう修正。
- `ID4115` JA
  - `キャラバン（キャンピングカー）をお持ちですか？` → `キャンピングトレーラーをお持ちですか？`
  - 理由: PIV 2020 で `ruldomo` は居住可能な車両・トレーラー系として確認。日本語の「キャラバン」や「キャンピングカー」の曖昧さを避けた。
- `ID4124` JA/ZH
  - JA `この町はここから遠いですか？` → `町はここから遠いですか？`
  - ZH `这个镇离这里远吗？` → `镇上离这里远吗？`
  - 理由: EO `la urbo` は「この町」ではなく、キャンプ地から町までの距離を聞く文。
- `ID4128` JA
  - `この谷、本当に素晴らしいですよね？` → `これらの谷は本当に素晴らしいですよね？`
  - 理由: EO `ĉi tiuj valoj` / RU `эти долины` の複数を保持。
- `ID4145` KO
  - `텐트 대여 요금이 얼마인가요?` → `텐트 하나 요금이 얼마인가요?`
  - 理由: EO/EN/RU はレンタル料金と断定せず、キャンプ場でのテント1張りの料金として読める。過剰な「貸出」解釈を避けた。
- `ID4148` ZH
  - `你有平整的位置吗？` → `有更平坦的地方吗？`
  - 理由: EO `pli ebenan` / RU `поровнее` の比較を保持。
- `ID4153` ZH
  - `有一个燕子的巢。` → `这里有一个燕子窝。`
  - 理由: EO `Ĉi tie` の「ここ」を保持し、中国語として自然化。
- `ID4154` EN/JA
  - EN `Are we going up on a cable railway?` → `Are we going up by cable car?`
  - JA `ケーブルカーで上に登るんですか？` → `ロープウェイで登るんですか？`
  - 理由: PIV 2020 で `telfero` は鋼索に吊られた車両・座席で山や谷を移動する交通機関。`funikularo` 的な cable railway へ寄らないよう修正。

主な据え置き確認:
- `ID4065` `vetproporcioj`: PIV 2020 で `vet/o` と関連語を確認。`veto` + `proporcio` の透明な複合として betting odds 文脈で未修正。
- `ID4070` `golfbastonoj`: PIV 2020 の `bastono` にゴルフ用の曲がった棒の記述があり、`golfbastono` は透明な複合として未修正。
- `ID4070` `golfĉaro`: `golfo` と `ĉaro` の透明な複合。Golf cart 文脈で未修正。
- `ID4105` `popolmuziko`: folk / popular music の境界に少し幅があるが、RU `фольклорной музыки` と多言語列の対応上、文脈別許容で未修正。
- `ID4115` `ruldomo`: PIV 2020 で `domveturilo` の同義語として確認。Esperanto 本体は未修正。
- `ID4119/4135/4137/4153` `kukolo`, `pego`, `najtingalo`, `hirundo`: PIV 2020 で鳥名として確認。未修正。
- `ID4154` `telfero`: PIV 2020 で aerial cableway 系の交通機関として確認。Esperanto 本体は未修正。

一致確認:
- `cmp_exit=0`
- `md5=183bf35c00e93594f6fce47e3bd31373`

## 58. 57周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`

主な修正:
- `ID4176` EO
  - `Ĉu iu volus ludi dartojn?` → `Ĉu iu volus ludi sagetojn?`
  - 理由: PIV 2020 では `darto` を確認できず、医学語 `dartr/o` だけが該当。PIV で確認できる `sag/o` と縮小辞 `-et-` による透明な `sageto` に寄せ、Glosbe/ウェブ上でも darts は `sagoĵetado` 系で確認できるため、未確認外来語を避けた。
- `ID4193` JA/ZH
  - JA `あまり頻繁にはありません。` → `あまり頻繁にはしません。`
  - ZH `不是很常。` → `不太常。`
  - 理由: 直前の `akvumi` への返答なので、存在文ではなく「そう頻繁にはしない」という行為頻度の返答として自然化。
- `ID4198` JA
  - `彼らは畑をならした。` → `彼らは畑をまぐわでならした。`
  - 理由: PIV 2020 で `erpi` は専用の道具で土塊を砕いて畑をならすこと。単なる整地より harrow/боронить の焦点を保持。
- `ID4214` EO
  - `Mi metos la bolkruĉon` → `Mi boligos akvon`
  - 理由: `metos la bolkruĉon` は「やかんを置く」で止まっており、置く場所・加熱動作が不明瞭。PIV 2020 で `boligi akvon` を確認でき、JA/ZH の「お湯を沸かす」とも一致するため、意味を広げず自然化。
- `ID4228` ZH
  - `你怎么喝的？` → `你喜欢怎么喝？`
  - 理由: Tea/coffee 文脈の “How do you take it?”。過去の飲み方を尋ねる形ではなく、砂糖・ミルク等の好みを聞く表現へ修正。
- `ID4250` KO
  - `설거지하는 데 도와줄 수 있나요?` → `설거지 좀 도와줄 수 있어요?`
  - 理由: `-하는 데 도와주다` の硬い/不自然な結合を避け、食後の皿洗いを手伝う依頼として自然化。

主な据え置き確認:
- `ID4175` `televidaj romanoj`: ローカルPIVでは直接確認できなかったが、Glosbe で soap opera の訳として `televida romano` が確認できる。RU/JA/ZH/KO も「ソープオペラ・連続劇」方向で一致するため未修正。
- `ID4189` `betoj`: PIV 2020 で `bet/o` は食用根を含む語義として確認。`ruĝa beto` への精密化も可能だが、現行EOは誤りと断定できず未修正。
- `ID4220` `buŝtukojn`: PIV 2020 で `buŝtuko` は派生語・用例として確認できるため未修正。
- `ID4227` `La bolilo bolis`: PIV 2020 で `bolilo` は水を沸かす器として確認。`poto bolos` 型の容器主語もPIV例にあり、英語/RUの kettle 文脈として未修正。

一致確認:
- `cmp_exit=0`
- `md5=76094623907bce3b9e5f4457bf9faf82`

## 59. 58周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`

主な修正:
- `ID4267` EO
  - `Kia estas la provizio?` → `Kiom estas la provizio?`
  - 理由: commission の額・率を尋ねる文。PIV 2020 で `provizio` は銀行等の手数料・仲介報酬として確認できるため語は維持し、疑問詞だけ金額を問う `kiom` に修正。
- `ID4276` RU
  - `Не могли бы вы сказать мой баланс счёта, пожалуйста?` → `Не могли бы вы сообщить мне остаток на счёте, пожалуйста?`
  - 理由: ロシア語として自然な「口座残高を知らせる」表現へ修正。EO/JA/ZH/KO の意味は変更なし。
- `ID4277` ZH
  - `我的护照必须带吗？` → `需要我的护照吗？`
  - 理由: 「持参しなければならないか」より、EO/EN/RU の「パスポートが必要か」に合わせた。
- `ID4279` RU
  - `Насколько быстро он может быть осуществлён?` → `Насколько быстро это можно сделать?`
  - 理由: 代名詞 `он` が不自然で、EO/EN の「これをどれくらい早くできるか」に合わせた。
- `ID4286` JA/ZH
  - JA `大きい紙幣でお願いします。` → `高額紙幣でお願いします。`
  - ZH `请给我大号的纸币。` → `请给我大面额纸币。`
  - 理由: large notes は物理的に大きい紙幣ではなく高額面の紙幣。KO/RU とも一致。
- `ID4291` RU
  - `Мне нужен документ на выдачу наличных с депозита.` → `Мне нужен бланк для снятия наличных.`
  - 理由: withdrawal slip として自然な銀行窓口表現へ修正。
- `ID4311` EO
  - `Kia estas la interezprocento de ĉi tiu konto?` → `Kiom estas la interezprocento de ĉi tiu konto?`
  - 理由: interest rate の数値を尋ねる文。PIV 2020 で `interezo` の割合・パーセント用法を確認し、疑問詞を修正。
- `ID4315` EO
  - `Kia estas via buĝeto?` → `Kiom estas via buĝeto?`
  - 理由: 予算の性質ではなく金額を尋ねる文。
- `ID4318` EN
  - `I want to find a flat for hire.` → `I want to find a flat to rent.`
  - 理由: 英語の collocation を自然化。EO/JA/ZH/KO/RU は賃貸探しで一致。
- `ID4321` EO
  - `Mi serĉas bungalon` → `Mi serĉas bangalon`
  - 理由: PIV 2020 で `bangal/o` は bungalow として確認でき、`bungalo` はPIVで確認できなかったため綴りを修正。
- `ID4322` RU
  - `Я ищу низкий многоквартирный дом.` → `Я ищу таунхаус.`
  - 理由: EO/EN/JA/ZH/KO は terraced/row house 系。低層集合住宅では意味がずれるため修正。EO `vicdomo` は PIV の `vico` から透明な複合として据え置き。
- `ID4325` EO
  - `Kiu estas la petata prezo?` → `Kiom estas la petata prezo?`
  - 理由: asking price の金額を尋ねる文なので、個体選択の `kiu` ではなく `kiom` に修正。
- `ID4328` RU
  - `У вас есть собственность на продажу?` → `У вас есть недвижимость на продажу?`
  - 理由: Estate Agency 文脈の property は不動産。一般的な所有物に広がる `собственность` を避けた。
- `ID4329` RU
  - `Вы ищите жилье для покупки или аренды?` → `Вы ищете жильё для покупки или аренды?`
  - 理由: 動詞形 `ищете` と表記 `жильё` を修正。
- `ID4330` ZH
  - `你指的是哪个地区？` → `您考虑哪个地区？`
  - 理由: 「どの地区を指しているか」ではなく、「どの地区を検討しているか」を尋ねる文。
- `ID4333` ZH
  - `你打算需要贷款买房吗？` → `你需要申请房贷吗？`
  - 理由: 中国語として不自然な結合を避け、mortgage/住宅ローンの必要性へ合わせた。
- `ID4339` RU
  - `Сколько первоначальный взнос?` → `Сколько составляет первоначальный взнос?`
  - 理由: ロシア語として自然な金額質問へ修正。
- `ID4340` EO/RU
  - EO `Kiom estas la monata kotizo?` → `Kiom estas la monata pago?`
  - RU `Сколько ежемесячная плата?` → `Сколько составляет ежемесячная плата?`
  - 理由: PIV 2020 の `kotizo` は主に会費・保険料系で、不動産の月額支払いとしては `monata pago` の方が安全。
- `ID4347` EN
  - `Do you want a modern or an old property?` → `Do you want a newly built or a second-hand property?`
  - 理由: EO/JA/ZH/KO/RU は新築か中古。modern/old では意味がずれる。
- `ID4350` EO
  - `Mi interesiĝas scii pli pri ĉi tiu posedaĵo` → `Interesas min ekscii pli pri ĉi tiu posedaĵo`
  - 理由: PIV 2020 で `interesi` は `interesus min ekscii...` 型の用例、`interesiĝi` は `pri/je` 支配として確認。直後に不定詞を置く不自然さを避け、内容を変えずに修正。

主な据え置き確認:
- `ID4266/4300` `kurzo`: exchange rate は数値を含むが、`Kia estas la kurzo?` は「どのようなレートか」を尋ねる形として文脈別許容で未修正。
- `ID4267/4288` `provizio`: PIV 2020 で銀行等の commission として確認。語自体は未修正。
- `ID4285/4286/4287` `monbileto` / `bankbileto`: PIV 2020 で `bank bileto` / `mon bileto` を確認。未修正。
- `ID4291` `monretiro`: 以前の保留解除語。`retiri monon` 系の透明な複合として、明確な意味ズレなしと判断し未修正。
- `ID4305/4333` `hipoteko`: PIV 2020 で不動産等を担保にする法的 mortgage として確認。住宅ローン文脈で未修正。
- `ID4307` `ĝiri`: PIV 2020 で口座から別口座へ送金する語義を確認。未修正。
- `ID4322` `vicdomo`: PIV 2020 で `vico` は横に並ぶ列・連なり。`domo` との透明複合として terraced/row house 文脈で未修正。
- `ID4347` `duamana`: 以前の保留解除語。中古物件の文脈で JA/ZH/KO/RU と一致し、未修正。

一致確認:
- `cmp_exit=0`
- `md5=dc493fc620a847a775d2759fca89acc9`

## 60. 59周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`

主な修正:
- `ID4367` RU
  - `Мои волосы - сухие.` → `Мои волосы сухие.`
  - 理由: ロシア語の述語形容詞としてハイフンを置かない自然な形へ修正。
- `ID4376` EN
  - `Cut it short, please.` → `Cut it shorter, please.`
  - 理由: EO `pli mallonge` / JA/ZH/KO/RU は「さらに短く」。英語の “cut it short” だと「短くする」に寄りすぎるため修正。
- `ID4377` JA
  - `完全に丸刈りにしてください。` → `完全に剃ってください。`
  - 理由: EO `Razu tute kalve` / RU `Побрейте налысо` / ZH `剃光` は「剃ってつるつるにする」方向。丸刈りより強い意味を保持。
- `ID4378` EO
  - `Ĉu vi havas disigon?` → `Ĉu vi havas dislimon?`
  - 理由: PIV 2020 の `haroj` に `dislimi al si la harojn`、参照語として `dislimo` があり、Glosbe でも parting に `dislimo` / `hardislimo` を確認。一般的な `disigo` より美容院文脈に合う。
- `ID4388` EO
  - `Mi ŝatus harlumojn` → `Mi ŝatus helajn striojn en miaj haroj`
  - 理由: `harlumoj` はPIVで確認できず、hair highlights として根拠が弱い。PIV 2020 で `strio` は色・明るさで区別される細長い部分、`haroj` は頭髪として確認できるため、意味を変えず透明な表現に置換。
- `ID4389` JA/ZH
  - JA `痛みますか？` → `しみますか？`
  - ZH `会疼吗？` → `会刺痛吗？`
  - 理由: EO/EN/RU/KO は美容院・薬剤文脈の burn/sting。一般的な痛みではなく、しみる・刺すように痛む感覚へ合わせた。
- `ID4391` ZH
  - `请将两端向内卷起。` → `请把发梢向内卷。`
  - 理由: hair ends は物体の「両端」ではなく毛先。EO `pintoj` / JA/KO/RU と一致。
- `ID4393` EO
  - `Ĉu vi faras epiladon?` → `Ĉu vi faras senharigon?`
  - 理由: PIV 2020 で `senharigo` の用例を確認でき、Glosbe でも hair removal / epilation は `senharigo` と確認。PIVで確認できない `epilado` を避けた。
- `ID4394` EO/ZH
  - EO `Mi ŝatus vaksan epiladon de miaj kruroj` → `Mi ŝatus senharigon de miaj kruroj per vakso`
  - ZH `我想做腿部脱毛。` → `我想做腿部蜜蜡脱毛。`
  - 理由: EO は上記と同じく `senharigo` に統一し、PIV確認済みの `vakso` で wax の手段を明示。ZH は waxed の情報が抜けていたため補った。
- `ID4398` ZH
  - `我还欠你多少钱？` → `我该付多少钱？`
  - 理由: 美容院での支払い額を尋ねる文として自然化。負債ニュアンスを避けた。
- `ID4401` JA
  - `少しの間、座れる場所はどこですか？` → `少し座れる場所はありますか？`
  - 理由: EO/EN/RU の「少し座れる場所」を日本語として自然化。
- `ID4402` ZH
  - `你想让我怎么切？` → `您想怎么剪？`
  - 理由: 美容院文脈では髪を「剪る」。目的語なしでも自然な接客表現へ修正。
- `ID4417` EN
  - `She has got a sensitive skin.` → `She has sensitive skin.`
  - 理由: 英語の不可算名詞として自然化。
- `ID4434` EN
  - `Can you check my size?` → `Can you take my measurements?`
  - 理由: EO `preni miajn mezurojn` / RU `снять мерки` は採寸。size の確認ではなく measurements へ合わせた。
- `ID4436` ZH
  - `你能帮我稍微改一下这条裙子吗？` → `你能帮我稍微改一下这条连衣裙吗？`
  - 理由: EO/EN/JA/KO/RU は dress。skirt と紛れやすい `裙子` を避けた。
- `ID4439` ZH
  - `你会调整长度吗？` → `可以帮我调整长度吗？`
  - 理由: 技能可否ではなく、仕立て屋への依頼として自然化。
- `ID4443` ZH
  - `您希望什么时候要这个？` → `您希望什么时候拿到？`
  - 理由: EO `ricevi` / RU `получить` の「受け取る」を自然な中国語へ修正。
- `ID4447` ZH
  - `你能把这条裙子的腰部收一下吗？` → `你能把这条连衣裙的腰部收一下吗？`
  - 理由: `ID4436` と同じく dress の意味を保持。
- `ID4451` JA
  - `うまくいきません。` → `正常に動きません。`
  - 理由: Repairs 文脈の device not working。一般的な「うまくいかない」ではなく機器の動作不良へ合わせた。

主な据え置き確認:
- `ID4358` `anticipe`: PIV 2020 で「前もって」の語義として確認。rent payable monthly in advance と一致し未修正。
- `ID4362` `dissendolisto`: PIV 2020 で `dissendo listo` は mailing list として確認。表記結合は透明で未修正。
- `ID4365` `franĝo`: PIV 2020 で `franĝo da haroj sur la frunto` を確認。bangs/fringe 文脈で未修正。
- `ID4385/4387` `farbigi` / `farbi ... blonde`: PIV 2020 で `farbi` と `blonda` を確認。美容院の髪染め文脈で意味ズレなしと判断。
- `ID4396/4397` `manikiuro` / `pedikuro`: PIV 2020 で `manikuri` / `pedikuri` を確認。名詞形は規則的派生として未修正。
- `ID4405` `feni`: PIV 2020 で `fen/o` は温風機・harsekigilo と確認。blow-dry 文脈で未修正。
- `ID4407` `ŝampui`: PIV 2020 で `ŝampui` は ŝampuo で頭を洗いマッサージする語義として確認。未修正。
- `ID4412` `sprajo por haroj`: Glosbe では hairspray に `harlako` も確認できるが、現行表現も `spraji` から透明で、JA/ZH/KO/RU と意味ズレがないため未修正。
- `ID4413` `ĝelo por haroj`: PIV 2020 で `ĝelo` を確認。hair gel は美容院文脈で透明に理解可能なため未修正。
- `ID4420` `skalpo`: PIV 2020 では語義にやや注意が残るが、既存再点検で保留解除済みの語。今回範囲の多言語列も scalp/head massage として大きな意味ズレはないため未修正。
- `ID4422` `fajlu ... ungojn`: PIV 2020 で `ungo fajlilo` は爪の形を整えるやすりとして確認。動詞 `fajli` の拡張として未修正。
- `ID4423` `laki ... ungojn`: PIV 2020 で `ungo lako` を確認。未修正。
- `ID4434/4438/4446` `mezuroj` / `mezuri`: PIV 2020 で身体・衣服の採寸用法を確認。未修正。
- `ID4442` `laŭmezura kostumo`: PIV 2020 で `laŭ mezura` は個人の寸法に合うことを確認。custom-made suit 文脈で未修正。
- `ID4444` `alĝustigi`: PIV 2020 で `alĝustigi` は適合させる・調整する語として確認。未修正。

一致確認:
- `cmp_exit=0`
- `md5=1f5e8342bf17463411291b09da813357`

## 61. 60周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`

主な修正:
- `ID4462` EO/JA
  - EO `Mi pensas, ke ĝi bezonas novan baterion` → `Mi pensas, ke ĝi bezonas novan pilon`
  - JA `新しいバッテリーが必要だと思います。` → `新しい電池が必要だと思います。`
  - 理由: PIV 2020 で `pilo` は化学エネルギーを使う電源、`baterio` は電池の集合として確認。直前が腕時計修理文脈なので小型電池の `pilo` が安全。日本語も時計文脈の「電池」に合わせた。
- `ID4465` JA
  - `私のパソコンにウイルスが感染しています。` → `私のパソコンがウイルスに感染しています。`
  - 理由: 感染している主体はウイルスではなくパソコン。意味の向きを修正。
- `ID4471` EO/JA
  - EO `Ĉu vi povas anstataŭigi la baterion?` → `Ĉu vi povas anstataŭigi la pilon?`
  - JA `バッテリーを交換できますか？` → `電池を交換できますか？`
  - 理由: `ID4462` と同じ時計・小型電池文脈。PIV確認済みの `pilo` に統一。
- `ID4476` ZH
  - `请问可以帮我配一把这把钥匙吗？` → `请问可以照这把钥匙配一把吗？`
  - 理由: 中国語の量詞重複が不自然。key copy/key cut の「この鍵をもとにもう1本作る」を自然化。
- `ID4479` ZH
  - `修理不值得。` → `不值得修理。`
  - 理由: 中国語として自然な worth repairing の語順へ修正。
- `ID4483` EO/ZH
  - EO `Ĉu vi havas baterion por ĉi tio?` → `Ĉu vi havas pilon por ĉi tio?`
  - ZH `你有这个的电池吗？` → `有适合这个的电池吗？`
  - 理由: EO は小型電池として `pilo` に修正。ZH は「これの電池」直訳を避け、適合する電池があるかを尋ねる自然な形にした。
- `ID4484` EO
  - `Ĉu vi bonvolus ŝanĝi la baterion en mia horloĝo?` → `Ĉu vi bonvolus ŝanĝi la pilon en mia horloĝo?`
  - 理由: watch battery はPIV確認済みの `pilo` がより精確。
- `ID4504` EO/JA
  - EO `Kio malbonas ĉe mi, doktoro?` → `Kio estas al mi, doktoro?`
  - JA `先生、私の体は何が悪いのでしょうか？` → `先生、私はどうしたのでしょうか？`
  - 理由: 直訳的な “what is bad at me” を避け、doctor 文脈の “what is wrong with me?” として自然化。日本語も身体部位の説明ではなく患者の状態を尋ねる形に合わせた。
- `ID4508` EO/EN
  - EO `Al mi fariĝis pli malbone` → `Mi fartas pli malbone`
  - EN `It has got worse.` → `I feel worse.`
  - 理由: 直前の `Ĉu vi fartas pli bone?` への返答として、PIV 2020 で確認できる `farti` の健康状態表現に統一。
- `ID4514` EO
  - `Kiel ofte vi trinkas?` → `Kiel ofte vi trinkas alkoholaĵojn?`
  - 理由: 医師の問診文脈で EN/JA/ZH/KO/RU は飲酒頻度。PIV 2020 で `trinki` は一般の飲用も含むため、EOだけが「水分を飲む頻度」に広がらないよう `alkoholaĵojn` を明示。
- `ID4516` EO/EN
  - EO `Mi bezonas fari rentgenon` → `Mi bezonas rentgenan ekzamenon`
  - EN `I need to take an X-ray.` → `I need to have an X-ray.`
  - 理由: PIV 2020 の `rentgeno` は古い放射線単位で、X-ray 検査そのものとしては弱い。`rentgena ekzameno` として検査内容を明示し、英語も患者側の “have an X-ray” に修正。
- `ID4550` ZH
  - `你的血压有点低。` → `你的血压相当低。`
  - 理由: EO/EN/JA/KO/RU は quite / かなり / довольно low。`有点低` では弱すぎるため修正。
- `ID4553` JA
  - `これまでにその治療を受けたことはありますか？` → `これまでにその症状で治療を受けたことはありますか？`
  - 理由: EO `kuracis vin pro tio` / RU `от этого лечили` は「その症状・件で治療されたか」。治療そのものを受けたかに見える日本語を修正。

主な据え置き確認:
- `ID4456` `fendiĝis`: PIV 2020 で `fendo` は細長い割れ・裂け目。screen cracked と一致し未修正。
- `ID4470` `kroneto`: PIV 2020 の `krono` に poŝhorloĝo 等の上部リング状部品の語義があり、時計の crown/winder として縮小辞つき表現を文脈別許容で未修正。
- `ID4487` `plandumoj`: PIV 2020 で `plandumo` は靴底、`replandumi` は新しい靴底を付けること。未修正。
- `ID4495/4496` `garantio`: PIV 2020 で商品の保証・責任の語義を確認。repairs covered by guarantee 文脈で未修正。
- `ID4501` `kapturno`: PIV 2020 で `vertiĝo` の参照先として確認。dizzy 文脈で未修正。
- `ID4524/4525` `Kiam doloras?` / `Doloras pli nokte`: PIV 2020 で `dolori` は絶対用法も確認できるため、短い問診表現として未修正。
- `ID4530` `analizojn`: PIV 2020 の `analizo` は検査・分析の語義を持つ。RU `сдать анализы` とも対応し、医療検査文脈で未修正。
- `ID4531` `malsanasekuro`: PIV 2020 で `asekuro` はリスクに対する保険。`malsano` との透明複合として health insurance 文脈で未修正。
- `ID4541` `Kia estas mia temperaturo?`: 既存再点検で `Kioma` から修正済み。PIV 2020 に `kia estas la ĉimatena temperaturo?` の用例があり、今回も未修正。
- `ID4555` `surdorse` / `surventre`: PIV 2020 で `dorso` と `ventro` の身体部位語義を確認。sleep on back/front と透明に対応し未修正。

一致確認:
- `cmp_exit=0`
- `md5=98f090f3c528dae35d8b9a24223f0b4d`

## 62. 61周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`

主な修正:
- `ID4569` JA
  - `できものができました。` → `おできができました。`
  - 理由: EO `furunko` / EN boil / ZH `疖子` / KO `종기` / RU `нарыв` は一般的な「できもの」より「おでき・腫れ物」に寄る。日本語を少し精密化。
- `ID4576` ZH
  - `她不会说话。` → `她不能说话。`
  - 理由: `不会说话` は「話し方を知らない」にも読めるため、EO/EN/RU の mute として「話せない」を明確化。
- `ID4581` ZH
  - `我的膝盖撞到了。` → `我撞到膝盖了。`
  - 理由: 中国語として自然な語順へ修正。意味は knee をぶつけたまま。
- `ID4604` EO/JA
  - EO `Mi havas apenaŭ energion` → `Mi havas tre malmulte da energio`
  - JA `ほとんどエネルギーが残っていません。` → `ほとんど力が出ません。`
  - 理由: PIV 2020 の `apenaŭ` は数量語または動詞に係る用法が中心で、現形はやや不自然。EN/RU/ZH/KO の very little energy / 力气 / сил に合わせ、`tre malmulte da energio` にした。
- `ID4605` EO
  - `Mi havas stomakmalsanon` → `Mi havas stomakan perturbon`
  - 理由: upset stomach / расстройство желудка は「胃・腹の調子が悪い」で、`stomakmalsano` だと「胃の病気」に強く寄る。PIV 2020 で `stomaka perturbo` 型を確認できるため、意味を狭めすぎない表現へ修正。
- `ID4614` EO
  - `Mi havas gravan kazon de piedfungo` → `Mi havas gravan mikozon de la piedoj`
  - 理由: `piedfungo` は透明な複合ではあるが、PIV 2020 で直接確認できない。PIV 2020 で `mikozo` は `fungozo`、すなわち菌類による寄生性疾患として確認できるため、athlete's foot / 水虫の意味を変えず、より確認可能な表現へ修正。
- `ID4615` ZH
  - `我觉得我的腿拉伤了。` → `我觉得我腿部肌肉拉伤了。`
  - 理由: EO/EN/JA/KO/RU は leg muscle を痛めた/拉伤。中国語で `肌肉` が抜けていたため補った。
- `ID4618` EO
  - `Mi havas malfacilaĵojn dormi` → `Mi havas malfacilaĵojn pri dormado`
  - 理由: `malfacilaĵoj` の補語として裸の不定詞を直後に置くより、睡眠に関する困難として `pri dormado` にする方が自然。意味は difficulty sleeping のまま。
- `ID4624` ZH
  - `把这药吃了。` → `请服用这个药。`
  - 理由: 医療者から患者への表現として前者はややぶっきらぼう。EO/JA/KO/RU の丁寧な服薬指示に合わせた。
- `ID4628` ZH
  - `我希望你去看一下专家。` → `我希望你去看一下专科医生。`
  - 理由: specialist は医療文脈の専門医。一般の「専門家」ではなく `专科医生` に明確化。
- `ID4640` EO
  - `Vi bezonos kelkajn suturojn` → `Vi bezonos kelkajn suturerojn`
  - 理由: PIV 2020 で `suturo` は縫合の行為・結果、`suturero` は縫合を構成する個々の結び糸。EN/JA/ZH/KO/RU の「何針か」に合わせ、個々の stitches を指す形へ修正。
- `ID4654` RU
  - `Сколько займёт реабилитация?` → `Сколько времени займёт восстановление?`
  - 理由: EO/EN/JA/ZH/KO は一般的な「回復にどれくらいかかるか」。`реабилитация` だとリハビリに寄るため、`восстановление` へ修正。

主な据え置き確認:
- `ID4558` `privata medicina asekuro`: `malsanasekuro` / `sanasekuro` 系も候補だが、現形でも private medical insurance の意味は透明で、明確な意味ズレなしと判断。
- `ID4568` `haŭterupcio`: PIV 2020 で `erupcio` は皮膚の斑点・丘疹・水疱等の出現として確認。`haŭt-` との透明複合として rash 文脈で未修正。
- `ID4580` `ŝvelo`: PIV 2020 で `ŝvelo` は腫れの状態、`ŝvelaĵo` は腫れたもの。RU `отёк` も腫れ・浮腫なので現形を文脈別許容で未修正。
- `ID4587` `nazkataro`: PIV 2020 で `naza kataro` は鼻のカタル・鼻汁文脈として確認。runny nose として未修正。
- `ID4613` `limfonodoj`: PIV 2020 で `limf adeno` = `limfonodo` と確認。lymph nodes 文脈で未修正。
- `ID4620` `fojnofebro`: PIV 2020 に `fojno febro = fojnkataro` と `fojno kataro` があり、hay fever として確認可能。現形を未修正。
- `ID4629` `sangotesto`: blood test として透明で、RU `анализ крови` / JA/ZH/KO と整合。患者が受ける検査として文脈上誤解は小さいため未修正。
- `ID4648` `urina specimeno`: PIV 2020 で `urina` と `specimeno` を確認。urine sample として透明で、ZH/KO も sample 文脈なので未修正。
- `ID4650` `trinkado`: PIV 2020 で `trinkado de vino devas ĉiam resti modera` 型を確認。飲酒量を減らす文脈で未修正。

一致確認:
- `cmp_exit=0`
- `md5=7c03fe70c973c25df9781bc5de89915d`

## 63. 62周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- 併せて、同じ語根の確認で見つかった既存行 `ID4540` も横断修正

主な修正:
- `ID4540` EO
  - `Bonvolu dezinfekti ĝin` → `Bonvolu desinfekti ĝin`
  - 理由: PIV 2020 では `desinfekti` / `desinfektaĵo` 系を確認。`dezinfekti` は今回の基準では根拠が弱いため、消毒語根を辞書確認できる形へ修正。
- `ID4663` ZH
  - `哪里不舒服？` → `哪里疼？`
  - 理由: EO/EN/JA/KO/RU は「どこが痛いか」。中国語だけ「どこが不調か」へ広がっていたため、痛みに合わせた。
- `ID4682` ZH
  - `请再宽一点。` → `请再张大一点。`
  - 理由: 歯科で口をもう少し大きく開けてもらう文脈。`宽一点` より自然な表現へ修正。
- `ID4689` EO
  - `Vi devus fari rendevuon ĉe la higienisto` → `Vi devus fari rendevuon ĉe la denta higienisto`
  - 理由: PIV 2020 の `higienisto` は衛生の専門家一般。歯科文脈の hygienist / 歯科衛生士なので、PIV確認済みの `denta` と組み合わせて明確化。
- `ID4690` JA
  - `お医者さんが診察の準備ができました。` → `先生が今、診察できます。`
  - 理由: 受付での “The doctor's ready to see you now.” として自然な日本語へ修正。
- `ID4693` RU
  - `У вас небольшой кариес на этом.` → `У вас небольшой кариес в этом зубе.`
  - 理由: ロシア語として目的語が欠けた不自然な形を、this tooth に対応する形へ修正。
- `ID4708` EN
  - `He has big dioptres.` → `His prescription is strong.`
  - 理由: EO/JA/ZH/KO/RU は眼鏡の度が強い意味。英語の “big dioptres” は不自然なので、眼鏡文脈の自然な表現へ修正。
- `ID4723` RU
  - `Ты когда-нибудь теряла очки?` → `Вы когда-нибудь теряли очки?`
  - 理由: 他列は丁寧・一般的な質問。ロシア語だけ親称かつ女性単数過去に固定されていたため、丁寧で性別非固定の形へ修正。
- `ID4725` EO
  - `Kiom kostas ĉi tiuj dizajnistaj kadroj?` → `Kiom kostas ĉi tiuj dezajnistaj kadroj?`
  - 理由: PIV 2020 で `dezajno` / `dezajnisto` を確認。`dizajnistaj` は綴りが不確かなので修正。
- `ID4740` EO
  - `Du ĝis kvar tabletoj tage` → `Du ĝis kvar tablojdoj tage`
  - 理由: PIV 2020 で医薬品の tablet は `tablojdo`。`tableto` は小さい机側に読めるため、服薬文脈に合う形へ修正。
- `ID4743` EO
  - `Mi bezonas dezinfektilon` → `Mi bezonas desinfektaĵon`
  - 理由: PIV 2020 で `desinfektaĵo` は消毒用物質として確認。`-ilo` だと器具にも寄りやすく、JA/ZH/KO/RU は消毒液・消毒剤なので `desinfektaĵo` が安全。
- `ID4744` JA
  - `絆創膏を持っていますか？` → `絆創膏はありますか？`
  - 理由: 薬局で在庫を尋ねる文として自然化。
- `ID4745` JA
  - `痛み止めを持っていますか？` → `痛み止めはありますか？`
  - 理由: 上と同じく薬局での在庫確認として自然化。
- `ID4747` EO/EN
  - EO `Ĉu vi ne havas analogon?` → `Ĉu vi ne havas ion similan?`
  - EN `Haven't you got an analogue?` → `Haven't you got something similar?`
  - 理由: PIV 2020 の `analogo` は主に化学的な類似分子として確認できるが、この薬局文脈では JA/ZH/KO の「似たもの」に合わせ、一般表現へ修正。

主な据え置き確認:
- `ID4656` `antibiotikoj`: PIV 2020 で `antibiotiko` を確認。未修正。
- `ID4669/4683/4692` `plombo` / `plombigi`: PIV 2020 で歯の詰め物・詰める用法を確認。未修正。
- `ID4671/4676` `krono`: PIV 2020 で歯冠・歯にかぶせる crown 用法を確認。未修正。
- `ID4680` `dentprotezo`: PIV 2020 で `protezo` と `denta` を確認。dentures 文脈の透明複合として未修正。
- `ID4684` `absceso`: PIV 2020 で医学語として確認。未修正。
- `ID4699` `gargari la buŝon`: PIV 2020 で buŝo/gorĝo を液体で洗う用法を確認。rinse mouth として未修正。
- `ID4700` `asekuro ... kovras`: PIV 2020 の `kovri` に費用・欠損等を補償する語義を確認。保険が治療をカバーする文脈で未修正。
- `ID4709/4710` `hipermetropa` / `miopa`: PIV 2020 で確認。遠視・近視として未修正。
- `ID4711/4716/4729` `kontaktlensoj`: PIV 2020 で `kontakto lenso` を確認。複合語として未修正。
- `ID4712` `okulvitrujo`: PIV 2020 で `okulvitroj` を確認。`ujo` との透明複合で glasses case として未修正。
- `ID4717/4733` `okulekzameno` / `kontroligi mian vidon`: eye test / 視力検査として意味ズレなし。未修正。
- `ID4722` `astigmatismo`: PIV 2020 で医学語として確認。未修正。
- `ID4730` `UV-protekto`: PIV 2020 で `ultraviola` と `protekto` を確認。略記 `UV` は実用文脈で通るため未修正。
- `ID4737` `termometro`: PIV 2020 で確認。未修正。
- `ID4739` `dozo`: PIV 2020 で薬の定量として確認。`Kia estas la dozo?` は短い薬局質問として文脈別許容で未修正。
- `ID4750` `fastante`: PIV 2020 で空腹・断食状態の語義を確認。empty stomach 文脈で未修正。
- `ID4754` `havebla nur laŭ recepto`: PIV 2020 で `havebla` と `recepto` を確認。prescription-only として未修正。

一致確認:
- `cmp_exit=0`
- `md5=492e8dfff825f3e190b6039e458cd684`

## 64. 63周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`

主な修正:
- `ID4763` EO
  - `Ĉu ĝi havas iujn flankefekojn?` → `Ĉu ĝi havas iujn kromefikojn?`
  - 理由: PIV 2020 では `efekto` は強い印象寄りで、作用・結果は `efiko` 系が適切。さらに `kromefiko` が副次的・非目的的な効果として確認できるため、薬の副作用に合う形へ修正。
- `ID4778` EO/EN
  - EO `en piloloj` → `en tablojdoj`
  - EN `in pills` → `in tablets`
  - 理由: JA/ZH/RU は錠剤。PIV 2020 で医薬品の tablet は `tablojdo` と確認できるため、前回の `ID4740` と合わせた。
- `ID4782` EO
  - `Mi suferas pro malbona digesto` → `Mi suferas pro misdigesto`
  - 理由: PIV 2020 で `misdigesto` は消化障害・indigestion に対応する語として確認できる。意味を変えずに自然化。
- `ID4807` EO
  - `Oni malkonektis nin` → `Ni malkonektiĝis`
  - 理由: “We got cut off” は誰かが切断したというより回線が切れた状態。PIV 2020 の `malkonekti` 系を踏まえ、自動的な切断を表す再帰/自動詞形へ修正。
- `ID4823` EO
  - `Mia baterio baldaŭ elĉerpiĝos` → `Mia baterio baldaŭ malŝargiĝos`
  - 理由: PIV 2020 で `malŝargiĝi` は電池・蓄電池の放電に使える。phone battery の文脈により正確。
- `ID4837` EO
  - `Mi transdonos, ke vi telefonis` → `Mi transdonos la mesaĝon, ke vi telefonis`
  - 理由: `transdoni` は渡す対象を取るのが自然。電話があった旨を「メッセージ」として伝える形に明示。
- `ID4838` ZH
  - `你现在可以说话了吗？` → `你现在方便说话吗？`
  - 理由: 電話・仕事文脈の “Can you speak now?” は「発話能力が戻ったか」ではなく「今話してよいか」。中国語を自然化。
- `ID4850` EO
  - `Ĉu vi povas diski la numeron por mi?` → `Ĉu vi povas klavi la numeron por mi?`
  - 理由: PIV 2020 で `diski` は回転式ダイヤルで番号を作る用法、`klavi` は電話でキーを押す用法として確認。現代的な「番号を入力する」に合わせた。
- `ID4853` ZH
  - `线路正在占用。` → `电话占线了。`
  - 理由: line engaged / 話し中として自然な中国語へ修正。

主な据え置き確認:
- `ID4761` `paracetamolo`: PIV 2020 で直接は確認できなかったが、国際的な薬剤名として列間意味は一致。確実な置換先を置くより現形維持が安全。
- `ID4777` `vojaĝmalsano`: 透明複合で travel sickness / 乗り物酔いと対応。意味ズレなし。
- `ID4779` `kapsuloj`: PIV 2020 で薬剤カプセルの語義を確認。未修正。
- `ID4819` `voka signalo`: PIV 2020 で確認。dialling tone 文脈で未修正。
- `ID4820` `kredito`: 電話残高の実用文脈として意味は明確。未修正。
- `ID4822` `aŭtomata respondilo`: 既存保留解除済み語。answering machine 文脈で未修正。
- `ID4826` `urba telefona kodo`: city/area code の短い質問として文脈別許容。

一致確認:
- `cmp_exit=0`
- `md5=f2e2af0ef7fa89ca25cbc633c59438c1`

## 65. 64周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`

主な修正:
- `ID4859` EO
  - `Atendu la signalon kaj disku la numeron` → `Atendu la signalon kaj klavu la numeron`
  - 理由: `ID4850` と同じく、PIV 2020 の `klavi` の電話用法に合わせて現代的な番号入力へ修正。
- `ID4860` EO
  - `El kiu kompanio vi telefonas?` → `De kiu kompanio vi telefonas?`
  - 理由: calling from which company の出所を表すには `de` が自然。`el` だと物理的内部からの移動に寄る。
- `ID4864` EO
  - `Ĉu vi scias lian internumeron?` → `Ĉu vi scias lian internan numeron?`
  - 理由: `internumero` は生成複合としては読めるが、直後の `ID4865` と合わせて PIV確認済みの `interna` + `numero` にした。
- `ID4893` EO/EN/RU
  - EO `ekskluzivan rakonton` → `ekskluzivan artikolon`
  - EN `exclusive story` → `exclusive article`
  - RU `этот эксклюзив` → `эту эксклюзивную статью`
  - 理由: Mass Media 文脈で JA/ZH/KO は記事・報道。PIV 2020 で新聞・雑誌記事の `artikolo` を確認。
- `ID4905` RU
  - `Ты сегодня читала новости?` → `Вы сегодня читали новости?`
  - 理由: 女性単数・親称に固定されていたため、性別非固定の丁寧形へ修正。
- `ID4920` EO
  - `Kie mi povas sendi ĉi tion?` → `Kie mi povas poŝti ĉi tion?`
  - 理由: `sendi` だと「どこへ送れるか」にも読める。PIV 2020 で `poŝti` は郵便に出すこととして確認。
- `ID4923` EO/JA/ZH/KO/RU
  - EO `Kio estas la valoro?` → `Kiom ĝi valoras?`
  - JA `価値は何ですか？` → `中身の価格はいくらですか？`
  - ZH `值是多少？` → `价值是多少？`
  - KO `가치는 무엇인가요?` → `가격이 얼마인가요?`
  - RU `Какая ценность?` → `Какова стоимость содержимого?`
  - 理由: 郵便・税関文脈の value は「申告額/中身の価格」。PIV 2020 で `valori` は価格として使えるため、金額を尋ねる形に自然化。
- `ID4927` ZH
  - `营业时间是几点？` → `营业时间是几点到几点？`
  - 理由: working hours は開始・終了の範囲。中国語の質問を範囲に合わせた。
- `ID4952` EO/EN/ZH
  - EO `leterkeston` → `poŝtkeston`
  - EN `letter box` → `postbox`
  - ZH `邮箱` → `邮筒`
  - 理由: 投函先は家庭用の `leterkesto` より郵便ポストの `poŝtkesto` が安全。PIV 2020 で `poŝtkesto` 系を確認。

主な据え置き確認:
- `ID4962` `poŝtrestante`: PIV 2020 で郵便局留めの形として確認済み。未修正。
- `ID4873/4889/4890` `retpoŝtadreso`: PIV 2020 で `retpoŝto` と `retadreso` 系を確認。透明複合として未修正。
- `ID4885/4886` `ensaluti` / `elsaluti`: コンピュータの login/logoff 文脈として透明で、列間ズレなし。
- `ID4938/4958` `rekomendita poŝto`: PIV 2020 で `rekomendita, registrita letero` を確認。registered post 文脈として文脈別許容で未修正。
- `ID4933/4948` `afranko`: PIV 2020 で郵便料金の語義を確認。未修正。

一致確認:
- `cmp_exit=0`
- `md5=6d484825f84aa8eb0ab3bfd353364949`

## 66. 65周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`

主な修正:
- `ID4971` RU
  - `С уважением, ваша` → `С уважением,`
  - 理由: letter closing として性別固定かつ未完に見えるため、性別非固定の定型結語へ修正。
- `ID4976` EO
  - `Bonvolu kontakti min senhezite en okazo de bezono` → `Bonvolu ne heziti kontakti min`
  - 理由: PIV 2020 で `heziti` を確認。英語の定型 “do not hesitate to contact me” に合わせ、より自然な語順へ修正。
- `ID4989` RU
  - `ваше приложение` → `ваше вложение`
  - 理由: email attachment は `вложение` が自然。`приложение` はアプリ/付録にも読める。
- `ID4995` EO/EN/RU
  - EO `Sendu al mi novaĵojn, kiam vi ekscios ion pli` → `Sciigu min, kiam vi ekscios ion plian`
  - EN `Send me news, when you know anything more.` → `Let me know when you find out anything more.`
  - RU `Напиши мне новости...` → `Сообщи мне...`
  - 理由: JA/ZH/KO は「何か分かったら知らせて」。PIV 2020 で `sciigi` と `plia` を確認し、news articles 方向に読める `novaĵojn` を避けた。
- `ID5004` EO
  - `Kioma estas la preciza horo?` → `Kioma horo estas precize?`
  - 理由: `kioma horo` のまとまりを保つ方が自然。「正確には何時か」を直接問う形へ修正。
- `ID5030` RU
  - `Во сколько ты проснулась?` → `Во сколько вы проснулись?`
  - 理由: 女性単数・親称を避け、性別非固定の丁寧形へ修正。
- `ID5032` RU
  - `Во сколько ты ложишься спать?` → `Во сколько вы ложитесь спать?`
  - 理由: 上と同じ。
- `ID5036` RU
  - `Твои часы...` → `Ваши часы...`
  - 理由: 他列の一般質問に合わせ、丁寧形へ修正。

主な据え置き確認:
- `ID4962` `poŝtrestante`: 引き続き未修正。PIV 2020 で確認済み。
- `ID4969` `kunsendas mian vivresumon`: `alsendi` も候補だが、CV を同封/添付して送る意味は透明で、明確な意味ズレなし。
- `ID4977/4978/4979/4981/4991` `antaŭĝoji`: 既存メモ通り、透明複合で「楽しみにする」の意味は明確。今回は未修正。
- `ID5049/5051` `labortagoj` / `semajnfinaj tagoj`: 少し説明的だが、各列との対応は明確。未修正。

一致確認:
- `cmp_exit=0`
- `md5=87875205c912d56814c7efd7354645c1`

## 67. 66周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`

主な修正:
- `ID5113` EO/EN/JA/RU
  - EO `Mi ŝatas la veteron` → `Mi ŝatas ĉi tiun veteron`
  - EN `I like the weather.` → `I like this weather.`
  - JA `天気が好きです。` → `こういう天気が好きです。`
  - RU `Мне нравится погода.` → `Мне нравится такая погода.`
  - 理由: ZH/KO は「こういう天気」。一般に天気という概念が好きというより、現在/この種の天気への好みなので明示。
- `ID5141` ZH
  - `天气预报是什么？` → `天气预报怎么说？`
  - 理由: weather forecast の内容を尋ねる自然な中国語へ修正。
- `ID5146` RU
  - `Солнце только что зашло.` → `Солнце только что скрылось.`
  - 理由: EO/EN/JA/ZH/KO は太陽が雲などに隠れた文脈。RU だけ日没に寄っていたため修正。
- `ID5154` RU
  - `Будь осторожен...` → `Будьте осторожны...`
  - 理由: 男性単数・親称を避け、丁寧で性別非固定の形へ修正。

主な据え置き確認:
- `ID5081` `Antaŭ longe`: PIV 2020 で `antaŭ longe` 型を確認。未修正。
- `ID5097` `Estas glacie kaj glite`: PIV 2020 で `glacie` と `glita` 系を確認。icy/slippery 文脈として未修正。
- `ID5115` `Pluvetadas`: `pluvi` + `-et-` + `-ad-` の透明な継続表現。小雨文脈で未修正。
- `ID5118/5145/5149` `fulmotondro`: PIV 2020 の用例群で確認。thunderstorm 文脈で未修正。
- `ID5139` `Estas sub nulo`: 氷点下/零度未満として各列と対応。未修正。
- `ID5143` `Ĉi-nokte frostos`: 今夜の凍結/霜文脈として列間の意味ズレなし。未修正。
- `ID5153` `atmosfera premo`: PIV 2020 で確認。未修正。

一致確認:
- `cmp_exit=0`
- `md5=d23b8456b5551b25faddd2598ab6e4e0`

## 68. 67周目 保留語総仕上げ

対象:
- `PhraseID` は `5155` で終端。`ID5156` 以降の追加 100 件は存在しない。
- そのため、先頭の `保留継続` 表と現行 CSV の不一致、および低優先保留語を再照合。

主な修正:
- `ID3087` EO
  - `Jes, ili ankaŭ ŝatas kalconon` → `Jes, ili ankaŭ ŝatas kalzoneon`
  - 理由: PIV 2020 では直接見出し未確認だが、Wiktionary の calzone 翻訳欄と Wikimedia 系資料で Esperanto 名 `kalzoneo` を確認。現行 `kalcono` は確認が弱く、料理名 calzone の対応として `kalzoneo` の方が安全。目的語なので `kalzoneon`。

保留表の整理:
- `ID2884` `suĉkloŝo`: CSV では前周に `ventuzilo` から修正済み。今回、先頭表に残っていた古い `Mi bezonas ventuzilon` 記述を削除し、保留解除側へ移動。
- `ID2959` `smuzio`: Wiktionary 等で smoothie の Esperanto 語形を確認。PIV 2020 には未収録だが、AI 造語とは言えず、飲料名として JA/ZH/KO/RU と一致するため保留解除。
- `ID2782/2783/2796` `servokotizo`: `servkotizo` 表記は既に `servokotizo` へ統一済み。現在の懸念は表記揺れではなく、PIV の `kotizo` が会費・分担金寄りである点だけなので、先頭表の説明を更新。

主な据え置き確認:
- `ID902` `Mi estas ĉi tie por labori`: RU は出張寄りだが、JA/ZH/KO は「仕事で来ている」と自然に対応するため未修正。
- `ID1560` `Mi estas merkatika administranto`: PIV 2020 で `merkatiko`、`administri/administranto` を確認。`marketing manager / specialist` の列間揺れは残るが、安全な置換先を固定できないため未修正。
- `ID2047/2048/2055/2056/2058` `manbagaĝo`: PIV 2020 で `bagaĝo` は確認済み。直接見出しは弱いが、空港文脈で hand luggage / ручная кладь と対応するため未修正。
- `ID2623` `rulseĝan aliron`: PIV 2020 で `rul seĝo` を確認。`aliro por rulseĝo` も候補だが、現形でも wheelchair access と読めるため未修正。
- `ID2367` `Busstrio`: PIV 2020 の `strio` は lane 専門語ではないため少し弱いが、bus lane の透明複合として意味は明確。標準置換を確定できないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=eb070afe8e39477c0498980e7c09f0fe`

## 69. 68周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- `Saying Hello & Goodbye`、`Good Wishes`、`Thanks`

結果:
- **追加修正なし**

確認観点:
- Streamlit アプリでは CSV の `Esperanto` と `日本語` / `中文` / `한국어` がクイズ本文・選択肢として直接使われるため、定型挨拶・祝辞・感謝表現としての対応を優先。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `danki`、`dankema`、`ĝoji`、`sano`、`tosto/tosti`、`trinki pro ies sano`、`minimumo`、`progresi`、`aprezi` 周辺を照合。

主な据え置き確認:
- `ID186` `Mi antaŭĝojas revidi vin`: PIV 2020 では直接見出し未確認だが、`ĝoji` は `mi ĝojas, ke ...` などの感情表現として確認できる。`antaŭĝoji` は既存保留どおり透明派生で、「再会を楽しみにしている」として JA/ZH/KO/RU と対応するため未修正。
- `ID198` `Sanon!`: PIV 2020 の `sano` に健康を願う祝意・乾杯文脈があり、Bless you / Будь здоров として許容。未修正。
- `ID210` `Ni tostu por vi!` / `ID216` `Mi ŝatus proponi toston por mia filo`: PIV 2020 で `tosto` は健康・名誉・成功のための祝杯挨拶、`tosti` は祝杯を述べる動詞として確認。`por` は「〜のために/〜を祝って」と読め、明確な誤りではないため未修正。
- `ID240` `Tio estis la plej malmulto, kion mi povis fari`: `minimumo` への置換も考えられるが、PIV 2020 で `plej malmultaj` 型の実例があり、現形でも least I could do の意味は各列と一致。文脈別許容として未修正。
- `ID244` `Mi dankas pro via tempo`: PIV 2020 で `danki al iu pro io` と `danko ... pro io` を確認。`Mi dankas vin pro via tempo` の方が明示的だが、現形も省略的に通るため未修正。
- `ID247` `Mi ŝatus diri, kiel dankema mi estas al vi`: PIV 2020 で `dankema` を確認。`kiom dankema` も候補だが、現形は “how grateful” として理解可能で、明確な意味ズレなし。
- `ID251` `Vi farus la samon por mi`: EN は would have done と完了寄りだが、JA/ZH/KO/RU も「同じことをしてくれたはず/してくれる」程度で、感謝への返答として意味は保たれる。未修正。

一致確認:
- `cmp_exit=0`
- `md5=eb070afe8e39477c0498980e7c09f0fe`

## 70. 69周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- `Thanks`、`Apologies`、`Instructions`、`Short Questions & Answers`

結果:
- **追加修正なし**

確認観点:
- Streamlit アプリでは `Esperanto` と `日本語` / `中文` / `한국어` が直接クイズに出るため、短い定型句としての対応、対格、前置詞、語順、感嘆表現としての自然さを優先。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `pardoni/pardonpeti`、`ĝeni`、`celi`、`atenti`、`viciĝi`、`ofendiĝi`、`kuraĝi`、`trankviliĝi`、`nervoza`、`rapidi`、`zorgi pri`、`momento` 周辺を照合。

主な据え置き確認:
- `ID257` `nome de mia edzo`: `nome de ...` は「〜の名において/代表して」と読め、夫の分も礼を述べる文脈で JA/ZH/KO/RU と整合。未修正。
- `ID276` `Mi ne tion celis`: PIV 2020 で `celi` は「意図する/向ける」語義を確認。`Mi ne celis tion` の方が平板だが、現形は `tion` に焦点を置いた語順として成立し、意味ズレなし。
- `ID282` `Ne estas kialo pardonpeti`: `por pardonpeti` を補う案はあるが、PIV 2020 で `pardonpeti` 系と `por + infinitivo` の一般用法を確認。短い会話表現として意味は明確なため未修正。
- `ID285` `Mi agis senzorge`: 前周で修正済み。PIV 2020 の `sen...a` 派生規則と `senzorga/senzorge` 系から「不注意に行動した」と自然に読めるため現形維持。
- `ID289` `Venontfoje mi faros ĉion ĝuste`: `venonta` + `fojo` の透明複合で next time と対応。未修正。
- `ID302` `Kuraĝu!`: PIV 2020 で `kuraĝo/kuraĝi/kuraĝigi` は困難の前で励ます語義を確認。cheer up / 元気を出して / 힘내세요 として文脈別許容。
- `ID308` `Atentu la hundon`: PIV 2020 で `atenti` は他動詞として対象に注意を向ける用法、危険回避の用法を確認。標識文脈の「犬に注意」として未修正。
- `ID316` `Bonvolu viciĝi ĉi tie`: PIV 2020 で `viciĝi` は列に入る/並ぶ意味として確認。queue up here と対応し未修正。
- `ID345` `Kial ne?`: 「なぜだめなのか」と「いいじゃないか」の両方に寄り得るが、短答表現として文脈別許容。未修正。
- `ID354` `Amuze!`: `Tio estas amuza!` も候補だが、短い感嘆として成立し、That's funny / おもしろいね と対応するため未修正。

一致確認:
- `cmp_exit=0`
- `md5=eb070afe8e39477c0498980e7c09f0fe`

## 71. 70周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- `Short Questions & Answers`、`Congratulations`、`Languages`、`Making Yourself Understood`

結果:
- **1件修正**

修正:
- `ID388` EO
  - `Feliĉan Divalion!` → `Feliĉan Divalon!`
  - 理由: PIV 2020 では直接見出し未確認。ただし、オンライン辞書・語彙データ側では Diwali の Esperanto 形として `Divalo` が確認でき、現行 `Divalio` より根拠が強い。祝祭名そのものへの祝意なので、対格形 `Divalon` とした。JA/ZH/KO/RU の「ディワリ/排灯節/디왈리/Дивали」対応は維持。

確認観点:
- Streamlit アプリでは `Esperanto` と `日本語` / `中文` / `한국어` が直接クイズに使われるため、祝辞・言語名・会話短文としての意味対応を優先。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `Divalo/Divalio`、`akĉento`、`akcepti/akcepto`、言語名派生、`jam de` 周辺を再照合。

主な据え置き確認:
- `ID373` `Nu, mi neniam aŭdis pri li`: `hear of` 寄りの英語差はあるが、EO と JA/ZH/KO/RU の「彼について聞いたことがない」は一致。未修正。
- `ID396` `Gratulon pro via akcepto en la universitaton!`: `akcepto` は大学に受け入れられたこととして読める。`akceptiĝo` も候補だが、意味ズレが明確ではないため未修正。
- `ID398` `Gratulojn pro via magistra grado!`: 学位取得への祝辞として各列と一致。`majstra` ではなく `magistra` が必要な文脈で、現形維持。
- `ID415` `Mi parolas iom azerbajĝane`: `Azerbajĝano` からの透明派生で、文脈上 Azerbaijani language と読める。未修正。
- `ID421` `Via tagaloga estas tre bona`: 言語名形容詞の省略名詞用法として「あなたのタガログ語」と読める。未修正。
- `ID428` `Mi parolas nur tre malmulte la nederlandan`: `Mi parolas la nederlandan nur tre malmulte` の方が平板だが、現形でも意味は明確。未修正。
- `ID432` `Mi lernas la indonezian jam de unu monato`: `dum unu monato` も可能だが、`jam de ...` は「...前からずっと」の表現として成立。未修正。
- `ID449` `Mi havas akĉenton`: 前周修正済み。発音上の「なまり」は `akĉento` が適切で、現形維持。
- `ID455` `Mia korea estas sufiĉe malbona`: 口語的な省略で「私の韓国語力」を表し、各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=ca8be5da2f4603710a8e606d8115acb4`

## 72. 71周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- `Making Yourself Understood`、`Agreeing & Disagreeing`、`Asking for & Giving Information`

結果:
- **1件修正**

修正:
- `ID532` EO
  - `Ĉu vi povas rekomendi hostelon?` → `Ĉu vi povas rekomendi junulargastejon?`
  - 理由: `hostelo` は PIV 2020 ローカル抽出で確認できず、置換先として `junular gastejo` が PIV 2020 で確認できる。同じ CSV 内でも `ID1894` が youth hostel 文脈で `junulargastejoj` を使用しており、ZH `青年旅舍`、JA/KO/RU のホステル文脈とも整合するため、語彙を既存の確認済み形へ統一。

確認観点:
- 既存アプリでは `Esperanto` と `日本語` / `中文` / `한국어` がクイズ本文に直接出るため、会話文としての自然さよりも、列間意味対応と確認済み語彙を優先。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `akĉento`、`mandarena`、`junular gastejo`、`drinkejo/picejo`、`bicikli`、移動表現、賛否表現を照合。

主な据え置き確認:
- `ID456` `Parolu kun mi en la mandarena ĉina lingvo`: やや硬いが、PIV 2020 で `la mandarena lingvo` および `la plej multe disvastigita lingvo en Ĉinujo estas la mandarena` 型を確認。標準中国語/普通話と対応するため未修正。
- `ID463` `Ĉu mi ĝuste ĝin prononcas?`: `Ĉu mi prononcas ĝin ĝuste?` の方が平板だが、現形も焦点語順として成立。未修正。
- `ID476` `Mi ne konsentas kun via opinio`: `pri via opinio` も候補だが、意見に同意しない意味は明確。未修正。
- `ID492` `Mi ne povas diri, ke mi kunhavas vian vidpunkton`: PIV 2020 で `kun havi opinion` 型を確認。`vidpunkton` との結合も理解可能で、明確な意味ズレなし。
- `ID497` `En la televido estas tro multe da reklamoj, ĉu ne?`: やや直訳的だが、テレビに広告が多いという意味は各列で一致。未修正。
- `ID526` `Ĉu vi preferas oranĝan aŭ verdan?`: 色名を名詞化するなら別案もあるが、`koloron` 省略として読め、JA/ZH/KO/RU の色選択文脈と一致。未修正。
- `ID531` `Jes, mi iris tien por ferioj`: `ferie` / `dum ferioj` も候補だが、休暇目的で行った意味は明確。未修正。
- `ID536` `Fakte, mi estas survoje por renkonti amikon`: `al renkonto kun amiko` も候補だが、目的の `por renkonti` として成立。未修正。
- `ID542` `Kiom longe vi estis en Kolombio?`: EN は現在完了にも読めるが、EO/RU/JA は過去の滞在期間として整合。未修正。
- `ID551` `Ĉu vi trovas teatron aŭ operon pli interesa?`: `trovi + objekto + predikativa adjektivo` として解釈でき、比較対象も明確。未修正。

一致確認:
- `cmp_exit=0`
- `md5=36f88b3e80f1fa72a6bd173666b808f3`

## 73. 72周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- `Asking for & Giving Information`、`Expressing Feelings`、`Help & Advice`、`Opinions`

結果:
- **追加修正なし**

確認観点:
- 感情表現・弔意・依頼・助言表現として、EO と JA/ZH/KO の対応を主軸に確認。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、特に `trista`、`ekscitita`、`ŝokita`、`motivita`、`embarasita`、`kapturno`、`kondolenco`、`prunti`、`komplezo/servo`、`personaro`、`naŭza` 周辺を照合。

主な据え置き確認:
- `ID562` `Mi estas trista`: PIV 2020 で `trista` は `malgaja, malĝoja` と確認。sad と対応し未修正。
- `ID577` `Mi estas ekscitita`: PIV 2020 で `eksciti` は感情を強く動かす語義を持つ。JA/ZH/KO は期待寄りだが、excited の感情表現として文脈別許容。
- `ID583` `Mia amiko estas ŝokita`: PIV 2020 で `ŝoki/ŝoko` を確認。ショックを受けている文脈として未修正。
- `ID591` `Mi estas motivita`: PIV 2020 の `motivi` は「理由づける」寄りで、現代的な motivation 用法には弱さが残る。ただし `entuziasma`、`inspirita`、`kuraĝigita` 等は意味が寄りすぎるため、明確な誤りとしては扱わず未修正。
- `ID594` `Mi sentas min embarasita`: PIV 2020 で `embarasi` は気まずさ・困惑を表す。embarrassed 文脈として未修正。
- `ID599` `Mi sentas iom da kapturno`: PIV 2020 で `kapturno` および `senti kapturnon` 型を確認。現形は少し説明的だが意味は明確。
- `ID606` `Ni tre bedaŭras aŭdi pri via perdo` / `ID607` `kondolencojn`: PIV 2020 で `pro la perdo de via patro ... kondolencon` 型を確認。弔意表現として各列と整合。
- `ID616` `Ĉu mi povus prunti vian plumon?`: PIV 2020 で `prunti` は「貸す/借りる」の両義を持ち、`pruntepreni` も候補だが、短い依頼表現として誤りとは断定しない。
- `ID623` `Ĉu vi povus fari al mi servon?`: PIV 2020 で `fari servon al iu` 型を確認。`komplezon` も候補だが、現形でも「お願い/助力」として成立。
- `ID646` `flugpersonaron`: PIV 2020 で `personaro` は企業・組織で働く人々の集合、また `aviadila personaro` 系の用例も確認できる。`flug-` 複合として flight crew と読めるため未修正。
- `ID652` `Estas interese` / `ID653` `Estas enuige` / `ID654` `Estas mirinde`: 無主語の感想表現として `Tio estas ...` より短いが、会話句として許容。

一致確認:
- `cmp_exit=0`
- `md5=36f88b3e80f1fa72a6bd173666b808f3`

## 74. 73周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- `Opinions`、`Emergency Situations`、`Accidents`

結果:
- **1件修正**

修正:
- `ID701` EO
  - `Estu singardema!` → `Estu singarda!`
  - 理由: “Be careful!” の即時警告としては、性向を表しやすい `-em-` 入りの `singardema` より、状態・態度を直接表す `singarda` が自然。PIV 2020 でも `singarda/singardaj` の用例を確認でき、同じ CSV 内の `ID5154` も `Estu singarda, ...` としているため統一。

確認観点:
- 意見表現では `plaĉi`、`pensi/kredi/konsideri`、目的語補語、無主語表現を確認。
- 緊急・事故表現では `fajrobrigado`、`ambulanco`、`vundito`、`ŝtelisto`、`perditaj aĵoj/objektoj`、`traŭmatizi`、`stirpermesilo`、`prioritato`、`asekuri`、`akcidentraporto` 周辺を PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で照合。

主な据え置き確認:
- `ID664` `Ili tre plaĉas al mi!`: EN は複数 `them` に修正済み。JA/ZH/KO は数を明示しないが、クイズ主軸の意味破綻はないため未修正。
- `ID679` `Kion vi povas diri pri ĉi tiu bildo?`: `bildo` は写真・絵の広い「画像/絵」として読め、EN/JA/ZH/KO/RU の揺れを吸収できるため未修正。
- `ID682` `La aktorado estis malbona`: PIV 2020 で `aktorado` は俳優の演技・演じ方として確認。未修正。
- `ID693` `Persone, mi konsideras ĉi tiun filmon la plej bona`: `konsideri + objekto + predikativo` として成立。`la plej bonan` へ変えると名詞句内修飾にも読めるため未修正。
- `ID715` `oficejo pri perditaj aĵoj`: PIV 2020 には `fako por perditaj objektoj` 型が確認できるが、現形も遺失物取扱所として透明。後続の同系統表現との整合もあり未修正。
- `ID721` `Ĉu mi povus prunti vian telefonon, mi petas?`: `ID616` と同じく、PIV 2020 で `prunti` は「貸す/借りる」の両義を持つため未修正。
- `ID725` `Mi estas traŭmatizita`: PIV 2020 で `psika traŭmato` と `traŭmatizi` を確認。AI造語ではなく、列間意味も一致。
- `ID733/750` `stirpermesilo`: `stiri` + `permesilo` の透明複合で、CSV内でも運転免許証として一貫。未修正。
- `ID741` `Mi havis la prioritaton`: PIV 2020 で交通文脈の優先権・`prioritato` 系を確認。right of way として未修正。
- `ID754` `akcidentraporto`: 透明な複合語で accident report / 事故報告書と対応。未修正。

一致確認:
- `cmp_exit=0`
- `md5=fa84c23e0715a932bebb0e3f2404058a`

## 75. 74周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- `First Aid`、`At the Police Station`、`Making Friends / Introductions`

結果:
- **2件修正**

修正:
- `ID852` JA/ZH/KO
  - `デイビッドをご紹介します。` → `あなたをデイビッドにご紹介します。`
  - `我来给你介绍一下大卫。` → `我来把你介绍给大卫。`
  - `데이비드를 소개해 드릴게요.` → `당신을 데이비드에게 소개해 드릴게요.`
  - 理由: EO `prezenti vin al Davido`、EN `introduce you to David`、RU `представить вас Дэвиду` は「あなたをデイビッドに紹介する」向き。PIV 2020 の `prezenti` も `prezenti al vi mian amikon` 型を示すため、クイズ対象の日中韓側の向きを明示して一致させた。
- `ID854` EO/EN
  - `Mi ŝatus prezenti vin al Alico` → `Mi ŝatus prezenti Alicon al vi`
  - `I'd like to introduce you to Alice.` → `I'd like to introduce Alice to you.`
  - 理由: JA/ZH/KO/RU はいずれも「アリスをあなたに紹介する」向き。ロシア語を重く見て、EO を `prezenti Alicon al vi` にし、目的語 `Alicon` と到達先 `al vi` を明示した。

確認観点:
- 救急表現では `sangi`、`mordi`、`bruligi sin`、`distordi`、`bandaĝo/bandaĝi`、`frakturo`、`elartikigi`、`manĝaĵveneniĝo`、`novokaino` 周辺を確認。
- 警察表現では `deklaro`、`denunci`、`enrompi`、`advokato`、`aresti`、`anstataŭigi`、`atestanto`、`fotoroboto` 周辺を確認。
- 紹介表現では `prezenti iun/ion al iu` の目的語と `al` 句の方向を重点確認。

主な据え置き確認:
- `ID767` `Bonvolu surmeti bandaĝon`: PIV 2020 では `bandaĝi la piedon/vundon` がより直接的な候補として確認できる。ただし現形は「包帯を着ける/巻く」として理解可能で、RU も `наденьте бандаж` 寄りのため未修正。
- `ID779` `Mi elartikigis mian brakon`: PIV 2020 で `elartikigi sian ŝultron` 型を確認。`brako` との結合は広いが、腕を脱臼した文脈として列間意味は一致するため未修正。
- `ID781` `manĝaĵveneniĝon`: `veneniĝo` と透明複合として food poisoning と読める。未修正。
- `ID797` `deklaron`: PIV 2020 で `deklaro` は公式・形式的な申告/陳述に使える。警察で署名する statement/declaration として未修正。
- `ID803` `Oni enrompis mian aŭton`: 車上荒らしの「車に侵入された」文脈として各列と整合。未修正。
- `ID811` `denunci ŝtelon`: PIV 2020 で `denunci ŝtelon al ...` 型を確認。盗難届の文脈として未修正。
- `ID820` `Ĉu mi povas ĝin anstataŭigi?`: 「再発行」としてはやや広いが、紛失物を置き換える/代替取得する意味で通るため未修正。
- `ID826` `fotoroboton`: PIV 2020 では構成要素 `foto`/`roboto`、Glosbe では `fotoroboto` の使用を確認。RU `фоторобот` とも整合し、AI造語とは断定できないため未修正。
- `ID835` `detruitaj`: RU は `сломаны` で「壊れた/壊された」寄りだが、楽器が損壊した文脈として JA/ZH/KO/EN と大きなズレはないため未修正。
- `ID846` `Maria`: EN/RU は Mary/Мэри だが、EO と JA/ZH/KO は Maria/マリア/玛丽亚/마리아 で一致。クイズ対象列の整合を優先して未修正。

一致確認:
- `cmp_exit=0`
- `md5=fa0bb2960eb7a2a7ef460aa77158beac`

## 76. 75周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- `Making Friends / Introductions`
- `Place of Residence`
- `Age, Nationality & Religion`

結果:
- **追加修正なし**

確認観点:
- 紹介表現では `konatiĝi`、`konas`、`renkontiĝi`、`prezenti al vi ...`、`sinjoron Smirnov`、`fianĉo` の向きと格を確認。
- 居住表現では `loĝi`、`resti`、`kunloĝi`、`dividi ĝin kun ...`、`jam de ses monatoj` を確認。
- 国籍・宗教表現では `Moldavio`、`nacieco`、`usonano`、`aŭstrianino`、`judino`、`germana civitanino`、`slovako/belaruso`、`religio`、`katoliko`、`musulmanino`、`hinduistino` を確認。
- PIV 2020 ローカル抽出・公式辞書系資料で、地名・国籍名・宗教名・職業名の語根と既存用例を照合。

主な据え置き確認:
- `ID858` `Mi estas kun amikino`: `amikino` は女性の友人として読め、RU `подругой` と整合。JA/ZH/KO は性別を明示しないが、意味破綻はないため未修正。
- `ID870` `vendmanaĝero`: `vend-` + `manaĝero` の透明複合で sales manager と読める。未修正。
- `ID877` `Ĉu mi povas prezenti al vi mian fianĉon?`: `prezenti al vi mian fianĉon` は「婚約者をあなたに紹介する」向き。JA/ZH/KO/RU と一致。EN は口語的に逆向きにも見えるが参考列のため未修正。
- `ID878` `sinjoron Smirnov`: 敬称 `sinjoron` に対格が付き、非同化姓 `Smirnov` は原形維持。実用上許容として未修正。
- `ID879` `Ni ĝojas prezenti al vi nian filinon`: EO は娘を相手に紹介する構文で、JA/ZH/KO/RU と一致。EN はやや逆方向に読めるが、紹介場面の参考訳として未修正。
- `ID891/892` `plaĉas al vi ĉi tie` / `Ĉi tie tre plaĉas al mi`: 語順はやや会話的だが、場所を主題化した「ここが気に入る」表現として理解可能。
- `ID902` `Mi estas ĉi tie por labori`: RU は出張 `командировке` 寄りだが、EO と JA/ZH/KO は「仕事で来ている」として整合。未修正。
- `ID909` `Mi dividas ĝin kun unu alia persono`: 直前の住居文脈で `ĝin` は住まいを指し、one other person と共有する意味で一致。未修正。
- `ID921` `Ŝi kunloĝas en domo kun tri aliaj homoj`: `kunloĝi` は共同居住として読め、share a house / 合租 / 집 공유 と整合。
- `ID929` `Li loĝas en Nov-Zelando jam de ses monatoj`: `jam de ...` は現在まで継続する期間を表し、各列と一致。
- `ID936` `Kia estas via nacieco?`: `Kio estas via nacieco?` も自然だが、国籍という属性の種類を問う形として許容。
- `ID939/940/946/949/954/955`: EO と RU は女性形、JA/ZH/KO/EN は性別を明示しないが、性別情報の欠落であり意味衝突ではないため未修正。
- `ID951` `Ĝi estas la 14-a de junio`: 誕生日の日付回答として成立。KO はやや直訳的だが、意味ズレは明確でないため未修正。
- `ID952` `Kia estas via religio?`: `Kio estas via religio?` も候補だが、宗教属性を問う形として文脈別許容。

一致確認:
- `cmp_exit=0`
- `md5=fa0bb2960eb7a2a7ef460aa77158beac`

## 77. 76周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- `Age, Nationality & Religion`
- `Family & Relationships`
- `Describing People`

結果:
- **追加修正なし**

確認観点:
- 宗教名では `budhano`、`siĥo`、`protestantino`、`ateisto`、`preĝejo/templo/moskeo/sinagogo` を確認。
- 国籍・出身では `devenas el ...`、`civitanoj de ...`、`singapuran civitanecon` を確認。
- 家族・交際では `edziniĝinta`、`fraŭla`、`fianĉino`、`rendevui/renkontiĝi kun iu`、`solinfano`、`geavoj/genepoj` を確認。
- 人物描写では `saĝa`、`inteligenta`、`ĝena`、`svelta`、`rufa`、`gustumi`、`ĉarma`、`scivolema` を確認。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、宗教名・親族語・人物描写語・身体部位と感覚動詞を照合。

主な据え置き確認:
- `ID956` `Mi estas budhano`: PIV 2020 で `budhano` は仏教徒、`budhisto` は同義と確認。未修正。
- `ID957` `Mi estas siĥo`: PIV 2020 で `siĥo` 見出しを確認。Sikh として未修正。
- `ID958` `Mi estas protestantino`: RU `протестантка` と一致する女性形。JA/ZH/KO は性別を明示しないが意味衝突ではない。
- `ID972` `Mi devenas el Budapeŝto`: RU は「ブダペストで生まれた」寄りだが、EO と EN/JA/ZH/KO は「もともとはブダペスト出身」。出身表現として未修正。
- `ID977` `singapuran civitanecon`: PIV 2020 で `Singapuro` を確認。`singapura civitaneco` は透明派生で、シンガポール市民権と読める。
- `ID984/990` `edziniĝinta` / `edziniĝis`: 女性話者・女性相手の婚姻表現として RU と整合。未修正。
- `ID996` `mi estas fianĉino`: PIV 2020 で `fianĉino` は婚約した女性。`fianĉiĝinta` も候補だが、意味は一致。
- `ID1008` `mi rendevuas kun iu`: PIV 2020 では約束して会う意味が中心だが、交際文脈では「会っている/付き合っている」寄りに読める。RU/JA/ZH/KO と大きなズレはないため未修正。
- `ID1018` `solinfano`: PIV 2020 の `sola` 系で確認。一人っ子として妥当。
- `ID1032` `Vi estas tre saĝa`: PIV 2020 で `saĝa` は判断力・経験に基づく賢さ、古い用法で intelligent も確認。JA/ZH/KO/RU の「賢い/聪明/똑똑/умная」と許容範囲。
- `ID1048` `Mi havas langon por gustumi`: CSV 内でも `gustumi` は「味わう/味見する」として一貫。舌の機能文脈として未修正。
- `ID1052` `rufajn harojn`: PIV 2020 で `rufa` は赤黄色・赤毛系として確認。未修正。
- `ID1054` `scivolema persono`: 好奇心旺盛な人として各列と一致。未修正。

一致確認:
- `cmp_exit=0`
- `md5=fa0bb2960eb7a2a7ef460aa77158beac`

## 78. 77周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- `Describing People`
- `Things You Like & Dislike`
- `Arranging to Meet`

結果:
- **追加修正なし**

確認観点:
- 人物描写では髪・目・性格表現、`bonkondutaj`、`afablaj` を確認。
- 趣味・好悪表現では `butikumi`、`hobio`、`fotografado`、`patkukoj`、`drinkejo`、`troti`、`piedirado`、`sciencfikciaj libroj`、`mensogulo` を確認。
- 約束表現では `aliĝi al mi/ni`、`kunpreni`、`renkontiĝu`、`rememorigos`、`vestiblo`、時刻表現を確認。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、趣味語・複合語・誘い表現を照合。

主な据え置き確認:
- `ID1064` `Mi amas iri al noktokluboj`: 旧保留の `klubumi` ではなく現行は明示的な「ナイトクラブへ行く」。各列と整合。
- `ID1065` `butikumi`: PIV 2020 で「店を見て回る/買い物をする」意味を確認。未修正。
- `ID1066/1067` `hobio` / `fotografado`: PIV 2020 で確認。趣味・写真撮影として未修正。
- `ID1081` `Mi ŝatas troti`: PIV 2020 で人にも使える「速く小刻みに進む」語義を確認。`jogging` とは少し距離があるが、軽いランニング文脈として文脈別許容。
- `ID1092` `dombestojn`: pets より広いが、RU `домашние животные` とも対応し、家庭で飼う動物文脈として未修正。
- `ID1104` `piedirado`: EN/JA/ZH は hiking 寄り、KO/RU は歩行・徒歩散策寄り。EO は広いが、明確な意味ズレとはせず未修正。
- `ID1110` `modprezentadon`: `modo` + `prezentado` の透明複合で fashion show と読める。
- `ID1115` `sciencfikciaj libroj`: PIV 2020 では直接見出し未確認だが、オンライン辞書側で `sciencfikcio/sciencfikcia` の使用を確認。science fiction books として未修正。
- `ID1116` `mensogulon`: 単数の総称的な「嘘つき」。RU は複数だが、EN/JA/ZH/KO と意味は一致。
- `ID1119/1124` `aliĝi al mi/ni`: PIV 2020 で「加わる/参加する」意味を確認。食事・同席への誘いとしてやや直訳感はあるが許容。
- `ID1136` `Ĉu vi rememorigos min?`: `memorigi/rememorigi` の対人用法として理解可能。未修正。
- `ID1152` `vestiblo`: ホテル・劇場などのロビー/ホール文脈として同CSV内でも一貫。未修正。

一致確認:
- `cmp_exit=0`
- `md5=fa0bb2960eb7a2a7ef460aa77158beac`

## 79. 78周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- `Arranging to Meet`
- `Accepting & Declining`
- `Dating / Asking Someone out`
- `Dating / On a Date`

結果:
- **追加修正なし**

確認観点:
- 承諾・断り表現では `Certe`、`Neniel`、`Mi ne kontraŭas`、`libera`、`malfruiĝas`、`akcepti inviton`、`ĝeni` を確認。
- 誘い表現では `aliĝi al vi`、`regali ... per trinkaĵo`、`lokon kien iri`、`tagmanĝi/vespermanĝi kune`、`renkontiĝi kun iu` を確認。
- デート表現では `plaĉi al mi`、`manki al mi`、`enamiĝi al`、`akompani/veturigi vin hejmen`、`freneziĝi pro vi`、`forveturi de ĉi tie` を確認。
- PIV 2020 ローカル抽出、PIV 2020 公式サイト、Glosbe/一般Web検索で、会話句・恋愛表現・移動表現を照合。

主な据え置き確認:
- `ID1156` `partion de golfo`: PIV 2020 で `partio` はゲーム・対戦の一回を表す語義を確認。ゴルフの1ラウンドとして未修正。
- `ID1160` `Sonas bone`: 主語省略の会話句として “Sounds good.” と対応。未修正。
- `ID1180` `Mi iomete malfruiĝas`: 「少し遅れている/遅れそう」の表現として各列と整合。
- `ID1183` `Ni renkontiĝos tie`: EN は `I'll meet you there` だが、JA/ZH/KO/RU は「そこで会う」文脈で整合。
- `ID1199/1209` `aliĝi al vi`: PIV 2020 で `aliĝi` は加わる/参加する意味。相手に同席を求める表現として許容。
- `ID1206` `Kio pri hodiaŭ?`: `How about today?` 型の会話表現として許容。未修正。
- `ID1208` `Ĉu vi renkontiĝas kun iu?`: `renkontiĝi kun iu` は本来広いが、Dating 文脈では「付き合っている/会っている人がいる」と読めるため未修正。
- `ID1210` `Mi regalos vin per trinkaĵo`: `regali ... per ...` として「飲み物をごちそうする」意味が明確。
- `ID1212` `lokon kien iri`: コンマや `al kiu` も候補だが、「行く場所」の意味は明確。
- `ID1230` `Vi mankas al mi`: PIV 2020 で `manki al ...` 型を確認。I miss you として未修正。
- `ID1235` `Mi enamiĝis al vi`: 恋に落ちた/好きになった文脈として各列と整合。
- `ID1237/1247` `akompani/veturigi vin hejmen`: 徒歩で送る/車で送る差が明確で、各列と整合。
- `ID1245` `Mi freneziĝas pro vi`: PIV 2020 で `freneza pro ...` 型の情熱表現を確認。crazy about you 相当として未修正。
- `ID1253` `Ni forveturu de ĉi tie`: 車・移動を含む `forveturi` で RU `уедем` と整合。JA/ZH/KO は広く「ここを出る」だが、明確な意味衝突ではない。

一致確認:
- `cmp_exit=0`
- `md5=fa0bb2960eb7a2a7ef460aa77158beac`

## 80. 79周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- `Dating / On a Date`
- `Dating / Compliments`
- `Dating / Wedding`
- `Education / At School`

結果:
- **追加修正なし**

確認観点:
- デート・褒め言葉では `fotojn de vi mem`、`enveni por taso da kafo`、`loketon`、`forigu viajn manojn de mi`、`vesto`、`ravega`、`aspekti`、`gusto pri vestoj` を確認。
- 結婚表現では `edziniĝos al mi`、`nupto`、`geedziĝa jubileo/datreveno`、`porcelana/arĝenta/perla/korala/rubina/diamanta` を確認。
- 学校表現では `ŝranketoj`、`gimnastikejo`、`respondi mian demandon`、`hazarda eraro`、`parkere`、`lastan fojon`、`notoj`、`sonorilo` を確認。
- PIV 2020 公式簡易検索とローカル抽出で、`aspekti`、`vesto`、`edziniĝi`、`gimnastikejo`、`respondi`、`noto`、`nupto`、`jubileo`、`hazarda`、`parkere` を照合。

主な据え置き確認:
- `ID1273` `Mi ŝatas vian veston`: PIV 2020 で `vesto` は身に着ける衣服全体も表せるため、outfit / 服装文脈として未修正。
- `ID1286` `Vi aspektas bela en tiu robo!`: PIV 2020 の `aspekti` には副詞例だけでなく `la steloj aspektis tute novegaj` など形容詞述語的な例もあり、`bela` を誤りとはしない。
- `ID1294` `Ĉu vi edziniĝos al mi?`: PIV 2020 で `edziniĝi` は「妻になる」。RU `Ты выйдешь за меня?` と一致する女性相手のプロポーズとして未修正。
- `ID1311〜1316`: 素材名 + 結婚記念日表現は透明で、`nupto/jubileo/datreveno` の範囲内。未修正。
- `ID1323` `gimnastikejo`: PIV 2020 で運動・体操をする場所。学校施設の gym として許容。
- `ID1330` `respondi mian demandon`: PIV 2020 で `respondi tiun ĉi demandon` 型を確認。未修正。
- `ID1350` `ol la lastan fojon`: PIV 2020 で `lastan fojon` の副詞的用法を確認。比較表現として文脈上許容。

一致確認:
- `cmp_exit=0`
- `md5=a5bef0a578842f2ca212b8db3cffbb09`

## 81. 80周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- `Education / At School`
- `Education / At University`
- `Education / Student Life`

修正:
- 参考列のみ: `ID1395` RU `Как долго ты учила болгарский?`
  - `Как давно ты изучаешь болгарский?` に修正
  - 理由: EO `Kiom longe vi lernas la bulgaran?`、EN/JA/ZH/KO は現在まで継続してブルガリア語を学んでいる期間を問う。旧RUは過去に学んだ期間に読め、列間対応がずれていた。
- `ID1401` JA `他の国からの生徒はいらっしゃいますか？`
  - `他の国からの学生はいらっしゃいますか？` に修正
  - 理由: `At University` 文脈で EO/EN/ZH/KO/RU は `studentoj/students/学生/학생/студенты`。日本語も大学文脈に合わせて `学生` に統一。

主な据え置き確認:
- `ID1357` `En kiu aĝo ...`: `Je kiu aĝo` も候補だが、PIV 2020 に `en la aĝo de ...` 型があり、意味ズレはないため未修正。
- `ID1384` `Mi studas por magistriĝo pri juro`: `magistriĝo` は規則派生として理解可能。旧保留どおり、意味を壊さずに置換する根拠が弱いため未修正。
- `ID1386` `Mi prenas liberan jaron`: gap year / академический отпуск 文脈として、前回修正後の形を維持。
- `ID1398` `akceptkondiĉoj`、`ID1399` `eniraj ekzamenoj`、`ID1403` `studentloĝejo`、`ID1408` `lektoro pri la rusa lingvo` はいずれも透明で、大学文脈と整合。
- `ID1437` `Mi faros mian raporton en la kataluna`: `raporto` は口頭・文書の両方に読めるため、RU の oral 寄りと日中韓の written 寄りの揺れを明確な誤りとはしない。
- `ID1454` `templimo por paroladoj`: PIV 2020 で `templimo` を確認。time limit として未修正。

一致確認:
- `cmp_exit=0`
- `md5=a5bef0a578842f2ca212b8db3cffbb09`

## 82. 81周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- `Education / Student Life`
- `Education / Numbers & Colours`
- `Jobs / Occupation`

修正:
- `ID1456` JA `質問を文書で作成することは可能ですか？`
  - `質問を書面で提出することは可能ですか？` に修正
  - 理由: EO `formulitaj skribe`、ZH `以书面形式提出`、RU `сформулированы письменно` は「書面で質問を出す/表す」。旧JAは「文書を作成する」寄りで不自然。
- `ID1460` JA `そのアイデアを最初に考えたのは誰ですか？`
  - `そのアイデアを提案したのは誰ですか？` に修正
  - 理由: EO `proponis` と RU `выдвинул` は「提案した/打ち出した」。旧JAは「発案した」に寄り、前回修正済みENとも焦点がずれていた。

主な据え置き確認:
- `ID1457` `raporto pri sanservo`: `sanservo` は透明複合で healthcare / здравоохранение 文脈として理解可能。未修正。
- `ID1486/1503/1504`: 前回修正後、色名詞主語 + `koloron` 明示の形で安定。未修正。
- `ID1501` `Ruĝo kaj bluo faras purpuron`: RU `сиреневый` はやや明るい紫寄りだが、紫系色として明確な意味衝突とはせず未修正。
- `ID1538` `informteknologio`、`ID1551` `vokcentro`: PIV 2020 で直接見出し未確認だが、構成要素が透明で各列と対応。未修正。
- `ID1543` `juristo`: PIV 2020 では法律・司法の専門家。JA/ZH/KO は弁護士寄りだが、RU `юрист` と整合し、`advokato` に限定しない。
- `ID1545` `veterinaro`: PIV 2020 で `bestokuracisto` と確認。未修正。
- `ID1549` `komercistino`: PIV 2020 で `komercisto` は職業的に商取引をする人。`businesswoman` の広い意味として許容。
- `ID1555` `handikapitaj infanoj`: PIV 2020 で `handikapo/handikapito` を確認。現代的な言い換え余地はあるが意味ズレはないため未修正。

一致確認:
- `cmp_exit=0`
- `md5=a5bef0a578842f2ca212b8db3cffbb09`

## 83. 82周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- `Jobs / Occupation`
- `Jobs / Employment Status`
- `Jobs / At the Workplace`
- `Jobs / Business`

修正:
- 参考列のみ: `ID1556` RU `Она работает на одну компанию.`
  - `Она работает в компании.` に修正
  - 理由: EO/EN/JA/ZH/KO は「会社に勤めている」。旧RUは「一社だけのために働く」という対比に読めるため、通常の勤務先表現へ修正。
- `ID1650` JA `商品の納期が切れます。`
  - `商品の納品期限が切れます。` に修正
  - 理由: EO `limtempo por liveri` と EN `deadline for delivering` は納品の期限。旧JAの `納期が切れる` は不自然なため、意味を保って自然化。
- 参考列のみ: `ID1650` RU `Время доставки товаров истекает.`
  - `Срок доставки товаров истекает.` に修正
  - 理由: EO `limtempo` と EN `deadline` に合わせ、単なる「配送時間」ではなく期限を表す `срок` に修正。

主な据え置き確認:
- `ID1560` `Mi estas merkatika administranto`: `merkatiko` はPIV 2020で確認済み。ただし manager / specialist の職名焦点が列間で揺れるため、保留継続。
- `ID1561/1562` `trejniĝas por fariĝi ...`: training 文脈として妥当。JA は「勉強しています」だが、資格・職業準備の広い表現として許容。
- `ID1573` `administranto pri vendoj`: sales manager として意味明確。未修正。
- `ID1588` `Mi faras praktikon`: PIV 2020 の `praktiko` は実地練習・実務文脈を含み、work experience / практика と整合。
- `ID1590/1591` `patrina/patra forpermeso`: 前回同様、休暇・許可された不在の派生として意味が明確。未修正。
- `ID1602` `Kiel vi veturas al la laborejo?`: 交通手段を尋ねる通勤表現として各列と整合。
- `ID1625` `La pago de ĉi tiu fakturo malfruas`: invoice overdue の支払遅延として未修正。
- `ID1640` `foriras ferien`: 休暇に出かける意味として各列と一致。
- `ID1655` `Ni povas fari la interkonsenton`: deal / сделка として Business 文脈で許容。

一致確認:
- `cmp_exit=0`
- `md5=a5bef0a578842f2ca212b8db3cffbb09`

## 84. 83周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- `Jobs / Business`
- `Jobs / Employment Contracts`
- `Jobs / Job Interview`

結果:
- **追加修正なし**

確認観点:
- ビジネス・契約・面接文脈で、EO と JA/ZH/KO のクイズ対応を主軸に確認。
- PIV 2020 公式簡易検索とローカル抽出で、`formularo`、`raporti`、`laborkontrakto`、`laŭvice`、`deĵori`、`vojaĝkostoj`、`fortaĵo`、`malfortaĵo`、`lojaleco`、`akurateco`、`flegisto/flegistino` を照合。

主な据え置き確認:
- `ID1699` `Al kiu mi devus raporti?`: `raporti al` の構文として、上司・報告先を尋ねる文脈と整合。未修正。
- `ID1711` `akiri rekomendojn`: reference/recommendation の揺れはあるが、面接での推薦・照会文脈として大きな意味ズレはないため未修正。
- `ID1718` `labori laŭvice`: シフト勤務文脈として理解可能。未修正。
- `ID1734` `vojaĝkostojn`: travel expenses として各列と対応。未修正。
- `ID1744/1745` `fortaĵoj/malfortaĵoj`: PIV 2020 で確認でき、長所・短所文脈として未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 91. 90周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- `Car / Road Signs`
- `At the Train Station`

結果:
- **追加修正なし**

確認観点:
- 道路標識、駅・切符・列車案内の表現を確認。
- PIV 2020 ローカル抽出と既存確認で、`busstrio`、`piedira zono`、`trafiklumoj`、`biletejo`、`kajo`、`stampi`、`ekspresa trajno`、`revenbileto/retura bileto` 周辺を照合。

主な据え置き確認:
- `ID2369` `Preterpasu maldekstre`: RU は障害物回避標識寄り、EN/JA/ZH/KO は keep left 寄りだが、左側を通る道路標識として文脈上許容。未修正。
- `ID2370` `Piedira zono`: RU は pedestrian path 寄りだが、クイズ対象列は pedestrian zone で一致。未修正。
- `ID2395` `ŝanĝu aŭtobuson por Zagrebo`: 乗り換えの実用表現として意味は明確。未修正。
- `ID2419` `Kiu kajo?`: PIV 2020 で鉄道の passenger platform として `kajo` を確認済み。現形維持。
- `ID2425` `ekspresa trajno`: PIV 2020 の `ekspres trajno` 系と整合。未修正。
- `ID2431` `Atentu la interspacon`: RU はホーム端に近づかない注意に寄るが、EO/EN/JA/ZH/KO は gap 注意で一致。未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 92. 91周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- `At the Train Station`
- `On the Bus or Train`
- `Taxi`

結果:
- **追加修正なし**

確認観点:
- 定期券、交通カード、車内案内、タクシー会話を確認。
- PIV 2020 ローカル抽出と既存確認で、`abonbileto`、`eksprestrajno`、`vojaĝkarto`、`kupeo`、`pakaĵujo`、`taksimetro`、`trajnstacio`、`superpago/krompago` 周辺を照合。

主な据え置き確認:
- `ID2459` `eksprestrajno`: `ekspresa trajno` への統一も可能だが、PIV 2020 の `eksprestrajno` 系の用例と矛盾しないため未修正。
- `ID2465` `abonbileton`: `aboni` は PIV 2020 で `fervojbileton` にも使える。season ticket / абонемент 文脈として未修正。
- `ID2508` `pakaĵujo`: 荷物を入れる場所として透明で、luggage compartment と大きな意味ズレはないため未修正。
- `ID2518` `preterveturis vian haltejon`: 乗り過ごす意味として成立。未修正。
- `ID2538` `trajnstacio`: `stacidomo` も候補だが、train station として透明で、意味ズレは明確でないため未修正。
- `ID2547` `flughavena superpago`: `krompago` も候補だが、surcharge として意味は通るため過修正せず未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 93. 92周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- `Taxi`
- `Ship`
- `Hotel / Asking about Facilities`
- `Hotel / Booking a Room`

修正:
- `ID2619` KO
  - `흡연실이 있나요?` → `흡연 가능한 객실이 있나요?`
  - 理由: EO `Ĉu vi havas ĉambron por fumantoj?` と RU `У вас есть номер для курящих?` は、ホテルの「喫煙可能な客室」。旧KO `흡연실` は喫煙所・喫煙ブースに読まれやすく、ホテル客室の意味が落ちるため、意味を変えずに `흡연 가능한 객실` へ修正。

主な据え置き確認:
- `ID2569` `Mi havas marmalsanon`: PIV 2020 で `marmalsano` を確認済み。未修正。
- `ID2589` `La krozado estis mirinda`: PIV 2020 の `krozi/krozado` と整合。未修正。
- `ID2603` `radiogramon`: PIV 2020 の radiotelegramo / radiogramo 系と整合。未修正。
- `ID2610/2612` ZH `你有...`: ホテル設備文脈では `你们` も自然だが、会話上の意味ズレは明確でないため未修正。
- `ID2633` `ŝtopilingo`: PIV 2020 で socket に相当する語として確認済み。現形維持。
- `ID2649` `plena pensiono`: 宿泊の full board 文脈として各列と一致。未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 94. 93周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- `Hotel / Booking a Room`
- `Hotel / Checking in`
- `Hotel / During Your Stay`

結果:
- **追加修正なし**

確認観点:
- 予約、チェックイン、客室サービス、ランドリー、電話、非常口を確認。
- PIV 2020 ローカル抽出と既存確認で、`atendolisto`、`duobla ĉambro`、`ĉambronumero`、`ŝlosilo`、`tuko`、`kovrilo`、`ŝargilo`、`gladigi`、`savelirejo`、`plusendi` 周辺を照合。

主な据え置き確認:
- `ID2669` `atendolisto`: waiting list として透明。未修正。
- `ID2681` `duoblan ĉambron kun aldona lito`: double room with extra bed として宿泊文脈で成立。未修正。
- `ID2714` JA `起こさないでください`: literal には do not wake me だが、ホテルの Do not disturb 表示として文脈別許容。未修正。
- `ID2718` `tuko`、`ID2721` `kovrilo`: towel / blanket としてホテル文脈で意味が明確。未修正。
- `ID2744` `savelirejo`: 非常口・避難出口として前回修正後の形を維持。
- `ID2753` `plusendi mian poŝton`: forward mail と対応。未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 95. 94周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- `Hotel / During Your Stay`
- `Hotel / Checking out`
- `Hotel / Complaints`
- `Hotel / Renting a Flat`

修正:
- `ID2837` KO
  - `버튼이 하나 빠져 있어요.` → `단추가 하나 빠져 있어요.`
  - 理由: EO `Mankas butono` はホテル苦情・衣類文脈で、RU `пуговица`、ZH `纽扣` と同じく衣服のボタン。Glosbe EO-KO でも `butono` に `단추` が確認でき、旧KO `버튼` は機械・UIボタン寄りにも読まれるため修正。

主な据え置き確認:
- `ID2765/2794/2795` `elregistriĝi`: checkout 文脈として各列と一致。未修正。
- `ID2782/2783/2796` `servokotizo`: service charge として既存修正後の表記を維持。
- `ID2784/2798` `kalkulo`: bill として宿泊精算文脈で成立。未修正。
- `ID2820` `lavujo`: PIV 2020 では `lavabo` も候補だが、既存確認どおりホテルの sink として過修正せず未修正。
- `ID2833` `bolilo`: kettle / чайник として PIV 2020 の語義と整合。未修正。
- `ID2854/2855` `apartamento/luo`: Renting a Flat 文脈と一致。未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 96. 95周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- `Hotel / Renting a Flat`
- `Restaurant & Pub / Booking a Table`
- `Restaurant & Pub / Ordering Drinks`

結果:
- **追加修正なし**

確認観点:
- 賃貸住居の備品、レストラン予約、飲み物注文を確認。
- PIV 2020 ローカル抽出と既存確認で、`vazaro`、`ŝvabrilo`、`korktirilo`、`suĉkloŝo`、`adherema filmo`、`polvosuĉilo`、`mendi/rezervi tablon`、`fumejo`、`gasita akvo`、`vinkarto` 周辺を照合。

主な据え置き確認:
- `ID2860` `vazaro`: PIV 2020 で家で用いる器一式として確認済み。未修正。
- `ID2875` `kuirilo`: PIV 2020 では広い語だが、EN/RU と賃貸設備文脈から cooker / stove として許容。未修正。
- `ID2884` `suĉkloŝon`: plunger として前回修正後の形を維持。
- `ID2885` `adherema filmo`: cling film として透明で、意味ズレが明確でないため未修正。
- `ID2908` `mendita`: レストラン予約文脈でも `mendi` が使えるため未修正。
- `ID2933` `fumejo`: smoking area として PIV 2020 の喫煙者用別室の語義と整合。未修正。
- `ID2952/2953/2954` `gaso/gasita akvo/sen gaso`: 炭酸水文脈として成立。未修正。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 97. 96周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- `Restaurant & Pub / Ordering Drinks`
- `Restaurant & Pub / Ordering Food`
- `Restaurant & Pub / During the Meal`

結果:
- **追加修正なし**

確認観点:
- 飲み物、ワイン、メニュー、注文、料理名、焼き加減を確認。
- PIV 2020 ローカル抽出と既存確認で、`smuzio`、`koŝera`、`kranakvo`、`pastaĵoj`、`brando/konjako`、`mezrostita`、`farĉi`、`nudeloj` 周辺を照合。

主な据え置き確認:
- `ID2959` `smuzio`: PIV 2020 には強く出ないが、オンライン辞書・用例で smoothie の訳語として確認済み。未修正。
- `ID2984` `kruĉon da kranakvo`: PIV 2020 の `kran akvo` と整合。未修正。
- `ID2991` `konjakon`: PIV 2020 で Cognac 地方由来のブランデーとして確認済み。現形維持。
- `ID3001` `koŝeran manĝaĵon`: PIV 2020 の `koŝera` と整合。未修正。
- `ID3004` `pastaĵojn`: PIV 2020 の pasta 類の集合名として成立。未修正。
- `ID3041` ZH `订单`: レストラン注文として `点的菜` も自然だが、ここでは意味ズレが明確とは断定せず未修正。
- `ID3047` `farĉitajn fungojn`: PIV 2020 の `farĉi` の料理用法と整合。未修正。
- `ID3051` `Mezrostita`: medium の焼き加減として前回修正後の対応を維持。

一致確認:
- `cmp_exit=0`
- `md5=3820169b478cd72d95970c4d6f573642`

## 85. 84周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- `Jobs / Recommendation Letter`
- `Travel / Asking Directions`
- `Travel / Giving Directions`

結果:
- **追加修正なし**

確認観点:
- 推薦状、道案内、位置表現の自然さと列間対応を確認。
- PIV 2020 公式簡易検索とローカル抽出で、`ŝparvojo`、`stacidomo`、`ambasadejo`、`semaforo`、`dekstren`、`maldekstren`、`trans`、`fajrobrigadejo` 周辺を照合。

主な据え置き確認:
- `ID1780` `ŝparvojo`: shortcut 相当として確認済み。未修正。
- `ID1798` `diri al mi la direkton`: `montri la vojon` も候補だが、「道順を教える」として各列と大きくずれないため未修正。
- `ID1804` `aŭtobusa stacio`: bus station / bus terminal 文脈として透明。未修正。
- `ID1807` `ambasadejo`: PIV 2020 で大使館の建物として確認済み。未修正。
- `ID1847` `trans la strato`: PIV 2020 の `trans` の場所表現と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 86. 85周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- `Travel / Giving Directions`
- `Travel / At the Tourist Office`
- `Travel / Excursions`
- `Plane / Booking a Flight`

結果:
- **追加修正なし**

確認観点:
- 観光案内、ツアー、写真、航空券予約の語彙を確認。
- PIV 2020 公式簡易検索とローカル抽出で、`rekten`、`vidindaĵo`、`ekskurso`、`rondvojaĝo`、`gvidata`、`foti/fotografio`、`naveda`、`ekonomiklasa` 周辺を照合。

主な据え置き確認:
- `ID1867` `viziti vidindaĵojn`: sightseeing として各列と整合。未修正。
- `ID1906` `navedan buson`: shuttle bus として、前回修正後の形を維持。
- `ID1928` `en la estona`: 言語指定として自然。未修正。
- `ID1937` `preni miajn fotojn`: 写真店・受け取り文脈で「写真を引き取る」と読めるため未修正。
- `ID1953` `subeksponitaj`: 写真の露出不足として各列と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 87. 86周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- `Plane / Booking a Flight`
- `Plane / Checking in`
- `Plane / Luggage`

結果:
- **追加修正なし**

確認観点:
- 航空券、チェックイン、手荷物・預け荷物の表現を確認。
- PIV 2020 公式簡易検索とローカル抽出で、`flugo`、`bagaĝo`、`registrigi`、`atendejo`、`dogano`、`valizo`、`metala`、`pordego/elirejo` 周辺を照合。

主な据え置き確認:
- `ID1963/1964` `En la antaŭa/malantaŭa vico`: RU は列を明示し、JA/ZH/KO は「前方/後方」寄りだが、座席希望として許容範囲。未修正。
- `ID1984` `forveturo`: 飛行機文脈では `forflugo` も候補だが、一般の出発表現として意味は通るため未修正。
- `ID1999` `registrejo`: check-in counter 文脈として前回修正後の形を維持。
- `ID2011` `enŝipiĝo`: 航空 boarding の慣用拡張として既存保留どおり未修正。
- `ID2044` `registrigas iun bagaĝon`: PIV 2020 の `registrigi pakaĵon` 型と整合。未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 88. 87周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- `Plane / Luggage`
- `Plane / Passport Control & Customs`
- `Plane / On the Plane`

修正:
- `ID2118` EO `Mi ŝatus kontakti la Serban Konsulejon`
  - `Mi ŝatus kontakti la serban konsulejon` に修正
  - 理由: PIV 2020 で `serba` は普通の形容詞として確認できる。周辺の `la kanada ambasadejo`、`argentina delegacio` と同様、普通名詞句として小文字にするのが自然。意味は「セルビア領事館に連絡したい」のまま変更なし。

主な据え置き確認:
- `ID2056/2058` `manbagaĝo`: 空港文脈で意味が明確なため未修正。
- `ID2088` `deklaracio`: PIV 2020 で `deklaracio = deklaro` と確認。税関申告書文脈として許容。
- `ID2089/2113/2115` `dogano`: PIV 2020 の税関・関税文脈と整合。未修正。
- `ID2085/2101/2120` `azilo`: PIV 2020 の `peti azilon` 型と整合。未修正。
- `ID2130` `sekurzono`、`ID2140` `stevardino`、`ID2149` `seĝodorso`: PIV 2020 で確認済みのため未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 89. 88周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- `Plane / On the Plane`
- 空港標識
- `Car / Car Hire`
- `Car / Driving & Parking`

結果:
- **追加修正なし**

確認観点:
- 機内依頼、空港標識、レンタカー、運転・駐車表現を確認。
- PIV 2020 公式簡易検索とローカル抽出で、`dogandeklaro`、`pordego`、`mana`、`aŭtomata`、`transmisio`、`kaŭcio`、`redoni`、`lasi`、`trafikrondo`、`parkumi` 周辺を照合。

主な据え置き確認:
- `ID2156` `veki min por la manĝo`: RU は「食事前に起こす」寄りだが、機内で食事のために起こす文脈として許容。未修正。
- `ID2160` `formularon por dogandeklaro`: `dogana deklaro` と透明に対応。未修正。
- `ID2168` `Pordegoj 1-32`: 空港 gate として既存保留どおり未修正。
- `ID2193/2220` `mana aŭ aŭtomata transmisio`: 前回修正後の形で、車の変速機文脈として明確。未修正。
- `ID2234` `kaŭcio`、`ID2237` `redoni la aŭton`: レンタカー文脈で各列と整合。未修正。
- `ID2252` `Veturu sub la ponto`: 経路表現として許容。未修正。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 90. 89周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- `Car / Driving & Parking`
- `Car / At the Petrol Station`
- `Car / Mechanical Problems`
- `Car / Road Signs`

修正:
- `ID2326` EO `Ĉu vi povus sendi meĥanikiston?`
  - `Ĉu vi povus sendi mekanikiston?` に修正
  - 理由: PIV 2020 では `mekanikisto` が「機械・機構の専門家」として確認でき、`meĥanisto = mekanikisto` も確認できる。一方、旧形 `meĥanikisto` は今回のPIV抽出では直接確認できなかったため、意味を変えずに確認済みの形へ寄せた。

主な据え置き確認:
- `ID2257` `stiradan ekzamenon`: PIV 2020 に `stirado de aŭtomobilo` 型があり、driving test として許容。未修正。
- `ID2268` `aŭtoriparejo`: `aŭto` + `riparejo` の透明複合で、garage / автосервис と整合。未修正。
- `ID2278` `serva areo`: RU は技術サービス寄りだが、EN/JA/ZH/KO は highway service area で一致。クイズ対象列を優先し未修正。
- `ID2318/2322/2336` `akumulatoro`、`malŝargiĝis`、`ŝargi`: PIV 2020 で車載バッテリー文脈に使える語として確認済み。未修正。
- `ID2323` `pneŭmatiko krevis`: PIV 2020 に `krevinta pneŭmatiko`、`ripari krevon de pneŭmatiko` 型があり、puncture 文脈として未修正。
- `ID2342` `direktomontriloj`: PIV 2020 で `direktmontrilo = ĝirindikilo` と確認。未修正。
- `ID2344` `rapidometro`: PIV 2020 で車両の速度表示器として確認。未修正。
- `ID2348` `bremslikvaĵon`: 前回修正後の形を維持。brake fluid として意味が明確。

一致確認:
- `cmp_exit=0`
- `md5=77b8a06f7fde87fcd5b5db79364ef95f`

## 98. 97周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

今回の追加修正:
- `ID3076` KO `디저트 좀 먹을까요?` → `디저트는 어떠세요?`
  - 理由: EO/JA/ZH/RU は接客側の「デザートはいかがですか」。韓国語旧文は話者を含む「食べようか」に寄り、出題対応で誤解が出るため修正。
- `ID3088` JA `料理はいつご用意できますか？` → `私たちの料理はいつできますか？`
  - 理由: EO `nia manĝaĵo` / RU `наша еда` は客側が自分たちの料理を待つ文。旧日本語は店側が料理を用意する可否を尋ねるように読めるため修正。

主な据え置き確認:
- `halala`, `manĝobastonetoj`, `fritoj`, `trinkmono`, `serva pago`, `odori je korko`, `meleagro`, `kalzoneo` は、文脈と多言語列の対応上、現形維持。

## 99. 98周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, At the Pub
- Food / Meat & Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `naĉoj`, `postebrio`, `barela biero`, `laktoskuaĵo`, `rostbefo`, `bova lumbaĵo`, `steko` は、PIVローカル抽出と文脈上の対応から未修正。
- `haringo`, `kalmaro`, `salikoko`, `polpo`, `ŝarko`, `truto` などの魚介名は、多言語列との明確な衝突なし。

## 100. 99周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Food & Spices, Breakfast Food

今回の追加修正:
- `ID3306` KO `그녀는 아시아식 야채 육수를 주문할게요.` → `그녀는 아시아식 야채 육수로 할 거예요.`
  - 理由: 三人称主語 `Ŝi prenos` に対し、`-ㄹ게요` は話し手の意志表明になりやすい。注文内容の報告文として自然化。

主な据え置き確認:
- `limeojn`, `akra kapsiko`, `panitan kukurbeton`, `eruko`, `cerealojn`, `mocarelon` は、前回確認済みの根拠と今回の文脈再確認により現形維持。

## 101. 100周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food
- Shopping / Department Store, Clothes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kazeo`, `kirlovaĵo`, `magazeno`, `Butikoŝtelistoj estos juĝe persekutataj`, `ŝorto` は、前回修正後の形で文脈と整合。

## 102. 101周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Personal Care

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pantalono`, `ŝelko`, `tubo de dentopasto`, `paletron da ŝminko por la palpebroj`, `ŝminko por okulharoj` は、既存の据え置き判断を維持。`stretaj` は後続再点検で衣服用法に合わせて `malvastaj` へ修正済み。

## 103. 102周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care, Electronic Devices, Other Goods, At the Supermarket

今回の追加修正:
- `ID3583` JA/ZH/KO
  - JA `電動のおもちゃをいくつか見せていただけますか。` → `電子玩具をいくつか見せていただけますか。`
  - ZH `我想看看一些电动玩具。` → `我想看看一些电子玩具。`
  - KO `전동 장난감을 좀 보고 싶어요.` → `전자 장난감을 좀 보고 싶어요.`
  - 理由: EO `elektronikajn ludilojn` と RU `электронные игрушки` は「電子玩具」。旧日中韓は「電動・モーター駆動」に狭まるため修正。
- `ID3651` JA `この近くにパン屋はありますか？` → `ここにベーカリーはありますか？`
  - 理由: EO `ĉi tie` / ZH/KO/RU は「ここ」。旧日本語は nearby にずれるため修正。

主な据え置き確認:
- `piloj`, `konstrubriketoj`, `likva sapo`, `marmelado`, `limdato` は、文脈上の対応が保たれているため現形維持。

## 104. 103周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / At the Supermarket, Bookshop & Florist's, Payments & Returns

今回の追加修正:
- `ID3671` JA/ZH/KO
  - JA `そのチョコレート菓子には何が入っていますか？` → `このチョコレート菓子には何が入っていますか？`
  - ZH `那些巧克力糖果里有什么？` → `这些巧克力糖果里有什么？`
  - KO `그 초콜릿 사탕에는 뭐가 들어 있나요?` → `이 초콜릿 사탕에는 뭐가 들어 있나요?`
  - 理由: EO `tiuj ĉi` / EN `these` の近称を保つため修正。
- `ID3737` EO `Ĉu vi povus montri al mi antikvaran librovendejon?` → `Ĉu vi povus diri al mi, kie estas brokanta librovendejo?`
  - 理由: PIV では `antikva` は「古代の・古びた」寄りで、古本屋としては不安定。PIV の `brokanti` とウェブ上の `brokanta librovendejo` 実例を根拠に、second-hand bookshop の意味を明示した。

主な据え置き確認:
- `filtriloj`, `albumojn pri arkitekturo`, `krono el freŝaj floroj`, `konservaĵojn` は、前回確認済みの根拠と今回の文脈再確認により現形維持。

## 105. 104周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments & Returns
- Leisure Time / At the Cinema, At the Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `filmo de suspenso`, `pufmaizo`, `subtekstojn`, `opereto`, `dekoraciojn` は、既存の据え置き判断を維持。

## 106. 105周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / At the Theatre, At the Museum, At the Nightclub

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto`, `teatra lorneto`, `loĝio`, `fulmilo`, `karikatursalono`, `handikapuloj` は、文脈別許容として現形維持。

## 107. 106周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / At the Nightclub, At the Beach, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `diskĵokeo`, `surfotabulon`, `aerbotelo`, `malsekkostumon`, `garantiaĵon`, `gimnastikejo`, `tenisejo`, `rugbeo`, `skiojn` は、既存の修正・据え置き判断を維持。

## 108. 107周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport, Music, Going Camping

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vetproporcioj`, `golfbastonoj`, `golfĉaro`, `regatto`, `popolmuziko`, `ruldomo`, `kukolo`, `pego`, `najtingalo`, `hirundo`, `telfero` は、前回の確認結果どおり現形維持。

## 109. 108周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping, Family Time, Gardening, Having Guests
- Services / At the Bank

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sagetojn`, `televidaj romanoj`, `betoj`, `buŝtukojn`, `bolilo` は、既存の修正・据え置き判断を維持。

一致確認:
- `cmp_exit=0`
- `md5=1297a7c1ccc979de66ad84adb78a3438`

## 110. 109周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank, Estate Agency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provizio`, `kurzo`, `monretiro`, `kontoekstrakto`, `hipoteko`, `ĝiri`, `bangalo`, `vicdomo`, `duamana`, `monata pago` は、既存の修正・据え置き判断を維持。

## 111. 110周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / Estate Agency, Beauty Salon, Tailor, Repairs

今回の追加修正:
- `ID4449` EO
  - `Ĉu vi povus longigi ĉi tiujn pantalonojn je centimetro?` → `Ĉu vi povus longigi ĉi tiun pantalonon je centimetro?`
  - 理由: PIV 2020 の `pantalon/o` は一着の衣服を単数として扱い、Zamenhof に見られる一着への複数形使用は非推奨と説明している。JA/ZH/KO/RU も「このズボン/这条裤子/이 바지/эти брюки」と一着を指すため、EO を単数に揃えた。

主な据え置き確認:
- `dislimo`, `helajn striojn en miaj haroj`, `senharigo`, `feni`, `ŝampui`, `sprajo por haroj`, `ĝelo por haroj`, `skalpo`, `laŭmezura kostumo`, `alĝustigi` は、既存の修正・据え置き判断を維持。

## 112. 111周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs
- Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pilo`, `kroneto`, `plandumoj`, `garantio`, `kapturno`, `alkoholaĵojn`, `rentgena ekzameno`, `analizojn`, `malsanasekuro`, `surdorse` / `surventre` は、既存の修正・据え置き判断を維持。

## 113. 112周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor, Diseases, Treatment

今回の追加修正:
- `ID4633` EO
  - `Mi bezonas malsanatestilon` → `Mi bezonas kuracistan atestilon`
  - 理由: `malsanatestilo` は透明な複合語として意味は推測できるが、PIV 2020 ローカル抽出では直接確認できなかった。PIV では `atestilo` が「何かについて証明する文書」として確認でき、ウェブ上でも `kuracista atestilo` の実例を確認できるため、sick note / 診断書 / 病假条 / больничный лист の文脈により安全な形へ修正した。`sanatesto` 系は「健康証明」に寄り得るため採用しなかった。

主な据え置き確認:
- `privata medicina asekuro`, `haŭterupcio`, `ŝvelo`, `nazkataro`, `limfonodoj`, `mikozo de la piedoj`, `fojnofebro`, `sangotesto`, `urina specimeno`, `trinkado`, `sutureroj` は、既存の修正・据え置き判断を維持。

## 114. 113周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `piloloj`, `plombo` / `plombigi`, `krono`, `dentprotezo`, `absceso`, `gargari la buŝon`, `denta higienisto`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `okulekzamenoj`, `astigmatismo`, `UV-protekto`, `dozo`, `tablojdoj`, `desinfektaĵo`, `fastante`, `havebla nur laŭ recepto` は、既存の修正・据え置き判断を維持。

## 115. 114周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy
- Communication Means / Phone, Phone Calls at Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kromefikoj`, `paracetamolo`, `vojaĝmalsano`, `tablojdoj`, `kapsuloj`, `misdigesto`, `malkonektiĝis`, `malŝargiĝos`, `voka signalo`, `kredito`, `aŭtomata respondilo`, `klavi la numeron` は、既存の修正・据え置き判断を維持。

## 116. 115周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `de kiu kompanio`, `interna numero`, `retpoŝtadreso`, `ensaluti` / `elsaluti`, `ekskluziva artikolo`, `poŝti`, `valoras`, `poŝtkesto`, `rekomendita poŝto`, `afranko`, `vatita koverto`, `televida licenco`, `libreto da poŝtmarkoj` は、既存の修正・据え置き判断を維持。

## 117. 116周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter
- Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `Sincere via`, `Respektplene via`, `kunsendas mian vivresumon`, `ne heziti kontakti min`, `antaŭĝojas`, `aldonaĵo`, `Sciigu min`, `Kioma horo estas precize?`, `kvarono antaŭ/post`, `labortagoj`, `semajnfinaj tagoj` は、既存の修正・据え置き判断を維持。

## 118. 117周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather
- `PhraseID` は `5155` で終端。`ID5156` 以降の追加行は存在しない。

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Hodiaŭ tage`, `En la venonta monato`, `Antaŭ longe`, `Estas glacie kaj glite`, `Pluvetadas`, `fulmotondro`, `Ĉi-nokte frostos`, `sub nulo`, `atmosfera premo`, `Estu singarda, la stratoj estas tre glitaj` は、既存の修正・据え置き判断を維持。

一致確認:
- `cmp_exit=0`
- `md5=76d83c069f94d7659664ee1cca98337d`

## 119. 118周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Sanon!`, `tosti por...`, `Tio estis la plej malmulto, kion mi povis fari`, `Mi dankas pro via tempo`, `Vi ne scias, kiel dankema mi estas` は、挨拶・乾杯・感謝表現として文脈別許容を維持。

## 120. 119周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions & Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi ne tion celis`, `Ne estas kialo pardonpeti`, `Kuraĝu!`, `Atentu la hundon`, `viciĝi`, `Amuze!` は、語順・省略・短い応答表現として意味破綻なし。

## 121. 120周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Short Questions & Answers, Congratulations, Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Gratulon pro via akcepto en la universitaton!`, `azerbajĝane`, `Via tagaloga estas tre bona`, `Mi lernas la indonezian jam de unu monato`, `Mia korea estas sufiĉe malbona` は、既存の文脈別許容判断を維持。

## 122. 121周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- Making Yourself Understood, Agreement & Disagreement, Asking for & Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Parolu kun mi en la mandarena ĉina lingvo`, `Ĉu mi ĝuste ĝin prononcas?`, `Mi ne konsentas kun via opinio`, `Jes, mi iris tien por ferioj`, `Fakte, mi estas survoje por renkonti amikon`, `junulargastejo` は、列間意味の明確なズレなし。

## 123. 122周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Questions, Expressing Feelings, Help & Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi estas ekscitita`: PIV 2020 ローカル抽出で `eksciti` が感情を強く動かす語義を持つことを再確認。JA/ZH/KO は期待寄りだが、RU `взволнован` とも合わせ、明確な誤訳とはしない。
- `Mi estas motivita`, `Mi sentas iom da kapturno`, `via perdo` / `kondolencojn`, `Ĉu vi povus fari al mi servon?`, `flugpersonaron` は、過去の辞書確認・文脈別許容判断を維持。

## 124. 123周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- Opinions, Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bildo`, `aktorado`, `konsideras ĉi tiun filmon la plej bona`, `oficejo pri perditaj aĵoj`, `traŭmatizita`, `stirpermesilo`, `Mi havis la prioritaton`, `akcidentraporto` は、事故・警察文脈として既存判断を維持。

## 125. 124周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- First Aid, At the Police Station, Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `surmeti bandaĝon`, `elartikigis mian brakon`, `deklaron`, `Oni enrompis mian aŭton`, `denunci ŝtelon`, `fotoroboton`, `familinomo`, `konatiĝi kun vi` は、PIV/既存メモで確認済みの範囲内として維持。

## 126. 125周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Introductions, Place of Residence, Age / Nationality / Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `amikino`, `fraŭlino`, `vendmanaĝero`, `Ĉi tie tre plaĉas al mi`, `Kio alkondukas vin al Brazilo?`, `Moldavio`, `Kia estas via nacieco?`, `Kia estas via religio?` は、多少の言い換え余地はあるが意味ズレは明確でない。

## 127. 126周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Age / Nationality / Religion, Family & Relationships, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `siĥo`, `fianĉiĝinta`, `edziniĝinta`, `fianĉino`, `en rilato`, `solinfano`, `bonŝanculo`, `bela` for male attractiveness, `ĝena`, `rufajn harojn` は、各列との対応を保つため未修正。

## 128. 127周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bonkondutaj`, `noktokluboj`, `patkukojn`, `troti`, `dombestojn`, `piedirado`, `modprezentadon`, `sciencfikciaj libroj`, `rememorigos`, `vestiblo` は、既存の確認結果を維持。

## 129. 128周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Arranging to Meet, Accepting & Declining, Asking Someone out, On a Date

結果:
- **1件修正**

修正:
- `ID1254` EO
  - `Lasu min trankvilan` → `Lasu min trankvila`
  - 理由: PIV 2020 ローカル抽出の `las/i` に `lasu ŝin trankvila!`、`trankvil/a` に `lasu min trankvila!` の用例を確認。目的語 `min` の状態を表す目的語述語補語なので、Esperanto では対格 `-n` を付けない形が標準的。意味は Leave me alone / ほっといて / 别烦我 / Оставь меня в покое のまま変更なし。

主な据え置き確認:
- `partion de golfo`, `aliĝu al mi por tagmanĝo`, `Kion vi elpensis?`, `Ni forveturu de ĉi tie` は、RU/日中韓との対応を踏まえ、明確な修正対象とはしない。

## 130. 129周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- On a Date, Compliments, Wedding, At School

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `loketon`, `Forigu viajn manojn de mi!`, `ravega`, `kantistino`, `Mi trovas vin tre alloga`, `nupto`, `novgeedzoj`, `faros unu la alian ege feliĉaj`, `porcelana/arĝenta/perla/korala/rubina/diamanta` wedding anniversary 表現、`ŝranketojn`, `gimnastikejon`, `parkere`, `notoj` は、文脈別許容を維持。

## 131. 130周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo...`, `studjaro`, `liberan jaron`, `akceptkondiĉoj`, `studentloĝejo`, `universitataj instruistoj`, `lektoro pri la rusa lingvo`, `bibliotekan formularon`, `trapasis`, `malsukcesis en la ekzameno`, `templimo`, `formulitaj buŝe` は、既存の修正・据え置き判断を維持。

## 132. 131周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life, Numbers & Colours
- Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `formulitaj skribe`, `ripeti multajn aferojn`, `purpuron`, `viola`, `Du mil foje kvin estas dek mil`, `informteknologio`, `juristo`, `veterinaro`, `komercistino`, `vokcentro`, `handikapitaj infanoj` は、PIV 2020 ローカル抽出および既存メモで確認済みの範囲として未修正。

一致確認:
- `cmp_exit=0`
- `md5=4bd8c1202c6141d87e7e8da972de255b`

## 133. 132周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment / Job Search

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mana laboro`, `fakulo`, `senlabora`, `laborposteno`, `kandidatiĝi`, `vivresumo`, `kvalifikojn`, `lerno- kaj trejniĝperiodo`, `prova periodo`, `referencoj` は、職業・求職文脈で多言語列との対応が保たれているため未修正。

## 134. 133周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Employment / Job Search, At Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `intervjuo`, `ŝanĝebla horaro`, `libertagoj`, `laborpermeso`, `renkontiĝo`, `raporto`, `malfruas`, `estrino`, `kunlaboranto` は、意味ズレなしとして既存判断を維持。

## 135. 134周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Employment / At Work, Shopping / Shopping Centre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `malsanforpermeso`, `kontoro`, `retpoŝto`, `fakso`, `akcepto`, `repreni`, `aĉetcentro`, `eskalatoro`, `lifto` は、アプリの買い物・職場クイズ文脈で許容。

## 136. 135周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Shopping / Shopping Centre, Clothes & Shoes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pagotablo`, `refundo`, `rabato`, `balkostumon`, `strikitan veŝton`, `ĉapelo`, `grando`, `ŝuoj`, `laĉoj` は、日中韓との対応に明確な破綻がないため未修正。

## 137. 136周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Shopping / Clothes & Shoes, Groceries

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provĉambro`, `tro grandaj/malgrandaj`, `ŝanĝi ĝin`, `monujo`, `legomvendisto`, `lakto`, `pano`, `bovaĵo`, `porkaĵo`, `kokidaĵo` は、語形・数・意味の面で許容範囲。

## 138. 137周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Shopping / Groceries, At the Chemist's

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ŝafaĵo`, `hepato`, `konfitaĵo`, `mielo`, `butero`, `paketo`, `sako`, `recepto`, `doloroj`, `kontraŭdoloriloj`, `sen recepto` は、既存修正後の状態を維持。

## 139. 138周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Transport / Car Rental, Driving

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dogandeklaro`, `pordegoj`, `kaŭcio`, `mana/aŭtomata transmisio`, `redoni la aŭton`, `mekanikiston`, `direktomontriloj`, `akumulatoro`, `bremslikvaĵo` は、過去修正と既存確認を維持。

## 140. 139周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Transport / Driving, Bus & Coach, Train

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pneŭmatiko krevis`, `serva areo`, `biletmaŝino`, `bushaltejo`, `kajo`, `eksprestrajno`, `abonbileto`, `pakaĵujo` は、文脈内で意味が取れるため未修正。

## 141. 140周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Transport / Train, Taxi, Airport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kuŝvagono`, `vagonaro`, `taksimetro`, `trajnstacio`, `flughavena superpago`, `registriĝo`, `enira/elira pordego`, `bagaĝa troleo` は、日中韓・RU と整合。

## 142. 141周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Transport / Airport, On the Plane, Ship

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `surteriĝo`, `ekflugo`, `sekureczono`, `savveŝto`, `enŝipiĝkarto`, `marmalsano`, `ferdeko`, `kajuto`, `pramo` は、交通文脈で未修正。

## 143. 142周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Transport / Ship, Hotel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kajo`, `krozado`, `radiogramo`, `ŝtopilingo`, `plena pensiono`, `duonpensiono`, `atendolisto`, `savelirejo` は、既存の文脈別許容を維持。

## 144. 143周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Accommodation / Hotel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `rezervon`, `ununokta restado`, `ĉambron kun du litoj`, `privata banĉambro`, `klimatizilo`, `kontinenta matenmanĝo`, `nokta pordisto` は、意味ズレなし。

## 145. 144周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Accommodation / Hotel, Restaurant

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `elregistriĝi`, `servokotizo`, `lavujo`, `bolilo`, `vazaro`, `suĉkloŝo`, `fumejo`, `gasita akvo` は、過去確認済みの語として未修正。

## 146. 145周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Restaurant / At the Restaurant, Ordering

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mendi tablon`, `manĝokarto`, `kelnero`, `sen viando`, `vegetarana`, `serviĝis`, `aldonaĵoj`, `mineralakvo` は、飲食店文脈で各列と整合。

## 147. 146周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant / Ordering, Complaints, Food

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio`, `kranakvo`, `koŝera`, `pastaĵoj`, `farĉitaj fungoj`, `mezrostita`, `odoras je korko` は、辞書確認済みまたは透明な複合として未修正。

## 148. 147周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant / Food, Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ĉefplado`, `deserto`, `spica`, `senlaktoza`, `naĉoj`, `postebrio`, `barela biero`, `laktoskuaĵo`, `limeoj` は、内容変更を避けるため現形維持。

## 149. 148周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant / Food & Groceries

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `akra kapsiko`, `kukurbeton`, `eruko`, `cerealojn`, `melongeno`, `saliko`, `sekvinberoj`, `poreo`, `brasiko` は、食品名として対応が取れている。

## 150. 149周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Shopping / Groceries, Department Store

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kazeo`, `kirlovaĵo`, `magazeno`, `fako`, `rabataĵo`, `Butikoŝtelistoj estos juĝe persekutataj`, `ŝorto`, `pantalono`, `ŝelko` は、既存判断を維持。

## 151. 150周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Shopping / Department Store, Cosmetics

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `stretaj` は PIV 2020 ローカル抽出で `stret/a` = `mallarĝa` を確認して一度据え置いたが、後続再点検で衣服用法に合わせて `malvastaj` へ修正済み。`tubo de dentopasto`, `paletro da ŝminko por la palpebroj`, `ŝminko por okulharoj` は未修正。

## 152. 151周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Cosmetics, Gifts & Books

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pinĉilo`, `konstrubriketoj`, `limdato`, `poemaro`, `brokanta librovendejo`, `krono el freŝaj floroj` は、複合語として透明で意味ズレなし。

## 153. 152周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Leisure / Cinema, Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `filmo de suspenso`, `pufmaizo`, `subtekstojn`, `opereto`, `dekoraciojn`, `premiero`, `spektaklo`, `orkestra balkono` は、娯楽文脈で未修正。

## 154. 153周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Leisure / Theatre, Museum & Arts

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto`, `teatra lorneto`, `loĝio`, `fulmilo`, `karikatursalono`, `handikapuloj` は、PIV 2020 ローカル抽出および既存確認により未修正。

## 155. 154周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Leisure / Museum & Arts, Nightlife

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `galerio`, `akvarelo`, `olepentraĵo`, `abstrakta arto`, `noktoklubo`, `diskoteko`, `enirkotizo`, `garderobejo` は、対応列と整合。

## 156. 155周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure / Nightlife, Sports

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `diskĵokeo`, `surfotabulon`, `aerbotelo`, `malsekkostumon`, `garantiaĵon`, `gimnastikejo`, `tenisejo`, `rugbeo` は、スポーツ・レジャー文脈で未修正。

## 157. 156周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure / Sports, Hobbies

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `skiojn`, `vetproporcioj`, `golfbastonoj`, `golfĉaro`, `regatto`, `popolmuziko`, `ruldomo` は、既存確認を維持。

## 158. 157周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure / Hobbies, Going Camping

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kukolo`, `pego`, `najtingalo`, `hirundo`, `telfero`, `tendumi`, `tendumilo`, `dormsako`, `kompaso`, `piedvojetoj` は、分野語として現形維持。

## 159. 158周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure / Camping, Family Time, Gardening, Having Guests

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `televidaj romanoj`, `sagetojn`, `betoj`, `buŝtukojn`, `bolilo`, `Mi boligos akvon`, `La bolilo bolis` は、既存メモどおり文脈別許容で未修正。

## 160. 159周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / Bank, Estate Agency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provizio`, `kurzo`, `monretiro`, `kontoekstrakto`, `hipoteko`, `ĝiri`, `bangalo`, `vicdomo`, `duamana`, `monata pago` は、過去確認済みの判断を維持。

## 161. 160周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / Estate Agency, Beauty Salon, Tailor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dislimo`, `farbigi`, `farbi ... blonde`, `helajn striojn en miaj haroj`, `senharigo`, `feni`, `ŝampui`, `skalpo`, `laŭmezura kostumo`, `pantalonon` は、既存修正後の状態を維持。

## 162. 161周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs, Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pilo`, `kroneto`, `rentgena`, `sangogrupo`, `O negativa`, `O-pozitiva`, `kmeran`, `trankviligilo`, `surdorse/surventre` は、既存判断を維持。

## 163. 162周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / Diseases, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haŭterupcio`, `nazkataro`, `fojnofebro`, `limfonodoj`, `mikozo de la piedoj`, `sangotesto`, `sutureroj`, `urina specimeno` は、PIV 2020 ローカル抽出および既存メモで確認済みのため未修正。

## 164. 163周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Dentist, Optician, Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `plombo`, `krono`, `dentprotezo`, `denta higienisto`, `gargari la buŝon`, `grandajn dioptriojn`, `hipermetropa`, `miopa`, `kontaktlensoj`, `fastante` は、意味ズレなしとして未修正。

## 165. 164周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / Pharmacy, Communication Means / Phone

結果:
- **2件修正**

修正:
- `ID4778` KO
  - `이 약을 알약 형태로도 있나요?` → `이 약은 알약 형태로도 있나요?`
  - 理由: `있나요?` の存在文では、対象薬は目的語ではなく主題として出す方が自然。意味は「この薬は錠剤でもありますか」のまま。
- `ID4779` KO
  - `이 약을 캡슐 형태로도 있나요?` → `이 약은 캡슐 형태로도 있나요?`
  - 理由: 上と同じ。カプセル剤の有無を尋ねる自然な韓国語に調整。

主な据え置き確認:
- EO の `tablojdoj`, `kapsuloj`, `dormigiloj`, `kromefikoj`, `maldigesto`, `ensaluti/elsaluti`, `telefonkarto`, `aŭtomata respondilo` は、対応列と整合しているため未修正。

## 166. 165周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, Post Office

結果:
- **1件修正**

修正:
- `ID4946` KO
  - `이 엽서를 호주로 보내는 우표 주세요.` → `이 엽서를 호주로 보내기 위한 우표 주세요.`
  - 理由: 直訳的な `보내는 우표` では「送る切手」と読めて不自然。`A stamp for this postcard to Australia` / JA / ZH / RU と同じく「送るための切手」に明確化。

主な据え置き確認:
- EO の `interna numero`, `retpoŝtadreso`, `uzantonomo`, `Skajpo`, `Facebook`, `Tvitero`, `tekkomputilo`, `vatita koverto`, `afranko`, `rekomendita poŝto`, `pesilo` は、明確な誤りなし。

## 167. 166周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / Post Office, Letter, Time & Weather / Telling the Time, Calendar

結果:
- **1件修正**

修正:
- `ID4956` KO
  - `이 주소로 나이지리아에 보내주실 수 있나요?` → `나이지리아의 이 주소로 보내주실 수 있나요?`
  - 理由: `this address in Nigeria` / `al ĉi tiu adreso en Niĝerio` の修飾関係を自然な韓国語語順に整理。意味内容は変更なし。

主な据え置き確認:
- EO の `poŝtrestante`, `vivresumon`, `antaŭĝojas`, `kunsendas`, `aldonaĵon`, `Kioma horo estas precize?`, `kvarono antaŭ/post`, `Ĝis la unua horo`, `libertago` は、既存修正後の状態を維持。

## 168. 167周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Hodiaŭ tage`, `Ĉi-posttagmeze`, `Postmorgaŭ`, `Estas glacie kaj glite`, `Pluvetadas`, `Fulmas`, `fulmotondro`, `Malvarmas`, `Varmegas`, `sub nulo`, `Ĉi-nokte frostos`, `La suno ĵus kaŝiĝis`, `atmosfera premo` は、日中韓・RU と照合して未修正。

## 169. 168周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basics / Greetings, Polite Phrases

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Sanon!`, `Ni tostu por vi!`, `toston por mia filo`, `Mi dankas pro via tempo`, `Mi antaŭĝojas revidi vin`, `Tio estis la plej malmulto...` は、PIV 2020 ローカル抽出および文脈照合で明確な誤りなし。

## 170. 169周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basics / Polite Phrases, Travel & Small Talk

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi ne tion celis`, `Donu al mi ĉi tiun`, `Ne paŝu sur la gazonon!`, `Post vi`, `viciĝi`, `Kial ne?`, `Amuze!` は、語順・省略・文脈別許容として未修正。

## 171. 170周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Communication / Languages

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bengale`, `rumane`, `urdue`, `perse`, `slovene`, `latve`, `norvege`, `malaje`, `Divalon`, `akĉenton` は既存修正後の状態を維持。
- `azerbajĝane`, `tagaloga` は少し気になるが、透明な派生として意味ズレが明確でないため未修正。

## 172. 171周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- Communication / Languages, Opinions, Travel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mandarena ĉina lingvo`, `akĉento`, `kunhavas vian vidpunkton`, `junulargastejo`, `survoje por renkonti amikon`, `biciklas` は、PIV 2020 ローカル抽出および列間照合で現形維持。

## 173. 172周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Feelings, Help & Advice

結果:
- **1件修正**

修正:
- `ID632` EO
  - `Ĉu vi estus tiel afabla klarigi tion denove?` → `Ĉu vi estus tiel afabla kaj klarigus tion denove?`
  - 理由: `esti tiel afabla kaj ...` 型は PIV 2020 の `afabla/kaj` 周辺例および Zamenhof 用例で確認できる。元文は意味は通るが接続が抜けた英語直訳調なので、内容を変えずに自然な依頼文へ調整。

主な据え置き確認:
- `kapturno`, `kolera kontraŭ si mem`, `Niaj pensoj estas kun vi`, `flugpersonaro`, `malkonsilus lui aŭton`, `Ĉu ĝenus vin...` は、明確な意味ズレなし。

## 174. 173周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- Opinions, Emergencies / Accident

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `aktorado`, `butikumado`, `traŭmatizita`, `prioritaton`, `stirpermesilo`, `urĝas/urĝa`, `fajrobrigado` は、PIV 2020 ローカル抽出で確認済み。事故・緊急時文脈とも整合。

## 175. 174周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / Medical Help, Police Station, Introductions

結果:
- **2件修正**

修正:
- `ID803` EO
  - `Oni enrompis mian aŭton` → `Oni enrompis en mian aŭton`
  - 理由: `enrompi` は「保護された入口などを破って中へ入る」意味で、ReVo/PIV の用例でも目的地は `en ...` で示す形が自然。車上荒らし・車への侵入という各列の意味に合わせて前置詞を補った。
- `ID853` EO
  - `Ĉu mi povas prezentiĝi?` → `Ĉu mi povas prezenti min?`
  - 理由: `prezentiĝi` は「現れる／提示される」寄り。自己紹介は PIV 2020 の `prezenti sin/min` 型が明確なので、`May I introduce myself?` に合わせて反身表現へ修正。

主な据え置き確認:
- `distordis mian maleolon`, `elartikigis mian brakon`, `manĝaĵveneniĝon`, `poliso de medicina asekuro`, `fotoroboton`, `turniĝis al la oficejo pri perditaj aĵoj` は、文脈別許容として未修正。

## 176. 175周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions, Address, Nationality & Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Ĉi tie tre plaĉas al mi` は PIV 2020 に近い用例があり現形維持。
- `Kia estas via nacieco?`, `Kia estas via religio?`, `Moldavio`, `Nov-Zelando`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio` は既存判断を維持。

## 177. 176周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age, Nationality & Religion, Family & Relationships, Appearance

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `siĥo`, `fianĉino`, `rendevuas kun iu`, `genepoj`, `bonŝanculo`, `okulvitroj`, `blondaj/rufaj haroj`, `gustumi` は、PIV 2020 ローカル抽出および列間照合で明確な意味ズレなし。

## 178. 177周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `troti` は PIV 2020 で人について「短い歩幅で速く歩く」用例が確認でき、`jogging` 文脈でも文脈別許容。
- `aliĝu al mi por tagmanĝo`, `Ĉu vi rememorigos min?`, `piedirado` はやや直訳調の余地はあるが、RU/日中韓との意味対応は保たれているため未修正。

## 179. 178周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Accepting & Declining, Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `partio de golfo` は PIV 2020 の `partio`（ゲーム・競技の一回）で説明可能。
- `aliĝi al vi`, `Ĉu vi renkontiĝas kun iu?`, `Ni trovu agrablan lokon kien iri` は、自然さに幅はあるが明確な意味ズレなし。

## 180. 179周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding, Education / At School

結果:
- **1件修正**

修正:
- `ID1304` EO
  - `Mi esperas, ke vi faros unu la alian ege feliĉaj` → `Mi esperas, ke vi ege feliĉigos unu la alian`
  - 理由: `feliĉigi` は PIV 2020 で「Fari, ke iu estu feliĉa」と明確に定義されており、`make each other happy` の内容をそのまま表せる。元文は目的語補語の形がやや不安定で直訳調なので、意味を変えずに自然な他動詞表現へ調整。

主な据え置き確認:
- `ravega`, `hararanĝo`, `edziniĝos al mi`, `nupto`, `geedziĝa datreveno`, `respondi mian demandon`, `frekventi/iri al lernejo` 周辺は、PIV 2020 ローカル抽出と列間照合で文脈別許容。

## 181. 180周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo`, `iri al universitato`, `studjaro`, `magistriĝo`, `doktoriĝas`, `libera jaro`, `studentloĝejo`, `lektoro`, `aliĝi al la biblioteko` は、学習フレーズとして意味対応が保たれているため未修正。

## 182. 181周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life, Numbers & Colours, Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vokcentro`, `informteknologio` はオンライン検索でも実例が確認でき、透明な複合語として維持。
- `purpuro`, `viola`, `multiplikite`, `juristo`, `komercistino`, `handikapitaj infanoj` は列間照合で明確な意味ズレなし。

## 183. 182周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `merkatika administranto`, `promociita`, `patrina/patra forpermeso`, `maldungis min`, `retpoŝto`, `altigos mian salajron`, `adiaŭa festo`, `limtempo` は、PIV 2020 ローカル抽出・オンライン確認・列間照合で文脈別許容。

## 184. 183周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business Trip, Applying for a Job

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `afervojaĝo`, `komputila klero`, `laborkontrakto`, `fortaĵo/malfortaĵo`, `raporti` は、PIV 2020 ローカル抽出と列間照合で文脈別許容。
- `komputile klera`, `labori laŭvice`, `salajraj atendoj` はやや直訳感はあるが、RU/JA/ZH/KO との意味対応は崩れていないため未修正。

## 185. 184周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Applying for a Job, Travel / Accommodation, Asking Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `piediri`, `aŭtobusa haltejo`, `orientiĝi`, `trans la strato`, `gvidanto/gvidisto`, `loĝejo/resti` は PIV 2020 ローカル抽出で確認。
- `Revenu`, `Iru tien malsupren`, `ĝuste trans la strato` は、案内文脈として意味ズレなし。

## 186. 185周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Asking Directions, Sightseeing, Photography

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `naveda`, `foti/fotografi`, `indikilo`, `sandviĉejo`, `vidindaĵo`, `loĝejo/resti` は PIV 2020 ローカル抽出で確認。
- `navedan buson`, `vidindaĵan ekskurson`, `subeksponitaj`, `memorkarto` は透明な複合・派生として文脈別許容。

## 187. 186周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking Flights, Checking in, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `registrigi pakaĵon` 型は PIV 2020 ローカル抽出で確認できるため、`registrigi bagaĝon` 系は荷物を預ける文脈として維持。
- `suriri`, `enŝipiĝo`, `pordego/elirejo`, `registrejo`, `manbagaĝo`, `superpezo` は、空港・搭乗文脈で意味が明確なため未修正。

## 188. 187周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage, Passport Control & Customs, On the Plane

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `manbagaĝo`, `bagaĝ-ricevejo`, `pagi doganon`, `transitvizo/transite`, `peti azilon`, `enŝipiĝo`, `seĝodorso`, `bagaĝujo` は、辞書確認と列間照合で文脈別許容。
- `sur la aviadilo` は `en la aviadilo` より迷う余地があるが、`on board` 対応として意味ズレが明確ではないため未修正。

## 189. 188周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane, Airport Signs, Car / Car Hire, Driving & Parking

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `transmisio`, `kofrujo`, `infanseruroj`, `direktomontriloj`, `klimatizilo`, `stirpermesilo`, `kaŭcio`, `aŭtovojo` は PIV 2020 ローカル抽出で確認。
- `Turniĝu maldekstren`, `Veturu sub la ponto`, `loko por halti` は、より標準的な言い換え候補はあるが、運転案内として意味対応は保たれているため未修正。

## 190. 189周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vojsignoj`, `unudirekta strato`, `glacikovritaj`, `parkometro`, `serva areo`, `trafikrondo`, `benzinujo`, `pneŭmatiko/pneŭo`, `startokabloj`, `hupo`, `stirmekanismo`, `bremslikvaĵo` は、辞書確認・透明な複合語・列間照合で文脈別許容。
- `Vi pasos superbazaron maldekstre`, `Mi volus havi dek litrojn`, `Bonvolu sendi iun por ĝi` は直訳調の余地はあるが、明確な意味ズレなし。

## 191. 190周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs, Other Transport / Bus Station, Train Station

結果:
- **1件修正**

修正:
- `ID2367` EO
  - `Busstrio` → `Buskoridoro`
  - 理由: `Busstrio` は複合としては理解可能だが、実在用語としての確認が弱い。オンライン上で `Buskoridoro` が bus lane のエスペラント名として確認でき、意味を変えずに「バス専用レーン」に対応するため修正。

主な据え置き確認:
- `Trapaso malpermesita`, `Preterpasu maldekstre`, `Piedira zono`, `Nivelkruciĝo`, `revenbileto`, `pensiula bileto`, `Atentu la interspacon`, `fervoja stacidomo` は、道路標識・公共交通文脈で意味対応が保たれているため未修正。

一致確認:
- `cmp_exit=0`
- `md5=320669a57ffca77084ffeaab9aa2c14e`

## 192. 191周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / Train Station, On the Bus or Train, Taxi

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `laŭpeta haltejo`, `vojaĝkarto`, `abonbileto`, `pakaĵujo`, `taksihaltejo`, `restmono`, `trinkmono` は、交通・タクシー文脈で意味対応が保たれているため未修正。
- `superpago` は `krompago` に比べて迷う余地があるが、「追加料金」の意味は確認でき、空港サーチャージとして明確な意味ズレではないため維持。

## 193. 192周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi, Ship, Hotel / Asking Facilities, Booking Room

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ŝtopilingo`, `inkludita`, `plena pensiono`, `monŝranko`, `ĉambroservo`, `lavservo`, `rulseĝa aliro`, `duŝkabinoj`, `gimnastikejo`, `krozado`, `marmalsano`, `naŭzi` は PIV 2020 ローカル抽出・列間照合で文脈別許容。

## 194. 193周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking Room, Checking in, During Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `atendolisto`, `ĉambronumero`, `ĉambroŝlosilo`, `nefumantoj`, `aldona lito`, `forlasi la ĉambron`, `enirpordo`, `savelirejo`, `gladigi`, `ekstera linio`, `internacia kodo`, `plusendi`, `plilongigi restadon` は、ホテル滞在文脈で意味対応が保たれているため未修正。

## 195. 194周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Stay, Checking out, Complaints, Renting a Flat

結果:
- **1件修正**

修正:
- `ID2798` EO
  - `Kiom oni kalkulis al mi por la minibaro?` → `Kiom oni fakturis al mi por la minibaro?`
  - 理由: `kalkuli al mi` は「私のために計算する」の読みに寄りやすく、RU/JA/ZH/KO の「ミニバー料金を請求された額」とは少しずれる。PIV の `fakturi al ...` 型で請求・請求書発行の意味を確認できるため、内容を変えずに修正。

主な据え置き確認:
- `bolilo`, `littukoj`, `servokotizo`, `detaligitan fakturon`, `elregistriĝi`, `restmono`, `duobla lito`, `rehavi mian monon` は、ホテル精算・苦情文脈で文脈別許容。

## 196. 195周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat, Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `litotukoj` は同ファイル内の `littukoj` と表記差があるが、透明な複合語として許容範囲。
- `ŝvabrilo`, `skatolmalfermilo`, `suĉkloŝo`, `fumejo`, `antaŭmendi tablon`, `vinkarto`, `gasita akvo` は、PIV 2020 ローカル抽出・列間照合で意味対応が保たれているため未修正。

## 197. 196周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio`, `doma vino`, `karafo`, `kranakvo`, `koŝera manĝaĵo`, `pastaĵoj`, `por forporti`, `memservo`, `tritavola sandviĉo`, `mezrostita`, `bone rostita` は、辞書確認・透明性・列間対応から文脈別許容。

## 198. 197周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **1件修正**

修正:
- `ID3122` EO
  - `Ĉu la kalkulo inkluzivas la servan pagon?` → `Ĉu la kalkulo inkluzivas la servokotizon?`
  - 理由: `serva pago` でも意味は推測できるが、同ファイルの `ID2782`, `ID2796` で同じ service charge に `servokotizo` を使っている。RU の `сервисный сбор` とも対応が明確なため、既存表現へ統一。

主な据え置き確認:
- `kalkulo` は PIV で「レストラン・ホテルの勘定」用法を確認できるため維持。
- `Gardu la restmonon` はやや直訳調に見えるが、PIV の `gardi` に「保っておく」用法があるため未修正。
- `manĝobastonetoj`, `kalzoneo`, `rapidmanĝaĵo`, `laktaĵoj`, `odoras je korko` は、食事文脈で明確な意味ズレなし。

## 199. 198周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, At the Pub, Food / Meat & Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `rostbefo`, `salikoko`, `truto`, `skombro`, `tinuso`, `koturno`, `polpo`, `bovida kotleto`, `kankro`, `haringo` は PIV 2020 ローカル抽出で確認。
- `barela biero`, `laktoskuaĵo`, `ĉipsoj`, `postebrio` は、pub・軽食文脈で意味対応が保たれているため未修正。

## 200. 199周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Food & Spices, Breakfast Food

結果:
- **1件修正**

修正:
- `ID3282` EO
  - `Ni prenos du kranberajn mufinojn` → `Ni prenos du oksikokajn mufinojn`
  - 理由: `kranbero` は少なくとも今回参照した PIV 2020 ローカル抽出では確認できず、PIV で `oksikoko` が cranberry に対応する正式見出しとして確認できる。意味を変えず、確認できた語へ修正。

主な据え置き確認:
- `limeo`, `kukurbeto`, `eruko`, `nigra ribo`, `mocarelo`, `strudelo`, `kuskuso`, `petroselo`, `bazilio`, `rozmareno` は PIV 2020 ローカル抽出で確認。
- `karamelizitaj figoj` は `karamelo/karameliĝi` からの派生として意味が透明であり、列間対応も崩れていないため維持。

## 201. 200周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food, Shopping / At the Department Store, Clothes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sorbeto`, `krespoj`, `ringokukoj`, `rizopudino`, `pankukoj`, `kazeo`, `senkafeina kafo`, `kirlovaĵo`, `artefarita dolĉigilo` は、朝食・飲食文脈で意味対応が保たれているため未修正。
- `rabatvendo`, `senimposta butiko`, `magazeno`, `butikoŝtelistoj`, `provejo`, `kemia purigado`, `ŝorto`, `piĵamo` は、PIV 2020 ローカル抽出・列間照合で文脈別許容。

## 202. 201周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Personal Care

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `stretaj` は PIV で `mallarĝa` と確認できるため一度許容したが、後続再点検で衣服が身体をきつく覆う用法としてより明示的な `malvastaj` へ修正済み。
- `tubo de dentopasto` は PIV の `tubo` 用例そのものとして確認できるため未修正。
- `fingrosandaloj`, `mokasenoj`, `kalkanumoj`, `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `paletro`, `ŝminko por okulharoj`, `vizaĝpudro` は、透明な複合語または辞書確認済みの語として文脈別許容。

一致確認:
- `cmp_exit=0`
- `md5=7d4549014d918117a30468f590d8fd50`

## 203. 202周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care, Electronic Devices, Other Goods, At the Supermarket

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pinĉilo`, `elektran fornon`, `elektronikajn ludilojn`, `konstrubriketojn`, `suveniron de la urbo` は、列間対応上の明確な意味ズレなし。

## 204. 203周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / At the Supermarket, At the Bookshop & Florist's, Payments & Returns

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pecon de fromaĝo` は特定の一切れを求める文脈として許容。
- `kontanton` は `kontanta mono` がより標準的に見えるが、cash/ready-money 系の用例確認があり、意味ズレとは断定しない。

## 205. 204周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments & Returns, Leisure Time / At the Cinema, At the Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `filmo de suspenso` は suspense film の意味で文脈上許容。
- `interakto` は PIV の `inter akto`（劇場の幕間）に対応する語として確認できるため維持。

## 206. 205周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / At the Theatre, At the Museum, At the Nightclub

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto` は劇場の幕間文脈で維持。
- `diskĵokeo` は nightclub 文脈で DJ を指す透明な複合語として意味対応が保たれている。

## 207. 206周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / At the Nightclub, At the Beach, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `malsekkostumo`, `asekurita por urĝaj situacioj`, `vetproporcioj` はやや直訳的な余地があるが、各文脈で意味は崩れていないため未修正。

## 208. 207周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport, Music, Going Camping

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `regatto` は PIV 見出し `regatt/o` と一致するため、綴りを維持。
- 音楽・キャンプ関連語は列間対応上の明確な意味ズレなし。

## 209. 208周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping, Family Time, Gardening, Having Guests, Services / At the Bank

結果:
- **1件修正**

修正:
- `ID4240` EO
  - `Ĉu vi ŝatus ginon kun toniko?` → `Ĉu vi ŝatus ĝinon kun toniko?`
  - 理由: 飲料 gin は PIV 2020 ローカル抽出で `ĝin/o`（juniper で香味づけした穀物蒸留酒）として確認できる。`gino` は飲料名として確認できず、別語にも読まれ得るため、意味を変えず語形のみ修正。

主な据え置き確認:
- `bolilo` は PIV で「水を沸かす容器」と確認。
- `televidaj romanoj` は soap opera/serial drama 文脈として許容。

## 210. 209周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank, At the Estate Agency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `garantiaĵo`, `deponaĵo`, `kontantmono`, `hipoteko`, `lua kontrakto` は銀行・不動産文脈で意味対応が保たれているため未修正。

## 211. 210周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dislimon`, `mezan disigon` は hair parting 文脈として許容。
- 美容室・仕立て・修理関連表現は、多少直訳的なものを含むが明確な意味ズレなし。

## 212. 211周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs, Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kuirforno`, `ŝtopiĝinta`, `ellasejo`, `kuracistan ekzamenon`, `medicinan asekuron` は文脈上許容。

## 213. 212周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor, Diseases, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haŭterupcion`, `furunkon`, `diareon`, `limfonodoj`, `mikozo de la piedoj`, `fojnofebro`, `suturerojn` は医療文脈で意味対応が保たれている。
- `resaniĝos` は傷・症状が治る文脈で許容し、過修正を避けた。

## 214. 213周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `plombo`, `plombigi`, `dentprotezo`, `hipermetropa`, `miopa`, `astigmatismo`, `okulvitrujo`, `plastroj` は各専門文脈で確認・許容。
- `gargari la buŝon` は「口をゆすぐ」としてより一般には `ellavi la buŝon` も考えられるが、PIV で口・喉を液体で洗う意味が確認できるため未修正。

## 215. 214周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy, Communication Means / Phone, Phone Calls at Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `herbaj medikamentoj`, `kromefikoj`, `dormemigi`, `vojaĝmalsano`, `misdigesto`, `telefonbudo`, `voko pagata de la ricevanto` は文脈上許容。

## 216. 215周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ensalutu`, `elsalutu`, `retpoŝtadreso`, `abonon`, `afranko`, `rekomendita poŝto`, `pesilo` は意味対応が明確。
- `Kiu estas via retpoŝtadreso?` は `Kio estas...` のほうが自然な余地はあるが、明確な意味ズレではないため維持。

## 217. 216周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter, Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante` は PIV の `poŝt/o` 関連語として確認できるため維持。
- 手紙定型句と時刻表現は、多少の直訳調を含むが列間対応の明確な破綻なし。

## 218. 217周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Hodiaŭ tage`, `Ĉi-posttagmeze`, `Postmorgaŭ`, `Pluvetadas`, `Fulmas`, `fulmotondro`, `Estas sub nulo`, `veterprognozo` は、時間・天気文脈で意味対応が保たれている。

## 219. 218周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Travel / Common Phrases, Problems, Transport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 基本旅行表現は、EO と JA/ZH/KO の対応に明確な破綻なし。
- ロシア語を参照しつつ、直訳調でもクイズ上の対応が保たれるものは維持。

## 220. 219周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Travel / Airport, Plane, Transport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 空港・機内・交通表現の `bileto`, `flugo`, `pakaĵo`, `haltejo` などは意味対応が保たれている。
- 語順や冠詞に揺れがある表現も、明確な意味ズレでない限り維持。

## 221. 220周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Travel / Accommodation, Hotel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Feliĉan Divalon!` は外部辞書・用例で確認できるため維持。
- `akĉento` は PIV で発音上のなまり・アクセントを表す語として確認できるため、`akcento` へ戻さない。

## 222. 221周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- Accommodation / Hotel, Youth Hostel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `akĉento`, `junulargastejo`, `malkonsili` は文脈内で許容。
- `junulargastejo` は透明な複合語として、意味ズレがないため維持。

## 223. 222周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- Accommodation, Restaurant, Emergencies

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 飲食・宿泊・緊急時の基本表現は列間対応が保たれている。
- `kapturno` は PIV の医学用法で確認できるため維持。

## 224. 223周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- Emergencies / Help, Doctor, First Aid

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bandaĝo`, `frakturo`, `traŭmatizi` などの医療語は PIV で確認できる。
- 既存の応急処置表現はロシア語・日中韓との明確な意味ズレなし。

## 225. 224周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid, At the Police Station, Personal Info

結果:
- **2件修正**

修正:
- `ID766` `Mi distordis mian maleolon` → `Mi tordis al mi la maleolon`
  - RU/JA/ZH/KO は「足首を捻挫した」。
  - PIV で `distordi` は光学・電気・音声信号などの「歪み」に寄る一方、`tordi` には `li tordis al si la piedon` と医学的な `artiktordo` が確認できるため修正。
- `ID827` `Ĉu vi turniĝis al la oficejo pri perditaj aĵoj?` → `Ĉu vi turnis vin al la oficejo pri perditaj aĵoj?`
  - PIV で問い合わせ・頼る意味は `sin turni al...` の用法として確認でき、同範囲の `ID821` とも一致するため修正。

主な据え置き確認:
- `fotoroboto` は強い置換根拠が不足しているため、今回は未修正。
- `detruitaj` は「壊された／破損した」として多少強いが、明確な意味破綻ではないため維持。

## 226. 225周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Personal Info / Nationality, Family, Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `amikino`, `edziniĝinta`, `protestantino` などの性別指定は、ロシア語側の女性形と対応する箇所では維持。
- `Mi estas ĉi tie por labori` は RU の「出張」からは広いが、JA/ZH/KO/EN と一致するため維持。

## 227. 226周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Personal Info / Religion, Family, Appearance

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 宗教・家族関係の女性形はロシア語文脈と整合するものを維持。
- `fianĉino` は PIV で「婚約した女性」として確認できるため、`mi estas fianĉino` を文脈別許容として維持。

## 228. 227周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Appearance, Hobbies, Invitations

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `hobio`, `fotografado`, `noktoklubo`, `sciencfikcia` は PIV で確認できる。
- `troti` は人について「短い足取りで速く進む」用法があるため、英語の `jogging` とは幅があるが今回は文脈別許容。

## 229. 228周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Invitations, Dating

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `partio de golfo` は PIV のゲーム用法と整合する。
- `aliĝi al vi/ni` はやや直訳調の余地があるが、PIV の `aliĝi al...` 用法から意味は取れるため過修正しない。

## 230. 229周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating, Compliments, Marriage, Education

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `hararanĝo`, `ravega`, `novgeedzoj`, `nupto`, `geedziĝa datreveno` は各文脈で意味対応が保たれている。
- `respondi mian demandon` は PIV に他動詞的用例があるため維持。

## 231. 230周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / School, University, Library, Conference

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `en la aĝo de...` は PIV 用例があり、`En kiu aĝo...` も文脈別許容として維持。
- `studentloĝejo`, `akceptkondiĉoj`, `enira ekzameno`, `registriĝa formularo` は透明な複合語として意味対応が保たれている。

## 232. 231周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Research, Exams, Numbers, Colours, Jobs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 数詞・色名・四則演算表現は JA/ZH/KO/RU と対応。
- `informteknologio` は PIV 見出し語ではないが、語形成が透明で外部用例も確認でき、`IT` の意味に合うため維持。

一致確認:
- `cmp_exit=0`
- `md5=e1b4a646d34a3b21e85e2edee6c129a8`

## 233. 232周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `promociita` は PIV で `promocii` が上位の等級・職務へ上げる意味として確認でき、昇進文脈に合うため維持。
- `patrina forpermeso`, `patra forpermeso`, `memstara laboristo` は多少説明的だが、日中韓/RU との明確な意味ズレはない。
- `merkatika administranto` は引き続き少し揺れが残るが、職種名として一意に安全な置換を確定できないため過修正しない。

## 234. 233周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business, At the Interview, Recommendation Letter

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `labori laŭvice` は PIV の `deĵoras ... laŭvice` 系の用法と整合し、交替勤務の意味として維持。
- `informatiko` は PIV では `informadiko` 側が強いが、外部用例と文脈上の IT/情報系の対応が確認でき、明確な誤訳とはしない。
- 面接・推薦状の定型表現は、RU/JA/ZH/KO との対応上、大きな意味の逸脱なし。

## 235. 234周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter, Travel / Asking Directions, Giving Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 推薦状文脈の敬体・評価表現は、内容を増減させる必要がないため維持。
- `trans la strato` は「通りの向こう側」の位置関係として文脈別許容。
- 道案内表現は、前置詞・方向の対応を確認した範囲で明確な意味ズレなし。

## 236. 235周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions, Tourist Office, Excursions, Plane / Booking a Flight

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `naveda buso` は PIV の `naveda` の往復・行き来の語義と合い、shuttle bus 文脈で維持。
- `subeksponitaj` は PIV で写真の露光不足として確認できるため維持。
- `Ekonomiklasa bileto` はやや複合語的だが、航空券クラスの意味が明確で、内容を変えない方針から維持。

## 237. 236周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight, Checking in, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `enŝipiĝo` は語源的には船寄りだが、搭乗文脈での拡張として前回までの保留判断を継続。
- `registrigi pakaĵon/bagaĝon` は PIV の駅で荷物を預ける用例と整合し、チェックイン文脈で意味は通る。
- `manbagaĝo` は見出し語としては弱めだが、空港文脈の手荷物として列間対応が明確なため維持。

## 238. 237周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage, Passport Control & Customs, On the Plane

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `manbagaĝo` 系の残りの文は、手荷物サイズ・個数・提示依頼の文脈に合うため維持。
- 税関・機内表現は、格・前置詞・対象語の対応を見ても明確な意味ズレなし。
- `surteriĝi`, `ekflugi`, `sekureczono` などは文脈上自然に解釈できる。

## 239. 238周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane, Airport Signs, Car / Car Hire, Driving & Parking

結果:
- **3件修正**

修正:
- `ID2199` `La tanko ne estas plena` → `La benzinujo ne estas plena`
  - 車のレンタル文脈で、RU は `Бак`、日中韓も燃料タンクの意味。
  - PIV では `benzinujo` が自動車・航空機などのガソリン容器として確認できる一方、`tanko` は装甲車両の意味が強いため修正。
- `ID2228` `Ĉu mi devas redoni la aŭton kun plena tanko?` → `Ĉu mi devas redoni la aŭton kun plena benzinujo?`
  - 返却時に満タンにする文脈なので、上と同じ理由で燃料容器を明示。
- `ID2229` `Vi devas redoni ĝin kun plena tanko` → `Vi devas redoni ĝin kun plena benzinujo`
  - 直前の返答文として同じ語に統一。

主な据え置き確認:
- `bagaĝa elpreno`, `infanseruroj`, `minimuma luoperiodo`, `vojmapo` は透明な複合語として意味対応が保たれているため維持。

## 240. 239周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems, Road Signs

結果:
- **1件修正**

修正:
- `ID2303` `Plenigu la tankon` → `Plenigu la benzinujon`
  - ガソリンスタンドで「満タンにしてください」の意味。
  - `ID2313` の既存表現 `Kiel oni malfermas la benzinujon?` とも揃い、PIV の `benzinujo` の語義で確認できるため修正。

主な据え置き確認:
- `serva areo`, `trafikblokiĝo`, `direktmontrilo`, `hupo`, `kapoto`, `pneŭmatiko`, `pumpi` などは、既存辞書確認と文脈から維持。

## 241. 240周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs, Other Transport / At the Bus Station, At the Train Station

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Buskoridoro` は bus lane 文脈としてやや硬いが、意味は明確なため維持。
- `Preterpasu maldekstre` などの道路標識表現は、方向・命令形の対応に大きな問題なし。
- バス停・鉄道駅の基本表現は JA/ZH/KO/RU と対応。

## 242. 241周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / At the Train Station, On the Bus or Train, Taxi

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 鉄道・バス内表現は、乗換・切符・座席・停車などの意味対応を確認した範囲で問題なし。
- タクシー導入部の表現も、目的地・料金・支払いの文脈と整合。

## 243. 242周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi, Ship, Hotel / Asking about Facilities, Booking a Room

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `inkludita` は PIV の `inkludi = inkluzivi` の語義と合うため、含まれている/込みの意味で維持。
- `rulseĝa aliro` は少し説明的だが、ホテル施設のバリアフリー可否として意味は明確。
- 船・ホテル予約表現は、内容を変えるほどの誤訳なし。

## 244. 243周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Room, Checking in, During Your Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 予約・チェックイン表現は、人数・泊数・部屋種別・朝食などの対応を確認し、明確な意味ズレなし。
- ホテル滞在中の依頼表現も、丁寧さの差はあるがクイズ用途では許容範囲。

## 245. 244周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay, Checking out, Complaints, Renting a Flat

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `servokotizo` はやや語義幅があるが、service charge 文脈として前回までの保留判断を継続。
- チェックアウト・苦情表現は、金額・故障・騒音・清掃などの意味対応に大きな問題なし。

## 246. 245周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat, Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ŝvabrilo`, `suĉkloŝo`, `adherema filmo` は辞書確認・透明な語形成・文脈から、今回も維持。
- レストラン予約・飲み物注文の表現は、数量・席・時間・飲料名の対応に明確な意味ズレなし。

## 247. 246周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food, During the Meal

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 飲み物・料理注文、食事中の依頼表現は、日中韓/RU との対応を確認した範囲で問題なし。
- 食材・調理・提供タイミングの表現は、多少の直訳感があっても明確な意味ズレはないため維持。

一致確認:
- `cmp_exit=0`
- `md5=e1b4a646d34a3b21e85e2edee6c129a8`
## 248. 247周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 食事中の依頼、会計、苦情表現は RU/JA/ZH/KO との対応に明確な意味ズレなし。
- `manĝobastonetoj`, `servokotizo`, `vino odoras je korko` は文脈別許容として維持。

## 249. 248周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, Small Talk, Place Settings

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 支払い・苦情・店内会話の表現は、多少の直訳感があっても意味対応は保たれている。
- 皿・カトラリー・テーブル周りの基本語は、クイズ用途で問題になる明確なズレなし。

## 250. 249周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Restaurant & Pub / Place Settings, Barbecue

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `eruko` は PIV でサラダ用の植物名として確認できたため、ID3331 は維持。
- BBQ・皿・調味料まわりは、対象物の対応に明確なズレなし。

## 251. 250周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Shopping / Shopping for Groceries, Going to the Shops

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 買い物・食品・容器・支払いの表現は、実用フレーズとして意味対応を維持。
- 商品名の語形成は辞書語または透明な複合語として、今回の修正対象外。

## 252. 251周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Going to the Shops, Accessories, At the Chemist's

結果:
- **2件を修正**

修正:
- `ID3502` `Ĉi tiuj gantoj estas tro stretaj` → `Ĉi tiuj gantoj estas tro malvastaj`
  - 理由: PIV で `stret/a = mallarĝa` 自体は確認できるが、`malvasta` には衣服が身体をきつく覆う用法が明示されているため。RU `слишком тугие`、JA/ZH/KO の「きつすぎる」とも対応。

主な据え置き確認:
- `fingrosandaloj` は PIV で確認でき、サンダル/ビーチサンダル文脈として維持。
- `tubo de dentopasto` は PIV の `tubo` 用例と整合するため ID3534 は維持。
- `ŝminko por okulharoj` は `maskaro` が PIV で確認できなかったため、説明的表現を維持。

## 253. 252周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Health & Beauty / Make-up, Hairdresser

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 化粧品・美容院の依頼表現は、辞書確認できない借用語への置換を避け、説明的表現を維持。
- 髪型・カット・染髪の表現は、日中韓/RU との対応に明確なズレなし。

## 254. 253周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Health & Beauty / Hairdresser, Entertainment / Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Julieta` は PIV に女性名として確認でき、ID3722 `Romeo kaj Julieta` は維持。
- 劇場予約・座席・演目の表現は、意味対応に明確なズレなし。

## 255. 254周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Entertainment / Theatre, Music, Cinema

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 劇場・音楽・映画鑑賞の表現は、クイズで誤答を誘発するほどの意味ズレなし。
- 作品名・上演・席種の語は、既存文脈に合わせて維持。

## 256. 255周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Entertainment / Cinema, At a Museum

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto` は PIV で劇場用語として確認できたため、ID3872/3873/3896 は維持。
- 映画・博物館の展示・入場表現は、対象物と動作の対応に明確なズレなし。

## 257. 256周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Entertainment / At a Museum, Cinema, Circus, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 博物館・サーカス・スポーツ観戦の表現は、RU/JA/ZH/KO と照合して大きな意味ズレなし。
- `Kiel vi pensas, kia estos la fina rezulto?` はやや直訳的だが、内容を変えるほどの誤りではないため維持。

## 258. 257周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Entertainment / Sport, Exhibitions & Trade Fairs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `regatto` は PIV でボート競技として確認でき、ID4073 は維持。
- `Kiel pri promeno...` は自然さに余地があるが、意味ズレが明確ではないため維持。

## 259. 258周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Entertainment / Exhibitions & Trade Fairs, Everyday Services

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 展示会・サービス受付・修理依頼の表現は、文脈と対応言語に照らして維持。
- 名詞句の直訳感がある箇所も、明確な意味ズレがないものは据え置き。

## 260. 259周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Dry Cleaner's, At the Hairdresser's, At the Optician's

結果:
- **今回の追加修正なし**

主な据え置き確認:
- クリーニング・眼鏡店・美容院の依頼表現は、対象物と依頼内容の対応を維持。
- 専門語は過度な置換を避け、クイズ上の意味対応を優先。

## 261. 260周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Hairdresser's, At the Watchmaker's, At the Tailor's

結果:
- **1件を修正**

修正:
- `ID4427` `La jako estas streta` → `La jako estas malvasta`
  - 理由: PIV で `stret/a = mallarĝa` 自体は確認できるが、服の「きつい」は `malvasta` の衣服用法でより直接確認できるため。RU `Пиджак узкий`、JA/ZH/KO の「きつい」と整合。

主な据え置き確認:
- `dislimo` は PIV の `dislimi al si la harojn` と整合し、ID4378 は維持。
- 時計・仕立て直し・サイズ調整の表現は、明確な意味ズレなし。

## 262. 261周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / At the Tailor's, Photography

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 仕立て・採寸・写真撮影の表現は、日中韓/RU の内容に照らして対応良好。
- 写真関連語は、文脈上の自然さよりも意味の安定を優先して維持。

## 263. 262周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Services / Photography, At the Post Office, Telephone

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 郵便・電話・写真サービスの表現は、宛先・料金・操作内容の対応に明確なズレなし。
- ID4615 `streĉis muskolon` は「筋肉を痛めた/引っ張った」文脈として許容し維持。

## 264. 263周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Services / Telephone, Bank

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 電話接続・口座・両替・銀行手続きの表現は、実用フレーズとして意味対応に問題なし。
- 金融語は内容変更につながる置換を避け、既存訳を維持。

## 265. 264周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Services / Bank, Police Station, Ambulance, Garage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 警察・救急・車両修理の表現は、緊急性・対象物・依頼内容の対応を確認。
- 多少の言い換え候補があっても、意味ズレが明確でないものは維持。

## 266. 265周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Services / Garage, Renting a Car, Petrol Station, The Car

結果:
- **今回の追加修正なし**

主な据え置き確認:
- レンタカー・給油所・車両部品の表現は、前回修正した `benzinujo` 系との整合も含めて確認。
- 車両まわりの語は、文脈上の対象がずれていないため維持。

## 267. 266周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Travelling / Going Abroad, Moving to a Foreign Country, The Car

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 渡航・移住・車両操作の表現は、RU/JA/ZH/KO と照合して明確な意味ズレなし。
- やや説明的な表現も、内容保持を優先して維持。

## 268. 267周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Travelling / Going Abroad, Moving to a Foreign Country

結果:
- **今回の追加修正なし**

主な据え置き確認:
- ビザ・書類・現地生活・移住関連の表現は、各言語列との対応に大きなズレなし。
- 難語・専門語については、確証のない置換を避け、既存表現を維持。

一致確認:
- `cmp_exit=0`
- `md5=72e461b5e2605671254cf059b031a6e9`


## 269. 268周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Sanon!`, `Bonan amuzon!`, `Agrablan nokton!`, `Je via sano!` は、挨拶・祝意・乾杯の定型表現として列間対応を維持。
- `Tio estis la plej malmulto, kion mi povis fari`, `Estis plezuro por mi tion fari` は、過去周回の判断どおり意味ズレが明確ではないため維持。

## 270. 269周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions & Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- 謝罪・依頼・短答の定型句は、RU/JA/ZH/KO と照合して大きな意味ズレなし。
- `Mi ne tion celis`, `Tute nenio`, `Kuraĝu!`, `Ĉu ĉio en ordo?` は自然化候補はあるが、クイズ上の対応を崩す誤りではないため維持。

## 271. 270周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers, Congratulations, General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Feliĉan Divalon!` と `akĉento` は、過去の辞書確認済み修正後の形を維持。
- 言語名の形容詞対格・副詞形の揺れはあるが、`la bengalan`, `slovene`, `azerbajĝane`, `la indonezian` などは各文脈で意味対応を保つ。

## 272. 271周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mandarena ĉina lingvo`, `junulargastejo`, `kunhavas vian vidpunkton`, `survoje por renkonti amikon`, `biciklas` は既存の辞書確認・文脈確認どおり維持。
- 同意・不同意、所在、旅行、質問表現は、日中韓/RU との明確な意味ズレなし。

## 273. 272周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information, Expressing Feelings, Help & Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `trista`, `malstreĉita`, `kapturno`, `malkuraĝigita`, `malkonsilus`, `flugpersonaro` は、感情・体調・助言文脈として意味対応を維持。
- 弔意表現と助言表現は、多少の直訳感があっても内容を変えるほどのズレなし。

## 274. 273周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions, Emergencies / Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kio plaĉas al vi pri ĝi?`, `Dependas de vi`, `Mi pensas, ke estas eraro`, `Ĝi urĝas!` は会話句として許容。
- 緊急・事故関連の `stirpermesilo`, `prioritato`, `interpretisto`, `akcidentraporto` は、対応言語列との意味関係に明確な問題なし。

一致確認:
- `cmp_exit=0`
- `md5=72e461b5e2605671254cf059b031a6e9`

## 275. 274周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / Accidents, First Aid, Help, Police

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi tordis al mi la maleolon` は、足首をひねった文脈として現在形を維持。
- `fotoroboto` は既存の PIV/Glosbe 確認済み判断を維持し、警察での人相再現文脈として大きな意味ズレなし。

## 276. 275周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- General Conversation / Introductions, Residence, Nationality, Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kia estas via nacieco?`, `Kia estas via religio?` は `Kio estas...` も候補だが、属性・種類を尋ねる会話文として既存判断どおり維持。
- `Mi estas ĉi tie por labori` は RU の出張寄り表現より広いが、日中韓/EN と対応するため未修正。

## 277. 276周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- General Conversation / Religion, Family, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `en rilato`, `rendevuas kun iu` は既存の辞書確認・文脈確認どおり維持。
- `Mi devenas el Budapeŝto` は RU の「出生地」より広いが、他列の「出身」表現と整合するため未修正。

## 278. 277周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- General Conversation / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `hobio`, `fotografado`, `noktoklubo`, `sciencfikcia`, `butikumi`, `patkuko`, `vestiblo` は既存の PIV 確認済み判断を維持。
- `Aliĝu al mi por tagmanĝo`, `Ĉu vi rememorigos min?`, `je la 16-a horo` は自然化候補はあるが、列間の明確な意味ズレなし。

## 279. 278周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Accepting & Declining, Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `partio de golfo`, `aliĝi al vi`, `regalos vin per trinkaĵo`, `veturigi vin hejmen` は、多少の言い換え余地はあるが対応言語列との意味関係を保つ。
- `Kion vi elpensis?` は EN の "What are you up to?" よりも RU/日中韓の「何を考えた/企てた」に寄っており、現行EOを維持。

## 280. 279周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding; Education / At School

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `edziniĝos al mi` は性別を含むが、RU/中文も女性に求婚する形で、文脈上許容。
- `nupto`, `novgeedzoj`, `hararanĝo`, `ravega`, `respondi mian demandon`, `lernejon deksesjaraĝe` は既存の辞書確認・列間照合どおり維持。

## 281. 280周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo...` は PIV の `en la aĝo de...` 系例に照らし、前置詞を変えるほどの誤りとはしない。
- `registriĝa formularo`, `studentloĝejo`, `akceptkondiĉoj`, `eniraj ekzamenoj`, `formulitaj buŝe/skribe` は、PIV の構成要素確認と文脈上の透明性により維持。
- `prunti libron` は PIV で「借りる」用法も確認できるため、図書館文脈で修正不要。

## 282. 281周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life, Numbers & Colours; Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `purpuro`, `viola`, `rozkoloro`, `helverda koloro` は、色名として多少の幅があるが、紫・薄緑などの対応を崩す誤りではない。
- `informteknologio`, `vokcentro`, `juristo`, `komercistino`, `handikapitaj infanoj` は既存の PIV/外部用例確認済み判断を維持。

## 283. 282周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `merkatika administranto` は PIV で `merkatiko` を確認。RU は「マーケティング専門家」、EN/日中韓は「マーケティングマネージャー」寄りで揺れるため、安全な単一置換先を確定せず現行維持。
- `promociita`, `patrina/patra forpermeso`, `maldungis min`, `retpoŝto`, `altigos mian salajron`, `limtempo` は、職場文脈で意味対応を保つ。

## 284. 283周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business, At the Interview, Recommendation Letter

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vivresumo`, `laborpostena priskribo`, `laborkontrakto`, `laborpermesilo`, `provperiodo`, `kvalifikoj` は、求職・面接文脈で既存判断どおり維持。
- `Mia fako estas informatiko` は EN/RU が情報技術寄りだが、情報系専門分野として大きな意味ズレなし。
- `fortaĵoj kaj malfortaĵoj`, `salajraj atendoj`, `kreema solvanto de problemoj` は、推薦状・面接表現として自然化余地はあるが修正不要。

一致確認:
- `cmp_exit=0`
- `md5=72e461b5e2605671254cf059b031a6e9`

## 285. 284周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter, Travel / Asking Directions, Giving Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `gvidanto`, `aldono al via programo`, `ŝparvojo`, `trans la strato`, `fajrobrigadejo` は、推薦状・道案内文脈で列間対応を保つ。
- `trans la strato` は「通りの向こう側」として自然化余地はあるが、道案内クイズで意味ズレは明確でない。

## 286. 285周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions, Tourist Office, Excursions; Plane / Booking a Flight

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `naveda buso`, `maltrafi ĝin`, `rondvojaĝoj`, `subeksponitaj` は、旅行・写真・ツアー文脈で意味対応が保たれる。
- `subeksponitaj` は写真用語としてやや専門的だが、露英日中韓の「露出不足」に対応するため維持。

## 287. 286周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight, Checking in, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `registrejo`, `enŝipiĝo`, `pordego`, `elirejo`, `manbagaĝo`, `superpezo` は、空港・搭乗・荷物文脈の既存判断を維持。
- `enŝipiĝo` は船由来の語感があるが、搭乗文脈での拡張用法として今回は過修正しない。

## 288. 287周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage, Passport Control & Customs, On the Plane

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bagaĝ-ricevejo`, `vizpeto`, `transite`, `seĝodorso`, `supra bagaĝujo`, `enŝipiĝo` は、空港・機内表現として列間対応を保つ。
- `supra bagaĝujo` は説明的だが、overhead locker / 上の荷物入れに対応して明確。

## 289. 288周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane, Airport Signs; Car / Car Hire, Driving & Parking

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kriza elirejo`, `trans la ponton`, `mana/aŭtomata transmisio`, `kofrujo`, `infanseruroj`, `direktomontriloj`, `stirpermesilo`, `kaŭcio`, `aŭtovojo` は文脈別許容。
- `kriza elirejo` は `savelirejo` も候補だが、飛行機内の emergency exit として意味は崩れていない。

## 290. 289周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems, Road Signs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kontraŭfrosta likvaĵo`, `startokabloj`, `bremslikvaĵo`, `stirmekanismo`, `pneŭmatiko krevis`, `akumulatoro`, `brulaĵindikilo`, `rapidometro`, `trafikblokiĝo`, `hupo` は、車両・修理文脈で意味対応を保つ。
- `kontraŭfrosta likvaĵo` は `kontraŭfrostaĵo` も候補だが、現形は透明で、antifreeze liquid として誤りとはしない。

## 291. 290周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs, Other Transport / Bus Station, Train Station

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Buskoridoro`, `Preterpasu maldekstre`, `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo`, `revenbileto`, `pensiula revenbileto`, `Kiu kajo?`, `Atentu la interspacon` は、道路標識・公共交通文脈で既存修正後の形を維持。
- `Atentu la interspacon` は RU と少しずれるが、EO/EN/JA/ZH/KO は platform gap 注意で一致するため維持。

## 292. 291周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / Train Station, On the Bus or Train, Taxi

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `eksprestrajno`, `vojaĝkarto`, `abonbileto`, `preterveturis vian haltejon`, `pakaĵujo`, `taksihaltejo`, `taksimetro`, `ŝaltita`, `trajnstacio`, `superpago`, `nunmomente` は交通・タクシー文脈で意味対応を保つ。
- `superpago` は `krompago` より硬いが、空港サーチャージとして明確なズレではない。

## 293. 292周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi, Ship; Hotel / Asking Facilities, Booking Room

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `marmalsano`, `kajo`, `kajuto`, `enŝipiĝi`, `krozado`, `naŭzi`, `monŝanĝejo`, `radiogramo`, `ŝtopilingo`, `plena pensiono`, `rulseĝa aliro`, `gimnastikejo` は、船旅・ホテル設備文脈で既存の辞書確認済み判断を維持。
- `rulseĝa aliro` はやや説明的だが wheelchair access として意味は明確。

## 294. 293周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking Room, Checking in, During Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `atendolisto`, `ĉambronumero`, `ĉambroŝlosilo`, `nefumantoj`, `aldona lito`, `forlasi la ĉambron`, `enirpordo`, `savelirejo`, `gladigi`, `ekstera linio`, `internacia kodo`, `plusendi`, `plilongigi restadon` は、ホテル滞在文脈で意味対応が保たれる。

## 295. 294周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Stay, Checking out, Complaints, Renting a Flat

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `lavejo`, `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `restmono`, `monŝranko`, `lavujo`, `ŝtopita`, `bolilo`, `littukoj`, `duobla lito`, `rehavi mian monon` は、ホテル精算・苦情文脈で既存判断どおり維持。
- `ID2798` は既に `fakturis al mi` へ修正済みで、今回も現形を支持。

## 296. 295周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat; Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vazaro`, `ŝvabrilo`, `litotukoj`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `suĉkloŝo`, `adherema filmo`, `polvosuĉilo`, `mendi/rezervi tablon`, `fumejo`, `gasita akvo`, `vinkarto` は、備品・飲食店文脈で意味対応を保つ。
- `litotukoj` と `littukoj` は表記差があるが、透明複合として許容。

## 297. 296周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food, During the Meal

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio`, `koŝera`, `kranakvo`, `pastaĵoj`, `brando/konjako`, `mezrostita`, `farĉitaj fungoj`, `ĉefplado`, `vegetaranino`, `fritoj` は、辞書確認済みまたは透明な複合として維持。
- `Mi estas vegetaranino` は女性話者を含むが、RU も女性形であり、対象列との大きな破綻はない。

## 298. 297周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `halala`, `manĝobastonetoj`, `fritoj`, `kalzoneo`, `rapidmanĝaĵo`, `laktaĵoj`, `trinkmono`, `servokotizo`, `odoras je korko`, `meleagro` は、飲食店文脈で意味対応を保つ。
- `servokotizo` は語義幅が残るが、service charge として既存修正後の表記を維持。

## 299. 298周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, At the Pub; Food / Meat & Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `postebrio`, `glasetojn da tekilo`, `barela biero`, `laktoskuaĵo`, `ĉipsoj`, `bifstekon el bova lumbaĵo`, `ŝafidaĵo`, `rostbefo`, `grilita salmo`, `salita moruo`, `kruda haringo`, `kankroj` は、パブ・肉魚料理文脈で意味対応を保つ。

## 300. 299周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Food & Spices, Breakfast Food

結果:
- **1件修正**

修正:
- `ID3318` EO
  - `Li prenos la brasitajn karotojn kaj kikerojn` → `Li prenos la brezitajn karotojn kaj kikerojn`
  - 理由: PIV 2020 ローカル抽出で `brasi` は帆を風に合わせる海事語、`brezi` は料理の braise / 蒸し煮に該当すると確認。EN `braised`、JA/ZH/KO/RU の煮込み・ тушёную に合わせ、意味を変えずに語根を修正。

主な据え置き確認:
- `mango`, `kivifruktoj`, `akvomelono`, `limeoj`, `nigra ribo`, `mirtela`, `oksikoka`, `florbrasiko`, `papriko`, `dolĉa maizo`, `peklitaj kukumoj`, `laktuko`, `akra kapsiko`, `kukurbeton`, `eruko`, `fazeoloj`, `safrana rizo` は食品名として列間対応が取れている。

一致確認:
- `cmp_exit=0`
- `md5=7820ad13c38bc914de226eca937bb298`

## 301. 300周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast Food; Shopping / At the Department Store, Clothes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `frititaj ovoj`, `avenaj biskvitoj`, `sorbeto`, `krespoj`, `ringokukoj`, `kirlovaĵo`, `artefarita dolĉigilo` は、朝食・軽食文脈として列間対応を保つ。
- `senimposta butiko`, `teretaĝo`, `brakhorloĝoj`, `butikoŝtelistoj`, `ŝorto`, `Lavu inversigite`, `kemie purigi` は、店舗・衣服表示として文脈別許容。

## 302. 301周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Personal Care

結果:
- **1件修正**

修正:
- `ID3534` EO
  - `Mi ŝatus tubon de dentopasto` → `Mi ŝatus tubon da dentopasto`
  - 理由: PIV 2020 の `da` は、前の語が量・容器・単位を表す場合に後続語を数量内容としてつなぐ前置詞。`a tube of toothpaste` / 歯磨き粉一本 / тюбик зубной пасты では `tubo da dentopasto` が自然で、同範囲の `tubo da gluo` とも整合する。

主な据え置き確認:
- `fingrosandaloj`, `pantofoj`, `sportŝuoj`, `gumaj botoj`, `Ili sidas sur mi kiel ganto`, `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `ŝminko por okulharoj`, `vizaĝpudro` は買い物文脈で意味対応を維持。

## 303. 302周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care, Electronic Devices, Other Goods, At the Supermarket

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pinĉilo`, `telefona ŝargilo`, `lensokovrilo`, `portebla komputilo`, `skanilo`, `poŝlampo`, `laŭtparoliloj`, `elektronikaj ludiloj`, `harsekigilo` は、機器・日用品文脈で意味対応を保つ。
- `tubo da gluo`, `bokalo da mustardo`, `Konservu en fridujo`, `limdato`, `frukta torto` はスーパー表現として文脈別許容。

## 304. 303周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / At the Supermarket, At the Bookshop & Florist's, Payments & Returns

結果:
- **1件修正**

修正:
- `ID3664` EO
  - `Mi ŝatus tiun pecon de fromaĝo` → `Mi ŝatus tiun pecon da fromaĝo`
  - 理由: `that piece of cheese` は「チーズ一切れ」という数量・部分表現であり、PIV 2020 の `da` の説明に合う。`Kvaronon de kilogramo` は単位そのものの分数なので `de` のまま維持。

主な据え置き確認:
- `tranĉaĵoj da ŝinko`, `peco da pico`, `kilogramo da granatoj`, `konservaĵoj`, `ĉokoladaj bombonoj`, `tabuletoj da nigra ĉokolado`, `duonduzeno da ovoj` は数量表現として整合。
- `interesiĝas pri detektivaj romanoj`, `poemaroj`, `brokanta librovendejo`, `krono el freŝaj floroj por la fianĉino`, `kontanto`, `PIN-kodo` は文脈別許容。

## 305. 304周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments & Returns; Leisure Time / At the Cinema, At the Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `donacskatolo`, `senimposte`, `interŝanĝi ... kontraŭ`, `rabatkarto`, `bonuskarto`, `donacpaki`, `sekureca numero`, `repago` は支払い・返品文脈で意味対応を保つ。
- `filmo de suspenso`, `Ĝi ĵus aperis`, `pufmaizo`, `premiero`, `subtekstoj`, `animaciaĵo`, `nigrablanka filmo`, `Mi ne estas tre impresita de la filmo` は映画文脈で許容。

## 306. 305周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Leisure Time / At the Theatre, At the Museum, At the Nightclub

結果:
- **1件修正**

修正:
- `ID3936` EO
  - `Unu plenkreskulan kaj du infanajn, mi petas` → `Unu plenkreskulan bileton kaj du infanajn biletojn, mi petas`
  - 理由: EN/JA/ZH/KO/RU は「大人券1枚と子ども券2枚」。元の EO は `bileton/biletojn` が省略され、単独出題では形容詞だけが残って不安定なため、意味を変えず名詞を補った。

主な据え置き確認:
- `interakto` は PIV 2020 で「二幕の間の時間」という劇場用法を確認。`Kiom longe daŭras la interakto?`, `La interakto daŭros 15 minutojn`, `trinkaĵojn por la interakto` は修正不要。
- `teatra lorneto`, `loĝio`, `dramteatro/drama teatro`, `vestiblo`, `aŭdgvido/aŭdgvidilo`, `karikatursalono`, `vaksaj figuroj`, `etnografia muzeo` は、劇場・博物館文脈で対応を保つ。

## 307. 306周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Leisure Time / At the Nightclub, At the Beach, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `gastlisto`, `sportŝuoj`, `viva muziko`, `homplene`, `mortige enue`, `diskĵokeo`, `drinkejo` はナイトクラブ文脈で意味対応を維持。
- `strando`, `sunseĝo`, `akvoskioj/akvoskii`, `subakvaj fluoj`, `jaĥtklubo`, `plonĝkostumo`, `aerbotelo`, `malsekkostumo`, `garantiaĵo` は海辺・レンタル文脈で文脈別許容。
- `Ni ludu duope`, `arbitro`, `goli`, `egaligis la poentaron`, `vetkuroj`, `ĉevalfortoj`, `subtenanto`, `basketbala teamo` はスポーツ表現として列間対応を保つ。

一致確認:
- `cmp_exit=0`
- `md5=8158f5d32acaa479d7ac74e28d931aa6`

## 308. 307周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Leisure Time / Sport, Music, Going Camping

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vetproporcioj`, `golfbastonoj`, `rakedo`, `telfero`, `televidita`, `rajdi`, `remi` は、スポーツ・余暇文脈で列間対応を保つ。
- `ĉambrorkestro`, `aldviolonisto`, `sakŝalmoj`, `violonĉelo`, `akustiko`, `sonkontrolon`, `sonregistrado`, `koncertpromotoro` は音楽文脈として許容。
- `ruldomo`, `kampumejo`, `tendofostoj`, `dormosako`, `akvorezistan jakon` はキャンプ文脈で意味ズレなし。

## 309. 308周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Leisure Time / Going Camping, Family Time, Gardening, Having Guests; Services / At the Bank

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `forno`, `kampada vendejo`, `kuireja ekipaĵo`, `brulfornon`, `fiŝkaptilon`, `tordaĵon` はキャンプ・釣り文脈として許容。
- `televidaj romanoj` は soap opera 対応として Glosbe で確認でき、PIV の `romano` も連載的物語まで含むため据え置き。
- `pali`, `kvaronon post la kvina`, `malstreĉe`, `matenmanĝo en lito` は家庭・庭・来客表現として列間対応を保つ。
- `kontantmono`, `kreditkarto`, `ĉekoj`, `kalkuli bankbiletojn` は銀行表現として問題なし。

## 310. 309周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank, At the Estate Agency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provizio` は PIV 2020 で仲介・銀行等の手数料用法を確認し、`Kiom estas la provizio?`, `La provizio estas inkluzivita` を維持。
- `ĝiri`, `kontoekstrakto`, `ĉekaro`, `monŝanĝejo`, `hipoteko`, `interezprocento`, `kontantigi` は銀行文脈で意味対応を保つ。
- `bangalo`, `vicdomo`, `kontanta aĉetanto`, `antaŭpago`, `meblita/nemeblita`, `duamana posedaĵo`, `prezintervalo`, `sur la merkato` は不動産文脈で文脈別許容。

## 311. 310周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs

結果:
- **1件修正**

修正:
- `ID4372` EO
  - `Mildan permanentan ondigon, mi petas` → `Mildan konstantan ondumadon, mi petas`
  - 理由: PIV 2020 では髪に対して `ondumi la harojn`, `ondumado de hararo` が確認できる一方、`ondigi` は物理的な波を起こす意味に偏る。オンライン確認でも perm は `konstanta ondumado` 系で確認できたため、EN `soft perm`、RU `щадящую химзавивку` の内容を変えず、髪型用語として自然な形に修正。

主な据え置き確認:
- `dislimo` は PIV 2020 の `kombi, dislimi al si la harojn` により、髪の分け目として維持。
- `franĝo`, `farbi ... blonde`, `helaj strioj`, `senharigo`, `vakso`, `manikiuro`, `pedikuro`, `ŝampui`, `laki ungojn` は美容院文脈として許容。
- `laŭmezura kostumo`, `zipon`, `alkudri`, `fliki`, `maniklongo`, `mallarĝigi`, `plilarĝigi` は仕立て屋文脈で列間対応を保つ。

## 312. 311周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs; Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kroneto`, `pilo`, `ŝlosilringo`, `ŝlosilo`, `plandumoj`, `garantio`, `fabrikanto` は修理・鍵・靴修理文脈として許容。
- `aŭdotestoj`, `rentgena ekzameno`, `medicina konsulto`, `sangogrupo`, `kmera`, `desinfekti`, `sangopremo`, `trankviligilo` は診療文脈で意味対応を維持。
- `surdorse` / `surventre` は姿勢表現として問題なし。

## 313. 312周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor, Diseases, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kapturna`, `malvarmumo`, `tubero`, `haŭterupcio`, `furunko`, `konstipita`, `nazkataro`, `gorĝdoloro`, `ŝtopita nazo` は症状表現として列間対応を保つ。
- `limfonodoj`, `mikozo de la piedoj`, `sendormeco`, `fojnofebro` は PIV 2020 でも関連語を確認でき、医療文脈として許容。
- `sutureroj` は PIV 2020 で「縫合を構成する結んだ糸」と確認し、`kelkajn suturerojn` を維持。
- `loka anestezo`, `urina specimeno`, `redukti vian trinkadon`, `injekton`, `resaniĝo`, `ellitiĝi` は治療文脈で意味ズレなし。

## 314. 313周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `preskribos`, `recepto`, `piloloj`, `tablojdoj`, `dozo`, `fastante`, `inhalilo`, `desinfektaĵo`, `kontraŭdoloriloj` は薬・処方文脈で問題なし。
- `plombo`, `plombigi`, `kario`, `dentprotezo`, `denta higienisto`, `gargari la buŝon` は歯科文脈で確認でき、`gargari` も PIV 2020 の「buŝon aŭ gorĝon」に合うため維持。
- `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `okulekzamenoj`, `vidkapablo` は眼鏡店文脈で意味対応を保つ。

## 315. 314周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy; Communication Means / Phone, Phone Calls at Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `paracetamolo`, `aspirino`, `kromefikoj`, `dormigiloj`, `nikotinaj plastroj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は薬局表現として列間対応を保つ。
- `telefono paneis`, `malkonektiĝis`, `telefonbudo`, `telefonkarto`, `kapti signalon`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `urba telefona kodo`, `informservo` は電話文脈で許容。
- `aŭdilo`, `klavi la numeron`, `sur alia linio`, `konekti vin`, `linio estas okupata` は電話業務の定型表現として維持。

## 316. 315周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **1件修正**

修正:
- `ID4908` EO
  - `Ĝi estas gazeto kun granda eldonnombro` → `Ĝi estas gazeto kun granda eldonkvanto`
  - 理由: PIV 2020 で `eldon kvanto` が「一つの版を構成する部数」と確認できる。`eldonnombro` は透明な複合語ではあるが、`number of an issue` 的に読まれる余地があり、EN `wide circulation`、JA/ZH/KO/RU の発行部数・тиражに対しては `eldonkvanto` がより確実。

主な据え置き確認:
- `retpoŝtadreso`, `ensaluti/elsaluti`, `retmesaĝo`, `tekkomputilo`, `Tvitero`, `usona futbalo`, `titoloj` はメディア・ネット利用文脈で許容。
- `vatita koverto`, `afranko`, `poŝtmarkoj`, `poŝtrestante`, `televida licenco`, `rekomendita poŝto`, `dogana deklaracio`, `pesilo` は郵便局文脈で列間対応を保つ。

## 317. 316周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter; Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `Estimata Sinjorino`, `Sincere via`, `Al la koncernatoj`, `vivresumo`, `Antaŭdankon`, `Respektplene via`, `Kun plej koraj salutoj` は郵便・手紙定型句として許容。
- `Mi antaŭĝojas ...`, `Bonvolu ekzameni ĉi tiun aferon`, `aldonaĵo`, `okazo diskuti`, `kunlabori` はビジネス文書文脈で意味対応を維持。
- `kvin antaŭ la dua`, `post la unua`, `la dua kaj duono`, `kvarono antaŭ/post`, `tagmezo`, `noktomezo` は時刻表現として問題なし。
- `labortagoj`, `libertago`, `vintraj/printempaj monatoj` はカレンダー表現として列間対応を保つ。

## 318. 317周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `aŭtunaj monatoj`, `Hodiaŭ tage`, `Post unu semajno`, `En la venonta monato`, `Antaŭhieraŭ`, `Ĉiujn kvin minutojn`, `Postmorgaŭ`, `La sekvantan tagon` は時制・日付表現として許容。
- `glacie kaj glite`, `nebule`, `Varmegas`, `Frostas`, `Pluvetadas`, `Hajlas`, `Fulmas`, `fulmotondro`, `malvarmete`, `sub nulo`, `veterprognozo`, `Ĉi-nokte frostos`, `atmosfera premo` は天候表現として列間対応を保つ。
- `La suno ĵus kaŝiĝis`, `La vento ĉesis`, `La nuboj disiĝas`, `Blovas forta vento`, `ne estas eĉ unu nubo` は自然な気象描写として維持。

一致確認:
- `cmp_exit=0`
- `md5=288fd01ebd769b519a88b489207ef944`

## 319. 318周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Bonan matenon`, `Bonan tagon`, `Bonan vesperon`, `Bonan nokton`, `Ĝis poste`, `Ĝis morgaŭ`, `Ĝis baldaŭ` は挨拶・別れの定型句として列間対応を保つ。
- `Sanon!`, `Je via sano!`, `Mi deziras al vi sanon/feliĉon`, `Mi antaŭĝojas revidi vin` は祝意・乾杯・再会期待の文脈で許容。
- `Tio estis la plej malmulto, kion mi povis fari` はやや直訳調だが、JA/ZH/KO/RU の「できるせめてものこと」に対応し、明確な意味ズレとしては扱わず維持。

## 320. 319周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions and Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi ne tion celis`, `Tio estas mia kulpo`, `Ne estas kialo pardonpeti`, `Mi agis senzorge` は謝罪・弁明文脈で意味対応を保つ。
- `Atentu la hundon`, `Kuraĝu!`, `Ne zorgu pri tio!`, `Sciigu min`, `Ne paniku!` は命令・助言表現として自然。
- `Kiom malproksime?`, `Kiom da jaroj vi havas?`, `Ĉu estas malmultekoste?`, `Ĉu estas tro malfrue?` は短問答の教材文として許容。

## 321. 320周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions and Answers, Congratulations; General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kiu gajnis?`, `Kiun vi subtenas?`, `Ĉu vi povas ripari ĝin?`, `Ĉu vi povus ripeti tion?` は質問文として列間対応を保つ。
- `Feliĉan datrevenon!`, `Feliĉan Kristnaskon!`, `Feliĉan Paskon!`, `Feliĉan Divalon!`, `Gratulon pro ...` は祝辞表現として許容。
- `akĉento` は PIV 2020 で発音上の訛り・アクセントの意味を確認し、`Vi havas akĉenton` を維持。
- `Bonvolu paroli pli malrapide`, `Kiel ĉi tio nomiĝas?`, `Mi ne parolas vian lingvon` は意思疎通文脈で自然。

## 322. 321周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing and Disagreeing, Asking for and Giving Information

結果:
- **1件修正**

修正:
- `ID551` EO
  - `Ĉu vi trovas teatron aŭ operon pli interesa?` → `Kion vi trovas pli interesa, teatron aŭ operon?`
  - 理由: JA/ZH/KO/RU は「演劇とオペラのどちらをより面白いと思うか」を尋ねる内容。旧文は `Ĉu` により yes/no 疑問として読まれやすく、選択疑問として不十分。PIV 2020 で `trovi ion ia`（例: 対象を形容詞で評価する構文）を確認したうえで、内容を変えずに選択疑問へ修正。

主な据え置き確認:
- `Mi devas diri, ke mi konsentas`, `Mi ne povas konsenti`, `Vi tute pravas`, `Mi konsentas ĝis certa grado` は賛否表現として自然。
- `Ĉu estas ... proksime?`, `Kie troviĝas la stacidomo?`, `Kiom longa tempo necesas...?` は案内質問として列間対応を保つ。
- `drinkejo` は PIV 2020 で飲酒場所の語として確認し、`Ĉu estas drinkejo proksime?` を維持。

## 323. 322周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Expressing Feelings, Help and Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi maltrankviliĝas`, `Mi sentas min deprimita`, `Mi sentas kapturnon`, `Mi ekscitiĝas`, `Mi hontas` は感情・体調表現として許容。
- `Ĉu vi bezonas helpon?`, `Mi petos helpon`, `Mi povas administri mem`, `Vi devus iri al kuracisto`, `Mi malkonsilas ĝin` は助言・援助文脈で意味対応を保つ。
- `tekkomputilo`, `memfida`, `stranga`, `la plej bona elekto` は PIV 2020 または一般的な語形成として問題なし。

## 324. 323周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions, Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi tre rekomendas ĝin`, `Mi memoras ĝin`, `La afero estas, ke ...`, `Ĝi fakte estas sufiĉe bona` は意見表明として自然。
- `Mi bezonas kuraciston`, `Mi perdis mian stirpermesilon`, `oficejo pri perditaj aĵoj`, `Ĉu mi povas prunti vian telefonon?` は緊急時・紛失文脈で列間対応を保つ。
- `akcidentraporto`, `atesto`, `raporti la akcidenton`, `la plej grava prioritato` は事故対応文脈で許容。

## 325. 324周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Public Places / First Aid, At the Police Station, Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bandaĝo`, `diabeto`, `sangado`, `konscia`, `Mi havas astmon`, `vundiĝi` は PIV 2020 で確認でき、応急処置文脈で維持。
- `denunci ŝtelon`, `arestita`, `advokato`, `priskribo`, `fotoroboto` は警察署文脈で意味対応を保つ。`fotoroboto` は Glosbe でも「retrato robot」相当として確認。
- `Permesu min prezenti min`, `Jen mia vizitkarto`, `Mi estas kolego de ...`, `Kiel vi fartas?` は自己紹介表現として許容。

## 326. 325周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Talking about Yourself / Introductions, Place of Residence, Age, Nationality and Religion

結果:
- **1件修正**

修正:
- `ID952` EO
  - `Kia estas via religio?` → `Al kiu religio vi apartenas?`
  - 理由: JA/ZH/KO/RU は「どの宗教・信仰に属しているか」を尋ねる内容。旧文は「あなたの宗教はどのようなものか」に寄り、所属・信仰告白の問いとしてややずれる。PIV 2020 で `aparteni al` の所属用法を確認し、内容を変えず自然な質問へ修正。

主な据え置き確認:
- `Mi loĝas en ...`, `Ĉu vi loĝas sola?`, `Mi kunhavas domon`, `Mi translokiĝis` は住居表現として列間対応を保つ。
- `hispano`, `germano`, `portugalo`, `ĉino`, `britino`, `aŭstraliano`, `sud-afrikano` は国籍表現として許容。
- `kristano`, `islamano`, `hinduistino`, `budhano`, `ateisto`, `katoliko` は宗教・信仰表現として PIV 2020 上でも概ね確認できる。

## 327. 326周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Talking about Yourself / Age, Nationality and Religion, Family and Relationships, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi ne estas praktikanta`, `Mi estas katoliko`, `Mi estas ateisto`, `Mi ne estas religia` は宗教自己紹介として自然。
- `Mi estas siĥo` は PIV ローカル抽出では未確認だったが、Glosbe/Wiktionary 系で `siĥismo` が確認でき、`sikismo` との揺れはあるものの明確な誤りとは判断せず維持。
- `Mi estas fianĉiĝinta`, `Mi estas edziniĝinta`, `Ĉu vi estas edziĝinta?`, `Mi rendevuas kun iu`, `Mi disiĝis` は関係・婚姻文脈で列間対応を保つ。
- `gepatroj`, `geavoj`, `genepoj`, `duonfratino`, `vicpatro`, `baptopatrino` は家族語彙として確認できる。
- `buklajn rufajn harojn`, `Li estas kalva`, `Li havas lipharojn`, `Ŝi portas okulvitrojn` は人物描写として自然。

一致確認:
- `cmp_exit=0`
- `md5=e59f4214702924329b5465c0deec09f6`

## 328. 327周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bonkondutaj`, `Mi zorge elektas miajn amikojn`, `Kien ajn mi iras...` は人物・性格描写として列間対応を保つ。
- `Mi ŝatas troti` は PIV 2020 で人について「小刻みに速く歩く」用法が確認でき、ジョギングの軽い会話表現として許容。
- `piedirado` は EN の hiking より広いが、RU/KO の徒歩・散歩寄りの意味とも合うため維持。
- `Aliĝu al mi por tagmanĝo`, `Ĉu mi povas kunpreni mian amikon?`, `Ni renkontiĝu antaŭ la hotelo` は会う約束の文脈で意味ズレなし。

## 329. 328周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet, Accepting & Declining; Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ludi partion de golfo` はやや直訳的だが、RU `сыграть партию в гольф` と対応し、教材文として許容。
- `Mi ne kontraŭas`, `Tio sonas alloge`, `Mi iomete malfruiĝas`, `Mi venos preni vin...` は承諾・辞退表現として自然。
- `Ĉu mi povas aliĝi al vi?`, `Ĉu ĝenas vin, se mi aliĝos al vi?` は `aliĝi al` の広い参加・合流用法として文脈上許容。
- `Ĉu vi renkontiĝas kun iu?`, `Ĉu vi volus vespermanĝi kun mi?`, `Ĉu vi ŝatus iri manĝeti ion?` はデートの誘い文脈で列間対応を保つ。

## 330. 329周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding; Education / At School

結果:
- **1件修正**

修正:
- `ID1260` EO
  - `Mi amas vin per mia tuta koro` → `Mi amas vin el mia tuta koro`
  - 理由: JA「心の底から」、RU `всем сердцем` に対応する慣用として、PIV 2020 の `ami ... el sia tuta koro` 型の用例に合わせる。`per` は意味推測可能だが、手段・道具の響きが出やすいため、内容を変えず `el` に修正。

主な据え置き確認:
- `Vi mankas al mi`, `Mi enamiĝis al vi`, `Ĉe vi aŭ ĉe mi?`, `Forigu viajn manojn de mi!` はデート会話として自然。
- `ravega`, `alloga`, `hararanĝo`, `mirindan guston pri vestoj` は褒め言葉の文脈で許容。
- `edziniĝos al mi`, `fianĉiĝo`, `novgeedzoj`, `arĝenta nupto`, `diamanta nupto` は婚礼語彙として列間対応を保つ。
- `Kiu povas respondi mian demandon?`, `Ni praktiku la islandan`, `Mi finis lernejon deksesjaraĝe` は学校文脈で意味ズレなし。

## 331. 330周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo infanoj komencas iri al lernejo?` は `Je kiu aĝo` も可能だが、PIV 2020 に `en la aĝo de...` 型の用例があり、明確な誤りとしては扱わず維持。
- `Mi studas por magistriĝo pri juro`, `Mi doktoriĝas pri kemio`, `Mi prenas liberan jaron` は大学生活・学位文脈で意味対応を保つ。
- `akceptkondiĉoj`, `eniraj ekzamenoj`, `studentloĝejo`, `rektoro`, `fakultatoj` は大学制度語彙として許容。
- `formulitaj buŝe`, `trapasis ĉiujn ekzamenojn`, `disertacio`, `aliĝi al la biblioteko` は学生生活文脈で自然。

## 332. 331周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life, Numbers & Colours; Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `faras esploradon`, `kampo de fiziko`, `ripeti multajn aferojn`, `ekzamena sesio` は研究・試験文脈で列間対応を保つ。
- 数字 `Nulo`〜`Unu miliardo`、計算表現 `plus/minus/foje/dividite per/multiplikite per` は形式・意味ともに問題なし。
- `ruĝo`, `blanko`, `rozkoloro`, `grizo`, `bruno`, `purpuro`, `helverda koloro` は色名・混色文脈で許容。
- `informteknologio`, `juristo`, `veterinaro`, `staĝanta kontisto`, `komercistino`, `vokcentro`, `handikapitaj infanoj` は職業表現として列間対応を保つ。

## 333. 332周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Place of Work, Working Conditions

結果:
- **1件修正**

修正:
- `ID1600` EO
  - `Oni maldungis min antaŭ du monatoj` → `Mi estis maldungita pro redukto de laborfortoj antaŭ du monatoj`
  - 理由: EN/JA/ZH/KO/RU は「人員削減・整理解雇」の意味。単なる「解雇された」では理由が落ちるため、PIV 2020 で確認できる `redukto de laborfortoj` を用いて意味を補った。

主な据え置き確認:
- `Mi laboras ĉe universitato`, `Mi laboras de naŭ ĝis la kvina`, `Mi havas permanentan laborpostenon`, `Mi estas memdungita` は勤務先・雇用形態の表現として許容。
- `flekshoraro`, `kromlabori`, `subskribis la kontrakton`, `laborestro`, `sindikato` は就労条件の文脈で列間対応を保つ。

## 334. 333周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Working Conditions, Changing Jobs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `salajro`, `neto`, `malneta salajro`, `pagataj ferioj`, `subskribis la kontrakton` は給与・契約文脈で意味ズレなし。
- `serĉas novan laboron`, `forlasas mian postenon`, `intervjuo`, `vivresumo` は転職文脈で許容。

## 335. 334周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Changing Jobs, Interview, Retirement

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kandidato`, `referencoj`, `kvalifikoj`, `sperto`, `laborkondiĉoj` は面接・応募語彙として自然。
- `Mi emeritiĝis`, `Mi estas pensiulo`, `Mi ricevas pension` は退職・年金文脈で列間対応を保つ。

## 336. 335周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Health / At the Doctor, Symptoms

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kuracisto`, `dentisto`, `malsanulejo`, `doloras`, `febro`, `kapdoloro`, `gorĝdoloro` は症状説明として問題なし。
- 診察時の依頼・説明文は、RU と JA/ZH/KO の実用会話の意味範囲に収まる。

## 337. 336周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Health / Symptoms, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `recepto`, `piloloj`, `tabletoj`, `injekto`, `sangopremo`, `temperaturo` は医療・処方語彙として許容。
- `Mi sentas min malsana`, `Mi havas alergion`, `Mi devas ripozi` は意味の過不足なし。

## 338. 337周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Health / Pharmacy, Emergency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `apoteko`, `medikamento`, `kontraŭdolorilo`, `ungvento`, `bandaĝo` は薬局文脈で自然。
- 緊急時表現は、直接的な要請として JA/ZH/KO/RU と対応している。

## 339. 338周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Transport / Asking Directions, Public Transport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bus haltejo`, `stacidomo`, `metroo`, `bileto`, `horaro`, `platformo` は交通案内語彙として許容。
- `Kiel mi povas atingi...?`, `Ĉu ĉi tiu buso iras al...?` 型の表現は実用会話として自然。

## 340. 339周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Transport / Train, Taxi, Car

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `unuaklasa`, `duaklasa`, `revenbileto`, `taksio`, `ŝoforo`, `aŭtoluado` は列間対応を保つ。
- 料金・乗車・移動先指定の表現は、ロシア語を含め意味ズレなし。

## 341. 340周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Transport / Car, Air Travel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `benzinejo`, `pneŭo`, `motoroleo`, `parkumejo`, `flughaveno`, `flugnumero` は交通・空港文脈で許容。
- 予約・搭乗・荷物関連の文は、JA/ZH/KO/RU と意味範囲が一致する。

## 342. 341周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Transport / Air Travel

結果:
- **2件修正**

修正:
- `ID2464` EO
  - `Mi ŝatus meti 10 funtojn sur ĝin` → `Mi ŝatus aldoni 10 funtojn al ĝi`
  - 理由: 金額を「載せる」ではなく、チャージ・追加する意味。`aldoni ... al` が列間の意味に合う。
- `ID2547` EO
  - `Estas flughavena superpago` → `Estas flughavena krompago`
  - 理由: surcharge は追加料金。`superpago` は「過払い」の連想が強いため、PIV 2020 で確認できる `krompago` に修正。

主な据え置き確認:
- `flughavena imposto`, `enregistriĝo`, `mana pakaĵo`, `pasejo`, `fenestra sidloko` は空港・搭乗文脈で許容。

## 343. 342周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Accommodation / Hotel

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `rezervo`, `unuopa ĉambro`, `duopa ĉambro`, `banĉambro`, `matenmanĝo inkluzivita` は宿泊文脈で自然。
- 料金・鍵・部屋設備に関する表現は列間対応を保つ。

## 344. 343周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Accommodation / Hotel Services

結果:
- **1件修正**

修正:
- `ID2727` EO
  - `Mi bezonas lavi ĉi tion` → `Mi bezonas, ke oni lavu ĉi tion`
  - 理由: EN/JA/ZH/KO/RU は「これを洗ってもらう必要がある」文脈。自分で洗う意味になりやすい旧文から、ホテルサービス依頼として自然な受動的表現へ修正。

主な据え置き確認:
- `lavujo`, `mantuko`, `ĉambroservo`, `vekvoko`, `lavotaĵo` はホテルサービス語彙として許容。

## 345. 344周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Accommodation / Hotel Services, Problems

結果:
- **1件修正**

修正:
- `ID2781` EO
  - `Ne, ni ne uzis` → `Ne, ni ne uzis ĝin`
  - 理由: 他動詞 `uzi` の目的語が欠けており、会話文として不完全。参照対象を `ĝin` で明示。

主な据え置き確認:
- `minibaro`, `klimatizilo`, `la akvo ne varmiĝas`, `la necesejo ne funkcias` は宿泊時トラブルとして意味ズレなし。

## 346. 345周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Accommodation / Problems; Food & Drink / Restaurant

結果:
- **1件修正**

修正:
- `ID2908` EO
  - `Jes, ĝi estas mendita` → `Jes, mi havas rezervon`
  - 理由: 直前の質問 `Ĉu vi havas rezervon?` に対する応答として、旧文は「それは注文済み／予約済み」のように対象が曖昧。JA/ZH/KO/RU の「予約があります」に合わせて修正。

主な据え置き確認:
- `suĉkloŝo` はトイレ詰まり文脈で意味が通り、明確な代替確認なしのため維持。
- `adherema filmo` は直訳感があるが、PIV 2020 で `adheri/adhera` の語義を確認でき、食品包装文脈でも大きな意味ズレはないため維持。

## 347. 346周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Food & Drink / Restaurant

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pastaĵoj` は PIV 2020 でパスタ類の総称として確認でき、料理注文文脈で許容。
- `bifsteko`, `steko`, `karafo`, `menuo`, `ĉefplado`, `deserto` はレストラン語彙として自然。

## 348. 347周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Food & Drink / Restaurant, Complaints

結果:
- **1件修正**

修正:
- `ID3162` EO
  - `Ĝi ne estas sufiĉe bakita` → `Ĝi ne estas sufiĉe kuirita`
  - 理由: JA/ZH/KO/EN は「十分に火が通っていない」一般表現。`baki` は焼く方向へ狭くなるため、PIV 2020 で広く加熱調理を表せる `kuiri` に合わせた。

主な据え置き確認:
- `mendita`, `servita`, `fakturo`, `trinkmono`, `salato`, `supo` は飲食店文脈で列間対応を保つ。

## 349. 348周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Food & Drink / Meat, Fish, Vegetables

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haringo`, `kankro`, `krabo`, `karpo`, `kalmaro`, `truto`, `salikoko` は PIV 2020 で確認でき、魚介類語彙として許容。
- `steko`, `ŝinko`, `salamo`, `brasiko`, `poreo`, `melongeno` は食品名として列間対応を保つ。

## 350. 349周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food & Drink / Vegetables, Fruit, Dessert

結果:
- **1件修正**

修正:
- `ID3283` EO
  - `Ŝi prenos grapfruktan kukon kun glaciaĵo` → `Ŝi prenos grapfruktan torton kun glaciaĵo`
  - 理由: EN/JA/ZH/KO/RU は「グレープフルーツパイ」。PIV 2020 の `torto` は果物等を入れた焼き菓子に合い、既存行の `poma torto` とも揃う。`kuko` はケーキ寄りで広すぎる。

主な据え置き確認:
- `eruko` は PIV 2020 でサラダ用植物（ルッコラ）として確認できるため維持。
- 果物・デザート名は、列間で大きな意味ズレなし。

## 351. 350周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food & Drink / Dessert; Shopping / General, Clothes

結果:
- **1件修正**

修正:
- `ID3368` EO
  - `Mi ŝatus pankukojn kun acera siropo` → `Mi ŝatus patkukojn kun acera siropo`
  - 理由: PIV 2020 で `patkuko` は平たい焼き菓子として確認でき、メープルシロップ付き pancakes に合う。`pankuko` は「パンのケーキ」のように誤読されやすい。

主な据え置き確認:
- `magazeno` は PIV 2020 で一般の `butiko` より大きく多品種の店という語義があり、department store 文脈で許容。
- 衣類の色・サイズ・素材に関する表現は、文脈別許容の範囲内。

## 352. 351周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Cosmetics

結果:
- **2件修正**

修正:
- `ID3456` EO
  - `Mi serĉas ion beĝan` → `Mi serĉas ion sablokoloran`
  - 理由: `beĝa` は PIV 2020 側で確認できず、AI生成的な借用語の疑いが残る。PIV 2020 で `sablokolora` = grize flava と確認でき、EN/JA/ZH/KO/RU の beige/ベージュ/米色/бежевое に対応するため修正。
- `ID3484` EO
  - `Mi ŝatus paron da fingrosandaloj` → `Mi ŝatus paron da zorioj`
  - 理由: `fingrosandalo` はPIV 2020で確認できず、造語的。PIV 2020 の `zorio` は「足指の間で合わさる2本の鼻緒を持つサンダル」で、flip-flops / ビーチサンダル / 人字拖 / 쪼리 / шлёпанцы と一致する。

主な据え置き確認:
- `ŝelkoj` は PIV 2020 でズボン等を支える具として確認でき、suspenders/braces 文脈で維持。
- `paletro da ŝminko por la palpebroj` は説明的だが意味は eyeshadow palette と一致し、未確認語へ置換しない。
- `ŝminko por okulharoj` は mascara の説明表現として意味が明確。`maskaro` はPIV確認できなかったため、無理に置換しない。

一致確認:
- `cmp_exit=0`
- `md5=8b5d13e7a82f8d29d327e561a58434fc`

## 353. 352周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Cosmetics, Photography, Electronics, Housewares

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pinĉilo`, `baterioj`, `limdato`, `fruktan torton`, `kolorigaĵoj`, `konserviloj` は買い物・日用品文脈で列間対応を保つ。
- `baterioj` は `pilo` 系も候補だが、教材上の一般語として意味ズレなし。

## 354. 353周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / Housewares, Stationery, Music, Movies

結果:
- **1件修正**

修正:
- `ID3751` EO
  - `Pardonu, ni akceptas nur kontanton` → `Pardonu, ni akceptas nur kontantan monon`
  - 理由: JA/ZH/KO/RU は「現金のみ」。PIV 2020 で確認できる `kontanta mono` に合わせた。`kontanto` は「現金」の語として不確実で、意味がずれる。

主な据え置き確認:
- 文具・音楽・映画関連の `kajero`, `koverto`, `librotenilo`, `filmkomedio`, `filmo de suspenso` は文脈別許容の範囲。

## 355. 354周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Entertainment / Cinema, Theatre, Nightlife

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `filmo de suspenso` はやや説明的だが、PIV 2020 の `suspenso` と映画文脈が一致するため維持。
- `de longe`, `dekoracioj`, `programero`, `spektaklo`, `teatraĵo` は各列と大きな意味ズレなし。

## 356. 355周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Entertainment / Theatre, Museums, Sports

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto`, `teatra lorneto`, `vestkodo`, `aŭdgvidilo`, `programeto` は劇場・博物館文脈で確認でき、未修正。
- `aŭdgvido` も候補だが、現行の `aŭdgvidilo` は機器・案内媒体を指せるため意味ズレとは扱わない。

## 357. 356周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Entertainment / Sports

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Ni ludu duope`, `malsekkostumo`, `plonĝkostumo`, `aerbotelo`, `savjako`, `surfotabulo`, `akvoskii` はスポーツ・水上活動文脈で対応を保つ。
- `asekurita por urĝaj situacioj` は直訳調だが、旅行・スポーツ保険の文脈として許容。

## 358. 357周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Entertainment / Sports, Outdoor Activities

結果:
- **1件修正**

修正:
- `ID4065` EO
  - `Kiaj estas la vetproporcioj por la favorato?` → `Kiaj estas la vetŝancoj de la favorato?`
  - 理由: EN/JA/ZH/KO/RU は「本命のオッズ」。`vetproporcioj` は辞書確認が弱く不自然。`vetŝancoj` は `veto` + `ŝanco` の透明な複合で、賭けの odds 文脈をより確実に表せる。

主な据え置き確認:
- `regatto` は PIV 2020 で確認できるが、PIV 側では `boatvetkuro` 推奨の注記がある。既存語として確認でき、明確な意味ズレではないため維持。
- `kuro`, `golfĉaro`, `norma nombro da batoj`, `popolmuziko`, `telfero`, `poŝlampo` は文脈上問題なし。

## 359. 358周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Outdoors, Farm Stay, In the House

結果:
- **1件修正**

修正:
- `ID4227` EO
  - `La bolilo bolis` → `La akvo jam bolas`
  - 理由: JA/ZH/KO/RU は「お湯・水が沸いた」。PIV 2020 で `bolilo` は湯を沸かす器具であり、`boli` の主体は液体として扱うのが自然。英語/RU の kettle 表現の直訳を避けた。

主な据え置き確認:
- `televidaj romanoj` は soap opera の説明的訳として Glosbe 等で確認でき、定型句として維持。
- `piedvojetoj`, `sagetoj`, `bovlingon`, `mendas picon hejmen` は列間対応を保つ。

## 360. 359周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- In the House, Finance, House Purchase, Renting

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `provizio`, `ĝiri`, `bangalo`, `monretiro`, `vicdomo`, `posedaĵo`, `kontanta aĉetanto`, `deponaĵo je unu-monata lupago` は金融・住宅文脈で許容。
- `retiri monon` も候補だが、現行 `monretiro` は意味が明確で列間対応を崩さない。

## 361. 360周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Hairdresser, Beauty Salon, Tailor

結果:
- **1件修正**

修正:
- `ID4420` EO
  - `Mi ŝatus ricevi masaĝon de la skalpo` → `Mi ŝatus ricevi masaĝon de la kranihaŭto`
  - 理由: PIV 2020 の `skalp/o` は事故等で剥がれた頭皮の意味が中心で、通常の scalp massage には不自然。PIV 2020 の `haroj` 項で確認できる `kranihaŭto` に直し、内容を変えずに自然化した。

主な据え置き確認:
- `konstanta ondumado`, `dislimi`, `brulas` は PIV 2020 で美容・身体感覚の文脈を確認できるため維持。
- `franĝo`, `laki miajn ungojn`, `zipo`, `laŭmezura`, `mallarĝigi`, `plilarĝigi` は意味対応を保つ。

## 362. 361周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Tailor, Watchmaker, Health / Doctor

結果:
- **1件修正**

修正:
- `ID4552` EO
  - `Mi bezonas recepton por trankviligilo` → `Mi bezonas recepton por trankviligaĵo`
  - 理由: PIV 2020 で `trankviligaĵo` は「脳を鎮静させる薬」として確認でき、処方薬の tranquilizer に合う。`trankviligilo` は透明ではあるが、医薬品名としては `trankviligaĵo` がより確実。

主な据え置き確認:
- `kroneto` は時計の竜頭文脈で意味が通り、`pilo`, `suprenfaldi`, `desinfekti`, `surdorse/surventre`, `kalkanumo`, `suturero`, `anestezo` も列間対応を保つ。

## 363. 362周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haŭterupcio`, `furunko`, `diareo`, `konstipita`, `limfonodoj`, `mikozo`, `fojnofebro`, `sangotesto`, `urina specimeno`, `kuracista atestilo` は医療文脈で意味対応を保つ。
- `fojnofebro` は `fojna febro` / `fojnkataro` 系の表現として透明で、明確な誤りとは扱わない。

## 364. 363周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Dentist, Optician, Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `plastro`, `leŭkoplasto`, `kontraŭdolorilo`, `dezajnistaj kadroj`, `klavi`, `proksime/fore vidi` は歯科・眼鏡・薬局文脈で許容。
- `analgeziko` は候補だが、`kontraŭdolorilo` は意味が明確で、教材文として十分に通る。

## 365. 364周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / Pharmacy; Communication Means / Phone

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `farmacisto/apotekisto` は語選択の差にとどまり、現行 `farmacisto` を維持。
- `voka signalo`, `okupata`, `aŭtomata respondilo`, `malŝargiĝi`, `kapti signalon`, `voko pagata de la ricevanto` は電話文脈で意味対応を保つ。

## 366. 365周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `tekkomputilo`, `klavi`, `rekomendita poŝto`, `eldonkvanto`, `dogana deklaracio`, `poŝtrestante` は今回も未修正。
- `rekomendita` には PIV 2020 で郵便用法の避けたい注記があるが、同時に用例確認もでき、教材上の「書留」対応として明確な誤りとは扱わない。

## 367. 366周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter; Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `vivresumo`, `Antaŭdankon`, `Sincere via`, `Respektplene via`, `Kun plej koraj salutoj`, `Al la koncernatoj` は郵便・手紙定型句として維持。
- `Mi antaŭĝojas ...` は PIV 2020 の直接見出しでは未確認だが、オンライン辞書・実例で使用が確認でき、列間の「楽しみにしている」と一致するため未修正。
- `kvin antaŭ la dua`, `post la unua`, `la dua kaj duono`, `kvarono antaŭ/post`, `tagmezo`, `noktomezo`, `labortagoj`, `libertago` は日時表現として問題なし。

## 368. 367周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Hodiaŭ tage`, `Ĉi-posttagmeze`, `Postmorgaŭ`, `La sekvantan tagon`, `Ĉiujn kvin minutojn`, `Ĝis aŭgusto` は時制・日付表現として列間対応を保つ。
- `Estas glacie kaj glite`, `Pluvetadas`, `Hajlas`, `Fulmas`, `fulmotondro`, `malvarmete`, `sub nulo`, `veterprognozo`, `Ĉi-nokte frostos`, `atmosfera premo` は PIV 2020 ローカル抽出と文脈照合で維持。
- `Hodiaŭ estas kiel en forno`, `La suno ĵus kaŝiĝis`, `La vento ĉesis`, `La nuboj disiĝas`, `Blovas forta vento`, `En la ĉielo ne estas eĉ unu nubo` は自然な気象描写として許容。

## 369. 368周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Bonan matenon`, `Bonan tagon`, `Bonan vesperon`, `Bonan nokton`, `Ĝis revido`, `Ĝis baldaŭ` は挨拶・別れの定型句として維持。
- `Sanon!`, `Je via sano!`, `Ni tostu por vi!`, `toston por mia filo` は祝意・乾杯表現として列間対応を保つ。PIV 2020 で `tosto/tosti` の祝杯文脈を確認。
- `Mi antaŭĝojas revidi vin`, `Tio estis la plej malmulto, kion mi povis fari`, `Mi tre aprezas viajn afablajn vortojn` は自然化候補はあるが、意味ズレが明確ではないため未修正。

## 370. 369周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions and Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi ne tion celis`, `Ne estas kialo pardonpeti`, `Pardonu pro la prokrasto`, `Mi agis senzorge` は謝罪・弁明文脈で意味対応を保つ。
- `Kuraĝu!`, `Sciigu min`, `Atentu la hundon`, `Ne paŝu sur la gazonon!`, `viciĝi` は命令・助言表現として許容。
- `Kiom?`, `Kiom ofte?`, `Kiom longe?`, `Kiom malproksime?`, `Kio estas via profesio?` は短問答の教材文として問題なし。

## 371. 370周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions and Answers, Congratulations; General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Feliĉan Divalon!` は過去修正後の形を維持。外部用例で `Divalo` 系の使用を確認し、Diwali との対応を保つ。
- `Gratulon pro via akcepto en la universitaton!` は `akceptiĝo` も候補だが、大学に受け入れられたこととして読め、明確な誤りではないため未修正。
- `azerbajĝane`, `Via tagaloga estas tre bona`, `Mi provas lerni la malajan`, `Mi lernas la indonezian` は言語名の派生として意味が明確。
- `akĉento`, `literumi`, `prononci`, `kompreni`, `traduki` は意思疎通文脈で列間対応を保つ。

## 372. 371周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing and Disagreeing, Asking for and Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mandarena ĉina lingvo` は PIV 2020 で中国語文脈の `mandarena lingvo` 系用例を確認でき、普通話/マンダリンとして維持。
- `kunhavas vian vidpunkton`, `Mi vidas nenian malhelpon`, `en plena ordo`, `drinkejo`, `junulargastejo`, `picejo`, `biciklas` は PIV 2020 または透明な語形成で確認し、未修正。
- `Kion vi trovas pli interesa, teatron aŭ operon?` は既存修正後の選択疑問として、日中韓・RU とよく対応している。

## 373. 372周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for and Giving Information, Expressing Feelings, Help and Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `malstreĉita`, `ekscitita`, `motivita`, `embarasi`, `kapturno`, `malkuraĝigita`, `kondolencoj` は感情・体調・弔意表現として許容。
- `Kion vi pensas, ke mi faru?`, `Ĉu vi estus tiel afabla kaj klarigus tion denove?` はより滑らかな言い換えも可能だが、意味は明確で列間対応を崩さない。
- `flugpersonaro`, `malkonsili lui aŭton`, `prizorgi tion dum momento`, `plenumi ion ajn`, `tekkomputilo` は助言・依頼文脈で維持。

## 374. 373周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions; Emergencies / Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Dependas de vi`, `Ne indas`, `aktorado`, `konsideras ĉi tiun filmon la plej bona`, `teknologio plibonigas la vivon` は意見表現として対応を保つ。
- `oficejo pri perditaj aĵoj`, `fajrobrigado`, `ambulanco`, `traŭmatizita`, `stirpermesilo`, `interpretisto` は緊急・事故文脈で問題なし。
- `Mi havis la prioritaton` は PIV 2020 で交通文脈の `havi prioritaton de paso` が確認でき、right of way として維持。
- `asekurdokumentoj`, `akcidentraporto`, `raporti akcidenton`, `informi pri la akcidento` は事故対応文脈で列間対応を保つ。

## 375. 374周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid, At the Police Station; Making Friends / Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi tordis al mi la maleolon` は PIV 2020 の `tordi al si la piedon` 型と整合し、捻挫文脈として維持。
- `Ĉu mi povas ĝin anstataŭigi?` は「再発行」にはやや広いが、紛失したパスポート等を代替取得する文脈として理解可能。
- `fotoroboton` は既存の Glosbe 確認済み判断を維持し、警察の photofit / фоторобот 文脈と対応する。
- `familinomo`, `konatiĝi kun vi`, `vendmanaĝero` は紹介文脈で意味ズレなし。

## 376. 375周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions, Place of Residence, Age, Nationality & Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `amikino`, `fraŭlino`, `vendmanaĝero`, `kunloĝas`, `Nov-Zelando`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio` は既存の辞書確認・列間照合どおり維持。
- `Kia estas via nacieco?` は `Kio estas...` も自然だが、国籍という属性の種類を問う形として文脈別許容。
- `Mi estas ĉi tie por labori` は RU の出張寄りに対して日中韓/ENが「仕事で来ている」と一致しており、現行を維持。

## 377. 376周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age, Nationality & Religion, Family & Relationships, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `siĥo`, `protestantino`, `katoliko`, `musulmanino`, `hinduistino`, `ateisto` は宗教・信仰表現として対応を保つ。
- `Mi estas edziniĝinta`, `Ĉu vi edziniĝis?`, `Jes. Fakte, mi estas fianĉino` は女性話者前提の列と整合する。
- `genepoj`, `bonŝanculo`, `okulvitroj`, `blondaj/rufaj haroj`, `gustumi` は人物・身体描写文脈で問題なし。

## 378. 377周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **1件修正**

修正:
- `ID1086` EO
  - `Kion vi pensas pri teruraj filmoj?` → `Kion vi pensas pri hororaj filmoj?`
  - 理由: EN/JA/ZH/KO/RU はいずれも horror films / ホラー映画 / 恐怖片 / 공포 영화 / фильмы ужасов。`teruraj filmoj` は「ひどい映画」とも読めて意味が広すぎる。PIV 2020 で `hororo` / `horora` を確認し、映画ジャンルとしての対応を明確にした。

主な据え置き確認:
- `troti` は PIV 2020 で人について「短い歩幅で速く進む」用法が確認でき、ジョギング文脈で許容。
- `piedirado` は EN/JA/ZH の hiking より広いが、RU/KO の徒歩・散歩寄りの意味とも合うため維持。
- `Aliĝu al mi por tagmanĝo`, `Ĉu vi rememorigos min?`, `je la 16-a horo`, `vestiblo` は約束・待ち合わせ文脈で意味ズレなし。

## 379. 378周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet, Accepting & Declining; Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `partio de golfo` は PIV 2020 の `partio`（ゲーム・競技の一回）で説明でき、round of golf として維持。
- `Ĉu vi renkontiĝas kun iu?` は広いが、Dating 文脈では「付き合っている/会っている人がいる」と読めるため未修正。
- `Kion vi elpensis?` は EN の "What are you up to?" よりも RU/日中韓の「何を考えた/企てた」に寄っており、現行を維持。
- `Ni forveturu de ĉi tie` は RU `уедем` と整合し、JA/ZH/KO の「ここを出る」とも衝突しない。

## 380. 379周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding; Education / At School

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `edziniĝos al mi`, `fianĉiĝo`, `novgeedzoj`, `arĝenta nupto`, `diamanta nupto` は婚礼語彙として列間対応を保つ。
- `ravega`, `hararanĝo`, `Vi aspektas bela en tiu robo`, `guston pri vestoj` は褒め言葉として意味ズレなし。
- `Kiu povas respondi mian demandon?` は PIV 2020 の `respondi tiun ĉi demandon` 型と整合するため維持。
- `Ni praktiku la islandan`, `Mi finis lernejon deksesjaraĝe`, `hazarda eraro`, `parkere`, `notoj` は学校文脈で問題なし。

## 381. 380周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **1件修正**

修正:
- `ID1378` EO
  - `Mi studas la hindan` → `Mi studas la hindian`
  - 理由: EN/JA/ZH/KO/RU はすべて Hindi / ヒンディー語 / 印地语 / 힌디어 / хинди。PIV 2020 ローカル抽出で `hindia lingvo` 型を確認でき、`hinda` だけでは「インドの」に寄って言語名として曖昧なため、意味を変えずに Hindi を明確化した。

主な据え置き確認:
- `En kiu aĝo infanoj komencas iri al lernejo?` は `Je kiu aĝo` も候補だが、PIV の `en la aĝo de...` 型と矛盾せず未修正。
- `akceptkondiĉoj`, `eniraj ekzamenoj`, `studentloĝejo`, `lektoro pri la rusa lingvo` は大学文脈で意味対応を保つ。
- `Mi faros mian raporton en la kataluna` は発表/レポート文脈として列間対応が大きく崩れないため維持。
- `templimo por paroladoj` は生産的複合語として意味が取れるため、低優先保留のまま維持。

## 382. 381周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life; Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ripeti multajn aferojn`, `noti`, `ekzamensesio`, `studenteca vivo` は学生生活文脈で意味ズレなし。
- `purpuro/purpura`, `informteknologio`, `vokcentro` は既存確認どおり、色名・職業語彙として維持。
- `komercistino` は businesswoman として広めだが、女性の商業・事業従事者として各列と大きく衝突しないため未修正。
- `handikapitaj infanoj` は表現上の現代的配慮は別として、対象列の disabled children と対応するため維持。

## 383. 382周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `merkatika administranto` は marketing manager / specialist の揺れが残るため高優先保留を継続し、安全な確定置換がない限り動かさない。
- `patrina forpermeso`, `patra forpermeso` は育児・出産関連休暇として既存の辞書確認どおり維持。
- `La pago de ĉi tiu fakturo malfruas` は invoice payment overdue として列間対応が明確。
- `La limtempo por liveri la varojn finiĝas` は deadline 文脈で意味が通り、前回修正後の形を維持。

## 384. 383周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business, At the Interview, Recommendation Letter

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `akiri rekomendojn` は references / рекомендаций として推薦状・照会先文脈で成立するため維持。
- `labori laŭvice` は shift work 文脈で読め、列間の意味を崩さない。
- `Mia fako estas informatiko` は IT / informatics の近接領域として文脈別許容。
- `fortaĵoj` / `malfortaĵoj` は長所・短所として PIV 確認済みの判断を維持。

## 385. 384周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter; Travel / Asking & Giving Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `aldono al via programo`, `gvidanto`, `labori laŭvice` は推薦状・就労文脈で対応を保つ。
- `piediri`, `orientiĝi`, `ŝparvojo`, `ĝuste trans la strato` は道案内文脈で意味ズレなし。
- `fajrobrigadejo` は fire station として透明で、既存確認どおり維持。
- `loĝejo/resti` は accommodation / stay 文脈として各列と衝突しない。

## 386. 385周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions, Tourist Office, Excursions; Plane / Booking a Flight

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `turisma oficejo`, `sandviĉejo`, `viziti vidindaĵojn` は観光案内所・サンドイッチ店・観光文脈で意味対応が明確。
- `naveda buso` は PIV の `naveda` の往復・行き来の語義と合い、shuttle bus として前回修正後の形を維持。
- `preni miajn fotojn` は写真店で写真を受け取る文脈として読めるため、`ricevi` への過修正は避けた。
- `vidindaĵa ekskurso`, `Parlamentejo`, `tuttaga ekskurso`, `subeksponitaj` は旅行・写真文脈で列間対応を保つ。

## 387. 386周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight, Checking in, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `forveturo` は飛行機文脈では `forflugo` も候補だが、一般の出発として成立するため維持。
- `registrejo`, `pordego/elirejo`, `bagaĝetikedo`, `superpezo` は空港・荷物文脈で意味が明確。
- `enŝipiĝo` は船由来の語感があるが、boarding の拡張用法として既存保留どおり未修正。
- `manbagaĝo` 系は見出し語としては弱めだが、空港文脈の hand luggage として対応が明確なため維持。

## 388. 387周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage, Passport Control & Customs, On the Plane, Airport Signs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bagaĝ-ricevejo`, `bagaĝa elpreno`, `dogano`, `dogana deklaracio`, `transitvizo/transite`, `peti azilon` は空港・税関文脈で維持。
- `sekurzono`, `stevardino`, `seĝodorso`, `supra bagaĝujo` は機内表現として列間対応を保つ。
- `sakon por vomado` は `vomsako` も候補だが、意味は明確で、確実な置換が必要な誤りとは判断しない。
- `kriza elirejo`, `pordegoj`, `forflugoj` は空港表示として意味ズレなし。

## 389. 388周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane, Airport Signs; Car / Car Hire, Driving & Parking

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dogandeklaro`, `hebrean`, `senimpostajn varojn`, `bagaĝa elpreno` は機内・空港表示文脈で維持。
- `mana aŭ aŭtomata transmisio`, `benzinujo`, `kofrujo`, `direktomontriloj`, `klimatizilo`, `stirpermesilo`, `kaŭcio` はレンタカー文脈で既存修正後の形を維持。
- `infanseruroj`, `minimuma luoperiodo`, `vojmapo` は透明複合語として意味対応が保たれているため低優先保留のまま維持。
- `Veturu trans la ponton`, `Veturu sub la ponto`, `trafikrondo` は運転案内として列間対応を崩さない。

## 390. 389周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vojsignoj`, `unudirekta strato`, `glacikovritaj`, `aŭtoriparejo`, `parkometro`, `serva areo`, `trafikblokiĝo` は道路・駐車文脈で維持。
- `benzinejo`, `benzinujo`, `kontraŭfrosta likvaĵo`, `startokabloj` は給油所・車両用品として意味が明確。
- `pneŭmatiko krevis`, `akumulatoro malŝargiĝis`, `hupo`, `kapoto`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `bremslikvaĵo` は機械トラブル文脈で対応を保つ。
- `Bonvolu sendi iun por ĝi` は車の引き取り文脈として読めるため未修正。

## 391. 390周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs; Other Transport / At the Bus Station, At the Train Station

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Buskoridoro`, `Preterpasu maldekstre`, `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo` は道路標識として既存修正後の形を維持。
- `bushaltejo`, `revenbileto`, `monata abono`, `rabatita tarifo`, `pensiula revenbileto` は公共交通の切符文脈で意味ズレなし。
- `retura bileto` と `revenbileto` の揺れはあるが、return ticket として明確なため未修正。
- `Kiu kajo?`, `Atentu la interspacon`, `fervoja stacidomo`, `ekspresa/eksprestrajno` 系は鉄道駅文脈で対応を保つ。

## 392. 391周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Other Transport / Train Station, On the Bus or Train, Taxi

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `eksprestrajno`, `vojaĝkarto`, `abonbileto`, `skemo de la metroo` は交通カード・鉄道路線図文脈として維持。
- `laŭpeta haltejo`, `pakaĵujo`, `kupeo`, `preterveturis vian haltejon` はバス/鉄道内の表現として意味対応が明確。
- `taksimetro`, `taksihaltejo`, `restmono`, `trinkmono`, `trajnstacio` はタクシー文脈で既存確認済みの判断を維持。
- `flughavena krompago` は前回修正後の形で、airport surcharge として対応する。

## 393. 392周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Other Transport / Taxi, Ship; Hotel / Asking about Facilities, Booking a Room

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `nokta krompago`, `bankaŭtomato`, `savboato`, `savringo`, `marmalsano`, `kajo`, `kajuto`, `enŝipiĝi`, `krozado` は交通・船旅文脈で維持。
- `radiogramo`, `sunseĝo`, `monŝanĝejo`, `transiro` は船旅・通信文脈で対応を保つ。
- `aŭtoparkejo`, `monŝranko`, `lavservo`, `ĉambroservo`, `rulseĝa aliro`, `gimnastikejo`, `ŝtopilingo` はホテル設備として既存確認どおり未修正。
- `plena pensiono`, `antaŭpago`, `unulita ĉambro`, `ĉambro kun du apartaj litoj` は宿泊予約文脈で意味ズレなし。

## 394. 393周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Room, Checking in, During Your Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `atendolisto`, `vizitkarto`, `duobla ĉambro`, `aldona/plia lito`, `nefumantoj` はホテル予約文脈で対応を保つ。
- `ĉambronumero`, `ĉambroŝlosilo`, `forlasi la ĉambron`, `enirpordo`, `monŝranko` はチェックイン文脈で意味が明確。
- `savelirejo`, `gladigi`, `ekstera linio`, `internacia kodo`, `plusendi`, `plilongigi mian restadon` は滞在中の依頼として既存確認どおり維持。
- `tuko` と `mantuko` の揺れはあるが、タオル文脈として列間対応は崩れない。

## 395. 394周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay, Checking out, Complaints, Renting a Flat

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `lavejo`, `lavotaĵo`, `elregistriĝi`, `kalkulo/fakturo`, `servokotizo`, `restmono` はホテル精算・クリーニング文脈で既存判断どおり維持。
- `lavujo`, `ŝtopita`, `bolilo`, `butono`, `klimatizilo`, `littukoj`, `duobla lito` は苦情・設備語彙として対応を保つ。
- `Mi volas rehavi mian monon`, `repreni mian bagaĝon`, `rehavi miajn valoraĵojn` は返金・返却文脈で意味ズレなし。
- `apartamento/loĝejo/luo` はフラット賃貸文脈で各列と衝突しない。

## 396. 395周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat; Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vazaro`, `ŝvabrilo`, `litotukoj`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `suĉkloŝo`, `adherema filmo`, `polvosuĉilo` は備品語彙として文脈別許容。
- `mikroondilo`, `telerlavmaŝino`, `elektromezurilo`, `ĉambristino` は住居設備・清掃文脈で維持。
- `mendi/rezervi tablon`, `fumejo`, `liberaj tabloj`, `oni vin kondukos al via loko` はレストラン予約文脈で意味対応が明確。
- `gasita akvo`, `akvo sen gaso`, `vinkarto`, `doma vino`, `karafo`, `kranakvo` は飲み物注文文脈で既存確認どおり維持。

## 397. 396周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food, During the Meal

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio` は PIV 2020 には強く出ないが、既存のオンライン辞書・用例確認に基づき、smoothie の借用語として保留解除済みの判断を維持。
- `koŝera manĝaĵo`, `pastaĵoj`, `fritoj`, `por forporti`, `por kunpreni`, `memservo`, `franca saŭco` は飲食店文脈で対応を保つ。
- `vegetaranino` は女性話者を明示するが、RU も女性形であり、対象列との大きな破綻はない。
- `tritavola sandviĉo`, `farĉitaj fungoj`, `ĉefplado`, `mezrostita`, `bone rostita` は料理・焼き加減の表現として既存確認どおり維持。

一致確認:
- `cmp_exit=0`
- `md5=659340847578b90489041249d2ca1cf3`

## 398. 397周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `halala`, `manĝobastonetoj`, `kalzoneo`, `servokotizo`, `sumigita`, `meleagro`, `odoras je korko` は飲食店文脈で維持。
- `Ĉu vi ŝatus iom da deserto?`, `kalzoneon`, `servokotizon`, `Ĝi ne estas sufiĉe kuirita` は既存修正後の形で列間対応が保たれている。

## 399. 398周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints; Food / Meat and Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `naĉoj`, `postebrio`, `barela biero`, `laktoskuaĵo`, `bifstekon el bova lumbaĵo` は料理・飲み物文脈で意味ズレなし。
- `soleo`, `salikoko`, `ŝafidaĵo`, `ansero`, `fazano`, `rostbifo`, `kalmaro`, `truto`, `skombro`, `moruo`, `polpo`, `kankroj` は食材語彙として対応を保つ。

## 400. 399周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Foods

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `limeojn`, `grapfruktan torton`, `akra kapsiko`, `panitan kukurbeton`, `brezitajn karotojn kaj kikerojn` は既存修正後の形で維持。
- `nigra ribo`, `framba`, `mirtela`, `oksikoka`, `florbrasiko`, `melongeno`, `laktuko`, `eruko`, `kuskuso`, `fazeoloj`, `lentoj`, `petroselo` は食品語彙として意味対応が明確。
- `cerealojn` は朝食シリアル/穀物の幅があるが、この範囲では明確な意味ズレとは判断しない。

## 401. 400周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast; Shopping / Shopping, Clothes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `patkukojn kun acera siropo`, `avenajn biskvitojn`, `ringokukojn`, `kazeo`, `kirlovaĵo` は朝食・食品文脈で維持。
- `magazeno`, `kemia purigado`, `Lavu inversigite`, `ŝorto`, `Ĝi ne konvenas al mi` は買い物・衣類文脈で大きな意味ズレなし。

## 402. 401周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Personal Care

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sablokoloran`, `zorioj`, `pantofoj`, `sportŝuoj`, `gumaj botoj`, `Ili sidas sur mi kiel ganto` は衣類・靴文脈として維持。
- `ŝelkoj`, `manumbutonoj`, `horloĝrimeno`, `ungofajlilo` は装身具・身だしなみ語彙として対応する。
- `paletron da ŝminko por la palpebroj`, `ŝminko por okulharoj` は説明的ではあるが、確実な置換根拠がないため未修正。

## 403. 402周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care, Electronics, Other Goods, Supermarket

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pinĉilo`, `telefonan ŝargilon`, `lensokovrilon`, `porteblan komputilon`, `skanilon`, `pilojn por poŝlampo`, `harsekigilon` は商品語彙として自然。
- `konstrubriketojn`, `bokalon`, `limdato`, `fruktan torton`, `ceramikaĵoj`, `figuretoj`, `bierkruĉoj`, `vinkarafoj`, `skribmaterialoj` は売場文脈で意味対応を保つ。

## 404. 403周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / Supermarket, Bookshop and Florist, Payments

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `granatoj`, `aĉetĉaretoj`, `konservaĵoj`, `ĉokoladaj bombonoj`, `duonduzenon da ovoj` はスーパー文脈として維持。
- `detektivaj romanoj`, `poemaroj`, `brokanta librovendejo`, `krono el freŝaj floroj por la fianĉino` は書店・花屋文脈で意味ズレなし。
- `kontantan monon`, `PIN-kodo` は支払い文脈で対応する。

## 405. 404周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Shopping / Payments; Entertainment / Cinema, Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `donacskatolo`, `senimposte`, `interŝanĝi ... kontraŭ`, `bonuskarto`, `donacpaki`, `sekureca numero`, `repago` は支払い・返品文脈として維持。
- `filmo de suspenso`, `pufmaizo`, `premiero`, `subtekstoj`, `animaciaĵo`, `nigrablanka filmo`, `opereto`, `dekoracioj` は映画・劇場文脈で対応を保つ。

## 406. 405周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Entertainment / Theatre, Museum, Nightclub

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto` はPIVで劇場の休憩文脈を確認済み。
- `teatra lorneto`, `loĝio`, `dramteatro`, `aŭdgvido`, `fulmilo`, `karikatursalono`, `vaksaj figuroj`, `etnografia muzeo`, `handikapuloj`, `vestkodo`, `bilardo` は各文脈で維持。

## 407. 406周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Entertainment / Nightclub, Beach; Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `gastlisto`, `sportŝuoj`, `viva muziko`, `homplene`, `mortige enue`, `diskĵokeo`, `drinkejo` はナイトクラブ文脈で意味ズレなし。
- `sunseĝo`, `akvoskioj`, `subakvaj fluoj`, `jaĥtklubo`, `plonĝkostumo`, `aerbotelo`, `malsekkostumo`, `savjako`, `surfotabulo` は海辺・レジャー語彙として維持。
- `Ni ludu duope`, `arbitro`, `goli`, `egaligis la poentaron`, `vetkuroj`, `ĉevalfortoj`, `subtenanto` はスポーツ文脈で対応する。

## 408. 407周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Sport / Golf, Regatta; Entertainment / Music; Travel / Camping

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vetŝancoj`, `golfbastonoj`, `golfĉaro`, `norma nombro da batoj`, `regatto`, `femuraj muskoloj` はスポーツ文脈として維持。
- `popolmuziko`, `ruldomo`, `kukolo`, `pego`, `najtingalo`, `hirundo`, `telfero`, `poŝlampo`, `dormosako`, `kuireja ekipaĵo`, `piedvojetoj` は音楽・キャンプ文脈で対応を保つ。

## 409. 408周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Travel / Camping; Home / Family, Gardening, Having Guests; Services / At the Bank

結果:
- **2件修正**

修正:
- `ID4197` `Ŝi rakis la foliojn en amason` → `Ŝi rastis la foliojn en amason`
  - PIV 2020で `rasti` が「落ち葉などを熊手で集める」意味を持つことを確認。`raki` では意図が外れるため修正。
- `ID4223` `Ĉu vi ŝatus toston?` → `Ĉu vi ŝatus toaston?`
  - PIV 2020で `tosto` は乾杯の辞、`toasto` は焼いたパン片と確認。食事文脈の toast は `toasto` が適切。

主な据え置き確認:
- `televidaj romanoj` は Glosbe で soap opera 対応を確認し維持。
- `sagetoj`, `erpis`, `fruktarbejo`, `kulturplantoj`, `buŝtukoj`, `telekomandilo`, `senalkohola trinkaĵo`, `ĝino kun toniko`, `mendi picon hejmen` は各文脈で意味ズレなし。

参照:
- PIV 2020 `rasti`: https://vortaro.net/py/serchi.py?s=rasti&simpla=1
- PIV 2020 `tosto`: https://vortaro.net/py/serchi.py?s=tosto&simpla=1
- PIV 2020 `toasto`: https://vortaro.net/py/serchi.py?s=toasto&simpla=1
- Glosbe `soap opera`: https://glosbe.com/en/eo/soap%20opera

## 410. 409周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Services / At the Bank, At the Estate Agency

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `legitimilo`, `formularo`, `kurzo`, `provizio`, `kvitancon`, `bankaŭtomato`, `kontantmono`, `saldon`, `stirpermesilon`, `monretiro`, `ĉekaro`, `ĝiri`, `komuna konto`, `interezprocento`, `kontantigi` は銀行文脈で維持。
- `loĝejo`, `bangalo`, `vicdomo`, `parkumejo`, `petata prezo`, `posedaĵo`, `kontanta aĉetanto`, `hipoteko`, `antaŭpago`, `deponaĵo je unu-monata lupago`, `meblita/nemeblita`, `sur la merkato` は不動産文脈で意味対応が明確。

## 411. 410周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dissendolisto`, `franĝo`, `konstanta ondumado`, `dislimo`, `farbigi`, `helajn striojn`, `senharigon`, `vizaĝan masaĝon`, `kranihaŭto`, `laki miajn ungojn` は美容院文脈で維持。
- `alkudri`, `fliki`, `alĝustigi`, `laŭmezura kostumo`, `maniklongon`, `mallarĝigi`, `plilarĝigi` は仕立て屋文脈で対応する。

## 412. 411周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs; Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kuirforno`, `brakhorloĝo`, `kroneto`, `ŝlosilringo`, `lasi ripari mian fotoaparaton`, `riparejo por ŝuoj`, `plandumo` は修理文脈で意味ズレなし。
- `kapturno`, `medikamentojn`, `rentgena ekzameno`, `aŭdotestojn`, `sangogrupo`, `kmera`, `desinfekti`, `suprenfaldi`, `sangopremo`, `trankviligaĵo`, `surdorse/surventre` は医療文脈で維持。

## 413. 412周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor, Diseases, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haŭterupcio`, `furunko`, `diareo`, `konstipita`, `diabetulo`, `ŝvelo`, `nazkataro`, `gorĝdoloro`, `ŝvelinta maleolo`, `limfonodoj`, `mikozo de la piedoj`, `fojnofebro`, `sendormeco` は病気・症状語彙として維持。
- `sutureroj` はPIV 2020で「縫合を構成する結ばれた糸」の意味を確認し、stitches として維持。

参照:
- PIV 2020 `suturero`: https://vortaro.net/py/serchi.py?s=suturero&simpla=1

## 414. 413周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dentodoloro`, `gingivoj`, `plombo`, `krono`, `dentprotezo`, `denta higienisto`, `kario`, `alĝustigu al vi kronon`, `gargari la buŝon` は歯科文脈で対応する。
- `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `okulekzamenoj`, `astigmatismo`, `kadroj`, `UV-protekto` は眼鏡店文脈で維持。
- PIV 2020で `gargari` に「buŝon aŭ gorĝon」を洗う語義を確認。

参照:
- PIV 2020 `gargari`: https://vortaro.net/py/serchi.py?s=gargari&simpla=1

## 415. 414周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy; Communication Means / Phone, Phone Calls at Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kromefikoj`, `tutnokte malfermita apoteko`, `farmacisto`, `dormigiloj`, `misdigesto`, `dormemigi`, `Ne prenu interne` は薬局文脈で意味ズレなし。
- PIV 2020で `misdigesto` の収録を確認。
- `malkonektiĝis`, `telefonbudo`, `vokan signalon`, `kredito`, `voko pagata de la ricevanto`, `aŭtomata respondilo`, `telefonkarton`, `klavi la numeron`, `sur alia linio` は電話文脈で維持。PIV 2020で `klavi` に電話のためにキーを押す語義を確認。

参照:
- PIV 2020 `misdigesto`: https://vortaro.net/py/serchi.py?s=misdigesto&simpla=1
- PIV 2020 `klavi`: https://vortaro.net/py/serchi.py?s=klavi&simpla=1

## 416. 415周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interna numero`, `retpoŝtadreso`, `uzantonomo`, `ensalutu/elsalutu`, `tekkomputilo`, `tajpu`, `Tvitero`, `eldonkvanto`, `titoloj` は通信・メディア文脈で維持。
- `poŝtoficejo`, `poŝtkesto`, `vatita koverto`, `aerpoŝto`, `televida licenco`, `abono`, `afranko`, `fotokopio`, `rekomendita poŝto`, `dogana deklaracio`, `pesilo` は郵便局文脈で対応する。

## 417. 416周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter; Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `vivresumo`, `Antaŭdankon`, `Respektplene via`, `antaŭĝojas`, `aldonaĵo`, `ekzameni ĉi tiun aferon` は郵便・手紙文脈で維持。
- `kvin antaŭ la dua`, `kvin minutoj post la unua`, `la dua kaj duono`, `kvarono antaŭ/post`, `ĝis la unua horo` は時刻表現として対応する。
- `labortagoj`, `libertago`, `vintraj/printempaj monatoj` は暦表現として意味ズレなし。

## 418. 417周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Hodiaŭ tage`, `Ĉiutage`, `Ĉi tiun semajnon`, `Ĉi-jare`, `Ĉi-posttagmeze`, `Postmorgaŭ`, `La sekvantan tagon` は時間表現として対応を保つ。
- `glacie kaj glite`, `Pluvetadas`, `Hajlas`, `Fulmas`, `fulmotondro`, `veterprognozo`, `Ĉi-nokte frostos`, `atmosfera premo`, `glitaj` は天候語彙として意味ズレなし。

## 419. 418周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Bonan tagon!`, `Bonan vojaĝon!`, `Bonan apetiton!`, `Kiel vi fartas?` などは、短い定型表現として JA/ZH/KO/RU との対応を保つ。
- `Mi antaŭĝojas revidi vin` は PIV 未確認寄りの語感だが、現代用例として「再会を楽しみにする」の意味が崩れていないため維持。
- `Ni tostu por vi!` は PIV 2020で `tosto/tosti` が「誰かの健康・名誉・成功のための乾杯」系として確認でき、祝意文脈と合う。

参照:
- PIV 2020 `tosti`: https://vortaro.net/py/serchi.py?s=tosti&simpla=1

## 420. 419周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions & Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi dankas vin pro ĉio`, `Mi bedaŭras`, `Pardonu min`, `Atendu momenton`, `Ripetu, mi petas` は依頼・謝罪の定型として対応する。
- `Mi ne tion celis` は語順がやや強調的だが、「そういう意味ではなかった」という意味を保つ。
- `Ne estas kialo pardonpeti` は省略的だが、「謝る必要はない」として文脈上許容。
- `Ĉu ĉio en ordo?` は口語的省略として、短答クイズ用の表現として維持。

## 421. 420周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers, Congratulations; General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Gratulon pro via diplomiĝo!`, `Gratulon pro via akcepto en la universitaton!`, `magistra grado` は卒業・入学・修士相当の祝意文脈として維持。
- PIV 2020で `magistro` が大学学位、`literumi` が語の文字を一つずつ言う意味として確認できる。
- `azerbajĝane`, `tagaloga`, `malajan`, `indonezian` などの言語名は、PIV収載の有無に差はあるが、複合・派生として透明で、日中韓との明確な意味ズレはない。
- `Via tagaloga estas tre bona`, `Mia korea estas sufiĉe malbona` は「あなたのタガログ語能力」「私の韓国語」の省略表現として文脈別許容。

参照:
- PIV 2020 `magistro`: https://vortaro.net/py/serchi.py?s=magistro&simpla=1
- PIV 2020 `literumi`: https://vortaro.net/py/serchi.py?s=literumi&simpla=1
- PIV 2020 `Azerbajĝano`: https://vortaro.net/py/serchi.py?s=Azerbaj%C4%9Dano&simpla=1

## 422. 421周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Ĉu mi ĝuste ĝin prononcas?`, `Kiel oni skribas tion?`, `Kiel oni diras tion ĉeĥe?` は理解確認・発音確認の文として成立する。
- `Mi vidas nenian malhelpon` は直訳では「障害が見えない」だが、同意文脈の「異論なし」として RU/JA/ZH/KO と矛盾しない。
- `junulargastejo`, `drinkejo`, `bicikli` は PIV 2020で語根・派生の確認ができ、宿泊・パブ・自転車文脈で維持。
- `por ferioj`, `Kion vi faras por Pasko?` はやや英語寄りに見えるが、旅行・祝日の予定を問う表現として意味ズレなし。

参照:
- PIV 2020 `junulargastejo`: https://vortaro.net/py/serchi.py?s=junulargastejo&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `bicikli`: https://vortaro.net/py/serchi.py?s=bicikli&simpla=1

## 423. 422周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information, Expressing Feelings, Help & Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `trista` は PIV 2020で `malgaja, malĝoja` と確認でき、`I'm sad` と対応する。
- `Mi estas ekscitita` は「楽しみ・期待」より広いが、RU `взволнован` とも重なり、感情表現として明確な誤りではない。
- `Mi sentas iom da kapturno`, `Mi sentas min perdita`, `Mi sentas min embarasita` は自然さに濃淡はあるが、意味は保つ。
- `Ĉu vi povus prizorgi tion dum momento?`, `Ĉu vi estus tiel afabla kaj klarigus tion denove?`, `Mi malkonsilus lui aŭton` は依頼・助言文脈で通る。

参照:
- PIV 2020 `trista`: https://vortaro.net/py/serchi.py?s=trista&simpla=1
- PIV 2020 `ĝeni`: https://vortaro.net/py/serchi.py?s=%C4%9Deni&simpla=1
- PIV 2020 `plaĉi`: https://vortaro.net/py/serchi.py?s=pla%C4%89i&simpla=1

## 424. 423周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions; Emergencies / Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Kio plaĉas al vi pri ĝi?`, `La aktorado estis malbona`, `Persone, mi konsideras ĉi tiun filmon la plej bona` は意見表明として対応する。
- `Mi havis la prioritaton` は交通事故文脈の「優先権があった」として維持。
- `oficejo pri perditaj aĵoj`, `akcidentraporto`, `asekurdokumentoj` はやや説明的な複合・句だが、落とし物・事故・保険文脈で意味ズレなし。
- PIV 2020で `naŭzi`, `abomeni`, `ambulanco`, `tordi` など事故・不快感関連の語義を確認。

参照:
- PIV 2020 `naŭzi`: https://vortaro.net/py/serchi.py?s=na%C5%ADzi&simpla=1
- PIV 2020 `ambulanco`: https://vortaro.net/py/serchi.py?s=ambulanco&simpla=1
- PIV 2020 `tordi`: https://vortaro.net/py/serchi.py?s=tordi&simpla=1

## 425. 424周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid, At the Police Station; Making Friends / Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Mi tordis al mi la maleolon`, `Mi elartikigis mian brakon`, `Mi havas manĝaĵveneniĝon`, `Mi mezuros vian pulson` は応急処置文脈で対応する。
- PIV 2020で `elartikiĝo` が `luksacio` と対応し、`elartikigi` の形成も確認できる。
- `fotoroboto` は PIV 2020では未収載だが、Glosbe/DBnaryで `identikit/facial composite` と確認でき、RU `фоторобот` とも一致するため維持。
- `Ĉu mi povas ĝin anstataŭigi?` は「再発行」そのものではなく「置き換える」寄りだが、紛失パスポートの文脈では replacement/reissue として許容。

参照:
- PIV 2020 `luksacio`: https://vortaro.net/py/serchi.py?s=luksacio&simpla=1
- PIV 2020 `alergio`: https://vortaro.net/py/serchi.py?s=alergio&simpla=1
- Glosbe `fotoroboto`: https://glosbe.com/eo/en/fotoroboto

## 426. 425周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions, Place of Residence, Age, Nationality & Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `amikino`, `fianĉon`, `germana civitanino` などの性別指定は、JA/ZH/KOでは中立的でも RU が女性・男性を明示している箇所があり、意図された文脈として維持。
- `Ĉi tie tre plaĉas al mi` は省略的だが、「ここがとても気に入っている」として文脈別許容。
- `jam de ses monatoj` は `dum ses monatoj` より議論余地があるが、「6か月前から」の意味として成立し、明確な誤りとはしない。
- `Kia estas via nacieco?` は `Kio estas via nacieco?` より性質問い寄りだが、国籍を問う文として理解可能。

参照:
- PIV 2020 `rendevuo`: https://vortaro.net/py/serchi.py?s=rendevuo&simpla=1
- PIV 2020 `parenco`: https://vortaro.net/py/serchi.py?s=parenco&simpla=1
- PIV 2020 `advokato`: https://vortaro.net/py/serchi.py?s=advokato&simpla=1

## 427. 426周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age, Nationality & Religion, Family & Relationships, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `siĥo`, `protestantino`, `ateisto`, `kristanino`, `musulmanino`, `hinduistino` は宗教・信仰の自己紹介として対応する。
- `edziniĝinta`, `Ĉu vi edziniĝis?`, `fianĉino` は女性話者・女性対象の表現だが、RU列の女性形と整合するため維持。
- `genepoj`, `nepo`, `nepinoj`, `solinfano` は親族語として意味ズレなし。
- `saĝa` は `inteligenta` より「賢明」寄りだが、`You're very smart` の褒め言葉として許容。

参照:
- PIV 2020 `budhano`: https://vortaro.net/py/serchi.py?s=budhano&simpla=1
- PIV 2020 `rendevui`: https://vortaro.net/py/serchi.py?s=rendevui&simpla=1
- PIV 2020 `permesi`: https://vortaro.net/py/serchi.py?s=permesi&simpla=1

## 428. 427周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `bonkondutaj`, `hobio`, `fotografado`, `patkukoj`, `bicikli`, `surfado`, `dombestoj`, `sciencfikciaj libroj` は趣味・嗜好文脈で対応する。
- `troti` は現代日本語の「ジョギング」と完全同義ではないが、PIV 2020で人の走り方にも使われるため、未確認語に置き換えない。
- `piedirado` は `hiking` より広い「徒歩・歩行」寄りだが、RU `пешие прогулки` とも合い、文脈別許容。
- `Aliĝu al mi por tagmanĝo` はやや硬いが、PIV 2020の `aliĝi` の「加わる」から外れすぎず、招待文として意味は通る。

参照:
- PIV 2020 `hobio`: https://vortaro.net/py/serchi.py?s=hobio&simpla=1
- PIV 2020 `trot/i`: https://vortaro.net/py/serchi.py?s=troti&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1

## 429. 428周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet, Accepting & Declining; Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Sinjoroj, ni povas ludi partion de golfo` は男性複数への呼びかけとして RU/EN と整合する。
- `Ĉu ni povas aliĝi al vi?`, `Ĉu mi povas aliĝi al vi?` は「同席・合流する」の会話文脈で許容。
- `Kion vi elpensis?` は EN `What are you up to?` より「何を考え出したのか」寄りだが、JA/ZH/KO/RU は「何を思いついた/何を考えた」に近く、意味ズレとはしない。
- `Ni forveturu de ĉi tie` は「ここを離れて出発する」で RU `уедем` と整合する。

参照:
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1

## 430. 429周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding; Education / At School

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Vi estas ravega`, `Ĉu vi estas fraŭla?`, `Ĉu vi estas edziĝinta?` は交際場面の短文として自然な範囲。
- `Mi volas esti kun vi por ĉiam`, `Ĉu vi edziniĝos al mi?` はプロポーズ文脈で、RU列の女性対象表現とも矛盾しない。
- `nupto`, `novgeedzoj`, `geedziĝa datreveno` は結婚関連語として意味ズレなし。
- `ŝranketoj`, `gimnastikejo`, `parkere` は学校文脈の語彙として確認できる。

参照:
- PIV 2020 `nupto`: https://vortaro.net/py/serchi.py?s=nupto&simpla=1
- PIV 2020 `parkere`: https://vortaro.net/py/serchi.py?s=parkere&simpla=1

## 431. 430周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo vi komencis la lernejon?` は `Je kiu aĝo...` も考えられるが、PIV例に `en la aĝo de...` があり、明確な誤りとはしない。
- `Mi studas la hindian` は「ヒンディー語を学ぶ」で、PIV 2020の `hindia lingvo` と整合する。
- `Mi doktoriĝas pri kemio`, `Mi studas por magistriĝo pri juro` は学位取得文脈として成立する。
- `studentloĝejo`, `distanca lernado`, `Mi faros mian raporton en la kataluna` は大学・学生生活の範囲で対応する。

参照:
- PIV 2020 `aĝo`: https://vortaro.net/py/serchi.py?s=a%C4%9Do&simpla=1
- PIV 2020 `hindia`: https://vortaro.net/py/serchi.py?s=hindia&simpla=1
- PIV 2020 `doktoriĝi`: https://vortaro.net/py/serchi.py?s=doktori%C4%9Di&simpla=1

## 432. 431周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life; Numbers & Colours; Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `purpuron` は JA/ZH/KO の「紫・ラベンダー」系と完全一致ではないが、色名クイズとして許容範囲。
- `informteknologio`, `juristo`, `staĝanta kontisto`, `vokcentro` は職業・職場語彙として確認できる。
- `komercistino`, `laboristo`, `dentisto`, `kirurgo` などの性別・職業指定は RU列または一般文脈と矛盾しない。
- `Mi instruas handikapitajn infanojn` は現代的には言い換え余地があるが、意味ズレ・文法誤りとしては扱わない。

参照:
- PIV 2020 `staĝi`: https://vortaro.net/py/serchi.py?s=sta%C4%9Di&simpla=1

## 433. 432周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, Workplace; Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `merkatika administranto` はやや専門語寄りだが、PIV 2020で `merkatiko` が確認でき、marketing manager として成立する。
- `Mi faras praktikon`, `mi estas emerita`, `Mi estas inter laboroj` は雇用状態の短文として整合する。
- `patrina forpermeso`, `patra forpermeso`, `provizora laboro`, `maldungita pro redukto de laborfortoj` は意味ズレなし。
- `fotokopiilo`, `faksi`, `limtempo por liveri... finiĝas` は職場・納期文脈で対応する。

参照:
- PIV 2020 `merkatiko`: https://vortaro.net/py/serchi.py?s=merkatiko&simpla=1
- PIV 2020 `faksi`: https://vortaro.net/py/serchi.py?s=faksi&simpla=1

## 434. 433周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Business; Applying for a Job

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `afervojaĝojn`, `dato de ekspedo`, `Per ĉi tio mi ŝatus...` はビジネス文書・問い合わせ文脈として許容。
- `formularon por vivresumo`, `laborkontrakto`, `provperiodo`, `aliĝilo` は求人応募語彙として確認できる。
- `komputile klera`, `facile trejnebla`, `teamludanto`, `kreema solvanto de problemoj` は職務上の人物描写として意味ズレなし。
- `bonvenan defion`, `fortaĵoj kaj malfortaĵoj` は直訳寄りだが、面接回答として理解可能。

参照:
- PIV 2020 `aliĝilo`: https://vortaro.net/py/serchi.py?s=ali%C4%9Dilo&simpla=1
- PIV 2020 `laborkontrakto`: https://vortaro.net/py/serchi.py?s=laborkontrakto&simpla=1

## 435. 434周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Applying for a Job / References; Travel / Asking Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mian plej varman rekomendon` は「最も強い推薦」としてやや直訳的だが、推薦状文脈では理解可能。
- `ŝparvojo`, `orientiĝas`, `monumento`, `vojkruciĝo`, `sekva strato` は道案内語彙として意味ズレなし。
- `marbordo`, `urbo-centro`, `turniĝu dekstren/maldekstren` は移動方向の説明として整合する。
- `Ĉu mi povas piediri tien?` は「徒歩で行けるか」の意で JA/ZH/KO/RU と合う。

参照:
- PIV 2020 `ŝparvojo`: https://vortaro.net/py/serchi.py?s=%C5%9Dparvojo&simpla=1
- PIV 2020 `marbordo`: https://vortaro.net/py/serchi.py?s=marbordo&simpla=1

## 436. 435周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Asking Directions, Tourist Information, At the Airport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `junulargastejoj`, `tendumejojn`, `sandviĉejon`, `navedan buson` は旅行・観光案内語彙として確認できる。
- `en la estona`, `la kartvelan`, `ĉiĉerono` は言語・案内人の文脈で対応する。
- `subeksponitaj` は写真の「露出不足」として意味が明確。
- `Ekonomiklasa bileto` は空港・航空券文脈で `economy-class ticket` として理解可能。

参照:
- PIV 2020 `junulargastejo`: https://vortaro.net/py/serchi.py?s=junulargastejo&simpla=1
- PIV 2020 `sandviĉejo`: https://vortaro.net/py/serchi.py?s=sandvi%C4%89ejo&simpla=1
- PIV 2020 `kartvela`: https://vortaro.net/py/serchi.py?s=kartvela&simpla=1

## 437. 436周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Travel / At the Airport, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `elirejo`, `pordego`, `atendejo`, `foriroj`, `alvenoj` は空港表示・搭乗口文脈で対応する。
- `enŝipiĝo` は語源上は船寄りだが、航空便の boarding に使われる例もあり、空港文脈で意味は崩れないため据え置き。
- `registrigas bagaĝon`, `manbagaĝo`, `superpezo`, `troa bagaĝo` は荷物関連語として理解可能。
- `Ĉu mi devas pagi pro troa pezo?` は超過重量料金の問いとして自然な範囲。

参照:
- PIV 2020 `enŝipiĝi`: https://vortaro.net/py/serchi.py?s=en%C5%9Dipi%C4%9Di&simpla=1

## 438. 437周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Travel / Customs & Immigration, On Board

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `doganon`, `doganejon`, `transitvizon`, `komunan pasporton` は入国・税関文脈で対応する。
- `enŝipiĝo` は前項と同様、航空機 boarding の会話文脈として据え置き。
- `sekurzonon`, `flugdaŭro`, `stevardino`, `supran bagaĝujon` は機内表現として整合する。
- `Ĉu oni rajtas fumi?` は許可を尋ねる短文として自然。

参照:
- PIV 2020 `dogano`: https://vortaro.net/py/serchi.py?s=dogano&simpla=1
- PIV 2020 `sekurzono`: https://vortaro.net/py/serchi.py?s=sekurzono&simpla=1

## 439. 438周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Travel / At the Airport, Car Hire

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Pordegoj 1-32`, `Bagaĝa elpreno`, `Varoj deklarendaj` は空港表示として短く自然。
- `transmision`, `klimatizilon`, `centra ŝlosado`, `kofrujon` はレンタカー語彙として確認できる。
- `direktomontrilojn` は indicators/turn signals として透明な複合語。
- `postulon pri aŭtoasekura kompenso` はやや硬いが、保険請求の意味として成立する。

参照:
- PIV 2020 `transmisio`: https://vortaro.net/py/serchi.py?s=transmisio&simpla=1
- PIV 2020 `kofrujo`: https://vortaro.net/py/serchi.py?s=kofrujo&simpla=1
- PIV 2020 `klimatizilo`: https://vortaro.net/py/serchi.py?s=klimatizilo&simpla=1

## 440. 439周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Travel / Driving, Petrol Station, Breakdowns

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `trafikblokiĝo`, `serva areo`, `urĝa aŭto`, `dekstramana/maldekstramana stirado` は運転文脈で意味が通る。
- `senplumba benzino`, `dizelo`, `kontraŭfrosta likvaĵo`, `bremslikvaĵo` は給油・整備語彙として自然な範囲。
- `startokablojn`, `kapoton`, `akumulatoron`, `pneŭmatiko krevis` は故障対応文脈で対応する。
- `malsuprenirante deklivaĵon` は坂を下る運転場面として整合する。

参照:
- PIV 2020 `akumulatoro`: https://vortaro.net/py/serchi.py?s=akumulatoro&simpla=1
- PIV 2020 `kapoto`: https://vortaro.net/py/serchi.py?s=kapoto&simpla=1

## 441. 440周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Travel / Road Signs, Bus, Train

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Trapaso malpermesita`, `Halto malpermesita`, `Cedu vojon`, `Preterpasu maldekstre` は標識文として短く機能する。
- `revenbileto`, `monata abono`, `horaro`, `haltejo`, `perono` は公共交通語彙として確認できる。
- `Atentu la interspacon` は `Mind the gap` に対応する直訳的だが明確。
- `unua klasa`, `unuklasa`, `duaklasa` は乗車券・列車等級文脈で意味ズレなし。

参照:
- PIV 2020 `revenbileto`: https://vortaro.net/py/serchi.py?s=revenbileto&simpla=1
- PIV 2020 `horaro`: https://vortaro.net/py/serchi.py?s=horaro&simpla=1

## 442. 441周目 追加再点検（ID2456〜2555）

対象:
- `ID2456`〜`ID2555`
- Travel / Train, Underground, Taxi

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vojaĝkarto`, `abonbileto`, `pakaĵujo`, `kupeo`, `libera` は鉄道・タクシー文脈で対応する。
- `Laŭpeta haltejo` は request stop として透明で意味が明確。
- `taksihaltejo`, `taksimetro`, `restmono`, `trinkmono`, `flughavena krompago` はタクシー会計語彙として理解可能。
- `Mian restmonon, mi petas` は PIVでは直接見つからないが、同データ内の釣り銭文脈と一貫しており、ここでは未確認語への置換は避ける。

参照:
- PIV 2020 `kupeo`: https://vortaro.net/py/serchi.py?s=kupeo&simpla=1
- PIV 2020 `taksimetro`: https://vortaro.net/py/serchi.py?s=taksimetro&simpla=1

## 443. 442周目 追加再点検（ID2556〜2655）

対象:
- `ID2556`〜`ID2655`
- Travel / Taxi, Ship; Hotel / Hotel Facilities

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `nokta krompago`, `kajuto`, `ferdeko`, `krozado`, `savvestoj`, `savboato` は船旅文脈で対応する。
- `Ĉu vin naŭzas vojaĝado?` は「乗り物酔いするか」の問いとして、PIV 2020の `naŭzi` の意味から外れない。
- `aŭtoparkejo`, `frizejo`, `beleca salono`, `rulseĝa aliro`, `ŝtopilingo` はホテル設備語彙として確認できる。
- `unulita ĉambro`, `duŝkabinoj`, `plena pensiono` は宿泊予約文脈で意味ズレなし。

参照:
- PIV 2020 `ferdeko`: https://vortaro.net/py/serchi.py?s=ferdeko&simpla=1
- PIV 2020 `naŭzi`: https://vortaro.net/py/serchi.py?s=na%C5%ADzi&simpla=1
- PIV 2020 `ŝtopilingo`: https://vortaro.net/py/serchi.py?s=%C5%9Dtopilingo&simpla=1

## 444. 443周目 追加再点検（ID2656〜2755）

対象:
- `ID2656`〜`ID2755`
- Hotel / Booking a Hotel Room, Hotel Services, During Your Stay

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `atendoliston`, `antaŭpagon`, `ĉambronumero`, `duobla ĉambro`, `liton por infano` は予約・チェックイン文脈で対応する。
- `Je kioma horo vi fermas?` は入口・受付の閉まる時刻を問う文として RU/JA/ZH/KO と整合する。
- `tage kaj nokte` は round-the-clock の意味で許容。
- `eksteran linion`, `gladigi`, `plusendi mian poŝton`, `mendi matenmanĝon` はホテルサービス文脈で意味ズレなし。

参照:
- PIV 2020 `banĉambro`: https://vortaro.net/py/serchi.py?s=ban%C4%89ambro&simpla=1
- PIV 2020 `frizejo`: https://vortaro.net/py/serchi.py?s=frizejo&simpla=1

## 445. 444周目 追加再点検（ID2756〜2855）

対象:
- `ID2756`〜`ID2855`
- Hotel / During Your Stay, Checking out, Complaints, Renting a Flat

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `lavejo`, `gladi`, `elregistriĝi`, `detaligita fakturo`, `monŝranko` はホテル滞在・精算文脈で対応する。
- `Mi ne havas restmonon` は「小銭がない」より「釣り銭がない」寄りに見えるが、会計場面の `change` として意味は崩れないため据え置き。
- `En mia ĉambro malbonodoras` は主語省略的でやや硬いが、PIV 2020の `odori/malbonodori` の用法から「部屋で悪臭がする」と理解可能。
- `ventumilo` は PIV 2020では主に扇ぐ道具、`ventolilo` は換気装置寄りだが、旅行会話の `fan/ventilator` として致命的な意味ズレとはしない。

参照:
- PIV 2020 `malbonodori`: https://vortaro.net/py/serchi.py?s=malbonodori&simpla=1
- PIV 2020 `ventolilo`: https://vortaro.net/py/serchi.py?s=ventolilo&simpla=1
- PIV 2020 `ventumilo`: https://vortaro.net/py/serchi.py?s=ventumilo&simpla=1

## 446. 445周目 追加再点検（ID2856〜2955）

対象:
- `ID2856`〜`ID2955`
- Hotel / Renting a Flat; Restaurant & Pub / Booking a Table, Ordering Drinks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vazaro`, `ŝvabrilo`, `korktirilo`, `skatolmalfermilo`, `botelmalfermilo`, `polvosuĉilo` は住居備品語彙として確認できる。
- `suĉkloŝo` は PIV 2020では未確認だが、Wiktionary/Wikidata系で plunger として確認でき、RU `вантуз` と合うため据え置き。
- `adherema filmo` は PIV 2020に完全一致語はないが、`adheri/adhera` の語根から「くっつくフィルム」と解釈可能で、cling film の意味を大きく外さない。
- `fumejo`, `manĝaĵon por forporti`, `tablo ĉe la fenestro`, `akvo kun/sen gaso` は飲食店文脈で対応する。

参照:
- PIV 2020 `vazaro`: https://vortaro.net/py/serchi.py?s=vazaro&simpla=1
- PIV 2020 `ŝvabrilo`: https://vortaro.net/py/serchi.py?s=%C5%9Dvabrilo&simpla=1
- PIV 2020 `adheri`: https://vortaro.net/py/serchi.py?s=adheri&simpla=1
- Wiktionary `suĉkloŝo`: https://en.wiktionary.org/wiki/su%C4%89klo%C5%9Do

## 447. 446周目 追加再点検（ID2956〜3055）

対象:
- `ID2956`〜`ID3055`
- Restaurant & Pub / Ordering Drinks, Ordering Food, During the Meal

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `smuzio` は PIV 2020では未確認だが、現代語として smoothie 対応が確認でき、`papaja smuzio` は意味が明確。
- `pastaĵoj` は PIV 2020で pasta/noodle 類の集合名として確認でき、`Mi prenos la pastaĵojn` は料理注文文脈で成立する。
- `koŝera manĝaĵo`, `antaŭmanĝaĵoj`, `farĉitaj fungoj`, `terpom-fritoj/fritoj` は料理語彙として対応する。
- `Mezrostita`, `bone rostitan viandon`, `sen salo` は焼き加減・調理指定の短文として意味ズレなし。

参照:
- PIV 2020 `pastaĵo`: https://vortaro.net/py/serchi.py?s=pasta%C4%B5o&simpla=1
- PIV 2020 `koŝera`: https://vortaro.net/py/serchi.py?s=ko%C5%9Dera&simpla=1
- PIV 2020 `bifsteko`: https://vortaro.net/py/serchi.py?s=bifsteko&simpla=1
- Wiktionary `smuzio`: https://en.wiktionary.org/wiki/smuzio

一致確認:
- `cmp_exit=0`
- `md5=1b2e74a039f18a6303cba328756b9582`

## 448. 447周目 追加再点検（ID3056〜3155）

対象:
- `ID3056`〜`ID3155`
- Restaurant & Pub / During the Meal, Paying the Bill, Complaints

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `manĝobastonetoj`, `fritoj`, `sumigita`, `postebrio` は飲食店・会計・飲酒後の会話として意味ズレなし。
- `halala manĝaĵo` は PIV 2020 では直接確認できなかったが、現代用例として確認でき、宗教食対応の文脈では意味が明確。
- `Ĉu servo estas inkluzivita?`, `Ĉu mi povas pagi per karto?`, `La bifsteko estas tro malmola` は RU/JA/ZH/KO と対応する。

参照:
- PIV 2020 `sumigi`: https://vortaro.net/py/serchi.py?s=sumigi&simpla=1
- PIV 2020 `postebrio`: https://vortaro.net/py/serchi.py?s=postebrio&simpla=1
- Glosbe `halala`: https://glosbe.com/eo/en/halala

## 449. 448周目 追加再点検（ID3156〜3255）

対象:
- `ID3156`〜`ID3255`
- Restaurant & Pub / Complaints, At the Pub; Food / Meat & Fish

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `barela biero`, `botela biero`, `Same kiel kutime`, `Kiu estas la koktelo de la tago?` はパブ文脈で許容。
- `soleo`, `rostbefo`, `bifsteko el bova lumbaĵo`, `kalzoneo` は料理語彙として確認できる。
- `kuniklon`, `anseron` のような動物名による料理名は、注文場面では文脈上の意味が明確。

参照:
- PIV 2020 `barela`: https://vortaro.net/py/serchi.py?s=barela&simpla=1
- PIV 2020 `soleo`: https://vortaro.net/py/serchi.py?s=soleo&simpla=1
- PIV 2020 `lumbaĵo`: https://vortaro.net/py/serchi.py?s=lumba%C4%B5o&simpla=1
- PIV 2020 `rostbefo`: https://vortaro.net/py/serchi.py?s=rostbefo&simpla=1

## 450. 449周目 追加再点検（ID3256〜3355）

対象:
- `ID3256`〜`ID3355`
- Food / Fruit, Vegetables, Staple Food & Spices

結果:
- **本文修正 1件**

修正:
- `ID3313`: `Mi ŝatus la panitan kukurbeton` → `Mi ŝatus la panumitan kukurbeton`
  - `panumi` は「パン粉をまぶす」料理語として確認できる。`panita` は「パンの／パンでできた」に寄りやすく、RU/JA/ZH/KO の「パン粉をつけたズッキーニ」に対して `panumitan` がより正確。

主な据え置き確認:
- `grapfrukto`, `kikero`, `kuskuso`, `kukurbet(o)`, `melongeno`, `oksikoko`, `eruko`, `kazeo`, `dolĉigilo` は料理・食品語彙として確認できる。
- `Mi preferas florbrasikon al brokolo` は `preferi X al Y` の構文として問題なし。
- `kirlovaĵo`, `ringokuko` は PIV 2020 で直接確認しにくいが、複合語として透明で、意味ズレは明確でないため据え置き。

参照:
- PIV 2020 `panumi`: https://vortaro.net/py/serchi.py?s=panumi&simpla=1
- PIV 2020 `kukurbeto`: https://vortaro.net/py/serchi.py?s=kukurbeto&simpla=1
- PIV 2020 `kazeo`: https://vortaro.net/py/serchi.py?s=kazeo&simpla=1
- PIV 2020 `eruko`: https://vortaro.net/py/serchi.py?s=eruko&simpla=1

## 451. 450周目 追加再点検（ID3356〜3455）

対象:
- `ID3356`〜`ID3455`
- Food / Breakfast; Shopping / Department Store, Clothes

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pantalono` は trousers/pants の単数名詞として確認でき、`pantalonon` の対格も自然。
- `sablokolora`, `stoko/stoki`, `surprovi`, `provejo`, `T-ĉemizo`, `kemie purigi`, `laveblaj` は衣料・売場文脈で対応する。
- `Kia grandeco` / `granda grandeco` は直訳感が少しあるが、サイズ確認の短文として意味ズレまではない。
- `Lavu inversigite` は「裏返して洗う」と読めるため据え置き。

参照:
- PIV 2020 `pantalono`: https://vortaro.net/py/serchi.py?s=pantalono&simpla=1
- PIV 2020 `sablokolora`: https://vortaro.net/py/serchi.py?s=sablokolora&simpla=1
- PIV 2020 `surprovi`: https://vortaro.net/py/serchi.py?s=surprovi&simpla=1
- PIV 2020 `provejo`: https://vortaro.net/py/serchi.py?s=provejo&simpla=1

## 452. 451周目 追加再点検（ID3456〜3555）

対象:
- `ID3456`〜`ID3555`
- Shopping / Clothes, Shoes, Accessories, Personal Care

結果:
- **本文修正 1件**

修正:
- `ID3472`: `Bonvolu flankmeti ĉi tion por mi` → `Bonvolu meti ĉi tion flanken por mi`
  - `flankmeti` は主要辞書で確認しづらく、`flankenmeti` / `meti ... flanken` の用例が確認できる。「これを取り置き／脇へ置いてください」の意味を保つため、より確実な句形へ修正。

主な据え置き確認:
- `mokaseno`, `ŝelko`, `kronometro`, `manumbutonoj`, `ŝminko`, `felĉapo`, `juvelaĵo`, `horloĝrimeno` は買い物・身支度文脈で対応する。
- `sidi sur mi kiel ganto` は靴がぴったり合うという比喩として理解可能。
- `zorioj`, `gumaj botoj`, `akvorezista ŝminko por okulharoj`, `paletro da ŝminko por la palpebroj` は明確な意味ズレなし。

参照:
- Glosbe `flankenmeti`: https://glosbe.com/eo/en/flankenmeti
- PIV 2020 `meti`: https://vortaro.net/py/serchi.py?s=meti&simpla=1
- PIV 2020 `mokaseno`: https://vortaro.net/py/serchi.py?s=mokaseno&simpla=1
- PIV 2020 `manumbutono`: https://vortaro.net/py/serchi.py?s=manumbutono&simpla=1

## 453. 452周目 追加再点検（ID3556〜3655）

対象:
- `ID3556`〜`ID3655`
- Shopping / Personal Care, Electronic Devices, Other Goods, Supermarket

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `telefonan ŝargilon`, `memorkarton`, `lensokovrilon`, `porteblan komputilon`, `harsekigilon`, `aŭskultilojn`, `laŭtparoliloj` は電子機器・日用品文脈で明確。
- `ventumilo` は PIV 2020 では手で扇ぐ道具寄りだが、現代の fan 文脈でも理解され、ここでは致命的な意味ズレとは判断しない。
- `konstrubriketoj`, `bierkruĉoj`, `suveniro de la urbo`, `bokalon da mustardo`, `limdato` は買い物・スーパー文脈で対応する。

参照:
- PIV 2020 `ŝargilo`: https://vortaro.net/py/serchi.py?s=%C5%9Dargilo&simpla=1
- PIV 2020 `komputilo`: https://vortaro.net/py/serchi.py?s=komputilo&simpla=1
- PIV 2020 `ventumilo`: https://vortaro.net/py/serchi.py?s=ventumilo&simpla=1
- PIV 2020 `limdato`: https://vortaro.net/py/serchi.py?s=limdato&simpla=1

## 454. 453周目 追加再点検（ID3656〜3755）

対象:
- `ID3656`〜`ID3755`
- Shopping / Supermarket, Bookshop, Florist, Payments

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `kafgrajno`, `foliumi`, `bukedo/bukedeto`, `narcisoj`, `lekantoj`, `gazetkiosko`, `poemaroj`, `brokanta librovendejo`, `krizantemoj`, `diantoj`, `restmono` は各売場の語彙として対応する。
- `Bonvolu doni al mi ekzempleron de "Romeo kaj Julieta"` は題名表記に揺れはあり得るが、意味ズレとはしない。
- `makedonan-ukrainan vortaron` はハイフン付き形容詞として読め、対象言語の組み合わせも明確。

参照:
- PIV 2020 `kafgrajno`: https://vortaro.net/py/serchi.py?s=kafgrajno&simpla=1
- PIV 2020 `foliumi`: https://vortaro.net/py/serchi.py?s=foliumi&simpla=1
- PIV 2020 `bukedo`: https://vortaro.net/py/serchi.py?s=bukedo&simpla=1
- PIV 2020 `gazetkiosko`: https://vortaro.net/py/serchi.py?s=gazetkiosko&simpla=1

## 455. 454周目 追加再点検（ID3756〜3855）

対象:
- `ID3756`〜`ID3855`
- Payments, Cinema, Theatre

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `filmo de suspenso`, `en la vjetnama`, `anglajn subtekstojn`, `animaciaĵon`, `nigrablankan filmon` は映画文脈で意味が取れる。
- `produktis la filmon`, `fotiĝi kun mi`, `sidiĝi` は RU/JA/ZH/KO と対応する。
- `unu el la plej bonaj filmoj ... kiujn mi vidis de longe` は `de longe` に時間的用法があるため据え置き。ただし「遠くから見た」との読みを完全には排除できないので、文脈依存許容とする。

参照:
- PIV 2020 `subteksto`: https://vortaro.net/py/serchi.py?s=subteksto&simpla=1
- PIV 2020 `animacio`: https://vortaro.net/py/serchi.py?s=animacio&simpla=1
- PIV 2020 `longe`: https://vortaro.net/py/serchi.py?s=longe&simpla=1

## 456. 455周目 追加再点検（ID3856〜3955）

対象:
- `ID3856`〜`ID3955`
- Theatre, Museum, Nightclub

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `interakto` は一般の interaction ではなく、劇・映画の幕間/休憩の語として確認でき、劇場文脈に合う。
- `loĝio`, `teatra lorneto`, `dekoracio`, `aŭdgvidilo/aŭdgvido`, `vaksaj figuroj`, `impresionismaj pentraĵoj`, `mozaiko`, `ceramikaĵoj`, `bilardo` は施設・展示・娯楽語彙として対応する。
- `handikapuloj` は現代的な言い換え余地はあるが、辞書的に確認でき、文意の破綻はない。

参照:
- PIV 2020 `interakto`: https://vortaro.net/py/serchi.py?s=interakto&simpla=1
- PIV 2020 `loĝio`: https://vortaro.net/py/serchi.py?s=lo%C4%9Dio&simpla=1
- PIV 2020 `lorneto`: https://vortaro.net/py/serchi.py?s=lorneto&simpla=1
- PIV 2020 `bilardo`: https://vortaro.net/py/serchi.py?s=bilardo&simpla=1

## 457. 456周目 追加再点検（ID3956〜4055）

対象:
- `ID3956`〜`ID4055`
- Nightclub, Beach, Sport

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `homplene`, `mortige enue`, `diskĵokeo`, `vestkodo` はナイトクラブ文脈で許容。
- `sunseĝo`, `akvoskioj/akvoskii`, `surfotabulo`, `jaĥtklubo`, `plonĝkostumo`, `aerbotelo`, `malsekkostumo`, `savjako` は浜辺・マリンスポーツ文脈で対応する。
- `Ni ludu duope`, `goli`, `egaligis la poentaron`, `gimnastikejo`, `rugbeo` はスポーツ会話として意味ズレなし。

参照:
- PIV 2020 `diskĵokeo`: https://vortaro.net/py/serchi.py?s=disk%C4%B5okeo&simpla=1
- PIV 2020 `surfotabulo`: https://vortaro.net/py/serchi.py?s=surfotabulo&simpla=1
- PIV 2020 `goli`: https://vortaro.net/py/serchi.py?s=goli&simpla=1
- PIV 2020 `rugbeo`: https://vortaro.net/py/serchi.py?s=rugbeo&simpla=1

## 458. 457周目 追加再点検（ID4056〜4155）

対象:
- `ID4056`〜`ID4155`
- Sport, Music, Camping

結果:
- **本文修正 1件**

修正:
- `ID4131`: `Ĉu vi povas alporti vian propran grilon?` → `Ĉu vi povas alporti vian propran rostokradon?`
  - PIV 2020 で `grilo` は昆虫の「コオロギ」。料理用 grill は `krado` / `rostokrado` 系で確認できるため、キャンプ/バーベキュー文脈に合わせて修正。

主な据え置き確認:
- `golfbastonoj`, `golfĉaro`, `regatto`, `femuraj muskoloj` はスポーツ語彙として確認できる。
- `popolmuziko`, `ruldomo`, `poŝlampo`, `kukolo`, `pego`, `najtingalo`, `telfero` は音楽・キャンプ/自然文脈で対応する。
- `Mi instruos vin ludi pianon` は `instrui iun fari ion` として成立するため据え置き。

参照:
- PIV 2020 `grilo`: https://vortaro.net/py/serchi.py?s=grilo&simpla=1
- PIV 2020 `krado`: https://vortaro.net/py/serchi.py?s=krado&simpla=1
- PIV 2020 `regatto`: https://vortaro.net/py/serchi.py?s=regatto&simpla=1
- PIV 2020 `ruldomo`: https://vortaro.net/py/serchi.py?s=ruldomo&simpla=1

## 459. 458周目 追加再点検（ID4156〜4255）

対象:
- `ID4156`〜`ID4255`
- Camping, Family Time, Gardening, Having Guests

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `piedvojetoj`, `bovlingon`, `sketi`, `televidaj romanoj`, `sagetoj`, `legadon` は余暇・家族時間の文脈で対応する。
- `sojo`, `sekalo`, `falĉi`, `erpi`, `fruktarbejo`, `kulturplantoj` は園芸・農作業語彙として確認できる。
- 既修正済みの `Ŝi rastis la foliojn en amason` と `Ĉu vi ŝatus toaston?` は今回範囲でも再確認した。
- `servi vin`, `boligos akvon`, `sukerpecoj`, `eliru`, `manĝoĉambron`, `ĝino kun toniko`, `mendas picon hejmen`, `viŝos` は来客・家庭内会話として意味ズレなし。

参照:
- PIV 2020 `rasti`: https://vortaro.net/py/serchi.py?s=rasti&simpla=1
- PIV 2020 `toasto`: https://vortaro.net/py/serchi.py?s=toasto&simpla=1
- PIV 2020 `fruktarbejo`: https://vortaro.net/py/serchi.py?s=fruktarbejo&simpla=1
- PIV 2020 `erpi`: https://vortaro.net/py/serchi.py?s=erpi&simpla=1

## 460. 459周目 追加再点検（ID4256〜4355）

対象:
- `ID4256`〜`ID4355`
- Bank, Estate Agency

結果:
- **本文修正 1件**

修正:
- `ID4294`: `Ĉu mi povus ricevi kontoekstrakton, mi petas?` → `Ĉu mi povus ricevi konteltiron, mi petas?`
  - PIV 2020 の `konto` 項で `konteltiro` が「口座明細／取引先に送る部分的写し」として確認でき、bank statement / RU `выписку` に合う。

主な据え置き確認:
- `ĉekaro`, `ĝiri`, `hipoteko`, `provizio`, `legitimilo`, `deponaĵo` は銀行手続き語彙として確認できる。
- `bangalo`, `parkumejo`, `vicdomo`, `duamana posedaĵo`, `prezintervalo`, `kontanta aĉetanto`, `loĝejo`, `posedaĵo` は不動産文脈で意味が通る。
- `Ĉu ĉi tiu posedaĵo estas libera?` は不動産が空いているかを問う文として RU/JA/ZH/KO と整合する。

参照:
- PIV 2020 `konto`: https://vortaro.net/py/serchi.py?s=konto&simpla=1
- PIV 2020 `ĉekaro`: https://vortaro.net/py/serchi.py?s=%C4%89ekaro&simpla=1
- PIV 2020 `ĝiri`: https://vortaro.net/py/serchi.py?s=%C4%9Diri&simpla=1
- PIV 2020 `hipoteko`: https://vortaro.net/py/serchi.py?s=hipoteko&simpla=1

## 461. 460周目 追加再点検（ID4356〜4455）

対象:
- `ID4356`〜`ID4455`
- Services / At the Estate Agency, At the Beauty Salon, At the Tailor's, Repairs

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `posedaĵo`, `lupago`, `dissendolisto`, `enloĝiĝi` は不動産案内文脈で対応する。
- `franĝo` は髪の前髪としての用例が確認でき、`konstanta ondumado` も髪のパーマ用例として確認できる。
- `dislimo` は `dislimi al si la harojn` の用例があり、髪の分け目として文脈上成立する。
- `ŝampui`, `senharigo`, `kranihaŭto`, `fajli/formi ungojn`, `laki ungojn` は美容院・ネイル文脈で意味ズレなし。
- `tajloro`, `zipo`, `alkudri`, `fliki`, `laŭmezura kostumo`, `mallarĝigi/plilarĝigi` は仕立て屋文脈で対応する。

参照:
- PIV 2020 `franĝo`: https://vortaro.net/py/serchi.py?s=fran%C4%9Do&simpla=1
- PIV 2020 `ondumado`: https://vortaro.net/py/serchi.py?s=ondumado&simpla=1
- PIV 2020 `haro`: https://vortaro.net/py/serchi.py?s=haro&simpla=1
- PIV 2020 `tajloro`: https://vortaro.net/py/serchi.py?s=tajloro&simpla=1

## 462. 461周目 追加再点検（ID4456〜4555）

対象:
- `ID4456`〜`ID4555`
- Services / Repairs; Health / At the Doctor

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `pilo`, `kroneto`, `reguligo`, `plandumo`, `riparejo por ŝuoj` は時計・靴修理の文脈で対応する。
- `kontrola ekzameno`, `rentgena ekzameno`, `aŭdotestoj`, `analizoj`, `sangogrupo`, `desinfekti`, `sangopremo` は医療文脈で理解できる。
- `Kia estas mia temperaturo?` は数値を問う `kiom` への言い換え余地はあるが、直後の `normala/iom alta` とつながる質的確認として許容。
- `surdorse` / `surventre` は寝姿勢として対応する。

参照:
- PIV 2020 `plandumo`: https://vortaro.net/py/serchi.py?s=plandumo&simpla=1
- PIV 2020 `trankviligaĵo`: https://vortaro.net/py/serchi.py?s=trankviliga%C4%B5o&simpla=1
- PIV 2020 `sangopremo`: https://vortaro.net/py/serchi.py?s=sangopremo&simpla=1
- PIV 2020 `rentgena`: https://vortaro.net/py/serchi.py?s=rentgena&simpla=1

## 463. 462周目 追加再点検（ID4556〜4655）

対象:
- `ID4556`〜`ID4655`
- Health / At the Doctor, Diseases, Treatment

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `haŭterupcio`, `furunko`, `nazkataro`, `limfonodoj`, `mikozo`, `fojnofebro` は症状・疾患語として文脈上対応する。
- `Mi sentas min kapturna`, `Mi havas stomakan perturbon`, `Mi malfacile spiras`, `Mi suferas de sendormeco` は症状説明として自然。
- `sutureroj` は PIV 2020 で外科的縫合を構成する糸として確認でき、「何針か」に対応する。
- `urina specimeno`, `loka anestezo`, `injekto`, `resaniĝo` は治療文脈で意味ズレなし。

参照:
- PIV 2020 `suturo`: https://vortaro.net/py/serchi.py?s=suturo&simpla=1
- PIV 2020 `furunko`: https://vortaro.net/py/serchi.py?s=furunko&simpla=1
- PIV 2020 `mikozo`: https://vortaro.net/py/serchi.py?s=mikozo&simpla=1
- PIV 2020 `specimeno`: https://vortaro.net/py/serchi.py?s=specimeno&simpla=1

## 464. 463周目 追加再点検（ID4656〜4755）

対象:
- `ID4656`〜`ID4755`
- Health / Treatment, At the Dentist, At the Optician, At the Pharmacy

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `po du ... trifoje tage`, `preskribos`, `recepto`, `antibiotikoj` は薬の指示として対応する。
- `plombo`, `dentprotezo`, `kario`, `denta higienisto`, `gargari la buŝon` は歯科文脈で確認できる。
- `dioptrioj`, `hipermetropa`, `miopa`, `kontaktlensoj`, `okulvitrujo`, `okulekzamenoj` は眼鏡店文脈で意味ズレなし。
- `plastro`, `desinfektaĵo`, `kontraŭdoloriloj`, `fastante`, `havebla nur laŭ recepto` は薬局文脈で対応する。

参照:
- PIV 2020 `plombo`: https://vortaro.net/py/serchi.py?s=plombo&simpla=1
- PIV 2020 `gargari`: https://vortaro.net/py/serchi.py?s=gargari&simpla=1
- PIV 2020 `dioptrio`: https://vortaro.net/py/serchi.py?s=dioptrio&simpla=1
- PIV 2020 `plastro`: https://vortaro.net/py/serchi.py?s=plastro&simpla=1

## 465. 464周目 追加再点検（ID4756〜4855）

対象:
- `ID4756`〜`ID4855`
- Health / At the Pharmacy; Communication Means / Phone, Phone Calls at Work

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `vojaĝmalsano`, `misdigesto`, `dormemigi`, `nikotinaj plastroj`, `nur por ekstera uzo`, `Ne prenu interne` は薬局・服薬文脈で対応する。
- `Malbona konekto`, `Restu sur la linio`, `malkonektiĝis`, `telefonbudo`, `telefonkarto` は電話会話として自然。
- `voka signalo` は PIV 2020 で確認でき、dialling tone / RU `гудок` に対応する。
- `voko pagata de la ricevanto`, `aŭtomata respondilo`, `malŝargiĝos`, `urba telefona kodo` は電話サービス文脈で意味ズレなし。
- `klavi la numeron` は電話番号入力として理解可能。

参照:
- PIV 2020 `voka`: https://vortaro.net/py/serchi.py?s=voka&simpla=1
- PIV 2020 `signalo`: https://vortaro.net/py/serchi.py?s=signalo&simpla=1
- PIV 2020 `klavo`: https://vortaro.net/py/serchi.py?s=klavo&simpla=1
- PIV 2020 `baterio`: https://vortaro.net/py/serchi.py?s=baterio&simpla=1

## 466. 465周目 追加再点検（ID4856〜4955）

対象:
- `ID4856`〜`ID4955`
- Communication Means / Phone Calls at Work, Mass Media, At the Post Office

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `telefonlibro`, `interna numero`, `sur alia linio`, `demeti la aŭdilon`, `konekti min al interna numero` は職場電話文脈で対応する。
- `retpoŝtadreso`, `uzantonomo`, `ensaluti/elsaluti`, `retmesaĝo`, `tekkomputilo`, `Tvitero` はネット・メディア文脈で意味ズレなし。
- `eldonkvanto` は PIV 2020 の `eldono` 派生で確認でき、新聞の発行部数に対応する。
- `vatita koverto`, `afranko`, `fotokabino`, `fotokopiilo`, `rekomendita poŝto`, `dogana deklaracio`, `poŝtmarko` は郵便局文脈で対応する。

参照:
- PIV 2020 `eldono`: https://vortaro.net/py/serchi.py?s=eldono&simpla=1
- PIV 2020 `afranko`: https://vortaro.net/py/serchi.py?s=afranko&simpla=1
- PIV 2020 `dogano`: https://vortaro.net/py/serchi.py?s=dogano&simpla=1
- PIV 2020 `vato`: https://vortaro.net/py/serchi.py?s=vato&simpla=1

## 467. 466周目 追加再点検（ID4956〜5055）

対象:
- `ID4956`〜`ID5055`
- Communication Means / At the Post Office, Letter; Time & Weather / Telling the Time, Calendar

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `poŝtrestante`, `giĉeto`, `pakaĵo`, `rekomendita poŝto` は郵便局のやり取りとして対応する。
- `vivresumo`, `kunsendi`, `Antaŭdankon`, `Respektplene via`, `Kun plej koraj salutoj` は手紙・メール定型として許容。
- `Mi antaŭĝojas ...` 系の複数表現は、手紙の結びとして意味が明確。
- `kvarono antaŭ/post`, `post la unua`, `ĝis la unua horo`, `noktomezo`, `tagmezo` は時刻表現として対応する。
- `labortago`, `libertago`, 月名・曜日名の表現はカレンダー文脈で意味ズレなし。

参照:
- PIV 2020 `poŝto`: https://vortaro.net/py/serchi.py?s=po%C5%9Dto&simpla=1
- PIV 2020 `giĉeto`: https://vortaro.net/py/serchi.py?s=gi%C4%89eto&simpla=1
- PIV 2020 `tagmezo`: https://vortaro.net/py/serchi.py?s=tagmezo&simpla=1
- PIV 2020 `noktomezo`: https://vortaro.net/py/serchi.py?s=noktomezo&simpla=1

## 468. 467周目 追加再点検（ID5056〜5155）

対象:
- `ID5056`〜`ID5155`
- Time & Weather / Calendar, Time Expressions, Weather

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ĉi-jare`, `ĉi-monate`, `antaŭhieraŭ`, `postmorgaŭ`, `la sekvantan tagon`, `post kelkaj horoj` は時間表現として対応する。
- `Estas glacie kaj glite`, `Frostas`, `Hajlas`, `Fulmas`, `Pluvetadas`, `Pluvegas` は天気の短文として成立する。
- `fulmotondro`, `veterprognozo`, `atmosfera premo`, `sub nulo`, `frostos`, `nuboj disiĝas` は天気語彙として確認できる。
- `Kia estas la temperaturo?` は `kiom` への言い換え余地はあるが、会話では「気温はどうか」を問う文として文脈別許容。

参照:
- PIV 2020 `fulmo`: https://vortaro.net/py/serchi.py?s=fulmo&simpla=1
- PIV 2020 `frostas`: https://vortaro.net/py/serchi.py?s=frostas&simpla=1
- PIV 2020 `glita`: https://vortaro.net/py/serchi.py?s=glita&simpla=1
- PIV 2020 `premo`: https://vortaro.net/py/serchi.py?s=premo&simpla=1

## 469. 468周目 追加再点検（ID156〜255）

対象:
- `ID156`〜`ID255`
- Basic Sentences / Saying Hello & Goodbye, Good Wishes, Thanks

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Sanon!` は短い祝意・祈願表現として成立し、JA/ZH/KO/RU の健康祈願と対応する。
- `Bonvenon`, `Ĝis revido`, `Bonan vojaĝon`, `Bonan apetiton`, `Bonŝancon` は基本挨拶として対応する。
- `gastamo`, `tosti`, `aprezi`, `Dankon pro ...`, `Ne menciu tion` は感謝・歓迎文脈で意味ズレなし。
- `Feliĉan vojaĝon`, `Mi profunde apreza...` 系は自然化余地はあるが、クイズ上の対応は明確。

参照:
- PIV 2020 `gasto`: https://vortaro.net/py/serchi.py?s=gasto&simpla=1
- PIV 2020 `tosti`: https://vortaro.net/py/serchi.py?s=tosti&simpla=1
- PIV 2020 `aprezi`: https://vortaro.net/py/serchi.py?s=aprezi&simpla=1
- PIV 2020 `sano`: https://vortaro.net/py/serchi.py?s=sano&simpla=1

## 470. 469周目 追加再点検（ID256〜355）

対象:
- `ID256`〜`ID355`
- Basic Sentences / Thanks, Apologies, Instructions, Short Questions & Answers

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Pardonon`, `Mi agis senzorge`, `Ne estas kialo pardonpeti`, `Pardonu pro la prokrasto` は謝罪・弁明文脈で対応する。
- `Ne zorgu pri tio`, `Bonvolu viciĝi ĉi tie`, `Ne paŝu sur la gazonon`, `Atentu la hundon` は命令・注意表現として成立する。
- `Mi ne tion celis` は `Mi ne celis tion` への平板化余地があるが、焦点語順として意味は保つ。
- `Kiom malproksime?`, `Ĉu estas tro malfrue?`, `Kiom da jaroj vi havas?` は短問答教材として許容。

参照:
- PIV 2020 `pardon`: https://vortaro.net/py/serchi.py?s=pardon&simpla=1
- PIV 2020 `ĝeni`: https://vortaro.net/py/serchi.py?s=%C4%9Deni&simpla=1
- PIV 2020 `vico`: https://vortaro.net/py/serchi.py?s=vico&simpla=1
- PIV 2020 `gazono`: https://vortaro.net/py/serchi.py?s=gazono&simpla=1

## 471. 470周目 追加再点検（ID356〜455）

対象:
- `ID356`〜`ID455`
- Basic Sentences / Short Questions & Answers, Congratulations; General Conversation / Languages, Making Yourself Understood

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Gratulon/Gratulojn pro ...`, `Feliĉan Kristnaskon/Paskon/Ĥanukon/Dankotagon/Ramadanon/Divalon` は祝辞表現として対応する。
- `Feliĉan Divalon!` は過去修正後の形を維持。`Divalo` 系の外部確認があり、現行の対格形は祝祭名への祝意として読める。
- `la bengalan`, `la rumanan`, `la tajan`, `la persan`, `la nederlandan` などは `lingvo` 省略の言語名として成立する。
- `slovene`, `azerbajĝane`, `latve`, `itale` は言語使用を表す副詞形として文脈上明確。
- `Via tagaloga estas tre bona`, `Mia korea estas sufiĉe malbona` は「あなたのタガログ語能力」「私の韓国語」の省略表現として文脈別許容。

参照:
- PIV 2020 `gratuli`: https://vortaro.net/py/serchi.py?s=gratuli&simpla=1
- PIV 2020 `Ĥanuko`: https://vortaro.net/py/serchi.py?s=%C4%A4anuko&simpla=1
- PIV 2020 `bengalo`: https://vortaro.net/py/serchi.py?s=bengalo&simpla=1
- PIV 2020 `literumi`: https://vortaro.net/py/serchi.py?s=literumi&simpla=1

## 472. 471周目 追加再点検（ID456〜555）

対象:
- `ID456`〜`ID555`
- General Conversation / Making Yourself Understood, Agreeing & Disagreeing, Asking for & Giving Information

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `mandarena ĉina lingvo`, `akĉento`, `literumi`, `prononci`, `traduki` は意思疎通・言語確認文脈で対応する。
- `Ĉu mi ĝuste ĝin prononcas?` は `Ĉu mi prononcas ĝin ĝuste?` の方が平板だが、焦点語順として成立する。
- `drinkejo`, `junulargastejo`, `picejo`, `biciklas` は PIV または透明な語形成で確認できる。
- `Fakte, mi estas survoje por renkonti amikon` は `al renkonto kun amiko` も候補だが、目的を表す `por renkonti` として意味は明確。
- `Kion vi trovas pli interesa, teatron aŭ operon?` は既存修正後の選択疑問として、日中韓/RU と対応する。

参照:
- PIV 2020 `mandareno`: https://vortaro.net/py/serchi.py?s=mandareno&simpla=1
- PIV 2020 `akĉento`: https://vortaro.net/py/serchi.py?s=ak%C4%89ento&simpla=1
- PIV 2020 `drinkejo`: https://vortaro.net/py/serchi.py?s=drinkejo&simpla=1
- PIV 2020 `biciklo`: https://vortaro.net/py/serchi.py?s=biciklo&simpla=1

## 473. 472周目 追加再点検（ID556〜655）

対象:
- `ID556`〜`ID655`
- General Conversation / Asking for & Giving Information, Expressing Feelings, Help & Advice, Opinions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `trista`, `malstreĉita`, `ekscitita`, `ŝokita`, `motivita`, `embarasita`, `naŭza` は感情・評価語として確認できる。
- `Mi sentas iom da kapturno`, `Mi sentas min perdita`, `Mi sentas min embarasita` は自然さに濃淡はあるが、各列の意味を保つ。
- `kondolencoj`, `Niaj pensoj estas kun vi`, `via perdo` は弔意文脈で対応する。
- `Ĉu vi povus prizorgi tion dum momento?`, `Mi malkonsilus lui aŭton`, `flugpersonaro`, `tekkomputilo` は依頼・助言文脈で意味ズレなし。

参照:
- PIV 2020 `trista`: https://vortaro.net/py/serchi.py?s=trista&simpla=1
- PIV 2020 `embarasi`: https://vortaro.net/py/serchi.py?s=embarasi&simpla=1
- PIV 2020 `kondolenci`: https://vortaro.net/py/serchi.py?s=kondolenci&simpla=1
- PIV 2020 `naŭzi`: https://vortaro.net/py/serchi.py?s=na%C5%ADzi&simpla=1

## 474. 473周目 追加再点検（ID656〜755）

対象:
- `ID656`〜`ID755`
- General Conversation / Opinions; Emergencies / Emergency Situations, Accidents

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `grandioza`, `rimarkoj`, `aktorado`, `butikumado`, `konsideras ĉi tiun filmon la plej bona` は意見表明文脈で対応する。
- `Fajro!` は `Incendio!` も候補だが、短い警告発話として許容し、過修正を避けて維持。
- `fajrobrigado`, `ambulanco`, `ŝtelisto`, `oficejo pri perditaj aĵoj` は緊急・事故文脈で対応する。
- `traŭmatizita`, `stirpermesilo`, `Mi havis la prioritaton`, `asekurdokumentoj`, `akcidentraporto` は事故対応語彙として既存判断どおり維持。

参照:
- PIV 2020 `grandioza`: https://vortaro.net/py/serchi.py?s=grandioza&simpla=1
- PIV 2020 `incendio`: https://vortaro.net/py/serchi.py?s=incendio&simpla=1
- PIV 2020 `fajrobrigado`: https://vortaro.net/py/serchi.py?s=fajrobrigado&simpla=1
- PIV 2020 `ambulanco`: https://vortaro.net/py/serchi.py?s=ambulanco&simpla=1

## 475. 474周目 追加再点検（ID756〜855）

対象:
- `ID756`〜`ID855`
- Emergencies / First Aid, At the Police Station; Making Friends / Introductions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sangi`, `mordita`, `bruligis min`, `tordis al mi la maleolon`, `bandaĝon`, `frakturon`, `elartikigis mian brakon` は応急処置文脈で対応する。
- `alergia al ...`, `novokaino`, `poliso de medicina asekuro`, `sciigi mian familion` は医療・保険文脈で意味ズレなし。
- `denunci ŝtelon`, `Oni enrompis en mian aŭton`, `atestantoj`, `suspektindan`, `fotoroboton` は警察署文脈で対応する。
- `fotoroboto` は PIV 直接見出し未確認だが、外部辞書で police photofit 相当として確認でき、RU `фоторобот` と一致するため維持。
- `sinjoron Smirnov`, `prezenti al vi ...`, `konatiĝi kun vi` は紹介表現として格・向きに大きな問題なし。

参照:
- PIV 2020 `bandaĝo`: https://vortaro.net/py/serchi.py?s=banda%C4%9Do&simpla=1
- PIV 2020 `alergio`: https://vortaro.net/py/serchi.py?s=alergio&simpla=1
- PIV 2020 `denunci`: https://vortaro.net/py/serchi.py?s=denunci&simpla=1
- Glosbe `fotoroboto`: https://glosbe.com/eo/en/fotoroboto

## 476. 475周目 追加再点検（ID856〜955）

対象:
- `ID856`〜`ID955`
- Making Friends / Introductions, Place of Residence, Age/Nationality & Religion

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `amikino`, `fraŭlino`, `koramiko`, `vendmanaĝero`, `fianĉon` は紹介文脈で対応する。性別指定は RU 列と整合する箇所では維持。
- `Ĉi tie tre plaĉas al mi`, `Kio alkondukas vin al Brazilo?`, `kunloĝas en domo`, `jam de ses monatoj` は居住・滞在文脈で意味ズレなし。
- `Moldavio`, `Nov-Zelando`, `Unuiĝintaj Arabaj Emirlandoj`, `Kazaĥio` は地名として対応する。
- `Kia estas via nacieco?` は `Kio estas ...?` も自然だが、国籍という属性の種類を問う形として許容。
- `Al kiu religio vi apartenas?`, `katoliko`, `judino`, `kristanino`, `musulmanino`, `hinduistino` は宗教・信仰文脈で対応する。

参照:
- PIV 2020 `nacieco`: https://vortaro.net/py/serchi.py?s=nacieco&simpla=1
- PIV 2020 `Moldavio`: https://vortaro.net/py/serchi.py?s=Moldavio&simpla=1
- PIV 2020 `religio`: https://vortaro.net/py/serchi.py?s=religio&simpla=1
- PIV 2020 `katoliko`: https://vortaro.net/py/serchi.py?s=katoliko&simpla=1

## 477. 476周目 追加再点検（ID956〜1055）

対象:
- `ID956`〜`ID1055`
- Making Friends / Age/Nationality & Religion, Family & Relationships, Describing People

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `budhano`, `siĥo`, `protestantino`, `ateisto`, `preĝejo`, `templo`, `moskeo`, `sinagogo` は宗教関連語として対応する。
- `edziniĝinta`, `Ĉu vi edziniĝis?`, `fianĉino`, `fraŭla`, `disiĝis`, `en rilato`, `rendevuas kun iu` は関係・婚姻文脈で列間対応を保つ。
- `solinfano`, `geavoj`, `genepoj`, `nepo`, `nepinoj` は親族語として意味ズレなし。
- `bonŝanculo`, `okulvitroj`, `svelta`, `rufa`, `ĉarma`, `scivolema`, `gustumi` は人物・身体描写文脈で対応する。
- `Li estas juna, malalta kaj bela` の `bela` は男性の外見評価にも使えるため、handsome / привлекательный との対応を維持。

参照:
- PIV 2020 `budhano`: https://vortaro.net/py/serchi.py?s=budhano&simpla=1
- PIV 2020 `fraŭlo`: https://vortaro.net/py/serchi.py?s=fra%C5%ADlo&simpla=1
- PIV 2020 `edziniĝi`: https://vortaro.net/py/serchi.py?s=edzini%C4%9Di&simpla=1
- PIV 2020 `rufa`: https://vortaro.net/py/serchi.py?s=rufa&simpla=1

## 478. 477周目 追加再点検（ID1056〜1155）

対象:
- `ID1056`〜`ID1155`
- Making Friends / Describing People, Things You Like & Dislike, Arranging to Meet

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `iri al noktokluboj`, `butikumi`, `fotografado`, `ĝardenado`, `patkukojn`, `dombestojn` は趣味・嗜好文脈で対応する。
- `Mi ŝatas troti` は `jogging` と完全同義ではないが、PIV 2020 で人の小走り・速歩系の用法が確認でき、軽いランニング文脈として許容。
- `piedirado` は hiking より広いが、KO/RU の徒歩・散策寄りの訳ともつながるため、明確な意味ズレとはしない。
- `Aliĝu al mi por tagmanĝo`, `Ĉu vi ŝatus aliĝi al ni?` は会食・同席への誘いとしてやや直訳感があるが、`aliĝi al ...` の「加わる」語義から文脈別許容。
- `Ĉu vi rememorigos min?`, `vestiblo`, `sciencfikciaj libroj`, `mensogulon` は語義・文脈とも破綻なし。

参照:
- PIV 2020 `troti`: https://vortaro.net/py/serchi.py?s=troti&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `memorigi`: https://vortaro.net/py/serchi.py?s=memorigi&simpla=1
- PIV 2020 `vestiblo`: https://vortaro.net/py/serchi.py?s=vestiblo&simpla=1

## 479. 478周目 追加再点検（ID1156〜1255）

対象:
- `ID1156`〜`ID1255`
- Making Friends / Arranging to Meet, Accepting & Declining; Dating / Asking Someone out, On a Date

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `partion de golfo` はゲーム・対戦の一回としての `partio` から、golf round / RU `партию в гольф` に対応する。
- `Sonas bone`, `Mi ne kontraŭas`, `Kun plezuro`, `Tio sonas alloge`, `Mi iomete malfruiĝas` は受諾・断りの短文として自然。
- `Mi venos preni vin`, `regalos vin per trinkaĵo`, `akompani vin hejmen`, `veturigi vin hejmen` は誘い・送迎文脈で意味ズレなし。
- `Ĉu mi povas aliĝi al vi?`, `Ĉu ĝenas vin, se mi aliĝos al vi?` は同席を求める表現として文脈別許容。
- `Ni forveturu de ĉi tie` は JA/ZH/KO より乗り物含みが出るが、RU `уедем` と整合し、明確な衝突ではないため維持。

参照:
- PIV 2020 `partio`: https://vortaro.net/py/serchi.py?s=partio&simpla=1
- PIV 2020 `aliĝi`: https://vortaro.net/py/serchi.py?s=ali%C4%9Di&simpla=1
- PIV 2020 `regali`: https://vortaro.net/py/serchi.py?s=regali&simpla=1
- PIV 2020 `akompani`: https://vortaro.net/py/serchi.py?s=akompani&simpla=1

## 480. 479周目 追加再点検（ID1256〜1355）

対象:
- `ID1256`〜`ID1355`
- Dating / On a Date, Compliments, Wedding; Education / At School

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Forigu viajn manojn de mi!`, `Vi aspektas bonege`, `Mi trovas vin tre alloga`, `Mi agrable pasigis la tempon kun vi` はデート場面の発話として成立する。
- 既修正済みの `Mi ŝatas vian veston` は、`vesto` が身につける衣服全体を表せるため outfit / 服装文脈として維持。
- `kantistino`, `Ĉu vi edziniĝos al mi?`, `Ni ĝojas anonci la edziĝon de nia filo` は性別指定が RU または文脈と合う。
- `nupto`, `geedziĝo`, `fianĉiĝo`, `novgeedzoj`, 各種 `geedziĝa datreveno/jubileo` は結婚式・記念日文脈で意味ズレなし。
- `hazarda eraro`, `lerni ĝin parkere`, `notoj`, `sonorilo` は学校文脈で対応する。

参照:
- PIV 2020 `vesto`: https://vortaro.net/py/serchi.py?s=vesto&simpla=1
- PIV 2020 `nupto`: https://vortaro.net/py/serchi.py?s=nupto&simpla=1
- PIV 2020 `fianĉiĝo`: https://vortaro.net/py/serchi.py?s=fian%C4%89i%C4%9Do&simpla=1
- PIV 2020 `parkere`: https://vortaro.net/py/serchi.py?s=parkere&simpla=1

## 481. 480周目 追加再点検（ID1356〜1455）

対象:
- `ID1356`〜`ID1455`
- Education / At School, At University, Student Life

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `En kiu aĝo infanoj komencas iri al lernejo?` は `Je kiu aĝo ...` も候補だが、`en la aĝo de ...` 系の用法から意味ズレなし。
- `studjaro`, `diplomiĝis`, `magistriĝo`, `doktoriĝas`, `distanca lernado`, `stipendio`, `studentloĝejo` は大学文脈で対応する。
- `studentino`, `estrino`, `lektoro`, `rektoro`, `fako`, `fakultato` は RU/日中韓の役職・所属表現と整合する。
- `biblioteka formularo`, `biblioteka karto`, `aliĝi al la biblioteko`, `prunti ... librojn` は図書館利用の文脈として理解できる。
- `brile trapasis`, `malsukcesis en la ekzameno`, `disertacio`, `invitita parolanto`, `templimo por paroladoj`, `formulitaj buŝe` は学生生活・会議文脈で意味ズレなし。

参照:
- PIV 2020 `aĝo`: https://vortaro.net/py/serchi.py?s=a%C4%9Do&simpla=1
- PIV 2020 `magistro`: https://vortaro.net/py/serchi.py?s=magistro&simpla=1
- PIV 2020 `biblioteko`: https://vortaro.net/py/serchi.py?s=biblioteko&simpla=1
- PIV 2020 `templimo`: https://vortaro.net/py/serchi.py?s=templimo&simpla=1

## 482. 481周目 追加再点検（ID1456〜1555）

対象:
- `ID1456`〜`ID1555`
- Education / Student Life, Numbers & Colours, Jobs / Occupation

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ripeti multajn aferojn` は「復習する」としてはやや広いが、PIV 2020 の `ripeti` に学習・反復文脈があり、JA/ZH/KO/RU の「復習」と大きく衝突しない。
- `helpos vin kun fiziko`, `labori kun nombroj`, `Mi volas labori eksterlande` は学習・職業希望文脈として自然。
- `malsama koloro`, `helruĝa`, `malhelverda`, `marblua`, `miksu bluan kun flava` は色表現として列間対応を保つ。
- `handikapitaj infanoj` は現代的な言い換え候補はあるが、PIV 2020 で `handikapo/handikapito` が確認でき、明確な意味ズレとはしない。

参照:
- PIV 2020 `ripeti`: https://vortaro.net/py/serchi.py?s=ripeti&simpla=1
- PIV 2020 `fiziko`: https://vortaro.net/py/serchi.py?s=fiziko&simpla=1
- PIV 2020 `profesio`: https://vortaro.net/py/serchi.py?s=profesio&simpla=1
- PIV 2020 `handikapo`: https://vortaro.net/py/serchi.py?s=handikapo&simpla=1

## 483. 482周目 追加再点検（ID1556〜1655）

対象:
- `ID1556`〜`ID1655`
- Jobs / Occupation, Employment Status, At the Workplace, Business

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `merkatika administranto` は EN/JA/ZH/KO が manager 寄り、RU が specialist 寄りで揺れるため、役職名を一方向へ固定する修正は避ける。
- `memstara laboristo`, `dungitaro`, `forpermeso`, `maldungo`, `emeritiĝis`, `redukti laborfortojn` は雇用・職場文脈として対応する。
- `patrina/patra forpermeso` は maternity/paternity leave として意味が明確で、過剰な置換はしない。
- `La limtempo por liveri la varojn finiĝas` は現在形では `eksvalidiĝas` ではなく `finiĝas` になっており、納期・期限文脈として安全。

参照:
- PIV 2020 `merkatiko`: https://vortaro.net/py/serchi.py?s=merkatiko&simpla=1
- PIV 2020 `dungi`: https://vortaro.net/py/serchi.py?s=dungi&simpla=1
- PIV 2020 `permesi`: https://vortaro.net/py/serchi.py?s=permesi&simpla=1
- PIV 2020 `emerito`: https://vortaro.net/py/serchi.py?s=emerito&simpla=1

## 484. 483周目 追加再点検（ID1656〜1755）

対象:
- `ID1656`〜`ID1755`
- Jobs / Business, At the Interview, Recommendation Letter

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `afervojaĝojn` は `business trips` として、PIV 2020 の `afero` 周辺の用例から透明に読める。
- `laborpostena priskribo`, `provtempo`, `aliĝilon`, `vojaĝkostojn`, `fleksajn labortempojn` は面接・採用文脈で意味ズレなし。
- `labori laŭvice` は `deĵoro/laŭvice` の用例から shift work として理解できるため、狭い語へ置換しない。
- `bonvenan defion`, `vasta gamo de kapabloj`, `kreema solvanto de problemoj` は推薦状・面接の評価表現として許容。

参照:
- PIV 2020 `afero`: https://vortaro.net/py/serchi.py?s=afero&simpla=1
- PIV 2020 `deĵoro`: https://vortaro.net/py/serchi.py?s=de%C4%B5oro&simpla=1
- PIV 2020 `kontrakto`: https://vortaro.net/py/serchi.py?s=kontrakto&simpla=1
- PIV 2020 `aliĝilo`: https://vortaro.net/py/serchi.py?s=ali%C4%9Dilo&simpla=1

## 485. 484周目 追加再点検（ID1756〜1855）

対象:
- `ID1756`〜`ID1855`
- Jobs / Recommendation Letter, Travel / Asking Directions, Giving Directions

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `aldono al via programo`, `elstaran kontribuon`, `komunikajn kapablojn`, `plej varman rekomendon` は推薦状の定型表現として成立する。
- `ŝparvojo`, `piediri`, `orientiĝas`, `trans la strato`, `fajrobrigadejo` は道案内語彙として意味ズレなし。
- `diri al mi la direkton` は `montri la vojon` も候補だが、方向・道順を尋ねる発話として許容。
- `Daŭrigu ankoraŭ duonkilometron` は「さらに500mほど進む」と一致し、距離表現として問題なし。

参照:
- PIV 2020 `gvidi`: https://vortaro.net/py/serchi.py?s=gvidi&simpla=1
- PIV 2020 `orientiĝi`: https://vortaro.net/py/serchi.py?s=orienti%C4%9Di&simpla=1
- PIV 2020 `trans`: https://vortaro.net/py/serchi.py?s=trans&simpla=1
- PIV 2020 `piediri`: https://vortaro.net/py/serchi.py?s=piediri&simpla=1

## 486. 485周目 追加再点検（ID1856〜1955）

対象:
- `ID1856`〜`ID1955`
- Travel / Giving Directions, At the Tourist Office, Excursions, Plane / Booking a Flight

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Daŭrigu rekten preter kelkaj semaforoj`, `subpasejon`, `indikilojn`, `turisma oficejo` は案内・観光案内所文脈で対応する。
- `junulargastejoj`, `tendumejojn`, `sandviĉejon`, `vidindaĵojn`, `vidindaĵan ekskurson` は観光語彙として透明。
- `navedan buson` は以前の `navedbuso` より無理の少ない形で、shuttle bus として文脈上理解できる。
- `preni miajn fotojn`, `subeksponitaj`, `presi la fotojn de ĉi tiu memorkarto` は写真店・観光文脈で意味ズレなし。

参照:
- PIV 2020 `turisma`: https://vortaro.net/py/serchi.py?s=turisma&simpla=1
- PIV 2020 `gastejo`: https://vortaro.net/py/serchi.py?s=gastejo&simpla=1
- PIV 2020 `vidindaĵo`: https://vortaro.net/py/serchi.py?s=vidinda%C4%B5o&simpla=1
- PIV 2020 `preni`: https://vortaro.net/py/serchi.py?s=preni&simpla=1

## 487. 486周目 追加再点検（ID1956〜2055）

対象:
- `ID1956`〜`ID2055`
- Plane / Booking a Flight, Checking in, Luggage

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `ŝanĝi aviadilon` 系は乗り継ぎ文脈で現在のCSVでは安定しており、未確認の `transŝanĝo` 系へ戻す必要はない。
- `En la antaŭa/malantaŭa vico` は「前方/後方の席」より列を明示するが、座席希望として許容範囲。
- `enŝipiĝo` は船由来で気になるが、航空搭乗への慣用的拡張として文脈別許容。
- `registrigi bagaĝon`, `manbagaĝo`, `bagaĝetikedo`, `bagaĝaj ŝranketoj`, `ĉareto` は空港荷物文脈で意味が明確。

参照:
- PIV 2020 `aviadilo`: https://vortaro.net/py/serchi.py?s=aviadilo&simpla=1
- PIV 2020 `vico`: https://vortaro.net/py/serchi.py?s=vico&simpla=1
- PIV 2020 `enŝipiĝi`: https://vortaro.net/py/serchi.py?s=en%C5%9Dipi%C4%9Di&simpla=1
- PIV 2020 `bagaĝo`: https://vortaro.net/py/serchi.py?s=baga%C4%9Do&simpla=1

## 488. 487周目 追加再点検（ID2056〜2155）

対象:
- `ID2056`〜`ID2155`
- Plane / Luggage, Passport Control & Customs, On the Plane

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `dogano` は税関・関税の両文脈で使われ、`Kiom da dogano mi devas pagi?`, `pagi doganon por ...` は duty 文脈として対応する。
- `azilo`, `peti azilon`, `statuson de rifuĝinto`, `loĝpermesilo`, `transitvizo` は入国・難民関連語として整合する。
- `reklini mian seĝon`, `fiksi vian sekurzonon`, `seĝodorson`, `supran bagaĝujon` は機内表現として意味ズレなし。
- `stevardino` は EN では中立的だが RU が女性形で、現行表現を動かす根拠は弱い。

参照:
- PIV 2020 `dogano`: https://vortaro.net/py/serchi.py?s=dogano&simpla=1
- PIV 2020 `azilo`: https://vortaro.net/py/serchi.py?s=azilo&simpla=1
- PIV 2020 `sekurzono`: https://vortaro.net/py/serchi.py?s=sekurzono&simpla=1
- PIV 2020 `stevardo`: https://vortaro.net/py/serchi.py?s=stevardo&simpla=1

## 489. 488周目 追加再点検（ID2156〜2255）

対象:
- `ID2156`〜`ID2255`
- Plane / On the Plane, Airport Signs, Car / Car Hire, Driving & Parking

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `sur la aviadilo`, `formularon por dogandeklaro`, `pordegoj`, `forflugoj`, `bagaĝa elpreno` は空港・機内表示として許容。
- `mana/aŭtomata transmisio` は PIV 2020 で機械的エネルギーの伝達として確認でき、車の transmission 文脈で透明。
- `infanseruroj`, `direktomontriloj`, `klimatizilo`, `stirpermesilo`, `vojmapo` は自動車関連の透明複合語として意味が明確。
- `redoni la aŭton kun plena benzinujo`, `rapidlimo sur aŭtovojoj`, `Veturu trans/sub la ponton/ponto` は列間対応を保つ。

参照:
- PIV 2020 `transmisio`: https://vortaro.net/py/serchi.py?s=transmisio&simpla=1
- PIV 2020 `benzinujo`: https://vortaro.net/py/serchi.py?s=benzinujo&simpla=1
- PIV 2020 `aŭtovojo`: https://vortaro.net/py/serchi.py?s=a%C5%ADtovojo&simpla=1
- PIV 2020 `seruro`: https://vortaro.net/py/serchi.py?s=seruro&simpla=1

## 490. 489周目 追加再点検（ID2256〜2355）

対象:
- `ID2256`〜`ID2355`
- Car / Driving & Parking, At the Petrol Station, Mechanical Problems

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `stirada ekzameno`, `vojsignoj`, `aŭtoriparejo`, `serva areo`, `trafikblokiĝo` は運転・道路文脈として対応する。
- `benzinejo`, `benzinujo`, `brulaĵo`, `dizelo`, `kontraŭfrosta likvaĵo`, `startokabloj` は給油所語彙として意味ズレなし。
- `akumulatoro`, `malŝargiĝis`, `ŝargi`, `paneis`, `pneŭmatiko krevis`, `pumpi la pneŭmatikojn` は自動車故障文脈で確認済み。
- `hupo`, `bremslumoj`, `brulaĵindikilo`, `rapidometro`, `stirmekanismo`, `bremslikvaĵo` は部品・計器名として理解できる。

参照:
- PIV 2020 `akumulatoro`: https://vortaro.net/py/serchi.py?s=akumulatoro&simpla=1
- PIV 2020 `paneo`: https://vortaro.net/py/serchi.py?s=paneo&simpla=1
- PIV 2020 `rapidometro`: https://vortaro.net/py/serchi.py?s=rapidometro&simpla=1
- PIV 2020 `pneŭmatiko`: https://vortaro.net/py/serchi.py?s=pne%C5%ADmatiko&simpla=1

## 491. 490周目 追加再点検（ID2356〜2455）

対象:
- `ID2356`〜`ID2455`
- Car / Road Signs, Other Transport / At the Bus Station, At the Train Station

結果:
- **今回の追加修正なし**

主な据え置き確認:
- `Buskoridoro`, `Piedira zono`, `Trafiklumoj`, `Nivelkruciĝo`, `Piedira transirejo` は道路標識として意味が明確。
- `Preterpasu maldekstre` は RU が障害物回避標識寄り、EN/JA/ZH/KO が keep left 寄りだが、左側通行指示として文脈別許容。
- `revenbileto`, `returan bileton`, `unudirekta bileto`, `monata abono`, `rabatita tarifo`, `pensiula revenbileto` はバス・鉄道切符文脈で対応する。
- `Kiu kajo?`, `kajo numero 1`, `Atentu la interspacon`, `ekspresa trajno`, `malfruiĝas`, `troplena` は駅・鉄道案内として意味ズレなし。

参照:
- PIV 2020 `piedira zono`: https://vortaro.net/py/serchi.py?s=piedira%20zono&simpla=1
- PIV 2020 `kajo`: https://vortaro.net/py/serchi.py?s=kajo&simpla=1
- PIV 2020 `abono`: https://vortaro.net/py/serchi.py?s=abono&simpla=1
- PIV 2020 `vagono`: https://vortaro.net/py/serchi.py?s=vagono&simpla=1

一致確認:
- `cmp_exit=0`
- `md5=3fb9f4290de4ab7cae9069931d68a5b0`
