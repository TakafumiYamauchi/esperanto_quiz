# エスペラント例文 強引な外来語・カルク修正一覧

作成日: 2026-06-10
最終更新日: 2026-06-11

対象ファイル: `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`

## 先に読む要約

今回の一連の作業は、`minibaro` のような強引な外来語化、英語・ロシア語からの直訳調、
文法・語法上かなり不安定な表現を点検し、エスペラント学習教材として明確に直した方がよい箇所だけを直したもの。

| 観点 | 結果 |
|---|---|
| エスペラント本文の修正 | 125行 |
| 訳のみの調整 | 2行 |
| 音声再生成 | 127件、すべて RHVoice `spomenka` |
| 維持した方針 | 正しい範囲内の多様性は残す |
| 代表的に維持した表現 | `regato`, `smuzio`, `toasto`, `Mi feriumas`, `Mi faras praktikon` |
| Drive状態 | matched 5000 / missing 0 / extra 0 |
| Driveで削除してよい旧音声 | `drive_audio_extra_files_to_delete_20260611.md` に一覧化 |

特に重要なのは、Claude Code の候補をそのまま採用したのではなく、PIV・既存コーパス・教材方針を見て
「直すもの」と「多様性として残すもの」を分けた点である。

## 目次

- 概要
- 判断方針
- 最終結論
- 件数
- ラウンド別まとめ
- カテゴリ別の見取り図
- 最終修正一覧
- 第6ラウンド追加修正一覧
- 主に維持した候補
- 第7・第8ラウンド追加裁定
- 音声・モバイルデータ
- Google Drive状態
- 関連文書

## 概要

`minibaro` 級の強引な外来語化や、英語・ロシア語の連語をそのまま移したような表現を点検し、エスペラント学習教材として明確に直した方がよい箇所だけを修正した。

最終的なCSV差分は **127行**。このうちエスペラント本文の変更は **125行**、訳だけの焦点調整は **2行**（PID 3241 / 3679）である。音声差し替え操作は **127件** だが、これは PID 2271 と PID 3248 を途中でさらに再調整したためで、最終CSV上のエスペラント本文変更行数は125行である。

この文書は、今回の一連の修正について、後から次の5点を確認できるように整理したもの。

- 何件直したか
- どの方針で直したか
- 具体的にどの文をどう直したか
- どの候補をあえて直さず残したか
- 音声・モバイルデータ・Google Drive側に何が残っているか

## 判断方針

- 表現が正しい範囲内なら、教材としての多様性を尊重して維持する。
- PIV / ReVo / 既存コーパス内の用法を見て、明確な意味ズレ・非文法・強い内部不整合があるものだけを修正する。
- 料理名・現代的職名・口語として成立する表現は、過度に純化しない。
- 修正後は RHVoice `spomenka` で音声を再生成し、root音声とスマホ用音声を同期する。

## 最終結論

| 項目 | 結論 |
|---|---|
| CSV本文 | 127行を修正（エスペラント本文125行 + 訳のみ2行） |
| 音声 | 修正文は RHVoice `spomenka` で再生成済み |
| root音声 | 5000 WAVで整合 |
| スマホ用音声 | 5000 WAVで整合 |
| PWAデータ | `mobile_app/data/sentences.json` を再生成済み |
| Drive manifest | 残り51件アップロード後に `mobile_app/data/audio_manifest.json` を再生成済み |
| 第7ラウンド | `Mi feriumas` は教材上の多様性として維持。追加修正なし |
| 第8ラウンド | `Mi faras praktikon` は維持。`ankaŭ` の訳焦点だけ2件調整 |
| 関連commit | `7684656`, `a7cfbd8`, `39fbd76`, `6c83b47`, `355cd9e`, および本commitで反映済み |

## 件数

| 区分 | 内容 | 件数 |
|---|---:|---:|
| 最終CSV変更行 | 一連の修正前のCSVから最終CSVまでの変更行 | 127 |
| うちエスペラント本文変更行 | 音声再生成を伴う本文変更 | 125 |
| うち訳のみ調整行 | エスペラント本文・音声キーは維持 | 2 |
| 音声生成操作 | 第1・第2・第3・最終検品・第5・第6ラウンドの合計 | 127 |
| root例文音声 | `Esperanto例文5000文_収録音声/` のWAV | 5000 |
| スマホ例文音声 | `mobile_app/sentence-audio/` のWAV | 5000 |
| Drive fallback | 第6ラウンド新51音声アップロード後 | matched 5000 / missing 0 / extra 0 |
| Drive上の旧重複 | 手作業削除後、旧音声は残存なし | extra 0 |

