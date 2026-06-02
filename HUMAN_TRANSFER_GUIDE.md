# Human Transfer Guide

This file is for humans preparing to copy this harness into a new project, usually as `memory-bank/`.

It is not part of the default `00-HARNESS.md` load order. Agents should not read this file unless the user explicitly asks for transfer or reset guidance.

## New Project Reset Prompt

Use this prompt after copying the harness into a new repository as `memory-bank/`:

```text
Read memory-bank/00-HARNESS.md first. Then reset this memory-bank for the current project:
- Keep the harness, rules, playbooks, and adapter structure.
- Remove or archive project-specific facts from the previous repository.
- Rewrite projectBrief, productContext, systemPatterns, techContext, activeContext, progress, changelog, and verificationMatrix from the current repo.
- Keep only generic cross-agent lessons in consolidated_learnings.
- Do not delete safety, verification, code-change, Serena, OOP, or design-pattern rules.
- Report every file changed and what old project assumptions were removed.
```

If the harness is installed at repository root instead, replace `memory-bank/00-HARNESS.md` with `00-HARNESS.md` in the prompt.

## What To Keep

- `00-HARNESS.md`
- `rules/`
- `playbooks/`
- `adapters/`
- Generic cross-agent lessons in `consolidated_learnings.md`

## What To Rewrite

- `projectBrief.md`
- `productContext.md`
- `systemPatterns.md`
- `techContext.md`
- `activeContext.md`
- `progress.md`
- `changelog.md`
- `verificationMatrix.md`

## What To Remove Or Archive

- Old project history in `activeContext.md`
- Old repository changelog entries
- Project-specific lessons that do not apply to the new repo
- References to old stack, modules, services, product names, private paths, credentials, endpoints, or customer data
- `raw_reflection_log.md` scratch notes from the old project
- `HARNESS_BACKLOG.md` items that only applied to the old project
