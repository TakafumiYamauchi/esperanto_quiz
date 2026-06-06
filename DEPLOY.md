# Streamlit Cloud デプロイ手順（Google Sheets 連携）

本番用シークレットを誤ってコミットしないための作業手順をまとめます。

## スマホ向けUIについて

スマートフォンでの利用は `mobile_app/` の `localStorage` 保存型UIを優先します。`app.py`、`sentence_app.py`、中国語版、韓国語版はスマホアクセスを検出すると、このUIをStreamlitコンポーネントとして表示します。PCユーザーは従来のStreamlit版を使い、画面上部の「PC版モード」から単語版と例文版を切り替えられます。

- エントリポイント: `mobile_app/index.html`
- Streamlit連携: `mobile_streamlit_bridge.py`
- サービスワーカー: `mobile-sw.js`
- PWA用データ: `mobile_app/data/vocab.json`, `mobile_app/data/sentences.json`, `mobile_app/data/audio_manifest.json`
- スマホ状態保存: ブラウザの `localStorage`
- 進行中クイズの保護: 再開導線を表示し、新規開始で上書きする前に確認
- スマホ版スコア保存: 結果画面の「ランキングに保存」から `mobile_score_sync.py` 経由でGoogle Sheetsの `Scores` / `UserStats` / `UserStatsSentence` に反映
- スマホ版ランキング表示: 成績画面から `mobile_ranking.py` 経由でGoogle Sheetsの累積・本日・今月・殿堂ランキングを表示
- ランキング集計: PC版とスマホ版で `ranking_utils.py` の共通集計ロジックを使い、`Scores` と `UserStats` の扱いを揃える
- PC/従来版の途中保存: 日本語版・中国語版・韓国語版の単語/例文アプリは、進行中クイズを端末内 `localStorage` に保存し、復元時はユーザー確認を挟む。途中状態はGoogle Sheetsへ送信しない。
- 診断画面: 下部ナビの「診断」から、データ件数、音声、端末保存、ランキング、スコア保存状態を確認
- 音声診断: 診断画面から単語・例文のサンプル音声を実際に再生し、スマホ実機の音声配信を確認
- localStorage復旧: 端末保存容量不足時は古い端末内成績履歴を整理し、進行中クイズの保存を優先
- 音声: スマホ版は `mobile_app/audio/` と `mobile_app/sentence-audio/` をコンポーネント配下から同一オリジン配信。`mobile_app/data/audio_manifest.json` はGoogle Driveフォールバックとして使う。
- 音声キャッシュ: Service Workerのランタイムキャッシュは上限件数を持ち、古い音声キャッシュを自動削除
- 音声ボタン: 表示中のテキストがエスペラントのときだけ表示。日本語の問題文・日本語の選択肢には音声ボタンを出さない。
- 復習音声: 結果画面の復習リストから、間違えた問題のエスペラント正解音声を手動再生できる。
- スコア保存再送: 保存中の再読み込み後や累積更新だけ失敗した場合は同じ `save_id` で再送し、Google Sheets側の重複加算を避ける。
- アプリ間リンク: スマホ版の下部から日本語版・中国語版・韓国語版、PC/従来版へ移動できる。Streamlitコンポーネントのiframe制約を避けるため、スマホ版内のリンクは新しいタブで開く。PC/従来版の上部からもスマホ版へ戻れる。

Streamlitの静的ファイル配信はHTML/JSアプリ配信向けではないため、Streamlit Cloudではカスタムコンポーネントとして埋め込みます。CSV更新後やスマホ版JS/UI更新後は、JSON生成と診断画面用バージョン更新をまとめて実行します。

```bash
npm run build:mobile -- 2026-06-06-mobile-data-1
```

Google Drive上の音声ファイルを入れ替えた場合は、フォールバック用manifest更新も含めます。

```bash
npm run build:mobile -- 2026-06-06-mobile-data-1 --with-drive-manifest
```

個別に実行する必要がある場合は、従来通り次も使えます。

```bash
python3 tools/build_mobile_data.py
python3 tools/build_drive_audio_manifest.py
npm run version:mobile -- 2026-05-19-mobile-quality-1
```