## ラウンド別まとめ

| ラウンド | 主な内容 | 音声生成 | 備考 |
|---|---|---:|---|
| 第1ラウンド | `minibaro` 周辺の強引な外来語・露骨なカルクを修正 | 8 | 初期対応 |
| 第2ラウンド | 候補の追加精査。料理名・現代語は過度に純化せず、明確な不自然箇所だけ修正 | 18 | 教材方針を明確化 |
| 第3ラウンド | 連語・文脈・語義ズレを広めに修正 | 41 | 多くは英語式構文の自然化 |
| 最終検品 | 途中修正した文の再調整 | 4 | PID 2271 / 3248 など |
| 第5ラウンド | PIV用例や固定設備名に合わせて追加修正 | 5 | `Savelirejo`, `Krizbremso`, `fotobudo` など |
| 第6ラウンド | 文法・語法・文末pleaseタグを追加修正 | 51 | `bonvolu` 文末タグ26件を `mi petas` に整理 |
| 第7ラウンド | `Mi feriumas` を再検討 | 0 | `feriumi` は透明な派生・実使用ありとして維持 |
| 第8ラウンド | `praktiko` と `ankaŭ` の追加再裁定 | 0 | `Mi faras praktikon` は維持。訳焦点のみ2件調整 |

## カテゴリ別の見取り図

| カテゴリ | 代表例 | 判断 |
|---|---|---|
| 強引な外来語・不安定な借用 | `fotoroboto`, `fotokabino`, `remiso` | 透明なエスペラント表現へ修正 |
| 英語・ロシア語式カルク | `make a reservation`, `come with`, `have attention`, `withdraw money` 型 | エスペラントで自然な動詞・構文へ修正 |
| 文法・格・相関詞 | `ŝaltitajn`, `io ... kiun`, `atingi tien` | 文法上より安定する形へ修正 |
| 文脈上の語義ズレ | `aliĝilo`, `pakaĵo da aspirino`, `daŭrigu` 道案内 | 場面に合う語へ修正 |
| 設備名・固定表現 | `Kriza elirejo`, `Urĝa bremso`, `televido` 機器名 | `Savelirejo`, `Krizbremso`, `televidilo` などへ整理 |
| 飲食・注文表現 | 食べる意味の `havi`, 注文文脈の `havi` | `manĝi`, `mendi`, `preni` などへ自然化 |
| 丁寧表現 | 文末 `bonvolu/bonvole` | 文末タグだけ `mi petas` へ。`Bonvolu + 不定詞` は維持 |
| 維持した多様性 | `regato`, `smuzio`, `toasto`, `Mi feriumas`, `Mi faras praktikon` | 正しい範囲内の多様性として維持 |

## 最終修正一覧

