# Spec-Driven Workflow

Every PDLC stage is human-initiated. At the specification, planning, and post-test code gates, the responsible stage agent automatically invokes Compliance Reviewer before completing. The review does not start the next stage; a human reviews the result and manually starts the next stage. Critical, High, and Medium findings block the handoff until remediated and re-reviewed or explicitly accepted.

> [!WARNING]
> A `FAIL` with only Low-severity findings retains its status and emits `REVIEW_GATE_WARNING`, but does not automatically stop the review handoff. Findings remain visible and may carry downstream. Mixed severities follow the highest-severity outcome; independent stage hard gates remain blocking.

Both frontend and backend must be assessed against story scope. Only changed surfaces require implementation and unit tests, using an 80% coverage gate for each supported metric. API/UI functional testing has separate applicability and produces executed or N/A reports before the Documenter's code-review gate; no separate QA agent is required.

## Existing Documents Flow

```text
Existing requirement folder
-> Requirement Intake Consolidator
-> Context, BRD, Requirements, Gap Report, Traceability Matrix
-> Traceability Manager
-> Technical Specifier
-> Technical Specifier automatically invokes Compliance Reviewer (spec gate)
-> Implementation Planner
-> Implementation Planner automatically invokes Compliance Reviewer (plan gate)
-> Implementation Builder
-> API Tester (uses output/{RUN_ID}/specify/spec.md; N/A when `API In Scope: NO`)
-> Functional Automation Test (uses output/{RUN_ID}/specify/spec.md; N/A when `UI In Scope: NO`)
-> Technical Documenter (automatically invokes Compliance Reviewer as code gate before final documentation)
-> Traceability Manager
```

## New Business Problem Flow

```text
Business problem
-> Context Builder (when project context is absent)
-> User Story Generator
-> Technical Specifier
-> Technical Specifier automatically invokes Compliance Reviewer (spec gate)
-> Implementation Planner
-> Implementation Planner automatically invokes Compliance Reviewer (plan gate)
-> Implementation Builder
-> API Tester (uses output/{RUN_ID}/specify/spec.md; N/A when `API In Scope: NO`)
-> Functional Automation Test (uses output/{RUN_ID}/specify/spec.md; N/A when `UI In Scope: NO`)
-> Technical Documenter (automatically invokes Compliance Reviewer as code gate before final documentation)
-> Traceability Manager
```

## Canonical Requirement Input

Use:

```text
.github/templates/requirements-input-template.md
```

Final `/specify` input:

```text
requirement/{ProjectName}_Requirements.md
```

## GitHub Traceability
Use one GitHub issue as the root anchor when available.

Track:
- Issue
- Branch
- Commit
- Pull request
- Run ID
- Trace IDs

## Quality Gate Rule

```text
If Critical gaps exist:
  Do not proceed to specification.
  Run consolidation or ask for clarification.

If only High or Medium gaps exist:
  Proceed only when gaps are accepted and documented.

If no Critical or High gaps exist:
  Proceed to specification.
```
