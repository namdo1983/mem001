# 80 - Context Tools

Memory-bank is the required project contract. External context tools are optional helpers.

## Required Context

For architecture, debugging, feature, and cross-module questions, start with:

1. `memory-bank/` load order.
2. `.planning/codebase/` when present.
3. Local search with `rg` / `rg --files`.
4. Source files, tests, configs, and runtime logs.
5. Optional indexes or tools when available.

## Optional Tools

Optional context tools may include Graphify, IDE/LSP indexes, ctags, Sourcegraph, ast-grep, dependency graphs, or GSD codebase maps.

Use them when they are installed and useful, but never require them to complete a task. Do not fail or block work just because an optional context tool is missing.

## Serena MCP

When Serena MCP is available:

- Activate the current project before source exploration.
- Prefer Serena's semantic tools for symbol discovery, references, and targeted source inspection.
- Use Serena alongside `rg`, tests, runtime logs, and diff review; do not treat semantic indexes as a substitute for verification.
- If Serena is unavailable or unsuitable for a non-code file operation, continue with the smallest reliable local tool and report the fallback when relevant.

## Graphify

If `graphify-out/` exists, Graphify may be used as one optional context source:

- Read `graphify-out/GRAPH_REPORT.md` for architecture or codebase orientation when useful.
- If `graphify-out/wiki/index.md` exists, use it as an index before deep raw-file reading.
- For cross-module relationship questions, `graphify query`, `graphify path`, or `graphify explain` may complement `rg` and source reading.
- After modifying code files, run `graphify update .` only when Graphify is installed, available, and appropriate. If it is unavailable, do not treat that as a task failure; report that the graph was not updated if relevant.

Never claim graph traversal, IDE indexing, or other tool-assisted analysis happened unless that tool actually ran.
