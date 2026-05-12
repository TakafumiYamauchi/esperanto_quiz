# Streamlit Cloud デプロイ手順（Google Sheets 連携）

本番用シークレットを誤ってコミットしないための作業手順をまとめます。

## スマホ向けUIについて

スマートフォンでの利用は `mobile_app/` の `localStorage` 保存型UIを優先します。`app.py` と `sentence_app.py` はスマホアクセスを検出すると、このUIをStreamlitコンポーネントとして表示します。PCユーザーは従来のStreamlit版をそのまま使えます。

- エントリポイント: `mobile_app/index.html`
- Streamlit連携: `mobile_streamlit_bridge.py`
- サービスワーカー: `mobile-sw.js`
- PWA用データ: `mobile_app/data/vocab.json`, `mobile_app/data/sentences.json`, `mobile_app/data/audio_manifest.json`
- スマホ状態保存: ブラウザの `localStorage`
- 進行中クイズの保護: 再開導線を表示し、新規開始で上書きする前に確認
- スマホ版スコア保存: 結果画面の「ランキングに保存」から `mobile_score_sync.py` 経由でGoogle Sheetsの `Scores` / `UserStats` / `UserStatsSentence` に反映
- 音声: スマホ版は `mobile_app/audio/` と `mobile_app/sentence-audio/` をコンポーネント配下から同一オリジン配信。`mobile_app/data/audio_manifest.json` はGoogle Driveフォールバックとして使う。

Streamlitの静的ファイル配信はHTML/JSアプリ配信向けではないため、Streamlit Cloudではカスタムコンポーネントとして埋め込みます。CSV更新後は次を実行してJSONを更新します。

```bash
python3 tools/build_mobile_data.py
```

Google Drive上の音声ファイルを入れ替えた場合は、フォールバック用manifest更新のため必要に応じて次も実行します。

```bash
python3 tools/build_drive_audio_manifest.py
```

PCでスマホUIを強制表示する確認URL:

```text
https://<your-app>.streamlit.app/?mobile_app=1
```

スマホで従来版を確認するURL:

```text
https://<your-app>.streamlit.app/?classic=1
```

## 1. シークレットの準備（ローカルで開かない）
- `gen-lang-client-0360673218-9b47aa22b42f.json` は **コミットしない**（`.gitignore` 済み）。
- JSON を開く必要がある場合はローカルで確認し、`private_key` の改行を `\n` に置換しておく。
- 秘密鍵をチャット、GitHub、README、Issue、PR本文に貼ってしまった場合、その鍵は漏洩済みとして扱い、Google Cloudで削除して新しい鍵を作り直す。

## 2. Streamlit Cloud の Secrets 設定
1. Streamlit Cloud のデプロイ済みアプリで **Settings** → **Secrets** を開く。
2. 以下を貼り付け、`project_id`・`client_email`・`private_key` を JSON から転記する（1行形式では改行を `\n` として入れる）。
   ```toml
   [connections.gsheets]
   type = "service_account"
   project_id = "gen-lang-client-0360673218"
   private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
   client_email = "streamlit-sheets-sa@gen-lang-client-0360673218.iam.gserviceaccount.com"
   spreadsheet = "https://docs.google.com/spreadsheets/d/1WnlZ2BACdf3uCha0JOscdk2wPselC_VVm_Ua6VlhC-I"
   token_uri = "https://oauth2.googleapis.com/token"
   ```
3. 複数行形式で貼る場合は、TOMLの複数行文字列を使う。
   ```toml
   private_key = """-----BEGIN PRIVATE KEY-----
   ...
   -----END PRIVATE KEY-----
   """
   ```
4. 保存後にアプリを再起動または再デプロイし、ログにGoogle Sheets認証エラーが出ないことを確認する。

## 2.1. スマホ版音声
スマホ版音声は、`mobile_app/audio/` と `mobile_app/sentence-audio/` から再生する。これにより、Streamlit Cloudのiframe内でもGoogle Drive直リンクに依存せず、同一オリジンの音声URLを使える。

通常はSecrets設定不要。Cloud Storage等の `<base_url>/<audioKey>.wav` 形式へ切り替えたい場合だけ、Streamlit Cloud の **Settings** → **Secrets** に次を追加する。

```toml
[mobile_audio]
drive_download_base_url = "https://drive.google.com/uc?export=download&id="
vocab_base_url = "https://example.com/audio/"
sentence_base_url = "https://example.com/sentence-audio/"
```

PC/従来版は従来通り、ローカルの音声フォルダが存在する場合に `st.audio()` で音声を扱う。

## 3. 動作確認（手順）
1. デプロイされたアプリをスマホで開き、スマホUIが表示されることを確認。
2. 任意のユーザー名でクイズを開始し、数問回答する。
3. ブラウザを再読み込みし、進行中のクイズが復元されることを確認。
4. 不正解を出した場合、復習対象が保持されることを確認。
5. 設定画面へ戻った場合に「続きから再開」が表示され、新規開始時に上書き確認が出ることを確認。
6. ユーザー名を入れた状態で完了し、結果画面の「ランキングに保存」でGoogle Sheetsの累積得点に加算されることを確認。
7. スマホ版の音声設定をオンにし、単語・例文の音声が再生できることを確認。
8. 結果画面と成績画面がスマホ幅で読みやすいことを確認。
9. 従来版を確認する場合は `?classic=1` を付けて開く。

## 4. ローカルの鍵ファイルの扱い
- 作業後は鍵ファイルを安全な場所に移動するか削除する。
- 追加で鍵を扱う場合は、`.gitignore` にあることを確認し、誤ってステージングしないよう注意する。

## 5. 依存関係
- `requirements.txt` に `streamlit`, `pandas`, `streamlit-gsheets` を記載済み。Cloud で自動インストールされる。

## 6. トラブルシュートのヒント
- 認証エラー: Secrets の `private_key` の改行が `\n` に置換されているか確認。
- 書き込みエラー: Sheets 側でサービスアカウントが「編集者」権限になっているか確認。
- 反映遅延: ネットワーク遅延の場合があるため数秒待つ。キャッシュは `ttl=0` なので基本即時反映。
