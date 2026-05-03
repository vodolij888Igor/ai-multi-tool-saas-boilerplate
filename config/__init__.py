# Config package: load app, ai, payments from env and constants.
from config.constants import SUPPORTED_LANGUAGES


class Config:
    """Legacy Config class for routes that expect Config.LANGUAGES."""
    LANGUAGES = SUPPORTED_LANGUAGES
