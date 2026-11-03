---
description: Defines canonical requirement structure and quality criteria for spec-driven workflows.
---

# Requirement Standards

## Purpose
Every `/specify` input must be a canonical requirement file. Existing BRDs, UI specs, design files, integration guides, and discovery notes are source material that must be consolidated before specification.

## Requirement Governance
- Each requirement must identify its source, accountable business owner, status, priority, and approval state. Preserve source IDs and record mappings when IDs are normalized.
- Separate business outcome, policy, and constraint from solution design. Mark user-provided facts, observed implementation, regulatory obligations, assumptions, recommendations, and unresolved questions distinctly.
- Classify requirements by capability, data sensitivity, risk/criticality, jurisdiction, and affected channels or integrations when applicable. Do not infer regulatory scope or business behavior from a technology choice.
- Define measurable acceptance evidence and exception ownership for regulated or financially material behavior. An unresolved requirement affecting funds movement, authorization, customer eligibility, financial reporting, or sensitive data blocks specification readiness.
- Record dependencies, effective dates, precedence, and conflict resolution for requirements that span products, jurisdictions, legal entities, channels, or external providers.

## Canonical Template
Use:

```text
.github/templates/requirements-input-template.md
```

Preferred final input:

```text
requirement/{ProjectName}_Requirements.md
```

## Required Sections

### 0. Trace Metadata
Must include GitHub issue, run ID, branch, source commit, upstream artifact, upstream IDs, generated IDs, and status.

### 1. Project Overview
- Summary.
- Business context.
- Relationship to existing system.

### 2. Actors & Personas
Examples:
- End User / Customer
- Administrator
- Support Agent
- Manager / Supervisor
- System Integrator
- System Admin

### 3. User Stories
Format:

```text
AS A <actor>
I WANT TO <action>
SO THAT <outcome>
```

Each story must include preconditions, main flow, alternate flows, and postconditions.

### 4. Functional Requirements
Use `FR-001`, `FR-002`, ...

Each requirement must be specific, measurable, testable, and mapped to acceptance criteria.

### 5. Non-Functional Requirements
Use `NFR-001`, `NFR-002`, ...

Cover performance, security, privacy, compliance, availability, scalability, auditability, observability, and resilience.
For application-security requirements, identify applicable OWASP ASVS controls by version-qualified ID, state measurable acceptance criteria, and record the security/data scope. Do not copy OWASP Top 10 categories into requirements without a project-specific risk or approved requirement.
Specify the measurement, target, workload, environment, observation period, owner, and verification method for each material NFR. For production services, cover SLOs/error budgets, capacity, recovery time/recovery point, data durability, support hours, and degraded-mode behavior where relevant.

### 6. Data Requirements
List entities, fields, classification, source, retention, and masking/encryption needs.

When the organization has adopted a Financial Services Data Model (FSDM), apply the FSDM mapping requirements below. FSDM is not a single universal model; record the organization's actual model, owner, edition, and source rather than assuming a vendor or release.

Allowed classifications:
- `[PII]`
- `[SENSITIVE_FINANCIAL]`
- `[CONFIDENTIAL]`
- `[PUBLIC]`

### FSDM Data Model Alignment
Apply when an adopted FSDM is in scope for the product, data domain, or integration.

- Record the FSDM authority/owner, product or model name, edition/version, scope, and approved source. Identify whether the reference is conceptual, logical, or physical.
- Map in-scope business entities and attributes to FSDM concepts using stable model identifiers and names where available. Record mapping status (`ALIGNED`, `EXTENDED`, `UNMAPPED`, or `NOT_APPLICABLE`), rationale, and owner approval for extensions.
- Specify business definitions, identifiers, relationships/cardinality, lifecycle, effective dates, source-of-truth ownership, and applicable data-quality rules. Do not infer semantics from a matching field name.
- Identify data provenance and lineage from source systems through transformations to consuming services, reports, and regulatory outputs where relevant.
- Distinguish FSDM business concepts from BIAN capability/service-domain names, physical database tables, API schemas, and ISO 20022 message elements. Keep mappings between them explicit and traceable.
- Do not claim FSDM conformance from partial name matching. Record gaps, local extensions, and unresolved ownership or semantic decisions for data/domain-owner review.

### 7. Integration Points
For each system, define direction, protocol, timeout, retry, fallback, error handling, and owner.

Example systems:
- Core banking
- Customer information file
- KYC/AML screening
- Risk profiling
- Product master
- Portfolio management
- Order management
- Market data
- Document/statement service
- Notification service
- Payment or settlement systems

