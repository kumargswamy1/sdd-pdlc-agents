# Architectural Standards

## Purpose
These standards define the required architecture for applications using this spec-driven PDLC workflow. They are mandatory unless the plan explicitly documents and approves an exception.

## Architecture Governance
- Assign a business owner and technical owner to each material capability, service, data product, and external contract.
- For material changes, record an architecture decision with context, decision, alternatives, consequences, security/data implications, operational impact, dependencies, and review/approval status. Link it to the relevant `FR-*`, `NFR-*`, `SPEC-*`, and `TASK-*` IDs.
- Maintain current system-context, integration, and data-flow views for production-impacting boundaries. Show trust zones, sensitive-data flows, external providers, systems of record, and failure boundaries.
- Assess proposed changes against the approved target architecture, lifecycle roadmap, and non-functional requirements. Record deviations, affected consumers, transition state, and an owner-approved exception rather than silently introducing a parallel pattern.
- Design material changes for observability, recovery, rollback or forward-fix, and safe operation during partial dependency failure.

## Architectural Principles
- Build from approved requirements and specifications only.
- Preserve traceability from requirements to code and tests.
- Prefer simple, explicit boundaries over implicit coupling.
- Keep regulated workflows auditable, deterministic, and secure.

## Application Architecture
- Apply technology-specific patterns only when the project context confirms that stack. The Flutter examples below do not govern React, web, native mobile, or backend-only projects; use the corresponding project standards instead.
- Use feature-oriented folder structures and reusable UI components.
- Keep cross-cutting concerns in core services, not duplicated across features.
- Keep presentation logic focused on view composition and interaction; move business and integration logic to services or state management.
- Use explicit types and sound null safety; avoid hidden global dependencies and unchecked casts.

## Layering and Dependency Direction
- Enforce equivalent dependency direction in the detected stack; apply the following widget/service rules only to Flutter projects.
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

## Backend API Naming and Contract Standards
- Name REST resources with business nouns, not actions, database tables, UI labels, team names, or vendor names. Use lowercase kebab-case path segments and plural collection names, for example `/api/v1/current-accounts/{currentAccountId}`.
- Use HTTP methods for resource operations: `GET` to retrieve, `POST` to initiate or submit a command, `PUT` to replace, and `PATCH` to partially update. Use `DELETE` only when deletion is a valid business lifecycle action; do not expose a generic delete for retained financial or audit records.
- Keep paths stable and shallow. Nest a resource only when its lifecycle or authorization is genuinely scoped by its parent; represent filters and selections as query parameters rather than encoded path verbs.
- Use lowerCamelCase for JSON properties and stable lowerCamelCase OpenAPI `operationId` values based on business intent, such as `retrieveCurrentAccount` or `initiatePaymentInstruction`. Use PascalCase for named OpenAPI schemas and define request/response models explicitly.
- Version public contracts deliberately, preserve backward compatibility within a major version, and document deprecation and migration plans. Do not version by implementation release or expose internal service topology in public paths.
- Define authorization scope, validation, error responses, pagination/filtering, correlation, timeout, retry, and idempotency behavior in the API contract. Require idempotency protection for retryable commands that can create duplicate financial effects.
- Maintain an OpenAPI contract for synchronous HTTP APIs. Validate schemas, examples, authentication requirements, and backward compatibility in CI; treat intentional breaking changes as a versioning decision, not an undocumented implementation detail.
- Define one machine-readable error envelope with a stable domain error code, safe client message, correlation identifier, and field-level validation details where appropriate. Map errors consistently to HTTP status codes and never expose stack traces, internal topology, or sensitive customer data.
- Define pagination, filtering, and sorting parameters consistently. Use deterministic ordering with a stable tie-breaker, and prefer cursor pagination for large or changing datasets.
- Define concurrency behavior for updates that can race, using version fields, ETags/`If-Match`, or an equivalent precondition. Return a clear conflict response instead of silently overwriting a newer state.
- Represent monetary values without binary floating-point ambiguity. Specify currency, scale, rounding mode, and any minor-unit conversion; define date/time formats, business-date semantics, and time-zone handling in the contract.
- For long-running operations, return an operation resource or another documented asynchronous contract with explicit accepted, pending, completed, failed, and cancellation behavior. Do not report a financial command as complete before its defined business outcome is confirmed.
- Apply `.github/rules/security-quality-standards.md` as the canonical OWASP control-selection source. For APIs, use relevant API Security Top 10 risks to inform design and map applicable risks to approved ASVS requirements and verification; do not treat the Top 10 as a conformance claim.

## Banking Architecture and BIAN Alignment
Apply these controls when banking capabilities, products, or integrations are in scope.

