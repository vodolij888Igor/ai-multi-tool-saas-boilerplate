"""
Admin module: dashboard, user credits and plan management, tier preview, blog. 403 for non-admins.
"""
import re
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort, session
from flask_login import login_required, current_user
from models import User, BlogArticle, BlogCategory
from extensions import db
from backend.modules.credits.services import add_credits as credits_add, deduct_credits as credits_deduct
from tools_config import VALID_PLAN_NAMES

admin_bp = Blueprint("admin", __name__)
PREVIEW_CHOICES = ("Full", "Pro", "Starter")  # + Off


def _slugify(text):
    if not text:
        return ""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "article"


def admin_required():
    if not current_user.is_authenticated or not getattr(current_user, "is_admin", False):
        abort(403)


@admin_bp.route("/admin")
@login_required
def admin_dashboard():
    admin_required()
    users = User.query.order_by(User.created_at.desc()).all()
    tier_preview = session.get("tier_preview")
    return render_template(
        "admin/dashboard.html",
        users=users,
        plan_choices=VALID_PLAN_NAMES,
        preview_choices=PREVIEW_CHOICES,
        tier_preview=tier_preview,
    )


@admin_bp.route("/admin/user/<int:user_id>/credits", methods=["POST"])
@login_required
def admin_user_credits(user_id):
    admin_required()
    user = User.query.get_or_404(user_id)
    try:
        amount = int(request.form.get("amount", 0))
    except (TypeError, ValueError):
        amount = 0
    action = (request.form.get("action") or "").strip().lower()
    if amount <= 0:
        flash("Please enter a positive amount.", "warning")
        return redirect(url_for("admin.admin_dashboard"))
    if action == "add":
        credits_add(user, amount)
        flash(f"Added {amount} credits to {user.email}. New balance: {user.credits}.", "success")
    elif action == "remove":
        credits_deduct(user, amount)
        flash(f"Removed {amount} credits from {user.email}. New balance: {user.credits}.", "success")
    else:
        flash("Invalid action. Use Add or Remove.", "warning")
    return redirect(url_for("admin.admin_dashboard"))


@admin_bp.route("/admin/user/<int:user_id>/plan", methods=["POST"])
@login_required
def admin_user_plan(user_id):
    admin_required()
    user = User.query.get_or_404(user_id)
    plan = (request.form.get("plan") or "").strip()
    if plan not in VALID_PLAN_NAMES:
        flash("Invalid plan. Use Starter, Pro, or Full.", "warning")
        return redirect(url_for("admin.admin_dashboard"))
    user.plan_name = plan
    db.session.commit()
    flash(f"Plan for {user.email} set to {plan}.", "success")
    return redirect(url_for("admin.admin_dashboard"))


@admin_bp.route("/admin/preview-tier", methods=["POST"])
@login_required
def admin_preview_tier():
    admin_required()
    value = (request.form.get("tier_preview") or "").strip()
    if value in ("Starter", "Pro", "Full"):
        session["tier_preview"] = value
        flash(f"Preview mode: viewing product as {value}. Your access remains full.", "info")
    elif value.lower() == "off" or value == "":
        session.pop("tier_preview", None)
        flash("Preview off. You see the app with full access.", "info")
    else:
        flash("Invalid preview choice.", "warning")
    return redirect(request.referrer or url_for("admin.admin_dashboard"))


# ---------- Blog management ----------

@admin_bp.route("/admin/blog")
@login_required
def admin_blog_list():
    admin_required()
    articles = BlogArticle.query.order_by(BlogArticle.updated_at.desc()).all()
    return render_template("admin/blog_list.html", articles=articles)


@admin_bp.route("/admin/blog/categories")
@login_required
def admin_blog_categories():
    admin_required()
    categories = BlogCategory.query.order_by(BlogCategory.name).all()
    return render_template("admin/blog_categories.html", categories=categories)


