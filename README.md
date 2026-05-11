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
- 音声は静的PWAとして単独起動した場合に利用可能。Streamlit Cloud内蔵表示では、`[mobile_audio]` に外部配信URLを設定した場合だけ音声設定を有効化します。

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

## スマホ版で音声を使う場合

大量の音声ファイルはGitHubへ入れず、Cloud Storageなどの外部配信先へ置きます。Streamlit CloudのSecretsに次を追加すると、スマホ版の音声選択が有効になります。

```toml
[mobile_audio]
vocab_base_url = "https://example.com/audio/"
sentence_base_url = "https://example.com/sentence-audio/"
```

各音声は `audioKey.wav` として参照します。

## 検証

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
