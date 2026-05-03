"""
Security helpers (password hashing). User model uses werkzeug.
"""
from werkzeug.security import generate_password_hash, check_password_hash

__all__ = ["generate_password_hash", "check_password_hash"]
