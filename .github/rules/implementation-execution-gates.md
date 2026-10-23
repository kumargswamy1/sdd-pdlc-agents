---
description: Execution gates and output schema for Implementation Builder runs.
---

# Implementation Execution Gates

## Validation Checkpoints
- Apply screen, screenshot, and visual-fidelity checks only when `UI In Scope: YES`. For `UI In Scope: NO`, record `NOT_APPLICABLE` with scope evidence and skip design-file requirements; backend and unit-test gates still apply according to change scope.
- Every in-scope `TASK-*` maps to one or more `CODE-*` references.
- Every in-scope `SPEC-*` has implementation coverage and linked tests.
- Every effective screen from spec.md has a documented per-screen section with component list, layout, and visual PNG reference.
- For every effective screen, implementation captures design attributes from spec.md per-screen section (component names, variants, labels, colors, typography, spacing, states, icons).
- Implementation references PNG screenshots from `output/{RUN_ID}/specify/figma/png/screens/` for visual verification of colors, spacing, positioning, state rendering.
- Screen-level labels/text match requirement/spec wording unless explicitly inherited.
- Requirement-logic behavior (conditions, option sets, editability, transitions, prefixes) is preserved exactly as documented in spec.
- API impact decision is enforced (`NO_API_CHANGE`, `EXISTING_API_CHANGE`, `NEW_API_REQUIRED`) with required contract/client updates.
- Security/privacy/audit controls from in-scope tasks are implemented and tested.
- No plaintext PII, credentials, account numbers, holdings, tokens, or secrets in code/logs/tests/artifacts.

## Required Evidence Structure
When `UI In Scope: YES`, required outputs under `output/{RUN_ID}/implement/design/`:
- `spec-to-code-mapping.json`
- `screen-implementation-report.md`

`screen-implementation-report.md` MUST include `## Screen Implementation Coverage` with columns:
- `Screen Name`
- `Node ID / Screen ID` (Figma node ID or `SCR-*` screenshot ID)
- `Design Source` (`LIVE_FIGMA_API` or `Manual upload (no Figma link)`)
- `Spec Section` (reference to spec.md per-screen section)
- `PNG Screenshot` (path to visual reference)
- `Mapped TASK-*`
- `Mapped CODE-*`
- `Implementation Status` (`IMPLEMENTED` or `BLOCKED`)
- `Design Fidelity Notes`

If any screen row is `BLOCKED`, run is `BLOCKED`.
For `UI In Scope: NO`, record design evidence as `NOT_APPLICABLE` in implementation notes; do not require the design directory or screen reports.

### Unit Test Evidence

Persist under `output/{RUN_ID}/implement/unit-tests/`:
- `report.md` with the exact commands, working directories, exit codes, execution time, coverage scope, exclusions and rationale, failures, and native report paths for each surface.
- For each required surface, separate `frontend/` and/or `backend/` evidence containing command output and native machine-readable coverage reports (for example, coverage-summary JSON, LCOV, or coverage XML). Unchanged surfaces require only their applicability rationale in `report.md`, not suite output, coverage reports, or evidence directories.

Include this table in `report.md` and in the final response, using measured values only:

| Surface | Passed | Failed | Skipped | Statements % | Branches % | Functions % | Lines % | Required % | Status | Evidence |
|---------|--------|--------|---------|--------------|------------|-------------|---------|------------|--------|----------|

Use one row per surface, with `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE` status. For required surfaces, link saved test output and coverage reports in Evidence. For an unchanged surface, give the spec/plan rationale and implementation evidence, using `N/A` for counts, metrics, and threshold, not invented zeros. Use `NOT_SUPPORTED` only for metrics the native tool does not provide, with an explanation; unavailable reports for required surfaces are `BLOCKED`, not unsupported.

## Hard Gates

### Frontend and Backend Unit Tests Required
- Determine applicability independently for each surface using the approved story/spec, plan/tasks, and actual implementation changes. When no backend changes are required or made, skip backend unit-test creation/execution and coverage; do the same for frontend when no frontend changes are required or made. Record `NOT_APPLICABLE`, `N/A` counts/metrics/threshold, and linked scope evidence in the results table. Missing test tooling or reports for an unchanged surface is not a blocker.
- Using an existing API or screen unchanged does not make that surface's unit tests applicable. Any actual change makes the surface `REQUIRED`; incomplete implementation, missing tasks, or unclear/conflicting scope cannot justify an exemption. These exemptions do not remove separately required API, integration, or functional testing.
- After implementing production code, write or update and execute unit tests for every in-scope frontend and backend surface before completing this stage.
- Each required surface must independently meet an 80% coverage gate for lines, statements, branches, and functions where supported by its native tool. Flutter requires executable-line coverage. Apply the same 80% gate to all layers, including validation; measured coverage may exceed it.
- Use the approved project production-source scope, including untested files; report the scope explicitly. Do not substitute a narrow selected-file report or combined frontend/backend average for surface totals.
- Configure the native runner's coverage thresholds when supported and verify the measured report against every required metric. Do not lower thresholds, add coverage exclusions to make the run pass, or replace unit coverage with API/integration/end-to-end coverage.
- Any failed unit test or required metric below threshold blocks completion. Missing tests/reports, an unexecuted suite, an unexplained skipped required test, or an execution/tooling failure also blocks completion with an explicit unblock action.
- A surface may be `NOT_APPLICABLE` only when approved scope and implementation evidence confirm no changes are required or made to that surface. For required suites, existing unrelated failures must be reported as blockers, not silently fixed or represented as passing.
- Show the Unit Test Evidence results table before any successful next-stage handoff.

