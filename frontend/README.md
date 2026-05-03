# Frontend (SaaS Boilerplate)

Structure for UI assets and templates.

- **layout/** – Base layout (`templates/base.html`). **partials/** for header, sidebar, footer.
- **pages/** – Full-page templates: **auth/**, **dashboard/**, **tools/**, **pricing/** (see each README).
- **features/** – **auth**, **billing**, **credits**, **ai-tools** (see each README).
- **components/** – Reusable UI pieces (buttons, cards, forms).
- **hooks/** – Placeholder for frontend hooks (e.g. React/Vue).
- **utils/** – JS helpers; current: `static/js/main.js`.
- **styles/** – CSS; current: `static/css/style.css`.
- **static/** – Canonical static root when migrating (see README inside).
- **i18n/** – Translations: project root `translations/` (Babel).
- **branding/** – Logo and theme; project root `branding/`.

Templates and static are under project root `templates/` and `static/` so Flask works unchanged. To migrate: set `template_folder="frontend/templates"`, `static_folder="frontend/static"`, and move files.
