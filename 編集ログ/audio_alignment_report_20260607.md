# 音声整合確認レポート

作成日: 2026-06-07

## 対象

- 例文CSV: `phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv`
- 例文音声: `Esperanto例文5000文_収録音声/`
- 音声生成: RHVoice `spomenka` / 24000 Hz WAV

## 実施前

- rows: 5000
- exact: 4999
- legacy fallback: 0
- prefix fallback: 1
- missing: 0

## 実施内容

- 差し替え候補一覧を作成: `編集ログ/phrases_audio_replacement_candidates_20260607.csv`
- RHVoice/Spomenka で exact-key WAV を生成: `編集ログ/phrases_audio_replacement_generation_20260607.csv`
- 旧prefix/legacy音声を退避: `Esperanto例文5000文_収録音声/archived_replaced_audio_20260607/`
- 退避件数: 1

## 実施後

- rows: 5000
- exact WAV: 5000
- bad audio: 0

## 補足

- アプリは `PhraseID - 155` と Esperanto 文の正規化キーで音声を先に exact 検索する。
- 今回の更新後は、CSV上のEsperanto文と同じキーのWAVが全件存在するため、旧音声へのprefix fallbackは通常使われない。
- 検証はファイル名・存在・WAV可読性の確認であり、ASRによる発話内容の文字起こし照合までは含まない。
