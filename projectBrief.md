# Project Brief

## Project

This repository is a portable memory-bank engineering harness for AI coding agents.

## Core Goal

Provide a clean, reusable operating contract that helps agents work safely across repositories by combining project memory, sequential reasoning, baby-step execution, verification, and durable learning capture.

## Harness Goal

Keep one compact source of truth that can be installed into another project as a `memory-bank/` folder or used directly from this root repository.

## Success Criteria

- `00-HARNESS.md` is the highest-priority rule inside the installed harness.
- Root adapters, including `AGENTS.md`, stay thin and point agents back to the harness entrypoint.
- Every agent session runs sequential-thinking MCP before skills, edits, risky commands, or implementation.
- Work is broken into Baby Steps and validated after each meaningful step.
- Error recovery retries the same failing step at most 3 times before reporting the blocker to the user.
- Durable changes automatically update memory files and connected Serena MCP memory before final response.
- Memory files describe the active project or installed harness accurately, without stale project-specific facts.