| PID | 修正前 | 修正後 | 主な理由 |
|---:|---|---|---|
| 190 | `Delonge ni ne vidiĝis` | `Delonge ni ne intervidiĝis` | 「互いに会う」の意味を明確化 |
| 374 | `Ĉu mi povus havi vian atenton?` | `Vian atenton, mi petas!` | 英語的な `have attention` を回避 |
| 753 | `Ĉu mi povas havi vian nomon kaj adreson?` | `Ĉu vi bonvolus diri al mi vian nomon kaj adreson?` | 名前・住所を「持つ」許可ではなく、伝えてもらう表現へ |
| 769 | `Ĉio estos bone kun vi` | `Vi fartos bone` | 露語・英語的な構文を自然化 |
| 826 | `Ni penos fari lian fotoroboton` | `Ni penos fari lian portreton laŭ priskribo` | `fotoroboto` を避け、説明に基づく人物像を透明化 |
| 998 | `Li estas en rilato` | `Li havas amrilaton` | 恋愛関係を明示 |
| 1201 | `Ni manĝu ekstere hodiaŭ vespere` | `Ni manĝu eksterhejme hodiaŭ vespere` | 外食の意味で、屋外食との混同を避ける |
| 1208 | `Ĉu vi renkontiĝas kun iu?` | `Ĉu vi havas amrilaton kun iu?` | 「交際している」の意味を明確化 |
| 1301 | `Fraŭlino Wane baldaŭ fariĝos sinjorino Jones` | `Fraŭlino Wayne baldaŭ fariĝos sinjorino Jones` | 固有名 Wayne に修正。英語列も同時修正 |
| 1559 | `Per kio vi gajnas vian vivon?` | `Per kio vi vivtenas vin?` | `gajni sian vivon` は避け、生活を支える表現へ |
| 1703 | `Ĉu vi estas komputile klera?` | `Ĉu vi estas lerta pri komputiloj?` | `computer literate` 直訳感を回避 |
| 1734 | `Ĉu mi ricevos vojaĝkostojn?` | `Ĉu oni repagos al mi la vojaĝkostojn?` | 受け取る対象を「費用」ではなく返金として明確化 |
| 1764 | `Ŝi estos bonega aldono al via programo` | `Ŝi estos tre valora por via programo` | 人を `aldono` とする直訳感を回避 |
| 1841 | `Daŭrigu rekte antaŭen ĉirkaŭ unu kilometron` | `Iru plu rekte antaŭen ĉirkaŭ unu kilometron` | 無目的語 `Daŭrigu` を道案内として自然化 |
| 1853 | `Daŭrigu preter la fajrobrigadejo` | `Iru plu preter la fajrobrigadejo` | 同上 |
| 1854 | `Daŭrigu ankoraŭ ducent metrojn` | `Iru plu ankoraŭ ducent metrojn` | 同上 |
| 1855 | `Daŭrigu ankoraŭ duonkilometron` | `Iru plu ankoraŭ duonkilometron` | 同上 |
| 1856 | `Daŭrigu rekte preter kelkaj semaforoj` | `Iru plu rekte preter kelkaj semaforoj` | 同上 |
| 1921 | `Mi ŝatus grandigi ĉi tiujn fotografiojn` | `Mi ŝatus grandigi ĉi tiujn fotojn` | 可算の写真として既存語 `fotoj` に統一 |
| 1968 | `Sur ĉi tiu aviadilo ne plu estas lokoj` | `En ĉi tiu aviadilo ne plu estas lokoj` | 機内は `en aviadilo` が自然 |
| 1987 | `Ĉu estas liberaj lokoj sur ĉi tiu flugo?` | `Ĉu estas liberaj lokoj por ĉi tiu flugo?` | 便に対する空席として `por` へ |
| 2158 | `Ĉu sur la aviadilo estas stevardino, kiu parolas la hebrean?` | `Ĉu en la aviadilo estas stevardino, kiu parolas la hebrean?` | 機内は `en aviadilo` |
| 2172 | `Kriza elirejo` | `Savelirejo` | PIV用例 `savelirejo ... en aviadilo` に合わせる |
| 2184 | `En kazo de fajro uzu la ŝtuparon` | `Okaze de fajro uzu la ŝtuparon` | 一般の「〜の場合」は `okaze de` が教材として安全 |
| 2271 | `Kie estas la parkometro?` | `Kie estas la pagmaŝino por parkumado?` | `parkometro` を避けつつ、支払い機の焦点を保持 |
| 2290 | `Vi pasos superbazaron maldekstre` | `Vi preterpasos superbazaron maldekstre` | 「通り過ぎる」は `preterpasi` |
| 2464 | `Mi ŝatus aldoni 10 funtojn al ĝi` | `Mi ŝatus aldoni 10 pundojn al ĝi` | 通貨ポンドは `pundoj` に統一 |
| 2483 | `Urĝa bremso` | `Krizbremso` | 固定設備名として「緊急時用」を明確化 |
| 2620 | `Ĉu en la ĉambro estas televido?` | `Ĉu en la ĉambro estas televidilo?` | 機器は `televidilo` |
| 2640 | `Mi ŝatus fari rezervon` | `Mi ŝatus rezervi` | `make a reservation` 直訳を避ける |
| 2684 | `Mi faris rezervon` | `Mi rezervis` | 同上 |
| 2704 | `Rezervoj estis faritaj por mi kaj mia familio` | `Ĉambroj estas rezervitaj por mi kaj mia familio` | 予約対象を明確化 |
| 2870 | `Mi bezonas detergenton` | `Mi bezonas deterganton` | PIV派生形 `deterganto` に修正 |
| 2885 | `Mi bezonas rulon da adherema filmo` | `Mi bezonas rulon da adhera plastfolio` | `cling film` 直訳感を抑える |
| 2918 | `Ĉu vi povus fari rezervon por mi?` | `Ĉu vi povus rezervi tablon por mi?` | レストラン文脈の予約対象を明確化 |
| 2923 | `Ĉu vi povas rekomendi picerion?` | `Ĉu vi povas rekomendi picejon?` | PIV掲載の `picejo` に修正 |
| 2925 | `Kien vi kutime iras, kiam vi manĝas ekstere?` | `Kien vi kutime iras, kiam vi manĝas eksterhejme?` | 外食の意味を明確化 |
| 3013 | `Kion vi ŝatus havi?` | `Kion vi ŝatus mendi?` | 注文文脈で `havi` を避ける |
| 3053 | `Ĉu la manĝaĵo venas kun legomoj?` | `Ĉu la manĝaĵo estas servata kun legomoj?` | 英語 `come with` 直訳を回避 |
| 3192 | `La sekvan rondon mi pagas` | `La sekvajn trinkaĵojn mi pagas` | 酒席の英語 `round` 直訳を回避 |
| 3226 | `Ĉu vi ŝatas fumitan viandon?` | `Ĉu vi ŝatas fumaĵitan viandon?` | 燻製は `fumaĵi` 系 |
| 3229 | `Mi prenos la fumitan truton` | `Mi prenos la fumaĵitan truton` | 同上 |
| 3232 | `Mi ŝatus la grilitan salmon` | `Mi ŝatus la kradrostitan salmon` | 料理のグリルは `kradrostita` |
| 3248 | `Li havos grilitan karpon` | `Li prenos kradrostitan karpon` | `grilita` と飲食の `havi` を同時に修正 |
| 3298 | `Li havos kelkajn tomatojn` | `Li manĝos kelkajn tomatojn` | 食べる意味の `havi` を回避 |
| 3330 | `Li ŝatas kaperojn` | `Li ŝatas kaporojn` | 食用ケッパーは `kaporo` |
| 3334 | `Li havos iom da faboj` | `Li manĝos iom da faboj` | 食べる意味の `havi` を回避 |
| 3347 | `Mi ŝatas cerealojn` | `Mi ŝatas cerealaĵojn` | 朝食用シリアルとして `cerealaĵo` |
| 3410 | `Kia grandeco ĝi estas?` | `Kiun grandecon ĝi havas?` | 英語式構文を避け、既存の `Kian grandecon havas...` 型へ |
| 3526 | `Ĉu estas certifikato por ĝi?` | `Ĉu estas atestilo por ĝi?` | 証明書は既存コーパスの `atestilo` に統一 |
| 3568 | `Ĉu ĝi venas kun instrukcioj?` | `Ĉu instrukcioj estas inkluzivitaj?` | 英語 `come with` 直訳を回避 |
| 3682 | `Mi ŝatus duonduzenon da ovoj` | `Mi ŝatus ses ovojn` | 非PIV寄りの `duonduzeno` を数詞で明確化 |
| 3788 | `Tiam mi iros ien alian` | `Tiam mi iros aliloken` | `ien alian` の非文法性を修正 |
| 3999 | `Kiom kostas lui malsekkostumon por unu tago?` | `Kiom kostas lui plonĝkostumon por unu tago?` | `wetsuit` 直訳を避ける |
| 4014 | `Estis remiso` | `La rezulto estis egala` | 不安定な借用形を透明化 |
| 4171 | `Ĉu vi volas, ke mi ŝaltu la televidon?` | `Ĉu vi volas, ke mi ŝaltu la televidilon?` | 機器は `televidilo` |
| 4284 | `Mi ŝatus fari retiron` | `Mi ŝatus elpreni monon` | 銀行出金の `make a withdrawal` 直訳を回避 |
| 4291 | `Mi bezonas formularon por monretiro` | `Mi bezonas formularon por elpreno de mono` | 出金表現を `elpreni/elpreno de mono` に統一 |
| 4296 | `Ĉu mi povas retiri monon de mia kreditkarto ĉi tie?` | `Ĉu mi povas elpreni monon per mia kreditkarto ĉi tie?` | `retiri monon` の出金語義を避ける |
| 4303 | `Mi ŝatus retiri 100 pundojn, mi petas` | `Mi ŝatus elpreni 100 pundojn, mi petas` | 同上 |
| 4341 | `Necesas deponaĵo je unu-monata lupago` | `Necesas kaŭcio egala al unu-monata lupago` | 敷金は `kaŭcio` |
| 4385 | `Mi ŝatus ilin farbigi` | `Mi ŝatus tinkturigi miajn harojn` | 髪を染める文脈は `tinkturi/tinkturigi` |
| 4387 | `Bonvolu farbi miajn harojn blonde` | `Bonvolu tinkturi miajn harojn blonde` | 同上 |
| 4403 | `Malantaŭe kojne, mi petas` | `Malantaŭe laŭgrade mallongigite, mi petas` | 髪型指示として意味を透明化 |
| 4411 | `Ĉu vi ŝatus ion sur ĝi?` | `Ĉu mi metu ion sur la harojn?` | 指示対象不明の `ĝi` を避ける |
| 4419 | `Mi ŝatus havi traktadon de la vizaĝo` | `Mi ŝatus haŭtflegadon de la vizaĝo` | `treatment` 直訳を避ける |
| 4455 | `Ĉu vi povas ripari la televidon?` | `Ĉu vi povas ripari la televidilon?` | 機器は `televidilo` |
| 4561 | `Mi sentas min kapturna` | `Mi havas kapturnon` | めまいの自然表現へ |
| 4650 | `Vi devus redukti vian trinkadon` | `Vi devus redukti vian alkoholtrinkadon` | 飲酒量を明確化 |
| 4708 | `Li havas grandajn dioptriojn` | `Li bezonas fortajn okulvitrojn` | 光学単位の所有表現を回避 |
| 4802 | `Kiun mobilan reton vi havas?` | `Kiun poŝtelefonan reton vi havas?` | `mobile network` 直訳感を避ける |
| 4871 | `Je kioma horo li estas atendata reveni?` | `Je kioma horo oni atendas, ke li revenos?` | 英語風受動構文を自然化 |
| 4934 | `Ĉu vi havas fotokabinon?` | `Ĉu vi havas fotobudon?` | `fotokabino` の露語鏡像感を避け、PIV語根 `bud/o` で透明化 |
| 4941 | `Bonvolu pezi ĉi tiun pakaĵon` | `Bonvolu pesi ĉi tiun pakaĵon` | 他動詞「量る」は `pesi` |

