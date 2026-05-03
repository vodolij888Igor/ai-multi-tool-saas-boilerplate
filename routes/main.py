"""
Роути для головної сторінки: sitemap, legacy /creative, /<lang>/tool; / and /tool are overridden by ai_bp.
"""
from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from flask_login import login_required, current_user
from config import Config
from backend.utils.locale import get_locale

main_bp = Blueprint('main', __name__)

def get_translations():
    """Повертає словник перекладів для поточної мови"""
    locale = str(get_locale())
    
    translations = {
        'uk': {
            'title': 'MindixoAI - Професійна SaaS Платформа',
            'hero_title': 'MindixoAI',
            'hero_subtitle': 'Створюйте професійний контент за секунди за допомогою штучного інтелекту',
            'select_niche': 'Оберіть нішу',
            'create_content': 'Створити контент',
            'selected_niche': 'Обрана ніша:',
            'select_niche_placeholder': 'Оберіть нішу зверху',
            'content_type': 'Тип контенту:',
            'select_content_type': 'Оберіть тип контенту',
            'article': 'Стаття',
            'social': 'Соціальні мережі',
            'email': 'Email',
            'describe_prompt': 'Опишіть, що потрібно створити:',
            'prompt_placeholder': 'Наприклад: Напиши статтю про 10 способів економії грошей...',
            'generate': 'Згенерувати контент',
            'generated_content': 'Згенерований контент',
            'copy': 'Копіювати',
            'loading': 'Завантаження...',
            'generating': 'Генеруємо ваш контент...',
            'access_tools': 'Доступ до інструментів',
            'login_required': 'Для використання генератора AI контенту необхідно увійти в систему або зареєструватися.',
            'login': 'Увійти',
            'register': 'Зареєструватися',
            'logout': 'Вийти',
            'rights': 'Всі права захищені.'
        },
        'en': {
            'title': 'MindixoAI - Professional SaaS Platform',
            'hero_title': 'MindixoAI',
            'hero_subtitle': 'Create professional content in seconds with artificial intelligence',
            'select_niche': 'Select a niche',
            'create_content': 'Create content',
            'selected_niche': 'Selected niche:',
            'select_niche_placeholder': 'Select a niche above',
            'content_type': 'Content type:',
            'select_content_type': 'Select content type',
            'article': 'Article',
            'social': 'Social media',
            'email': 'Email',
            'describe_prompt': 'Describe what you need to create:',
            'prompt_placeholder': 'For example: Write an article about 10 ways to save money...',
            'generate': 'Generate content',
            'generated_content': 'Generated content',
            'copy': 'Copy',
            'loading': 'Loading...',
            'generating': 'Generating your content...',
            'access_tools': 'Access to tools',
            'login_required': 'To use the AI content generator, you need to log in or register.',
            'login': 'Log in',
            'register': 'Register',
            'logout': 'Log out',
            'rights': 'All rights reserved.'
        },
        'es': {
            'title': 'MindixoAI - Plataforma SaaS Profesional',
            'hero_title': 'Generador de Contenido AI',
            'hero_subtitle': 'Crea contenido profesional en segundos con inteligencia artificial',
            'select_niche': 'Selecciona un nicho',
            'create_content': 'Crear contenido',
            'selected_niche': 'Nicho seleccionado:',
            'select_niche_placeholder': 'Selecciona un nicho arriba',
            'content_type': 'Tipo de contenido:',
            'select_content_type': 'Selecciona el tipo de contenido',
            'article': 'Artículo',
            'social': 'Redes sociales',
            'email': 'Email',
            'describe_prompt': 'Describe lo que necesitas crear:',
            'prompt_placeholder': 'Por ejemplo: Escribe un artículo sobre 10 formas de ahorrar dinero...',
            'generate': 'Generar contenido',
            'generated_content': 'Contenido generado',
            'copy': 'Copiar',
            'loading': 'Cargando...',
            'generating': 'Generando tu contenido...',
            'access_tools': 'Acceso a herramientas',
            'login_required': 'Para usar el generador de contenido AI, necesitas iniciar sesión o registrarte.',
            'login': 'Iniciar sesión',
            'register': 'Registrarse',
            'logout': 'Cerrar sesión',
            'rights': 'Todos los derechos reservados.'
        }
    }
    
    return translations.get(locale, translations['en'])

def get_niches():
    """Повертає список ніш з перекладами"""
    locale = str(get_locale())
    niches_data = {
        'finance': {'uk': 'Фінанси', 'en': 'Finance', 'es': 'Finanzas', 'icon': '💰'},
        'kdp': {'uk': 'KDP (Kindle Direct Publishing)', 'en': 'KDP (Kindle Direct Publishing)', 'es': 'KDP (Kindle Direct Publishing)', 'icon': '📚'},
        'business': {'uk': 'Бізнес', 'en': 'Business', 'es': 'Negocios', 'icon': '💼'},
        'marketing': {'uk': 'Маркетинг', 'en': 'Marketing', 'es': 'Marketing', 'icon': '📢'},
        'technology': {'uk': 'Технології', 'en': 'Technology', 'es': 'Tecnología', 'icon': '💻'},
        'health': {'uk': 'Здоров\'я', 'en': 'Health', 'es': 'Salud', 'icon': '🏥'},
        'education': {'uk': 'Освіта', 'en': 'Education', 'es': 'Educación', 'icon': '🎓'},
        'travel': {'uk': 'Подорожі', 'en': 'Travel', 'es': 'Viajes', 'icon': '✈️'},
        'food': {'uk': 'Їжа та ресторани', 'en': 'Food & Restaurants', 'es': 'Comida y Restaurantes', 'icon': '🍽️'},
        'fitness': {'uk': 'Фітнес', 'en': 'Fitness', 'es': 'Fitness', 'icon': '💪'},
        'beauty': {'uk': 'Краса', 'en': 'Beauty', 'es': 'Belleza', 'icon': '💄'},
        'real-estate': {'uk': 'Нерухомість', 'en': 'Real Estate', 'es': 'Bienes Raíces', 'icon': '🏠'},
        'psychology': {'uk': 'Психологічна підтримка', 'en': 'Psychological Support', 'es': 'Apoyo Psicológico', 'icon': '🧠'}
    }
    
    niches = []
    for niche_id, niche_info in niches_data.items():
        niches.append({
            'id': niche_id,
            'name': niche_info.get(locale, niche_info.get('en', niche_info['uk'])),
            'icon': niche_info['icon']
        })
    
    return niches

