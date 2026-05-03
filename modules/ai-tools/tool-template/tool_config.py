"""
Template: tool config for a single AI tool.
Copy this and prompt_template into a new folder under modules/ai-tools and register in tools_config.py.
"""
TOOL_ID = "my-tool"
CATEGORY = "Professional"  # or "Personal"
TOOL_NAME = "my-tool"
ICON = "🛠️"

LOCALES = {
    "en": {
        "name": "My Tool",
        "description": "Short description for cards and search.",
        "seo_title": "My Tool - AI Generator",
        "meta_description": "Meta description for search engines.",
        "keywords": "my tool, ai, generator",
        "tool_long_description": "Optional long description for the tool page.",
    },
    "uk": {
        "name": "Мій інструмент",
        "description": "Короткий опис.",
        "seo_title": "Мій інструмент - AI Генератор",
        "meta_description": "Мета-опис.",
        "keywords": "мій інструмент, ai",
        "tool_long_description": "Довгий опис для сторінки інструмента.",
    },
}
