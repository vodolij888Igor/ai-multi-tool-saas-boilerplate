# -*- coding: utf-8 -*-
"""Add missing translation entries to ru, es, de, fr .po files."""
import os
import re

BASE = os.path.join(os.path.dirname(__file__), '..', 'translations')

def parse_po(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    entries = {}
    for block in content.split('\n\n'):
        msgid_m = re.search(r'msgid\s+"(.*?)"(?=\nmsgstr|\Z)', block, re.DOTALL)
        msgstr_m = re.search(r'msgstr\s+"(.*?)"(?=\n\n#|\nmsgid|\Z)', block, re.DOTALL)
        if msgid_m and msgstr_m:
            mid = msgid_m.group(1).replace('\\n', '\n').strip()
            mst = msgstr_m.group(1).replace('\\n', '\n').strip()
            if mid:
                entries[mid] = mst
    return entries

def read_po_blocks(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Keep header (first block with empty msgid)
    parts = content.split('\n\n')
    header = parts[0] + '\n\n'
    rest = '\n\n'.join(parts[1:])
    return header, rest

def append_entries(path, entries_text):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.endswith('\n'):
        content += '\n'
    content = content.rstrip()
    content += '\n\n' + entries_text.strip() + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Translations for missing keys: (msgid -> {lang: msgstr})
# Keys that en has but ru/es/de/fr may lack (from check_po output)
MISSING_TRANSLATIONS = {
    "Get started": {
        "ru": "Начать",
        "es": "Empezar",
        "de": "Loslegen",
        "fr": "Commencer",
    },
    "Tools": {"ru": "Инструменты", "es": "Herramientas", "de": "Tools", "fr": "Outils"},
    "Professional Tools": {"ru": "Профессиональные инструменты", "es": "Herramientas profesionales", "de": "Profi-Tools", "fr": "Outils professionnels"},
    "Creative Tools": {"ru": "Творческие инструменты", "es": "Herramientas creativas", "de": "Kreative Tools", "fr": "Outils créatifs"},
    "Admin Panel": {"ru": "Панель администратора", "es": "Panel de administración", "de": "Admin-Bereich", "fr": "Panneau d'administration"},
    "Menu": {"ru": "Меню", "es": "Menú", "de": "Menü", "fr": "Menu"},
    "Upgrade to Pro": {"ru": "Перейти на Pro", "es": "Pasar a Pro", "de": "Auf Pro upgraden", "fr": "Passer à Pro"},
    "Welcome back": {"ru": "С возвращением", "es": "Bienvenido de nuevo", "de": "Willkommen zurück", "fr": "Bon retour"},
    "Search tools": {"ru": "Поиск инструментов", "es": "Buscar herramientas", "de": "Tools suchen", "fr": "Rechercher des outils"},
    "Search tools by name...": {"ru": "Поиск по названию...", "es": "Buscar por nombre...", "de": "Tools nach Name suchen...", "fr": "Rechercher par nom..."},
    "Recently Used": {"ru": "Недавно использованные", "es": "Usados recientemente", "de": "Zuletzt verwendet", "fr": "Récemment utilisés"},
    "Featured Tools": {"ru": "Избранные инструменты", "es": "Herramientas destacadas", "de": "Empfohlene Tools", "fr": "Outils en vedette"},
    "Upgrade to Ultimate": {"ru": "Перейти на Ultimate", "es": "Pasar a Ultimate", "de": "Auf Ultimate upgraden", "fr": "Passer à Ultimate"},
    "Open Tool": {"ru": "Открыть инструмент", "es": "Abrir herramienta", "de": "Tool öffnen", "fr": "Ouvrir l'outil"},
    "All tools": {"ru": "Все инструменты", "es": "Todos los herramientas", "de": "Alle Tools", "fr": "Tous les outils"},
    "Use the sidebar": {"ru": "Используйте боковую панель", "es": "Use la barra lateral", "de": "Sidebar nutzen", "fr": "Utilisez la barre latérale"},
    "to browse Professional Suite and Creative Studio.": {"ru": "для просмотра Professional Suite и Creative Studio.", "es": "para explorar Professional Suite y Creative Studio.", "de": "um Professional Suite und Creative Studio zu durchsuchen.", "fr": "pour parcourir Professional Suite et Creative Studio."},
    "Create professional content in seconds with artificial intelligence.": {"ru": "Создавайте профессиональный контент за секунды с ИИ.", "es": "Cree contenido profesional en segundos con IA.", "de": "Erstellen Sie in Sekunden professionelle Inhalte mit KI.", "fr": "Créez du contenu professionnel en secondes avec l'IA."},
    "Access to Tools": {"ru": "Доступ к инструментам", "es": "Acceso a herramientas", "de": "Zugang zu Tools", "fr": "Accès aux outils"},
    "To use AI tools, you need to log in or register.": {"ru": "Войдите или зарегистрируйтесь для использования ИИ-инструментов.", "es": "Inicie sesión o regístrese para usar las herramientas de IA.", "de": "Melden Sie sich an oder registrieren Sie sich für KI-Tools.", "fr": "Connectez-vous ou inscrivez-vous pour utiliser les outils IA."},
    "Log in": {"ru": "Войти", "es": "Iniciar sesión", "de": "Anmelden", "fr": "Connexion"},
    "Register": {"ru": "Регистрация", "es": "Registrarse", "de": "Registrieren", "fr": "S'inscrire"},
    "Log in — AI Multi Tool": {"ru": "Войти — AI Multi Tool", "es": "Iniciar sesión — AI Multi Tool", "de": "Anmelden — AI Multi Tool", "fr": "Connexion — AI Multi Tool"},
    "Sign in to use AI tools and manage your credits.": {"ru": "Войдите, чтобы использовать ИИ-инструменты и управлять кредитами.", "es": "Inicie sesión para usar las herramientas de IA y gestionar sus créditos.", "de": "Melden Sie sich an, um KI-Tools zu nutzen und Credits zu verwalten.", "fr": "Connectez-vous pour utiliser les outils IA et gérer vos crédits."},
    "Password": {"ru": "Пароль", "es": "Contraseña", "de": "Passwort", "fr": "Mot de passe"},
    "Remember me": {"ru": "Запомнить меня", "es": "Recordarme", "de": "Angemeldet bleiben", "fr": "Se souvenir de moi"},
    "Don't have an account?": {"ru": "Нет аккаунта?", "es": "¿No tiene cuenta?", "de": "Noch kein Konto?", "fr": "Pas de compte ?"},
    "Sign up": {"ru": "Регистрация", "es": "Registrarse", "de": "Registrieren", "fr": "S'inscrire"},
    "Sign up — AI Multi Tool": {"ru": "Регистрация — AI Multi Tool", "es": "Registrarse — AI Multi Tool", "de": "Registrieren — AI Multi Tool", "fr": "S'inscrire — AI Multi Tool"},
    "Create account": {"ru": "Создать аккаунт", "es": "Crear cuenta", "de": "Konto erstellen", "fr": "Créer un compte"},
    "Register to get 10 free credits to try our AI tools.": {"ru": "Зарегистрируйтесь и получите 10 бесплатных кредитов.", "es": "Regístrese y obtenga 10 créditos gratis para probar nuestras herramientas de IA.", "de": "Registrieren Sie sich und erhalten Sie 10 kostenlose Credits.", "fr": "Inscrivez-vous et recevez 10 crédits gratuits pour essayer nos outils IA."},
    "Confirm password": {"ru": "Подтвердите пароль", "es": "Confirmar contraseña", "de": "Passwort bestätigen", "fr": "Confirmer le mot de passe"},
    "At least 6 characters": {"ru": "Минимум 6 символов", "es": "Al menos 6 caracteres", "de": "Mindestens 6 Zeichen", "fr": "Au moins 6 caractères"},
    "Already have an account?": {"ru": "Уже есть аккаунт?", "es": "¿Ya tiene cuenta?", "de": "Bereits ein Konto?", "fr": "Déjà un compte ?"},
    "Settings": {"ru": "Настройки", "es": "Ajustes", "de": "Einstellungen", "fr": "Paramètres"},
    "Language": {"ru": "Язык", "es": "Idioma", "de": "Sprache", "fr": "Langue"},
    "AI": {"ru": "AI", "es": "IA", "de": "KI", "fr": "IA"},
    "Multi Tools": {"ru": "Мультиинструменты", "es": "Multi Herramientas", "de": "Multi-Tools", "fr": "Multi Outils"},
    "English": {"ru": "Английский", "es": "Inglés", "de": "Englisch", "fr": "Anglais"},
    "Ukrainian": {"ru": "Украинский", "es": "Ucraniano", "de": "Ukrainisch", "fr": "Ukrainien"},
    "Spanish": {"ru": "Испанский", "es": "Español", "de": "Spanisch", "fr": "Espagnol"},
    "German": {"ru": "Немецкий", "es": "Alemán", "de": "Deutsch", "fr": "Allemand"},
    "French": {"ru": "Французский", "es": "Francés", "de": "Französisch", "fr": "Français"},
    "Russian": {"ru": "Русский", "es": "Ruso", "de": "Russisch", "fr": "Russe"},
    "No tools found": {"ru": "Инструменты не найдены", "es": "No se encontraron herramientas", "de": "Keine Tools gefunden", "fr": "Aucun outil trouvé"},
    "Close": {"ru": "Закрыть", "es": "Cerrar", "de": "Schließen", "fr": "Fermer"},
    "Professional Suite": {"ru": "Профессиональный пакет", "es": "Suite profesional", "de": "Professional Suite", "fr": "Suite professionnelle"},
    "Creative Studio": {"ru": "Творческая студия", "es": "Estudio creativo", "de": "Creative Studio", "fr": "Studio créatif"},
    "Account & Billing": {"ru": "Аккаунт и оплата", "es": "Cuenta y facturación", "de": "Konto & Abrechnung", "fr": "Compte et facturation"},
    "Get started free": {"ru": "Начать бесплатно", "es": "Empezar gratis", "de": "Kostenlos starten", "fr": "Commencer gratuitement"},
    "See full pricing": {"ru": "Посмотреть тарифы", "es": "Ver precios", "de": "Preise ansehen", "fr": "Voir les tarifs"},
    "Ready to create?": {"ru": "Готовы создавать?", "es": "¿Listo para crear?", "de": "Bereit zu erstellen?", "fr": "Prêt à créer ?"},
    "Sign up in seconds. No credit card required for the free plan.": {"ru": "Регистрация за секунды. Без карты для бесплатного плана.", "es": "Regístrese en segundos. No se requiere tarjeta para el plan gratis.", "de": "In Sekunden registrieren. Keine Karte für den kostenlosen Plan nötig.", "fr": "Inscription en secondes. Pas de carte requise pour le plan gratuit."},
    "Simple pricing": {"ru": "Простые тарифы", "es": "Precios simples", "de": "Einfache Preise", "fr": "Tarifs simples"},
    "Blog": {"ru": "Блог", "es": "Blog", "de": "Blog", "fr": "Blog"},
    "Fast & simple": {"ru": "Быстро и просто", "es": "Rápido y sencillo", "de": "Schnell und einfach", "fr": "Rapide et simple"},
    "Why AI Multi Tools": {"ru": "Почему AI Multi Tools", "es": "Por qué AI Multi Tools", "de": "Warum AI Multi Tools", "fr": "Pourquoi AI Multi Tools"},
    "Amazon, Shopify, Etsy, resumes, KDP, YouTube scripts, TikTok hooks, and Google Ads copy.": {"ru": "Amazon, Shopify, Etsy, резюме, KDP, сценарии YouTube, TikTok и реклама Google.", "es": "Amazon, Shopify, Etsy, currículos, KDP, guiones YouTube, TikTok y Google Ads.", "de": "Amazon, Shopify, Etsy, Lebensläufe, KDP, YouTube-Skripte, TikTok, Google Ads.", "fr": "Amazon, Shopify, Etsy, CV, KDP, scripts YouTube, TikTok, Google Ads."},
    "Finance, business, marketing, tech, health, education, travel, food, fitness, beauty, real estate, psychology.": {"ru": "Финансы, бизнес, маркетинг, технологии, здоровье, образование, путешествия, еда, фитнес, красота, недвижимость, психология.", "es": "Finanzas, negocios, marketing, tecnología, salud, educación, viajes, comida, fitness, belleza, bienes raíces, psicología.", "de": "Finanzen, Business, Marketing, Technik, Gesundheit, Bildung, Reisen, Essen, Fitness, Beauty, Immobilien, Psychologie.", "fr": "Finance, business, marketing, tech, santé, éducation, voyage, alimentation, fitness, beauté, immobilier, psychologie."},
    "Describe your task, get optimized content. Credits-based usage with flexible plans.": {"ru": "Опишите задачу — получите контент. Кредиты и гибкие планы.", "es": "Describa su tarea, obtenga contenido optimizado. Uso por créditos con planes flexibles.", "de": "Beschreiben Sie Ihre Aufgabe, erhalten Sie optimierte Inhalte. Nutzung auf Kreditbasis mit flexiblen Plänen.", "fr": "Décrivez votre tâche, obtenez du contenu optimisé. Crédits et forfaits flexibles."},
    "AI Multi Tools": {"ru": "AI Multi Tools", "es": "AI Multi Tools", "de": "AI Multi Tools", "fr": "AI Multi Tools"},
    "Open menu": {"ru": "Открыть меню", "es": "Abrir menú", "de": "Menü öffnen", "fr": "Ouvrir le menu"},
    "Toggle navigation": {"ru": "Переключить навигацию", "es": "Alternar navegación", "de": "Navigation umschalten", "fr": "Basculer la navigation"},
    "Notifications": {"ru": "Уведомления", "es": "Notificaciones", "de": "Benachrichtigungen", "fr": "Notifications"},
    "Main": {"ru": "Главное", "es": "Principal", "de": "Haupt", "fr": "Principal"},
    "AI Multi Tools - Create professional content in seconds with artificial intelligence": {"ru": "AI Multi Tools — создавайте профессиональный контент за секунды с ИИ", "es": "AI Multi Tools — cree contenido profesional en segundos con IA", "de": "AI Multi Tools — professionelle Inhalte in Sekunden mit KI erstellen", "fr": "AI Multi Tools — créez du contenu professionnel en secondes avec l'IA"},
    "Create professional content in seconds with AI. Amazon, Shopify, Etsy, resumes, KDP, YouTube, TikTok, and 20+ tools. Free tier available.": {"ru": "Создавайте контент за секунды с ИИ. Amazon, Shopify, Etsy, резюме, KDP, YouTube, TikTok и 20+ инструментов. Есть бесплатный план.", "es": "Cree contenido profesional en segundos con IA. Amazon, Shopify, Etsy, currículos, KDP, YouTube, TikTok y 20+ herramientas. Plan gratis disponible.", "de": "Erstellen Sie in Sekunden professionelle Inhalte mit KI. Amazon, Shopify, Etsy, Lebensläufe, KDP, YouTube, TikTok und 20+ Tools. Kostenloser Plan verfügbar.", "fr": "Créez du contenu professionnel en secondes avec l'IA. Amazon, Shopify, Etsy, CV, KDP, YouTube, TikTok et 20+ outils. Plan gratuit disponible."},
    "AI multi tools, artificial intelligence, content creation, SEO content, Amazon, Shopify, Etsy": {"ru": "AI мультиинструменты, искусственный интеллект, создание контента, SEO, Amazon, Shopify, Etsy", "es": "Herramientas IA, inteligencia artificial, creación de contenido, SEO, Amazon, Shopify, Etsy", "de": "KI-Multi-Tools, künstliche Intelligenz, Content-Erstellung, SEO, Amazon, Shopify, Etsy", "fr": "Outils IA, intelligence artificielle, création de contenu, SEO, Amazon, Shopify, Etsy"},
    "AI Multi Tools - Create Professional Content in Seconds": {"ru": "AI Multi Tools — создавайте профессиональный контент за секунды", "es": "AI Multi Tools — cree contenido profesional en segundos", "de": "AI Multi Tools — professionelle Inhalte in Sekunden erstellen", "fr": "AI Multi Tools — créez du contenu professionnel en secondes"},
    "Create professional content in seconds with AI. Free tier, Pro and Business plans. Start free.": {"ru": "Создавайте контент за секунды с ИИ. Бесплатный, Pro и Бизнес планы. Начните бесплатно.", "es": "Cree contenido en segundos con IA. Plan gratis, Pro y Business. Empiece gratis.", "de": "Erstellen Sie in Sekunden Inhalte mit KI. Kostenloser, Pro- und Business-Plan. Kostenlos starten.", "fr": "Créez du contenu en secondes avec l'IA. Plan gratuit, Pro et Business. Commencez gratuitement."},
    "Create professional content in seconds with AI.": {"ru": "Создавайте профессиональный контент за секунды с ИИ.", "es": "Cree contenido profesional en segundos con IA.", "de": "Erstellen Sie in Sekunden professionelle Inhalte mit KI.", "fr": "Créez du contenu professionnel en secondes avec l'IA."},
    "AI Multi Tools - Create professional content in seconds": {"ru": "AI Multi Tools — создавайте профессиональный контент за секунды", "es": "AI Multi Tools — cree contenido profesional en segundos", "de": "AI Multi Tools — professionelle Inhalte in Sekunden erstellen", "fr": "AI Multi Tools — créez du contenu professionnel en secondes"},
    "All plans include access to the dashboard and AI tools. Secure payment via Stripe.": {"ru": "Все планы включают доступ к панели и ИИ-инструментам. Оплата через Stripe.", "es": "Todos los planes incluyen acceso al panel y herramientas de IA. Pago seguro con Stripe.", "de": "Alle Pläne beinhalten Zugang zum Dashboard und KI-Tools. Sichere Zahlung über Stripe.", "fr": "Tous les forfaits incluent l'accès au tableau de bord et aux outils IA. Paiement sécurisé via Stripe."},
}

def escape_po(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def format_entry(comment, msgid, msgstr):
    mid_esc = escape_po(msgid)
    mst_esc = escape_po(msgstr)
    return f'{comment}\nmsgid "{mid_esc}"\nmsgstr "{mst_esc}"'

def main():
    en_path = os.path.join(BASE, 'en', 'LC_MESSAGES', 'messages.po')
    en = parse_po(en_path)
    all_ids = set(en.keys())
    for lang in ['ru', 'es', 'de', 'fr']:
        path = os.path.join(BASE, lang, 'LC_MESSAGES', 'messages.po')
        data = parse_po(path)
        missing = all_ids - set(data.keys())
        if not missing:
            print(f'{lang}: no missing keys')
            continue
        lines = []
        en_order = list(en.keys())
        missing_ordered = [k for k in en_order if k in missing]
        for msgid in missing_ordered:
            if msgid not in MISSING_TRANSLATIONS:
                tr = en.get(msgid, msgid)
            else:
                tr = MISSING_TRANSLATIONS[msgid].get(lang, en.get(msgid, msgid))
            lines.append(format_entry('# (added)', msgid, tr))
        append_entries(path, '\n\n'.join(lines))
        print(f'{lang}: added {len(missing)} entries')

if __name__ == '__main__':
    main()