def get_seo_data(niche_id=None):
    """Повертає SEO дані для поточної мови та ніші"""
    locale = str(get_locale())
    
    seo_data = {
        'uk': {
            'home': {
                'title': 'AI Генератор Контенту - Створюйте Професійний Контент за Секунди',
                'description': 'Генератор AI контенту для фінансів, бізнесу, маркетингу, KDP та інших ніш. Створюйте статті, блоги, пости для соцмереж та email за допомогою штучного інтелекту.',
                'keywords': 'AI генератор контенту, штучний інтелект, створення контенту, генератор статей, AI контент, автоматичне написання'
            },
            'finance': {
                'title': 'AI Генератор Фінансового Контенту - Статті про Фінанси та Інвестиції',
                'description': 'Створюйте професійний фінансовий контент: статті про інвестиції, фінансове планування, економію грошей. AI генератор для фінансових блогів та медіа.',
                'keywords': 'фінансовий контент, статті про інвестиції, фінансове планування, AI фінанси, генератор фінансових статей'
            },
            'kdp': {
                'title': 'AI Генератор Контенту для KDP - Kindle Direct Publishing',
                'description': 'Створюйте контент для книг на Amazon KDP: описи, анотації, маркетингові тексти. AI помічник для авторів Kindle.',
                'keywords': 'KDP контент, Kindle Direct Publishing, AI для авторів, генератор описів книг, Amazon KDP'
            },
            'business': {
                'title': 'AI Генератор Бізнес Контенту - Статті про Бізнес та Підприємництво',
                'description': 'Професійний генератор бізнес контенту: статті про стратегії, управління, підприємництво. AI для бізнес блогів та медіа.',
                'keywords': 'бізнес контент, статті про бізнес, підприємництво, AI бізнес, генератор бізнес статей'
            },
            'marketing': {
                'title': 'AI Генератор Маркетингового Контенту - Контент для Маркетингу',
                'description': 'Створюйте ефективний маркетинговий контент: рекламні тексти, пости для соцмереж, email кампанії. AI генератор для маркетологів.',
                'keywords': 'маркетинговий контент, рекламні тексти, AI маркетинг, генератор маркетингових статей, контент маркетинг'
            },
            'technology': {
                'title': 'AI Генератор Технічного Контенту - Статті про Технології',
                'description': 'Створюйте технічний контент про технології, програмування, інновації. AI генератор для технічних блогів та медіа.',
                'keywords': 'технічний контент, статті про технології, AI технології, генератор технічних статей, програмування'
            },
            'health': {
                'title': 'AI Генератор Контенту про Здоров\'я - Статті про Здоров\'я та Медицину',
                'description': 'Створюйте інформативний контент про здоров\'я, дієти, фітнес, медицину. AI генератор для здоров\'я блогів.',
                'keywords': 'контент про здоров\'я, статті про здоров\'я, AI здоров\'я, генератор статей про здоров\'я, медицина'
            },
            'education': {
                'title': 'AI Генератор Освітнього Контенту - Навчальні Матеріали',
                'description': 'Створюйте навчальний контент для освіти: статті, уроки, навчальні матеріали. AI генератор для педагогів та освітніх платформ.',
                'keywords': 'освітній контент, навчальні матеріали, AI освіта, генератор освітніх статей, навчання'
            },
            'travel': {
                'title': 'AI Генератор Контенту про Подорожі - Статті про Туризм',
                'description': 'Створюйте захоплюючий контент про подорожі, туризм, відпочинок. AI генератор для туристичних блогів та медіа.',
                'keywords': 'контент про подорожі, туристичні статті, AI подорожі, генератор туристичних статей, туризм'
            },
            'food': {
                'title': 'AI Генератор Кулінарного Контенту - Статті про Їжу та Ресторани',
                'description': 'Створюйте апетитний контент про їжу, рецепти, ресторани. AI генератор для кулінарних блогів та медіа.',
                'keywords': 'кулінарний контент, рецепти, AI їжа, генератор кулінарних статей, ресторани'
            },
            'fitness': {
                'title': 'AI Генератор Фітнес Контенту - Статті про Фітнес та Тренування',
                'description': 'Створюйте мотивуючий контент про фітнес, тренування, здорове життя. AI генератор для фітнес блогів.',
                'keywords': 'фітнес контент, статті про тренування, AI фітнес, генератор фітнес статей, здорове життя'
            },
            'beauty': {
                'title': 'AI Генератор Контенту про Красу - Статті про Красу та Косметику',
                'description': 'Створюйте стильний контент про красу, косметику, модні тренди. AI генератор для блогів про красу.',
                'keywords': 'контент про красу, косметика, AI краса, генератор статей про красу, мода'
            },
            'real-estate': {
                'title': 'AI Генератор Контенту про Нерухомість - Статті про Нерухомість',
                'description': 'Створюйте професійний контент про нерухомість, інвестиції, нерухомість. AI генератор для нерухомості блогів.',
                'keywords': 'контент про нерухомість, статті про нерухомість, AI нерухомість, генератор статей про нерухомість, інвестиції'
            },
            'psychology': {
                'title': 'AI Психолог - Психологічна Допомога та Консультації',
                'description': 'Отримайте психологічну підтримку та консультації за допомогою AI. Допомога з ментальним здоров\'ям, стресом, тривогою та іншими психологічними питаннями.',
                'keywords': 'психологічна допомога, AI психолог, ментальне здоров\'я, психологічні консультації, стрес, тривога'
            }
        },
        'en': {
            'home': {
                'title': 'MindixoAI - Create Professional Content in Seconds',
                'description': 'AI content generator for finance, business, marketing, KDP and other niches. Create articles, blogs, social media posts and emails with artificial intelligence.',
                'keywords': 'AI content generator, artificial intelligence, content creation, article generator, AI content, automatic writing'
            },
            'finance': {
                'title': 'AI Finance Content Generator - Articles about Finance and Investments',
                'description': 'Create professional finance content: articles about investments, financial planning, saving money. AI generator for finance blogs and media.',
                'keywords': 'finance content, investment articles, financial planning, AI finance, finance article generator'
            },
            'kdp': {
                'title': 'MindixoAI for KDP - Kindle Direct Publishing',
                'description': 'Create content for Amazon KDP books: descriptions, summaries, marketing texts. AI assistant for Kindle authors.',
                'keywords': 'KDP content, Kindle Direct Publishing, AI for authors, book description generator, Amazon KDP'
            },
            'business': {
                'title': 'AI Business Content Generator - Articles about Business and Entrepreneurship',
                'description': 'Professional business content generator: articles about strategies, management, entrepreneurship. AI for business blogs and media.',
                'keywords': 'business content, business articles, entrepreneurship, AI business, business article generator'
            },
            'marketing': {
                'title': 'AI Marketing Content Generator - Marketing Content',
                'description': 'Create effective marketing content: ad copy, social media posts, email campaigns. AI generator for marketers.',
                'keywords': 'marketing content, ad copy, AI marketing, marketing article generator, content marketing'
            },
            'technology': {
                'title': 'AI Technology Content Generator - Articles about Technology',
                'description': 'Create technical content about technology, programming, innovation. AI generator for tech blogs and media.',
                'keywords': 'technology content, tech articles, AI technology, technology article generator, programming'
            },
            'health': {
                'title': 'AI Health Content Generator - Articles about Health and Medicine',
                'description': 'Create informative content about health, diets, fitness, medicine. AI generator for health blogs.',
                'keywords': 'health content, health articles, AI health, health article generator, medicine'
            },
            'education': {
                'title': 'AI Education Content Generator - Educational Materials',
                'description': 'Create educational content: articles, lessons, learning materials. AI generator for educators and educational platforms.',
                'keywords': 'education content, educational materials, AI education, education article generator, learning'
            },
            'travel': {
                'title': 'AI Travel Content Generator - Articles about Tourism',
                'description': 'Create engaging content about travel, tourism, vacation. AI generator for travel blogs and media.',
                'keywords': 'travel content, travel articles, AI travel, travel article generator, tourism'
            },
            'food': {
                'title': 'AI Food Content Generator - Articles about Food and Restaurants',
                'description': 'Create appetizing content about food, recipes, restaurants. AI generator for food blogs and media.',
                'keywords': 'food content, recipes, AI food, food article generator, restaurants'
            },
            'fitness': {
                'title': 'AI Fitness Content Generator - Articles about Fitness and Training',
                'description': 'Create motivating content about fitness, training, healthy living. AI generator for fitness blogs.',
                'keywords': 'fitness content, training articles, AI fitness, fitness article generator, healthy living'
            },
            'beauty': {
                'title': 'AI Beauty Content Generator - Articles about Beauty and Cosmetics',
                'description': 'Create stylish content about beauty, cosmetics, fashion trends. AI generator for beauty blogs.',
                'keywords': 'beauty content, cosmetics, AI beauty, beauty article generator, fashion'
            },
            'real-estate': {
                'title': 'AI Real Estate Content Generator - Articles about Real Estate',
                'description': 'Create professional content about real estate, investments, property. AI generator for real estate blogs.',
                'keywords': 'real estate content, real estate articles, AI real estate, real estate article generator, investments'
            },
            'psychology': {
                'title': 'AI Psychologist - Psychological Support and Counseling',
                'description': 'Get psychological support and counseling with AI. Help with mental health, stress, anxiety and other psychological issues.',
                'keywords': 'psychological support, AI psychologist, mental health, psychological counseling, stress, anxiety'
            }
        },
        'es': {
            'home': {
                'title': 'Generador de Contenido AI - Crea Contenido Profesional en Segundos',
                'description': 'Generador de contenido AI para finanzas, negocios, marketing, KDP y otros nichos. Crea artículos, blogs, publicaciones en redes sociales y emails con inteligencia artificial.',
                'keywords': 'generador de contenido AI, inteligencia artificial, creación de contenido, generador de artículos, contenido AI, escritura automática'
            },
            'finance': {
                'title': 'Generador de Contenido Financiero AI - Artículos sobre Finanzas e Inversiones',
                'description': 'Crea contenido financiero profesional: artículos sobre inversiones, planificación financiera, ahorro de dinero. Generador AI para blogs financieros y medios.',
                'keywords': 'contenido financiero, artículos sobre inversiones, planificación financiera, AI finanzas, generador de artículos financieros'
            },
            'kdp': {
                'title': 'Generador de Contenido AI para KDP - Kindle Direct Publishing',
                'description': 'Crea contenido para libros de Amazon KDP: descripciones, resúmenes, textos de marketing. Asistente AI para autores de Kindle.',
                'keywords': 'contenido KDP, Kindle Direct Publishing, AI para autores, generador de descripciones de libros, Amazon KDP'
            },
            'business': {
                'title': 'Generador de Contenido Empresarial AI - Artículos sobre Negocios y Emprendimiento',
                'description': 'Generador profesional de contenido empresarial: artículos sobre estrategias, gestión, emprendimiento. AI para blogs empresariales y medios.',
                'keywords': 'contenido empresarial, artículos empresariales, emprendimiento, AI negocios, generador de artículos empresariales'
            },
            'marketing': {
                'title': 'Generador de Contenido de Marketing AI - Contenido de Marketing',
                'description': 'Crea contenido de marketing efectivo: textos publicitarios, publicaciones en redes sociales, campañas de email. Generador AI para especialistas en marketing.',
                'keywords': 'contenido de marketing, textos publicitarios, AI marketing, generador de artículos de marketing, marketing de contenido'
            },
            'technology': {
                'title': 'Generador de Contenido Tecnológico AI - Artículos sobre Tecnología',
                'description': 'Crea contenido técnico sobre tecnología, programación, innovación. Generador AI para blogs tecnológicos y medios.',
                'keywords': 'contenido tecnológico, artículos tecnológicos, AI tecnología, generador de artículos tecnológicos, programación'
            },
            'health': {
                'title': 'Generador de Contenido de Salud AI - Artículos sobre Salud y Medicina',
                'description': 'Crea contenido informativo sobre salud, dietas, fitness, medicina. Generador AI para blogs de salud.',
                'keywords': 'contenido de salud, artículos de salud, AI salud, generador de artículos de salud, medicina'
            },
            'education': {
                'title': 'Generador de Contenido Educativo AI - Materiales Educativos',
                'description': 'Crea contenido educativo: artículos, lecciones, materiales de aprendizaje. Generador AI para educadores y plataformas educativas.',
                'keywords': 'contenido educativo, materiales educativos, AI educación, generador de artículos educativos, aprendizaje'
            },
            'travel': {
                'title': 'Generador de Contenido de Viajes AI - Artículos sobre Turismo',
                'description': 'Crea contenido atractivo sobre viajes, turismo, vacaciones. Generador AI para blogs de viajes y medios.',
                'keywords': 'contenido de viajes, artículos de viajes, AI viajes, generador de artículos de viajes, turismo'
            },
            'food': {
                'title': 'Generador de Contenido Culinario AI - Artículos sobre Comida y Restaurantes',
                'description': 'Crea contenido apetitoso sobre comida, recetas, restaurantes. Generador AI para blogs culinarios y medios.',
                'keywords': 'contenido culinario, recetas, AI comida, generador de artículos culinarios, restaurantes'
            },
            'fitness': {
                'title': 'Generador de Contenido de Fitness AI - Artículos sobre Fitness y Entrenamiento',
                'description': 'Crea contenido motivador sobre fitness, entrenamiento, vida saludable. Generador AI para blogs de fitness.',
                'keywords': 'contenido de fitness, artículos de entrenamiento, AI fitness, generador de artículos de fitness, vida saludable'
            },
            'beauty': {
                'title': 'Generador de Contenido de Belleza AI - Artículos sobre Belleza y Cosméticos',
                'description': 'Crea contenido elegante sobre belleza, cosméticos, tendencias de moda. Generador AI para blogs de belleza.',
                'keywords': 'contenido de belleza, cosméticos, AI belleza, generador de artículos de belleza, moda'
            },
            'real-estate': {
                'title': 'Generador de Contenido Inmobiliario AI - Artículos sobre Bienes Raíces',
                'description': 'Crea contenido profesional sobre bienes raíces, inversiones, propiedades. Generador AI para blogs inmobiliarios.',
                'keywords': 'contenido inmobiliario, artículos inmobiliarios, AI bienes raíces, generador de artículos inmobiliarios, inversiones'
            },
            'psychology': {
                'title': 'Psicólogo AI - Apoyo Psicológico y Asesoramiento',
                'description': 'Obtén apoyo psicológico y asesoramiento con AI. Ayuda con salud mental, estrés, ansiedad y otros problemas psicológicos.',
                'keywords': 'apoyo psicológico, psicólogo AI, salud mental, asesoramiento psicológico, estrés, ansiedad'
            }
        }
    }
    
    niche_key = niche_id if niche_id else 'home'
    return seo_data.get(locale, seo_data['en']).get(niche_key, seo_data['en']['home'])

