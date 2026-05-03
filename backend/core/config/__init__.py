"""
Core config: re-export from project config package for backend use.
"""
try:
    from config.app import (
        SECRET_KEY,
        SQLALCHEMY_TRACK_MODIFICATIONS,
        MAX_CONTENT_LENGTH,
    )
    from config.constants import SUPPORTED_LANGUAGES
except ImportError:
    SECRET_KEY = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = None
    SUPPORTED_LANGUAGES = ["en", "uk", "ua", "es", "ru", "de", "fr"]

__all__ = [
    "SECRET_KEY",
    "SQLALCHEMY_TRACK_MODIFICATIONS",
    "MAX_CONTENT_LENGTH",
    "SUPPORTED_LANGUAGES",
]