## 第6ラウンド追加修正一覧

第6ラウンドでは、強引な外来語ではなく、構文・語法の英露語写しや文法上の不整合を中心に51文を追加修正した。`Bonvolu + 不定詞` の正用例や単独の `Bonvolu` は維持し、文末pleaseタグとして並ぶものだけ `mi petas` に寄せた。

| PID | 修正前 | 修正後 | 主な理由 |
|---:|---|---|---|
| 240 | `Tio estis la plej malmulto, kion mi povis fari` | `Tio estis la plej malgranda afero, kiun mi povis fari` | 名詞先行詞との一致と定型句の自然化 |
| 286 | `Mi timas, ke mi ne povas resti plu longe` | `Mi timas, ke mi ne povas resti pli longe` | `plu longe` の重複感を避ける |
| 922 | `Li loĝas en Unuiĝintaj Arabaj Emirlandoj` | `Li loĝas en la Unuiĝintaj Arabaj Emirlandoj` | 複数形国名の冠詞を補う |
| 936 | `Kia estas via nacieco?` | `Kio estas via nacieco?` | 国籍の同定質問として自然化 |
| 990 | `Ĉu vi edziniĝis?` | `Ĉu vi estas edziniĝinta?` | 出来事ではなく婚姻状態の質問へ |
| 992 | `Li estas divorciĝinta` | `Li estas eksedziĝinta` | `divorci` への二重 `-iĝ-` を避ける |
| 1479 | `Kvarfoje tri estas dek du` | `Kvaroble tri estas dek du` | 乗算表現を `-oble` に統一 |
| 1528 | `Du mil foje kvin estas dek mil` | `Dumiloble kvin estas dek mil` | 乗算表現を `-oble` に統一 |
| 1718 | `Ĉu mi devos labori laŭvice?` | `Ĉu mi devos labori laŭ deĵoroj?` | 交代勤務を `deĵoro` で明確化 |
| 1726 | `Ĉu mi povus ricevi aliĝilon?` | `Ĉu mi povus ricevi kandidatiĝan formularon?` | 求職文脈の応募書類として明確化 |
| 1809 | `Kiom da tempo necesas por atingi tien?` | `Kiom da tempo necesas por alveni tien?` | `atingi` の直接目的語問題を避ける |
| 2000 | `Kie mi suriru?` | `Kie mi suriru la aviadilon?` | 他動詞 `suriri` の目的語を明示 |
| 2073 | `La sekva, bonvolu!` | `La sekva, mi petas!` | 文末pleaseタグを `mi petas` に統一 |
| 2106 | `Vian doganan deklaracion, bonvolu` | `Vian doganan deklaracion, mi petas` | 同上 |
| 2242 | `Turnu dekstren` | `Turniĝu dekstren` | 方向転換は `turniĝi` 型へ |
| 2249 | `Kie mi turnu?` | `Kie mi turniĝu?` | 同上 |
| 2250 | `Turnu dekstren ĉe la kruciĝo` | `Turniĝu dekstren ĉe la kruciĝo` | 同上 |
| 2267 | `Turnu dekstren ĉe la T-kruciĝo` | `Turniĝu dekstren ĉe la T-kruciĝo` | 同上 |
| 2282 | `Turnu maldekstren ĉe la unua turniĝo` | `Turniĝu maldekstren ĉe la unua turniĝo` | 同上 |
| 2284 | `Turnu dekstren ĉe la dua turniĝo` | `Turniĝu dekstren ĉe la dua turniĝo` | 同上 |
| 2295 | `Vi lasis viajn lumojn ŝaltitajn` | `Vi lasis viajn lumojn ŝaltitaj` | 目的語述語の形容詞から対格を外す |
| 2312 | `Por 25 frankoj, bonvolu` | `Por 25 frankoj, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 2377 | `Ne trinku kaj veturu` | `Ne stiru ebria` | 道路標識として飲酒運転を直接表す |
| 2466 | `Mi ne kontraŭas vojaĝi per trajno ĉiutage` | `Ne ĝenas min vojaĝi per trajno ĉiutage` | `kontraŭi + 不定詞` を避ける |
| 2750 | `La ŝlosilon de ĉambro numero 621, bonvolu!` | `La ŝlosilon de ĉambro numero 621, mi petas!` | 文末pleaseタグを `mi petas` に統一 |
| 2909 | `Sekvu min, bonvolu` | `Sekvu min, mi petas` | 同上 |
| 2910 | `Infanan seĝeton, bonvolu` | `Infanan seĝeton, mi petas` | 同上 |
| 2978 | `Mi ŝatus koktelon, bonvolu` | `Mi ŝatus koktelon, mi petas` | 同上 |
| 2980 | `Mi prenos la samon, bonvolu` | `Mi prenos la samon, mi petas` | 同上 |
| 2986 | `Ĉu mi povus vidi la vinkarton, bonvole?` | `Ĉu mi povus vidi la vinkarton, mi petas?` | `bonvole` の係り先の曖昧さを避ける |
| 3030 | `Ankoraŭ iomete, bonvolu` | `Ankoraŭ iomete, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 3040 | `Pardonu, ni ŝatus mendi, bonvolu` | `Pardonu, ni ŝatus mendi, mi petas` | 同上 |
| 3091 | `Ni ŝatus mendi deserton, bonvolu` | `Ni ŝatus mendi deserton, mi petas` | 同上 |
| 3105 | `Ĉu ni povus pagi, bonvole?` | `Ĉu ni povus pagi, mi petas?` | `bonvole` の係り先の曖昧さを避ける |
| 3202 | `Tri glasetojn da tekilo, bonvolu` | `Tri glasetojn da tekilo, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 3243 | `Mi prenos la kokidan supon, bonvolu` | `Mi prenos la kokidan supon, mi petas` | 同上 |
| 3249 | `Ni prenos kokidajn flugilojn, bonvolu` | `Ni prenos kokidajn flugilojn, mi petas` | 同上 |
| 3311 | `Mi prenos tomatsupon, bonvolu` | `Mi prenos tomatsupon, mi petas` | 同上 |
| 3366 | `Hejmfaritan panon, bonvolu` | `Hejmfaritan panon, mi petas` | 同上 |
| 3553 | `Akvorezistan ŝminkon por okulharoj, bonvolu` | `Akvorezistan ŝminkon por okulharoj, mi petas` | 同上 |
| 3582 | `Ĉu estas io speciala, kiun vi ŝatus vidi?` | `Ĉu estas io speciala, kion vi ŝatus vidi?` | `io` 先行詞に合わせた相関詞へ |
| 4384 | `Rekte malantaŭe, bonvolu` | `Rekte malantaŭe, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 4481 | `Ĉu vi scias, kie mi povas lasi ripari mian fotoaparaton?` | `Ĉu vi scias, kie mi povas riparigi mian fotoaparaton?` | 修理依頼の使役は `riparigi` が自然 |
| 4682 | `Iom pli larĝe, bonvolu` | `Iom pli larĝe, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 4691 | `Mi ŝatus dentpurigadon, bonvolu` | `Mi ŝatus dentpurigadon, mi petas` | 同上 |
| 4762 | `Mi ŝatus pakaĵon da aspirino` | `Mi ŝatus paketon da aspirino` | 薬の一箱・一包は `paketo` が自然 |
| 4768 | `Mi ŝatus paroli kun la farmaciisto, bonvolu` | `Mi ŝatus paroli kun la farmaciisto, mi petas` | 文末pleaseタグを `mi petas` に統一 |
| 4880 | `Plilaŭtigu, bonvolu` | `Plilaŭtigu, mi petas` | 同上 |
| 4881 | `Mallaŭtigu, bonvolu` | `Mallaŭtigu, mi petas` | 同上 |
| 4918 | `Mi ŝatus vatitan koverton, bonvolu` | `Mi ŝatus vatitan koverton, mi petas` | 同上 |
| 4962 | `Ĉe kiu giĉeto estas poŝtrestante?` | `Kiu giĉeto estas por poŝtrestantaj sendaĵoj?` | `poŝtrestante` を郵便物の形容詞句として整理 |

## 主に維持した候補

以下は、Claude Code 側で候補化されたが、教材として正しい範囲内の多様性・現代語・文化語として維持したもの。

- `toasto`, `feni`, `smuzio`, `regato`, `vendmanaĝero`
- `naĉoj`, `kalzoneo`, `servi la pilkon`, `viva muziko`
- `belaruso`, `informatiko`, `konstruktiva`, `diskĵokeo`
- `Wi-Fi`, `Facebook`, `Tvitero`, `evento`, `mufino`, `bovlingo`, `sprajo`
- `Ĉu mi povas/povus havi X?` 系のうち、現代会話として十分通る依頼表現
- `aliĝi al ni/vi`, `Kion ni havos por tagmanĝo/deserto?`
- `Tiel-tiel`, `dufoje pripensus`, `iri al universitato`, `vidi ... kiel`
- `doma vino`, `perdi pezon`, `havi abonon`, `fari rendevuon`
- `deklaracio`, `inkludita`, `fragila`, `poŝtejo`, `doktoro`, `kmera`, `Skajpon`
- `jaĥto / jaĥtklubo`
- `elregistriĝi`, `plena pensiono`, `pensia programo`, `centra tribuno`
- `Bankoko`, `Abu-Dabio`, `Oxford-strato`, `London Kings Cross`
- `Laŭran`, `Emilin`, `pagmaŝino por parkumado`
- 単独の `Bonvolu` と `Bonvolu + 不定詞` の正用例
- `Li laboras sur farmo`、`Ĉu la jaĥto estas asekurita por urĝaj situacioj?`

## 第7ラウンド追加裁定

第7ラウンドでは、Claude Code が `Mi feriumas` → `Mi ferias` を graylist 候補として挙げた。
Codex側でPIV2020と実使用例を確認した結果、`ferii` の方が辞書的・標準的ではあるが、
`feriumi` も透明な派生で、入国審査の「休暇中です」という応答として意味が明確に通ると判断した。

教材方針として「正しい範囲内の多様性」を残すため、PID 2074 `Mi feriumas` は維持した。
したがって第7ラウンドでのCSV・音声・モバイルデータの追加変更はない。

## 第8ラウンド追加裁定

第8ラウンドでは、Claude Code が PID 1588 `Mi faras praktikon` を `Mi faras staĝon` へ
修正する候補として挙げた。Codex側でPIV2020を再確認した結果、`staĝo` は確かにこの文脈で
自然だが、`praktiko/praktiki` も実務・職業実践の範囲を含むため、明確な誤りとは判断しなかった。
教材方針として、PID 1588 `Mi faras praktikon` は多様性として維持した。

一方、`ankaŭ` の焦点と訳がずれていた2件は、エスペラント本文を維持したまま訳だけ調整した。

| PID | エスペラント | 調整内容 |
|---:|---|---|
| 3241 | `Provu ankaŭ vi la stekon!` | `ankaŭ vi` = 「あなたも」に合わせ、英日中韓訳を調整 |
| 3679 | `Mi ankaŭ bezonas aĉeti duonkilogramon da faruno` | `also need` の焦点に合わせ、日訳を「小麦粉も...」へ調整 |

この第8ラウンドではエスペラント本文・音声キーは変えていないため、音声再生成は不要。

## 音声・モバイルデータ

修正文の音声は RHVoice `spomenka` で作成した。

生成ログ:

- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round2.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round3.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_final_audit.csv`
- `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round5.csv`
- `編集ログ/phrases_audio_replacement_generation_20260611_grammar_round6.csv`

