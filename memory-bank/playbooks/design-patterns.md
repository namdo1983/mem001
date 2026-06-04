# Design Patterns Playbook

Load when a task involves architecture, refactoring, repeated branching, new module boundaries, or cross-agent harness behavior.

## Pattern Selection Rules

- Start with simple functions and clear modules.
- Use a pattern only when it reduces real complexity or protects a boundary.
- Prefer composition over inheritance unless the language/framework idiom says otherwise.
- Keep pattern names out of code unless they clarify intent.

## OOP and SOLID Guardrails

- Give each class/module one reason to change.
- Keep public interfaces narrow and stable; add adapters or wrappers when compatibility matters.
- Depend on abstractions at external, persistence, UI, and provider boundaries; keep concrete details near the edge.
- Prefer composition, delegation, and small collaborators over deep inheritance trees.
- Use polymorphism or strategy tables when behavior varies by type, provider, state, or runtime and conditionals are spreading.
- Do not introduce a class hierarchy for one-off behavior that simple functions or a local module can express clearly.

## Common Patterns

### Adapter

Use when one interface must fit another without leaking tool-specific details.

Harness use: `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md` adapt different agents to the same installed harness entrypoint. Keep active root `.clinerules/` and extra adapter files absent unless a specific local tool requires them.

### Strategy

Use when behavior varies by language, runtime, provider, or test capability.

Harness use: Node, Python, Java, and Playwright playbooks are strategies selected by `70-capability-router.md`.

### Factory

Use when object creation depends on runtime configuration, provider, environment, or validated input.

Keep construction policy in one owner. Do not scatter `if provider == ...` branches across callers.

### Facade

Use when a stable public API should hide multiple internal collaborators.

Good fit for preserving old tests or callers while moving repeated behavior into smaller components.

### Chain of Responsibility

Use when ordered rules or handlers decide what applies.

Harness use: the load-order chain and lexical rule ordering.

### Template Method

Use when the workflow is stable but steps vary.

Harness use: context -> plan -> implement -> verify -> document remains stable across agents and languages.

### Repository / Gateway

Use for persistence or external service boundaries.

Keep database/API details behind one project-local boundary so application logic does not scatter transport details.

### Observer / Pub-Sub

Use for event streams, realtime updates, and subscriptions.

Keep event subscription, invalidation, and listener cleanup policy in one owner when the project has realtime or pub-sub behavior.

### State Machine

Use when workflows have explicit statuses, transitions, and invalid moves.

Good fit for jobs, agent completion states, uploads, and locks.

### Page Object / Screenplay

Use for browser automation when flows repeat or selectors become noisy.

Keep one-off debug exploration separate from durable E2E test abstractions.

## Anti-Patterns

- Pattern-first design without a repeated problem.
- Global state as a shortcut around boundaries.
- Deep inheritance for behavior that could be composed.
- Generic service classes that hide unrelated responsibilities.
- Test helpers that obscure the behavior being asserted.
- Breaking public callers to make an internal pattern look cleaner.
