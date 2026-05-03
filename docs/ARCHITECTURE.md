# Project Architecture — Current State & Refactoring Plan

## 1. Current Structure (High Level)

```
AI_Multi_Tool/
├── app.py                      # Entry point; registers blueprints, set_language, 403
├── config/                     # Canonical config (env, constants, app, ai, payments, feature_flags)
├── config.py                   # LEGACY: old single-file config (Config class)
├── backend/
│   ├── core/                   # database (re-export db), security
│   ├── models/                 # re-export User, Project from root models
│   ├── services/               # openai, payments (Stripe), email (stub)
│   ├── utils/                  # locale (get_locale, get_language_for_prompt)
│   └── modules/
│       ├── auth/               # register, login, logout
│       ├── users/              # settings (password, plan, portal link)
│       ├── billing/            # pricing, checkout, success, portal session
│       ├── admin/              # admin dashboard, user credits
│       ├── ai/                 # dashboard (/), tool page, POST /api/generate
│       └── credits/            # stub (no routes)
├── routes/
│   ├── main.py                 # USED: main_bp — sitemap, /creative/<id>, /<lang>/tool/<id>; also defines / and /tool (overridden by ai_bp)
│   ├── auth.py                 # DEAD: superseded by backend.modules.auth
│   ├── ai_generation.py        # DEAD: superseded by backend.modules.ai
│   └── dashboard.py            # DEAD: never registered
├── models.py                   # User, Project
├── extensions.py               # Flask-SQLAlchemy db
├── tools_config.py             # TOOL_SYSTEM_PROMPTS, TOOLS_CONFIG; get_tools_by_category, get_tool_by_name, get_system_prompt
├── templates/, static/, translations/
├── modules/ai-tools/           # tool-template, README
├── frontend/                   # READMEs only (layout, pages, features, components, styles, i18n, branding)
├── branding/, docs/, scripts/
└── .env, .env.example, requirements.txt, babel.cfg
```

**Blueprint registration order:** auth → billing → admin → users → main → **ai** (last). So `/` and `/tool/<tool_name>` are served by **ai**, not main. main_bp still provides `/sitemap.xml`, `/creative/<niche_id>`, `/<language>/tool/<niche_id>`, and a duplicate `/set_language/<language>` (app’s route wins).

---

## 2. Weak Points

| # | Issue | Impact |
|---|--------|--------|
| 1 | **Dead code** | `routes/auth.py`, `routes/ai_generation.py`, `routes/dashboard.py` are never imported; they add noise and confusion. |
| 2 | **Duplicate set_language** | Both `app.py` and `routes/main.py` define `/set_language/...`; only app’s is used. main’s version is dead. |
| 3 | **Duplicate get_locale** | Defined in `app.py` and `routes/main.py`; backend has `backend.utils.locale.get_locale`. Inconsistent. |
| 4 | **Legacy config.py** | Root `config.py` exists alongside `config/` package. Only `config` package (and Config in config/__init__.py) is used by app and main. |
| 5 | **Missing get_creative_tools** | `main.creative_tool_page` calls `get_creative_tools()` which is **not defined** → NameError when visiting `/creative/<niche_id>`. |
| 6 | **Two sources of tool data** | `tools_config.py` (used by ai_bp) vs main’s inline `get_ai_tools()` / `get_personal_creative_tools()`. Duplication and possible drift. |
| 7 | **Mixed layering** | Backend modules import from root (`extensions`, `models`) instead of `backend.core.database` and `backend.models`. |
| 8 | **Frontend only on paper** | `frontend/` is READMEs; actual templates and static remain at root. No single “frontend” asset root. |

---

## 3. Refactoring Plan (No Breaking Changes)

**Step 1 — Fix runtime bug**  
- Define `get_creative_tools` in `routes/main.py` (e.g. return `get_personal_creative_tools()`) so `/creative/<niche_id>` works.

**Step 2 — Remove dead code**  
- Delete or move to `_legacy/`: `routes/auth.py`, `routes/ai_generation.py`, `routes/dashboard.py`. Confirm no imports reference them.

**Step 3 — Single source for locale**  
- Use `backend.utils.locale.get_locale` in `app.py` (context_processor + set_language). Remove duplicate `get_locale` from app.py.
- Remove `/set_language/<language>` from `routes/main.py` (keep only on app).

**Step 4 — Deprecate root config.py**  
- Add a short comment at top of `config.py`: “Deprecated; use config package.” Optionally make it re-export from `config.app` for any remaining references.

**Step 5 — Optional: main_bp uses tools_config**  
- (Later) Refactor main_bp to use `tools_config.get_tools_by_category` / `get_tool_by_name` instead of inline get_ai_tools / get_personal_creative_tools to have one source of truth. Can be a separate PR.

**Step 6 — Optional: backend imports**  
- (Later) Switch backend modules to `from backend.core.database import db` and `from backend.models import User` where applicable; then ensure no circular imports.

---

## 4. Execution Order

Execute in order: **Step 1** (bugfix) → **Step 2** (dead code) → **Step 3** (locale) → **Step 4** (config.py). Steps 5–6 can follow in a later pass.
