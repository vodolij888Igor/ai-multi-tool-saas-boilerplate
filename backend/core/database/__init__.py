"""
Database instance. Re-exports Flask-SQLAlchemy from project root.
"""
from extensions import db

__all__ = ["db"]
