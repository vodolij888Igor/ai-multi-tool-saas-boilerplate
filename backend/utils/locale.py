"""
Locale from session or cookie only. Strict default English; browser language is never used.
"""
from flask import session, request

_VALID = frozenset(("en", "uk", "ua", "es", "ru", "de", "fr"))


def get_locale():
    # 1) Session (user already chose language this session)
    lang = session.get("language") or session.get("locale")
    if lang and lang in _VALID:
        return "uk" if lang in ("uk", "ua") else lang
    # 2) Cookie (user chose language on a previous visit)
    cookie_lang = request.cookies.get("preferred_lang")
    if cookie_lang and cookie_lang in _VALID:
        session["language"] = cookie_lang
        session["locale"] = "uk" if cookie_lang in ("ua", "uk") else cookie_lang
        return "uk" if cookie_lang in ("uk", "ua") else cookie_lang
    # 3) First visit: strict default English (browser language is NOT used)
    return "en"


def get_language_for_prompt():
    """Return full language name for AI prompt."""
    lang = get_locale()
    return {"uk": "Ukrainian", "en": "English", "es": "Spanish", "ru": "Russian", "de": "German", "fr": "French"}.get(
        lang, "English"
    )
