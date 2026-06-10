# Google Drive 旧重複音声 削除候補一覧

作成日: 2026-06-11
最終確認: 2026-06-11

対象Driveフォルダ: `Esperanto例文5000文_収録音声`

## 現在の確認結果

`tools/build_drive_audio_manifest.py` でGoogle Driveを再読込した結果:

- Drive上の例文WAV: 5000件
- アプリが参照する必要WAV: 5000件
- matched: 5000件
- missing: 0件
- extra: 0件

現在の `mobile_app/data/sentences.json` から参照されない旧音声は残っていない。
Google Drive上から削除してよい候補は0件。

## 削除候補 0件

```text
```

## 内訳

- 手作業削除後に残っている旧音声: 0件
- Drive fallbackとして必要な5000件はすべて存在するため、アプリ動作上の不足はない。
