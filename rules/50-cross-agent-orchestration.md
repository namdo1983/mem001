# 50 - Cross-Agent Orchestration

## Shared Agent Contract

All agents follow the same harness, regardless of tool-specific capabilities.

Agent adapters should only answer:

- Where is the harness?
- What file should be read first?
- Which project-specific root file does this agent auto-load?

They should not fork behavior.

## Parallel Work

Use parallel agents only when tasks are independent and have disjoint write scopes.

For each delegated task, define:

- Ownership.
- Expected output.
- Files or modules in scope.
- Verification requirements.
- Warning not to overwrite unrelated changes.

## Cross-Agent Artifacts

Use Markdown for plans, handoffs, review notes, and memory updates so Codex, Gemini, Claude/Cline, Antigravity-style tools, and humans can all read the same state.

## Agent Notes

- Codex: root `AGENTS.md` should point to this harness.
- Gemini: root `GEMINI.md` should point to this harness first.
- Claude/Cline: root `CLAUDE.md` should point to this harness. Keep active root `.clinerules/` absent unless a specific tool requires it.
- Antigravity-style agents: for this repo, route through the shared `AGENTS.md`/`GEMINI.md` path. Use `memory-bank/adapters/ANTIGRAVITY.md` only as a template for projects or tools that explicitly need a dedicated root adapter.
- Browser-capable IDE agents should use their built-in browser for exploratory UI debugging and route to Playwright MCP only when the task asks for MCP or repeatable browser automation.
