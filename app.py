"""
SaaS Boilerplate entry point. Wires config, DB, Babel, LoginManager, and feature blueprints.
"""
import os
import xml.etree.ElementTree as ET
from datetime import date
from flask import Flask, session, request, redirect, url_for, render_template, abort, make_response
from flask_login import LoginManager, current_user
from flask_babel import Babel, gettext as flask_babel_gettext
from dotenv import load_dotenv

load_dotenv()

from extensions import db

# Optional: use centralized config
try:
    from config.app import SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS, MAX_CONTENT_LENGTH
    from config.constants import SUPPORTED_LANGUAGES
except ImportError:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-123")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SUPPORTED_LANGUAGES = ["en", "uk", "ua", "es", "ru", "de", "fr"]

# Single source for locale (used by context_processor and set_language)
from backend.utils.locale import get_locale


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instance")
    os.makedirs(instance_path, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or (
        "sqlite:///" + os.path.join(instance_path, "users.db")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    if MAX_CONTENT_LENGTH:
        app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    db.init_app(app)
    app.config.setdefault("BABEL_DEFAULT_LOCALE", "en")
    app.config.setdefault("BABEL_DEFAULT_TIMEZONE", "UTC")
    # Use absolute path so Babel always loads from this project's translations/ regardless of CWD or app.root_path
    _project_root = os.path.dirname(os.path.abspath(__file__))
    _translations_abs = os.path.join(_project_root, "translations")
    app.config.setdefault("BABEL_TRANSLATION_DIRECTORIES", _translations_abs)
    Babel(app, locale_selector=get_locale)
    # Ensure Jinja always resolves _() / gettext() to Flask-Babel (avoids missing translations).
    app.add_template_global(flask_babel_gettext, "_")
    app.add_template_global(flask_babel_gettext, "gettext")
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) if user_id else None

    @app.context_processor
    def inject_globals():
        from tools_config import get_tools_by_category, get_tier_for_plan
        is_admin = current_user.is_authenticated and getattr(current_user, "is_admin", False)
        user_package = "Starter"
        if current_user.is_authenticated:
            plan = getattr(current_user, "plan_name", None)
            if plan in ("Starter", "Pro", "Full"):
                user_package = plan
            else:
                user_package = "Pro" if getattr(current_user, "is_subscription_active", False) else "Starter"
        # Owner/admin: display uses preview tier or Full; real access is always full (handled in AI routes).
        if is_admin:
            tier_preview = session.get("tier_preview")
            effective_plan = tier_preview if tier_preview in ("Starter", "Pro", "Full") else "Full"
        else:
            effective_plan = user_package
        current_tier = get_tier_for_plan(effective_plan)
        sidebar_professional_tools = get_tools_by_category("Professional", get_locale(), tier=current_tier)
        sidebar_creative_tools = get_tools_by_category("Personal", get_locale(), tier=current_tier)
        return {
            "get_locale": get_locale,
            "seo": {"title": "MindixoAI", "description": "Best AI Tools"},
            "t": type("FakeTranslate", (), {"__getattr__": lambda s, n: n})(),
            "l": type("FakeTranslate", (), {"__getattr__": lambda s, n: n})(),
            "sidebar_professional_tools": sidebar_professional_tools,
            "sidebar_creative_tools": sidebar_creative_tools,
            "user_package": user_package,
            "effective_plan": effective_plan,
            "is_admin": is_admin,
            "tier_preview": session.get("tier_preview"),
            "current_year": date.today().year,
        }

    # Language switcher: store in session and cookie (browser language never used)
    @app.route("/set_language/<lang_code>")
    def set_language(lang_code):
        valid = list(SUPPORTED_LANGUAGES) if SUPPORTED_LANGUAGES else ["en", "uk", "ua", "es", "ru", "de", "fr"]
        lang_code = lang_code if lang_code in valid else "en"
        session["language"] = lang_code
        session["locale"] = "uk" if lang_code in ("ua", "uk") else lang_code
        resp = redirect(request.referrer or url_for("ai.dashboard"))
        resp.set_cookie("preferred_lang", lang_code, max_age=31536000, samesite="Lax")
        return resp

    # Blueprints: ai must be registered BEFORE main so "/" is handled by ai.dashboard (Babel + get_locale).
    # main_bp.index would otherwise serve "/" and use get_translations() which defaulted to Ukrainian.
    from backend.modules.auth.routes import auth_bp
    from backend.modules.billing.routes import billing_bp
    from backend.modules.admin.routes import admin_bp
    from backend.modules.users.routes import users_bp
    from backend.modules.history.routes import history_bp
    from backend.modules.blog.routes import blog_bp
    from backend.modules.ai.routes import ai_bp
    from routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(billing_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(ai_bp)   # before main so / and /tool/<name> are ai (Babel-only, no Ukrainian fallback)
    app.register_blueprint(main_bp)

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("403.html"), 403

    @app.route("/robots.txt")
    def robots_txt():
        base = request.url_root.rstrip("/")
        body = f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n"
        resp = make_response(body)
        resp.mimetype = "text/plain"
        return resp

    @app.route("/debug-translations")
    def debug_translations():
        """Diagnostic: show which translation dir is loaded and sample strings. Use ?debug=1 to enable."""
        if request.args.get("debug") != "1":
            return "Add ?debug=1 to see translation diagnostics.", 404
        from flask import jsonify
        from flask_babel import get_babel, get_translations
        babel = get_babel()
        loc = str(get_locale())
        trans = get_translations()
        def _t(s):
            return trans.ugettext(s) if hasattr(trans, "ugettext") else trans.gettext(s)
        samples = {
            "Pricing": _t("Pricing"),
            "Get started free": _t("Get started free"),
            "Pricing Plans": _t("Pricing Plans"),
            "Email": _t("Email"),
        }
        return jsonify({
            "app_root_path": app.root_path,
            "babel_translation_directories": getattr(babel, "translation_directories", None),
            "current_locale": loc,
            "sample_translations": samples,
            "translations_dir_exists": os.path.isdir(_translations_abs),
            "mo_uk_exists": os.path.isfile(os.path.join(_translations_abs, "uk", "LC_MESSAGES", "messages.mo")),
        })

    @app.route("/sitemap.xml")
    def sitemap_xml():
        from models import BlogArticle
        base = request.url_root.rstrip("/")
        urlset = ET.Element("urlset")
        urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        for path, priority, changefreq in [
            ("/", "1.0", "daily"),
            ("/blog", "0.9", "daily"),
            ("/pricing", "0.8", "weekly"),
            ("/login", "0.5", "monthly"),
            ("/register", "0.8", "monthly"),
        ]:
            url_elem = ET.SubElement(urlset, "url")
            ET.SubElement(url_elem, "loc").text = base + path
            ET.SubElement(url_elem, "priority").text = priority
            ET.SubElement(url_elem, "changefreq").text = changefreq
        for article in BlogArticle.query.filter_by(status="published").order_by(BlogArticle.updated_at.desc()).all():
            url_elem = ET.SubElement(urlset, "url")
            ET.SubElement(url_elem, "loc").text = f"{base}/blog/{article.slug}"
            ET.SubElement(url_elem, "priority").text = "0.7"
            ET.SubElement(url_elem, "changefreq").text = "weekly"
            lastmod = (article.updated_at or article.published_at or article.created_at)
            if lastmod:
                ET.SubElement(url_elem, "lastmod").text = lastmod.strftime("%Y-%m-%d")
        xml_str = ET.tostring(urlset, encoding="unicode", method="xml")
        resp = make_response('<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str)
        resp.mimetype = "application/xml"
        resp.headers["Content-Type"] = "application/xml; charset=utf-8"
        return resp

    with app.app_context():
        db.create_all()
        try:
            from sqlalchemy import text
            with db.engine.connect() as conn:
                conn.execute(text("ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT 0 NOT NULL"))
                conn.commit()
        except Exception:
            pass
        try:
            with db.engine.connect() as conn:
                conn.execute(text("ALTER TABLE user ADD COLUMN stripe_customer_id VARCHAR(120)"))
                conn.commit()
        except Exception:
            pass

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        from models import User
        u = User.query.filter_by(email="vodolij888@gmail.com").first()
        if u and not getattr(u, "is_admin", False):
            u.is_admin = True
            from extensions import db
            db.session.commit()
    app.run(debug=True)
