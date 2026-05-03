"""
Centralized configuration for all AI tools.
Contains tool definitions, translations, and system prompts.
"""

# System prompts for each tool (professional persona and output format)
TOOL_SYSTEM_PROMPTS = {
    # Professional AI Tools
    'amazon': 'Expert Amazon Copywriter. Focus on high-volume keywords, bullet points with benefits, and compliance with Amazon TOS.',
    'shopify': 'E-commerce conversion expert. Use the AIDA formula and HTML formatting for clean product pages.',
    'etsy': 'Etsy SEO Guru. Generate a 140-char keyword-rich title and 13 relevant tags.',
    'resume': 'Professional HR Recruiter. Optimize the resume for ATS systems using industry-specific action verbs.',
    'kdp': 'Amazon KDP Consultant. Generate profitable niche titles, subtitles, and backend keywords for self-publishing.',
    'youtube-script': 'Viral Video Strategist. Provide a script with a hook, retention-focused body, and CTA.',
    'tiktok-hook': 'Social Media Growth Expert. Create 5 high-curiosity hooks for short-form video.',
    'google-ads': 'PPC Specialist. Write compelling ad copies with high CTR, focusing on headlines and descriptions.',

    # Personal & Creative Tools
    'finance': 'Financial Advisor. Provide structured advice on budgeting, investing, or tax optimization based on user input.',
    'business': 'Business Strategy Consultant. Help with business plans, SWOT analysis, and scaling strategies.',
    'marketing': 'Marketing Director. Create comprehensive 360-degree marketing strategies for brands.',
    'technology': 'Tech Lead & Architect. Explain complex technical concepts simply and provide architectural advice.',
    'health': 'Health & Wellness Coach. Provide general advice on healthy lifestyle, nutrition, and habits. Always add a medical disclaimer.',
    'education': 'Professional Educator. Create lesson plans, summaries, or study guides for any subject.',
    'travel': 'Travel Agent. Create detailed itineraries, destination guides, and travel tips.',
    'food': 'Culinary Expert. Provide recipes, restaurant review templates, or menu descriptions.',
    'fitness': 'Certified Personal Trainer. Design workout routines and motivation strategies.',
    'beauty': 'Beauty & Cosmetics Specialist. Advise on skincare routines, makeup trends, and product reviews.',
    'real-estate': 'Real Estate Professional. Write property descriptions and investment analysis.',
    'psychology': 'Empathetic Counselor. Provide supportive advice and mental health coping strategies. Always add a professional help disclaimer.'
}

