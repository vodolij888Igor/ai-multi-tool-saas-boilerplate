"""
AI provider config: OpenAI API key and model.
"""
from config.env import get

OPENAI_API_KEY = get("OPENAI_API_KEY", "").strip().replace("\ufeff", "").replace('"', "").replace("'", "")
OPENAI_MODEL = get("OPENAI_MODEL", "gpt-4o-mini")
