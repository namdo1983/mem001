# 20 - Engineering Loop

## Input Type Classification

Before choosing a work lane, classify the input. Use the classification to route work to the right artifact instead of creating duplicate plans.

- New spec: a project specification that must become GSD project artifacts, product context, requirements, roadmap, or initial phases.
- Spec slice: a selected behavior from accepted requirements that should become a GSD phase, phase spec, or plan.
- Change request: a bounded behavior change, bug fix, or product refinement.
- New initiative: a larger product area that needs multiple phases, stories, or a milestone.
- Maintenance request: dependency, architecture, performance, security, documentation, or operational work.
- Harness improvement: a process, rule, template, proof, adapter, or memory change that improves future agent work.

GSD remains the lifecycle engine when `.planning/` exists or the user invokes GSD. Memory-bank remains the quick project contract. Do not duplicate the same source of truth across `.planning/`, `memory-bank/`, and `docs/product/`.

## Complexity Assessment

Before software changes, silently score the task across scope, risk, ambiguity, architecture impact, and user impact.

- Fast Track: small, clear, low risk. Implement directly after confirming understanding internally.
- Standard: multiple files or moderate risk. Use a short plan and proceed in validated steps.
- Full Lifecycle: broad, risky, ambiguous, or architectural. Produce requirements/design checkpoints before implementation.

User-facing tier mapping:

- Tier 1 Lightweight maps to Fast Track: typos, minor docs, small style-only edits, and other low-risk changes.
- Tier 2 Standard maps to Standard: new bounded features, single-area refactors, new components, or moderate documentation/process updates.
- Tier 3 Critical maps to Full Lifecycle: database schema changes, broad refactors, core logic fixes, security-sensitive changes, or hard-gate risk flags. Propose a plan, document risks, and ask for explicit confirmation before editing.

## Risk Flags

Escalate the complexity lane when the work touches these areas:

- Auth: login, logout, sessions, tokens, passwords, refresh behavior.
- Authorization: roles, permissions, tenant or company scope.
- Data model: schemas, migrations, uniqueness, deletion, retention.
- Audit/security: audit logs, privacy, sensitive data, access logs.
- External systems: email, payments, cloud services, provider SDKs, queues, webhooks, Jenkins, PocketBase integrations.
- Public contracts: API shape, response envelope, user-visible behavior, import/export formats.
- Cross-platform: browser, mobile, desktop, CLI, or runtime differences.
- Existing behavior: already implemented or test-covered behavior changes.
- Weak proof: unclear, missing, or brittle validation around the affected area.
- Multi-domain: more than one product domain changes at once.

Classification guidance:

- 0-1 flags: Fast Track or Standard based on code impact.
- 2-3 flags: Standard with stronger verification.
- 4+ flags: Full Lifecycle.
- Any hard gate is Full Lifecycle unless the user explicitly narrows scope: auth, authorization, data loss or migration, audit/security, external provider behavior, or removing validation requirements.

## Operating Loop

1. Understand the project context.
2. Restate the work item internally: input type, complexity lane, affected docs/artifacts, and validation shape.
3. For code changes, apply `25-code-change-safety.md` before editing.
4. Make the smallest meaningful change.
5. Review the diff for unintended logic changes.
6. Verify the change.
7. Document progress if project state changed.
8. Capture product delta and harness delta before completion.
9. Repeat until complete.

## Guardrails

- Prefer existing patterns over new abstractions.
- Keep changes scoped to the requested behavior.
- Do not revert unrelated user work.
- Do not alter working logic unless requested or proven wrong.
- Do not claim success before verification.
- Ask the user only when a required decision cannot be inferred safely.

## Handoff

When pausing or splitting work across agents, include:

- Goal.
- Completed work.
- Files changed.
- Current state.
- Remaining steps.
- Verification already run.
- Risks or decisions still open.
