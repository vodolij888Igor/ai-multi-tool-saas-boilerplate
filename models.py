from datetime import datetime
from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """User model for SaaS Boilerplate: id, email (unique), hashed password, credits, created_at."""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(256), nullable=False)  # stores hashed password
    credits = db.Column(db.Integer, default=10, nullable=False)
    is_subscription_active = db.Column(db.Boolean, default=False, nullable=False, server_default="0")
    plan_name = db.Column(db.String(20), nullable=True)  # Starter, Pro, Full — used for tier/tool access
    is_admin = db.Column(db.Boolean, default=False, nullable=False, server_default="0")
    stripe_customer_id = db.Column(db.String(120), nullable=True, index=True)  # for Stripe Customer Portal
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    projects = db.relationship("Project", backref="author", lazy=True)

    def set_password(self, raw_password: str) -> None:
        self.password = generate_password_hash(raw_password, method="scrypt")

    def check_password(self, raw_password: str) -> bool:
        return bool(check_password_hash(self.password, raw_password))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tool_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Generation(db.Model):
    """One AI generation: prompt, result, tool. saved_at set when user saves to Saved Results."""
    __tablename__ = "generation"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    tool_name = db.Column(db.String(80), nullable=False, index=True)
    prompt = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    saved_at = db.Column(db.DateTime, nullable=True)  # when not null, appears in Saved Results

    user = db.relationship("User", backref=db.backref("generations", lazy="dynamic"))


class BlogCategory(db.Model):
    """Blog category for grouping articles."""
    __tablename__ = "blog_category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True, index=True)

    articles = db.relationship("BlogArticle", backref="category", lazy="dynamic")


class BlogArticle(db.Model):
    """SEO blog article: title, content, author, category, publish/draft, SEO fields."""
    __tablename__ = "blog_article"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    excerpt = db.Column(db.String(500), nullable=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey("blog_category.id"), nullable=True, index=True)
    status = db.Column(db.String(20), nullable=False, default="draft")  # draft | published
    published_at = db.Column(db.DateTime, nullable=True)
    meta_title = db.Column(db.String(255), nullable=True)
    meta_description = db.Column(db.String(500), nullable=True)
    meta_keywords = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    author = db.relationship("User", backref=db.backref("blog_articles", lazy="dynamic"))
