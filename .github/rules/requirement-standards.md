---
description: Defines canonical requirement structure and quality criteria for spec-driven workflows.
---

# Requirement Standards

## Purpose
Every `/specify` input must be a canonical requirement file. Existing BRDs, UI specs, design files, integration guides, and discovery notes are source material that must be consolidated before specification.

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

### 6. Data Requirements
List entities, fields, classification, source, retention, and masking/encryption needs.

Allowed classifications:
- `[PII]`
- `[SENSITIVE_FINANCIAL]`
- `[CONFIDENTIAL]`
- `[PUBLIC]`

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
- Trace metadata is present.
- Functional requirements use `FR-*`.
- Non-functional requirements use `NFR-*`.
- Business rules use `BR-*`.
- Acceptance criteria use Gherkin and map to requirements.
- PII and sensitive financial data are classified.
- Integration points include timeouts and fallback behavior.
- Performance SLAs are numeric.
- Compliance assumptions are explicit.
- No real customer PII, account numbers, portfolio holdings, secrets, tokens, or production data.
