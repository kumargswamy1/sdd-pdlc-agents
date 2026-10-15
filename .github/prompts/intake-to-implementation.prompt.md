---
description: "Run the full spec-driven workflow from existing docs to implementation."
---

# Intake To Implementation Workflow

Use this prompt when the user wants a complete spec-driven run from existing requirement documents.

Arguments expected from the user:
- Source folder
- Project name
- Optional GitHub issue URL or number

This prompt is a runbook. Every step is a **HUMAN CHECKPOINT**: perform exactly one step per invocation, produce its output, report `NEXT_STEP`, and stop. Do not start the next step until the human explicitly runs it (by starting the named agent or re-invoking this prompt with the step number).

1. Requirement intake: act as `Requirement Intake Consolidator`.
2. Intake gate: act as `Traceability Manager`; stop on Critical gaps.
3. Specification: human starts `Technical Specifier`.
4. Spec review: human starts `Compliance Reviewer`; stop on Critical findings.
5. Planning & Tasks: human starts `Implementation Planner`.
6. Plan review: human starts `Compliance Reviewer`; stop on Critical findings.
7. Implementation: human starts `Implementation Builder`.
8. Backend API testing: human starts `API Tester` using `output/{RUN_ID}/specify/spec.md`; the agent reports N/A when `API In Scope: NO`.
9. Component functional testing: human starts `Functional Automation Test` using `output/{RUN_ID}/specify/spec.md`; the agent reports N/A when `UI In Scope: NO`.
10. User-workflow testing: human starts `Quality Tester`.
11. Code review: human starts `Compliance Reviewer`; stop on Critical findings.
12. Documentation: human starts `Technical Documenter`.
13. Final traceability: human starts `Traceability Manager`.
14. Final report: list generated files, run ID, gaps, findings, and PR readiness.

Follow `.github/copilot-instructions.md`.
