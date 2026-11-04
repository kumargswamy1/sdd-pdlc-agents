---
description: Cross-language baseline for readable, maintainable, secure, and verifiable application code.
---

# Coding Standards

## Purpose and Scope
Use this baseline when agents create, change, plan, or review application source code and executable test code. Apply only the practices relevant to the changed technology and scope.

Project-specific language, framework, formatter, linter, and build instructions remain authoritative for syntax and idioms. Follow them alongside these cross-language requirements. Do not impose one language's patterns on another stack or reformat unrelated code.

## Implementation Standards
- Follow approved requirements, specifications, plans, architecture decisions, and established repository patterns. Do not introduce behavior, dependencies, abstractions, or public contracts without traceable need.
- Keep changes cohesive and minimal. Use clear names, explicit contracts, appropriate types, and simple control flow. Avoid duplicate logic, hidden global state, dead code, unexplained magic values, and speculative generalization.
- Separate presentation, domain/business behavior, integration, and persistence responsibilities according to the project's architecture. Keep external-system and data-access boundaries explicit.
- Validate untrusted input at trust boundaries and enforce authorization at the server or authoritative service. Do not rely on client-side controls for security decisions.
- Handle errors deliberately: preserve actionable diagnostic context for operators, return stable and safe errors to callers, and do not swallow failures or expose internals.
- Use structured logging and correlation identifiers where supported. Never log secrets, credentials, tokens, or unmasked customer/financial data.
- Manage dependencies through the approved package manager and lockfiles. Prefer maintained, supported dependencies; assess security, license, provenance, and upgrade impact before adding or changing dependencies.
- Keep configuration external to code, validate it at startup or use, and never embed environment-specific secrets or production data in source, tests, fixtures, or examples.
- Add comments and documentation for non-obvious intent, invariants, security decisions, or operational constraints. Keep documentation aligned with the implemented behavior.
- Preserve compatibility for consumers. Document API, event, schema, and persistence changes and follow `.github/rules/versioning-standards.md`.

## Test Code Standards
- Map tests to requirements, specifications, tasks, and observable behavior. Keep tests focused and deterministic; isolate only the boundaries that the test is intended to isolate.
- Use synthetic or approved-masked data. Do not call production systems or trigger real payments, trades, or customer-impacting actions from tests.
- Assert meaningful outcomes and failure behavior. Avoid tests that only mirror implementation details or pass without exercising the intended behavior.
- Preserve existing test conventions and use the test framework and coverage evidence defined by project context and `.github/rules/implementation-execution-gates.md`.

## Review and Exceptions
- Run the repository's applicable formatter, linter, type checker, security checks, and tests for the changed scope. Report commands, outcomes, and any checks that could not run.
- Review diffs for unintended files, generated artifacts, secrets, customer data, and unrelated changes before handoff.
- A deviation from this baseline or project-specific coding policy requires a documented rationale, scope, risk, compensating controls, accountable approver, and review/expiry date under `.github/rules/pdlc.md`. Agents must not approve their own exceptions.
