# Customization

## Branding

- **App name**: Edit `branding/app-name.txt`.
- **Colors and theme**: Edit `branding/theme.json` (primary, secondary, accent, sidebar colors). The app CSS can read these or you can map them in your styles.
- **Logo**: Replace files in `branding/` (e.g. `logo.png`) and update `templates/base.html` or `frontend/templates/layout/base.html` to reference them.

See **docs/how-to-change-branding.md** for step-by-step rebranding.

## Adding a new AI tool

See **docs/how-to-add-tool.md** for the modular tool structure (config, prompt, handler) and how to register a new tool.

## Feature flags

In `.env` you can enable optional features:

- `FEATURE_EMAIL=true` – enable transactional emails (when implemented).
- `FEATURE_ANALYTICS=true` – enable analytics (when implemented).

## Languages

Supported locales are defined in `config/constants.py` (`SUPPORTED_LANGUAGES`). To add a new language, add the code there, add a corresponding folder under `translations/`, and run `pybabel compile -d translations`.
