# Harness Backlog

Use this file when an agent discovers a missing harness capability but should not change the operating model immediately. Small clarifications tied to the current task may be patched directly; structural changes should start here.

## Template

```md
## Missing Harness Capability

### Title
Short name.

### Discovered While
Task or phase that exposed the gap.

### Current Pain
What was hard, repeated, ambiguous, or unsafe?

### Suggested Improvement
What should be added or changed?

### Risk
Fast Track | Standard | Full Lifecycle

### Status
proposed | accepted | implemented | rejected
```

## Items

## Missing Harness Capability

### Title
Memory-bank freshness checks.

### Discovered While
Mapping OpenAI's harness-engineering article into the local memory-bank.

### Current Pain
The harness has strong Markdown contracts, but freshness, cross-links, and drift are reviewed manually.

### Suggested Improvement
Add a lightweight script or checklist that verifies required core files exist, root adapters point to `memory-bank/00-HARNESS.md`, important memory-bank links resolve, and changelog/source-map updates accompany structural harness changes.

### Risk
Standard

### Status
proposed

## Missing Harness Capability

### Title
Agent-legibility quality score.

### Discovered While
Mapping OpenAI's harness-engineering article into the local memory-bank.

### Current Pain
The repo has a `verificationMatrix.md`, but no compact score or review cadence for whether project knowledge remains easy for future agents to navigate.

### Suggested Improvement
Define a small quality rubric for agent legibility: compact entrypoint, routed docs, current commands, proof coverage, stale-doc risk, and optional-tool clarity. Keep it manual until repeated drift justifies automation.

### Risk
Fast Track

### Status
proposed
