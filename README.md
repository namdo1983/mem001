# Memory Bank

This folder is the portable engineering harness for the project. Agents should begin with `00-HARNESS.md`, then follow the chained core memory files and rule modules.

## Reuse Policy

`memory-bank/` can be kept local-only or committed to a repository.

Use local-only when the memory contains personal workflow notes, private paths, internal URLs, customer data, or temporary debugging details. Add `memory-bank/` to `.gitignore` if it should stay private.

Commit it when you want a reusable personal or team harness. Before committing, remove secrets, tokens, local machine paths, private endpoints, customer data, and overly personal scratch notes. Treat committed memory as project operating documentation.

GSD is optional. If `.planning/` exists or the user invokes GSD, GSD is the lifecycle engine and memory-bank is the quick project contract. Without GSD, agents still use memory-bank, local search, source reading, tests, diff review, and the safety gate.

Graphify and other index tools are optional. They may improve orientation, but the harness must still work with only memory-bank, `rg`, source files, tests, logs, and `.planning/codebase/` when present.

## Install In Another Project

1. Copy `memory-bank/` into the target repository.
2. Copy only the needed root adapter from `memory-bank/adapters/` to the repository root, such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `ANTIGRAVITY.md`.
3. Customize `projectBrief.md`, `productContext.md`, `systemPatterns.md`, and `techContext.md` for the real project.
4. Remove stale project-specific facts from `activeContext.md`, `progress.md`, `changelog.md`, and `verificationMatrix.md`.
5. Keep root adapters thin. Durable guidance belongs in `memory-bank/`.

## Core Files

- `00-HARNESS.md`: highest-priority operating rule.
- `projectBrief.md`: project scope and success definition.
- `productContext.md`: user and product intent.
- `systemPatterns.md`: architecture and implementation patterns.
- `techContext.md`: stack, commands, constraints.
- `activeContext.md`: current state and most recent events.
- `progress.md`: what works, remaining work, risks.
- `changelog.md`: dated project/harness changes.
- `consolidated_learnings.md`: durable lessons.
- `raw_reflection_log.md`: fresh learnings not yet consolidated.
- `verificationMatrix.md`: behavior-to-proof map for product and harness contracts.
- `HARNESS_BACKLOG.md`: proposed harness improvements that should not be applied immediately.
- `harnessEngineering.md`: OpenAI harness-engineering article distilled into local memory-bank criteria.

## Rule Modules

Rules live in `memory-bank/rules/` and are loaded in lexical order. Lower numbers have higher priority.

`20-engineering-loop.md` classifies each input by type, complexity lane, and risk flags. When GSD artifacts exist, GSD remains the lifecycle engine and memory-bank remains the quick project contract.

`25-code-change-safety.md` blocks broad or speculative code edits and requires pre-completion diff review for code changes.

`80-context-tools.md` centralizes optional context tools. Graphify is optional; memory-bank, local search, source reading, tests, and `.planning/codebase/` remain the baseline.

## Safety Gate

The safety gate is the core protection against agents breaking working code.

For every code change, agents must:

- Preserve working behavior unless the user requested a change or evidence proves the behavior is wrong.
- Inspect callers, consumers, data contracts, tests, and runtime flows before editing.
- Keep edits scoped to the requested behavior.
- Avoid speculative rewrites, unrelated cleanup, broad formatting churn, and validation weakening.
- Review `git diff` before completion and confirm every changed hunk maps to the request.
- Verify the original bug or feature behavior, not only lint/build.

If an agent finds unrelated problems, it should record them in `HARNESS_BACKLOG.md`, `.planning`, or final notes instead of opportunistically changing working logic.

## Routed Playbooks

Expert playbooks live in `memory-bank/playbooks/`. They are not all loaded by default. `memory-bank/rules/70-capability-router.md` selects the matching playbooks based on repository files and the current task.

Examples:

- React/Vite task: Node/TypeScript playbook.
- Python task: Python playbook.
- Java task: Java playbook.
- UI debug or E2E task: Playwright/browser playbook plus the active language playbook.
- Browser/fullstack automation task: Playwright/browser playbook for the POM + Component + Flow baseline, plus the active language playbook.
- Feature, bug fix, refactor, API, or fullstack task: fullstack-patterns playbook plus the active language playbook.
- Architecture or refactor task: design-patterns and expert-programming playbooks.
- Prototype/spike/bootstrap task: rapid-prototyping playbook.

## Agent Adapters

Adapter templates live in `memory-bank/adapters/`. For tools that only auto-read root files, copy the relevant adapter to the repository root.

Keep root adapters minimal. Project guidance belongs in `memory-bank/`; root files should only point the tool back to `memory-bank/00-HARNESS.md`.

## Self-Improvement Loop

When a task involved repeated friction, user correction, broken assumptions, missed safety checks, or a reusable lesson, capture it before closing the work:

- Use `raw_reflection_log.md` for fresh task reflections.
- Use `HARNESS_BACKLOG.md` for proposed rule, template, validation, or workflow improvements that should not be applied immediately.
- Move stable lessons into `consolidated_learnings.md`.
- Update `changelog.md` when the harness itself changes.

This replaces Cline-style self-improving `.clinerules` with a memory-bank-native loop. Agents should propose harness improvements, but structural changes should be applied only when they are clearly useful and approved or low-risk.