確認結果:

- 第1ラウンド: 8件、`voice=spomenka`、全件 `generated`
- 第2ラウンド: 18件、`voice=spomenka`、全件 `generated`
- 第3ラウンド: 41件、`voice=spomenka`、全件 `generated`
- 最終検品: 4件、`voice=spomenka`、全件 `generated`
- 第5ラウンド: 5件、`voice=spomenka`、全件 `generated`
- 第6ラウンド: 51件、`voice=spomenka`、全件 `generated`
- 第8ラウンド: 訳のみ2件、音声再生成なし
- root音声: 5000 WAV
- スマホ用音声: 5000 WAV
- `npm run validate:mobile-assets`: passed（Drive fallback は matched 5000 / missing 0 / extra 0）
- `npm run test:unit`: 69 tests passed

## Google Drive状態

第6ラウンド新51音声をDriveへアップロードし、旧重複音声を手作業で削除した後、
`tools/build_drive_audio_manifest.py` でDriveを再読込した現時点では次の状態:

- Drive上の例文WAV: 5000件
- mobile data と一致する必要音声: 5000件
- matched: 5000件
- missing: 0件
- extra: 0件

アプリ同梱のローカル音声は root / スマホ用とも5000件で揃っているため通常再生には支障ない。
Drive fallbackも5000件で完全一致している。

