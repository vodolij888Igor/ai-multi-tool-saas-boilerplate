"""Find missing and untranslated keys in .po files."""
import re
import os

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

base = os.path.join(os.path.dirname(__file__), '..', 'translations')
en = parse_po(os.path.join(base, 'en', 'LC_MESSAGES', 'messages.po'))
all_ids = set(en.keys())
print('Total msgids in en:', len(all_ids))

for lang in ['uk', 'ru', 'es', 'de', 'fr']:
    path = os.path.join(base, lang, 'LC_MESSAGES', 'messages.po')
    data = parse_po(path)
    missing = all_ids - set(data.keys())
    untranslated = [k for k, v in data.items() if v == k or not v]
    print(f'{lang}: has {len(data)}, missing {len(missing)}, untranslated {len(untranslated)}')
    if missing:
        print(f'  missing keys (first 20): {list(missing)[:20]}')
