# How to Change Branding

To rebrand the SaaS boilerplate for a new product:

1. **App name**
   - Edit `branding/app-name.txt` with your product name.
   - Search the codebase for "AI Multi Tools" and replace with your name (or use a template variable that reads from `branding/app-name.txt` or config).

2. **Theme colors**
   - Edit `branding/theme.json`: `primary`, `secondary`, `accent`, `sidebar_bg`, `sidebar_bg_dark`.
   - In `static/css/style.css` (or `frontend/static/css/`), either:
     - Use CSS variables that you set from this file (e.g. via a build step or inline in base template), or
     - Replace the hex values for primary, header, and sidebar with the values from `theme.json`.

3. **Logo**
   - Place your logo in `branding/` (e.g. `logo.png`, `favicon.ico`).
   - In the base layout template (`templates/base.html` or `frontend/templates/layout/base.html`), update the `<img>` or SVG source to point to your logo (e.g. `{{ url_for('static', filename='branding/logo.png') }}` if you serve branding from static).

4. **Meta and SEO**
   - Update default `og:title`, `og:description`, and meta tags in the base template and in any view that passes `seo` to templates (e.g. dashboard, tool pages).

5. **Footer**
   - Change the footer text (e.g. "© 2024 AI Multi Tools") in the base template or the block that provides `footer_text`.

After changes, run the app and check the landing page, dashboard, and auth pages for consistent branding.
