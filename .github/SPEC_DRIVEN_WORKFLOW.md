# Spec-Driven Workflow

Every PDLC stage is human-initiated. At the specification, planning, and post-test code gates, the responsible stage agent automatically invokes Compliance Reviewer before completing. The review does not start the next stage; a human reviews the result and manually starts the next stage. Critical findings block the handoff until resolved and re-reviewed.

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
-> Quality Tester
-> Technical Documenter (automatically invokes Compliance Reviewer as code gate before final documentation)
-> Traceability Manager
```

## New Business Problem Flow

```text
Business problem
-> Context Clarifier
-> BRD Generator
-> Requirements Expander
-> User Story Generator
-> Technical Specifier
-> Technical Specifier automatically invokes Compliance Reviewer (spec gate)
-> Implementation Planner
-> Implementation Planner automatically invokes Compliance Reviewer (plan gate)
-> Implementation Builder
-> API Tester (uses output/{RUN_ID}/specify/spec.md; N/A when `API In Scope: NO`)
-> Functional Automation Test (uses output/{RUN_ID}/specify/spec.md; N/A when `UI In Scope: NO`)
-> Quality Tester
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
