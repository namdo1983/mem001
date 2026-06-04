# Cross-Agent Engineering Harness

Priority: highest. If this file is present, every agent working in this project MUST read it before repository code, local plans, or lower-priority rule files.

This harness is agent-neutral. It is written for Codex, Gemini, Claude/Cline, Antigravity-style agents, and any compatible coding assistant. Tool names differ by agent, but the operating contract is the same.

## Repository Shape

This repository is the harness source itself. Core memory files, rules, playbooks, and adapter templates live at the repository root:

- Core memory files: `projectBrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `activeContext.md`, `progress.md`, `changelog.md`, `consolidated_learnings.md`.
- Rule modules: `rules/*.md` in lexical order.
- Routed playbooks: `playbooks/*.md`.
- Adapter templates: `adapters/*.md`.

When this harness is installed into another repository as a `memory-bank/` folder, keep the same internal file layout under that folder and update the root adapter path accordingly.

## Load Order

Read these files in order at the start of every task:

1. `00-HARNESS.md`
2. `projectBrief.md`
3. `productContext.md`
4. `systemPatterns.md`
5. `techContext.md`
6. `activeContext.md`
7. `progress.md`
8. `changelog.md`
9. `consolidated_learnings.md`
10. `rules/*.md` in lexical order
11. Routed playbooks from `playbooks/*.md` selected by `rules/70-capability-router.md`

Conflict rule: lower-numbered files win. Later files may add detail, but MUST NOT weaken safety, verification, memory, sequential-thinking, or baby-step requirements from earlier files.

## Mission

Provide a portable engineering harness that can be copied between projects and still preserve:

- Project memory across sessions.
- Sequential task reasoning through the sequential-thinking MCP.
- Baby-step execution with small, validated changes.
- Test and build verification before completion claims.
- Review-first quality standards.
- Cross-agent handoff and orchestration conventions.
- Continuous learning capture.
- Routed expert playbooks for language, browser automation, and design-pattern capabilities.
- Workspace/project discovery rules for safe use across single projects, monorepos, and prototype workspaces.

## Mandatory Reasoning Gate

For every new session and every user task, the agent MUST call the sequential-thinking MCP after loading the harness context and before selecting skills, changing files, running risky commands, or implementing a fix.

The sequential-thinking pass must identify:

1. **Clarification Gate:** Identify any ambiguities, assumptions, or missing requirements in the user request. Stop and ask the user or explicitly document assumptions if critical details are missing.
2. **Consistency Check (Alignment):** Confirm that the proposed plan and tasks fully align with the project brief and tech context constraints without introducing duplicate plans.
3. The requested outcome.
4. The smallest meaningful next step.
5. Relevant risks, affected files, and validation shape.
6. Whether the task needs Fast Track, Standard, or Full Lifecycle handling.
7. The current retry number when recovering from a failed step.

If sequential-thinking MCP is unavailable, the agent must report that limitation before proceeding and use a short written reasoning substitute. Do not silently skip the gate.

## Baby-Step Contract

All execution uses Baby Steps:

1. Break the task into the smallest meaningful step.
2. Complete one substantive accomplishment at a time.
3. Validate after each step with the cheapest reliable check.
4. Document progress when durable project knowledge or harness state changed.
5. Start the next step only after the current step is complete or explicitly blocked.

Baby-step execution is inspired by Cline's `baby-steps.md`: smallest meaningful change, one accomplishment at a time, complete and validate each step, and keep focused progress notes. The harness paraphrases that source instead of copying it wholesale.

## Start-of-Task Protocol

For every task:

1. Read the load-order chain above.
2. Activate and recall project memory when Serena MCP is available.
3. Run the Mandatory Reasoning Gate with sequential-thinking MCP.
4. Identify project state, active work, relevant commands, and known risks.
5. Classify the input type and task complexity using `rules/20-engineering-loop.md`.
6. For code changes, apply the safety gate in `rules/25-code-change-safety.md` before editing and before completion.
7. Run the capability router from `rules/70-capability-router.md` and load only matching playbooks.
8. Execute with Baby Steps.
9. Verify with the cheapest reliable command set.
10. Update memory files and Serena memory when project facts, decisions, progress, verification expectations, or reusable lessons changed.

## Error Recovery Loop

When a command, test, edit, or validation step fails:

1. Stop broad implementation and inspect the failure signal.
2. Increment the retry counter for the current failing step.
3. Re-run sequential-thinking MCP to re-break the task around the observed failure.
4. Pick the next smallest baby step that can test one hypothesis.
5. Run only the narrow validation needed for that hypothesis.
6. Record the outcome and continue if it resolves the failure.

If the same step fails after 3 retries, break the loop. Do not keep spinning. Report to the user:

- The failing step.
- The 3 attempts made.
- The evidence collected.
- The suspected blocker.
- The decision or external input needed to continue.

## Memory Bank Update Check

Before every final response after a non-trivial task, plan, review, design decision, code change, or debugging session, run a Memory Bank Update Check.

Update memory files automatically when any of these changed:

- Project facts, stack, setup, commands, or environment constraints.
- Architecture, conventions, patterns, or active decisions.
- Completed work, current progress, remaining work, or known risks.
- Verification commands, test expectations, or proof requirements.
- Reusable lessons, repeated friction, or mistakes that should not repeat.

Do not wait for the user to ask for memory updates.

If Serena MCP is available, also save durable changes with `write_memory` or `edit_memory` before the final response. A non-trivial task with changed durable knowledge is not complete until file memory and connected MCP memory are updated or a blocker is reported.

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
- Any memory updates made.

If verification fails, completion is not allowed. Enter the Error Recovery Loop unless the user asks to stop or the 3-retry cap is reached.

## Portability Contract

To apply this harness to another project:

1. Copy this harness into the target repository, usually as `memory-bank/`.
2. Add or copy the matching adapter from `adapters/` to the target repository root.
3. Ensure the adapter points to the actual installed path, such as `memory-bank/00-HARNESS.md` or `00-HARNESS.md`.
4. Keep `00-HARNESS.md` as the highest-priority rule within the installed harness.
5. Let `rules/70-capability-router.md` choose language and capability playbooks for the target project.
