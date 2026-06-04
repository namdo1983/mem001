# 80 - Context Tools

The installed harness is the required project contract. External context tools are optional helpers.

## Required Context

For architecture, debugging, feature, and cross-module questions, start with:

1. Harness load order from `00-HARNESS.md` or the installed entrypoint.
2. `.planning/codebase/` when present.
3. Local search with `rg` / `rg --files`.
4. Source files, tests, configs, and runtime logs.
5. Optional indexes or tools when available.

## Optional Tools

Optional context tools may include Understand-Anything, IDE/LSP indexes, ctags, Sourcegraph, ast-grep, dependency graphs, or GSD codebase maps.

Use them when they are installed and useful, but never require them to complete a task. Do not fail or block work just because an optional context tool is missing.

## Serena MCP

When Serena MCP is available:

- Activate the current project before source exploration.
- Prefer Serena's semantic tools for symbol discovery, references, and targeted source inspection.
- Use Serena alongside `rg`, tests, runtime logs, and diff review; do not treat semantic indexes as a substitute for verification.
- If Serena is unavailable or unsuitable for a non-code file operation, continue with the smallest reliable local tool and report the fallback when relevant.

## Understand-Anything

If `.understand-anything/knowledge-graph.json` exists, Understand-Anything may be used as one optional context source for codebase onboarding, architecture orientation, dependency impact, domain-flow discovery, and knowledge-base exploration.

Use it when it is already installed and useful, especially for:

- Large or unfamiliar repositories where a structural map would reduce blind file reading.
- Architecture or onboarding questions.
- Change-impact questions where `/understand-diff` can complement `git diff`, local search, and source reading.
- Domain or process questions where `/understand-domain` can surface business flows.
- Documentation/wiki questions where `/understand-knowledge` can map a knowledge base.

Guardrails:

- Treat the graph as context, not proof. Verify important claims against source files, tests, configs, logs, or runtime behavior.
- Do not install Understand-Anything, run long graph generation, open dashboards, or modify hooks unless the task needs it and the user approves or the tool is already available.
- Do not commit `.understand-anything/` outputs unless the project or team has chosen to share the graph. If committed, exclude local scratch such as intermediate outputs and diff overlays, and use large-file handling for big graph files.
- Re-run or refresh the graph only when it materially helps the current task; missing or stale graphs must not block baseline work.

Never claim Understand-Anything analysis, dashboard inspection, graph traversal, or diff-impact analysis happened unless the related tool or existing graph was actually used.

Never claim graph traversal, IDE indexing, or other tool-assisted analysis happened unless that tool actually ran.
