# Expert Programming Playbook

Load when implementing non-trivial code, reviewing architecture, debugging complex behavior, or choosing abstractions.

## Core Principles

- Make illegal states hard to represent.
- Prefer explicit boundaries over shared mutable state.
- Keep dependency direction stable and understandable.
- Optimize for local reasoning: small modules, clear interfaces, narrow side effects.
- Choose boring solutions until complexity earns a stronger pattern.
- Refactor under tests or with a clear characterization check.

## Implementation Standard

For each meaningful change:

1. Identify the behavior or invariant.
2. Find the closest existing project pattern.
3. Add or update tests/checks proportional to risk.
4. Implement the smallest change that satisfies the invariant.
5. Verify and document any durable project learning.

## Code Quality Heuristics

- A file that needs a long explanation probably needs clearer structure.
- A function with many condition branches may want a strategy, map, or state machine.
- A module that imports both UI and persistence concerns is probably crossing layers.
- Repeated data-shape conversions should be centralized at a boundary.
- Comments should explain why, not narrate what obvious code does.

## Debugging Standard

Use root-cause debugging:

- Reproduce the issue.
- Gather evidence at component boundaries.
- Compare with a working path.
- Test one hypothesis at a time.
- Fix the cause, not the symptom.