### 8. Business Rules
Use `BR-001`, `BR-002`, ...

Rules must use MUST/SHALL language and avoid ambiguity.

### Banking Business Domains and BIAN
Apply these requirements when banking capabilities, products, or integrations are in scope.

This section owns business terminology and capability mappings. Technical BIAN boundaries and API interpretation belong in `.github/rules/architectural-standards.md`.

- Record the BIAN Service Landscape release and source used for domain mapping. BIAN names and boundaries can change between releases.
- Use the BIAN hierarchy precisely: Business Area, Business Domain, and Service Domain. Do not use these terms interchangeably with an enterprise business unit, a Domain-Driven Design bounded context, a team, a microservice, or an API resource.
- For each in-scope banking capability, record its approved business name, corresponding BIAN Business Area/Business Domain/Service Domain when mapped, BIAN release, mapping status (`ALIGNED`, `EXTENDED`, `UNMAPPED`, or `NOT_APPLICABLE`), and rationale/source.
- Preserve the organization's approved business language. Record synonyms, legacy labels, and BIAN terms in a glossary; do not silently rename requirements or expose internal implementation names as business terminology.
- Define banking concepts such as party/customer, account/arrangement, product, transaction, position, and instruction in context. Identify the owning capability and distinguish concepts that have different lifecycle, ownership, or regulatory meaning.
- Map requirements to business capabilities and BIAN Service Domains where applicable. Capture actors, triggers, preconditions, outcomes, business objects, state changes, and provider/consumer responsibilities without assuming a one-to-one mapping between a requirement and a Service Domain.
- Do not invent a BIAN mapping or claim BIAN conformance from matching names alone. Record gaps, extensions, and unresolved mappings as explicit decisions for domain-owner review.

### ISO 20022 Payment and Financial Messages
Apply these requirements only when an in-scope payment, cash-management, securities, or other integration uses ISO 20022 messages.

This section owns business message use, scheme/profile selection, and requirement-to-message meaning. Technical schemas, adapters, and runtime validation belong in `.github/rules/architectural-standards.md`; version compatibility belongs in `.github/rules/versioning-standards.md`.

- Record the jurisdiction, market infrastructure or scheme, message family and identifier, message-definition version, applicable market-practice or implementation guideline, and authoritative source/version. Distinguish the base ISO 20022 definition from scheme-specific usage rules.
- Identify message direction, participants, business purpose, triggering event, lifecycle stages, acknowledgements/statuses, rejection reasons, cancellations/returns, settlement, and reconciliation outcomes that are in scope. Do not infer that every scheme supports the same flow.
- Map each requirement to the relevant message elements and business meaning, including mandatory/optional usage, cardinality, code sets, identifiers, and any approved extensions. Record unresolved mappings rather than inventing message content.
- Specify related identifiers and code standards only when applicable to the selected scheme, such as ISO 4217 currency codes, ISO 8601 date/time formats, ISO 9362 BICs, ISO 13616 IBANs, or ISO 17442 LEIs. Capture local validation and eligibility rules separately from the identifier's syntax.
- Keep payment-specific cutoffs, business dates, value dates, currencies, amount precision/rounding, duplicate handling, and business acceptance/rejection rules explicit and testable.
- Do not claim ISO 20022 or scheme conformance from a matching message name alone. Record the exact profile, validation evidence, deviations, and business-owner approval.

### 9. Acceptance Criteria
Use `AC-001`, `AC-002`, ...

Use Gherkin:

```gherkin
GIVEN <precondition>
WHEN <action>
THEN <expected result>
AND <additional assertion>
```

### 10. Error Handling
Use `ERR-001`, `ERR-002`, ...

Define scenario, trigger, system behavior, user message, and status code.

### 11. Out of Scope
Explicit exclusions.

### 12. Open Questions
Owner, needed-by date or phase, and impact if unanswered.

### 13. Traceability Summary
Map `CTX -> BRD -> FR/NFR -> US -> AC/BR/INT/ERR`.

## Quality Gates
- Business owner, sources, approval state, scope, and trace metadata are recorded.
- Trace metadata is present.
- Functional requirements use `FR-*`.
- Non-functional requirements use `NFR-*`.
- Business rules use `BR-*`.
- Acceptance criteria use Gherkin and map to requirements.
- PII and sensitive financial data are classified.
- Integration points include timeouts and fallback behavior.
- Performance SLAs are numeric.
- Compliance assumptions are explicit.
- Material decisions, exceptions, dependencies, and unresolved risks have owners and dispositions.
- No real customer PII, account numbers, portfolio holdings, secrets, tokens, or production data.