# Tool definitions with Ukrainian and English translations
TOOLS_CONFIG = {
    # Professional AI Tools (8 tools)
    'amazon': {
        'category': 'Professional',
        'tool_name': 'amazon',
        'uk': {
            'name': 'Amazon Listing Optimizer',
            'description': 'Оптимізуйте описи товарів для Amazon з SEO-ключовими словами',
            'seo_text': 'Професійний інструмент для оптимізації продуктів Amazon. Створюйте SEO-оптимізовані описи, які максимізують видимість та конверсію.',
            'seo_title': 'Amazon Listing Optimizer - SEO Оптимізація Товарів | AI Генератор',
            'meta_description': 'Оптимізуйте описи товарів для Amazon з AI. Створюйте SEO-оптимізовані листинги, які максимізують видимість та продажі на Amazon.',
            'keywords': 'amazon оптимізація, amazon seo, опис товару amazon, amazon листинг, ai генератор amazon',
            'tool_long_description': 'Amazon Listing Optimizer - це професійний AI-інструмент для створення та оптимізації описів товарів на Amazon. Чому використовувати AI для цього завдання? Amazon має мільйони товарів, і щоб ваш продукт виділявся, потрібні професійні описи з правильними ключовими словами, які максимізують видимість у пошуку та конверсію. Ручне написання таких описів займає багато часу та вимагає глибоких знань SEO. AI може проаналізувати ваш продукт, конкурентів та ринкові тенденції, щоб створити оптимізований контент за секунди. Як отримати найкращі результати? Надайте детальну інформацію про ваш продукт: назву, основні характеристики, переваги, цільову аудиторію та ключові слова. AI створить професійний опис з оптимальною структурою, ключовими словами та переконливим текстом, який мотивує покупців до дії та покращує ваші продажі на Amazon.'
        },
        'en': {
            'name': 'Amazon Listing Optimizer',
            'description': 'Optimize product listings for Amazon with SEO keywords',
            'seo_text': 'Professional tool for Amazon product optimization. Create SEO-optimized listings that maximize visibility and conversion.',
            'seo_title': 'Amazon Listing Optimizer - SEO Product Optimization | AI Generator',
            'meta_description': 'Optimize Amazon product listings with AI. Create SEO-optimized listings that maximize visibility and sales on Amazon.',
            'keywords': 'amazon optimization, amazon seo, amazon product description, amazon listing, ai generator amazon',
            'tool_long_description': 'Amazon Listing Optimizer is a professional AI tool for creating and optimizing Amazon product listings. Why use AI for this task? Amazon has millions of products, and to make yours stand out, you need professional descriptions with the right keywords that maximize search visibility and conversion. Manually writing such descriptions takes a lot of time and requires deep SEO knowledge. AI can analyze your product, competitors, and market trends to create optimized content in seconds. How to get the best results? Provide detailed information about your product: name, key features, benefits, target audience, and keywords. AI will create a professional description with optimal structure, keywords, and compelling text that motivates buyers to action and improves your Amazon sales.'
        },
        'icon': '📦'
    },
    'shopify': {
        'category': 'Professional',
        'tool_name': 'shopify',
        'uk': {
            'name': 'Shopify Description Generator',
            'description': 'Створюйте переконливі описи продуктів для Shopify',
            'seo_text': 'Генератор описів продуктів для Shopify. Створюйте переконливі, продаючі тексти, які мотивують покупців до дії.',
            'seo_title': 'Shopify Description Generator - AI Генератор Описів Продуктів',
            'meta_description': 'Створюйте переконливі описи продуктів для Shopify з AI. Генератор продаючих текстів, які мотивують покупців до дії.',
            'keywords': 'shopify опис продукту, shopify генератор, ai shopify, опис товару shopify, shopify seo',
            'tool_long_description': 'Shopify Description Generator - це потужний AI-інструмент для створення професійних описів продуктів для вашого Shopify магазину. Чому використовувати AI? Ефективні описи продуктів - це ключ до конверсії. Вони повинні бути переконливими, інформативними та мотивувати покупців до дії. Написання таких текстів вручну займає багато часу, особливо якщо у вас багато продуктів. AI може проаналізувати ваш продукт та створити унікальний, продаючий опис, який підкреслює переваги та мотивує покупців. Як отримати найкращі результати? Надайте детальну інформацію: назву продукту, основні характеристики, переваги, цільову аудиторію та стиль написання. AI створить професійний опис з правильною структурою, переконливими аргументами та призивом до дії, який збільшить ваші продажі на Shopify.'
        },
        'en': {
            'name': 'Shopify Description Generator',
            'description': 'Create compelling product descriptions for Shopify',
            'seo_text': 'Shopify product description generator. Create compelling, sales-focused texts that motivate buyers to action.',
            'seo_title': 'Shopify Description Generator - AI Product Description Tool',
            'meta_description': 'Create compelling Shopify product descriptions with AI. Generate sales-focused texts that motivate buyers to action.',
            'keywords': 'shopify product description, shopify generator, ai shopify, shopify product copy, shopify seo',
            'tool_long_description': 'Shopify Description Generator is a powerful AI tool for creating professional product descriptions for your Shopify store. Why use AI? Effective product descriptions are key to conversion. They need to be compelling, informative, and motivate buyers to action. Writing such texts manually takes a lot of time, especially if you have many products. AI can analyze your product and create a unique, sales-focused description that highlights benefits and motivates buyers. How to get the best results? Provide detailed information: product name, key features, benefits, target audience, and writing style. AI will create a professional description with proper structure, compelling arguments, and a call to action that will increase your Shopify sales.'
        },
        'icon': '🛍️'
    },
    'etsy': {
        'category': 'Professional',
        'tool_name': 'etsy',
        'uk': {
            'name': 'Etsy SEO Title Generator',
            'description': 'Генеруйте SEO-оптимізовані заголовки для Etsy',
            'seo_text': 'Генератор SEO заголовків для Etsy. Створюйте оптимізовані заголовки, які максимізують видимість в пошуку Etsy.',
            'seo_title': 'Etsy SEO Title Generator - AI Генератор Заголовків для Etsy',
            'meta_description': 'Генеруйте SEO-оптимізовані заголовки для Etsy з AI. Максимізуйте видимість ваших товарів у пошуку Etsy.',
            'keywords': 'etsy seo, etsy заголовок, etsy оптимізація, ai etsy, etsy генератор',
            'tool_long_description': 'Etsy SEO Title Generator - це спеціалізований AI-інструмент для створення SEO-оптимізованих заголовків для ваших товарів на Etsy. Чому використовувати AI? Etsy має унікальну систему пошуку, де заголовок товару є критично важливим для видимості. Правильний заголовок з ключовими словами може значно збільшити кількість переглядів та продажів. Ручне створення таких заголовків вимагає знання SEO та ринкових тенденцій. AI може проаналізувати ваш продукт, категорію та популярні ключові слова, щоб створити оптимальний заголовок. Як отримати найкращі результати? Надайте інформацію про ваш товар: назву, категорію, матеріали, стиль, цільову аудиторію. AI створить SEO-оптимізований заголовок, який використовує всі 140 символів максимально ефективно, включає релевантні ключові слова та привертає увагу покупців, що збільшить вашу видимість та продажі на Etsy.'
        },
        'en': {
            'name': 'Etsy SEO Title Generator',
            'description': 'Generate SEO-optimized titles for Etsy listings',
            'seo_text': 'Etsy SEO title generator. Create optimized titles that maximize visibility in Etsy search results.',
            'seo_title': 'Etsy SEO Title Generator - AI Title Generator for Etsy',
            'meta_description': 'Generate SEO-optimized Etsy titles with AI. Maximize visibility of your products in Etsy search.',
            'keywords': 'etsy seo, etsy title, etsy optimization, ai etsy, etsy generator',
            'tool_long_description': 'Etsy SEO Title Generator is a specialized AI tool for creating SEO-optimized titles for your Etsy listings. Why use AI? Etsy has a unique search system where the product title is critical for visibility. The right title with keywords can significantly increase views and sales. Manually creating such titles requires SEO knowledge and market trends. AI can analyze your product, category, and popular keywords to create an optimal title. How to get the best results? Provide information about your product: name, category, materials, style, target audience. AI will create an SEO-optimized title that uses all 140 characters most effectively, includes relevant keywords, and attracts buyers, which will increase your visibility and sales on Etsy.'
        },
        'icon': '🎨'
    },
    'resume': {
        'category': 'Professional',
        'tool_name': 'resume',
        'uk': {
            'name': 'Resume Keyword Optimizer',
            'description': 'Оптимізуйте резюме з ключовими словами для ATS систем',
            'seo_text': 'Оптимізатор резюме для ATS систем. Аналізуйте вакансії та оптимізуйте резюме з релевантними ключовими словами.',
            'seo_title': 'Resume Keyword Optimizer - AI Оптимізація Резюме для ATS',
            'meta_description': 'Оптимізуйте резюме з AI для ATS систем. Аналізуйте вакансії та додавайте релевантні ключові слова для проходження фільтрів.',
            'keywords': 'ats резюме, оптимізація резюме, ключові слова резюме, ai резюме, резюме seo',
            'tool_long_description': 'Resume Keyword Optimizer - це професійний AI-інструмент для оптимізації резюме під системи ATS (Applicant Tracking Systems). Чому використовувати AI? Більшість компаній використовують ATS для фільтрації резюме перед тим, як вони потрапляють до рекрутерів. Якщо ваше резюме не містить правильних ключових слів з опису вакансії, воно може бути відхилено автоматично, навіть якщо ви ідеальний кандидат. Ручна оптимізація вимагає глибокого розуміння ATS та аналізу кожної вакансії. AI може проаналізувати опис вакансії та ваше резюме, щоб визначити ключові слова та оптимізувати контент. Як отримати найкращі результати? Надайте ваше поточне резюме та опис вакансії, на яку ви претендуєте. AI проаналізує обидва документи, визначить ключові слова, навички та кваліфікації, які потрібно підкреслити, та оптимізує ваше резюме для максимальної сумісності з ATS, що збільшить ваші шанси отримати запрошення на співбесіду.'
        },
        'en': {
            'name': 'Resume Keyword Optimizer',
            'description': 'Optimize resumes with keywords for ATS systems',
            'seo_text': 'Resume optimizer for ATS systems. Analyze job descriptions and optimize resumes with relevant keywords.',
            'seo_title': 'Resume Keyword Optimizer - AI Resume Optimization for ATS',
            'meta_description': 'Optimize your resume with AI for ATS systems. Analyze job descriptions and add relevant keywords to pass filters.',
            'keywords': 'ats resume, resume optimization, resume keywords, ai resume, resume seo',
            'tool_long_description': 'Resume Keyword Optimizer is a professional AI tool for optimizing resumes for ATS (Applicant Tracking Systems). Why use AI? Most companies use ATS to filter resumes before they reach recruiters. If your resume doesn\'t contain the right keywords from the job description, it may be automatically rejected, even if you\'re the perfect candidate. Manual optimization requires deep understanding of ATS and analysis of each job posting. AI can analyze the job description and your resume to identify keywords and optimize content. How to get the best results? Provide your current resume and the job description you\'re applying for. AI will analyze both documents, identify keywords, skills, and qualifications to highlight, and optimize your resume for maximum ATS compatibility, increasing your chances of getting an interview invitation.'
        },
        'icon': '📄'
    },
    'kdp': {
        'category': 'Professional',
        'tool_name': 'kdp',
        'uk': {
            'name': 'KDP (Kindle Direct Publishing)',
            'description': 'Створюйте контент для Kindle Direct Publishing',
            'seo_text': 'Професійний інструмент для створення контенту для Kindle Direct Publishing. Створюйте описи книг, ключові слова та маркетингові матеріали.',
            'seo_title': 'KDP Content Generator - AI Генератор для Kindle Direct Publishing',
            'meta_description': 'Створюйте професійний контент для KDP з AI. Генератор описів книг, ключових слів та маркетингових матеріалів для Kindle.',
            'keywords': 'kdp генератор, kindle опис, kdp ключові слова, ai kdp, kindle publishing',
            'tool_long_description': 'KDP Content Generator - це спеціалізований AI-інструмент для створення професійного контенту для Kindle Direct Publishing. Чому використовувати AI? Успішна публікація на Amazon KDP залежить від якості опису книги, правильних ключових слів та маркетингових матеріалів. Ці елементи впливають на видимість вашої книги в пошуку Amazon та на рішення читачів про покупку. Ручне створення таких матеріалів вимагає знань маркетингу та SEO. AI може проаналізувати жанр вашої книги, цільову аудиторію та конкурентів, щоб створити оптимізований контент. Як отримати найкращі результати? Надайте інформацію про вашу книгу: назву, жанр, сюжет, цільову аудиторію, подібні книги. AI створить переконливий опис книги, релевантні ключові слова для Amazon, маркетингові теги та рекомендації, які максимізують видимість та продажі вашої книги на Kindle.'
        },
        'en': {
            'name': 'KDP (Kindle Direct Publishing)',
            'description': 'Create content for Kindle Direct Publishing',
            'seo_text': 'Professional tool for creating content for Kindle Direct Publishing. Create book descriptions, keywords, and marketing materials.',
            'seo_title': 'KDP Content Generator - AI Generator for Kindle Direct Publishing',
            'meta_description': 'Create professional KDP content with AI. Generate book descriptions, keywords, and marketing materials for Kindle.',
            'keywords': 'kdp generator, kindle description, kdp keywords, ai kdp, kindle publishing',
            'tool_long_description': 'KDP Content Generator is a specialized AI tool for creating professional content for Kindle Direct Publishing. Why use AI? Successful publishing on Amazon KDP depends on the quality of your book description, the right keywords, and marketing materials. These elements affect your book\'s visibility in Amazon search and readers\' purchase decisions. Manually creating such materials requires marketing and SEO knowledge. AI can analyze your book\'s genre, target audience, and competitors to create optimized content. How to get the best results? Provide information about your book: title, genre, plot, target audience, similar books. AI will create a compelling book description, relevant keywords for Amazon, marketing tags, and recommendations that maximize your book\'s visibility and sales on Kindle.'
        },
        'icon': '📚'
    },
    'youtube-script': {
        'category': 'Professional',
        'tool_name': 'youtube-script',
        'uk': {
            'name': 'YouTube Script Writer',
            'description': 'Створюйте професійні сценарії для YouTube відео',
            'seo_text': 'Професійний генератор сценаріїв для YouTube. Створюйте залучуючі, структуровані сценарії, які максимізують утримання аудиторії та engagement.',
            'seo_title': 'YouTube Script Writer - AI Генератор Сценаріїв для YouTube',
            'meta_description': 'Створюйте професійні сценарії для YouTube з AI. Генератор залучуючих сценаріїв, які максимізують утримання аудиторії та перегляди.',
            'keywords': 'youtube сценарій, youtube скрипт, ai youtube, генератор сценаріїв, youtube контент',
            'tool_long_description': 'YouTube Script Writer - це потужний AI-інструмент для створення професійних сценаріїв для ваших YouTube відео. Чому використовувати AI? Якісний сценарій - це основа успішного YouTube відео. Він визначає структуру, залучення аудиторії, утримання переглядів та загальну якість контенту. Написання ефективного сценарію вручну займає багато часу та вимагає знань про структуру відео, хуки, переходи та призиви до дії. AI може проаналізувати вашу тему, цільову аудиторію та формат, щоб створити структурований сценарій з оптимальним flow. Як отримати найкращі результати? Надайте детальну інформацію: тему відео, цільову аудиторію, тривалість, стиль (освітній, розважальний, огляд), ключові моменти для розкриття. AI створить професійний сценарій з сильним хуком на початку, чіткою структурою, переходами між секціями, призивом до дії та рекомендаціями для візуальних елементів, що збільшить утримання аудиторії та перегляди вашого відео.'
        },
        'en': {
            'name': 'YouTube Script Writer',
            'description': 'Create professional scripts for YouTube videos',
            'seo_text': 'Professional YouTube script generator. Create engaging, structured scripts that maximize audience retention and engagement.',
            'seo_title': 'YouTube Script Writer - AI Script Generator for YouTube',
            'meta_description': 'Create professional YouTube scripts with AI. Generate engaging scripts that maximize audience retention and views.',
            'keywords': 'youtube script, youtube screenplay, ai youtube, script generator, youtube content',
            'tool_long_description': 'YouTube Script Writer is a powerful AI tool for creating professional scripts for your YouTube videos. Why use AI? A quality script is the foundation of a successful YouTube video. It determines structure, audience engagement, view retention, and overall content quality. Writing an effective script manually takes a lot of time and requires knowledge of video structure, hooks, transitions, and calls to action. AI can analyze your topic, target audience, and format to create a structured script with optimal flow. How to get the best results? Provide detailed information: video topic, target audience, duration, style (educational, entertaining, review), key points to cover. AI will create a professional script with a strong hook at the beginning, clear structure, transitions between sections, call to action, and recommendations for visual elements, which will increase audience retention and views of your video.'
        },
        'icon': '🎬'
    },
    'tiktok-hook': {
        'category': 'Professional',
        'tool_name': 'tiktok-hook',
        'uk': {
            'name': 'TikTok Hook Generator',
            'description': 'Генеруйте залучуючі хуки для TikTok відео',
            'seo_text': 'Генератор хуків для TikTok. Створюйте привабливі перші секунди, які максимізують перегляд та engagement на TikTok.',
            'seo_title': 'TikTok Hook Generator - AI Генератор Хуків для TikTok',
            'meta_description': 'Генеруйте залучуючі хуки для TikTok з AI. Створюйте привабливі перші секунди, які максимізують перегляди та engagement.',
            'keywords': 'tiktok хук, tiktok генератор, ai tiktok, tiktok контент, tiktok вірус',
            'tool_long_description': 'TikTok Hook Generator - це спеціалізований AI-інструмент для створення залучуючих хуків для ваших TikTok відео. Чому використовувати AI? На TikTok перші 3 секунди визначають успіх відео. Якщо хук не зацікавить глядача, він прокрутить далі, і алгоритм TikTok знизить покази вашого відео. Створення ефективного хуку вимагає розуміння психології, трендів та формату платформи. AI може проаналізувати вашу тему, цільову аудиторію та поточні тренди, щоб створити хук, який миттєво привертає увагу. Як отримати найкращі результати? Надайте інформацію про ваше відео: тему, цільову аудиторію, стиль (освітній, розважальний, лайфстайл), ключове повідомлення. AI створить кілька варіантів хуків з різними підходами: питання, контроверсійна думка, обіцянка цінності, емоційний тригер, які максимізують шанси на вірус та збільшують перегляди та engagement на TikTok.'
        },
        'en': {
            'name': 'TikTok Hook Generator',
            'description': 'Generate engaging hooks for TikTok videos',
            'seo_text': 'TikTok hook generator. Create compelling opening seconds that maximize views and engagement on TikTok.',
            'seo_title': 'TikTok Hook Generator - AI Hook Generator for TikTok',
            'meta_description': 'Generate engaging TikTok hooks with AI. Create compelling opening seconds that maximize views and engagement.',
            'keywords': 'tiktok hook, tiktok generator, ai tiktok, tiktok content, tiktok viral',
            'tool_long_description': 'TikTok Hook Generator is a specialized AI tool for creating engaging hooks for your TikTok videos. Why use AI? On TikTok, the first 3 seconds determine video success. If the hook doesn\'t capture the viewer\'s attention, they\'ll scroll away, and TikTok\'s algorithm will reduce your video\'s reach. Creating an effective hook requires understanding psychology, trends, and platform format. AI can analyze your topic, target audience, and current trends to create a hook that instantly grabs attention. How to get the best results? Provide information about your video: topic, target audience, style (educational, entertaining, lifestyle), key message. AI will create multiple hook variations with different approaches: questions, controversial statements, value promises, emotional triggers, which maximize the chances of going viral and increase views and engagement on TikTok.'
        },
        'icon': '🎵'
    },
    'google-ads': {
        'category': 'Professional',
        'tool_name': 'google-ads',
        'uk': {
            'name': 'Google Ads Copywriter',
            'description': 'Створюйте переконливі тексти для Google Ads',
            'seo_text': 'Професійний копірайтер для Google Ads. Створюйте оптимізовані оголошення, які максимізують CTR та конверсію.',
            'seo_title': 'Google Ads Copywriter - AI Генератор Текстів для Google Ads',
            'meta_description': 'Створюйте переконливі тексти для Google Ads з AI. Генератор оптимізованих оголошень, які максимізують CTR та конверсію.',
            'keywords': 'google ads текст, google ads копірайтер, ai google ads, google ads оптимізація, ppc реклама',
            'tool_long_description': 'Google Ads Copywriter - це професійний AI-інструмент для створення ефективних текстів для Google Ads кампаній. Чому використовувати AI? Успішна Google Ads кампанія залежить від якості тексту оголошення. Правильний текст може значно підвищити CTR (click-through rate) та конверсію, зменшуючи вартість кліку та збільшуючи ROI. Написання таких текстів вручну вимагає знань про копірайтинг, психологію покупців та специфіку Google Ads. AI може проаналізувати ваш продукт, цільову аудиторію та конкурентів, щоб створити оптимізований текст. Як отримати найкращі результати? Надайте детальну інформацію: продукт/послуга, унікальні переваги, цільова аудиторія, ключові слова, стиль (формальний/неформальний). AI створить кілька варіантів текстів для заголовків та описів з оптимальною довжиною, переконливими аргументами, призивом до дії та релевантними ключовими словами, які максимізують CTR та конверсію ваших Google Ads кампаній.'
        },
        'en': {
            'name': 'Google Ads Copywriter',
            'description': 'Create compelling copy for Google Ads',
            'seo_text': 'Professional Google Ads copywriter. Create optimized ads that maximize CTR and conversion rates.',
            'seo_title': 'Google Ads Copywriter - AI Copy Generator for Google Ads',
            'meta_description': 'Create compelling Google Ads copy with AI. Generate optimized ads that maximize CTR and conversion.',
            'keywords': 'google ads copy, google ads copywriter, ai google ads, google ads optimization, ppc advertising',
            'tool_long_description': 'Google Ads Copywriter is a professional AI tool for creating effective copy for Google Ads campaigns. Why use AI? A successful Google Ads campaign depends on ad copy quality. The right copy can significantly increase CTR (click-through rate) and conversion, reducing cost per click and increasing ROI. Writing such copy manually requires knowledge of copywriting, buyer psychology, and Google Ads specifics. AI can analyze your product, target audience, and competitors to create optimized copy. How to get the best results? Provide detailed information: product/service, unique benefits, target audience, keywords, style (formal/informal). AI will create multiple variations of headlines and descriptions with optimal length, compelling arguments, call to action, and relevant keywords that maximize CTR and conversion of your Google Ads campaigns.'
        },
        'icon': '📊'
    },
    
    # Personal & Creative Tools (12 tools)
    'finance': {
        'category': 'Personal',
        'tool_name': 'finance',
        'uk': {
            'name': 'Фінанси',
            'description': 'Створюйте контент про фінанси, інвестиції та економіку',
            'seo_text': 'Професійний генератор контенту про фінанси та інвестиції. Створюйте статті, поради та аналітику для фінансових платформ.',
            'seo_title': 'Фінансовий Контент Генератор - AI Створення Контенту про Фінанси',
            'meta_description': 'Створюйте професійний контент про фінанси, інвестиції та економіку з AI. Генератор статей, порад та аналітики для фінансових платформ.',
            'keywords': 'фінансовий контент, інвестиції контент, ai фінанси, фінансові статті, економіка контент',
            'tool_long_description': 'Фінансовий Контент Генератор - це професійний AI-інструмент для створення якісного контенту про фінанси, інвестиції та економіку. Чому використовувати AI? Фінансовий контент вимагає точності, актуальності та професійного підходу. Написання таких статей вручну займає багато часу та вимагає глибоких знань у фінансовій сфері. AI може проаналізувати ринкові тенденції, економічні дані та створити структурований, інформативний контент. Як отримати найкращі результати? Надайте тему, цільову аудиторію, стиль (освітній, аналітичний, практичні поради), ключові моменти для розкриття. AI створить професійний контент з правильною структурою, актуальними даними, практичними порадами та зрозумілими поясненнями складних фінансових концепцій, який буде корисним для ваших читачів та покращить вашу експертність у фінансовій сфері.'
        },
        'en': {
            'name': 'Finance',
            'description': 'Create content about finance, investments and economics',
            'seo_text': 'Professional finance and investment content generator. Create articles, tips, and analysis for financial platforms.',
            'seo_title': 'Finance Content Generator - AI Finance Content Creation',
            'meta_description': 'Create professional finance, investment, and economics content with AI. Generate articles, tips, and analysis for financial platforms.',
            'keywords': 'finance content, investment content, ai finance, financial articles, economics content',
            'tool_long_description': 'Finance Content Generator is a professional AI tool for creating quality content about finance, investments, and economics. Why use AI? Financial content requires accuracy, relevance, and a professional approach. Writing such articles manually takes a lot of time and requires deep knowledge in finance. AI can analyze market trends, economic data, and create structured, informative content. How to get the best results? Provide the topic, target audience, style (educational, analytical, practical tips), key points to cover. AI will create professional content with proper structure, current data, practical advice, and clear explanations of complex financial concepts that will be useful for your readers and improve your expertise in finance.'
        },
        'icon': '💰'
    },
    'business': {
        'category': 'Personal',
        'tool_name': 'business',
        'uk': {
            'name': 'Бізнес',
            'description': 'Створюйте бізнес-контент та стратегії',
            'seo_text': 'Генератор бізнес-контенту та стратегій. Створюйте статті про управління, підприємництво та корпоративний розвиток.',
            'seo_title': 'Бізнес Контент Генератор - AI Створення Бізнес Стратегій',
            'meta_description': 'Створюйте професійний бізнес-контент та стратегії з AI. Генератор статей про управління, підприємництво та корпоративний розвиток.',
            'keywords': 'бізнес контент, бізнес стратегії, ai бізнес, управління контент, підприємництво',
            'tool_long_description': 'Бізнес Контент Генератор - це потужний AI-інструмент для створення професійного бізнес-контенту та стратегій. Чому використовувати AI? Якісний бізнес-контент допомагає будувати експертність, привертати клієнтів та розвивати бізнес. Написання таких матеріалів вручну вимагає часу та знань у різних сферах бізнесу. AI може проаналізувати вашу тему, цільову аудиторію та створити структурований контент з практичними порадами. Як отримати найкращі результати? Надайте тему, тип контенту (стратегія, кейс, поради, аналіз), цільову аудиторію, стиль. AI створить професійний бізнес-контент з чіткою структурою, практичними рекомендаціями, прикладами та actionable insights, який допоможе вашій аудиторії та зміцнить вашу позицію як бізнес-експерта.'
        },
        'en': {
            'name': 'Business',
            'description': 'Create business content and strategies',
            'seo_text': 'Business content and strategy generator. Create articles about management, entrepreneurship, and corporate development.',
            'seo_title': 'Business Content Generator - AI Business Strategy Creation',
            'meta_description': 'Create professional business content and strategies with AI. Generate articles about management, entrepreneurship, and corporate development.',
            'keywords': 'business content, business strategies, ai business, management content, entrepreneurship',
            'tool_long_description': 'Business Content Generator is a powerful AI tool for creating professional business content and strategies. Why use AI? Quality business content helps build expertise, attract clients, and grow business. Writing such materials manually requires time and knowledge across various business areas. AI can analyze your topic, target audience, and create structured content with practical advice. How to get the best results? Provide the topic, content type (strategy, case study, tips, analysis), target audience, style. AI will create professional business content with clear structure, practical recommendations, examples, and actionable insights that will help your audience and strengthen your position as a business expert.'
        },
        'icon': '💼'
    },
    'marketing': {
        'category': 'Personal',
        'tool_name': 'marketing',
        'uk': {
            'name': 'Маркетинг',
            'description': 'Створюйте маркетинговий контент та кампанії',
            'seo_text': 'Генератор маркетингового контенту та кампаній. Створюйте стратегії, креативні ідеї та контент для соціальних мереж.',
            'seo_title': 'Маркетинговий Контент Генератор - AI Створення Маркетингових Кампаній',
            'meta_description': 'Створюйте професійний маркетинговий контент та кампанії з AI. Генератор стратегій, креативних ідей та контенту для соціальних мереж.',
            'keywords': 'маркетинговий контент, маркетингові кампанії, ai маркетинг, smm контент, маркетингові стратегії',
            'tool_long_description': 'Маркетинговий Контент Генератор - це професійний AI-інструмент для створення ефективного маркетингового контенту та кампаній. Чому використовувати AI? Успішний маркетинг потребує постійного створення якісного контенту для різних каналів: соціальні мережі, email, блоги, реклама. Ручне створення такого контенту займає багато часу та ресурсів. AI може проаналізувати вашу цільову аудиторію, канал комунікації та створити релевантний, залучуючий контент. Як отримати найкращі результати? Надайте інформацію: тип кампанії, цільова аудиторія, канал (Instagram, Facebook, email, блог), мета (підвищення впізнаваності, продажі, engagement), ключові повідомлення. AI створить маркетинговий контент з правильним тоном, структурою, призивом до дії та рекомендаціями для візуальних елементів, який максимізує ефективність ваших маркетингових кампаній.'
        },
        'en': {
            'name': 'Marketing',
            'description': 'Create marketing content and campaigns',
            'seo_text': 'Marketing content and campaign generator. Create strategies, creative ideas, and social media content.',
            'seo_title': 'Marketing Content Generator - AI Marketing Campaign Creation',
            'meta_description': 'Create professional marketing content and campaigns with AI. Generate strategies, creative ideas, and social media content.',
            'keywords': 'marketing content, marketing campaigns, ai marketing, smm content, marketing strategies',
            'tool_long_description': 'Marketing Content Generator is a professional AI tool for creating effective marketing content and campaigns. Why use AI? Successful marketing requires constant creation of quality content for various channels: social media, email, blogs, advertising. Manually creating such content takes a lot of time and resources. AI can analyze your target audience, communication channel, and create relevant, engaging content. How to get the best results? Provide information: campaign type, target audience, channel (Instagram, Facebook, email, blog), goal (brand awareness, sales, engagement), key messages. AI will create marketing content with the right tone, structure, call to action, and recommendations for visual elements that maximize the effectiveness of your marketing campaigns.'
        },
        'icon': '📢'
    },
    'technology': {
        'category': 'Personal',
        'tool_name': 'technology',
        'uk': {
            'name': 'Технології',
            'description': 'Створюйте технічний контент та огляди',
            'seo_text': 'Генератор технічного контенту та оглядів. Створюйте статті про технології, програмування та інновації.',
            'seo_title': 'Технологічний Контент Генератор - AI Створення Технічного Контенту',
            'meta_description': 'Створюйте професійний технічний контент та огляди з AI. Генератор статей про технології, програмування та інновації.',
            'keywords': 'технічний контент, технології статті, ai технології, програмування контент, tech огляди',
            'tool_long_description': 'Технологічний Контент Генератор - це професійний AI-інструмент для створення якісного технічного контенту та оглядів. Чому використовувати AI? Технологічний контент потребує актуальності, точності та зрозумілого пояснення складних концепцій. Написання таких статей вручну займає багато часу та вимагає глибоких технічних знань. AI може проаналізувати технологію, створити структурований контент та пояснити складні концепції доступною мовою. Як отримати найкращі результати? Надайте тему, тип контенту (огляд, туторіал, новини, аналіз), цільову аудиторію (початківці/експерти), ключові моменти. AI створить технічний контент з правильною структурою, актуальною інформацією, прикладами коду (якщо потрібно) та зрозумілими поясненнями, який буде корисним для ваших читачів та покращить вашу експертність у технологічній сфері.'
        },
        'en': {
            'name': 'Technology',
            'description': 'Create technical content and reviews',
            'seo_text': 'Technical content and review generator. Create articles about technology, programming, and innovation.',
            'seo_title': 'Technology Content Generator - AI Technical Content Creation',
            'meta_description': 'Create professional technical content and reviews with AI. Generate articles about technology, programming, and innovation.',
            'keywords': 'technical content, technology articles, ai technology, programming content, tech reviews',
            'tool_long_description': 'Technology Content Generator is a professional AI tool for creating quality technical content and reviews. Why use AI? Technology content requires relevance, accuracy, and clear explanation of complex concepts. Writing such articles manually takes a lot of time and requires deep technical knowledge. AI can analyze technology, create structured content, and explain complex concepts in accessible language. How to get the best results? Provide the topic, content type (review, tutorial, news, analysis), target audience (beginners/experts), key points. AI will create technical content with proper structure, current information, code examples (if needed), and clear explanations that will be useful for your readers and improve your expertise in technology.'
        },
        'icon': '💻'
    },
    'health': {
        'category': 'Personal',
        'tool_name': 'health',
        'uk': {
            'name': 'Здоров\'я',
            'description': 'Створюйте контент про здоров\'я та медицину',
            'seo_text': 'Генератор контенту про здоров\'я та медицину. Створюйте інформативні статті про здоров\'я, дієти та медичні теми.',
            'seo_title': 'Контент про Здоров\'я Генератор - AI Створення Медичного Контенту',
            'meta_description': 'Створюйте інформативний контент про здоров\'я та медицину з AI. Генератор статей про здоров\'я, дієти та медичні теми.',
            'keywords': 'здоров\'я контент, медичний контент, ai здоров\'я, дієти статті, медицина контент',
            'tool_long_description': 'Контент про Здоров\'я Генератор - це професійний AI-інструмент для створення інформативного контенту про здоров\'я та медицину. Чому використовувати AI? Контент про здоров\'я потребує точності, наукової обґрунтованості та доступного пояснення. Написання таких статей вручну вимагає часу та медичних знань. AI може проаналізувати тему, створити структурований контент з актуальною інформацією та практичними порадами. Як отримати найкращі результати? Надайте тему, тип контенту (інформативний, поради, дієта, вправи), цільову аудиторію, стиль. AI створить контент про здоров\'я з правильною структурою, науково обґрунтованою інформацією, практичними рекомендаціями та зрозумілими поясненнями, який буде корисним та безпечним для ваших читачів.'
        },
        'en': {
            'name': 'Health',
            'description': 'Create content about health and medicine',
            'seo_text': 'Health and medicine content generator. Create informative articles about health, diets, and medical topics.',
            'seo_title': 'Health Content Generator - AI Medical Content Creation',
            'meta_description': 'Create informative health and medicine content with AI. Generate articles about health, diets, and medical topics.',
            'keywords': 'health content, medical content, ai health, diet articles, medicine content',
            'tool_long_description': 'Health Content Generator is a professional AI tool for creating informative content about health and medicine. Why use AI? Health content requires accuracy, scientific validity, and accessible explanation. Writing such articles manually requires time and medical knowledge. AI can analyze the topic, create structured content with current information and practical advice. How to get the best results? Provide the topic, content type (informative, tips, diet, exercises), target audience, style. AI will create health content with proper structure, scientifically grounded information, practical recommendations, and clear explanations that will be useful and safe for your readers.'
        },
        'icon': '🏥'
    },
    'education': {
        'category': 'Personal',
        'tool_name': 'education',
        'uk': {
            'name': 'Освіта',
            'description': 'Створюйте навчальний контент та матеріали',
            'seo_text': 'Генератор навчального контенту та матеріалів. Створюйте уроки, курси та освітні ресурси для різних рівнів.',
            'seo_title': 'Освітній Контент Генератор - AI Створення Навчальних Матеріалів',
            'meta_description': 'Створюйте професійний навчальний контент та матеріали з AI. Генератор уроків, курсів та освітніх ресурсів для різних рівнів.',
            'keywords': 'освітній контент, навчальні матеріали, ai освіта, уроки генератор, курси контент',
            'tool_long_description': 'Освітній Контент Генератор - це потужний AI-інструмент для створення якісних навчальних матеріалів та контенту. Чому використовувати AI? Ефективне навчання потребує структурованого, зрозумілого та залученого контенту. Створення таких матеріалів вручну займає багато часу та вимагає педагогічних знань. AI може проаналізувати тему, рівень складності та створити структурований навчальний контент з правильним прогресом та практичними вправами. Як отримати найкращі результати? Надайте тему, рівень (початковий/середній/просунутий), тип матеріалу (урок, курс, вправи, тести), цільову аудиторію. AI створить навчальний контент з чіткою структурою, поступовим розкриттям теми, практичними прикладами, вправами та рекомендаціями, який допоможе учням ефективно засвоїти матеріал.'
        },
        'en': {
            'name': 'Education',
            'description': 'Create educational content and materials',
            'seo_text': 'Educational content and materials generator. Create lessons, courses, and educational resources for different levels.',
            'seo_title': 'Educational Content Generator - AI Learning Materials Creation',
            'meta_description': 'Create professional educational content and materials with AI. Generate lessons, courses, and educational resources for different levels.',
            'keywords': 'educational content, learning materials, ai education, lesson generator, course content',
            'tool_long_description': 'Educational Content Generator is a powerful AI tool for creating quality learning materials and content. Why use AI? Effective learning requires structured, clear, and engaging content. Creating such materials manually takes a lot of time and requires pedagogical knowledge. AI can analyze the topic, difficulty level, and create structured educational content with proper progression and practical exercises. How to get the best results? Provide the topic, level (beginner/intermediate/advanced), material type (lesson, course, exercises, tests), target audience. AI will create educational content with clear structure, gradual topic development, practical examples, exercises, and recommendations that will help students effectively master the material.'
        },
        'icon': '🎓'
    },
    'travel': {
        'category': 'Personal',
        'tool_name': 'travel',
        'uk': {
            'name': 'Подорожі',
            'description': 'Створюйте контент про подорожі та туризм',
            'seo_text': 'Генератор контенту про подорожі та туризм. Створюйте путівники, поради та описи туристичних напрямків.',
            'seo_title': 'Туристичний Контент Генератор - AI Створення Путівників',
            'meta_description': 'Створюйте захоплюючий контент про подорожі та туризм з AI. Генератор путівників, порад та описів туристичних напрямків.',
            'keywords': 'туристичний контент, путівники, ai подорожі, туризм контент, travel guides',
            'tool_long_description': 'Туристичний Контент Генератор - це професійний AI-інструмент для створення захоплюючого контенту про подорожі та туризм. Чому використовувати AI? Якісний туристичний контент допомагає читачам планувати подорожі, відкривати нові місця та отримувати корисні поради. Створення таких матеріалів вручну вимагає досвіду подорожей та знань про різні напрямки. AI може проаналізувати напрямок, створити структурований путівник з актуальною інформацією та практичними порадами. Як отримати найкращі результати? Надайте напрямок/місце, тип контенту (путівник, поради, маршрут, огляд), цільову аудиторію (бюджетні/розкішні подорожі), ключові моменти. AI створить туристичний контент з детальним описом місця, практичними порадами, рекомендаціями щодо проживання та харчування, маршрутами та корисними лайфхаками, який допоможе читачам спланувати незабутню подорож.'
        },
        'en': {
            'name': 'Travel',
            'description': 'Create content about travel and tourism',
            'seo_text': 'Travel and tourism content generator. Create guides, tips, and descriptions of travel destinations.',
            'seo_title': 'Travel Content Generator - AI Travel Guide Creation',
            'meta_description': 'Create engaging travel and tourism content with AI. Generate guides, tips, and descriptions of travel destinations.',
            'keywords': 'travel content, travel guides, ai travel, tourism content, travel guides',
            'tool_long_description': 'Travel Content Generator is a professional AI tool for creating engaging travel and tourism content. Why use AI? Quality travel content helps readers plan trips, discover new places, and get useful tips. Creating such materials manually requires travel experience and knowledge of various destinations. AI can analyze the destination, create a structured guide with current information and practical advice. How to get the best results? Provide destination/place, content type (guide, tips, itinerary, review), target audience (budget/luxury travel), key points. AI will create travel content with detailed place description, practical tips, accommodation and dining recommendations, itineraries, and useful hacks that will help readers plan an unforgettable trip.'
        },
        'icon': '✈️'
    },
    'food': {
        'category': 'Personal',
        'tool_name': 'food',
        'uk': {
            'name': 'Їжа та ресторани',
            'description': 'Створюйте контент про їжу та ресторани',
            'seo_text': 'Генератор контенту про їжу та ресторани. Створюйте рецепти, огляди ресторанів та кулінарні статті.',
            'seo_title': 'Кулінарний Контент Генератор - AI Створення Рецептів та Оглядів',
            'meta_description': 'Створюйте захоплюючий контент про їжу та ресторани з AI. Генератор рецептів, оглядів ресторанів та кулінарних статей.',
            'keywords': 'кулінарний контент, рецепти, огляди ресторанів, ai їжа, кулінарні статті',
            'tool_long_description': 'Кулінарний Контент Генератор - це професійний AI-інструмент для створення захоплюючого контенту про їжу та ресторани. Чому використовувати AI? Якісний кулінарний контент допомагає читачам відкривати нові рецепти, ресторани та кулінарні традиції. Створення таких матеріалів вручну вимагає кулінарного досвіду та знань про різні кухні. AI може проаналізувати рецепт або ресторан, створити структурований контент з детальними описями та практичними порадами. Як отримати найкращі результати? Надайте інформацію: тип контенту (рецепт, огляд ресторану, кулінарна стаття), назву страви/ресторану, стиль кухні, цільову аудиторію. AI створить кулінарний контент з детальним описом, покроковими інструкціями (для рецептів), рекомендаціями щодо інгредієнтів, порадами з приготування та корисними лайфхаками, який надихне читачів на кулінарні експерименти.'
        },
        'en': {
            'name': 'Food & Restaurants',
            'description': 'Create content about food and restaurants',
            'seo_text': 'Food and restaurant content generator. Create recipes, restaurant reviews, and culinary articles.',
            'seo_title': 'Culinary Content Generator - AI Recipe and Review Creation',
            'meta_description': 'Create engaging food and restaurant content with AI. Generate recipes, restaurant reviews, and culinary articles.',
            'keywords': 'culinary content, recipes, restaurant reviews, ai food, culinary articles',
            'tool_long_description': 'Culinary Content Generator is a professional AI tool for creating engaging food and restaurant content. Why use AI? Quality culinary content helps readers discover new recipes, restaurants, and culinary traditions. Creating such materials manually requires culinary experience and knowledge of various cuisines. AI can analyze a recipe or restaurant, create structured content with detailed descriptions and practical advice. How to get the best results? Provide information: content type (recipe, restaurant review, culinary article), dish/restaurant name, cuisine style, target audience. AI will create culinary content with detailed description, step-by-step instructions (for recipes), ingredient recommendations, cooking tips, and useful hacks that will inspire readers to culinary experiments.'
        },
        'icon': '🍽️'
    },
    'fitness': {
        'category': 'Personal',
        'tool_name': 'fitness',
        'uk': {
            'name': 'Фітнес',
            'description': 'Створюйте контент про фітнес та тренування',
            'seo_text': 'Генератор контенту про фітнес та тренування. Створюйте програми тренувань, поради та мотиваційний контент.',
            'seo_title': 'Фітнес Контент Генератор - AI Створення Програм Тренувань',
            'meta_description': 'Створюйте професійний контент про фітнес та тренування з AI. Генератор програм тренувань, порад та мотиваційного контенту.',
            'keywords': 'фітнес контент, програми тренувань, ai фітнес, фітнес поради, тренування контент',
            'tool_long_description': 'Фітнес Контент Генератор - це професійний AI-інструмент для створення якісного контенту про фітнес та тренування. Чому використовувати AI? Ефективний фітнес-контент допомагає людям досягати своїх цілей, мотивує та надає практичні поради. Створення таких матеріалів вручну вимагає знань про фізіологію, тренування та безпеку. AI може проаналізувати цілі, рівень фізичної підготовки та створити персоналізовану програму тренувань з правильними вправами та рекомендаціями. Як отримати найкращі результати? Надайте інформацію: цілі (схуднення, набір маси, витривалість), рівень (початківець/середній/просунутий), тип тренувань (силові/кардіо/йога), обмеження. AI створить фітнес-контент з детальною програмою тренувань, правильними техніками, рекомендаціями щодо харчування та мотиваційними порадами, який допоможе читачам досягти своїх фітнес-цілей безпечно та ефективно.'
        },
        'en': {
            'name': 'Fitness',
            'description': 'Create content about fitness and training',
            'seo_text': 'Fitness and training content generator. Create workout programs, tips, and motivational content.',
            'seo_title': 'Fitness Content Generator - AI Workout Program Creation',
            'meta_description': 'Create professional fitness and training content with AI. Generate workout programs, tips, and motivational content.',
            'keywords': 'fitness content, workout programs, ai fitness, fitness tips, training content',
            'tool_long_description': 'Fitness Content Generator is a professional AI tool for creating quality fitness and training content. Why use AI? Effective fitness content helps people achieve their goals, motivates, and provides practical advice. Creating such materials manually requires knowledge of physiology, training, and safety. AI can analyze goals, fitness level, and create a personalized workout program with proper exercises and recommendations. How to get the best results? Provide information: goals (weight loss, muscle gain, endurance), level (beginner/intermediate/advanced), workout type (strength/cardio/yoga), limitations. AI will create fitness content with detailed workout program, proper techniques, nutrition recommendations, and motivational tips that will help readers achieve their fitness goals safely and effectively.'
        },
        'icon': '💪'
    },
    'beauty': {
        'category': 'Personal',
        'tool_name': 'beauty',
        'uk': {
            'name': 'Краса',
            'description': 'Створюйте контент про красу та косметику',
            'seo_text': 'Генератор контенту про красу та косметику. Створюйте огляди продуктів, поради з догляду та модні тенденції.',
            'seo_title': 'Контент про Красу Генератор - AI Створення Оглядів та Порад',
            'meta_description': 'Створюйте професійний контент про красу та косметику з AI. Генератор оглядів продуктів, порад з догляду та модних тенденцій.',
            'keywords': 'краса контент, косметика огляди, ai краса, догляд поради, beauty trends',
            'tool_long_description': 'Контент про Красу Генератор - це професійний AI-інструмент для створення якісного контенту про красу та косметику. Чому використовувати AI? Ефективний beauty-контент допомагає читачам вибирати продукти, дізнаватися про нові тенденції та отримувати поради з догляду. Створення таких матеріалів вручну вимагає знань про косметику, шкіру та модні тенденції. AI може проаналізувати продукт, тип шкіри та створити структурований контент з детальними оглядами та практичними порадами. Як отримати найкращі результати? Надайте інформацію: тип контенту (огляд продукту, поради з догляду, тренди), продукт/послуга, тип шкіри, цільова аудиторія. AI створить beauty-контент з детальним оглядом продуктів, рекомендаціями щодо використання, порадами з догляду, інформацією про інгредієнти та актуальними трендами, який допоможе читачам зробити інформований вибір та покращити свій догляд.'
        },
        'en': {
            'name': 'Beauty',
            'description': 'Create content about beauty and cosmetics',
            'seo_text': 'Beauty and cosmetics content generator. Create product reviews, skincare tips, and fashion trends.',
            'seo_title': 'Beauty Content Generator - AI Review and Tips Creation',
            'meta_description': 'Create professional beauty and cosmetics content with AI. Generate product reviews, skincare tips, and fashion trends.',
            'keywords': 'beauty content, cosmetics reviews, ai beauty, skincare tips, beauty trends',
            'tool_long_description': 'Beauty Content Generator is a professional AI tool for creating quality beauty and cosmetics content. Why use AI? Effective beauty content helps readers choose products, learn about new trends, and get skincare advice. Creating such materials manually requires knowledge of cosmetics, skin, and fashion trends. AI can analyze a product, skin type, and create structured content with detailed reviews and practical advice. How to get the best results? Provide information: content type (product review, skincare tips, trends), product/service, skin type, target audience. AI will create beauty content with detailed product reviews, usage recommendations, skincare tips, ingredient information, and current trends that will help readers make informed choices and improve their skincare routine.'
        },
        'icon': '💄'
    },
    'real-estate': {
        'category': 'Personal',
        'tool_name': 'real-estate',
        'uk': {
            'name': 'Нерухомість',
            'description': 'Створюйте контент про нерухомість',
            'seo_text': 'Генератор контенту про нерухомість. Створюйте огляди ринку, поради для інвесторів та описи нерухомості.',
            'seo_title': 'Контент про Нерухомість Генератор - AI Створення Оглядів Ринку',
            'meta_description': 'Створюйте професійний контент про нерухомість з AI. Генератор оглядів ринку, порад для інвесторів та описів нерухомості.',
            'keywords': 'нерухомість контент, ринок нерухомості, ai нерухомість, інвестиції нерухомість, property content',
            'tool_long_description': 'Контент про Нерухомість Генератор - це професійний AI-інструмент для створення якісного контенту про нерухомість та ринок. Чому використовувати AI? Якісний контент про нерухомість допомагає читачам розуміти ринок, приймати інвестиційні рішення та знаходити відповідну нерухомість. Створення таких матеріалів вручну вимагає знань про ринок, законодавство та інвестиції. AI може проаналізувати ринкові дані, локацію та створити структурований контент з актуальною інформацією та практичними порадами. Як отримати найкращі результати? Надайте інформацію: тип контенту (огляд ринку, опис нерухомості, поради інвесторам), локація, тип нерухомості, цільова аудиторія. AI створить контент про нерухомість з детальним аналізом ринку, описом нерухомості, рекомендаціями для інвесторів, інформацією про тенденції та практичними порадами, який допоможе читачам зробити інформовані рішення у сфері нерухомості.'
        },
        'en': {
            'name': 'Real Estate',
            'description': 'Create content about real estate',
            'seo_text': 'Real estate content generator. Create market reviews, investor tips, and property descriptions.',
            'seo_title': 'Real Estate Content Generator - AI Market Review Creation',
            'meta_description': 'Create professional real estate content with AI. Generate market reviews, investor tips, and property descriptions.',
            'keywords': 'real estate content, real estate market, ai real estate, real estate investments, property content',
            'tool_long_description': 'Real Estate Content Generator is a professional AI tool for creating quality real estate and market content. Why use AI? Quality real estate content helps readers understand the market, make investment decisions, and find suitable properties. Creating such materials manually requires knowledge of the market, legislation, and investments. AI can analyze market data, location, and create structured content with current information and practical advice. How to get the best results? Provide information: content type (market review, property description, investor tips), location, property type, target audience. AI will create real estate content with detailed market analysis, property description, investor recommendations, trend information, and practical tips that will help readers make informed decisions in real estate.'
        },
        'icon': '🏠'
    },
    'psychology': {
        'category': 'Personal',
        'tool_name': 'psychology',
        'uk': {
            'name': 'Психологічна підтримка',
            'description': 'Створюйте контент про психологію та підтримку',
            'seo_text': 'Генератор контенту про психологію та підтримку. Створюйте статті про ментальне здоров\'я, стрес та психологічну допомогу.',
            'seo_title': 'Психологічний Контент Генератор - AI Створення Контенту про Ментальне Здоров\'я',
            'meta_description': 'Створюйте професійний контент про психологію та ментальне здоров\'я з AI. Генератор статей про стрес, психологічну підтримку та самодопомогу.',
            'keywords': 'психологія контент, ментальне здоров\'я, ai психологія, стрес менеджмент, психологічна підтримка',
            'tool_long_description': 'Психологічний Контент Генератор - це професійний AI-інструмент для створення якісного контенту про психологію та ментальне здоров\'я. Чому використовувати AI? Якісний психологічний контент допомагає людям розуміти себе, впоратися зі стресом та покращити ментальне здоров\'я. Створення таких матеріалів вручну вимагає знань про психологію, терапію та етичні аспекти. AI може проаналізувати тему, створити структурований контент з науково обґрунтованою інформацією та практичними порадами. Як отримати найкращі результати? Надайте інформацію: тема (стрес, тривога, самопізнання, стосунки), тип контенту (інформативний, поради, самодопомога), цільова аудиторія, стиль. AI створить психологічний контент з чіткою структурою, науково обґрунтованою інформацією, практичними техніками, рекомендаціями та важливими застереженнями, який буде корисним та безпечним для читачів, допомагаючи їм покращити своє ментальне здоров\'я.'
        },
        'en': {
            'name': 'Psychological Support',
            'description': 'Create content about psychology and support',
            'seo_text': 'Psychology and support content generator. Create articles about mental health, stress, and psychological assistance.',
            'seo_title': 'Psychology Content Generator - AI Mental Health Content Creation',
            'meta_description': 'Create professional psychology and mental health content with AI. Generate articles about stress, psychological support, and self-help.',
            'keywords': 'psychology content, mental health, ai psychology, stress management, psychological support',
            'tool_long_description': 'Psychology Content Generator is a professional AI tool for creating quality psychology and mental health content. Why use AI? Quality psychological content helps people understand themselves, cope with stress, and improve mental health. Creating such materials manually requires knowledge of psychology, therapy, and ethical aspects. AI can analyze the topic, create structured content with scientifically grounded information and practical advice. How to get the best results? Provide information: topic (stress, anxiety, self-discovery, relationships), content type (informative, tips, self-help), target audience, style. AI will create psychological content with clear structure, scientifically grounded information, practical techniques, recommendations, and important disclaimers that will be useful and safe for readers, helping them improve their mental health.'
        },
        'icon': '🧠'
    }
}


