# AI Content Generator - Професійна SaaS Платформа

Професійна SaaS-платформа для генерації контенту за допомогою штучного інтелекту на базі Flask та OpenAI.

## Особливості

- 🌍 Мультимовність (Українська 🇺🇦, Англійська 🇺🇸, Іспанська 🇪🇸)
- 🔍 SEO-оптимізація з унікальними title та meta description для кожної сторінки
- 🗺️ Автоматична генерація sitemap.xml для пошукових систем
- 🔗 Унікальні URL для кожного інструменту (/uk/tool/finance)
- 📊 Блок "Популярні запити" для покращення SEO
- 🔐 Система реєстрації та авторизації користувачів
- 💾 SQLite база даних для зберігання користувачів
- 🎯 Підтримка 12 ніш (фінанси, KDP, бізнес, маркетинг, технології, здоров'я, освіта, подорожі, їжа, фітнес, краса, нерухомість)
- 🌙 Темна/світла тема
- 📱 Адаптивний дизайн на Bootstrap 5
- 🤖 Інтеграція з OpenAI GPT-4o-mini з автоматичним вибором мови відповіді
- 🔄 Підтримка проксі-сервера для PythonAnywhere
- ⚡ Швидка генерація контенту

## Встановлення

1. Клонуйте репозиторій або завантажте файли

2. Створіть віртуальне середовище:
```bash
python -m venv venv
```

3. Активуйте віртуальне середовище:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Встановіть залежності:
```bash
pip install -r requirements.txt
```

5. Створіть файл `.env` на основі `.env.example`:
```bash
cp .env.example .env
```

6. Налаштуйте `.env` файл:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
SECRET_KEY=your_secret_key_here
USE_PROXY=False
PROXY_URL=http://proxy.server:port
```

## Запуск

```bash
python app.py
```

Додаток буде доступний за адресою: `http://localhost:5000`

## Структура проекту (SaaS Boilerplate)

Проект організовано як модульний SaaS Boilerplate для швидкого запуску нових продуктів (зміна брендингу, інструментів, промптів, теми).

```
AI_Multi_Tool/
├── app.py                    # Точка входу: створення додатку, реєстрація blueprints
├── config/                   # Централізована конфігурація
│   ├── app.py, ai.py, payments.py, env.py, constants.py, feature_flags.py
├── backend/                  # Бекенд: ядро, модулі, сервіси
│   ├── core/                 # database, security
│   ├── models/               # Re-export моделей (User, Project)
│   ├── services/             # openai, payments (Stripe), email (stub)
│   ├── modules/              # auth, users, billing, admin, ai, credits (stub)
│   └── utils/                # locale
├── modules/ai-tools/         # Модульні AI-інструменти
│   ├── tool-template/        # Шаблон для нового інструмента (config + prompt)
│   └── README.md
├── frontend/                 # Структура UI (layout, pages, features, components, styles, i18n, branding)
├── branding/                 # Брендинг: app-name, theme.json, logo
├── docs/                     # Документація
│   ├── installation.md, customization.md, deployment.md
│   ├── how-to-add-tool.md, how-to-change-branding.md
├── scripts/                  # setup.py, migrate.py, seed.py
├── routes/                   # main_bp (sitemap, set_language, legacy routes)
├── templates/                # Jinja2 шаблони (base, auth, dashboard, pricing, admin)
├── static/                   # CSS, JS
├── translations/             # Babel .po (en, uk, es, ru, de, fr)
├── models.py, extensions.py, tools_config.py  # Моделі, DB, конфіг інструментів
└── requirements.txt, .env.example, babel.cfg
```

Детальніше: **docs/installation.md**, **docs/how-to-add-tool.md**, **docs/how-to-change-branding.md**, **docs/deployment.md**.

## Використання

1. Зареєструйтеся або увійдіть в систему
2. Відкрийте головну сторінку
3. Оберіть нішу з доступних 12 опцій
4. Виберіть тип контенту (стаття, блог, соціальні мережі, email)
5. Введіть опис того, що потрібно створити
6. Натисніть "Згенерувати контент"
7. Скопіюйте згенерований контент за допомогою кнопки "Копіювати"

## Авторизація

Додаток використовує систему авторизації з Flask-Login та SQLite базу даних:
- Реєстрація доступна за адресою `/register`
- Вхід доступний за адресою `/login`
- Вихід доступний за адресою `/logout`
- Генерація контенту доступна тільки для авторизованих користувачів

## Мультимовність

Додаток підтримує три мови:
- 🇺🇦 Українська (за замовчуванням)
- 🇺🇸 English
- 🇪🇸 Español

### Як працює мультимовність:

1. **Перемикач мов**: Знаходиться у верхній навігаційній панелі (Navbar)
2. **Автоматичний вибір мови**: OpenAI автоматично генерує контент тією мовою, яку ви обрали
3. **Переклади ніш**: Всі 12 ніш перекладені на всі три мови
4. **Збереження вибору**: Ваш вибір мови зберігається в сесії браузера

### Технічні деталі:

- Використовується Flask-Babel для локалізації
- Мова зберігається в сесії Flask
- OpenAI отримує інструкцію відповідати обраною мовою
- Всі інтерфейсні елементи перекладені

## SEO-оптимізація

Додаток включає повну SEO-оптимізацію:

### Унікальні мета-теги
- Кожна сторінка має унікальний `<title>` та `<meta description>`
- Мета-теги адаптовані для кожної мови (UA, EN, ES)
- Кожен інструмент має свої унікальні SEO-дані

### Sitemap.xml
- Автоматична генерація sitemap.xml за адресою `/sitemap.xml`
- Включає всі сторінки для всіх мов
- Підтримка hreflang для мультимовних сторінок

### Унікальні URL
- Кожен інструмент має унікальний URL: `/{language}/tool/{niche_id}`
- Приклад: `/uk/tool/finance`, `/en/tool/business`, `/es/tool/marketing`
- Покращує індексацію пошуковими системами

### Популярні запити
- Блок "Популярні запити" на головній сторінці та сторінках інструментів
- Додає ключові слова для покращення SEO
- Адаптований для кожної мови

## Налаштування для PythonAnywhere

Якщо ви використовуєте PythonAnywhere та потрібен проксі:

1. Встановіть `USE_PROXY=True` в `.env`
2. Вкажіть `PROXY_URL` з адресою вашого проксі-сервера

## Ліцензія

MIT License

