# 90 - Source Map

This harness was synthesized from relevant Markdown files in `https://github.com/cline/prompts/tree/main/.clinerules`.

## Included Source Themes

- `memory-bank.md`: core memory-bank structure and mandatory startup memory read.
- `temporal-memory-bank.md`: recent-event window and changelog concept.
- `general-development-rules.md`: environment awareness, concise communication, progressive work.
- `workflow-rules.md`: standardized reusable workflow shape.
- `ai-dlc-adaptive-workflow.md`: complexity-based process levels.
- `baby-steps.md`: smallest meaningful validated steps, now codified as the Baby-Step Contract in `00-HARNESS.md` and `rules/20-engineering-loop.md`.
- `testing-strategy.md`: tests as first-class deliverables and test pyramid.
- `code-review.md`: severity-first review process.
- `codebase-onboarding.md`: top-down architecture and entrypoint analysis.
- `gemini-comprehensive-software-engineering-guide.md`: architecture, debugging, quality, security, reliability.
- `sequential-thinking.md`: use structured reasoning for every session/task and during error recovery.
- `claude-code-subagents.md`: parallel agent and handoff concepts.
- `new-task-automation.md`: context handoff structure.
- `cline-continuous-improvement-protocol.md`: raw reflections and consolidated learnings.
- `writing-effective-clinerules.md`: modular rule design with clear triggers and metadata.
- `uv-python-usage-guide.md`: uv-first Python project management, environment handling, dependency commands, quality checks, security, cache, and troubleshooting guidance.
- `BrainStorming workspace`: workspace/project boundary rules, rapid prototyping, template activation, cross-project knowledge, cleanup cadence, and automatic memory concepts.

## Excluded or Not Directly Imported

Domain-specific rules for C#, Next.js/Supabase, Vercel, Helm, Google Apps Script, audio plugins, vanilla web stacks, slides, MCP server development, and research-specific workflows were not imported directly because this repository is a general-purpose harness source, not an application project. Their general engineering principles are covered by the included modules. Python-specific uv guidance is imported into the routed Python playbook because it is useful when the harness is copied into Python projects.

`c#-guide.md` was reviewed and intentionally deferred. It is a large C# learning guide for Python/TypeScript developers, not a compact harness rule. The router detects C#/.NET markers, but a C# playbook should be added only for actual .NET work and should stay small.

## Adaptation Notes

The source rules are Cline-oriented. This harness converts them into neutral Markdown contracts and adapter entrypoints so multiple agent families can share the same operating model.

The routed playbook layer extends that synthesis with a Strategy-style capability router: core rules stay always-on, while language and browser automation guidance activates only when relevant.

The BrainStorming workspace source was intentionally narrowed: stack-specific defaults and broad cleanup commands were not imported, while portable workspace discovery, template activation, prototype promotion/archive, and memory behaviors were retained.

## Later Inspiration

`https://github.com/hoangnb24/harness-experimental` was reviewed as a blank harness template. The local harness did not copy its structure wholesale because GSD and memory-bank already provide lifecycle and project memory. The following reusable ideas were adapted:

- Input types for feature intake.
- Risk flags and lane escalation.
- Product delta plus harness delta as completion concepts.
- Behavior-to-proof verification matrix.
- Harness backlog for structural improvements that should not be applied immediately.

`https://github.com/cline/prompts/blob/main/.clinerules/self-improving-cline.md` was reviewed as a self-improvement prompt. Its useful idea is an explicit reflection checkpoint after feedback-heavy or multi-step work. The local harness maps that idea to `raw_reflection_log.md`, `HARNESS_BACKLOG.md`, `consolidated_learnings.md`, and `changelog.md` instead of requiring active `.clinerules`.

`https://openai.com/index/harness-engineering/` was reviewed as agent-first engineering guidance. The local harness maps its useful ideas into `harnessEngineering.md`: agent legibility, progressive disclosure, repo-local knowledge, enforceable invariants, feedback-loop closure, and entropy control. Its high-throughput merge philosophy is intentionally not adopted as a default because this repo's safety gate requires diff review and verification before completion claims.

`https://github.com/kinopeee/windsurf-antigravity-rules/blob/main/en/.agent/rules/v5.md` was reviewed as a compact coding-assistance rule. The local harness already covered most of it through task lanes, safety gates, verification, and completion reporting. The useful additions adopted here are:

- Full Lifecycle and Critical plans include rollback policy.
- Parallel execution is limited to independent read-only operations; state-changing actions stay sequential.
- Agents must not degrade types, contracts, assertions, or functionality to hide errors.
- Lightweight versus standard reporting should match task complexity without exposing long private reasoning traces.
- Durable changes must update both file memory and connected Serena MCP memory before final response.

`https://github.com/Lum1104/Understand-Anything` was reviewed as an optional codebase and knowledge-graph tool. The local harness does not require it, but `rules/80-context-tools.md` now documents how to use an existing `.understand-anything/knowledge-graph.json` or installed Understand-Anything commands for onboarding, architecture orientation, diff-impact analysis, domain-flow discovery, and knowledge-base exploration. It remains context only; source reading, tests, logs, runtime checks, and diff review remain the proof baseline.
