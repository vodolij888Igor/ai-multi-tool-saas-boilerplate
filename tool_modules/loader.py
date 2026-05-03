"""
Module loader for AI tools. Discovers tool modules, applies enable/disable list,
and exposes get_tools_by_category, get_tool_by_name, get_system_prompt, get_all_tools.
"""
import os
import sys
import importlib.util
from pathlib import Path

# Optional: set of tool_name to enable. None = all enabled.
# Can be overridden via env TOOL_MODULES_ENABLED (comma-separated) or set_enabled_tools().
_env = os.environ.get("TOOL_MODULES_ENABLED", "").strip()
ENABLED_TOOLS = set(_env.split(",")) if _env else None  # None = all; or set({"amazon", "shopify", ...})


def _tool_modules_dir():
    return Path(__file__).resolve().parent


def _discover_module_dirs():
    """Return list of subdirs that are tool modules (contain module.py)."""
    base = _tool_modules_dir()
    dirs = []
    for entry in base.iterdir():
        if entry.is_dir() and not entry.name.startswith("_") and entry.name != "__pycache__":
            if (entry / "module.py").is_file():
                dirs.append(entry.name)
    return sorted(dirs)


def _load_module_module(tool_name):
    """Load module.py from tool_modules/<tool_name>/ and return (metadata_dict, system_prompt_str)."""
    base = _tool_modules_dir() / tool_name
    module_py = base / "module.py"
    if not module_py.is_file():
        return None, None
    spec = importlib.util.spec_from_file_location(
        f"tool_modules.{tool_name}.module",
        module_py,
        submodule_search_locations=[str(base)],
    )
    if spec is None or spec.loader is None:
        return None, None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    metadata = getattr(mod, "METADATA", None)
    system_prompt = getattr(mod, "SYSTEM_PROMPT", None)
    return metadata, system_prompt


def _build_registry():
    """Build in-memory registry of all enabled tools from module dirs."""
    registry = []
    for name in _discover_module_dirs():
        if ENABLED_TOOLS is not None and name not in ENABLED_TOOLS:
            continue
        metadata, system_prompt = _load_module_module(name)
        if metadata is None:
            continue
        tool_name = metadata.get("tool_name", name)
        registry.append({
            "tool_name": tool_name,
            "category": metadata.get("category", "Personal"),
            "icon": metadata.get("icon", "🛠️"),
            "en": metadata.get("en", {}),
            "uk": metadata.get("uk", metadata.get("en", {})),
            "system_prompt": system_prompt or "Act as a helpful AI assistant.",
        })
    return registry


# Cache registry so we don't re-scan on every call. Clear cache when ENABLED_TOOLS changes.
_registry_cache = None


def _get_registry():
    global _registry_cache
    if _registry_cache is None:
        _registry_cache = _build_registry()
    return _registry_cache


def invalidate_cache():
    """Clear registry cache (e.g. after changing ENABLED_TOOLS)."""
    global _registry_cache
    _registry_cache = None


def set_enabled_tools(tool_names):
    """Set which tools are enabled. None = all. Call invalidate_cache() after if needed."""
    global ENABLED_TOOLS
    ENABLED_TOOLS = set(tool_names) if tool_names is not None else None
    invalidate_cache()


def get_enabled_tools():
    """Return set of enabled tool names, or None if all are enabled."""
    return ENABLED_TOOLS


def get_tools_by_category(category, locale="en"):
    """Return list of tool dicts for the given category (Professional or Personal)."""
    tools = []
    for r in _get_registry():
        if r["category"] != category:
            continue
        loc = r.get(locale, r.get("en", {}))
        tools.append({
            "id": r["tool_name"],
            "tool_name": r["tool_name"],
            "name": loc.get("name", r["tool_name"]),
            "description": loc.get("description", ""),
            "icon": r["icon"],
            "seo_text": loc.get("seo_text", ""),
            "seo_title": loc.get("seo_title", ""),
            "meta_description": loc.get("meta_description", ""),
            "keywords": loc.get("keywords", ""),
            "tool_long_description": loc.get("tool_long_description", ""),
            "category": r["category"],
        })
    return tools


def get_all_tools(locale="en"):
    """Return list of all enabled tools."""
    tools = []
    for r in _get_registry():
        loc = r.get(locale, r.get("en", {}))
        tools.append({
            "id": r["tool_name"],
            "tool_name": r["tool_name"],
            "name": loc.get("name", r["tool_name"]),
            "description": loc.get("description", ""),
            "icon": r["icon"],
            "seo_text": loc.get("seo_text", ""),
            "category": r["category"],
        })
    return tools


def get_tool_by_name(tool_name, locale="en"):
    """Return one tool dict by tool_name, or None."""
    for r in _get_registry():
        if r["tool_name"] == tool_name:
            loc = r.get(locale, r.get("en", {}))
            return {
                "id": r["tool_name"],
                "tool_name": r["tool_name"],
                "name": loc.get("name", r["tool_name"]),
                "description": loc.get("description", ""),
                "icon": r["icon"],
                "seo_text": loc.get("seo_text", ""),
                "seo_title": loc.get("seo_title", ""),
                "meta_description": loc.get("meta_description", ""),
                "keywords": loc.get("keywords", ""),
                "tool_long_description": loc.get("tool_long_description", ""),
                "category": r["category"],
            }
    return None


def get_system_prompt(tool_name):
    """Return system prompt for the tool, or default."""
    for r in _get_registry():
        if r["tool_name"] == tool_name:
            return r.get("system_prompt") or "Act as a helpful AI assistant."
    return "Act as a helpful AI assistant."
