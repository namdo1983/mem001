# Verification Matrix

This file maps important product and harness behaviors to proof. Do not mark a behavior implemented unless validation evidence exists or the row explains why executable proof is not available.

## Status Values

| Status | Meaning |
| --- | --- |
| planned | Accepted as intended behavior, not implemented yet |
| in_progress | Actively being built or verified |
| implemented | Implemented and proof exists |
| changed | Contract changed after earlier implementation |
| retired | No longer part of the product or harness contract |

## Matrix

| Behavior | Source | Unit | Integration | E2E | Manual | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Harness entrypoint loads before other repo guidance | `AGENTS.md`; `00-HARNESS.md`; `adapters/AGENTS.md`; `adapters/CLAUDE.md`; `adapters/GEMINI.md` | no | no | no | yes | Root adapter, load order, and adapter templates point agents to the installed harness entrypoint | implemented |
| Agents run sequential-thinking MCP for every session/task | `00-HARNESS.md`; `rules/05-agent-operating-protocol.md`; `rules/10-context-memory.md`; `rules/20-engineering-loop.md` | no | no | no | yes | Mandatory Reasoning Gate requires sequential-thinking MCP before skills, edits, risky commands, or implementation | implemented |
| Baby Steps drive implementation and recovery | `00-HARNESS.md`; `rules/05-agent-operating-protocol.md`; `rules/20-engineering-loop.md` | no | no | no | yes | Baby-Step Contract and engineering loop require one smallest meaningful step with validation after each step | implemented |
| Repeated failures stop after 3 retries on the same step | `00-HARNESS.md`; `rules/20-engineering-loop.md`; `rules/25-code-change-safety.md` | no | no | no | yes | Error Recovery Loop requires sequential-thinking re-break, smaller baby-step retries, and user reporting after 3 failures | implemented |
| Product and harness deltas are reported at completion | `00-HARNESS.md` | no | no | no | yes | Completion gate requires product delta, harness delta, verification, skipped checks, and memory updates | implemented |
| Task intake classifies input type, complexity, and risk | `rules/20-engineering-loop.md` | no | no | no | yes | Engineering loop defines input types, complexity lanes, risk flags, and escalation rules | implemented |
| Agents follow repository communication, encoding, tool, and planning-mode protocol | `rules/05-agent-operating-protocol.md`; `rules/20-engineering-loop.md`; `rules/80-context-tools.md` | no | no | no | yes | Agent protocol defines Vietnamese user-facing communication, English Conventional Commits, UTF-8/comment constraints, Serena MCP preference, and Planning Mode read-only guard | implemented |
| Code changes require safety gate and diff review | `rules/25-code-change-safety.md` | no | no | no | yes | Safety rule blocks unrelated edits, speculative rewrites, validation weakening, and unexplained behavior changes | implemented |
| Source-code changes require impact scanning and routed OOP/design guidance | `rules/25-code-change-safety.md`; `rules/70-capability-router.md`; `playbooks/design-patterns.md`; detected language playbook | no | no | no | yes | Safety gate requires Serena-first impact scans and public-symbol reference checks; router loads expert programming, language, and design-pattern guidance when relevant | implemented |
| Context tools are optional and not required | `rules/80-context-tools.md` | no | no | no | yes | Context rule treats harness load order, local search, source, tests, logs, and planning docs as baseline; optional tools may help but must not block work | implemented |
| Progressive disclosure keeps startup context compact | `00-HARNESS.md`; `rules/70-capability-router.md` | no | no | no | yes | Harness load order starts with compact core files; router loads only matching expert playbooks | implemented |
| External harness-engineering lessons pass through local adoption criteria | `harnessEngineering.md` | no | no | no | yes | Distillation doc defines adopt, backlog, and defer filters before changing durable rules | implemented |
| Fullstack coding checks existing patterns before creating new code | `playbooks/fullstack-patterns.md`; `rules/25-code-change-safety.md`; `rules/70-capability-router.md` | no | no | no | yes | Router loads the playbook for coding tasks; safety gate requires pattern/symbol search and duplicate checks before completion | implemented |
| Browser/fullstack automation defaults to POM + Component + Flow with typed data-driven cases | `playbooks/playwright-browser.md`; `playbooks/fullstack-patterns.md`; `rules/70-capability-router.md` | no | no | no | yes | Playbook defines automation layers, data-driven guardrails, language-specific parameterization shapes, and router triggers | implemented |
| Agents run a Memory Bank Update Check before final responses after non-trivial tasks | `00-HARNESS.md`; `rules/10-context-memory.md` | no | no | no | yes | Highest-priority harness requires automatic memory updates when durable project facts, decisions, progress, risks, verification expectations, or lessons change | implemented |
| Durable changes update connected Serena MCP memory automatically | `00-HARNESS.md`; `rules/10-context-memory.md` | no | no | no | yes | Memory rules require `write_memory` or `edit_memory` before final response when Serena MCP is available and durable knowledge changed | implemented |
| Critical plans include rollback policy before implementation approval | `rules/20-engineering-loop.md` | no | no | no | yes | Full Lifecycle plan minimum includes purpose, impact, risks, rollback, verification, and explicit approval | implemented |
| State-changing actions are not parallelized | `rules/05-agent-operating-protocol.md` | no | no | no | yes | Parallel and Command Safety allows parallel read-only operations while keeping edits, dependency changes, destructive commands, and other mutations sequential | implemented |
| Agents do not degrade contracts or functionality to hide errors | `rules/25-code-change-safety.md` | no | no | no | yes | Safety gate blocks degrading types, contracts, assertions, or functionality to make checks pass | implemented |
| Understand-Anything is optional context, not proof | `rules/80-context-tools.md`; `rules/90-source-map.md` | no | no | no | yes | Context-tools rule allows existing `.understand-anything/knowledge-graph.json` or installed commands for orientation and impact analysis, but requires verification against source, tests, logs, runtime behavior, or diff review | implemented |

## Evidence Rules

- Unit proof covers pure logic and isolated helpers.
- Integration proof covers provider boundaries, backend enforcement, data integrity, jobs, or external services.
- E2E proof covers user-visible browser flows.
- Manual proof covers documentation-only harness behavior, review evidence, screenshots, or command output that is not automated yet.
- A behavior can be implemented without every proof column if the source artifact explains why narrower proof is enough.
