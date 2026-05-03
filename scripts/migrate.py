#!/usr/bin/env python3
"""
Placeholder for DB migrations (e.g. Alembic).
Run from project root: python scripts/migrate.py
"""
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def main():
    # If using Alembic: os.system("alembic upgrade head")
    # For now, create_all is done in app startup and setup.py
    from app import create_app
    from extensions import db
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database schema up to date (create_all).")
        print("For versioned migrations, add Alembic and run: alembic upgrade head")


if __name__ == "__main__":
    main()
