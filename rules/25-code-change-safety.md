# 25 - Code Change Safety Gate

This gate exists to prevent agents from breaking working logic while debugging or adding features. It applies to every code change, including Fast Track work.

## Prime Directive

Do not change working behavior unless the user requested that behavior change or the existing behavior is proven wrong by requirements, tests, logs, or reproducible evidence.

If the task is ambiguous, preserve current behavior and make the smallest local fix.

## Before Editing Code

Before touching source files, identify and keep in mind:

1. The affected behavior and user-visible outcome.
2. The smallest file or module that can satisfy the request.
3. Callers, consumers, hooks, providers, routes, tests, and data contracts that depend on the code.
4. Existing proof: tests, build checks, screenshots, logs, UAT notes, or manual reproduction.
5. A rollback-safe edit shape: no broad rewrites, no unrelated cleanup, no style churn.
6. Existing patterns and symbols that might already satisfy the request. Search before creating new files, exports, hooks, services, routes, schemas, models, repositories, helpers, or shared types.

Use available context tools, but do not depend on any single optional tool. If an IDE index, code map, or optional context tool is unavailable, use `rg`, source reading, tests, and `.planning/codebase/` artifacts.

Before editing code, run sequential-thinking MCP to identify the affected behavior, smallest safe edit shape, and validation path.

## Serena-First Impact Scan

When Serena MCP is available for source code:

1. Activate the current project before code exploration.
2. Use symbol overview/search to locate the existing owner of the behavior.
3. Use reference lookup before deleting, renaming, moving, or changing the signature/meaning of any public function, class, method, fixture, hook, route, model, field, config key, or exported symbol.
4. If references are unclear or cross-tool lookup is unavailable, preserve backward compatibility with a wrapper, adapter, or narrow extension unless the user explicitly requested a breaking change.
5. If Serena is unavailable or the file type is unsuitable, use `rg`, source reading, and tests as the fallback impact scan.

Do not start implementation from a new abstraction until the existing owner and references have been checked.

## During Editing

- Keep the change scoped to the requested behavior.
- Preserve public contracts unless the task explicitly changes them.
- Preserve data shape, status values, auth semantics, realtime behavior, and API headers unless the task explicitly changes them.
- Preserve UTF-8 text encoding. Code comments should be English or Vietnamese without accents, and should avoid decorative symbols or unusual Unicode characters.
- Do not rename, move, or reformat unrelated code.
- Do not replace a working implementation with a speculative abstraction.
- Do not remove existing public functions, classes, methods, fixtures, hooks, routes, models, fields, config keys, or exports just because a new implementation looks cleaner.
- Do not insert new code into an unrelated owner when a closer module, class, service, or helper already owns the behavior.
- Do not introduce duplicate services, hooks, helpers, DTOs, schemas, or data mappers when an existing owner can be reused or extended.
- Do not shadow existing variables, exports, field names, status values, config keys, or route names with a different semantic meaning.
- Do not silence errors, remove validation, or weaken tests to make checks pass.
- Do not degrade types, contracts, assertions, or functionality to hide errors. If a temporary workaround is unavoidable, keep it narrow and document the reason, risk, and follow-up.
- Do not delete fallback behavior without proving it is dead or harmful.
- If unrelated issues are discovered, record them in `HARNESS_BACKLOG.md`, `.planning`, or the final notes instead of fixing them opportunistically.

## Terminal Safety

- Prefer the narrowest command that verifies the requested behavior.
- Do not run destructive commands, drop databases, delete generated evidence, or mutate external systems unless the user explicitly approved that action.
- If a command fails, inspect the failure signal before changing code or rerunning broader commands.
- For repeated failures, use the Error Recovery Loop in `20-engineering-loop.md`: re-run sequential-thinking MCP, retry with a smaller Baby Step, and stop after 3 failed retries on the same step.

## Debugging Gate

For bug fixes:

1. Reproduce or identify the failure signal before changing code when feasible.
2. State the suspected cause in terms of observed evidence.
3. Prefer a regression test or narrow verification command.
4. If no automated test surface exists, capture a manual verification path.
5. After the fix, verify the original symptom, not just lint/build.

## Feature Gate

For features:

1. Implement the smallest vertical slice that satisfies the accepted scope.
2. Keep old flows working unless the feature intentionally replaces them.
3. Reuse or extend the closest existing domain pattern before adding a new one.
4. Add or update proof at the lowest reliable layer.
5. Update `verificationMatrix.md` when the behavior becomes a durable contract item.

## Pre-Completion Diff Review

Before claiming completion after code changes:

1. Review `git diff` for every touched source file.
2. Confirm each changed hunk maps to the requested behavior.
3. Confirm any changed or removed public symbol had a reference check, or explain why the symbol is private/local.
4. Confirm no unrelated logic, formatting churn, dependency changes, generated files, or local user changes were swept in.
5. Confirm new files, exports, hooks, services, routes, schemas, models, repositories, helpers, and shared types were not duplicates of existing project patterns.
6. Run the relevant verification from `rules/30-testing-verification.md`.
7. Report any skipped checks and why.

Completion is blocked if diff review reveals unexplained behavior changes.
