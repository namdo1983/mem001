# Harness Engineering Distillation

## Source

- OpenAI Engineering, "Harness engineering: leveraging Codex in an agent-first world", Ryan Lopopolo, 2026-02-11: `https://openai.com/index/harness-engineering/`

## Local Reading

This repo uses the installed harness files as the agent-legible system of record. The OpenAI article should not be copied into the harness as another long rule file. Its durable value is a set of criteria for deciding what belongs in the repo, what should become tooling, and what should stay as human judgment.

Use this file as a mapping layer from the article to this repository's harness contract.

## Harness-Engineering Criteria

| Criterion | Local meaning | Primary memory-bank anchors |
| --- | --- | --- |
| Agent legibility | If an agent needs the fact to work reliably, encode it in repo-local Markdown, code, schemas, scripts, tests, or logs. Knowledge outside the repo is invisible during execution. | `00-HARNESS.md`, `README.md`, `rules/10-context-memory.md`, `rules/80-context-tools.md` |
| Progressive disclosure | Keep root adapters and mandatory startup context compact. Route deeper guidance by task, language, and capability instead of loading every rule for every task. | `00-HARNESS.md`, `rules/70-capability-router.md`, `playbooks/` |
| Enforceable invariants | Prefer small, checkable constraints over broad taste instructions. Promote repeated review feedback into rules, tests, linters, scripts, or verification rows. | `rules/25-code-change-safety.md`, `rules/30-testing-verification.md`, `rules/40-review-security-quality.md`, `verificationMatrix.md` |
| Human attention leverage | Humans set intent, acceptance criteria, and judgment calls. Agents handle context gathering, edits, local review, verification, and memory updates. | `rules/20-engineering-loop.md`, `rules/50-cross-agent-orchestration.md` |
| Feedback-loop closure | Bugs, review comments, failed checks, and friction should become memory updates, backlog items, tests, or tool improvements. | `rules/60-documentation-learnings.md`, `raw_reflection_log.md`, `HARNESS_BACKLOG.md`, `consolidated_learnings.md`, `changelog.md` |
| Entropy control | Agent-friendly repos drift unless stale docs, weak patterns, and duplicated guidance are continuously pruned. Prefer small recurring cleanup over large late rewrites. | `progress.md`, `HARNESS_BACKLOG.md`, `consolidated_learnings.md`, `rules/90-source-map.md` |

## Article-to-Memory-Bank Map

| OpenAI lesson | Local mapping | Distilled repo stance |
| --- | --- | --- |
| Humans steer; agents execute. | `20-engineering-loop.md` classifies work, risk, and validation before edits. | The human supplies direction and acceptance pressure; the agent performs the repo work and proves it. |
| A short `AGENTS.md` should act as a table of contents, not an encyclopedia. | Root `AGENTS.md` points to the installed harness entrypoint; deeper rules live in the harness. | Keep adapters thin. Do not move durable guidance back into root files. |
| Repository knowledge is the system of record. | Core memory files, rules, playbooks, changelog, source map, backlog, and verification matrix are versioned project artifacts. | Decisions that matter to future agents should land in the installed harness, `.planning/`, code, tests, or docs, not chat-only memory. |
| Agent legibility beats human-only convenience. | Router-selected playbooks and source maps make intent discoverable without overwhelming startup context. | Prefer repo structures that agents can inspect and verify over opaque external process. |
| Application state, logs, metrics, and UI should be directly inspectable by agents. | Browser and context-tool policy lives in `70-capability-router.md` and `80-context-tools.md`; UI work routes to browser proof when relevant. | Do not claim browser/log/graph inspection unless the tool actually ran. Add richer observability only when project work needs it. |
| Architecture and taste should be encoded as invariants. | Safety gate, review/security rules, design-pattern playbook, and verification matrix define protected boundaries. | State the invariant and proof path; avoid micromanaging implementation style unless drift repeats. |
| High agent throughput changes merge strategy. | Current repo intentionally keeps verification and diff review strict. | Do not import low-blocking merge philosophy until automated proof is strong enough for this project. |
| Agent-generated means docs, tests, tooling, and review artifacts too. | `60-documentation-learnings.md` and completion gate require memory updates when durable facts change. | Treat harness docs and verification artifacts as first-class engineering output. |
| Autonomy depends on encoded tooling and recovery loops. | Commands live in `techContext.md`; verification expectations live in `30-testing-verification.md` and `verificationMatrix.md`. | Only claim autonomy for loops that are actually executable in this repo. |
| Entropy requires recurring garbage collection. | `HARNESS_BACKLOG.md`, `raw_reflection_log.md`, `consolidated_learnings.md`, and `changelog.md` form the memory-bank cleanup path. | Turn repeated friction into small cleanup tasks, not occasional sweeping rewrites. |

## Adoption Filter

Adopt article-derived ideas directly when they:

- Make future agent work more legible from repo-local artifacts.
- Preserve the compact load order and routed-playbook model.
- Can be checked by a command, diff review, matrix row, or clear manual proof.
- Strengthen existing safety, verification, review, or memory contracts.

Put ideas in `HARNESS_BACKLOG.md` first when they require new cadence, tooling, CI checks, doc linting, quality scoring, observability infrastructure, or cross-agent automation.

Defer ideas when they mainly optimize for high-throughput merging, require heavy custom infrastructure, or weaken the current safety gate without replacing it with stronger proof.

## Current Fit

Strong alignment:

- `00-HARNESS.md` is the map-first entry point inside this root harness source.
- Root adapters are thin and agent-neutral.
- Memory files separate durable project facts from transient reflections.
- Capability routing supports progressive disclosure.
- Safety gate, verification rules, and completion reporting protect existing behavior.

Partial alignment:

- Documentation freshness is mostly manual.
- Verification matrix is manual proof, not a CI-enforced contract.
- Browser, logs, metrics, code maps, and other context tools are optional rather than fully integrated.
- No recurring doc-gardening or quality-score agent exists yet.

Intentional divergence:

- This repo does not adopt minimal blocking merge gates by default.
- This repo does not prefer reimplementing dependencies solely for agent legibility unless there is a concrete local reason.
- This repo keeps optional indexes and code maps as helpers only; source reading and verification remain the baseline.

## Maintenance Rule

When adding future harness-engineering lessons:

1. Map the lesson to an existing harness file before creating a new one.
2. If it changes a durable rule, update the rule and `changelog.md`.
3. If it proposes a larger structural improvement, add it to `HARNESS_BACKLOG.md`.
4. If it changes a protected behavior, add or update `verificationMatrix.md`.
5. If it is a general lesson, capture it in `raw_reflection_log.md` first, then consolidate when stable.
