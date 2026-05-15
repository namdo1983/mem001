# Fullstack Patterns Playbook

Load for feature work, bug fixes, refactors, or code generation that touches frontend, backend, API contracts, persistence, validation, jobs, integrations, or shared types.

This playbook exists to stop agent-coded systems from becoming fragmented: duplicated helpers, parallel services, inconsistent data shapes, shadowed variables, and new abstractions that ignore existing project patterns.

## Non-Negotiable Preflight

Before creating a new source file, exported symbol, hook, service, route, schema, model, repository, component, migration, command, or helper:

1. Search for the closest existing domain names, concepts, and data shapes with `rg`.
2. Read the nearest existing implementation and its callers.
3. Identify the owning boundary: UI component, hook, provider, route/controller, service/use case, repository/gateway, schema/model, or shared type.
4. Decide whether to reuse, extend, adapt, or create new.
5. If creating new, name why the existing pattern cannot safely absorb the change.

Useful searches:

```bash
rg -n "DomainName|domainName|domain_name|endpoint|collection|table|status|typeName|useThing|ThingService" .
rg --files | rg "domain|feature|service|repository|schema|model|hook|provider|component|route|controller"
```

Use stack-native search when better tools exist, but do not skip the search step.

## Reuse Decision

Choose in this order:

1. **Reuse existing behavior** when it already satisfies the requirement.
2. **Extend the existing owner** when the new behavior belongs to the same domain and boundary.
3. **Adapt at a boundary** when an external API, library, framework, or legacy shape must fit local conventions.
4. **Create a new module** only when responsibility is genuinely separate and callers can understand the boundary without reading internals.

Do not create a parallel abstraction just because it is faster in the moment.

## Ownership Boundaries

Keep one clear owner for each durable concept:

| Concept | Preferred owner | Avoid |
| --- | --- | --- |
| API contract | route/controller DTO, shared schema, or API client boundary | ad hoc request/response shapes in UI components |
| Validation | schema/model/form boundary closest to input | duplicated validation in every caller |
| Persistence | repository/gateway/model layer | direct database/client calls scattered through UI or services |
| External provider | adapter/gateway/client wrapper | provider SDK calls across unrelated modules |
| UI state | component or hook that owns the interaction | global/shared state for local behavior |
| Domain workflow | service/use-case/state machine | status strings and branching copied across screens |
| Data mapping | boundary mapper/normalizer | repeated shape conversion in callers |
| Browser automation | Page/Component Objects plus Flow Objects | selectors, waits, and workflows duplicated across tests or data files |

When a boundary already exists in the repo, follow it even if its name differs from this table.

## Browser and Fullstack Automation

When creating or refactoring browser automation, use the `playwright-browser.md` baseline even when the concrete stack is Selenium, WebdriverIO, Playwright Python, Playwright TypeScript, or Playwright Java.

Default to Page Object Model plus Flow Objects:

- Page/Component Objects own DOM structure, locators, component-level waits, and page readiness checks.
- Flow Objects own business workflows across pages, components, API setup, or job/status transitions.
- Action Objects own repeated technical interactions only when they remove real duplication.
- Fixtures/factories create drivers, contexts, authenticated sessions, API clients, pages, users, and test data. They should not run business workflows.
- Data-driven tests should load API, CSV, YAML, or JSON into typed case objects before execution.

Avoid introducing a custom Screenplay-style framework unless the team has explicitly chosen that vocabulary. The default should stay easy to debug, type-friendly, and close to the browser framework's native primitives.

## Language and Stack Patterns

### TypeScript / React / Node

- Reuse existing components, hooks, providers, resources, API clients, and shared types before adding new ones.
- Keep rendering in components; keep stateful behavior in hooks; keep backend access in providers/clients/gateways.
- Put response normalization at the API/provider boundary, not in every component.
- Prefer discriminated unions or literal status types for workflow state.
- Do not create duplicate types for the same payload; export and reuse the owning type or derive a narrow local view.

### Python

- Keep routes/controllers, schemas, services/use cases, repositories/gateways, and external clients separate when the project has those layers.
- Reuse Pydantic models, dataclasses, TypedDicts, and serializers before introducing another shape.
- Keep file/network/database I/O at edges; keep transformation logic testable and locally pure where practical.
- Do not hide broad behavior behind generic utility modules when a domain module already exists.

### Java / Spring

- Prefer controller -> service/use case -> repository/gateway direction.
- Keep DTOs, entities, and domain models distinct when they carry different responsibilities.
- Reuse constructor injection, transaction boundary, mapper, and validation conventions already present.
- Do not leak persistence objects into API responses unless that is the existing project contract.

### C# / .NET

- Prefer controller/minimal API -> application service -> repository/gateway direction.
- Reuse existing DI, options, DTO, result, validation, and EF/Core repository conventions.
- Keep mapping between API models, domain models, and persistence models at a boundary.
- Avoid static global helpers for behavior that should be injected, configured, or tested.

### Fullstack Contract

- Preserve names, status values, field meanings, and response envelopes unless the requested change explicitly changes the contract.
- Update both sides of a shared contract together, or add a compatibility adapter.
- Do not make UI assumptions about backend defaults unless the backend contract says so.
- Do not create a second source of truth for roles, permissions, statuses, feature flags, collection/table names, or environment variables.

## Naming and Collision Guard

Before adding or renaming symbols:

- Check for existing names in the same domain and adjacent layers.
- Avoid suffixes like `New`, `V2`, `Temp`, `Final`, `Manager`, `Helper`, or `Util` unless the repo already has a specific convention for them.
- Do not shadow an outer variable when the old binding is still used nearby.
- Do not reuse a familiar name with a different semantic meaning.
- Do not overwrite public exports, environment keys, config keys, route names, collection names, field names, or status strings without tracing consumers.

Prefer precise names that describe the domain role: `JobResultsGateway`, `normalizeAgentResult`, `useUploadLock`, `TaskStatus`, `RunSummary`.

## Duplicate-Code Guard

When code looks similar to existing code:

- If the same business rule appears twice, centralize it at the owning boundary.
- If the same mapping appears twice, create or reuse a mapper near the API/data boundary.
- If branches differ only by strategy, use a strategy table, map, or polymorphic handler.
- If UI repeats structure with minor content changes, extract a component only when the repetition is stable and improves clarity.
- If tests duplicate setup, use a fixture/helper only when it keeps the asserted behavior obvious.

Small local duplication is acceptable when abstraction would hide behavior or cross boundaries.

## Anti-Patterns

- Adding a new service/hook/type because the existing one was not searched.
- Creating parallel names such as `JobService2`, `useJobsNew`, `TaskResultV2`, or `agentResultHelper`.
- Spreading the same validation, status mapping, or response normalization across UI, API, and persistence layers.
- Mixing UI rendering, data fetching, transformation, and mutation in one large module when local patterns already separate them.
- Replacing a working pattern with a speculative architecture.
- Silencing type, lint, or test failures by widening types, deleting validation, or weakening assertions.

## Completion Proof

Before completion, report the pattern check:

- Existing patterns searched.
- Files or symbols reused/extended.
- New files or symbols created and why they were necessary.
- Duplicate or shadowing risks reviewed.
- Verification command or manual proof used.
