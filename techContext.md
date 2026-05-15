# Tech Context

## Stack

- Python 3.11+
- `uv` (Package manager)
- `pytest` (Test framework)
- Playwright (Browser automation)
- OpenCV (Image matching for canvas)
- Integrations: Discord, Google Sheets

## Common Commands

- Initialize environment: `uv sync`
- Install Playwright browsers: `uv run playwright install chromium`
- Run all tests: `uv run pytest`
- Run specific suite: `uv run pytest LDP2/urgent/test_urgent_ldp.py`
- Run with parallelization: `uv run pytest -n auto`

## Environment

- File `D:\isp.txt` containing the current ISP (e.g., VNPT, FPT, VIETTEL) is required by some suites.
- Credentials or webhooks for Google Sheets / Discord are required for reporting.

## Agent Notes

- Always use `uv run <command>` for running commands.
- Prefer `rg` for searching the codebase.
- Respect the folder boundaries (`G8`, `LDP2`, `web_app`) and use local `conftest.py` when appropriate.
- If using Serena MCP, remember to prompt: "Activate the current project using serena’s activation tool" at the start of the session to enable advanced features.
