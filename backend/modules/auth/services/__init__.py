"""
Auth module service: validation and user creation.
"""
import re
from extensions import db
from models import User


def validate_email(email: str) -> bool:
    """Return True if email format is valid."""
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email.strip()) is not None


def create_user(email: str, password: str, credits: int = None):
    """
    Create and persist a new user. Returns User on success, None on failure (caller may rollback).
    """
    if credits is None:
        from config.constants import DEFAULT_FREE_CREDITS
        credits = DEFAULT_FREE_CREDITS
    try:
        user = User(email=email.strip().lower(), credits=credits)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    except Exception:
        db.session.rollback()
        return None
