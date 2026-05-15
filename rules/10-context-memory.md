# 10 - Context and Memory Rules

## Required Startup

At the start of every task, read the memory-bank load chain from `00-HARNESS.md`. Do not rely on session memory alone.

## Memory File Roles

- `projectBrief.md`: scope and source of truth.
- `productContext.md`: user value and product behavior.
- `systemPatterns.md`: architecture and implementation patterns.
- `techContext.md`: commands, stack, setup, constraints.
- `activeContext.md`: current focus, decisions, recent events.
- `progress.md`: status, remaining work, known risks.
- `changelog.md`: chronological changes.
- `consolidated_learnings.md`: durable lessons.
- `raw_reflection_log.md`: unprocessed task reflections.

## Update Triggers

Before every final response after a non-trivial task, plan, review, design decision, code change, or debugging session, run the Memory Bank Update Check from `memory-bank/00-HARNESS.md`.

Update memory when:

- A project fact changes.
- A significant implementation lands.
- A command, environment constraint, or recurring issue is discovered.
- The user says to update memory.
- Work is paused or handed off.
- Durable architecture, conventions, verification expectations, active decisions, progress, risks, or reusable lessons changed.

Keep `activeContext.md` focused on the latest high-signal events.

