---
description: Execution gates and output schema for Implementation Builder runs.
---

# Implementation Execution Gates

## Validation Checkpoints
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
Required outputs under `output/{RUN_ID}/implement/design/`:
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

## Hard Gates

### Upstream Readiness Required
Require before completion:
- `Status: SUCCESS` in `spec.md`.
- `REQUIREMENT_COVERAGE_RESULT` with `MISSING_RULES: 0` and `CONTRADICTIONS: 0`.
- Planner continuity result with `MISSING_TASK_RULES: 0` and `CONTRADICTIONS: 0`.
- Spec.md per-screen design sections are complete and self-contained.

### Spec & PNG Artifacts Available
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
- `UI_FIDELITY_RESULT: [SUCCESS|FAILURE] [TOTAL_NODES: <n>] [MATCHED_NODES: <n>] [MISSING_NODE_ARTIFACTS: <n>] [STYLE_MISMATCHES: <n>] [TEXT_MISMATCHES: <n>] [CONTRADICTIONS: <n>]`

If `MISSING_NODE_ARTIFACTS > 0` or `CONTRADICTIONS > 0`, run is `BLOCKED`. For manual-upload design sources, count only missing screenshots as missing artifacts; absent Figma JSON is not counted.

## Post-Execution Validation
1. Re-read modified code, tests, and evidence files.
2. Verify each implemented `TASK-*` has corresponding `CODE-*` and verification.
3. Verify every effective node has both JSON and PNG artifacts under `nodes/` for Figma sources, or a screenshot PNG for `SCR-*` manual-upload screens.
4. Verify `screen-fidelity-report.md` has no `BLOCKED` rows.
5. Re-check requirement logic continuity for value-level rules.
6. Re-check no dangling references across `TASK-*`, `SPEC-*`, `FR-*`, `NFR-*`, `CODE-*`, and tests.
7. Re-run relevant syntax/lint/test checks where feasible.
8. Report gaps; if critical, mark run `BLOCKED`.
