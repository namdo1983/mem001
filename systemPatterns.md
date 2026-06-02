# System Patterns

## Architecture

The repository is a Markdown-first harness. Its structure is intentionally flat at the root so agents can load the entrypoint and memory files quickly.

Key patterns:

- Highest-priority contract: `00-HARNESS.md`.
- Core memory: project, product, system, tech, active context, progress, changelog, and learnings files.
- Ordered rules: `rules/*.md`, loaded in lexical order with lower numbers carrying higher priority.
- Routed playbooks: `playbooks/*.md`, loaded only when the task or repository markers require them.
- Thin adapters: `adapters/*.md`, copied to a target repository root when an agent needs an auto-loaded entrypoint.

## Operating Flow

1. Load `00-HARNESS.md` and the memory chain.
2. Activate and recall Serena MCP memory when available.
3. Run sequential-thinking MCP before skills, edits, risky commands, or implementation.
4. Classify the task by type, complexity, and risk.
5. Execute the smallest meaningful Baby Step.
6. Validate the step.
7. On failure, re-run sequential-thinking MCP, retry a smaller hypothesis-driven Baby Step, and stop after 3 failed retries on the same step.
8. Update memory and completion evidence when durable facts changed.

## Design Rules

- Keep root adapters minimal; durable behavior belongs in the harness.
- Prefer compact rules over monolithic prompts.
- Keep external prompt sources as paraphrased local guidance unless exact text is required.
- Keep optional tooling optional. Missing browser tools, code maps, or semantic indexes must not block the baseline workflow.
- Keep stale product-specific facts out of this harness source repository.
