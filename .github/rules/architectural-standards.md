# Architectural Standards

## Purpose
These standards define the required architecture for applications using this spec-driven PDLC workflow. They are mandatory unless the plan explicitly documents and approves an exception.

## Architectural Principles
- Build from approved requirements and specifications only.
- Preserve traceability from requirements to code and tests.
- Prefer simple, explicit boundaries over implicit coupling.
- Keep regulated workflows auditable, deterministic, and secure.

## Application Architecture
- Use feature-oriented folder structures and reusable UI components.
- Keep cross-cutting concerns in core services, not duplicated across features.
- Keep presentation logic focused on view composition and interaction; move business and integration logic to services or state management.
- Use explicit types and sound null safety; avoid hidden global dependencies and unchecked casts.

## Layering and Dependency Direction
- Widgets may depend on feature services, shared widgets, and Flutter/platform libraries.
- Feature services may depend on generated API clients, domain mappers, and utility services.
- Shared UI must not depend on feature-specific pages.
- Domain models and mapping utilities must not depend on presentation components.
- Avoid circular dependencies across pages, shared components, and services.

## Routing and Navigation Standards
- Use route-based feature boundaries and lazy loading where practical.
- Apply route guards/resolvers where required for authorization, entitlement checks, and critical prefetching.
- Use typed route params/query params and validate/normalize them before usage.
- Preserve deterministic navigation behavior for back/forward flows and deep links.

## Frontend Integration Contract Standards
- Use versioned integration paths/contracts, for example `/api/v1/...` when applicable.
- Send `Authorization` and `X-Correlation-ID` on protected integration calls.
- Include authenticated user identity and entitlements via approved auth context.
- Define timeout, retry, fallback, and error-handling behavior per integration.
- Do not call remote integrations directly from templates or ad-hoc utility code.

## Error and Response Handling Standards
Use stable domain-prefixed error codes:
- `AUTH-XXX`
- `CUST-XXX`
- `PORT-XXX`
- `ORDER-XXX`
- `PROD-XXX`
- `RISK-XXX`
- `KYC-XXX`
- `AML-XXX`
- `INT-XXX`
- `UI-XXX`


## State and Reactive Standards
- Use explicit Provider and Future/Stream patterns with predictable state transitions.
- Keep ephemeral UI state local; keep cross-screen state in scoped services/stores.
- Prevent leaks with lifecycle-safe teardown (`takeUntil`, `async` pipe, or equivalent).
- Handle loading, empty, success, and error states explicitly for all async flows.

## Forms and Validation Standards
- Use typed controllers, model validation, and explicit form state for regulated workflows and complex input flows.
- Apply validation rules from requirements/specs, including suitability and eligibility constraints.
- Keep validation messages safe, actionable, and non-revealing of sensitive internals.
- Capture consent and disclosure acceptance where required by compliance scope.

## UI and Theming Standards
- Use approved design tokens and shared theme styles from `frontend/lib/core/theme/app_theme.dart`.
- Avoid hard-coded brand colors/typography when tokenized equivalents exist.
- Maintain responsive behavior for desktop and mobile form factors.
- Enforce accessibility: semantic structure, keyboard support, focus management, and contrast compliance.

## Domain Areas
Common application domains:
- User profile and identity.
- User preferences and settings.
- Core feature workflows.
- Integration points with external systems.
- Portfolio and holdings.
- Watchlist.
- Advisory recommendations.
- Order capture and approval.
- Documents, statements, and disclosures.
- Notifications and alerts.
- Audit and reporting.

## Data and Privacy Modeling Standards
- Use clear entity relationships and cardinality.
- Classify sensitive fields as `[PII]`, `[SENSITIVE_FINANCIAL]`, `[CONFIDENTIAL]`, or `[PUBLIC]`.
- Define masking rules for UI, logs, exports, and telemetry.
- Define retention/audit requirements for sensitive financial actions.

## Banking and Compliance Controls
Include these only when in scope:
- PDPA consent and data privacy.
- KYC and AML screening.
- Customer risk profiling.
- Product suitability and eligibility.
- Maker-checker approval.
- Advisor approval and supervision.
- Audit trail and non-repudiation.
- Statement/reporting retention.
- Transaction limits and cooling-off controls.

## Quality and Review Gates
- Every feature change must map to `FR-*`/`NFR-*` and `SPEC-*` references.
- Critical user journeys require positive, negative, authorization, and failure-path test coverage.
- No merge with unresolved critical security/compliance findings.
- No merge for production-impacting behavior without traceability and test evidence.
