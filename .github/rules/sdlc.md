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
- Every PDLC stage is human-initiated. Each agent produces its output, stops, and emits `NEXT_STEP`; the human reviews the output and manually runs the next agent.
- Agents must not start the next stage or invoke its agent.
- Workflow prompts pause after every step and continue only on explicit human instruction.

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