# ---------------------------------------------------------------------------
# Product tiers: which tools are available per plan (modular SaaS).
# ---------------------------------------------------------------------------

STARTER = "STARTER"
PRO = "PRO"
FULL = "FULL"

# Tools allowed per tier. FULL = None means all tools (no filter).
TIER_TOOLS = {
    STARTER: ["amazon", "shopify", "etsy"],
    PRO: [
        "amazon", "shopify", "etsy", "resume", "kdp",
        "youtube-script", "tiktok-hook", "google-ads",
    ],
    FULL: None,  # All 20 tools (Professional + Personal)
}

# Plan name (from user/context) -> tier constant. Use "Full" as highest in app logic.
PLAN_TO_TIER = {
    "Starter": STARTER,
    "Pro": PRO,
    "Full": FULL,
}
VALID_PLAN_NAMES = ("Starter", "Pro", "Full")


def get_tier_for_plan(plan_name):
    """Return tier constant for a plan name. Default STARTER for unknown plans."""
    if plan_name is None:
        return STARTER
    return PLAN_TO_TIER.get(plan_name, STARTER)


def get_tools_allowed_for_tier(tier):
    """Return set of tool_name allowed for tier, or None if all tools (FULL)."""
    if tier == FULL:
        return None
    return set(TIER_TOOLS.get(tier, []))


