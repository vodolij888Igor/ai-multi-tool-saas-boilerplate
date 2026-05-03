"""
OpenAI service: single place for API key and chat completion.
Uses config.ai for key and model; tools_config for system prompt.
"""
import os
from openai import OpenAI


def get_client():
    """Build OpenAI client with key from env (with .env fallback)."""
    raw_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not raw_key:
        try:
            with open(".env", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("OPENAI_API_KEY="):
                        raw_key = line.split("=", 1)[1].strip()
                        break
        except FileNotFoundError:
            pass
    raw_key = raw_key.replace("\ufeff", "").replace('"', "").replace("'", "")
    return OpenAI(api_key=raw_key) if raw_key else None


def get_model():
    return os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


def generate(system_prompt: str, user_message: str, model: str = None):
    """
    Call chat completion. Returns (content, None) or (None, error_string).
    """
    client = get_client()
    if not client:
        return None, "OPENAI_API_KEY not configured."
    model = model or get_model()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return (response.choices[0].message.content, None)
    except Exception as e:
        return None, str(e)