def get_popular_queries():
    """Повертає популярні запити для поточної мови"""
    locale = str(get_locale())
    
    queries = {
        'uk': [
            'Як написати статтю про фінанси',
            'Генератор контенту для бізнесу',
            'AI для створення маркетингових текстів',
            'Як створити опис книги для KDP',
            'Генератор статей про технології',
            'AI контент для соціальних мереж',
            'Як написати email для клієнтів',
            'AI для створення контенту про здоров\'я',
            'Як написати статтю про подорожі'
        ],
        'en': [
            'How to write a finance article',
            'Business content generator',
            'AI for creating marketing copy',
            'How to create book description for KDP',
            'Technology article generator',
            'AI content for social media',
            'How to write email for clients',
            'AI for creating health content',
            'How to write a travel article'
        ],
        'es': [
            'Cómo escribir un artículo sobre finanzas',
            'Generador de contenido empresarial',
            'AI para crear textos de marketing',
            'Cómo crear descripción de libro para KDP',
            'Generador de artículos tecnológicos',
            'Contenido AI para redes sociales',
            'Cómo escribir email para clientes',
            'AI para crear contenido de salud',
            'Cómo escribir un artículo sobre viajes'
        ]
    }
    
    return queries.get(locale, queries['en'])

def get_ai_tools():
    """Повертає список AI інструментів"""
    locale = str(get_locale())
    
    tools_data = {
        'amazon': {
            'tool_name': 'amazon',
            'uk': {'name': 'Amazon Listing Optimizer', 'description': 'Оптимізуйте описи товарів для Amazon з SEO-ключовими словами', 'icon': '📦', 'seo_text': 'Професійний інструмент для оптимізації продуктів Amazon. Створюйте SEO-оптимізовані описи, які максимізують видимість та конверсію.'},
            'en': {'name': 'Amazon Listing Optimizer', 'description': 'Optimize product listings for Amazon with SEO keywords', 'icon': '📦', 'seo_text': 'Professional tool for Amazon product optimization. Create SEO-optimized listings that maximize visibility and conversion.'},
            'es': {'name': 'Optimizador de Listados Amazon', 'description': 'Optimiza listados de productos para Amazon con palabras clave SEO', 'icon': '📦', 'seo_text': 'Herramienta profesional para optimización de productos Amazon. Crea listados optimizados para SEO que maximicen la visibilidad y conversión.'}
        },
        'shopify': {
            'tool_name': 'shopify',
            'uk': {'name': 'Shopify Description Generator', 'description': 'Створюйте переконливі описи продуктів для Shopify', 'icon': '🛍️', 'seo_text': 'Генератор описів продуктів для Shopify. Створюйте переконливі, продаючі тексти, які мотивують покупців до дії.'},
            'en': {'name': 'Shopify Description Generator', 'description': 'Create compelling product descriptions for Shopify', 'icon': '🛍️', 'seo_text': 'Shopify product description generator. Create compelling, sales-focused texts that motivate buyers to action.'},
            'es': {'name': 'Generador de Descripciones Shopify', 'description': 'Crea descripciones de productos convincentes para Shopify', 'icon': '🛍️', 'seo_text': 'Generador de descripciones de productos Shopify. Crea textos convincentes y orientados a ventas que motiven a los compradores a actuar.'}
        },
        'etsy': {
            'tool_name': 'etsy',
            'uk': {'name': 'Etsy SEO Title Generator', 'description': 'Генеруйте SEO-оптимізовані заголовки для Etsy', 'icon': '🎨', 'seo_text': 'Генератор SEO заголовків для Etsy. Створюйте оптимізовані заголовки, які максимізують видимість в пошуку Etsy.'},
            'en': {'name': 'Etsy SEO Title Generator', 'description': 'Generate SEO-optimized titles for Etsy listings', 'icon': '🎨', 'seo_text': 'Etsy SEO title generator. Create optimized titles that maximize visibility in Etsy search results.'},
            'es': {'name': 'Generador de Títulos SEO Etsy', 'description': 'Genera títulos optimizados para SEO para listados de Etsy', 'icon': '🎨', 'seo_text': 'Generador de títulos SEO para Etsy. Crea títulos optimizados que maximicen la visibilidad en los resultados de búsqueda de Etsy.'}
        },
        'resume': {
            'tool_name': 'resume',
            'uk': {'name': 'Resume Keyword Optimizer', 'description': 'Оптимізуйте резюме з ключовими словами для ATS систем', 'icon': '📄', 'seo_text': 'Оптимізатор резюме для ATS систем. Аналізуйте вакансії та оптимізуйте резюме з релевантними ключовими словами.'},
            'en': {'name': 'Resume Keyword Optimizer', 'description': 'Optimize resumes with keywords for ATS systems', 'icon': '📄', 'seo_text': 'Resume optimizer for ATS systems. Analyze job descriptions and optimize resumes with relevant keywords.'},
            'es': {'name': 'Optimizador de Palabras Clave CV', 'description': 'Optimiza currículums con palabras clave para sistemas ATS', 'icon': '📄', 'seo_text': 'Optimizador de currículums para sistemas ATS. Analiza descripciones de trabajo y optimiza currículums con palabras clave relevantes.'}
        },
        'kdp': {
            'tool_name': 'kdp',
            'uk': {'name': 'KDP (Kindle Direct Publishing)', 'description': 'Створюйте контент для Kindle Direct Publishing', 'icon': '📚', 'seo_text': 'Професійний інструмент для створення контенту для Kindle Direct Publishing. Створюйте описи книг, ключові слова та маркетингові матеріали.'},
            'en': {'name': 'KDP (Kindle Direct Publishing)', 'description': 'Create content for Kindle Direct Publishing', 'icon': '📚', 'seo_text': 'Professional tool for creating content for Kindle Direct Publishing. Create book descriptions, keywords, and marketing materials.'},
            'es': {'name': 'KDP (Kindle Direct Publishing)', 'description': 'Crea contenido para Kindle Direct Publishing', 'icon': '📚', 'seo_text': 'Herramienta profesional para crear contenido para Kindle Direct Publishing. Crea descripciones de libros, palabras clave y materiales de marketing.'}
        },
        'youtube-script': {
            'tool_name': 'youtube-script',
            'uk': {'name': 'YouTube Script Writer', 'description': 'Створюйте професійні сценарії для YouTube відео', 'icon': '🎬', 'seo_text': 'Професійний генератор сценаріїв для YouTube. Створюйте залучуючі, структуровані сценарії, які максимізують утримання аудиторії та engagement.'},
            'en': {'name': 'YouTube Script Writer', 'description': 'Create professional scripts for YouTube videos', 'icon': '🎬', 'seo_text': 'Professional YouTube script generator. Create engaging, structured scripts that maximize audience retention and engagement.'},
            'es': {'name': 'Escritor de Guiones YouTube', 'description': 'Crea guiones profesionales para videos de YouTube', 'icon': '🎬', 'seo_text': 'Generador profesional de guiones para YouTube. Crea guiones atractivos y estructurados que maximicen la retención y participación de la audiencia.'}
        },
        'tiktok-hook': {
            'tool_name': 'tiktok-hook',
            'uk': {'name': 'TikTok Hook Generator', 'description': 'Генеруйте залучуючі хуки для TikTok відео', 'icon': '🎵', 'seo_text': 'Генератор хуків для TikTok. Створюйте привабливі перші секунди, які максимізують перегляд та engagement на TikTok.'},
            'en': {'name': 'TikTok Hook Generator', 'description': 'Generate engaging hooks for TikTok videos', 'icon': '🎵', 'seo_text': 'TikTok hook generator. Create compelling opening seconds that maximize views and engagement on TikTok.'},
            'es': {'name': 'Generador de Ganchos TikTok', 'description': 'Genera ganchos atractivos para videos de TikTok', 'icon': '🎵', 'seo_text': 'Generador de ganchos para TikTok. Crea primeros segundos convincentes que maximicen las visualizaciones y participación en TikTok.'}
        },
        'google-ads': {
            'tool_name': 'google-ads',
            'uk': {'name': 'Google Ads Copywriter', 'description': 'Створюйте переконливі тексти для Google Ads', 'icon': '📊', 'seo_text': 'Професійний копірайтер для Google Ads. Створюйте оптимізовані оголошення, які максимізують CTR та конверсію.'},
            'en': {'name': 'Google Ads Copywriter', 'description': 'Create compelling copy for Google Ads', 'icon': '📊', 'seo_text': 'Professional Google Ads copywriter. Create optimized ads that maximize CTR and conversion rates.'},
            'es': {'name': 'Redactor Publicitario Google Ads', 'description': 'Crea textos convincentes para Google Ads', 'icon': '📊', 'seo_text': 'Redactor publicitario profesional para Google Ads. Crea anuncios optimizados que maximicen el CTR y las tasas de conversión.'}
        }
    }
    
    tools = []
    for tool_id, tool_info in tools_data.items():
        locale_data = tool_info.get(locale, tool_info['en'])
        tools.append({
            'id': tool_id,
            'tool_name': tool_info['tool_name'],
            'name': locale_data['name'],
            'description': locale_data['description'],
            'icon': locale_data['icon'],
            'seo_text': locale_data.get('seo_text', '')
        })
    
    return tools

