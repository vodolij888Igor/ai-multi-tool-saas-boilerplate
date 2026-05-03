# Deployment

## Checklist

1. **Environment**
   - Set `SECRET_KEY` to a strong random value.
   - Set `OPENAI_API_KEY` and, if using payments, `STRIPE_SECRET_KEY`.
   - For production DB, set `DATABASE_URL` (e.g. PostgreSQL).

2. **Production server**
   - Do not run with `debug=True`. Use a WSGI server (e.g. Gunicorn, Waitress):
     ```bash
     gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
     ```
   - Or: `waitress-serve --call "app:create_app"` (Windows-friendly).

3. **Static files**
   - For high traffic, serve `/static` via Nginx or CDN.

4. **Database**
   - Run migrations if using Alembic. For SQLite, `db.create_all()` runs on startup; for PostgreSQL/MySQL, ensure schema is applied.

5. **HTTPS**
   - Use a reverse proxy (Nginx, Caddy) with SSL. Set `SESSION_COOKIE_SECURE=True` and `PREFERRED_URL_SCHEME=https` in config if needed.

6. **Stripe**
   - Use live keys in production; configure webhooks if you use subscription lifecycle events.
