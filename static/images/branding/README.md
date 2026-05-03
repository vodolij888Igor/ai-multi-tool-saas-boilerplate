# Branding assets

- **`logo-source.png`** — **current production logo** (navbar, hero, favicon). Use a **transparent-background PNG** so it blends on light and dark themes. Served via `url_for('static', filename='images/branding/logo-source.png')`.
- **`logo.svg` / `logo-dark.svg`** — optional vector assets (not used when PNG is the active logo).

Templates use:

```jinja
{{ url_for('static', filename='images/branding/logo-source.png') }}
```
