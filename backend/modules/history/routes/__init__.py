"""
History module: generation history list, saved results list, save/unsave, view, delete, download.
"""
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from flask_login import login_required, current_user
from extensions import db
from models import Generation
from tools_config import get_tool_by_name
from backend.utils.locale import get_locale

history_bp = Blueprint("history", __name__)


def _get_tool_display_name(tool_name, locale="en"):
    t = get_tool_by_name(tool_name, locale)
    return t.get("name", tool_name.replace("-", " ").title()) if t else tool_name.replace("-", " ").title()


@history_bp.route("/history")
@login_required
def history_list():
    items = (
        Generation.query.filter_by(user_id=current_user.id)
        .order_by(Generation.created_at.desc())
        .limit(200)
        .all()
    )
    locale = get_locale()
    list_ = [
        {
            "id": g.id,
            "tool_name": g.tool_name,
            "tool_display_name": _get_tool_display_name(g.tool_name, locale),
            "prompt": (g.prompt[:200] + "…") if len(g.prompt or "") > 200 else (g.prompt or ""),
            "result_preview": (g.result[:150] + "…") if len(g.result or "") > 150 else (g.result or ""),
            "created_at": g.created_at,
            "saved_at": g.saved_at,
        }
        for g in items
    ]
    return render_template("history/list.html", items=list_)


@history_bp.route("/saved")
@login_required
def saved_list():
    items = (
        Generation.query.filter_by(user_id=current_user.id)
        .filter(Generation.saved_at.isnot(None))
        .order_by(Generation.saved_at.desc())
        .limit(200)
        .all()
    )
    locale = get_locale()
    list_ = [
        {
            "id": g.id,
            "tool_name": g.tool_name,
            "tool_display_name": _get_tool_display_name(g.tool_name, locale),
            "prompt": (g.prompt[:200] + "…") if len(g.prompt or "") > 200 else (g.prompt or ""),
            "result_preview": (g.result[:150] + "…") if len(g.result or "") > 150 else (g.result or ""),
            "created_at": g.created_at,
            "saved_at": g.saved_at,
        }
        for g in items
    ]
    return render_template("saved/list.html", items=list_)


@history_bp.route("/history/<int:gen_id>")
@login_required
def history_view(gen_id):
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).first_or_404()
    locale = get_locale()
    return render_template(
        "history/view.html",
        item={
            "id": g.id,
            "tool_name": g.tool_name,
            "tool_display_name": _get_tool_display_name(g.tool_name, locale),
            "prompt": g.prompt,
            "result": g.result,
            "created_at": g.created_at,
            "saved_at": g.saved_at,
        },
    )


@history_bp.route("/saved/<int:gen_id>")
@login_required
def saved_view(gen_id):
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).filter(Generation.saved_at.isnot(None)).first_or_404()
    locale = get_locale()
    return render_template(
        "saved/view.html",
        item={
            "id": g.id,
            "tool_name": g.tool_name,
            "tool_display_name": _get_tool_display_name(g.tool_name, locale),
            "prompt": g.prompt,
            "result": g.result,
            "created_at": g.created_at,
            "saved_at": g.saved_at,
        },
    )


@history_bp.route("/history/<int:gen_id>/save", methods=["POST"])
@login_required
def save_result(gen_id):
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).first_or_404()
    if g.saved_at:
        flash("This result is already saved.", "info")
    else:
        g.saved_at = datetime.utcnow()
        db.session.commit()
        flash("Result saved to Saved Results.", "success")
    return redirect(request.referrer or url_for("history.history_list"))


@history_bp.route("/saved/<int:gen_id>/unsave", methods=["POST"])
@login_required
def unsave_result(gen_id):
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).first_or_404()
    g.saved_at = None
    db.session.commit()
    flash("Removed from Saved Results.", "info")
    return redirect(url_for("history.saved_list"))


@history_bp.route("/history/<int:gen_id>/delete", methods=["POST"])
@login_required
def delete_history(gen_id):
    """Delete a history record. Only the owner can delete (enforced by filter)."""
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).first_or_404()
    db.session.delete(g)
    db.session.commit()
    flash("History item deleted.", "info")
    return redirect(url_for("history.history_list"))


@history_bp.route("/history/<int:gen_id>/download")
@login_required
def download_result(gen_id):
    """Download result as .txt or .md. Only owner can download (enforced by filter)."""
    g = Generation.query.filter_by(id=gen_id, user_id=current_user.id).first_or_404()
    format_ = (request.args.get("format") or "txt").strip().lower()
    if format_ not in ("txt", "md"):
        format_ = "txt"
    filename = f"generation-{g.id}.{format_}"
    if format_ == "txt":
        body = g.result or ""
        mimetype = "text/plain"
    else:
        # Markdown: tool name, prompt, result
        tool_display = _get_tool_display_name(g.tool_name, get_locale())
        body = f"# {tool_display}\n\n## Prompt\n\n{g.prompt or ''}\n\n## Result\n\n{g.result or ''}\n"
        mimetype = "text/markdown"
    response = Response(body, mimetype=mimetype)
    response.headers["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
