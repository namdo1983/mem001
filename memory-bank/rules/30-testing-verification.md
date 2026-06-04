# 30 - Testing and Verification

## Testing Contract

Tests or equivalent checks are mandatory for code changes unless the user explicitly opts out or no relevant test surface exists.

Verification must prove the requested behavior and must not rely on lint/build alone when the task is a bug fix or user-visible feature.

Use the test pyramid:

- Unit tests for isolated logic.
- Integration tests for provider/API/module boundaries.
- End-to-end checks for critical user flows.

## For This Project

Prefer these checks as applicable:

- Markdown/path sanity check for changed harness files.
- `git diff -- <changed paths>` for scoped diff review.
- Local search for stale installed-path prefixes or stale project names when cleaning harness docs.
- Syntax, lint, build, or test commands from the target repository after the harness is installed into an actual code project.

If a dedicated test runner or validation script is added later, document it in `techContext.md` and use it before completion.

## Completion Evidence

Before completion, report:

- Whether `git diff` was reviewed for unintended logic changes.
- The command run.
- Whether it passed or failed.
- Any skipped checks and why.
