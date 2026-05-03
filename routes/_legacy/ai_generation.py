from flask import Blueprint, render_template, request, jsonify, session
from flask_login import login_required, current_user
from openai import OpenAI
from extensions import db
from models import User
import os
from dotenv import load_dotenv
from tools_config import (
    get_tools_by_category,
    get_tool_by_name,
    get_system_prompt
)

# Load environment variables
load_dotenv(override=True)

ai_bp = Blueprint('ai', __name__)

def _locale_from_session():
    from flask import session
    lang = session.get('language', session.get('locale', 'en'))
    return 'uk' if lang in ('uk', 'ua') else (lang if lang in ('en', 'es', 'ru', 'de', 'fr') else 'en')


@ai_bp.route('/')
def dashboard():
    from flask_login import current_user
    from flask import session, url_for

    locale = _locale_from_session()
    business_tools = get_tools_by_category('Professional', locale)
    personal_creative_tools = get_tools_by_category('Personal', locale)
    all_tools = business_tools + personal_creative_tools

    recent_tool_names = session.get('recent_tools', [])
    recent_tools = []
    for name in recent_tool_names[:4]:
        t = get_tool_by_name(name, locale)
        if t:
            recent_tools.append(t)
    featured_tools = (business_tools[:2] + personal_creative_tools[:1]) if not recent_tools else []
    if recent_tools:
        display_tools = recent_tools
        section_title_key = 'Recently Used'
    else:
        display_tools = featured_tools if featured_tools else business_tools[:3]
        section_title_key = 'Featured Tools'

    all_tools_for_search = [
        {'name': t['name'], 'url': url_for('ai.tool_page', tool_name=t['tool_name']), 'icon': t['icon'], 'tool_name': t['tool_name']}
        for t in all_tools
    ]

    seo = {
        'title': 'AI Multi Tools - Dashboard',
        'description': 'AI Multi Tools dashboard. Create professional content in seconds.',
        'keywords': 'AI tools, content generator'
    }
    translations = {'rights': 'All rights reserved.', 'logout': 'Log out'}

    return render_template('index.html',
                         business_tools=business_tools,
                         personal_creative_tools=personal_creative_tools,
                         recent_tools=recent_tools,
                         featured_tools=featured_tools,
                         display_tools=display_tools,
                         section_title_key=section_title_key,
                         all_tools_for_search=all_tools_for_search,
                         seo=seo,
                         t=translations,
                         current_user=current_user if hasattr(current_user, 'is_authenticated') else type('obj', (object,), {'is_authenticated': False})())

@ai_bp.route('/tool/<tool_name>')
def tool_page(tool_name):
    from flask import session

    locale = _locale_from_session()
    tool = get_tool_by_name(tool_name, locale)

    if tool:
        recent = list(session.get('recent_tools', []))
        if tool_name in recent:
            recent.remove(tool_name)
        recent.insert(0, tool_name)
        session['recent_tools'] = recent[:4]

    seo = {
        'title': tool.get('seo_title', tool.get('name', 'AI Tool')) if tool else 'AI Tool',
        'description': tool.get('meta_description', tool.get('description', '')) if tool else '',
        'keywords': tool.get('keywords', '') if tool else ''
    }
    return render_template('tool.html', tool_name=tool_name, tool=tool, seo=seo)

@ai_bp.route('/api/generate', methods=['POST'])
@login_required
def generate_content():
    user = User.query.get(current_user.id)

    # No credits: block and suggest buying a plan
    if user.credits < 1:
        return jsonify({'error': 'You have run out of credits. Please upgrade your plan.'}), 402

    # Credits > 10 but subscription inactive: lock (trial is only first 10 credits)
    if user.credits > 10 and not getattr(user, "is_subscription_active", False):
        return jsonify({'error': 'Your credits are locked. Please reactivate your subscription to continue.'}), 403

    # Allow: credits in 1..10 (trial) or credits > 10 with active subscription

    # Force reload .env file at the very beginning
    load_dotenv(override=True)
    
    # Get API key from environment with default empty string
    raw_key = os.getenv('OPENAI_API_KEY', '')
    
    # If missing, try manual file reading as fallback
    if not raw_key:
        print(f'System sees environment: {os.environ.keys()}')
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('OPENAI_API_KEY='):
                        # Extract the key value after the = sign
                        raw_key = line.split('=', 1)[1].strip()
                        print(f'SUCCESS: Key found and loaded from file.')
                        break
        except FileNotFoundError:
            return jsonify({'error': '.env file not found in project root.'}), 500
        except Exception as e:
            return jsonify({'error': f'Error reading .env file: {str(e)}'}), 500
    
    # Robust key cleaner: remove BOM, quotes, and whitespace
    cleaned_key = raw_key.strip().replace('\ufeff', '').replace('"', '').replace("'", "")
    
    # Check if cleaned key is empty
    if not cleaned_key:
        return jsonify({'error': 'OPENAI_API_KEY not found in .env file. Please add OPENAI_API_KEY=your_key to the file.'}), 500
    
    print(f'API Key starts with: {cleaned_key[:8]}...')
    
    data = request.json
    user_input = data.get('prompt', '')
    tool_name = data.get('tool_name', 'general')

    # Retrieve language from session; map codes to full names
    selected_lang = session.get('language', 'en')
    lang_map = {'ua': 'Ukrainian', 'uk': 'Ukrainian', 'en': 'English', 'es': 'Spanish'}
    full_language_name = lang_map.get(selected_lang, 'English')

    # Build user message with language instruction
    user_message = f"Answer the following request strictly in {full_language_name}.\n\n{user_input}"

    # Get system prompt
    system_prompt = get_system_prompt(tool_name)

    # Test: print final prompt to terminal
    print(f"[AI Generate] session['language']={selected_lang!r} -> {full_language_name!r}")
    print(f"[AI Generate] System prompt: {system_prompt[:200]}...")
    print(f"[AI Generate] User message: {user_message[:300]}...")

    try:
        # Use latest OpenAI client syntax
        client = OpenAI(api_key=cleaned_key)
        
        # OpenAI API call using latest client syntax
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        # Subtract 1 credit after successful generation
        user = User.query.get(current_user.id)
        user.credits -= 1
        db.session.commit()

        return jsonify({'result': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500