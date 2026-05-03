# Legacy route modules (not loaded)

These blueprints are **not registered** in `app.py`. They have been superseded by backend modules:

- `auth.py` → `backend.modules.auth.routes` (auth_bp)
- `ai_generation.py` → `backend.modules.ai.routes` (ai_bp)
- `dashboard.py` → never registered; uses `UserProject` model which does not exist (models have `Project`)

Kept here for reference only. Safe to delete once you are sure no external references remain.
