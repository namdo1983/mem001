# Changelog

## [Unreleased] - 2026-05-15

### Added
- Added `memory-bank/rules/05-agent-operating-protocol.md` for agent role, Vietnamese user-facing communication, English Conventional Commits, UTF-8/comment constraints, Serena MCP preference, Planning Mode guard, and security/instruction safety.
- Added `memory-bank/playbooks/c.md` for compact C/C++ routing, module-boundary, ownership/lifetime, ABI/API, RAII, and native design guidance.

### Updated
- Mapped user-facing Tier 1/2/3 task classification onto the existing Fast Track/Standard/Full Lifecycle engineering lanes.
- Added encoding/comment and terminal-safety guardrails to the code-change safety rule.
- Added Serena MCP guidance to the context-tools rule.
- Tightened code-change safety with a Serena-first impact scan, public-symbol reference checks, existing-owner reuse, and pre-completion reference-check evidence.
- Added a coding safety bundle to the router so source-code work loads expert programming, detected language, and design-pattern guidance when relevant.
- Expanded Python, TypeScript, Java, and design-pattern playbooks with concise OOP, SOLID, composition, dependency-boundary, and compatibility guidance.

## [Unreleased] - 2026-05-13

### Added
- Added a POM Component architecture update for `web_app/tests/solar/web_canvas`: `LoginComponent`, `PopupComponent`, `GameComponent`, and contract validation for tested brand methods while preserving existing CLI options and legacy template/config keys.

## [Unreleased] - 2026-05-11

### Updated
- Updated memory bank files (`projectBrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`) to reflect the actual `creqa_automation` project (Python, Pytest, Playwright monorepo) instead of the template content.

## [Unreleased] - 2026-05-08

### Added

- Created portable `memory-bank/` engineering harness.
- Added highest-priority `00-HARNESS.md` load contract.
- Added core project memory files.
- Added rule modules synthesized from relevant `cline/prompts` `.clinerules` Markdown.
- Added cross-agent adapter templates.
- Added routed capability selection via `memory-bank/rules/70-capability-router.md`.
- Added expert playbooks for programming, design patterns, Node/TypeScript, Python, Java, and Playwright/browser debugging.
- Added Antigravity-style browser guidance: use built-in browser for exploratory debug, Playwright MCP for repeatable automation or explicit MCP requests.
- Added uv-first Python workflow guidance adapted from `cline/prompts` `uv-python-usage-guide.md`.
- Added project discovery/workspace boundary rule and rapid prototyping playbook adapted from `cline/prompts` `BrainStorming workspace`.
- Added lightweight C#/.NET detection and documented deferral of the large `c#-guide.md` to preserve harness token efficiency.
- Added harness-experimental-inspired input type and risk flag classification to the engineering loop.
- Added product delta and harness delta reporting to the completion gate.
- Added `verificationMatrix.md` as a behavior-to-proof map for product and harness contracts.
- Added `HARNESS_BACKLOG.md` for proposed harness improvements that should not be applied immediately.
- Added `memory-bank/rules/80-knowledge-graph.md` and moved graphify guidance out of `GEMINI.md`.
- Removed active root `.clinerules/` adapter so durable guidance lives under `memory-bank/`.
- Added `memory-bank/rules/25-code-change-safety.md` to prevent unintended logic changes and require diff review.
- Replaced `80-knowledge-graph.md` with `80-context-tools.md`; Graphify is now optional, not required.
- Updated `memory-bank/README.md` with reuse guidance, local-only vs committed usage, optional GSD/Graphify, safety gate summary, and self-improvement loop.
- Added `memory-bank/harnessEngineering.md`, distilling OpenAI's 2026 harness-engineering article into local criteria and article-to-memory-bank mappings.
- Added harness-engineering source-map, learning, progress, verification, and backlog updates.
- Added `memory-bank/playbooks/fullstack-patterns.md` to require discover-before-create, reuse-before-new, ownership-boundary, duplicate-code, and naming/collision checks across fullstack coding work.
- Routed fullstack pattern enforcement from `memory-bank/rules/70-capability-router.md` and tightened `memory-bank/rules/25-code-change-safety.md` preflight/diff review requirements.
- Removed root `ANTIGRAVITY.md`; Antigravity-style agents should use the shared `AGENTS.md`/`GEMINI.md` path unless a dedicated adapter becomes necessary again.
- Added browser/fullstack automation architecture guidance: default to Page Object + Component Object + Flow Object, keep factories and fixtures thin, use typed data-driven loaders for API/CSV/YAML/JSON cases, and treat Screenplay as an optional extension rather than the baseline.
- Added a highest-priority Memory Bank Update Check requiring agents to update memory-bank automatically after non-trivial tasks, plans, reviews, design decisions, code changes, and debugging sessions when durable project knowledge changes.
