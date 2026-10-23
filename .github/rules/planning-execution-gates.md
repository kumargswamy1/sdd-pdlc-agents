---
description: Execution gates and output schema for Implementation Planner runs.
---

# Planning Execution Gates

## Validation Checkpoints
- The planner must inspect `spec.md`'s `## Clarification Log` before creating tasks. Every `CLAR-*` item must be `RESOLVED`, or the spec must explicitly state `CLARIFICATION_STATUS: NOT_REQUIRED` with evidence.
- If any `CLAR-*` item is `OPEN`, unanswered, incomplete, contradictory, or lacks a resulting `SPEC-*` decision, the planning run is `BLOCKED`; do not create final planning tasks or carry the ambiguity forward as an assumption.
- Every `SPEC-*` in scope is mapped to one or more `TASK-*` items.
- Every `FR-*` and `NFR-*` referenced by in-scope `SPEC-*` is covered by planned tasks.
- Every scope bullet in `plan.md` maps to at least one task in `tasks.md`.
- Every effective-screen node or `SCR-*` screenshot screen from spec (or grouped set) is mapped to at least one task.
- `tasks.md` includes verification method and dependency metadata (`BLOCKED_BY`) for every task.
- `tasks.md` uses a deterministic task table schema with at least: `TASK ID`, `Description`, `Trace (SPEC/FR/NFR)`, `BLOCKED_BY`, and `Verification`.
- Security/privacy/compliance tasks are present only when required by source spec and requirements.
- API impact tasks are present when spec declares `EXISTING_API_CHANGE` or `NEW_API_REQUIRED`.
- Every row in spec `Requirement-to-SPEC Logic Coverage` is represented by one or more planned tasks, or explicitly marked as inherited existing behavior with verification evidence.
- No requirement-logic rule from spec is dropped, generalized, or converted into a weaker statement during planning.
- Assess both frontend and backend against approved story scope. Carry spec's independent change declarations and unit-test applicability into plan.md/tasks.md with evidence and trace references. Plan implementation/unit tasks only for changed surfaces; use an 80% coverage gate per required surface and supported metric. Missing work or ambiguous scope is a blocker, not `NOT_APPLICABLE`.
- Document reused unchanged APIs/screens and required integration/functional verification without inventing implementation or unit-test tasks for them.

## Required Plan Structure
`plan.md` MUST include `## Requirement Logic To Task Coverage` with at least:
- `REQ_REF`
- `Mapped SPEC-*`
- `Mapped TASK-*`
- `Coverage Type` (`DIRECT_IMPLEMENTATION` or `INHERITED_EXISTING_BEHAVIOR`)
- `Verification`
- `Status` (`COVERED` or `BLOCKED`)

`REQ_REF` values MUST come from spec coverage rows.
If any row is `BLOCKED`, planner run is `BLOCKED`.

## Hard Gates

### Upstream Spec Readiness Required
- Do not generate final planning outputs when upstream spec is incomplete or blocked.
- Do not generate final planning outputs while any `CLAR-*` clarification item in `spec.md` is unresolved.
- If `spec.md` indicates blocked status (for example unresolved conflicts, missing mandatory evidence, or requirement coverage failure), stop and report `BLOCKED`. A Figma MCP failure is not a blocked status when `DESIGN_EVIDENCE_STATUS: AVAILABLE` from screenshots or manual uploads.
- Require ready upstream signals before completion:
  - `Status: SUCCESS` (or equivalent ready state) in spec artifacts.
  - No unresolved hard-gate notes in spec/compliance outputs.
  - `REQUIREMENT_COVERAGE_RESULT` present with `MISSING_RULES: 0` and `CONTRADICTIONS: 0`.
- Do not proceed if effective-screen mappings use placeholder IDs (`DUMMY-*`, `TBD`, `TBA`) unless simulation mode is explicitly approved. Screenshot IDs (`SCR-*`) are valid identifiers.
- A recorded Figma extraction failure (MCP error, rate limit, auth, network) is a gap, not a blocker, when alternate design evidence is available.

