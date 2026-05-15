# 90 - Source Map

This harness was synthesized from relevant Markdown files in `https://github.com/cline/prompts/tree/main/.clinerules`.

## Included Source Themes

- `memory-bank.md`: core memory-bank structure and mandatory startup memory read.
- `temporal-memory-bank.md`: recent-event window and changelog concept.
- `general-development-rules.md`: environment awareness, concise communication, progressive work.
- `workflow-rules.md`: standardized reusable workflow shape.
- `ai-dlc-adaptive-workflow.md`: complexity-based process levels.
- `baby-steps.md`: smallest meaningful validated steps.
- `testing-strategy.md`: tests as first-class deliverables and test pyramid.
- `code-review.md`: severity-first review process.
- `codebase-onboarding.md`: top-down architecture and entrypoint analysis.
- `gemini-comprehensive-software-engineering-guide.md`: architecture, debugging, quality, security, reliability.
- `sequential-thinking.md`: use structured reasoning for complex tasks.
- `claude-code-subagents.md`: parallel agent and handoff concepts.
- `new-task-automation.md`: context handoff structure.
- `cline-continuous-improvement-protocol.md`: raw reflections and consolidated learnings.
- `writing-effective-clinerules.md`: modular rule design with clear triggers and metadata.
- `uv-python-usage-guide.md`: uv-first Python project management, environment handling, dependency commands, quality checks, security, cache, and troubleshooting guidance.
- `BrainStorming workspace`: workspace/project boundary rules, rapid prototyping, template activation, cross-project knowledge, cleanup cadence, and automatic memory concepts.

## Excluded or Not Directly Imported

Domain-specific rules for C#, Next.js/Supabase, Vercel, Helm, Google Apps Script, audio plugins, vanilla web stacks, slides, MCP server development, and research-specific workflows were not imported directly because this project is a React + Refine + PocketBase dashboard. Their general engineering principles are covered by the included modules. Python-specific uv guidance is imported into the routed Python playbook because it is useful when `memory-bank/` is copied into Python projects.

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

`https://openai.com/index/harness-engineering/` was reviewed as agent-first engineering guidance. The local harness maps its useful ideas into `memory-bank/harnessEngineering.md`: agent legibility, progressive disclosure, repo-local knowledge, enforceable invariants, feedback-loop closure, and entropy control. Its high-throughput merge philosophy is intentionally not adopted as a default because this repo's safety gate requires diff review and verification before completion claims.