def tool_allowed_for_tier(tool_name, tier):
    """Return True if tool_name is allowed for the given tier."""
    allowed = get_tools_allowed_for_tier(tier)
    if allowed is None:
        return True
    return tool_name in allowed


# ---------------------------------------------------------------------------
# Module loader: delegate to tool_modules when available (modular SaaS).
# TOOLS_CONFIG and TOOL_SYSTEM_PROMPTS above remain for backward compatibility.
# ---------------------------------------------------------------------------

_loader_available = None

def _use_loader():
    """Use tool_modules loader if it has tools; otherwise fall back to legacy."""
    global _loader_available
    if _loader_available is not None:
        return _loader_available
    try:
        from tool_modules.loader import get_all_tools as _all
        _loader_available = bool(_all("en"))
    except Exception:
        _loader_available = False
    return _loader_available


def get_tools_by_category(category, locale='en', tier=None):
    """
    Get tools filtered by category (Professional or Personal).
    If tier is set (STARTER, PRO, FULL), only tools allowed for that tier are returned.
    Uses tool_modules loader when available; falls back to TOOLS_CONFIG.
    """
    if _use_loader():
        from tool_modules.loader import get_tools_by_category as _fn
        tools = _fn(category, locale)
    else:
        tools = []
        for tool_id, tool_config in TOOLS_CONFIG.items():
            if tool_config['category'] == category:
                locale_data = tool_config.get(locale, tool_config['en'])
                tools.append({
                    'id': tool_id,
                    'tool_name': tool_config['tool_name'],
                    'name': locale_data['name'],
                    'description': locale_data['description'],
                    'icon': tool_config['icon'],
                    'seo_text': locale_data.get('seo_text', ''),
                    'seo_title': locale_data.get('seo_title', ''),
                    'meta_description': locale_data.get('meta_description', ''),
                    'keywords': locale_data.get('keywords', ''),
                    'tool_long_description': locale_data.get('tool_long_description', ''),
                    'category': tool_config['category']
                })
    if tier is not None:
        allowed = get_tools_allowed_for_tier(tier)
        if allowed is not None:
            tools = [t for t in tools if t["tool_name"] in allowed]
    return tools


