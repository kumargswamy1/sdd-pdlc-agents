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
- `Requirement Intake Consolidator`: Consolidate existing source documents and create
  canonical IDs for the BRD and detailed requirements, including `BRD-*`, `FR-*`,
  `NFR-*`, `AC-*`, `BR-*`, `INT-*`, and `ERR-*`.
- `Context Builder`: Create `CTX-*` from verified project context and map them to
  related `BRD-*` entries when a BRD exists.
- `User Story Generator`: Create `US-*`.
- `Technical Specifier`: Create `SPEC-*`.
- `Implementation Planner`: Create `TASK-*`.
- `Implementation Builder`: Create `CODE-*` and unit-test `TEST-*` references with applicability and measured coverage evidence.
- `API Tester`: Create API-level `APT-*` execution records mapped to API IDs, controllers, and related `TASK-*`/`SPEC-*`/`CODE-*` IDs.
- `Functional Automation Test`: Create component-level `FT-*` execution records mapped to component IDs and related `TASK-*`/`SPEC-*` IDs.
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
- APIs in `spec.md` when `API In Scope: YES` without an `APT-*` result or explicit blocker.
- UI behavior in `spec.md` when `UI In Scope: YES` without an `FT-*` result or explicit blocker.
- Entries in optional `backend-apis.json` or `components.md` that are not reconciled with the specification.
- Requirements without tests.
- Compliance requirements without review evidence.
- Applicable OWASP ASVS/MASVS requirements without source-versioned control IDs and traceable implementation, verification, and review evidence.
- In-scope FSDM concepts without model/version identifiers and traceable requirement, mapping, implementation, migration, and verification evidence.
- ISO 20022 requirements without traceable message-definition/profile versions and mapped specification, implementation, and test evidence.
- Missing GitHub metadata when the repo is linked to GitHub.

## Control and Decision Traceability
- Trace material NFRs, architecture decisions, threat/control IDs, approved exceptions, data classifications, migration decisions, and operational readiness evidence alongside functional requirements.
- Each control or exception record must include source/version, accountable owner, applicability, verification evidence, status, and approval/expiry where relevant.
- Preserve lineage across renamed or superseded IDs. Do not silently delete, reuse, or relabel IDs; mark superseded artifacts and maintain forward/backward references.
- Reconcile the matrix at stage boundaries and release readiness. Report orphaned controls, missing owners, stale approvals, and evidence that no longer matches the deployed version as explicit gaps.

For ISO 20022 integrations, record the authoritative message definition, schema, and scheme/market-practice guideline versions in the requirement or specification artifacts. Trace each in-scope message mapping and validation rule through `FR-*`/`NFR-*`, `SPEC-*`, `TASK-*`, `CODE-*`, and the applicable API/integration test evidence.

## Data Protection
Never include real customer PII, account numbers, card numbers, portfolio holdings, credentials, secrets, tokens, or production data in generated artifacts.
