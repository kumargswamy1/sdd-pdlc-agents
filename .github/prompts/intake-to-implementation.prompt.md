---
description: "Run the full spec-driven workflow from existing docs to implementation."
---

# Intake To Implementation Workflow

Use this prompt when the user wants a complete spec-driven run from existing requirement documents.

Arguments expected from the user:
- Source folder
- Project name
- Optional GitHub issue URL or number

This prompt is a runbook. Every PDLC stage is a **HUMAN CHECKPOINT**: perform exactly one stage per invocation, produce its output, report `NEXT_STEP`, and stop. The Specifier, Planner, and final Documenter automatically invoke Compliance Reviewer at their respective gates. Do not start the next PDLC stage until the human explicitly runs it.

1. Requirement intake: act as `Requirement Intake Consolidator`.
2. Intake gate: act as `Traceability Manager`; stop on Critical gaps.
3. Specification: human starts `Technical Specifier`.
4. Spec review: Technical Specifier automatically invokes `Compliance Reviewer`; Critical, High, or Medium findings block the handoff until remediated and re-reviewed or explicitly accepted. Low-only `FAIL` results warn but do not automatically block.
5. Planning & Tasks: human starts `Implementation Planner`.
6. Plan review: Implementation Planner automatically invokes `Compliance Reviewer`; Critical, High, or Medium findings block the handoff until remediated and re-reviewed or explicitly accepted. Low-only `FAIL` results warn but do not automatically block.
7. Implementation: human starts `Implementation Builder`.
8. Backend API testing: human starts `API Tester` using `output/{RUN_ID}/specify/spec.md`; the agent reports N/A when `API In Scope: NO`.
9. Component functional testing: human starts `Functional Automation Test` using `output/{RUN_ID}/specify/spec.md`; the agent reports N/A when `UI In Scope: NO`.
10. Final code review and documentation: after applicable API/UI testing or evidence-backed N/A reports, the human starts `Technical Documenter`, which invokes `Compliance Reviewer` before final documentation; Critical, High, or Medium findings block the handoff until remediated and re-reviewed or explicitly accepted. Low-only `FAIL` results warn but do not automatically block. Preserve independent stage hard gates.
11. Final traceability: human starts `Traceability Manager`.
12. Final report: list generated files, run ID, gaps, findings, and PR readiness.

Follow `.github/copilot-instructions.md` and the severity-based review policy in `.github/rules/pdlc.md`. Preserve every `FAIL` status and keep all findings visible. Emit `REVIEW_GATE_WARNING` for Low-only failures; any Critical, High, or Medium finding blocks unless explicitly accepted by a human. Preserve independent stage hard gates.
