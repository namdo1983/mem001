# Changelog

## [Unreleased] - 2026-06-12

### Updated
- Updated README.md philosophy table: removed stale `Verification Matrix` (Repository Harness).
- Updated `.cursorrules` and `AGENTS.md` to use relative paths (`memory-bank/00-HARNESS.md`) and added compliance check rules (Output Anchors) to prevent Gemini/Claude from bypassing rules.

## [Unreleased] - 2026-06-02

### Added

- Added mandatory sequential-thinking MCP usage for every session/task before skills, edits, risky commands, or implementation.
- Added the Baby-Step Contract to require the smallest meaningful step, one accomplishment at a time, validation after each step, and focused progress notes.
- Added a 3-retry Error Recovery Loop: inspect failure, re-run sequential-thinking MCP, retry with a smaller baby step, and stop after 3 failed retries on the same step.
- Added root `AGENTS.md` as a thin adapter for this root-level harness source.
- Added v5-inspired harness refinements: Critical rollback policy, read-only-only parallel execution, no degrade-to-hide-errors safety, complexity-matched reporting, and explicit Serena memory save on durable changes.
- Added Understand-Anything as an optional context-tool pattern for existing knowledge graphs, onboarding, architecture orientation, diff-impact analysis, domain-flow discovery, and knowledge-base exploration.

### Updated

- Cleaned the harness source repository so core memory files describe the portable harness instead of a stale target project.
- Updated `00-HARNESS.md`, README, rules, adapters, and memory files to support both root harness usage and installation as `memory-bank/`.
- Updated verification guidance for Markdown/path sanity checks in this harness source.
- Updated playbooks to remove target-project-specific provider notes and keep guidance generic.
- Updated `.gitignore` to keep Serena local state out of repository changes.
- Updated source map and verification matrix to track the adopted `windsurf-antigravity-rules` `v5.md` lessons.
- Updated source map and verification matrix to track the adopted `Lum1104/Understand-Anything` optional-tool guidance.
- Removed Graphify-specific optional context-tool guidance from active harness rules.

## Historical Summary

- Created a portable cross-agent engineering harness with `00-HARNESS.md`, core memory files, ordered rules, routed playbooks, adapter templates, verification matrix, source map, backlog, and learning capture.
- Added code-change safety, completion reporting, diff review, optional context-tool guidance, routed language/playbook selection, and memory update checks.
- Added harness-engineering criteria for agent legibility, progressive disclosure, enforceable invariants, feedback-loop closure, and entropy control.