### Design Evidence Required (UI In Scope)
- If spec declares `UI In Scope = YES`, require `DESIGN_EVIDENCE_STATUS: AVAILABLE` in spec.md and screenshots in `output/{RUN_ID}/specify/figma/png/screens/`.
- If `SOURCE` is `USER_STORY_SCREENSHOTS`, `LOCAL_ARTIFACTS`, or `MANUAL_UPLOAD` (no Figma link), do not block. Proceed with the plan and:
  - Add `Design Source: Manual upload (no Figma link)` at the top of `plan.md`, `tasks.md`, and `frontend/components.md`.
  - Reference `SCR-*` screen IDs and screenshot paths in place of Figma node IDs in screen-to-task mappings.
  - Note in each UI task that visual fidelity is verified against manually supplied screenshots, without Figma JSON hierarchy.
- If `UI In Scope = YES` and status is `PENDING_MANUAL_UPLOAD`, do not generate plan or task outputs. Report `BLOCKED` with unblock action: add screenshots to `output/{RUN_ID}/specify/figma/png/screens/` and re-run Technical Specifier with the same `RUN_ID`.
- If screenshots exist in the folder but spec.md still shows `PENDING_MANUAL_UPLOAD`, report `BLOCKED` and ask for a Technical Specifier re-run; do not read the screenshots directly.
- If `UI In Scope = NO` (`DESIGN_EVIDENCE_STATUS: NOT_REQUIRED`), skip screenshot, per-screen, visual-fidelity, and frontend component-inventory requirements. Record `NOT_APPLICABLE` with scope evidence; do not require design files or create placeholder UI tasks.

## Required Status Reporting
Include these one-line fields in final output:
- `PLANNER_STATUS_SUMMARY: <plain one-line human message>`
- `PLANNER_STATUS_DETAIL: [SUCCESS|BLOCKED] [REASON: <short reason>] [UNBLOCK_ACTION: <action-or-n/a>]`
- `PLANNER_CLARIFICATION_STATUS: [READY|BLOCKED] [OPEN_ITEMS: <n>] [UNBLOCK_ACTION: <action-or-n/a>]`
- `PLANNER_DESIGN_SOURCE: [LIVE_FIGMA_API|USER_STORY_SCREENSHOTS|LOCAL_ARTIFACTS|MANUAL_UPLOAD|NOT_REQUIRED] [NOTE: <e.g. Manual upload (no Figma link) or n/a>]`
- `PLAN_REQUIREMENT_COVERAGE_SUMMARY: <plain one-line human message>`
- `PLAN_REQUIREMENT_COVERAGE_RESULT: [SUCCESS|FAILURE] [TOTAL_RULES: <n>] [TASK_COVERED_RULES: <n>] [MISSING_TASK_RULES: <n>] [AMBIGUOUS_TASK_RULES: <n>] [CONTRADICTIONS: <n>]`

If `MISSING_TASK_RULES > 0` or `CONTRADICTIONS > 0`, planner run is `BLOCKED`.

## Post-Execution Validation
1. Re-read all generated files in `output/{RUN_ID}/plan/`.
2. Verify all in-scope `SPEC-*` IDs are mapped to `TASK-*` without gaps.
3. Verify every task has `BLOCKED_BY`, verification method, and trace links.
4. Verify `## Pre-submit checks` exists in `tasks.md` and all checks are answered.
5. Verify effective-screen node coverage tasks are present when nodes are listed in spec.
6. Verify no dangling references across plan files (`SPEC-*`, `FR-*`, `NFR-*`, `TASK-*`).
7. Verify no placeholder node IDs (`DUMMY-*`, `TBD`, `TBA`) unless simulation mode is explicit.
8. Re-read spec coverage table and verify one-to-many mapping into planner coverage table with zero gaps.
9. Verify each requirement-logic row has at least one matching verification in tasks/tests artifacts.
10. Report gaps or contradictions; if critical, mark run `BLOCKED`.
