# Cross-Agent Engineering Harness

Priority: highest. If this file is present, every agent working in this project MUST read it before repository code, local plans, or lower-priority rule files.

This harness is agent-neutral. It is written for Codex, Gemini, Claude/Cline, Antigravity-style agents, and any compatible coding assistant. Tool names differ by agent, but the operating contract is the same.

## Load Order

Read these files in order at the start of every task:

1. `memory-bank/00-HARNESS.md`
2. `memory-bank/projectBrief.md`
3. `memory-bank/productContext.md`
4. `memory-bank/systemPatterns.md`
5. `memory-bank/techContext.md`
6. `memory-bank/activeContext.md`
7. `memory-bank/progress.md`
8. `memory-bank/changelog.md`
9. `memory-bank/consolidated_learnings.md`
10. `memory-bank/rules/*.md` in lexical order
11. Routed playbooks from `memory-bank/playbooks/*.md` selected by `memory-bank/rules/70-capability-router.md`

Conflict rule: lower-numbered files win. Later files may add detail, but MUST NOT weaken safety, verification, or memory requirements from earlier files.

## Mission

Provide a portable engineering harness that can be copied between projects and still preserve:

- Project memory across sessions.
- Methodical planning matched to task complexity.
- Small, validated implementation steps.
- Test and build verification before completion claims.
- Review-first quality standards.
- Cross-agent handoff and orchestration conventions.
- Continuous learning capture.
- Routed expert playbooks for language, browser automation, and design-pattern capabilities.
- Workspace/project discovery rules for safe use across single projects, monorepos, and prototype workspaces.

## Start-of-Task Protocol

For every task:

1. Read the load-order chain above.
2. Identify the project state, active work, relevant commands, and known risks.
3. Classify the input type and task complexity using `memory-bank/rules/20-engineering-loop.md`.
4. For code changes, apply the safety gate in `memory-bank/rules/25-code-change-safety.md` before editing and before completion.
5. Run the capability router from `memory-bank/rules/70-capability-router.md` and load only matching playbooks.
6. Execute with the smallest meaningful steps.
7. Verify with the cheapest reliable command set.
8. Update memory files when project facts, decisions, or progress changed.

## Memory Bank Update Check

Before every final response after a non-trivial task, plan, review, design decision, code change, or debugging session, run a Memory Bank Update Check.

Update memory-bank automatically when any of these changed:

- Project facts, stack, setup, commands, or environment constraints.
- Architecture, conventions, patterns, or active decisions.
- Completed work, current progress, remaining work, or known risks.
- Verification commands, test expectations, or proof requirements.
- Reusable lessons, repeated friction, or mistakes that should not repeat.

Do not wait for the user to ask for memory updates.

If no durable project knowledge changed, report:

`Memory-bank update: not needed.`

## Completion Gate

Before saying work is complete, the agent MUST report:

- Files created or changed.
- Product delta: behavior, code, tests, API shape, data model, or product documentation that changed.
- Harness delta: memory, rules, commands, validation expectations, backlog items, or lessons that changed.
- Diff safety review for code changes: whether every changed hunk maps to the requested behavior.
- Verification commands run and their outcomes.
- Any tests or checks that could not be run.
- Any memory-bank updates made.

If verification fails, completion is not allowed. Report the failure and continue fixing unless the user asks to stop.

## Portability Contract

To apply this harness to another project:

1. Copy the entire `memory-bank/` folder.
2. Add or copy the matching adapter from `memory-bank/adapters/` to the repository root when the target agent requires a root entrypoint.
3. Keep `memory-bank/00-HARNESS.md` as the highest-priority rule.
4. Let `memory-bank/rules/70-capability-router.md` choose language and capability playbooks for the target project.

For this project, root adapters have already been added so the harness is loaded first.
