"""
Auth routes: register, login, logout.
New users receive 10 free credits (default in User model).
"""
import re
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models import User

auth_bp = Blueprint("auth", __name__)


def validate_email(email):
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registration: email + password. New users get 10 free credits."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not email or not password:
            flash("Please fill in all fields.", "danger")
            return render_template("auth/register.html")

        if not validate_email(email):
            flash("Please enter a valid email address.", "danger")
            return render_template("auth/register.html")

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "danger")
            return render_template("auth/register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template("auth/register.html")

        if User.query.filter_by(email=email).first():
            flash("An account with this email already exists.", "danger")
            return render_template("auth/register.html")

        try:
            user = User(email=email, credits=10)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Account created. You have 10 free credits to try our AI tools. Please log in.", "success")
            return redirect(url_for("auth.login"))
        except Exception:
            db.session.rollback()
            flash("Registration failed. Please try again.", "danger")
            return render_template("auth/register.html")

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login with email and password."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        remember = bool(request.form.get("remember"))

        if not email or not password:
            flash("Please fill in all fields.", "danger")
            return render_template("auth/login.html")

        user = User.query.filter(db.func.lower(User.email) == email).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get("next")
            flash("Welcome back! You have {} credits remaining.".format(user.credits), "success")
            return redirect(next_page) if next_page else redirect(url_for("main.index"))
        flash("Invalid email or password.", "danger")
        return render_template("auth/login.html")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
