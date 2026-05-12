# Git Helper Windows/Ubuntu 互換セット

このフォルダに、Windows と Ubuntu の両方で使うための本命ファイルをまとめました。

## 入っているもの

- `.gitattributes`
  - Git 管理上の改行ルールを固定します。
  - `.sh` は LF、`.cmd` は CRLF、PDF や画像は binary 扱いにします。
- `git_command_2512.sh`
  - Ubuntu / Linux 用です。
  - LF 改行で使います。
  - Git 上では `100755`、つまり実行可能として登録するのが理想です。
- `git_command_2512.cmd`
  - Windows 用です。
  - CRLF 改行で使います。

## 各リポジトリに入れる方法

対象リポジトリの直下に、この3ファイルをコピーしてください。

その後、対象リポジトリで次を実行します。

```powershell
git config core.autocrlf false
git config core.eol lf
git config core.filemode false
git update-index --chmod=+x git_command_2512.sh
git update-index --chmod=-x git_command_2512.cmd
git add .gitattributes git_command_2512.sh git_command_2512.cmd
git add --renormalize .gitattributes git_command_2512.sh git_command_2512.cmd
git status
```

問題なければコミットします。

```powershell
git commit -m "Add Windows Ubuntu compatibility settings"
```

## 使い分け

Windows では:

```powershell
.\git_command_2512.cmd
```

Ubuntu では:

```bash
./git_command_2512.sh
```

もし Ubuntu で権限エラーが出る場合は、対象リポジトリで一度だけ次を実行してください。

```bash
chmod +x git_command_2512.sh
```

## 確認コマンド

対象リポジトリで次を実行すると、改行と権限を確認できます。

```powershell
git ls-files --eol git_command_2512.sh git_command_2512.cmd .gitattributes
git ls-files -s git_command_2512.sh git_command_2512.cmd .gitattributes
```

理想は次の形です。

```text
git_command_2512.sh  i/lf  w/lf    100755
git_command_2512.cmd i/lf  w/crlf  100644
```
