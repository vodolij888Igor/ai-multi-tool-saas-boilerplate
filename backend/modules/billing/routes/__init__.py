"""
Billing module: pricing page, Stripe checkout, success, customer portal.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import User
from config.constants import CREDITS_BY_PLAN
from backend.modules.credits.services import add_credits as credits_add
from backend.services.payments_service import (
    create_checkout_session as create_stripe_checkout,
    retrieve_checkout_session,
    create_portal_session as create_stripe_portal,
)

billing_bp = Blueprint("billing", __name__)


@billing_bp.route("/pricing")
def pricing():
    return render_template("pricing.html")


@billing_bp.route("/create-checkout-session/<plan_type>")
@login_required
def create_checkout_session(plan_type):
    plan_type = (plan_type or "").lower()
    if plan_type not in ("pro", "business"):
        flash("Invalid plan.", "warning")
        return redirect(url_for("billing.pricing"))
    base = request.url_root.rstrip("/")
    url, err = create_stripe_checkout(plan_type, current_user.id, current_user.email, base)
    if err:
        flash(err, "warning")
        return redirect(url_for("billing.pricing"))
    return redirect(url)


@billing_bp.route("/success")
@login_required
def success():
    session_id = request.args.get("session_id")
    if not session_id:
        flash("No session provided.", "warning")
        return redirect(url_for("billing.pricing"))
    checkout = retrieve_checkout_session(session_id)
    if not checkout:
        flash("Invalid or expired session.", "warning")
        return redirect(url_for("billing.pricing"))
    if checkout.payment_status != "paid":
        flash("Payment was not completed.", "warning")
        return redirect(url_for("billing.pricing"))
    user_id = checkout.client_reference_id
    plan_type = (checkout.metadata or {}).get("plan_type", "").lower()
    if not user_id or plan_type not in CREDITS_BY_PLAN:
        flash("Invalid session data.", "warning")
        return redirect(url_for("ai.dashboard"))
    if int(user_id) != current_user.id:
        flash("Session does not match your account.", "warning")
        return redirect(url_for("ai.dashboard"))
    user = User.query.get(current_user.id)
    if not user:
        return redirect(url_for("ai.dashboard"))
    user.is_subscription_active = True
    if getattr(checkout, "customer", None):
        user.stripe_customer_id = checkout.customer
    credits_add(user, CREDITS_BY_PLAN[plan_type])
    flash(
        f"Payment successful! {CREDITS_BY_PLAN[plan_type]} credits added. Your subscription is active.",
        "success",
    )
    return redirect(url_for("ai.dashboard"))


@billing_bp.route("/settings/create-portal-session", methods=["POST"])
@login_required
def create_portal_session():
    user = User.query.get(current_user.id)
    if not user or not user.stripe_customer_id:
        flash("No billing account found. Subscribe first to manage billing.", "info")
        return redirect(url_for("users.settings"))
    base = request.url_root.rstrip("/")
    url, err = create_stripe_portal(user.stripe_customer_id, f"{base}/settings")
    if err:
        flash(err, "danger")
        return redirect(url_for("users.settings"))
    return redirect(url)