def get_personal_creative_tools():
    """Повертає список особистих та креативних інструментів (12 ніш, KDP переміщено до Professional AI Tools)"""
    locale = str(get_locale())
    
    # 12 оригінальних ніш (без KDP, який тепер у Professional AI Tools) + описи та SEO тексти
    original_niches_data = {
        'finance': {
            'uk': 'Фінанси', 'en': 'Finance', 'es': 'Finanzas', 'icon': '💰',
            'description_uk': 'Створюйте контент про фінанси, інвестиції та економіку',
            'description_en': 'Create content about finance, investments and economics',
            'description_es': 'Crea contenido sobre finanzas, inversiones y economía',
            'seo_text_uk': 'Професійний генератор контенту про фінанси та інвестиції. Створюйте статті, поради та аналітику для фінансових платформ.',
            'seo_text_en': 'Professional finance and investment content generator. Create articles, tips, and analysis for financial platforms.',
            'seo_text_es': 'Generador profesional de contenido sobre finanzas e inversiones. Crea artículos, consejos y análisis para plataformas financieras.'
        },
        'business': {
            'uk': 'Бізнес', 'en': 'Business', 'es': 'Negocios', 'icon': '💼',
            'description_uk': 'Створюйте бізнес-контент та стратегії',
            'description_en': 'Create business content and strategies',
            'description_es': 'Crea contenido empresarial y estrategias',
            'seo_text_uk': 'Генератор бізнес-контенту та стратегій. Створюйте статті про управління, підприємництво та корпоративний розвиток.',
            'seo_text_en': 'Business content and strategy generator. Create articles about management, entrepreneurship, and corporate development.',
            'seo_text_es': 'Generador de contenido empresarial y estrategias. Crea artículos sobre gestión, emprendimiento y desarrollo corporativo.'
        },
        'marketing': {
            'uk': 'Маркетинг', 'en': 'Marketing', 'es': 'Marketing', 'icon': '📢',
            'description_uk': 'Створюйте маркетинговий контент та кампанії',
            'description_en': 'Create marketing content and campaigns',
            'description_es': 'Crea contenido de marketing y campañas',
            'seo_text_uk': 'Генератор маркетингового контенту та кампаній. Створюйте стратегії, креативні ідеї та контент для соціальних мереж.',
            'seo_text_en': 'Marketing content and campaign generator. Create strategies, creative ideas, and social media content.',
            'seo_text_es': 'Generador de contenido de marketing y campañas. Crea estrategias, ideas creativas y contenido para redes sociales.'
        },
        'technology': {
            'uk': 'Технології', 'en': 'Technology', 'es': 'Tecnología', 'icon': '💻',
            'description_uk': 'Створюйте технічний контент та огляди',
            'description_en': 'Create technical content and reviews',
            'description_es': 'Crea contenido técnico y reseñas',
            'seo_text_uk': 'Генератор технічного контенту та оглядів. Створюйте статті про технології, програмування та інновації.',
            'seo_text_en': 'Technical content and review generator. Create articles about technology, programming, and innovation.',
            'seo_text_es': 'Generador de contenido técnico y reseñas. Crea artículos sobre tecnología, programación e innovación.'
        },
        'health': {
            'uk': 'Здоров\'я', 'en': 'Health', 'es': 'Salud', 'icon': '🏥',
            'description_uk': 'Створюйте контент про здоров\'я та медицину',
            'description_en': 'Create content about health and medicine',
            'description_es': 'Crea contenido sobre salud y medicina',
            'seo_text_uk': 'Генератор контенту про здоров\'я та медицину. Створюйте інформативні статті про здоров\'я, дієти та медичні теми.',
            'seo_text_en': 'Health and medicine content generator. Create informative articles about health, diets, and medical topics.',
            'seo_text_es': 'Generador de contenido sobre salud y medicina. Crea artículos informativos sobre salud, dietas y temas médicos.'
        },
        'education': {
            'uk': 'Освіта', 'en': 'Education', 'es': 'Educación', 'icon': '🎓',
            'description_uk': 'Створюйте навчальний контент та матеріали',
            'description_en': 'Create educational content and materials',
            'description_es': 'Crea contenido educativo y materiales',
            'seo_text_uk': 'Генератор навчального контенту та матеріалів. Створюйте уроки, курси та освітні ресурси для різних рівнів.',
            'seo_text_en': 'Educational content and materials generator. Create lessons, courses, and educational resources for different levels.',
            'seo_text_es': 'Generador de contenido educativo y materiales. Crea lecciones, cursos y recursos educativos para diferentes niveles.'
        },
        'travel': {
            'uk': 'Подорожі', 'en': 'Travel', 'es': 'Viajes', 'icon': '✈️',
            'description_uk': 'Створюйте контент про подорожі та туризм',
            'description_en': 'Create content about travel and tourism',
            'description_es': 'Crea contenido sobre viajes y turismo',
            'seo_text_uk': 'Генератор контенту про подорожі та туризм. Створюйте путівники, поради та описи туристичних напрямків.',
            'seo_text_en': 'Travel and tourism content generator. Create guides, tips, and descriptions of travel destinations.',
            'seo_text_es': 'Generador de contenido sobre viajes y turismo. Crea guías, consejos y descripciones de destinos turísticos.'
        },
        'food': {
            'uk': 'Їжа та ресторани', 'en': 'Food & Restaurants', 'es': 'Comida y Restaurantes', 'icon': '🍽️',
            'description_uk': 'Створюйте контент про їжу та ресторани',
            'description_en': 'Create content about food and restaurants',
            'description_es': 'Crea contenido sobre comida y restaurantes',
            'seo_text_uk': 'Генератор контенту про їжу та ресторани. Створюйте рецепти, огляди ресторанів та кулінарні статті.',
            'seo_text_en': 'Food and restaurant content generator. Create recipes, restaurant reviews, and culinary articles.',
            'seo_text_es': 'Generador de contenido sobre comida y restaurantes. Crea recetas, reseñas de restaurantes y artículos culinarios.'
        },
        'fitness': {
            'uk': 'Фітнес', 'en': 'Fitness', 'es': 'Fitness', 'icon': '💪',
            'description_uk': 'Створюйте контент про фітнес та тренування',
            'description_en': 'Create content about fitness and training',
            'description_es': 'Crea contenido sobre fitness y entrenamiento',
            'seo_text_uk': 'Генератор контенту про фітнес та тренування. Створюйте програми тренувань, поради та мотиваційний контент.',
            'seo_text_en': 'Fitness and training content generator. Create workout programs, tips, and motivational content.',
            'seo_text_es': 'Generador de contenido sobre fitness y entrenamiento. Crea programas de entrenamiento, consejos y contenido motivacional.'
        },
        'beauty': {
            'uk': 'Краса', 'en': 'Beauty', 'es': 'Belleza', 'icon': '💄',
            'description_uk': 'Створюйте контент про красу та косметику',
            'description_en': 'Create content about beauty and cosmetics',
            'description_es': 'Crea contenido sobre belleza y cosméticos',
            'seo_text_uk': 'Генератор контенту про красу та косметику. Створюйте огляди продуктів, поради з догляду та модні тенденції.',
            'seo_text_en': 'Beauty and cosmetics content generator. Create product reviews, skincare tips, and fashion trends.',
            'seo_text_es': 'Generador de contenido sobre belleza y cosméticos. Crea reseñas de productos, consejos de cuidado de la piel y tendencias de moda.'
        },
        'real-estate': {
            'uk': 'Нерухомість', 'en': 'Real Estate', 'es': 'Bienes Raíces', 'icon': '🏠',
            'description_uk': 'Створюйте контент про нерухомість',
            'description_en': 'Create content about real estate',
            'description_es': 'Crea contenido sobre bienes raíces',
            'seo_text_uk': 'Генератор контенту про нерухомість. Створюйте огляди ринку, поради для інвесторів та описи нерухомості.',
            'seo_text_en': 'Real estate content generator. Create market reviews, investor tips, and property descriptions.',
            'seo_text_es': 'Generador de contenido sobre bienes raíces. Crea reseñas de mercado, consejos para inversores y descripciones de propiedades.'
        },
        'psychology': {
            'uk': 'Психологічна підтримка', 'en': 'Psychological Support', 'es': 'Apoyo Psicológico', 'icon': '🧠',
            'description_uk': 'Створюйте контент про психологію та підтримку',
            'description_en': 'Create content about psychology and support',
            'description_es': 'Crea contenido sobre psicología y apoyo',
            'seo_text_uk': 'Генератор контенту про психологію та підтримку. Створюйте статті про ментальне здоров\'я, стрес та психологічну допомогу.',
            'seo_text_en': 'Psychology and support content generator. Create articles about mental health, stress, and psychological assistance.',
            'seo_text_es': 'Generador de contenido sobre psicología y apoyo. Crea artículos sobre salud mental, estrés y asistencia psicológica.'
        }
    }
    
    tools = []
    for niche_id, niche_info in original_niches_data.items():
        locale_key = locale
        if locale_key not in ['uk', 'en', 'es']:
            locale_key = 'en'
        
        tools.append({
            'id': niche_id,
            'niche': niche_id,
            'tool_name': niche_id,  # Додаємо tool_name для використання /tool/<tool_name> route
            'name': niche_info.get(locale_key, niche_info.get('en', niche_info['uk'])),
            'description': niche_info.get(f'description_{locale_key}', niche_info.get('description_en', '')),
            'icon': niche_info['icon'],
            'seo_text': niche_info.get(f'seo_text_{locale_key}', niche_info.get('seo_text_en', ''))
        })
    
    return tools


