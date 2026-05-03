"""
Payments config: Stripe keys and plan mapping.
"""
from config.env import get
from config.constants import CREDITS_BY_PLAN, PRICE_BY_PLAN_CENTS

STRIPE_SECRET_KEY = get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = get("STRIPE_PUBLISHABLE_KEY")
CREDITS_BY_PLAN = CREDITS_BY_PLAN
PRICE_BY_PLAN_CENTS = PRICE_BY_PLAN_CENTS