### Upstream Readiness Required
Require before completion:
- `Status: SUCCESS` in `spec.md`.
- `REQUIREMENT_COVERAGE_RESULT` with `MISSING_RULES: 0` and `CONTRADICTIONS: 0`.
- Planner continuity result with `MISSING_TASK_RULES: 0` and `CONTRADICTIONS: 0`.
- When `UI In Scope: YES`, spec.md per-screen design sections are complete and self-contained; otherwise record `NOT_APPLICABLE`.

### Spec & PNG Artifacts Available
All requirements in this subsection apply only when `UI In Scope: YES`. For `UI In Scope: NO` with `DESIGN_EVIDENCE_STATUS: NOT_REQUIRED`, skip them and record `NOT_APPLICABLE`; absent screenshots, per-screen sections, and Figma JSON do not block backend-only work.

- If spec declares `UI In Scope = YES`, require `DESIGN_EVIDENCE_STATUS: AVAILABLE` in spec.md; `PENDING_MANUAL_UPLOAD` blocks implementation.
- If design source is `USER_STORY_SCREENSHOTS`, `LOCAL_ARTIFACTS`, or `MANUAL_UPLOAD` (no Figma link), do not block. Implement from spec.md per-screen sections and the screenshots, use `SCR-*` IDs, and record `Design Source: Manual upload (no Figma link)` in implementation evidence. Missing Figma JSON hierarchy is expected in this case; use the control order documented in spec.md and confirmed against the screenshot. Values marked `APPROXIMATE_FROM_SCREENSHOT` use the nearest project design token.
- Spec.md per-screen sections contain all component details, layout, interactive elements, and states.
- PNG screenshot files exist at `output/{RUN_ID}/specify/figma/png/screens/` for visual reference.
- Do NOT call Figma MCP or re-parse JSON—all extracted design information is in spec.md.
- If spec.md per-screen sections are incomplete or PNG files are missing, mark run `BLOCKED` with explicit unblock action.

### API Impact Alignment Required
- If spec indicates `EXISTING_API_CHANGE` or `NEW_API_REQUIRED`, implementation MUST include corresponding API client/contract updates and verification.
- If UI change requires backend behavior unavailable in current APIs, mark run `BLOCKED` and report required API delta.

### Requirement and Design Conflict Handling
- If design evidence contradicts requirement/spec business logic, do not silently implement design-only behavior.
- Flag conflict, preserve requirement-critical behavior, and mark run `BLOCKED` pending clarification.

## Required Status Reporting
Include these one-line fields in final output:
- `IMPLEMENT_MCP_STATUS_SUMMARY: <plain one-line human message>`
- `IMPLEMENT_MCP_API_RESULT: [SUCCESS|FAILURE|NOT_APPLICABLE] [API: GET <endpoint>] [HTTP: <status>] [ERROR: <message-or-n/a>] [RETRY_AFTER: <seconds-or-n/a>] [NODE_TYPE: <type-or-n/a>] [CHILD_COUNT: <count-or-n/a>]` (use `NOT_APPLICABLE` for manual-upload design sources)
- `IMPLEMENT_DESIGN_SOURCE: [LIVE_FIGMA_API|USER_STORY_SCREENSHOTS|LOCAL_ARTIFACTS|MANUAL_UPLOAD|NOT_REQUIRED] [NOTE: <e.g. Manual upload (no Figma link) or n/a>]`
- `UI_FIDELITY_SUMMARY: <plain one-line human message>`
- `UI_FIDELITY_RESULT: [SUCCESS|FAILURE|NOT_APPLICABLE] [TOTAL_NODES: <n>] [MATCHED_NODES: <n>] [MISSING_NODE_ARTIFACTS: <n>] [STYLE_MISMATCHES: <n>] [TEXT_MISMATCHES: <n>] [CONTRADICTIONS: <n>]`

If `MISSING_NODE_ARTIFACTS > 0` or `CONTRADICTIONS > 0`, run is `BLOCKED`. For manual-upload design sources, count only missing screenshots as missing artifacts; absent Figma JSON is not counted.
For `UI In Scope: NO`, emit `UI_FIDELITY_RESULT: NOT_APPLICABLE` with zero screen/mismatch counts and the scope rationale in `UI_FIDELITY_SUMMARY`. Do not require artifacts to produce this result.

## Post-Execution Validation
1. Re-read modified code, tests, and evidence files.
2. Verify each implemented `TASK-*` has corresponding `CODE-*` and verification.
3. When UI is in scope, verify each effective screen has a spec section and a referenced screenshot under `output/{RUN_ID}/specify/figma/png/screens/`. Figma parent JSON paths are recorded in `summary.json`; Builder does not re-parse or require per-screen JSON or a `nodes/` directory. For manual uploads, no Figma JSON is required.
4. When UI is in scope, verify `output/{RUN_ID}/implement/design/screen-implementation-report.md` has no `BLOCKED` rows and `spec-to-code-mapping.json` covers all effective screens. Otherwise mark both checks `NOT_APPLICABLE`.
5. Re-check requirement logic continuity for value-level rules.
6. Re-check no dangling references across `TASK-*`, `SPEC-*`, `FR-*`, `NFR-*`, `CODE-*`, and tests.
7. Re-run relevant syntax/lint/test checks where feasible.
8. Report gaps; if critical, mark run `BLOCKED`.
9. Verify that both applicable unit suites were executed, their native coverage reports match the final results table, and every required threshold passed. Otherwise mark run `BLOCKED` and do not issue a successful handoff.