def get_creative_tools():
    """Alias for get_personal_creative_tools for /creative/<niche_id> route (same structure: niche, tool_name, name, etc.)."""
    return get_personal_creative_tools()


@main_bp.route('/')
def index():
    """Головна сторінка - Dashboard AI інструментів"""
    business_tools = get_ai_tools()
    personal_creative_tools = get_personal_creative_tools()
    translations = get_translations()
    seo = get_seo_data()
    
    return render_template('index.html', business_tools=business_tools, personal_creative_tools=personal_creative_tools, current_user=current_user, t=translations, seo=seo)

@main_bp.route('/tool/<tool_name>')
def tool_page(tool_name):
    """Сторінка конкретного AI інструменту (Professional AI Tools та Personal & Creative Tools)"""
    # Отримуємо списки інструментів
    business_tools = get_ai_tools()
    personal_creative_tools = get_personal_creative_tools()
    
    # Шукаємо інструмент спочатку в Professional AI Tools
    tool = next((t for t in business_tools if t['tool_name'] == tool_name), None)
    
    # Якщо не знайдено, шукаємо в Personal & Creative Tools
    if not tool:
        tool = next((t for t in personal_creative_tools if t.get('tool_name') == tool_name), None)
        if tool:
            # Якщо знайдено в Personal & Creative Tools, використовуємо цей список для "інші інструменти"
            all_tools = personal_creative_tools
        else:
            flash('Інструмент не знайдено', 'warning')
            return redirect(url_for('main.index'))
    else:
        # Якщо знайдено в Professional AI Tools, використовуємо цей список
        all_tools = business_tools
    
    translations = get_translations()
    seo = get_seo_data()
    
    return render_template('tool.html', tool=tool, tools=all_tools, current_user=current_user, t=translations, seo=seo)

