# System Patterns

## Architecture

The project is a monorepo containing multiple independent or semi-independent automation suites organized by product domain (`G8`, `LDP2`, `web_app`).

Key patterns:
- **Monorepo Structure**: Separate folders for different domains, allowing targeted execution.
- **Shared Utilities**: `ultis/` contains common code like `base_page.py` (Playwright bootstrap), Discord reporting, and Google Sheets access.
- **Pytest Framework**: All suites use `pytest` as the runner and for fixtures.
- **Playwright Automation**: Used for web and canvas interactions (using image matching in some cases).
- **External Integrations**: Hooks and helpers for Discord, Google Sheets, and NocoDB.

## Important Runtime Flows

- **Standard Execution**: `uv run pytest` runs the configured suites.
- **Canvas Automation**: Uses OpenCV/image matching for canvas-based games (e.g., in `G8/bot_tools/access_canvas/`).
- **Reporting**: Tests send results to Discord channels or update Google Sheets/NocoDB after execution.

## Harness Pattern

The harness uses a layered rule chain:
1. Highest-priority runtime contract (`00-HARNESS.md`).
2. Project memory (`projectBrief.md`, etc.).
3. Ordered engineering rule modules.
