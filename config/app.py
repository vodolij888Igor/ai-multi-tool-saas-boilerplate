"""
Application config: secret key, database, Babel, content limits.
"""
import os
from config.env import get, get_int
from config.constants import MAX_CONTENT_LENGTH_MB, SUPPORTED_LANGUAGES

SECRET_KEY = get("SECRET_KEY", "dev-123")
DATABASE_URL = get("DATABASE_URL")  # None -> app will set SQLite path
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = (MAX_CONTENT_LENGTH_MB * 1024 * 1024) if MAX_CONTENT_LENGTH_MB else None

# Babel
BABEL_DEFAULT_LOCALE = get("BABEL_DEFAULT_LOCALE", "en")
BABEL_DEFAULT_TIMEZONE = get("BABEL_DEFAULT_TIMEZONE", "UTC")
LANGUAGES = SUPPORTED_LANGUAGES
