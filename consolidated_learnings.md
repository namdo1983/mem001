# Consolidated Learnings

## Cross-Agent Harness

- Keep one highest-priority file that defines load order and conflict resolution.
- Keep agent-specific files as adapters only. Shared behavior belongs in the harness, not in duplicated per-agent rules.
- Memory files should describe durable project facts; transient discoveries go into `raw_reflection_log.md` until consolidated.
- Use routed expert playbooks instead of always-on language rules. This preserves context while still giving depth when Python, Java, Node/TypeScript, Playwright, or design-pattern work is detected.
- Treat browser automation as a capability separate from language. Combine `playwright-browser.md` with the active language playbook when needed.
- For Python projects with `uv.lock`, `[tool.uv]`, or established uv commands, route through the Python playbook and prefer `uv sync`, `uv run`, `uv add/remove`, and `uv lock` over ad hoc pip/venv commands.
- For prototype work, preserve speed without polluting production memory: time-box experiments, capture the hypothesis and outcome, then promote, iterate, or archive.
- Maintain workspace/project boundaries so reusable templates and global rules do not overwrite project-specific context.
- Keep language playbooks opt-in and compact. For large source guides such as C#/.NET, route detection can exist without bundling a heavy playbook until real project work needs it.
- Treat working behavior as a protected contract. Agents must inspect impact, preserve existing logic unless change is requested or proven necessary, review diffs for unintended behavior changes, and verify the original symptom or feature before completion.
- Keep code indexes and graph tools optional. Memory-bank, `.planning/codebase/`, local search, source reading, tests, and diff review are the baseline safety system.
- For reusable harnesses, keep root adapters thin and put durable guidance in `memory-bank/`. Cline-style self-improvement should become explicit memory updates or backlog proposals, not automatic root rule churn.
- When importing user-provided agent protocols, synthesize them into compact routed rule modules and existing engineering lanes instead of pasting a second monolithic prompt that can drift or conflict.
- OpenAI-style harness engineering maps cleanly onto this memory-bank when treated as criteria, not copied as a monolithic manual: agent legibility, progressive disclosure, enforceable invariants, human-attention leverage, feedback-loop closure, and entropy control.
- Do not import high-throughput agent merge practices unless the repository has equally strong mechanical proof. In this repo, the strict safety gate remains the default.
- To prevent agent-coded fragmentation, fullstack work needs an explicit discover-before-create rule: search existing symbols and domain patterns, reuse or extend owners, and report duplicate/shadowing checks before completion.
- For coding agents, "best practices" must be operationalized as an impact scan and reference-check contract first, then routed OOP/design guidance second. Pattern advice alone does not prevent accidental deletion or duplicated owners.
- For browser/fullstack automation, the practical default should be POM + Component + Flow with typed data-driven loaders. Screenplay can scale well in teams that choose its vocabulary, but it should not be the baseline because it adds ceremony and onboarding cost.

## Project

- The project uses Refine, MUI, and PocketBase. New UI and data changes should fit those existing provider/hook patterns.
- PocketBase realtime behavior is sensitive to request headers; preserve the current bypass for realtime endpoints.
- `web_canvas` should keep its automation architecture as unified `BrandPage` facade + POM components + `GameActions` + `BrandConfig`: public test methods and legacy template keys stay stable, while repeated login/popup/game canvas mechanics live in components and are protected by contract tests.
