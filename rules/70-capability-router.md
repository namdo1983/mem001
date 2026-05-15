# 70 - Capability Router

The core harness is always active. Expert playbooks are loaded only when the repository or task indicates they are relevant.

## Routing Contract

At the start of implementation or debugging work:

1. Detect languages and capabilities from files, manifests, user request, and active task.
2. Load only the matching files from `memory-bank/playbooks/`.
3. If multiple capabilities apply, load all relevant playbooks.
4. When uncertain, prefer the smallest relevant set and state the assumption.

## Language Detection

- Node/TypeScript: `package.json`, `tsconfig.json`, `vite.config.*`, `*.ts`, `*.tsx`, `*.js`, `*.jsx`.
- Python: `pyproject.toml`, `requirements.txt`, `uv.lock`, `poetry.lock`, `.python-version`, `*.py`.
- Java: `pom.xml`, `build.gradle`, `settings.gradle`, `*.java`.
- C/C++: `CMakeLists.txt`, `Makefile`, `configure.ac`, `meson.build`, `*.c`, `*.h`, `*.cpp`, `*.cc`, `*.cxx`, `*.hpp`, `*.hh`.
- C#/.NET: `*.sln`, `*.csproj`, `Directory.Build.props`, `Directory.Packages.props`, `global.json`, `*.cs`. No C# playbook is bundled by default; use core expert/design/testing rules unless a real .NET task justifies adding `memory-bank/playbooks/csharp-dotnet.md`.

## Capability Detection

- Playwright/browser automation: `playwright.config.*`, `@playwright/test`, `pytest-playwright`, Playwright Java/.NET dependencies, Selenium/WebdriverIO browser test dependencies, `tests/e2e`, UI debug requests, screenshot requests, console/network inspection, locator/test flake work, Page Object/Flow Object automation architecture.
- Frontend UI: React/Vue/Svelte/Angular source, CSS, browser-rendered behavior, visual layout, accessibility, responsive design.
- Backend/API: controllers, routes, services, serializers, repositories, database migrations, auth, integration boundaries.
- Fullstack pattern enforcement: feature work, bug fixes, refactors, or code generation that touches frontend, backend, API contracts, persistence, validation, jobs, integrations, shared types, or cross-layer data flow.
- Architecture/design: new module boundaries, complex features, refactors, dependency direction, domain modeling, repeated conditional logic.
- Rapid prototyping/workspace management: user asks for brainstorm, prototype, spike, experiment, bootstrap, template activation, workspace cleanup, project discovery, or multi-project organization.

## Coding Safety Bundle

For any source-code feature, bug fix, refactor, or generated code:

1. Always apply `memory-bank/rules/25-code-change-safety.md`.
2. Load `memory-bank/playbooks/expert-programming.md`.
3. Load the detected language playbook.
4. Load `memory-bank/playbooks/design-patterns.md` when the work touches OOP, public APIs, shared abstractions, repeated branching, module boundaries, dependency direction, or any new class/service/helper.
5. Load `memory-bank/playbooks/fullstack-patterns.md` for frontend, backend, API, persistence, validation, integration, shared-type, or cross-layer changes.

## Routed Playbooks

Load these as needed:

- `memory-bank/playbooks/expert-programming.md`
- `memory-bank/playbooks/design-patterns.md`
- `memory-bank/playbooks/fullstack-patterns.md`
- `memory-bank/playbooks/node-typescript.md`
- `memory-bank/playbooks/python.md`
- `memory-bank/playbooks/java.md`
- `memory-bank/playbooks/c.md`
- `memory-bank/playbooks/playwright-browser.md`
- `memory-bank/playbooks/rapid-prototyping.md`

## Deferred Language Playbooks

Some language guides are intentionally not included to keep the harness light.

- C#/.NET is recognized by the router, but the full `c#-guide.md` source is a long learning guide. Add a small `csharp-dotnet.md` playbook only when working in a .NET repository.

## Browser Debug Policy

Browser debugging is a capability, not a language.

For UI debugging:

1. Prefer the IDE's built-in browser when available for fast interactive inspection.
2. Use Playwright MCP when the user asks for MCP, when repeatable automation is needed, or when E2E/test artifacts matter.
3. Use Playwright CLI/test runner when MCP is unavailable but browser automation is still required.
4. If no browser capability is available, say so and provide the minimum setup required.

Never claim browser inspection happened unless a browser tool, MCP server, or CLI actually ran.

## MCP Playwright Policy

When asked to use Playwright MCP:

1. Check that the MCP server is connected or configured for the current agent.
2. If connected, use MCP browser tools for navigation, snapshots, console/network inspection, screenshots, and interactions.
3. If disconnected, report the configuration issue and suggest the agent-specific config.
4. On Windows, prefer `npx.cmd` or `cmd /c npx` if plain `npx` fails.
5. Headed mode is preferred for local visual debug; headless mode is preferred for CI.
