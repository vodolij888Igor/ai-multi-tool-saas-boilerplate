"""
Stripe payments: checkout session, success handling, customer portal.
Uses config.payments for keys and plan constants.
"""
import stripe
from flask import request
from config.constants import CREDITS_BY_PLAN
from config.payments import STRIPE_SECRET_KEY, PRICE_BY_PLAN_CENTS


def ensure_stripe():
    if not STRIPE_SECRET_KEY:
        return False
    stripe.api_key = STRIPE_SECRET_KEY
    return True


def create_checkout_session(plan_type: str, user_id: int, user_email: str, base_url: str):
    """
    Create Stripe Checkout Session. Returns (session_url, None) or (None, error_message).
    """
    if not ensure_stripe():
        return None, "Payment is not configured."
    plan_type = (plan_type or "").lower()
    if plan_type not in ("pro", "business"):
        return None, "Invalid plan."
    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            payment_method_types=["card"],
            line_items=[
                {
                    "quantity": 1,
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": PRICE_BY_PLAN_CENTS[plan_type],
                        "product_data": {
                            "name": f"MindixoAI — {plan_type.capitalize()} Plan",
                            "description": f"{CREDITS_BY_PLAN[plan_type]} credits / month",
                        },
                    },
                }
            ],
            success_url=f"{base_url}/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{base_url}/pricing",
            client_reference_id=str(user_id),
            customer_email=user_email,
            metadata={"plan_type": plan_type},
        )
        return session.url, None
    except Exception as e:
        return None, str(e)


def retrieve_checkout_session(session_id: str):
    """Retrieve Stripe Checkout Session or None."""
    if not ensure_stripe():
        return None
    try:
        return stripe.checkout.Session.retrieve(session_id)
    except Exception:
        return None


def create_portal_session(customer_id: str, return_url: str):
    """Create Stripe Customer Portal session. Returns (url, None) or (None, error)."""
    if not ensure_stripe():
        return None, "Payment is not configured."
    try:
        portal = stripe.billing_portal.Session.create(
            customer=customer_id,
            return_url=return_url,
        )
        return portal.url, None
    except Exception as e:
        return None, str(e)
