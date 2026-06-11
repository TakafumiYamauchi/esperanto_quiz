import html

import streamlit as st


MODE_ALIASES = {
    "vocab": "vocab",
    "word": "vocab",
    "words": "vocab",
    "token": "vocab",
    "tokens": "vocab",
    "単語": "vocab",
    "語彙": "vocab",
    "sentence": "sentence",
    "sentences": "sentence",
    "phrase": "sentence",
    "phrases": "sentence",
    "例文": "sentence",
    "文章": "sentence",
}

MODE_SWITCH_LABELS = {
    "ja": {
        "caption": "PC版モード",
        "vocab": "単語",
        "sentence": "例文",
        "mobile": "スマホ版",
    },
    "zh": {
        "caption": "PC版模式",
        "vocab": "单词",
        "sentence": "例句",
        "mobile": "手机版",
    },
    "ko": {
        "caption": "PC 버전 모드",
        "vocab": "단어",
        "sentence": "예문",
        "mobile": "모바일 버전",
    },
}


def get_classic_quiz_mode(default: str = "vocab") -> str:
    """Resolve the classic Streamlit quiz mode from URL query parameters."""
    fallback = "sentence" if default == "sentence" else "vocab"
    for key in ("quiz", "mode", "view"):
        try:
            raw = str(st.query_params.get(key, "")).strip().lower()
        except Exception:
            raw = ""
        if raw:
            return MODE_ALIASES.get(raw, fallback)
    return fallback


def render_classic_mode_switch(current_mode: str, target_lang: str = "ja") -> None:
    """Render a small mode switch for desktop/classic Streamlit views."""
    lang = target_lang if target_lang in MODE_SWITCH_LABELS else "ja"
    labels = MODE_SWITCH_LABELS[lang]
    current = "sentence" if current_mode == "sentence" else "vocab"

    def item(mode: str) -> str:
        active = mode == current
        class_name = "classic-mode-link is-active" if active else "classic-mode-link"
        label = html.escape(labels[mode])
        href = f"?quiz={mode}&classic=1"
        return f"<a class='{class_name}' href='{href}' target='_self' rel='nofollow'>{label}</a>"

    mobile_href = f"?mobile_app=1&quiz={current}"

    st.markdown(
        f"""
        <style>
        .classic-mode-switch {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin: 0.4rem 0 1.0rem;
            flex-wrap: wrap;
        }}
        .classic-mode-caption {{
            color: #647067;
            font-size: 0.88rem;
            font-weight: 700;
            margin-right: 2px;
        }}
        .classic-mode-link {{
            display: inline-flex;
            min-width: 7.5rem;
            justify-content: center;
            align-items: center;
            padding: 0.55rem 1.0rem;
            border: 1px solid #cfd8d1;
            border-radius: 8px;
            color: #0b5c43 !important;
            background: #ffffff;
            font-weight: 800;
            text-decoration: none !important;
        }}
        .classic-mode-link:hover {{
            border-color: #12815f;
            background: #eef8f2;
        }}
        .classic-mode-link.is-active {{
            background: #0b7f5d;
            border-color: #0b7f5d;
            color: #ffffff !important;
        }}
        .classic-mode-link-secondary {{
            color: #5b654f !important;
            background: #f6f7f2;
        }}
        .classic-mode-link-secondary:hover {{
            color: #0b5c43 !important;
        }}
        @media (max-width: 640px) {{
            .classic-mode-switch {{
                margin-top: 0.2rem;
                gap: 6px;
            }}
            .classic-mode-caption {{
                width: 100%;
                text-align: center;
            }}
            .classic-mode-link {{
                flex: 1 1 42%;
                min-width: 0;
            }}
        }}
        </style>
        <nav class="classic-mode-switch" aria-label="{html.escape(labels['caption'])}">
            <span class="classic-mode-caption">{html.escape(labels['caption'])}</span>
            {item("vocab")}
            {item("sentence")}
            <a class="classic-mode-link classic-mode-link-secondary" href="{mobile_href}" target="_self" rel="nofollow">
                {html.escape(labels["mobile"])}
            </a>
        </nav>
        """,
        unsafe_allow_html=True,
    )
