---
description: PDLC rules for spec-driven workflows.
---

# PDLC Standards

## Flow

```text
Context -> BRD -> Requirements -> Spec -> Plan -> Implement -> Test -> Review -> Document -> Trace
```

For existing documents:

```text
Intake -> Gap Report -> Consolidated Requirements -> Spec -> Plan -> Implement
```

## Human Checkpoints
- Every PDLC stage is human-initiated. Each stage agent produces its output, stops, and emits `NEXT_STEP`; the human reviews the output and manually starts the next stage.
- Technical Specifier, Implementation Planner, and Technical Documenter automatically invoke Compliance Reviewer at the spec, plan, and post-test code gates, respectively. These bounded reviews do not start the next stage.
- Critical, High, and Medium review findings block the handoff. Keep the review status as `FAIL`, make every finding visible, and stop until a human records remediation or explicit acceptance. After remediation, rerun the review before continuing; an explicitly accepted finding must remain visible in the handoff.
- A finding that causes review failure must remain `FAIL` regardless of severity; severity controls blocking, not the reported status. Low-severity findings do not automatically block the handoff. If a review has only Low findings, preserve its `FAIL` status and emit `REVIEW_GATE_WARNING: Low-severity review failure does not automatically stop this handoff; unresolved findings may carry downstream. Human disposition required.` Keep all findings visible for human disposition.
- Review status and automatic stop policy are separate: never relabel a `FAIL` as `PASS` merely because its findings do not block the handoff. If findings have mixed severities, apply the highest-severity outcome; any Critical, High, or Medium finding blocks.
- Independent stage hard gates still block completion, including failed required unit tests or coverage below 80%. A nonblocking review result cannot override them.
- Workflow prompts pause after every step and continue only on explicit human instruction.

> [!WARNING]
> Only a review failure containing Low-severity findings and no Critical, High, or Medium findings may proceed with a warning. Critical, High, or Medium findings block the handoff until a human records remediation or explicit acceptance. Keep all findings visible and preserve the review status; independent stage hard gates remain blocking.

After implementation, humans start API Tester and Functional Automation Test for applicable story scope; each produces executed results or evidence-backed `NOT_APPLICABLE`. There is no separate Quality Tester stage. Technical Documenter then invokes the code compliance review before final documentation, using implementation/unit evidence and both test-stage reports. Acceptance checks outside API/UI automation must remain visible as human-verification gaps, not fabricated QA results.

## Quality Gates
- Requirements pass canonical structure checks.
- Traceability matrix is updated.
- Specification maps to `FR-*` and `NFR-*`.
- Plan maps tasks to specs and requirements.
- Implementation maps code to tasks.
- Tests map to requirements and acceptance criteria.
- Review findings are resolved or explicitly accepted.
- Documentation reflects implemented behavior.

## Stop Conditions
- Critical requirement gaps.
- Missing compliance-critical information.
- Missing authorization design for protected customer data.
- Missing data classification for PII or sensitive financial data.
- Hardcoded secrets or real customer data.

## Output Directories
Use:

```text
output/{RUN_ID}/specify/
output/{RUN_ID}/plan/
output/{RUN_ID}/implement/
output/{RUN_ID}/tests/
output/{RUN_ID}/review/
output/{RUN_ID}/docs/
```
