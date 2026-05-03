#!/usr/bin/env python3
"""
Setup script: create instance dir, optional DB, and ensure .env exists.
Run from project root: python scripts/setup.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def main():
    instance_path = os.path.join(ROOT, "instance")
    os.makedirs(instance_path, exist_ok=True)
    print("Instance directory OK:", instance_path)

    env_path = os.path.join(ROOT, ".env")
    if not os.path.isfile(env_path):
        example = os.path.join(ROOT, ".env.example")
        if os.path.isfile(example):
            with open(example, "r", encoding="utf-8") as f:
                content = f.read()
            with open(env_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Created .env from .env.example. Please edit .env with your keys.")
        else:
            print("No .env found. Create .env with SECRET_KEY and OPENAI_API_KEY.")
    else:
        print(".env exists.")

    # Optional: create app and db
    try:
        from app import create_app
        app = create_app()
        with app.app_context():
            from extensions import db
            db.create_all()
            print("Database tables created.")
    except Exception as e:
        print("Database setup skipped or failed:", e)

    print("Setup done.")


if __name__ == "__main__":
    main()
