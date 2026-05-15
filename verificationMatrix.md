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
| Memory-bank harness loads before other repo guidance | `memory-bank/00-HARNESS.md` | no | no | no | yes | Root adapters point agents to `memory-bank/00-HARNESS.md` | implemented |
| Product and harness deltas are reported at completion | `memory-bank/00-HARNESS.md` | no | no | no | yes | Completion gate requires product delta and harness delta | implemented |
| Task intake classifies input type, complexity, and risk | `memory-bank/rules/20-engineering-loop.md` | no | no | no | yes | Engineering loop defines input types and risk flags | implemented |
| Agents follow repository communication, encoding, tool, and planning-mode protocol | `memory-bank/rules/05-agent-operating-protocol.md`; `memory-bank/rules/20-engineering-loop.md`; `memory-bank/rules/80-context-tools.md` | no | no | no | yes | Agent protocol defines Vietnamese user-facing communication, English Conventional Commits, UTF-8/comment constraints, Serena MCP preference, and Planning Mode read-only guard | implemented |
| Code changes require safety gate and diff review | `memory-bank/rules/25-code-change-safety.md` | no | no | no | yes | Safety rule blocks unrelated edits, speculative rewrites, validation weakening, and unexplained behavior changes | implemented |
| Source-code changes require impact scanning and routed OOP/design guidance | `memory-bank/rules/25-code-change-safety.md`; `memory-bank/rules/70-capability-router.md`; `memory-bank/playbooks/design-patterns.md`; detected language playbook | no | no | no | yes | Safety gate requires Serena-first impact scans and public-symbol reference checks; router loads expert programming, language, and design-pattern guidance for code work involving APIs, abstractions, module boundaries, or new classes/services/helpers | implemented |
| Context tools are optional and Graphify is not required | `memory-bank/rules/80-context-tools.md` | no | no | no | yes | Context rule treats memory-bank, planning docs, local search, source, and tests as baseline; Graphify is optional | implemented |
| Progressive disclosure keeps startup context compact | `memory-bank/00-HARNESS.md`; `memory-bank/rules/70-capability-router.md` | no | no | no | yes | Harness load order starts with compact core files; router loads only matching expert playbooks | implemented |
| External harness-engineering lessons pass through local adoption criteria | `memory-bank/harnessEngineering.md` | no | no | no | yes | Distillation doc defines adopt, backlog, and defer filters before changing durable rules | implemented |
| Fullstack coding checks existing patterns before creating new code | `memory-bank/playbooks/fullstack-patterns.md`; `memory-bank/rules/25-code-change-safety.md`; `memory-bank/rules/70-capability-router.md` | no | no | no | yes | Router loads the playbook for coding tasks; safety gate requires pattern/symbol search and duplicate checks before completion | implemented |
| Browser/fullstack automation defaults to POM + Component + Flow with typed data-driven cases | `memory-bank/playbooks/playwright-browser.md`; `memory-bank/playbooks/fullstack-patterns.md`; `memory-bank/rules/70-capability-router.md` | no | no | no | yes | Playbook defines the automation layers, data-driven guardrails, language-specific parameterization shapes, and router triggers for Page Object/Flow Object automation architecture | implemented |
| `web_canvas` preserves public CLI, legacy config keys, and tested brand methods while using POM components | `web_app/tests/solar/web_canvas/AGENTS.md`; `web_app/tests/solar/web_canvas/docs/README.md`; `tests/test_web_canvas_pom_contract.py` | yes | no | partial | yes | Contract test checks component wiring, public `BrandPage` methods, required template keys, and image assets; live brand runs still require credentials | implemented |
| Agents run a Memory Bank Update Check before final responses after non-trivial tasks | `memory-bank/00-HARNESS.md`; `memory-bank/rules/10-context-memory.md` | no | no | no | yes | Highest-priority harness requires automatic memory updates when durable project facts, decisions, progress, risks, verification expectations, or lessons change; context-memory rule repeats the trigger | implemented |

## Evidence Rules

- Unit proof covers pure logic and isolated helpers.
- Integration proof covers provider boundaries, backend enforcement, data integrity, jobs, or external services.
- E2E proof covers user-visible browser flows.
- Manual proof covers documentation-only harness behavior, review evidence, screenshots, or command output that is not automated yet.
- A behavior can be implemented without every proof column if the source artifact explains why narrower proof is enough.
