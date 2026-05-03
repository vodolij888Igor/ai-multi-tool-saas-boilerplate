# Installation

## Requirements

- Python 3.10+
- pip

## Steps

1. **Clone and enter the project**
   ```bash
   cd AI_Multi_Tool
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment**
   - Copy `.env.example` to `.env` (or create `.env` with required variables).
   - Set at least: `SECRET_KEY`, `OPENAI_API_KEY`. For payments: `STRIPE_SECRET_KEY`.

5. **Run**
   ```bash
   python app.py
   ```
   Open http://127.0.0.1:5000

6. **Optional: compile translations**
   ```bash
   pybabel compile -d translations
   ```

## Database

The app uses SQLite by default. The database file is created at `instance/users.db`. For production, set `DATABASE_URL` to a PostgreSQL or MySQL connection string and run migrations.
