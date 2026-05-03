"""
Environment variables and defaults.
Load via dotenv in app bootstrap; access through config.app, config.ai, config.payments.
"""
import os
from dotenv import load_dotenv

load_dotenv()


def get(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


def get_int(key: str, default: int = 0) -> int:
    try:
        return int(os.environ.get(key, str(default)))
    except (TypeError, ValueError):
        return default


def get_bool(key: str, default: bool = False) -> bool:
    v = os.environ.get(key, "").strip().lower()
    return v in ("1", "true", "yes") if v else default
