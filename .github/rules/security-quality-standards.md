---
description: Security, privacy, quality, and review gates for in-scope PDLC changes.
---

# Security & Quality Standards

## Security
- Enforce authentication on protected routes, actions, and frontend integration calls.
- Enforce authorization using roles, entitlements, account ownership, relationship-manager assignment, and maker-checker rules where applicable.
- Enforce safe client-side input handling, output encoding, and platform-appropriate XSS/CSRF protections for Flutter and web deployments.
- Never log plaintext PII, account numbers, portfolio holdings, tokens, secrets, or credentials.
- Protect sensitive data in transit and in browser storage according to the approved platform standard.
- Use centralized secret management; no hardcoded secrets.
- Include correlation IDs in logs.
- Audit sensitive actions such as login, profile updates, risk-profile changes, suitability decisions, order submission, approval, cancellation, document access, and data export.

## Privacy And Compliance
Apply only when in scope:
- Thailand PDPA consent and privacy controls.
- KYC and AML checks.
- Suitability and risk profiling.
- Product eligibility restrictions.
- Advisory disclosure and consent capture.
- Data retention and deletion rules.
- Regulatory reporting and audit evidence.

## Quality
- Unit tests are mandatory for each frontend/backend surface requiring changes before implementation handoff. Use an 80% passing threshold independently for lines, statements, branches, and functions where supported; Flutter requires executable-line coverage. All layers, including validation, API endpoints, UI components, and utilities, use the same 80% gate; measured coverage may exceed it.
- Verify actual unit-test execution and native coverage reports. Show separate frontend/backend test counts, coverage metrics, commands, and evidence paths. Failed tests, below-threshold coverage, or missing execution/coverage evidence block implementation completion.
- Apply unit-test and coverage gates only to surfaces requiring changes in the story. If no backend changes are required or made, skip backend unit tests and coverage; apply the same rule to unchanged frontend. Report `NOT_APPLICABLE` with `N/A` metrics and approved scope evidence, without requiring suite output or coverage reports. Missing tasks or conflicting scope cannot justify skipping; separately required integration/API/functional checks still apply.
- Critical business rules require positive and negative tests.
- Integration clients require success, timeout, unavailable, malformed response, and retry/fallback tests.
- Security tests must cover unauthorized, unauthenticated, cross-customer, and privilege-escalation attempts.
- Performance tests must validate stated SLAs.

## Review Blockers
Critical blockers:
- Hardcoded secrets.
- Plaintext sensitive customer or financial data in logs.
- Missing authorization on protected operations.
- Missing input/output sanitization or unsafe rendering paths.
- Missing audit trail for regulated financial actions.
- Requirement or implementation with no traceability for production-impacting behavior.
