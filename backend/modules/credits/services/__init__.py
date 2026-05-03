"""
Credits module service: add/deduct credits and check if user can use AI tools.
"""
from extensions import db
from models import User


def add_credits(user, amount: int) -> None:
    """Add credits to user and commit."""
    if amount <= 0:
        return
    user.credits = getattr(user, "credits", 0) + amount
    db.session.commit()


def deduct_credits(user, amount: int) -> int:
    """Deduct credits (floor at 0). Commits. Returns actual amount deducted."""
    if amount <= 0:
        return 0
    current = getattr(user, "credits", 0)
    deducted = min(amount, current)
    user.credits = max(0, current - amount)
    db.session.commit()
    return deducted


def can_use_tools(user):
    """(allowed: bool, error_message or None)."""
    if not user:
        return False, "User not found."
    credits = getattr(user, "credits", 0)
    if credits < 1:
        return False, "You have run out of credits. Please upgrade your plan."
    if credits > 10 and not getattr(user, "is_subscription_active", False):
        return False, "Your credits are locked. Please reactivate your subscription to continue."
    return True, None
