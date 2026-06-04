# Progress

## Works

- Root-level harness structure is active: `AGENTS.md`, `00-HARNESS.md`, core memory files, `rules/`, `playbooks/`, and `adapters/`.
- Core load order is documented in `00-HARNESS.md`.
- Rule modules cover task classification, safety, verification, review, orchestration, documentation, capability routing, and optional context tools.
- Routed playbooks exist for Python, Node/TypeScript, Java, C/C++, Playwright/browser automation, design patterns, expert programming, fullstack patterns, and rapid prototyping.
- Mandatory sequential-thinking MCP, Baby Steps, and 3-retry error recovery are now part of the harness contract.
- v5-derived refinements are part of the harness contract: Critical rollback policy, read-only-only parallel execution, no degrade-to-hide-errors safety, complexity-matched reporting, and explicit Serena memory save after durable changes.
- Understand-Anything is documented as an optional context tool for existing knowledge graphs, onboarding, architecture orientation, diff-impact analysis, domain-flow discovery, and knowledge-base exploration.
- Core memory files no longer describe an unrelated automation monorepo.
- Distilled Spec-Kit's Clarification Gate and Consistency Check into the Mandatory Reasoning Gate to improve spec-driven development without adding CLI tools or folder bloat.

## Remaining

- Keep harness memory synchronized as the operating model evolves.
- Keep source-map and verification matrix entries current when new durable rules are added.
- Consider adding a lightweight script for stale-path and required-file checks if manual checks become repetitive.
- Customize memory files after installing the harness into a real target project.

## Known Risks

- Adapter paths can drift when the harness is copied as root versus `memory-bank/`; adapters must be checked after installation.
- Most harness behavior is Markdown-contract behavior, so proof is manual unless validation scripts are added later.
- Optional tools such as Serena, Understand-Anything, browser tools, or IDE indexes may be unavailable in a target agent environment; rules must keep a clear fallback path.
- Understand-Anything graph output can become stale or incomplete; it must not replace source reading, tests, logs, runtime verification, or diff review.
