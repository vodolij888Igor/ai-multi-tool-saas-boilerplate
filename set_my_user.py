"""One-off: set first user to credits=50, is_subscription_active=False."""
import os
import sys

# Add project root
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text
from app import create_app
from models import User
from extensions import db

app = create_app()
with app.app_context():
    # Add column if missing (SQLite doesn't update schema on create_all)
    try:
        db.session.execute(text("ALTER TABLE user ADD COLUMN is_subscription_active BOOLEAN DEFAULT 0 NOT NULL"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        if "duplicate column" not in str(e).lower():
            raise

    user = User.query.first()
    if not user:
        print("No user found in database.")
        sys.exit(1)
    user.credits = 50
    user.is_subscription_active = False
    db.session.commit()
    print(f"Updated user id={user.id} email={user.email}: credits=50, is_subscription_active=False")
