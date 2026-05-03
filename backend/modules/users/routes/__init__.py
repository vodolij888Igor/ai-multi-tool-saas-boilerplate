"""
Users module: settings (profile, password, subscription link).
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    user = User.query.get(current_user.id)
    if not user:
        return redirect(url_for("ai.dashboard"))

    if request.method == "POST":
        action = request.form.get("action")
        if action == "update_password":
            current_password = request.form.get("current_password", "")
            new_password = request.form.get("new_password", "")
            confirm_password = request.form.get("confirm_password", "")
            if not current_password or not new_password or not confirm_password:
                flash("Please fill in all password fields.", "warning")
                return redirect(url_for("users.settings"))
            if not user.check_password(current_password):
                flash("Current password is incorrect.", "danger")
                return redirect(url_for("users.settings"))
            if len(new_password) < 6:
                flash("New password must be at least 6 characters.", "warning")
                return redirect(url_for("users.settings"))
            if new_password != confirm_password:
                flash("New passwords do not match.", "warning")
                return redirect(url_for("users.settings"))
            user.set_password(new_password)
            db.session.commit()
            flash("Password updated successfully.", "success")
            return redirect(url_for("users.settings"))

    plan_name = "Pro" if user.is_subscription_active else "Free"
    return render_template("settings.html", user=user, plan_name=plan_name)
