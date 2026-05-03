# Tool Modules — Modular AI Tools

Each AI tool lives in its own module under `tool_modules/<tool_id>/`.

## Structure (per tool)

```
tool_modules/
  loader.py           # Discovers modules, applies enable/disable, exposes get_tools_by_category, get_tool_by_name, get_system_prompt
  __init__.py         # Re-exports loader API
  <tool_id>/          # e.g. amazon, shopify, youtube-script
    __init__.py       # Optional
    module.py         # METADATA (category, tool_name, icon, en, uk) + SYSTEM_PROMPT
```

## Enable/disable tools

- **All enabled (default):** Do nothing; all discovered modules are used.
- **Env:** `TOOL_MODULES_ENABLED=amazon,shopify,resume` (comma-separated) to allow only those tools.
- **Code:** `from tool_modules import set_enabled_tools; set_enabled_tools(["amazon", "shopify"])` then `invalidate_cache()`.

## Product packaging (Starter / Pro / Full)

Use `set_enabled_tools()` with a list of tool names for the plan (e.g. Starter = subset, Pro = more, Full = all). Call it at app startup from config or a feature-flag service.

## Adding a new tool

1. Create `tool_modules/<tool_id>/module.py` with `METADATA` and `SYSTEM_PROMPT`.
2. Restart the app (or call `tool_modules.invalidate_cache()` if you reload the registry at runtime).

Existing UI and routing (dashboard, sidebar, `/tool/<tool_name>`, `/api/generate`) are unchanged; they use `tools_config`, which delegates to this loader.
