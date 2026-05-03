"""
DEPRECATED: Use the config package (config/app.py, config/constants.py) and config.Config in config/__init__.py.
This file is kept for backward compatibility. Config.LANGUAGES is re-exported from config/__init__.py.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Клас конфігурації Flask додатку"""
    
    # Секретний ключ для сесій
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # OpenAI налаштування
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-4o-mini')
    
    # Максимальна довжина контенту
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # База даних SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Babel: default locale for first-time visitors and fallback
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = {
        'en': '🇺🇸 English',
        'uk': '🇺🇦 Українська',
        'es': '🇪🇸 Español',
        'ru': '🇷🇺 Русский',
        'de': '🇩🇪 Deutsch',
        'fr': '🇫🇷 Français',
    }

