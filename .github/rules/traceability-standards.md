---
description: Defines end-to-end traceability for GitHub Copilot spec-driven PDLC artifacts.
---

# Traceability Standards

## Required Chain

```text
CTX-001 -> BRD-001 -> FR-001/NFR-001 -> SPEC-001 -> TASK-001 -> CODE-001 -> APT-001 -> FT-001 -> TEST-001 -> REVIEW-001 -> DOC-001
                                -> US-001
```

## Traceability Matrix
Create and maintain:

```text
requirement/Traceability_Matrix.md
```

Required columns:

| CTX ID | BRD ID | FR/NFR ID | US ID | SPEC ID | TASK ID | Code Ref | APT ID | FT ID | TEST ID | REVIEW ID | DOC ID | GitHub Issue | PR | Commit | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Agent Responsibilities
- `Requirement Intake Consolidator`: Create canonical IDs from existing source docs.
- `Context Clarifier`: Create `CTX-*`.
- `BRD Generator`: Create `BRD-*`.
- `Requirements Expander`: Create `FR-*`, `NFR-*`, `AC-*`, `BR-*`, `INT-*`, and `ERR-*`.
- `User Story Generator`: Create `US-*`.
- `Technical Specifier`: Create `SPEC-*`.
- `Implementation Planner`: Create `TASK-*`.
- `Implementation Builder`: Create `CODE-*` references.
- `API Tester`: Create API-level `APT-*` execution records mapped to API IDs, controllers, and related `TASK-*`/`SPEC-*`/`CODE-*` IDs.
- `Functional Automation Test`: Create component-level `FT-*` execution records mapped to component IDs and related `TASK-*`/`SPEC-*` IDs.
- `Quality Tester`: Create `TEST-*`.
- `Compliance Reviewer`: Create `REVIEW-*`.
- `Technical Documenter`: Create `DOC-*`.
- `Traceability Manager`: Reconcile all IDs and flag gaps.

## GitHub Metadata
When available, every artifact should include:
- GitHub issue.
- Branch.
- Commit.
- Pull request.
- Run ID.
- Source artifact.
- Status.

## Gap Checks
Flag:
- Orphaned IDs.
- Requirements without specs.
- Specs without tasks.
- Tasks without code.
- APIs listed in `output/{RUN_ID}/plan/contracts/backend-apis.json` without an `APT-*` result or explicit blocker.
- Components listed in `output/{RUN_ID}/plan/frontend/components.md` without an `FT-*` result or explicit blocker.
- Requirements without tests.
- Compliance requirements without review evidence.
- Missing GitHub metadata when the repo is linked to GitHub.

## Data Protection
Never include real customer PII, account numbers, card numbers, portfolio holdings, credentials, secrets, tokens, or production data in generated artifacts.
