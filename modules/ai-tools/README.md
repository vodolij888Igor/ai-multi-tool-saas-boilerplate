# AI Tools (modular)

Each tool can live in its own folder with:

- **tool_config.py** (or `tool_config`) – `TOOL_NAME`, `CATEGORY`, `LOCALES`, `ICON`
- **prompt_template.txt** or inline in config – system prompt for the model
- **input_schema** / **output_schema** – optional; API currently uses free-form prompt text and plain text result
- **handler** – optional custom logic; default is: system prompt + user message → OpenAI → return content

Existing tools are defined in the central **tools_config.py** at project root (and optionally loaded from here). To add a new tool:

1. Add system prompt to `TOOL_SYSTEM_PROMPTS` in `tools_config.py`.
2. Add tool definition to `TOOLS_CONFIG` in `tools_config.py` (category, tool_name, uk/en, icon).
3. Or: create a folder under `modules/ai-tools/<tool-id>/` with `tool_config.py` and `prompt_template.txt`, then register it in a registry that `tools_config` or the AI module reads.

See **docs/how-to-add-tool.md** for details.
