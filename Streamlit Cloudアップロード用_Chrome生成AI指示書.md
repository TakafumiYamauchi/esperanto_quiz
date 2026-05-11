# Streamlit Cloudアップロード用 Chrome生成AI指示書

この文書は、Google Chrome上で操作できる生成AIに渡して、このエスペラント4択クイズアプリをGitHub経由でStreamlit Community Cloudへ公開してもらうための指示書です。

## 生成AIへ渡す指示

あなたは、GitHubとStreamlit Community Cloudにログイン済みのGoogle Chromeを操作して、エスペラント学習用4択クイズアプリを公開する作業担当者です。

最終目標は、GitHub上のリポジトリからStreamlit Community Cloudに `app.py` をエントリポイントとしてデプロイし、スマートフォンでは `mobile_app/` のlocalStorage保存型UIが表示される状態にすることです。PC版の既存Streamlit機能も壊さないでください。

### 重要な安全ルール

- `.streamlit/secrets.toml`、GoogleサービスアカウントJSON、`private_key` はGitHubへ絶対にアップロードしない。
- Secretsの値が必要な場合は、ユーザーにStreamlit CloudのSecrets欄へ直接貼り付けてもらう。秘密鍵の中身をチャット欄へ表示させない。
- Streamlit CloudでGoogle Sheets連携を動かす最大のポイントは、デプロイ済みアプリの `Settings` → `Secrets` に `[connections.gsheets]` を正しく貼り付けること。
- 秘密鍵をチャット、GitHub、README、Issue、PR本文に貼ってしまった場合、その鍵は漏洩済みとして扱い、Google Cloudで削除して新しい鍵を作り直す。
- `node_modules/`、`__pycache__/`、`test-results/`、`playwright-report/` はアップロードしない。
- 初回公開では、大容量の `audio/` と `Esperanto例文5000文_収録音声/` は必須扱いにしない。スマホ向けStreamlit内蔵表示では音声はオフになるため、まずアプリ公開を優先する。
- スマホ版で音声も使う場合は、音声ファイルをGitHubへ大量投入せず、Cloud Storageなどの外部配信URLを `[mobile_audio]` としてSecretsに設定する。
- 失敗した場合は、Streamlit Cloudのログを読んで原因を特定してから修正する。推測だけで再デプロイを繰り返さない。

### 公開対象の基本情報

- GitHubリポジトリ: `https://github.com/Takatakatake/esperanto-choice-quiz-streamlit`
- GitHubリポジトリSSH: `git@github.com:Takatakatake/esperanto-choice-quiz-streamlit.git`
- ブランチ: `main`
- Streamlit Cloudのメインファイル: `app.py`
- 例文版の既存アプリ: `sentence_app.py`
- スマホ用UI: `mobile_app/index.html`
- Streamlit連携: `mobile_streamlit_bridge.py`
- スマホ版スコア保存連携: `mobile_score_sync.py`
- PWAデータ: `mobile_app/data/vocab.json`, `mobile_app/data/sentences.json`
- 依存関係ファイル: `requirements.txt`
- 強制スマホUI確認URL: `https://<公開URL>/?mobile_app=1`
- 従来版確認URL: `https://<公開URL>/?classic=1`

## 作業手順

### 1. GitHubリポジトリを確認する

1. GitHubを開く。
2. `https://github.com/Takatakatake/esperanto-choice-quiz-streamlit` を開く。
3. このリポジトリが存在し、`main` ブランチにアプリ一式が入っていることを確認する。
4. 新しいリポジトリは作成しない。このリポジトリにアクセスできない場合だけ、ユーザーへ確認する。
5. 公開範囲がPrivateの場合は、Streamlit Cloud側でGitHub連携権限が必要になる。

### 2. GitHubへ必要ファイルを入れる

リポジトリのルートに、少なくとも以下を配置する。

```text
app.py
sentence_app.py
mobile_streamlit_bridge.py
mobile_score_sync.py
mobile-sw.js
requirements.txt
README.md
DEPLOY.md
data_sources.py
score_append_utils.py
score_row_utils.py
vocab_grouping.py
2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv
phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv
mobile_app/
tools/
.gitignore
.streamlit/config.toml
.streamlit/secrets.example.toml
```

アップロードしないもの:

```text
.streamlit/secrets.toml
gen-lang-client-*.json
node_modules/
__pycache__/
test-results/
playwright-report/
fuyou/
編集ログ/
```

音声を後から追加したい場合だけ、`audio/` や `Esperanto例文5000文_収録音声/` を別途検討する。ただしサイズが大きいため、初回公開の障害になりやすい。まず音声なしでStreamlit公開を完了する。

### 3. GitHub上で最低限の確認をする

以下を確認する。

- `requirements.txt` がリポジトリのルートにある。
- `app.py` がリポジトリのルートにある。
- `mobile_app/app.js`, `mobile_app/styles.css`, `mobile_app/index.html`, `mobile_app/data/vocab.json`, `mobile_app/data/sentences.json` が存在する。
- `mobile_score_sync.py` が存在し、スマホ版の「ランキングに保存」からGoogle Sheetsへ保存できる構成になっている。
- `.streamlit/secrets.toml` やGoogle秘密鍵JSONが含まれていない。

### 4. Streamlit Community Cloudでアプリを作成する

1. `https://share.streamlit.io` を開く。
2. ワークスペース右上の `Create app` を押す。
3. `Yup, I have an app` を選ぶ。
4. GitHubリポジトリ、ブランチ、メインファイルを指定する。
   - Repository: `Takatakatake/esperanto-choice-quiz-streamlit`
   - Branch: `main`
   - Main file path: `app.py`
