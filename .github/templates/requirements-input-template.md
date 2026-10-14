# {Project Name} Requirements

## 0. Trace Metadata

| Field | Value |
|-------|-------|
| GitHub Issue | N/A |
| Run ID | pre-specify |
| Branch | N/A |
| Source Commit | pending |
| Upstream Artifact | requirement/BRD_{Project}.md |
| Upstream IDs | BRD-001 |
| Generated IDs | FR-001, NFR-001, US-001, AC-001, BR-001, INT-001, ERR-001 |
| Status | Draft |

## 1. Project Overview

### Summary
Describe the feature, journey, or product change.

### Business Context
Explain the problem, user impact, operational impact, and business value.

### Relationship to Existing System
State whether this is a new feature, enhancement, integration, migration, or replacement.

## 2. Actors & Personas

| Actor | Role | Access Level | Key Goals |
|-------|------|--------------|-----------|
| End User | Primary user | USER | Accomplish key tasks |
| Administrator | System admin | ADMIN | Manage system operations |
| Support Agent | Support staff | SUPPORT | Assist users |

## 3. User Stories

### US-001: {Story Title}

AS A {actor}  
I WANT TO {action}  
SO THAT {business outcome}

**Derived From**: BRD-001

**Preconditions**:
- {Precondition}

**Main Flow**:
1. {Step}
2. {Step}

**Alternate Flows**:
- {Alternate or exception}

**Postconditions**:
- {Postcondition}

## 4. Functional Requirements

| ID | Requirement | Derived From | Priority | Acceptance Criteria |
|----|-------------|--------------|----------|---------------------|
| FR-001 | The system must {specific behavior}. | BRD-001 | Must Have | AC-001 |

## 5. Non-Functional Requirements

| ID | Category | Requirement | Target | Derived From |
|----|----------|-------------|--------|--------------|
| NFR-001 | Performance | {Flow/Frontend Integration} must complete within {target}. | P95 < {ms} | BRD-001 |
| NFR-002 | Security | {Security requirement}. | {Target} | BRD-001 |
| NFR-003 | Compliance | {PDPA/KYC/AML/Suitability/Audit/N/A}. | {Target} | BRD-001 |

## 6. Data Requirements

| Entity | Field | Type | Classification | Source | Retention | Notes |
|--------|-------|------|----------------|--------|-----------|-------|
| Customer | customer_id | string | [CONFIDENTIAL] | CIF | {Duration} | Internal identifier |
| Account | account_number | string | [SENSITIVE_FINANCIAL] | Core banking | {Duration} | Mask in logs and UI where needed |

## 7. Integration Points

| ID | System | Type | Direction | Protocol | Timeout | Fallback | Derived From |
|----|--------|------|-----------|----------|---------|----------|--------------|
| INT-001 | {System} | HTTP/Event/File/etc. | Outbound | HTTPS/JSON | {ms} | {Fallback} | FR-001 |

## 8. Business Rules

| ID | Rule | Derived From | Applies To |
|----|------|--------------|------------|
| BR-001 | The system MUST {business rule}. | BRD-001 | FR-001 |

## 9. Acceptance Criteria

### AC-001: {Criterion Title}

**Covers**: FR-001, US-001

```gherkin
GIVEN {precondition}
WHEN {action}
THEN {expected outcome}
AND {additional assertion}
```

## 10. Error Handling

| Error ID | Scenario | Trigger | System Behavior | User Message | HTTP Status |
|----------|----------|---------|-----------------|--------------|-------------|
| ERR-001 | {Scenario} | {Trigger} | {Behavior} | {Safe message} | {Status} |

## 11. Out of Scope

- {Explicit exclusion}

## 12. Open Questions

| ID | Question | Owner | Needed By | Impact If Unanswered |
|----|----------|-------|-----------|----------------------|
| Q-001 | {Question} | {Owner} | {Phase} | {Impact} |

## 13. Traceability Summary

| BRD ID | FR/NFR ID | US ID | AC ID | BR ID | Integration ID | Error ID | Status |
|--------|-----------|-------|-------|-------|----------------|----------|--------|
| BRD-001 | FR-001 | US-001 | AC-001 | BR-001 | INT-001 | ERR-001 | Draft |
