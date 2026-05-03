"""
Generate tool_modules/<name>/module.py from tools_config.TOOLS_CONFIG and TOOL_SYSTEM_PROMPTS.
Run from project root: python scripts/generate_tool_modules.py
"""
import os
import sys
from pathlib import Path

# Run from project root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

from tools_config import TOOLS_CONFIG, TOOL_SYSTEM_PROMPTS


def main():
    base = ROOT / "tool_modules"
    base.mkdir(exist_ok=True)
    for tool_id, config in TOOLS_CONFIG.items():
        tool_name = config.get("tool_name", tool_id)
        dir_path = base / tool_id
        dir_path.mkdir(exist_ok=True)
        # METADATA: category, tool_name, icon, en, uk
        metadata = {
            "category": config.get("category", "Personal"),
            "tool_name": tool_name,
            "icon": config.get("icon", "🛠️"),
            "en": config.get("en", {}),
            "uk": config.get("uk", config.get("en", {})),
        }
        prompt = TOOL_SYSTEM_PROMPTS.get(tool_id, "Act as a helpful AI assistant.")
        # Write module.py
        content = f'''"""
{tool_name} — AI tool module. Generated from tools_config.
"""
METADATA = {repr(metadata)}
SYSTEM_PROMPT = {repr(prompt)}
'''
        (dir_path / "module.py").write_text(content, encoding="utf-8")
        if not (dir_path / "__init__.py").exists():
            (dir_path / "__init__.py").write_text(f"# {tool_name} tool module\n", encoding="utf-8")
        print(f"Created {dir_path / 'module.py'}")
    print("Done.")


if __name__ == "__main__":
    main()
