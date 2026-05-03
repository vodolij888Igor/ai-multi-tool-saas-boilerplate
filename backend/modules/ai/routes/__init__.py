"""
AI module: dashboard, tool page, generate API.
"""
from flask import Blueprint, render_template, request, jsonify, session, url_for
from flask_login import login_required, current_user
from models import User, Generation
from extensions import db
from tools_config import (
    get_tools_by_category,
    get_tool_by_name,
    get_system_prompt,
    get_tier_for_plan,
    tool_allowed_for_tier,
)
from backend.utils.locale import get_locale, get_language_for_prompt
from backend.services.openai_service import generate as openai_generate
from backend.modules.credits.services import can_use_tools as credits_can_use, deduct_credits as credits_deduct

ai_bp = Blueprint("ai", __name__)


def _current_user_plan():
    """Saved plan for current user (Starter, Pro, Full). Used for normal users."""
    if not current_user.is_authenticated:
        return "Starter"
    plan = getattr(current_user, "plan_name", None)
    if plan in ("Starter", "Pro", "Full"):
        return plan
    return "Pro" if getattr(current_user, "is_subscription_active", False) else "Starter"


def _plan_for_access():
    """Plan used for access control (tool page, generate). Admin always gets Full."""
    if current_user.is_authenticated and getattr(current_user, "is_admin", False):
        return "Full"
    return _current_user_plan()


def _plan_for_display():
    """Plan used for UI (dashboard tool list). Admin uses preview tier or Full."""
    if current_user.is_authenticated and getattr(current_user, "is_admin", False):
        preview = session.get("tier_preview")
        return preview if preview in ("Starter", "Pro", "Full") else "Full"
    return _current_user_plan()


@ai_bp.route("/")
def dashboard():
    locale = get_locale()
    tier = get_tier_for_plan(_plan_for_display())
    business_tools = get_tools_by_category("Professional", locale, tier=tier)
    personal_creative_tools = get_tools_by_category("Personal", locale, tier=tier)
    all_tools = business_tools + personal_creative_tools

    recent_tool_names = session.get("recent_tools", [])
    recent_tools = []
    for name in recent_tool_names[:4]:
        t = get_tool_by_name(name, locale)
        if t:
            recent_tools.append(t)
    featured_tools = (business_tools[:2] + personal_creative_tools[:1]) if not recent_tools else []
    if recent_tools:
        display_tools = recent_tools
        section_title_key = "Recently Used"
    else:
        display_tools = featured_tools if featured_tools else business_tools[:3]
        section_title_key = "Featured Tools"

    all_tools_for_search = [
        {
            "name": t["name"],
            "url": url_for("ai.tool_page", tool_name=t["tool_name"]),
            "icon": t["icon"],
            "tool_name": t["tool_name"],
        }
        for t in all_tools
    ]

    seo = {
        "title": "MindixoAI - Dashboard",
        "description": "MindixoAI dashboard. Create professional content in seconds.",
        "keywords": "AI tools, content generator",
    }

    return render_template(
        "index.html",
        business_tools=business_tools,
        personal_creative_tools=personal_creative_tools,
        recent_tools=recent_tools,
        featured_tools=featured_tools,
        display_tools=display_tools,
        section_title_key=section_title_key,
        all_tools_for_search=all_tools_for_search,
        seo=seo,
    )


@ai_bp.route("/tool/<tool_name>")
def tool_page(tool_name):
    locale = get_locale()
    tier = get_tier_for_plan(_plan_for_access())
    if not tool_allowed_for_tier(tool_name, tier):
        return redirect(url_for("billing.pricing"))
    tool = get_tool_by_name(tool_name, locale)

    if tool:
        recent = list(session.get("recent_tools", []))
        if tool_name in recent:
            recent.remove(tool_name)
        recent.insert(0, tool_name)
        session["recent_tools"] = recent[:4]

    seo = {
        "title": tool.get("seo_title", tool.get("name", "AI Tool")) if tool else "AI Tool",
        "description": tool.get("meta_description", tool.get("description", "")) if tool else "",
        "keywords": tool.get("keywords", "") if tool else "",
    }
    return render_template("tool.html", tool_name=tool_name, tool=tool, seo=seo)


@ai_bp.route("/api/generate", methods=["POST"])
@login_required
def generate_content():
    user = User.query.get(current_user.id)
    allowed, err = credits_can_use(user)
    if not allowed:
        return jsonify({"error": err}), 402 if "run out" in (err or "") else 403

    tier = get_tier_for_plan(_plan_for_access())
    data = request.json
    user_input = data.get("prompt", "")
    tool_name = data.get("tool_name", "general")
    if not tool_allowed_for_tier(tool_name, tier):
        return jsonify({"error": "This tool is not available in your plan."}), 403
    system_prompt = get_system_prompt(tool_name)
    full_language_name = get_language_for_prompt()
    user_message = f"Answer the following request strictly in {full_language_name}.\n\n{user_input}"

    content, err = openai_generate(system_prompt, user_message)
    if err:
        return jsonify({"error": err}), 500

    user = User.query.get(current_user.id)
    credits_deduct(user, 1)
    gen = Generation(
        user_id=current_user.id,
        tool_name=tool_name,
        prompt=user_input,
        result=content,
    )
    db.session.add(gen)
    db.session.commit()
    return jsonify({"result": content, "generation_id": gen.id})