def get_all_tools(locale='en', tier=None):
    """Get all tools. If tier is set, only tools allowed for that tier. Uses loader or TOOLS_CONFIG."""
    if _use_loader():
        from tool_modules.loader import get_all_tools as _fn
        tools = _fn(locale)
    else:
        tools = []
        for tool_id, tool_config in TOOLS_CONFIG.items():
            locale_data = tool_config.get(locale, tool_config['en'])
            tools.append({
                'id': tool_id,
                'tool_name': tool_config['tool_name'],
                'name': locale_data['name'],
                'description': locale_data['description'],
                'icon': tool_config['icon'],
                'seo_text': locale_data.get('seo_text', ''),
                'category': tool_config['category']
            })
    if tier is not None:
        allowed = get_tools_allowed_for_tier(tier)
        if allowed is not None:
            tools = [t for t in tools if t["tool_name"] in allowed]
    return tools


def get_tool_by_name(tool_name, locale='en'):
    """Get one tool by tool_name. Uses tool_modules loader when available; else TOOLS_CONFIG."""
    if _use_loader():
        from tool_modules.loader import get_tool_by_name as _fn
        return _fn(tool_name, locale)
    for tool_id, tool_config in TOOLS_CONFIG.items():
        if tool_config['tool_name'] == tool_name:
            locale_data = tool_config.get(locale, tool_config['en'])
            return {
                'id': tool_id,
                'tool_name': tool_config['tool_name'],
                'name': locale_data['name'],
                'description': locale_data['description'],
                'icon': tool_config['icon'],
                'seo_text': locale_data.get('seo_text', ''),
                'seo_title': locale_data.get('seo_title', ''),
                'meta_description': locale_data.get('meta_description', ''),
                'keywords': locale_data.get('keywords', ''),
                'tool_long_description': locale_data.get('tool_long_description', ''),
                'category': tool_config['category']
            }
    return None


def get_system_prompt(tool_name):
    """Get system prompt for a tool. Uses tool_modules loader when available; else TOOL_SYSTEM_PROMPTS."""
    if _use_loader():
        from tool_modules.loader import get_system_prompt as _fn
        return _fn(tool_name)
    return TOOL_SYSTEM_PROMPTS.get(tool_name, "Act as a helpful AI assistant.")

