"""
Application constants: plans, credits, limits, supported languages.
"""

# Supported UI languages (session + Babel)
SUPPORTED_LANGUAGES = ["en", "uk", "ua", "es", "ru", "de", "fr"]

# Credits and pricing (cents)
CREDITS_BY_PLAN = {"pro": 500, "business": 2000}
PRICE_BY_PLAN_CENTS = {"pro": 1900, "business": 4900}

# Default free credits for new users
DEFAULT_FREE_CREDITS = 10

# Content limits
MAX_CONTENT_LENGTH_MB = 16

# Plan names for display
PLAN_NAMES = {"pro": "Pro", "business": "Business", "starter": "Starter", "free": "Free"}
