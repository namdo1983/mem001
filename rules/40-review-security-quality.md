# 40 - Review, Security, and Quality

## Code Review Stance

When reviewing, lead with findings ordered by severity:

- Critical: bugs, security issues, data loss, broken workflows.
- Important: logic gaps, error handling, performance, maintainability risks.
- Suggestions: readability, naming, simplification.

Every finding should include location, impact, and a concrete fix direction.

## Security Checks

Consider:

- Secrets or credentials in code or logs.
- Unsafe command execution.
- Missing auth or authorization checks.
- Input validation gaps.
- XSS or injection paths.
- Sensitive data exposure in UI, network, storage, or logs.

## Quality Checks

Prefer:

- Clear module boundaries.
- Small functions with focused responsibility.
- Explicit error handling.
- Minimal duplication.
- Consistent project naming and style.
- Comments only where they explain non-obvious intent.