@admin_bp.route("/admin/blog/categories", methods=["POST"])
@login_required
def admin_blog_category_create():
    admin_required()
    name = (request.form.get("name") or "").strip()
    slug = (request.form.get("slug") or "").strip() or _slugify(name)
    if not name:
        flash("Category name is required.", "warning")
        return redirect(url_for("admin.admin_blog_categories"))
    if BlogCategory.query.filter_by(slug=slug).first():
        flash("A category with this slug already exists.", "warning")
        return redirect(url_for("admin.admin_blog_categories"))
    cat = BlogCategory(name=name, slug=slug)
    db.session.add(cat)
    db.session.commit()
    flash(f"Category '{name}' created.", "success")
    return redirect(url_for("admin.admin_blog_categories"))


@admin_bp.route("/admin/blog/create", methods=["GET", "POST"])
@login_required
def admin_blog_create():
    admin_required()
    categories = BlogCategory.query.order_by(BlogCategory.name).all()
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        slug = (request.form.get("slug") or "").strip() or _slugify(title)
        excerpt = (request.form.get("excerpt") or "").strip() or None
        content = request.form.get("content") or ""
        category_id = request.form.get("category_id")
        category_id = int(category_id) if category_id else None
        status = (request.form.get("status") or "draft").strip()
        if status not in ("draft", "published"):
            status = "draft"
        meta_title = (request.form.get("meta_title") or "").strip() or None
        meta_description = (request.form.get("meta_description") or "").strip() or None
        meta_keywords = (request.form.get("meta_keywords") or "").strip() or None
        if not title:
            flash("Title is required.", "warning")
            return render_template("admin/blog_form.html", categories=categories, article=None)
        if BlogArticle.query.filter_by(slug=slug).first():
            flash("An article with this slug already exists. Choose another slug.", "warning")
            return render_template("admin/blog_form.html", categories=categories, article=None)
        published_at = datetime.utcnow() if status == "published" else None
        article = BlogArticle(
            title=title,
            slug=slug,
            excerpt=excerpt,
            content=content,
            author_id=current_user.id,
            category_id=category_id,
            status=status,
            published_at=published_at,
            meta_title=meta_title,
            meta_description=meta_description,
            meta_keywords=meta_keywords,
        )
        db.session.add(article)
        db.session.commit()
        flash("Article created.", "success")
        return redirect(url_for("admin.admin_blog_list"))
    return render_template("admin/blog_form.html", categories=categories, article=None)


@admin_bp.route("/admin/blog/<int:article_id>/edit", methods=["GET", "POST"])
@login_required
def admin_blog_edit(article_id):
    admin_required()
    article = BlogArticle.query.get_or_404(article_id)
    categories = BlogCategory.query.order_by(BlogCategory.name).all()
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        slug = (request.form.get("slug") or "").strip() or _slugify(title)
        excerpt = (request.form.get("excerpt") or "").strip() or None
        content = request.form.get("content") or ""
        category_id = request.form.get("category_id")
        category_id = int(category_id) if category_id else None
        status = (request.form.get("status") or "draft").strip()
        if status not in ("draft", "published"):
            status = "draft"
        meta_title = (request.form.get("meta_title") or "").strip() or None
        meta_description = (request.form.get("meta_description") or "").strip() or None
        meta_keywords = (request.form.get("meta_keywords") or "").strip() or None
        if not title:
            flash("Title is required.", "warning")
            return render_template("admin/blog_form.html", categories=categories, article=article)
        existing = BlogArticle.query.filter_by(slug=slug).first()
        if existing and existing.id != article.id:
            flash("An article with this slug already exists. Choose another slug.", "warning")
            return render_template("admin/blog_form.html", categories=categories, article=article)
        article.title = title
        article.slug = slug
        article.excerpt = excerpt
        article.content = content
        article.category_id = category_id
        article.meta_title = meta_title
        article.meta_description = meta_description
        article.meta_keywords = meta_keywords
        old_status = article.status
        article.status = status
        if status == "published" and not article.published_at:
            article.published_at = datetime.utcnow()
        elif status == "draft":
            article.published_at = None
        db.session.commit()
        flash("Article updated.", "success")
        return redirect(url_for("admin.admin_blog_list"))
    return render_template("admin/blog_form.html", categories=categories, article=article)


@admin_bp.route("/admin/blog/<int:article_id>/delete", methods=["POST"])
@login_required
def admin_blog_delete(article_id):
    admin_required()
    article = BlogArticle.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash("Article deleted.", "info")
    return redirect(url_for("admin.admin_blog_list"))
