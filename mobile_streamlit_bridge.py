from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from mobile_score_sync import save_mobile_score_request


BASE_DIR = Path(__file__).resolve().parent
MOBILE_APP_DIR = BASE_DIR / "mobile_app"
MOBILE_AUDIO_MANIFEST = MOBILE_APP_DIR / "data" / "audio_manifest.json"
DRIVE_AUDIO_DOWNLOAD_BASE = "https://drive.google.com/uc?export=download&id="
COMPONENT_VOCAB_AUDIO_BASE = "./audio/"
COMPONENT_SENTENCE_AUDIO_BASE = "./sentence-audio/"

_mobile_component = components.declare_component(
    "esperanto_mobile_pwa",
    path=str(MOBILE_APP_DIR),
)


TRUE_VALUES = {"1", "true", "yes", "on"}


def _query_flag(name: str) -> bool:
    try:
        return str(st.query_params.get(name, "")).strip().lower() in TRUE_VALUES
    except Exception:
        return False


def should_render_mobile_app(is_mobile: bool) -> bool:
    """Use the browser-side mobile app unless the user explicitly asks for classic Streamlit."""
    if _query_flag("classic"):
        return False
    if _query_flag("mobile_app"):
        return True
    return bool(is_mobile)


def _mobile_audio_config() -> dict:
    try:
        config = dict(st.secrets.get("mobile_audio", {}))
    except Exception:
        config = {}
    vocab_base_url = str(config.get("vocab_base_url", "")).strip() or COMPONENT_VOCAB_AUDIO_BASE
    sentence_base_url = str(config.get("sentence_base_url", "")).strip() or COMPONENT_SENTENCE_AUDIO_BASE
    drive_download_base_url = str(config.get("drive_download_base_url", "")).strip() or DRIVE_AUDIO_DOWNLOAD_BASE
    manifest_available = MOBILE_AUDIO_MANIFEST.exists()
    enabled = bool(vocab_base_url or sentence_base_url or manifest_available)
    return {
        "enabled": enabled,
        "vocabBaseUrl": vocab_base_url,
        "sentenceBaseUrl": sentence_base_url,
        "driveDownloadBaseUrl": drive_download_base_url,
        "useDriveManifest": manifest_available,
    }


def render_mobile_app_entry(is_mobile: bool, *, source: str) -> bool:
    """Render the localStorage-backed mobile app inside Streamlit Cloud.

    Streamlit's built-in static file serving is intentionally limited and does not
    serve arbitrary HTML/JS apps with browser-friendly MIME types. A local
    Streamlit component gives us a Cloud-compatible iframe while keeping desktop
    users on the existing app.
    """
    if not should_render_mobile_app(is_mobile):
        return False

    st.session_state.setdefault("mobile_score_sync_result", None)
    st.session_state.setdefault("mobile_score_sync_processed", {})

    st.markdown(
        """
        <style>
        div[data-testid="stToolbar"], div[data-testid="stDecoration"],
        header[data-testid="stHeader"], #MainMenu, footer {
            display: none !important;
        }
        div[data-testid="stAppViewContainer"] {
            background: #f7f8f4 !important;
        }
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        .block-container {
            max-width: 100% !important;
            padding: 0 !important;
        }
        iframe[title*="esperanto_mobile_pwa"] {
            display: block !important;
            width: 100% !important;
            min-height: 640px !important;
            border: 0 !important;
        }
        div[data-testid="stVerticalBlock"],
        div[data-testid="stVerticalBlock"] > div,
        div[data-testid="stElementContainer"] {
            gap: 0 !important;
            margin: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    component_value = _mobile_component(
        source=source,
        scoreSyncResult=st.session_state.mobile_score_sync_result,
        audioConfig=_mobile_audio_config(),
        default=None,
        key=f"esperanto_mobile_pwa_{source}",
        height=900,
    )
    if isinstance(component_value, dict) and component_value.get("type") == "save_score":
        request_id = str(component_value.get("requestId", "")).strip()
        processed = st.session_state.mobile_score_sync_processed
        if request_id and request_id not in processed:
            result = save_mobile_score_request(component_value)
            st.session_state.mobile_score_sync_result = result
            processed[request_id] = bool(result.get("ok"))
            if len(processed) > 100:
                for key in list(processed.keys())[:-100]:
                    processed.pop(key, None)
            st.rerun()
    st.markdown(
        """
        <div style="padding: 8px 12px 16px; text-align: center; font-size: 13px;">
            <a href="?classic=1" target="_self" rel="nofollow" style="color: #075f46; font-weight: 700;">
                従来のStreamlit版を開く
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return True
