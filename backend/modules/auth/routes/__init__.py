"""
Auth module: register, login, logout. Uses auth.services for validation and user creation.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models import User
from backend.modules.auth.services import validate_email, create_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
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

        user = create_user(email, password)
        if user:
            flash("Account created. You have 10 free credits to try our AI tools. Please log in.", "success")
            return redirect(url_for("auth.login"))
        flash("Registration failed. Please try again.", "danger")
        return render_template("auth/register.html")

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
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
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
