# How to Add a New AI Tool

The AI tools system is modular. Each tool can be defined with:

- **Tool config**: id, category, name/description per locale, icon.
- **Prompt template**: system prompt for the AI (persona + instructions).
- **Input/Output**: the API expects `prompt` (user text) and `tool_name`; output is plain text (or structured if you extend the handler).

## Option A: Register in central tools config

1. **Add system prompt**  
   In `tools_config.py` (or the backend module that holds prompts), add an entry to `TOOL_SYSTEM_PROMPTS`:
   ```python
   'my-tool': 'Expert in X. Do Y. Output format: Z.'
   ```

2. **Add tool definition**  
   In `TOOLS_CONFIG`, add a block with `category` (e.g. `'Professional'` or `'Personal'`), `tool_name`, `uk`/`en` (and other locales) with `name`, `description`, `seo_title`, `meta_description`, `keywords`, `tool_long_description`, and `icon`.

3. **Sidebar and dashboard**  
   Tools are loaded by category via `get_tools_by_category()`. The sidebar and dashboard will pick them up automatically.

4. **Route**  
   Tool page is `/tool/<tool_name>`. No new route needed; ensure `tool_name` matches your config key.

## Option B: Modular tool under `modules/ai-tools`

Each tool can live under `modules/ai-tools/<tool-id>/`:

- `tool_config.py` – dict with category, tool_name, locales, icon.
- `prompt.txt` or `prompt.py` – system prompt.
- `handler.py` (optional) – custom logic; otherwise the default handler uses the system prompt and user message.

Register the tool in the central registry (e.g. in `backend/modules/ai/registry.py`) so the app can find it by `tool_name`.

## API behavior

- **POST /api/generate**: body `{ "prompt": "user input", "tool_name": "my-tool" }`.
- Credits are checked and decremented by 1 on success.
- Language is taken from session and appended to the user message (e.g. "Answer in English").
- Response: `{ "result": "generated text" }` or `{ "error": "..." }` with appropriate status code.

After adding the tool, recompile translations if you added new UI strings, and test the tool page and generation.
