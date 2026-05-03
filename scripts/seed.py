#!/usr/bin/env python3
"""
Seed script: create demo admin user or sample data.
Run from project root: python scripts/seed.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def main():
    from app import create_app
    from extensions import db
    from models import User

    app = create_app()
    with app.app_context():
        # Example: ensure one admin exists (set email in env or below)
        admin_email = os.environ.get("ADMIN_EMAIL", "admin@example.com")
        user = User.query.filter_by(email=admin_email).first()
        if not user:
            user = User(email=admin_email, credits=100, is_admin=True)
            user.set_password(os.environ.get("ADMIN_PASSWORD", "changeme"))
            db.session.add(user)
            db.session.commit()
            print("Created admin user:", admin_email)
        else:
            if not user.is_admin:
                user.is_admin = True
                db.session.commit()
                print("Set existing user as admin:", admin_email)
            else:
                print("Admin already exists:", admin_email)


if __name__ == "__main__":
    main()
