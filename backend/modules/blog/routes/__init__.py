"""
Blog module: public blog homepage and article pages.
"""
from flask import Blueprint, render_template, abort
from models import BlogArticle, BlogCategory

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/blog")
def index():
    articles = (
        BlogArticle.query.filter_by(status="published")
        .order_by(BlogArticle.published_at.desc())
        .all()
    )
    return render_template(
        "blog/index.html",
        articles=articles,
        seo={
            "title": "Blog | MindixoAI",
            "description": "Tips, guides, and updates about AI content creation and our tools.",
            "keywords": "AI blog, content creation, AI tools",
        },
    )


@blog_bp.route("/blog/<slug>")
def article(slug):
    article = BlogArticle.query.filter_by(slug=slug, status="published").first_or_404()
    # Related: same category first, then others, exclude current, limit 4
    related = []
    if article.category_id:
        related = (
            BlogArticle.query.filter(
                BlogArticle.category_id == article.category_id,
                BlogArticle.id != article.id,
                BlogArticle.status == "published",
            )
            .order_by(BlogArticle.published_at.desc())
            .limit(4)
            .all()
        )
    if len(related) < 4:
        exclude_ids = [r.id for r in related] + [article.id]
        extra = (
            BlogArticle.query.filter(
                BlogArticle.status == "published",
                ~BlogArticle.id.in_(exclude_ids),
            )
            .order_by(BlogArticle.published_at.desc())
            .limit(4 - len(related))
            .all()
        )
        related = list(related) + list(extra)
    return render_template(
        "blog/article.html",
        article=article,
        related=related[:4],
        seo={
            "title": article.meta_title or article.title,
            "description": article.meta_description or article.excerpt or "",
            "keywords": article.meta_keywords or "",
        },
    )