## 関連文書

| 文書 | 用途 |
|---|---|
| `編集ログ/phrases_eo_forced_loanwords_findings_20260610.md` | Claude Code候補とCodex裁定を含む詳細調査ログ |
| `編集ログ/drive_audio_extra_files_to_delete_20260611.md` | Google Drive旧重複音声の最終確認結果 |
| `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords.csv` | 第1ラウンド音声生成ログ |
| `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round2.csv` | 第2ラウンド音声生成ログ |
| `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round3.csv` | 第3ラウンド音声生成ログ |
| `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_final_audit.csv` | 最終検品ラウンド音声生成ログ |
| `編集ログ/phrases_audio_replacement_generation_20260610_forced_loanwords_round5.csv` | 第5ラウンド音声生成ログ |
| `編集ログ/phrases_audio_replacement_generation_20260611_grammar_round6.csv` | 第6ラウンド音声生成ログ |

## 変更された主なファイル

- `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`
- `mobile_app/data/sentences.json`
- `mobile_app/data/audio_manifest.json`
- `mobile_app/app.js`
- `mobile-sw.js`
- `mobile_app/sentence-audio/*.wav`
- `Esperanto例文5000文_収録音声/*.wav`
- `編集ログ/phrases_eo_forced_loanwords_findings_20260610.md`
- `編集ログ/drive_audio_extra_files_to_delete_20260611.md`
- 本ファイル
