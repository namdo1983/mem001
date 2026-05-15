# Active Context

## Current Focus

The current work is upgrading the portable cross-agent engineering harness with routed expert capabilities.

## Recent Events

1. 2026-05-08: Cloned `cline/prompts` into `.tmp-cline-prompts` for local reference.
2. 2026-05-08: Reviewed relevant `.clinerules` Markdown files for memory bank, workflow, testing, review, onboarding, engineering best practices, subagents, and continuous improvement.
3. 2026-05-08: Created `memory-bank/` structure and root adapter plan.
4. 2026-05-08: Added routed capability design: core rules always active, language/browser/design playbooks activate by repository/task detection.
5. 2026-05-08: Added Playwright/browser debugging as a capability separate from language runtime, including Antigravity-style built-in browser guidance and MCP fallback rules.
6. 2026-05-08: Added uv-first Python workflow guidance from `cline/prompts` `uv-python-usage-guide.md` into the routed Python playbook.
7. 2026-05-08: Added project discovery/workspace boundary rule and rapid prototyping playbook from `cline/prompts` `BrainStorming workspace`.
8. 2026-05-08: Reviewed `c#-guide.md`; added lightweight C#/.NET detection but deferred a full playbook to keep the harness lean.
9. 2026-05-08: Compared `hoangnb24/harness-experimental` with local GSD + memory-bank usage; adopted only the reusable intake, proof, and backlog patterns instead of copying the blank template.
10. 2026-05-08: Consolidated agent guidance into `memory-bank/`; graphify guidance moved from `GEMINI.md` into `memory-bank/rules/80-knowledge-graph.md`, and active root `.clinerules/` was removed.
11. 2026-05-08: Added a mandatory code-change safety gate and converted Graphify guidance into optional context-tool guidance.
12. 2026-05-08: Updated `memory-bank/README.md` for personal reuse, local-only vs committed usage, optional GSD/Graphify, safety gate, and memory-bank-native self-improvement.
13. 2026-05-11: Reviewed OpenAI's harness-engineering article and distilled it into `memory-bank/harnessEngineering.md`, with source-map, verification, backlog, and learning updates.
14. 2026-05-11: Added `memory-bank/playbooks/fullstack-patterns.md` and routed it into coding work to force discover-before-create, reuse-before-new, duplicate-code checks, and naming/collision guards.
15. 2026-05-11: Removed root `ANTIGRAVITY.md`; Antigravity-style usage now shares `AGENTS.md`/`GEMINI.md` unless a future tool needs a dedicated adapter.
16. 2026-05-11: Added a default browser/fullstack automation architecture baseline: Page Object + Component Object + Flow Object, with typed data-driven loaders for API/CSV/YAML/JSON cases and Screenplay as an optional team-chosen extension.
17. 2026-05-11: Promoted Memory Bank Update Check into `00-HARNESS.md` so copied projects automatically require memory-bank updates after non-trivial tasks when durable knowledge changes.
18. 2026-05-13: Refactored `web_app/tests/solar/web_canvas` toward POM Component by adding login, popup, and game components plus contract validation while preserving CLI options, legacy template keys, and public `BrandPage` test methods.
19. 2026-05-15: Added `memory-bank/rules/05-agent-operating-protocol.md` and tightened engineering/context rules for Vietnamese user-facing communication, English Conventional Commits, UTF-8/comment constraints, Serena MCP preference, tier mapping, Planning Mode safety, and terminal safety.
20. 2026-05-15: Tightened coding safety around Serena-first impact scans, public-symbol reference checks, owner reuse, OOP/design-pattern routing, and added compact Python, TypeScript, Java, and C/C++ design guidance.

## Active Decisions

- Harness artifacts are written in English for cross-tool portability.
- User-facing chat, planning notes, explanations, and status updates should remain Vietnamese unless the user changes language; technical terms and code identifiers stay English.
- Git commit messages must be English Conventional Commits.
- The harness paraphrases and synthesizes source rules instead of copying them wholesale.
- Root adapters exist for this project; adapter templates live inside `memory-bank/adapters/` for portability.
- Durable user operating preferences belong in `memory-bank/rules/05-agent-operating-protocol.md` and should be mapped into existing rule modules instead of pasted as a duplicate monolithic prompt.
- Expert guidance should be routed by `70-capability-router.md`; do not force-load every language playbook for every task.
- Playwright/browser automation is a capability that combines with the active language playbook when needed.
- In Python projects that use `uv`, the Python playbook should treat `uv` as the package, venv, Python version, and command runner authority.
- Brainstorm/prototype/spike/bootstrap tasks should route to `rapid-prototyping.md`; multi-project or new-repo contexts should route through `15-project-discovery.md`.
- C#/.NET should be detected by router markers, but no C# playbook should be added until actual .NET work requires compact guidance.
- GSD is the lifecycle engine when `.planning/` artifacts are present; memory-bank is the quick project contract.
- Blank harness templates should be treated as seed material only. Useful patterns may be extracted, but project truth must stay specific.
- Completion reporting should distinguish product delta from harness delta.
- Important behaviors should be mapped to proof in `verificationMatrix.md` when they become durable contract items.
- Root instruction files should remain thin adapters only. Durable guidance belongs in `memory-bank/`.
- Do not keep a root `ANTIGRAVITY.md` in this repo while Antigravity-style agents can share `AGENTS.md`/`GEMINI.md`.
- Do not keep an active root `.clinerules/` folder unless a specific local tool requires it.
- Agents must not change working logic unless requested or proven wrong.
- Every code change must pass the safety gate: inspect impact before editing, check references before changing public symbols, keep scope narrow, review diff hunks, and verify the original behavior.
- Source-code work must route through the coding safety bundle: `expert-programming.md`, the detected language playbook, and `design-patterns.md` when OOP, public APIs, shared abstractions, module boundaries, dependency direction, or new classes/services/helpers are involved.
- Fullstack coding tasks must load `fullstack-patterns.md` and search existing domain patterns before creating new files, exports, hooks, services, routes, schemas, models, repositories, helpers, or shared types.
- Browser and fullstack automation should default to POM + Component + Flow, keep factories/fixtures thin, keep data-driven cases typed, and avoid custom flow DSLs unless the team explicitly chooses them.
- `web_canvas` now uses a unified `BrandPage` facade composed with `LoginComponent`, `PopupComponent`, and `GameComponent`; future changes should keep business game flow in `brand_actions.py`, repeated canvas interactions in components, and low-level OpenCV/browser mechanics in `BaseCanvas`.
- Agents must run the Memory Bank Update Check before final responses after non-trivial work and update memory-bank without waiting for the user when durable project knowledge changed.
- When Serena MCP is available, agents should activate the current project and prefer Serena semantic inspection before falling back to shell/source reads for code context.
- Graphify and other indexes are optional helpers only. Missing optional tools must not block work or replace source reading and verification.
- Memory-bank may be local-only or committed. If committed, remove secrets, private paths, internal endpoints, customer data, and personal scratch notes first.
- Cline-style self-improvement maps to `raw_reflection_log.md`, `HARNESS_BACKLOG.md`, `consolidated_learnings.md`, and `changelog.md`; do not require root `.clinerules/`.
- OpenAI-style harness engineering is treated as local criteria, not a wholesale rule import: agent legibility, progressive disclosure, enforceable invariants, feedback-loop closure, and entropy control should map to existing memory-bank artifacts first.

## Next Steps

- Keep memory files updated after significant code or process changes.
- Add project-specific lessons to `raw_reflection_log.md` first, then consolidate durable lessons into `consolidated_learnings.md`.
