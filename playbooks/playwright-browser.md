# Playwright and Browser Debug Playbook

Load for UI debugging, browser automation, screenshots, console/network inspection, E2E tests, Playwright MCP, or IDE browser work.

## Capability, Not Language

Playwright/browser automation is independent of language. Combine this playbook with the active language playbook:

- Node/TypeScript + Playwright for `@playwright/test`.
- Python + Playwright for `pytest-playwright` or Playwright Python.
- Java + Playwright for JUnit/TestNG-based browser flows.

## Default Automation Architecture

Use a pragmatic Page Object Model plus Flow baseline for durable browser and fullstack automation. Keep it simple enough that a team can extend it in its own style without inheriting a heavy framework.

Default layers:

```text
Test / Scenario
  -> Flow Object: business workflow, for example login or create job
    -> Action Object: reusable technical action, for example upload file or select table row
      -> Page Object / Component Object: DOM boundary and locators
        -> Driver / Browser / API client
```

Rules:

- Prefer Page Objects and Component Objects for DOM structure.
- Prefer Flow Objects for user-facing or business workflows that span pages/components.
- Use Action Objects only for repeated technical actions that would otherwise duplicate low-level steps.
- Keep factories and fixtures thin: create browser contexts, pages, clients, test users, and data. Do not put workflow logic in factories.
- Keep assertions in tests or expectation/question helpers. Page Objects may verify that the page/component is loaded, but should not own business assertions.
- Keep selectors in Page/Component Objects, not in tests, flows, data files, or factories.
- Keep DOM handles lazy: Playwright should expose `Locator`; Selenium-style frameworks should keep `By` or resolver functions instead of long-lived element instances.
- Use Screenplay only when the project already needs actor/ability/task vocabulary, multi-persona acceptance scenarios, or mixed UI/API activities. Do not start with full Screenplay ceremony by default.

Recommended folders can be adapted to the stack:

```text
tests/
  pages/
  components/
  actions/
  flows/
  fixtures/
  data/
    builders/
    cases/
```

## Data-Driven Test Baseline

Use typed parameterized tests plus data builders/loaders. Data should describe inputs and expected outcomes; code should still own workflows, selectors, waits, and assertions.

Good sources:

- In-code typed case arrays for small, stable suites.
- CSV/YAML/JSON when QA or external systems maintain case data.
- Internal API data when the test environment provides a stable test-data service.

Guardrails:

- Load API/CSV/YAML/JSON data through a typed loader or schema validator before tests use it.
- Normalize external data into language-native case objects such as dataclasses, TypeScript interfaces, or Java records.
- Keep case data small and domain-focused. Split large files by feature or workflow.
- Do not build a YAML/JSON-driven flow engine unless the project explicitly needs a DSL and accepts the debugging cost.
- Do not mix selectors, actions, expected outcomes, and environment configuration in one data file.
- Cache or snapshot API-provided test data when live API dependency would make tests flaky.

Idiomatic shapes:

- Python/pytest: `pytest.mark.parametrize` with dataclasses, `TypedDict`, or Pydantic validation for external data.
- TypeScript/Playwright: `const cases = [...] satisfies TestCase[]`, schema validation with Zod or JSON Schema when loading external files.
- Java/JUnit 5: `@ParameterizedTest` with `@MethodSource`, Java records, and Jackson or a schema validator for external data.

## Debug Routing

For UI debugging:

1. Use the IDE built-in browser when available for fast visual inspection.
2. Use Playwright MCP when the user asks for MCP, when automation should be repeatable, or when E2E artifacts matter.
3. Use Playwright CLI/test runner when MCP is unavailable but automation is still needed.
4. Capture console errors, network failures, URL/state, and screenshots where useful.

Do not claim browser inspection happened unless an actual browser, MCP tool, or Playwright command ran.

## Antigravity-Style IDE Browser

If the IDE provides a built-in browser or browser subagent:

- Use it for exploratory debugging, screenshots, recordings, console/network inspection, and quick UI verification.
- Ask for or invoke Playwright MCP only when repeatability, headless runs, cross-browser coverage, or test generation is needed.
- If the built-in browser fails to open, report the failure and fall back to Playwright MCP or CLI if configured.

## MCP Playwright

Common stdio config:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "timeout": 30000,
      "disabled": false
    }
  }
}
```

Windows alternatives if plain `npx` fails:

```json
{ "command": "npx.cmd", "args": ["-y", "@playwright/mcp@latest"] }
```

```json
{ "command": "cmd", "args": ["/c", "npx", "-y", "@playwright/mcp@latest"] }
```

Use headed mode for local visual debugging. Use `--headless` for CI or non-visual automation.

## Locator and Test Standards

- Prefer accessible locators: role, label, placeholder, text, test id.
- Avoid brittle CSS/XPath unless no better user-facing anchor exists.
- Replace hard sleeps with condition-based waits.
- Keep tests isolated: fresh context/state per test unless sharing is explicit and safe.
- Use traces, screenshots, and videos for debugging flaky or complex flows.
- For durable tests, use page objects or screen objects only when flows repeat enough to justify the abstraction.

## Failure Investigation

When a browser flow fails:

1. Read the exact error.
2. Capture current URL, visible text, console errors, network failures, and screenshot.
3. Check whether the selector, app state, auth state, route, or timing is the root cause.
4. Make the smallest fix and re-run the same flow.

