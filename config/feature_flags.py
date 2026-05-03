"""
Feature flags for optional functionality (email, analytics, etc.).
"""
from config.env import get_bool

# Enable sending transactional emails (e.g. welcome, password reset)
FEATURE_EMAIL = get_bool("FEATURE_EMAIL", False)
# Enable analytics / tracking
FEATURE_ANALYTICS = get_bool("FEATURE_ANALYTICS", False)
