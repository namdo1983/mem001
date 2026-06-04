# Python Playbook

Load for Python projects, scripts, services, data pipelines, tests, or automation.

## Detection

Relevant signals include `pyproject.toml`, `requirements.txt`, `uv.lock`, `poetry.lock`, `setup.py`, `tox.ini`, `pytest.ini`, `*.py`, FastAPI, Django, Flask, pytest, ruff, or mypy config.

## UV-First Workflow

When a Python project has `uv.lock`, `[tool.uv]`, or clear `uv` usage, treat `uv` as the package and environment authority.

Use these defaults:

- Sync environment: `uv sync`
- Run commands: `uv run <command>`
- Add runtime dependency: `uv add <package>`
- Add dev dependency: `uv add --dev <package>`
- Remove dependency: `uv remove <package>`
- Update lockfile: `uv lock`
- Upgrade one dependency: `uv lock --upgrade-package <package>`
- Create venv: `uv venv`
- Install/manage Python: `uv python install`, `uv python list`, `uv python find`, `uv python pin`

Do not bypass `uv` with raw `pip install` in uv-managed projects unless the repo explicitly documents that workflow.

## Commands

Prefer repo-defined tooling:

- With uv: `uv sync`, `uv run pytest`, `uv run ruff check .`, `uv run mypy .`
- With Poetry: `poetry install`, `poetry run pytest`
- With pip/venv: activate the repo venv, then use project scripts.

Do not install new packages without checking existing dependency management.

## Project and Environment Management

- Prefer `pyproject.toml` as the source of dependency and tool configuration.
- Keep `uv.lock` committed for reproducible installs when the project uses uv.
- Use `.python-version` or `uv python pin` when the project requires a specific Python version.
- Use `.venv/` as the local virtual environment location and keep it out of git.
- For monorepos, check for uv workspace configuration before adding dependencies to a subproject.

## UV Package Management

- Use `uv add` and `uv remove` for project dependencies so `pyproject.toml` and `uv.lock` stay aligned.
- Use `uv pip ...` only for pip-compatible workflows, legacy `requirements.txt`, editable installs, or when the repo lacks uv project metadata.
- Use extras and dependency groups when the project already models dev/test/docs dependencies that way.
- For private indexes, keep credentials in environment variables or secure config. Do not hardcode secrets in `pyproject.toml`.

## Python Standards

- Use type hints for public functions and shared boundaries.
- Prefer dataclasses, Pydantic models, or typed dictionaries for structured data.
- Keep I/O at the edges; keep core logic pure where practical.
- Use context managers for files, network clients, locks, and temporary resources.
- Avoid broad `except Exception` unless logging/re-raising or converting at a boundary.

## Python OOP and Design

- Prefer simple functions and modules until state, invariants, or multiple collaborators justify a class.
- Use `Protocol` for structural interfaces and `ABC` only when a subclass contract must be enforced.
- Prefer composition and dependency injection through constructors, function parameters, or pytest fixtures.
- Use dataclasses or Pydantic models for value objects; avoid mutable default arguments.
- Keep side-effecting clients, gateways, and adapters behind narrow interfaces so tests can replace them.
- Avoid broad base classes, mixin stacks, and generic utility classes that hide unrelated responsibilities.

## Testing

- Use pytest conventions when present.
- Prefer fixtures for setup and dependency injection.
- Mock external services at boundaries, not the unit under test.
- Cover error paths and edge cases, especially serialization and async behavior.
- In uv projects, run tests and quality tools through `uv run`, for example `uv run pytest`, `uv run pytest --cov=<package>`, `uv run ruff check .`, and `uv run mypy .`.

## Architecture

- For services: separate routes/controllers, domain logic, persistence gateways, and external clients.
- For scripts: keep argument parsing, I/O, and core transformation in separate functions.
- For async: avoid blocking calls inside event loops; use explicit timeouts.

## UV Troubleshooting

- Installation failure: retry with verbosity, for example `uv pip install --verbose <package>`.
- Dependency conflict: inspect with `uv pip check` and `uv pip tree`.
- Broken venv: recreate intentionally with `uv venv` and `uv sync` after confirming no local state must be preserved.
- Cache issue: inspect or clean with `uv cache info`, `uv cache clean`, and `uv cache prune`.
- Network or offline constraints: check `UV_HTTP_TIMEOUT`, `UV_OFFLINE`, and index configuration.

## Source

This uv guidance is adapted from `cline/prompts` `.clinerules/uv-python-usage-guide.md`.
