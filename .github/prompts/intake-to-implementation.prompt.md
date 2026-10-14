---
description: "Run the full spec-driven workflow from existing docs to implementation."
---

# Intake To Implementation Workflow

Use this prompt when the user wants a complete spec-driven run from existing requirement documents.

Arguments expected from the user:
- Source folder
- Project name
- Optional GitHub issue URL or number

Run this workflow:

1. Requirement intake: act as `Requirement Intake Consolidator`.
2. Intake gate: act as `Traceability Manager`; stop on Critical gaps.
3. Specification: act as `Technical Specifier`.
4. Spec review: act as `Compliance Reviewer`; stop on Critical findings.
5. Planning: act as `Implementation Planner`.
6. Plan review: act as `Compliance Reviewer`; stop on Critical findings.
7. Implementation: act as `Implementation Builder`.
8. Backend API testing: act as `API Tester` using `output/{RUN_ID}/plan/contracts/backend-apis.json` after implementation.
9. Component functional testing: act as `Functional Automation Test` using `output/{RUN_ID}/plan/frontend/components.md` after implementation.
10. User-workflow test design: act as `Quality Tester`.
11. Code review: act as `Compliance Reviewer`; stop on Critical findings.
12. Documentation: act as `Technical Documenter`.
13. Final traceability: act as `Traceability Manager`.
14. Final report: list generated files, run ID, gaps, findings, and PR readiness.

Follow `.github/copilot-instructions.md`.
