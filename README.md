# Esperanto 4択学習アプリ

このリポジトリには、既存の Streamlit 版に加えて、スマートフォン向けの `localStorage` 保存型クイズUIがあります。スマホで `app.py` または `sentence_app.py` を開くと、Streamlit Cloud上でもこのUIを優先表示します。

## Streamlit Cloudでのスマホ利用

通常どおりStreamlitアプリを起動します。

```bash
streamlit run app.py
```

スマートフォンのUser-Agentで開くと、`mobile_app/` のUIがStreamlitコンポーネントとして表示されます。PCから確認したい場合は次のURLで強制表示できます。

```text
http://127.0.0.1:8501/?mobile_app=1
```

従来のStreamlit版へ戻る場合:

```text
http://127.0.0.1:8501/?classic=1
```

## スマホ向けUIの特徴

- 単語クイズと例文クイズに対応
- 回答ごとに進行状態、回答履歴、得点、復習対象を端末内の `localStorage` へ自動保存
- Streamlitの再読み込みやセッション切れ後も、同じ端末・同じブラウザなら進行中のクイズを復元
- 進行中クイズがある場合は、設定画面に「続きから再開」を表示し、新規開始による上書き前に確認
- スマホ幅で読みやすい文字サイズ、下部配置の大きい選択肢ボタン
- 成績履歴は端末内に保存。Streamlit Cloud内では結果画面の「ランキングに保存」からGoogle Sheetsの累積得点・ランキングにも加算
- Streamlit Cloud内のスマホ版成績画面では、Google Sheetsの累積・本日・今月・殿堂ランキングを確認できます。
- 端末保存容量が不足した場合は、進行中クイズの保存を優先し、古い端末内成績履歴を自動整理します。
- スマホ版でも音声再生に対応。Streamlit Cloudでは `mobile_app/audio/` と `mobile_app/sentence-audio/` をコンポーネント配下から同一オリジン配信し、Google Drive manifestはフォールバックとして使います。
- 音声は、画面に表示されているテキストがエスペラントのときだけ再生します。エスペラント→日本語では問題文を自動再生し、日本語→エスペラントでは日本語問題文を読まず、エスペラントの選択肢音声だけ再生できます。
- 再生した音声はPWAのランタイムキャッシュに保存しますが、肥大化を避けるため古い音声キャッシュは自動で整理されます。
- 結果画面の復習リストでは、間違えた問題のエスペラント正解音声を手動再生できます。
- スコア保存中に再読み込みされた場合も、同じ `save_id` で安全に再送し、Google Sheets側の重複加算を防ぎます。

## 静的PWAとしての単独起動

起動:

```bash
python3 -m http.server 8765
```

ブラウザで開く:

```text
http://127.0.0.1:8765/mobile_app/
```

特徴:

単独起動時はPWAのサービスワーカーでアプリ本体とJSONデータをキャッシュします。

既存CSVを更新した後は、PWA用JSONを再生成します。

```bash
python3 tools/build_mobile_data.py
```

例文データはCSV上の5000件をすべて含めます。同じエスペラント文・同じ日本語訳の行も出題対象に残しつつ、4択の誤答候補では同一表示の選択肢を避けます。

## スマホ版で音声を使う場合

Streamlit Cloud内蔵のスマホ版では、`mobile_app/audio/` と `mobile_app/sentence-audio/` の音声ファイルを直接再生します。Google Drive直リンクはスマホブラウザやiframe内で不安定になる場合があるため、現在は同一オリジン配信を優先し、`mobile_app/data/audio_manifest.json` はフォールバックとして使います。Streamlit CloudのSecrets追加は不要です。

音声設定が「問題を自動再生」または「問題自動＋選択肢」のとき、クイズ開始や次問への移動がユーザー操作から発生した場合だけ、エスペラントの問題文を自動再生します。再読み込み復元のようにユーザー操作がない場面では、スマホブラウザの自動再生制限を避けるため手動の音声ボタンを使います。

Driveフォルダの中身を更新した場合は、必要に応じて次を実行してフォールバック用の対応表を再生成します。

```bash
python3 tools/build_drive_audio_manifest.py
```

必要な場合だけ、Streamlit CloudのSecretsで外部配信URLを上書きできます。

```toml
[mobile_audio]
drive_download_base_url = "https://drive.google.com/uc?export=download&id="
vocab_base_url = "https://example.com/audio/"
sentence_base_url = "https://example.com/sentence-audio/"
```

`vocab_base_url` / `sentence_base_url` は、Cloud Storageなどで `<base_url>/<audioKey>.wav` として配信する場合だけ指定します。

## 検証

スマホ用JSON、CSV、音声ファイル、Google Driveフォールバックmanifestの整合性検証:

```bash
npm run validate:mobile-assets
```

WAVヘッダ確認を省いた高速確認:

```bash
npm run validate:mobile-assets:quick
```

静的PWA版の再読み込み復元、結果・履歴、保存データ復旧テスト:

```bash
npm install
python3 -m http.server 8765
npm run test:mobile
```

Streamlit Cloud相当のコンポーネント表示、再読み込み復元、結果・履歴テスト:

```bash
npm install
streamlit run app.py --server.port 8501 --server.headless true
npm run test:streamlit-mobile
```

初回だけPlaywrightブラウザが必要です。

```bash
npx playwright install chromium
```

## Streamlit版

既存のPC向けStreamlitアプリは残しています。

```bash
streamlit run app.py
streamlit run sentence_app.py
```
