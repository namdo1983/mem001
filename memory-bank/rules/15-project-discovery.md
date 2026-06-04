# 15 - Project Discovery and Workspace Boundaries

Use when entering a new repository, finding multiple projects in one workspace, bootstrapping a project, or applying this harness to a new folder.

## Discovery Protocol

1. Identify whether the current directory is a single project, a monorepo, or a workspace containing multiple experimental projects.
2. Look for project markers: `README.md`, `package.json`, `pyproject.toml`, `pom.xml`, `build.gradle`, `go.mod`, `Cargo.toml`, app entrypoints, and test configs.
3. Locate existing guidance before creating new guidance: `00-HARNESS.md`, `memory-bank/`, `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `.clinerules/`, docs, plans, and workflow files.
4. Preserve the boundary between workspace-level guidance and project-specific guidance.
5. Document only durable discoveries in memory files.

## Boundary Rules

- Workspace-level rules describe how multiple projects are discovered, indexed, templated, archived, or compared.
- Project-level rules describe how one project is built, tested, deployed, and maintained.
- Shared templates may be referenced from projects, but copied templates must be customized and documented.
- Do not let experimental project assumptions leak into production projects.
- If rules conflict, prefer the file closest to the active project unless the installed harness entrypoint, such as `00-HARNESS.md` or `memory-bank/00-HARNESS.md`, defines a higher-priority rule.

## Bootstrap Checklist

When applying the harness to a new project:

- Ensure the installed harness entrypoint exists, usually `00-HARNESS.md` for a root harness or `memory-bank/00-HARNESS.md` for an installed folder.
- Ensure the relevant root adapter exists for the target agent.
- Populate core memory files with project facts, not generic filler.
- Run `70-capability-router.md` to select language/capability playbooks.
- Record setup decisions in `activeContext.md` and `changelog.md`.

## Template Activation

When using a reusable template:

1. Select the smallest template that fits the project.
2. Customize it to the actual stack and domain.
3. Test that the setup and commands work.
4. Document template use in the project README or memory bank.
5. Capture improvements back into the harness only if they are broadly reusable.

## Cross-Project Knowledge

Extract reusable patterns across projects, but keep them concise:

- Put durable patterns in `consolidated_learnings.md`.
- Put fresh observations in `raw_reflection_log.md`.
- Link related projects in workspace-level memory when a workspace index exists.
- Avoid copying large project-specific docs into global memory.

