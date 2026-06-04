# Node and TypeScript Playbook

Load for Node, JavaScript, TypeScript, React, Vite, or package-based frontend/backend work.

## Detection

Relevant signals include `package.json`, `tsconfig.json`, `vite.config.*`, `*.ts`, `*.tsx`, `*.js`, `*.jsx`, ESLint config, React components, and npm/pnpm/yarn lockfiles.

## Commands

Prefer project scripts:

- Install: `npm install` or the package manager already used by the repo.
- Lint: `npm run lint`
- Build/typecheck: `npm run build`, or `tsc --noEmit` when configured.
- Tests: `npm test`, `npm run test`, `npm run test:e2e`, or the repo-specific script.

Use the scripts already defined by the target repository. Do not assume this harness source repository has Node scripts.

## TypeScript Standards

- Preserve strict types where they exist.
- Avoid `any` unless crossing an untyped boundary; isolate and explain it.
- Prefer narrow types, discriminated unions, and explicit return types for shared helpers.
- Validate external data before trusting its shape.

## TypeScript Architecture and OOP

- Prefer plain functions, modules, and discriminated unions for simple data transformations and variant handling.
- Use interfaces or type aliases to describe public contracts; keep exported types owned by the module that owns the data shape.
- Use classes when they protect state, invariants, lifecycles, or framework idioms; avoid class wrappers around stateless helpers.
- Prefer composition through injected clients, providers, hooks, or small services over inheritance.
- Use Strategy, Adapter, or Factory patterns when provider/runtime behavior varies and conditionals are spreading.
- Keep API clients, validation, stateful hooks, and rendering components in separate owners when the repo already follows those boundaries.

## React/Frontend Standards

- Keep hooks focused on stateful behavior and side effects.
- Keep components focused on rendering and local interaction.
- Avoid large components that mix fetching, transformation, rendering, and mutation.
- Prefer accessible controls and stable layout dimensions.
- Verify user-facing UI with browser evidence when changing layout or behavior.

## Provider and API Notes

- Prefer existing provider patterns for data, auth, API clients, and realtime access.
- Do not add auth or API-key headers to endpoints that the target framework explicitly excludes.
- Keep backend resource names and field mappings centralized when practical.

