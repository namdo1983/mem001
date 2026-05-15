# Rapid Prototyping Playbook

Load for brainstorming sessions, experiments, throwaway prototypes, spikes, proof-of-concepts, or project bootstrap work where fast learning matters more than production hardening.

## Purpose

Move from idea to working evidence quickly while keeping project boundaries and memory clean.

## Time Box

Default to focused 30-60 minute prototype sessions. At the end of the time box, decide whether to:

- Promote: turn the prototype into planned project work.
- Iterate: schedule another focused prototype session.
- Archive: preserve the learning and stop investing.

## Prototype Standards

- Start with the smallest demoable path.
- Use the detected stack and existing templates; do not force a default stack.
- Avoid premature architecture, dependency sprawl, and production-only concerns.
- Name experiments clearly, for example `experiment-*` or `spike-*`, when creating new folders.
- Keep setup instructions short and executable.
- Capture the question the prototype answers.

## Promotion Criteria

Promote a prototype only when it has:

- Clear user or engineering value.
- A known path from prototype quality to production quality.
- Basic verification evidence.
- Documented trade-offs and shortcuts.
- A next-step plan or owner.

## Archive Criteria

Archive or remove a prototype when:

- It answered the question and no further action is needed.
- It is stale, confusing, or duplicated by better work.
- It would mislead future agents if left beside active code.

When archiving, keep a short note with what was learned and why it was not promoted.

## Memory Behavior

Memory updates are infrastructure, not a bonus task.

Capture:

- The hypothesis.
- The prototype approach.
- What worked.
- What failed.
- Reusable patterns.
- Whether the prototype was promoted, iterated, or archived.

Avoid verbose logs. Keep durable insights in `consolidated_learnings.md` and current state in `activeContext.md`.

## Guardrails

- Do not let prototype shortcuts leak into production code without an explicit hardening step.
- Do not update global templates from one experiment unless the pattern repeats or is clearly general.
- Do not run broad dependency updates as part of prototype cleanup.
- Do not claim a prototype proves more than it actually demonstrated.

