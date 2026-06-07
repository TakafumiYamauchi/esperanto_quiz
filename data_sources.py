from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
VOCAB_CSV = BASE_DIR / "2890 Gravaj Esperantaj Vortoj kun Signifoj en la Japana, Ĉina kaj Korea_260505_plej_nova.csv"
PHRASE_CSV = BASE_DIR / "phrases_eo_en_ja_zh_ko_ru_fulfilled_260505.csv"

# 例文音声/画像キーの連番オフセット（単一の信頼できる情報源）。
# PhraseID 156–5155 を 0001–5000 の連番に対応づける: f"{PhraseID - PHRASE_ID_OFFSET:04d}_<key>"。
# 以前は sentence_app.py・各言語クローン・tools の計7ファイルに 155 が直書きされていた。
PHRASE_ID_OFFSET = 155
