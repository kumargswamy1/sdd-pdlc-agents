# Spec-Driven Workflow

Every stage is human-initiated. Each agent produces its output and stops; a human reviews it and manually runs the next agent. No stage starts automatically.

## Existing Documents Flow

```text
Existing requirement folder
-> Requirement Intake Consolidator
-> Context, BRD, Requirements, Gap Report, Traceability Matrix
-> Traceability Manager
-> Technical Specifier
-> Compliance Reviewer
-> Implementation Planner
-> Compliance Reviewer
-> Implementation Builder
-> API Tester (uses output/{RUN_ID}/specify/spec.md; N/A when `API In Scope: NO`)
-> Functional Automation Test (uses output/{RUN_ID}/specify/spec.md; N/A when `UI In Scope: NO`)
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
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
-> Implementation Planner
-> Implementation Builder
-> API Tester (uses output/{RUN_ID}/specify/spec.md; N/A when `API In Scope: NO`)
-> Functional Automation Test (uses output/{RUN_ID}/specify/spec.md; N/A when `UI In Scope: NO`)
-> Quality Tester
-> Compliance Reviewer
-> Technical Documenter
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