5. App URLは任意。覚えやすい名前を付けられる場合は、Esperanto学習アプリだと分かる名前にする。
6. `Advanced settings` を開く。
7. Python versionは、特別な理由がなければStreamlit Cloudのデフォルト、または `3.12` を使う。
8. Google Sheets連携を使う場合だけ、Secrets欄にユーザーが直接Secretsを貼り付ける。
9. 保存して `Deploy` を押す。

### 5. Secretsに貼る内容

Google Sheets連携を使う場合、Streamlit Cloudのデプロイ済みアプリの `Settings` → `Secrets` 欄に、次の形式で貼る。これは公開後に成績保存やGoogle Sheets連携を動かすための重要設定であり、GitHubには置かない。

```toml
[connections.gsheets]
type = "service_account"
project_id = "gen-lang-client-0360673218"
private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
client_email = "streamlit-sheets-sa@gen-lang-client-0360673218.iam.gserviceaccount.com"
spreadsheet = "https://docs.google.com/spreadsheets/d/1WnlZ2BACdf3uCha0JOscdk2wPselC_VVm_Ua6VlhC-I"
token_uri = "https://oauth2.googleapis.com/token"
```

スマホ版で音声を有効化する場合だけ、同じSecrets欄に次も追加する。音声ファイルは `<base_url>/<audioKey>.wav` で取得できる形にしておく。

```toml
[mobile_audio]
vocab_base_url = "https://example.com/audio/"
sentence_base_url = "https://example.com/sentence-audio/"
```

注意:

- `private_key` の `...` は実際の秘密鍵で置き換える。
- 1行形式で貼る場合、`private_key` 内の改行は `\n` として入れる。
- 複数行形式で貼る場合は、TOMLの複数行文字列を使う。例:
  ```toml
  private_key = """-----BEGIN PRIVATE KEY-----
  ...
  -----END PRIVATE KEY-----
  """
  ```
- この値はGitHubに置かない。Streamlit CloudのSecrets欄だけに入れる。
- チャット、GitHub、README、Issue、PRなどに出した可能性がある秘密鍵は使わず、Google Cloudで削除して再発行した鍵だけを使う。
- `[mobile_audio]` は秘密鍵ではないが、音声ファイルが大量なためGitHub本体には音声フォルダを入れない。
- AIは秘密鍵の内容を読まない。必要ならユーザーに貼り付け操作だけ依頼する。
- Secretsを保存した後は、アプリを再起動または再デプロイし、ログにGoogle Sheets認証エラーが出ないことを確認する。

### 6. デプロイログを確認する

デプロイ中はログを確認する。

よくある失敗と対応:

- `ModuleNotFoundError`: `requirements.txt` に不足パッケージを追加する。
- `FileNotFoundError`: GitHubにCSV、`mobile_app/data/*.json`、必要なPythonファイルが入っているか確認する。
- Google Sheets認証エラー: Secretsの `private_key`、`client_email`、Sheets共有権限を確認する。
- アプリは開くがスマホUIにならない: `https://<公開URL>/?mobile_app=1` を開き、`mobile_streamlit_bridge.py` と `mobile_app/` が入っているか確認する。

### 7. 公開後の動作確認

公開URLで次を確認する。

1. PCのChromeで通常URLを開き、アプリが表示される。
2. PCのChromeで `?mobile_app=1` を付けて開き、スマホ向けUIが表示される。
3. `?mobile_app=1` で単語クイズを開始できる。
4. 選択肢を押して回答を進められる。
5. 1問以上回答した後にページを再読み込みし、進行中のクイズが復元される。
6. 不正解を出した場合、復習対象が保持される。
7. ホームへ戻ると「保存されたクイズがあります」「続きから再開」が表示される。
8. 進行中クイズがある状態で新規開始しようとすると、上書き確認が出る。
9. 結果画面がスマホ幅で読みやすい。
10. 成績画面がスマホ幅で読みやすく、下部ナビの `ホーム`、`クイズ`、`成績` が押せる。
11. ユーザー名を入れてクイズを完了し、結果画面の `ランキングに保存` でGoogle Sheetsの累積得点・ランキングへ加算される。
12. `[mobile_audio]` を設定した場合は、スマホ版の音声設定をオンにして再生できる。
13. `?classic=1` を付けると従来のStreamlit版を確認できる。

可能であれば、実機スマホでも同じ確認を行う。最低限、スマホ実機では「開始」「回答」「再読み込み復元」「ランキングに保存」「成績画面」「下部ナビ」を確認する。`[mobile_audio]` を設定した場合は音声再生も確認する。

### 8. 作業完了時の報告形式

完了後、次の形式でユーザーへ報告する。

```text
Streamlit Cloudへの公開が完了しました。

公開URL:
https://...

GitHubリポジトリ:
https://github.com/...

確認したこと:
- 通常表示
- ?mobile_app=1 のスマホUI
- クイズ開始
- 回答操作
- 再読み込み後の状態復元
- 不正解時の復習対象保持
- スマホ版のランキング保存
- [mobile_audio] を設定した場合のスマホ版音声再生
- 結果画面
- 成績画面
- ?classic=1 の従来版

未対応または注意点:
- 例: 音声ファイルは初回公開では含めていません。
- 例: Google SheetsのSecretsはユーザーが貼り付け済みです。
```

## 参考にした公式情報

- Streamlit Community Cloudの公開手順では、GitHubリポジトリ、ブランチ、ファイルパスを指定して `Create app` からデプロイする。
  - https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- SecretsはGitHubへ置かず、Streamlit CloudのAdvanced settingsまたはアプリ設定から貼り付ける。
  - https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management
- Streamlit Community Cloudはリポジトリのルートを作業ディレクトリとして扱うため、ファイルパスはルート基準で確認する。
  - https://docs.streamlit.io/deploy/streamlit-community-cloud/status