CSV、PWA用JSON、音声ファイル、Google Driveフォールバックmanifestの整合性は次で確認します。通常は完全検証を使い、急ぎの場合だけ `--quick` でWAVヘッダ確認を省略します。

```bash
python3 tools/validate_mobile_assets.py
python3 tools/validate_mobile_assets.py --quick
```

PCでスマホUIを強制表示する確認URL:

```text
https://<your-app>.streamlit.app/?mobile_app=1&quiz=vocab
https://<your-app>.streamlit.app/?mobile_app=1&quiz=sentence
```

スマホで従来版を確認するURL:

```text
https://<your-app>.streamlit.app/?classic=1
```

PC/従来版で単語版・例文版を直接開く確認URL:

```text
https://esperanto-quiz.streamlit.app/?quiz=vocab&classic=1
https://esperanto-quiz.streamlit.app/?quiz=sentence&classic=1
https://esperanto-quiz-ko.streamlit.app/?quiz=vocab&classic=1
https://esperanto-quiz-ko.streamlit.app/?quiz=sentence&classic=1
https://esperanto-quiz-zh.streamlit.app/?quiz=vocab&classic=1
https://esperanto-quiz-zh.streamlit.app/?quiz=sentence&classic=1
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

スマホ版では、表示中のテキストがエスペラントの場合だけ音声を再生する。エスペラント→日本語では問題文を自動再生し、日本語→エスペラントでは日本語問題文を読まず、エスペラントの選択肢音声だけを手動再生対象にする。

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
7. スマホ版の音声設定をオンにし、エスペラント→日本語では問題文が自動再生され、日本語→エスペラントでは日本語問題文が再生されないことを確認。
8. 日本語→エスペラントで「問題自動＋選択肢」を選び、エスペラントの選択肢音声だけを手動再生できることを確認。
9. 不正解を含む結果画面で、復習リストの音声ボタンからエスペラント正解音声を再生できることを確認。
10. 成績画面で累積・本日・今月・殿堂ランキングが表示または適切なエラーメッセージになることを確認。
11. 診断画面でデータ件数、音声設定、ランキング状態、スコア保存状態が表示されることを確認。
12. 診断画面の単語・例文音声テストで、サンプル音声が再生できることを確認。
13. 結果画面と成績画面がスマホ幅で読みやすいことを確認。
14. 従来版を確認する場合は `?classic=1` を付けて開く。
15. PC/従来版で、上部の「PC版モード」から単語版・例文版・スマホ版を切り替えられることを確認する。
16. スマホ版の下部リンクから、日本語版・中国語版・韓国語版、PC/従来版へ移動できることを確認する。

## 3.1. UserStats再構築

`Scores` が正本です。PC版・スマホ版の保存処理は `Scores` へ追記した後、`UserStats` と `UserStatsSentence` を再集計して更新します。通信失敗などで集計シートだけが古くなった場合は、次のメンテナンスツールで `Scores` から再構築します。

まず dry-run で対象行数を確認します。

```bash
python3 tools/rebuild_user_stats.py
```

問題なければバックアップ作成後に書き込みます。

```bash
python3 tools/rebuild_user_stats.py --apply
```

別の secrets や spreadsheet を使う場合:

```bash
python3 tools/rebuild_user_stats.py --secrets .streamlit/secrets.toml --spreadsheet <spreadsheet-key-or-url> --apply
```

## 4. ローカルの鍵ファイルの扱い
- 作業後は鍵ファイルを安全な場所に移動するか削除する。
- 追加で鍵を扱う場合は、`.gitignore` にあることを確認し、誤ってステージングしないよう注意する。

## 5. 依存関係
- `requirements.txt` に `streamlit`, `pandas`, `streamlit-gsheets` を記載済み。Cloud で自動インストールされる。

## 6. トラブルシュートのヒント
- 認証エラー: Secrets の `private_key` の改行が `\n` に置換されているか確認。
- 書き込みエラー: Sheets 側でサービスアカウントが「編集者」権限になっているか確認。
- 反映遅延: ネットワーク遅延の場合があるため数秒待つ。キャッシュは `ttl=0` なので基本即時反映。
