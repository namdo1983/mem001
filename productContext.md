# Product Context

## Users

Primary users are developers, QA engineers, technical leads, and AI coding agents that need a consistent working contract across tools and repositories.

## Problems Solved

- Prevent agent sessions from starting with stale or missing project context.
- Keep cross-agent instructions portable without duplicating behavior in every adapter.
- Force methodical reasoning before implementation through sequential-thinking MCP.
- Keep work small, observable, and recoverable through Baby Steps.
- Stop repeated error loops after 3 failed retries and surface the blocker to the user.
- Preserve project knowledge across sessions through memory updates.

## Experience Goals

- Fast startup with a compact load chain.
- Clear rules that are easy for Codex, Gemini, Claude/Cline, and similar agents to follow.
- Small validated changes instead of broad speculative rewrites.
- Honest completion reports with verification evidence and memory updates.
- Clean handoff artifacts for humans and other agents.
