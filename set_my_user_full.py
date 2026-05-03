"""One-off: add plan_name column if missing and set first user to Full plan."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text
from app import create_app
from models import User
from extensions import db

app = create_app()
with app.app_context():
    try:
        db.session.execute(text("ALTER TABLE user ADD COLUMN plan_name VARCHAR(20)"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        if "duplicate column" not in str(e).lower():
            raise

    user = User.query.first()
    if not user:
        print("No user found in database.")
        sys.exit(1)
    user.plan_name = "Full"
    db.session.commit()
    print(f"Updated user id={user.id} email={user.email}: plan_name=Full (all 20 tools)")