`.github/rules/requirement-standards.md` owns BIAN business vocabulary and capability mappings. This section owns the technical mapping to architecture boundaries, service contracts, and APIs.

- Record the adopted BIAN Service Landscape release and map applicable capabilities to its Business Area, Business Domain, and Service Domain vocabulary.
- Treat a BIAN Service Domain as a logical business-service boundary, not an instruction to create one microservice, database, team, or deployment per Service Domain. Document the mapping to internal bounded contexts and deployment units explicitly.
- Where a BIAN Service Domain API or business object model is adopted, preserve its documented control-record, behavior-qualifier, service-operation, and lifecycle semantics where applicable. Map external BIAN identifiers to internal identifiers explicitly; do not flatten distinctions that change business meaning.
- Document the applicable BIAN functional pattern, such as Initiate, Retrieve, Update, Control, Exchange, or Execute, for each relevant service operation. Map it to the API's HTTP method and resource contract; do not mechanically place action words in REST resource paths.
- Keep BIAN reference identifiers, release, API specification version, and any local extensions or deviations traceable in the API contract and architecture decision records.
- Use an explicit adapter or anti-corruption boundary when translating between BIAN business objects/contracts and internal domain models. Preserve lifecycle and qualifier semantics while preventing external schema changes from silently reshaping internal models.
- Assign ownership for each mapped capability, its authoritative data, and its contract. Document cross-Service-Domain orchestration, state ownership, and failure/recovery behavior rather than assuming BIAN boundaries determine deployment or transaction boundaries.
- Validate mappings and API contracts against the selected BIAN source and business-owner terminology. Matching a BIAN name alone does not establish conformance; record extensions, exclusions, and unmapped capabilities.

## FSDM Data Architecture
Apply when the organization has adopted a Financial Services Data Model (FSDM) for an in-scope data domain. Use the actual organization-approved model and version; do not assume one universal or vendor-specific FSDM.

- Treat the FSDM as a governed business/logical data reference unless its owner explicitly designates a physical implementation. Do not derive database, service, or deployment boundaries mechanically from FSDM entities.
- Maintain explicit mappings between FSDM concepts, internal domain models, physical persistence schemas, API contracts, and ISO 20022 message elements where applicable. Keep transformations in owned adapters/mappers and preserve semantics, identity, cardinality, and lifecycle.
- Assign a data owner and system of record for each authoritative entity. Document write authority, read consumers, lineage, quality controls, retention, and change ownership.
- Keep canonical business definitions separate from source-specific fields and implementation details. Use extensions with stable identifiers and documented rationale; do not silently repurpose canonical attributes.
- Validate mappings and migrations with representative positive, negative, nullability, cardinality, referential-integrity, and backward-compatibility tests as applicable.

## ISO 20022 Message Architecture
Apply these controls only when an in-scope integration uses ISO 20022 messages.

`.github/rules/requirement-standards.md` owns business message requirements, scheme/profile selection, and requirement-to-element meaning. This section owns technical schemas, adapters, serialization, and runtime validation; `.github/rules/versioning-standards.md` owns compatibility and retirement policy.

- Select the message definition and version together with the applicable market infrastructure or scheme implementation guideline. Treat schema, code-set, and market-practice versions as contract dependencies and pin the approved source artifacts.
- Preserve message identifiers, element semantics, cardinality, code sets, party roles, references, and lifecycle meaning across adapters. Map explicitly between ISO 20022 messages and internal models; do not silently drop, reinterpret, or synthesize fields.
- Validate XML messages against the selected schema and applicable scheme profile, then apply business validation. A JSON API representation is not an ISO 20022 XML message by default; document and test any mapping between JSON fields and ISO 20022 semantics.
- Model acknowledgements, status updates, rejection, cancellation, return, settlement, and reconciliation as distinct outcomes where the selected scheme defines them. Preserve end-to-end and instruction references and define duplicate, retry, replay, and idempotency behavior.
- Do not hard-code a message family, version, or optional element as universal. Record the selected scheme's requirements, supported subset, extensions, and compatibility policy.

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
- Identify data owner, system of record, permitted purpose, provenance/lineage, retention trigger, quality controls, and downstream consumers for material data entities.
- Separate conceptual, logical, and physical models. Document mappings between canonical business concepts, FSDM, BIAN capabilities, API/event contracts, and persistence schemas where those standards apply.
- Prohibit uncontrolled replication of sensitive data. Define approved caching, export, backup, archive, deletion, and test-data handling for each sensitive-data flow.

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
- Material architecture changes require an approved decision record, impact assessment, owner, and exception disposition before implementation is considered complete.
- Production-bound changes require operational ownership, monitoring/alerting, support documentation, dependency failure behavior, and recovery/rollback evidence appropriate to risk.