@main_bp.route('/creative/<niche_id>')
def creative_tool_page(niche_id):
    """Сторінка креативного інструменту"""
    # Отримуємо список креативних інструментів
    creative_tools = get_creative_tools()
    tool = next((t for t in creative_tools if t['niche'] == niche_id), None)
    
    if not tool:
        flash('Інструмент не знайдено', 'warning')
        return redirect(url_for('main.index'))
    
    # tool.html expects tool (with .name, .tool_long_description) and/or tool_name
    translations = get_translations()
    seo = get_seo_data()
    return render_template(
        'tool.html',
        tool=tool,
        tool_name=tool['tool_name'],
        tools=creative_tools,
        current_user=current_user,
        t=translations,
        seo=seo,
    )

@main_bp.route('/<language>/tool/<niche_id>')
def old_tool_page(language, niche_id):
    """Старий route для ніш (для зворотної сумісності)"""
    # Встановлюємо мову
    if language in Config.LANGUAGES:
        session['language'] = language
    
    # Перевіряємо чи ніша існує
    niches = get_niches()
    niche = next((n for n in niches if n['id'] == niche_id), None)
    
    if not niche:
        return redirect(url_for('main.index'))
    
    translations = get_translations()
    seo = get_seo_data(niche_id)
    popular_queries = get_popular_queries()
    
    return render_template('tool.html', niche=niche, niches=niches, current_user=current_user, t=translations, seo=seo, popular_queries=popular_queries)

# sitemap.xml and robots.txt: defined on app in app.py (includes blog articles)
# set_language: defined on app in app.py (single route); main no longer defines it

