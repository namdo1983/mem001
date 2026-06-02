# 10 - Context and Memory Rules

## Required Startup

At the start of every task, read the memory-bank load chain from `00-HARNESS.md`. Do not rely on session memory alone.

When Serena MCP is available, activate the project and recall existing memories with `list_memories` or `read_memory` before implementation. This recall is part of startup, not an optional final cleanup step.

After startup memory recall, run sequential-thinking MCP before selecting skills, editing files, running risky commands, or implementing a fix.

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

Before every final response after a non-trivial task, plan, review, design decision, code change, or debugging session, run the Memory Bank Update Check from `00-HARNESS.md`.

Update memory when:

- A project fact changes.
- A significant implementation lands.
- A command, environment constraint, or recurring issue is discovered.
- The user says to update memory.
- Work is paused or handed off.
- Durable architecture, conventions, verification expectations, active decisions, progress, risks, or reusable lessons changed.

Keep `activeContext.md` focused on the latest high-signal events.

When Serena MCP is available, mirror durable session updates into Serena memory with `write_memory` or `edit_memory` before the final response. Do not wait for the user to ask. If the update cannot be saved, report the blocker and what still needs to be written.

