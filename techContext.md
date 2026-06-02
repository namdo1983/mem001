# Tech Context

## Stack

- Markdown documentation.
- Git for version control.
- PowerShell-friendly commands on Windows.
- Optional Serena MCP for memory and semantic code navigation.
- Optional browser, graph, or index tools when the active task needs them.

## Common Commands

- List files: `Get-ChildItem -Recurse -File`
- Search files when `rg` works: `rg --files`
- Search text with PowerShell fallback: `Get-ChildItem -Recurse -File | Select-String -Pattern '<pattern>'`
- Review status: `git status --short`
- Review diff: `git diff -- <path>`

## Verification Commands

- Markdown/path sanity check: inspect changed Markdown files and run a local search for stale path prefixes or project-specific leftovers.
- Git diff review: `git diff -- <changed paths>`
- No build or test runner is required for this harness source unless future scripts are added.

## Environment

- Current workspace is Windows.
- Files should remain UTF-8.
- Durable comments or guidance should avoid unusual Unicode and decorative symbols.
- Serena local state lives in `.serena/` and is ignored by Git.

## Agent Notes

- Prefer `rg` for search when it is available and executable; otherwise use the PowerShell fallback.
- Activate Serena MCP and recall memories at the start of a task when Serena is connected.
- Use sequential-thinking MCP at the start of every session/task and during error recovery.
- Keep harness edits in small Baby Steps and verify after each meaningful change.
