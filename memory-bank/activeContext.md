# Active Context

## Current Focus

The current work is cleaning this repository into a root-level portable AI-agent harness and removing stale project-specific automation context.

## Recent Events

1. 2026-06-02: Confirmed this repository is the harness source itself, with core files at root and no `memory-bank/` directory in the workspace.
2. 2026-06-02: Reviewed Cline's `baby-steps.md` source and paraphrased its core ideas into the local harness contract.
3. 2026-06-02: Added mandatory sequential-thinking MCP usage for every session/task before skills, edits, risky commands, or implementation.
4. 2026-06-02: Added Baby Steps as the default execution model: smallest meaningful step, one accomplishment at a time, validation after each step, and focused documentation.
5. 2026-06-02: Added an error recovery loop that re-runs sequential-thinking MCP, retries with a smaller baby step, and breaks after 3 failed retries on the same step.
6. 2026-06-02: Removed stale target-project automation and product-stack context from the core harness memory files.
7. 2026-06-02: Added root `AGENTS.md` as a thin adapter that points to `00-HARNESS.md`.
8. 2026-06-02: Reviewed `windsurf-antigravity-rules` `v5.md` and adopted compact additions: rollback policy for Critical plans, read-only-only parallel execution, no degrade-to-hide-errors safety, complexity-matched reporting, and explicit Serena memory save after durable changes.
9. 2026-06-02: Reviewed `Lum1104/Understand-Anything` and adopted it as an optional context-tool pattern for existing knowledge graphs, onboarding, architecture orientation, diff-impact analysis, domain-flow discovery, and knowledge-base exploration.
10. 2026-06-04: Distilled Spec-Kit's Clarification Gate and Consistency Check into the Mandatory Reasoning Gate in 00-HARNESS.md, rules/20-engineering-loop.md, and init_harness.py.
11. 2026-06-12: Updated README.md philosophy table: removed Repository Harness verification matrix.
12. 2026-06-12: Updated .cursorrules and AGENTS.md to use relative paths for 00-HARNESS.md and added strict compliance output anchors for Gemini/Claude.

## Active Decisions

- Harness artifacts are written in concise English for cross-tool portability.
- User-facing chat, planning notes, explanations, and status updates should remain Vietnamese unless the user changes language; technical terms and code identifiers stay English.
- Git commit messages must be English Conventional Commits.
- This repository is the harness source at root. When copied into another repository, it may be installed as `memory-bank/`, but adapters must point to the actual installed path.
- Root adapters should remain thin. Durable guidance belongs in `00-HARNESS.md`, `rules/`, and core memory files.
- Every session/task must use sequential-thinking MCP before skills, edits, risky commands, or implementation.
- Baby Steps are mandatory for execution and recovery: smallest meaningful change, one substantive accomplishment at a time, validate each step, then proceed.
- If the same step fails 3 times, the agent must stop retrying and report the blocker to the user with attempts and evidence.
- Agents must activate and recall Serena MCP memory at startup when Serena is available, then save durable changes before completion.
- Durable changes must update both memory files and connected Serena MCP memory automatically before final response; do not wait for the user to ask.
- Full Lifecycle or Critical plans must include purpose, impact scope, risks, rollback policy, verification approach, and explicit user approval before implementation.
- Parallel execution is for independent read-only operations only. File edits, patches, dependency changes, destructive commands, and other state-changing actions stay sequential.
- Agents must not degrade types, contracts, assertions, or functionality to hide errors.
- Browser tools, code maps, and other indexes are optional helpers only. Missing optional tools must not block baseline work.
- Understand-Anything is optional context only. Use existing `.understand-anything/knowledge-graph.json` or installed commands when helpful, but verify important claims against source, tests, logs, runtime behavior, or diff review.
- Cline-style self-improvement maps to `raw_reflection_log.md`, `HARNESS_BACKLOG.md`, `consolidated_learnings.md`, and `changelog.md`; do not require root `.clinerules/`.
- External prompt sources should be paraphrased into compact local guidance unless exact text is explicitly required.

## Next Steps

- Keep memory files synchronized after significant harness or process changes.
- Keep adapter templates thin and path-aware.
- Add lightweight automated Markdown/path checks only if repeated drift makes the manual check too costly.
