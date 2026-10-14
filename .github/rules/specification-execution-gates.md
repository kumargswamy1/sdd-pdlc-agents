---
description: Execution gates and output schema for Technical Specifier runs.
---

# Specification Execution Gates

## Preflight Change Classification (Required)
Before writing spec content, determine change type using mandatory evidence inputs.

### Step 1: Collect 3 Evidence Inputs
- Requirement text evidence: objective, preconditions, business rules, references.
- Existing trace-chain evidence from `requirement/Traceability_Matrix.md`: whether this capability already has FR/SPEC/TASK history.
- Existing implementation footprint evidence: impacted routes, screens, components, and services in current codebase.

### Step 2: Classify Change Type Using Strict Rules
- `NEW_STORY`: no prior trace chain for this capability and requirement introduces new functional flow (new route, screen, domain behavior, or integration).
- `ENHANCEMENT_UI_ONLY`: prior trace chain exists and only labels/layout/style/components/states change; no business-rule or transition change.
- `ENHANCEMENT_LOGIC_ONLY`: prior trace chain exists and business rules/conditions/transitions/integration logic change; no UI-node impact.
- `ENHANCEMENT_UI_AND_LOGIC`: prior trace chain exists and both UI and business logic change.
- If evidence is insufficient or contradictory, classify as `BLOCKED`.

### Step 3: Emit Scope Declaration In `spec.md`
`spec.md` MUST include a section named `## Change Scope Declaration` with at least:
- `Change Type`
- `UI In Scope`: YES/NO
- `Logic In Scope`: YES/NO
- `API In Scope`: YES/NO
- `API Impact Type`: NO_API_CHANGE/EXISTING_API_CHANGE/NEW_API_REQUIRED
- `Impacted Existing Nodes`
- `New Nodes Required`: YES/NO
- `Inherited Existing Behavior` list

## Validation Checkpoints
- All `FR-*` and `NFR-*` are mapped to `SPEC-*`.
- All screens in Figma are accounted for or explicitly excluded with reason.
- No gaps in requirements before speccing; flag and request clarification if found.
- No invented financial, regulatory, or security requirements; only apply what's in source requirements.
- Do not assume UI, business-logic, API, status-transition, field-rule, or integration behavior that is not evidenced by requirement text, trace history, or implementation footprint.
- If required behavior cannot be evidenced, mark it `BLOCKED` and request clarification instead of inferring.
- Figma MCP inspection evidence is captured when Figma artifacts are available (root node type, root node ID, child count, and effective-vs-excluded node decision log); otherwise the design evidence source and failure reason are recorded.
- API impact assessment is explicit: NO_API_CHANGE, EXISTING_API_CHANGE, or NEW_API_REQUIRED.
- For EXISTING_API_CHANGE or NEW_API_REQUIRED, spec MUST define endpoint, method, request/response delta, error behavior, and versioning impact.
- Every business-rule statement in the source requirement is mapped to at least one `SPEC-*` item, or explicitly marked as inherited behavior with rationale.
- User story intent, preconditions, triggers, status transitions, field editability, option constraints, and exceptional-path rules are all explicitly covered in `spec.md`.

## Required Spec Structure
`spec.md` MUST include all sections below:
- `## Change Scope Declaration`
- `## Requirement-to-SPEC Logic Coverage`
- User story intent interpretation.
- Entry trigger and preconditions.
- Field-level behavior matrix (prefill source, editable state, constraints).
- Status-transition matrix (source status, condition, target status).
- Exceptional-case behavior.
- API change assessment (impact type, contract delta, backward compatibility).

`Requirement-to-SPEC Logic Coverage` MUST include columns:
- `REQ_REF`
- `Requirement Logic Statement`
- `Mapped SPEC-*`
- `Coverage Type` (`DIRECT` or `INHERITED_EXISTING_BEHAVIOR`)
- `Implementation Notes`
- `Status` (`COVERED` or `BLOCKED`)

## Hard Gates

### Design Evidence (Non-Blocking For Spec)
- If `UI In Scope = NO`, Figma and screenshots are optional; set `DESIGN_EVIDENCE_STATUS: NOT_REQUIRED`.
- If `UI In Scope = YES`, gather design evidence in order: live Figma → user story/Confluence screenshots → local screenshots in `output/{RUN_ID}/specify/figma/png/screens/`.
- Do not finalize screen inventory from Figma URL parsing alone; when Figma extraction succeeds, inspect the entry node plus child nodes.
- If Figma extraction fails (MCP error, rate limit, auth, network, or tool unavailable), do not block. Record the error and continue with the next evidence source.
- If no design evidence exists, complete the spec with `DESIGN_EVIDENCE_STATUS: PENDING_MANUAL_UPLOAD`, list expected screens under `## Pending Design Evidence`, and ask the user to add screenshots to `output/{RUN_ID}/specify/figma/png/screens/`.
- If screens come from Jira/Confluence user story screenshots or manual uploads (no Figma link), set `DESIGN_EVIDENCE_STATUS: AVAILABLE`, assign `SCR-<nnn>` screen IDs, and record `Design Source: Manual upload (no Figma link)` in spec.md and `figma_report.md`. This is a ready state; do not block.
- Planning and implementation remain blocked until `DESIGN_EVIDENCE_STATUS: AVAILABLE` when `UI In Scope = YES`.

### Requirement Logic Coverage Required
- Do not declare `Status: SUCCESS` if any business-logic statement lacks explicit mapping.
- Do not treat high-level summaries as sufficient coverage for rule-level requirements.
- If any required rule is missing, contradictory, or ambiguous, mark run `BLOCKED`.

### Change Classification Required
- Do not proceed with final output without completing preflight classification.
- If `UI In Scope = YES`: screen coverage is mandatory; Figma node analysis is required only when Figma artifacts are available.
- If `UI In Scope = NO`: skip UI checks only with explicit `N/A` justification in spec.
- If `Logic In Scope = YES`: full requirement-to-spec logic coverage is mandatory.
- If `API In Scope = YES` or `API Impact Type` is `EXISTING_API_CHANGE`/`NEW_API_REQUIRED`: API contract delta definition is mandatory.
- If classification remains ambiguous, mark run `BLOCKED`.

### No-Assumption Policy Required
- Do not declare success when any UI, logic, or API decision depends on unstated assumptions.
- Any inferred behavior must be backed by explicit evidence from requirement text, trace chain, or implementation footprint and recorded in spec.
- If evidence is missing or contradictory, mark run `BLOCKED` and request clarification.

## Required Status Reporting
Include these one-line fields in final output:
- `MCP_STATUS_SUMMARY: <plain one-line human message>`
- `MCP_API_RESULT: [SUCCESS|FAILURE|NOT_APPLICABLE] [API: GET <endpoint>] [HTTP: <status>] [ERROR: <message-or-n/a>] [RETRY_AFTER: <seconds-or-n/a>] [NODE_TYPE: <type-or-n/a>] [CHILD_COUNT: <count-or-n/a>]` (use `NOT_APPLICABLE` when no Figma link exists; `FAILURE` is non-blocking when alternate design evidence is available)
- `CHANGE_CLASSIFICATION_SUMMARY: <plain one-line human message>`
- `CHANGE_CLASSIFICATION_RESULT: [NEW_STORY|ENHANCEMENT_UI_ONLY|ENHANCEMENT_LOGIC_ONLY|ENHANCEMENT_UI_AND_LOGIC|BLOCKED] [UI_IN_SCOPE: YES|NO] [LOGIC_IN_SCOPE: YES|NO] [API_IN_SCOPE: YES|NO] [API_IMPACT: NO_API_CHANGE|EXISTING_API_CHANGE|NEW_API_REQUIRED] [REASON: <short reason>]`
- `REQUIREMENT_COVERAGE_SUMMARY: <plain one-line human message>`
- `REQUIREMENT_COVERAGE_RESULT: [SUCCESS|FAILURE] [TOTAL_RULES: <n>] [COVERED_RULES: <n>] [MISSING_RULES: <n>] [AMBIGUOUS_RULES: <n>] [CONTRADICTIONS: <n>]`
- `DESIGN_EVIDENCE_STATUS: [AVAILABLE|PENDING_MANUAL_UPLOAD|NOT_REQUIRED] [SOURCE: LIVE_FIGMA_API|USER_STORY_SCREENSHOTS|LOCAL_ARTIFACTS|MANUAL_UPLOAD|NONE] [SCREENS: <n>] [UNBLOCK_ACTION: <action-or-n/a>]`
1. Re-read both spec.md and compliance-validation.md.
2. Verify Traceability_Matrix was updated with unique SPEC IDs.
3. Verify every SPEC entry against FR/NFR links.
4. Confirm screen table exists with valid Figma node IDs or `SCR-*` screenshot IDs and their screenshot paths.
5. Confirm MCP evidence or the alternate design evidence source (or pending-design status) is recorded.
6. Re-validate data models and contracts for syntax/undefined references.
7. Validate API impact decision and required contract deltas.
8. Re-validate banking controls against source requirements.
9. Re-validate classification output against requirement, trace chain, and implementation footprint.
10. Re-read source requirement and verify zero unmapped business-rule lines.
11. Validate explicit rule preservation for intent/triggers/preconditions/constraints/transitions/exceptions.
12. Report gaps; do not declare completion if critical issues remain.

---

## Spec Structure: Per-Screen Figma Design Documentation (When UI In Scope)

**REQUIRED ONLY IF**: `UI In Scope = YES` and design evidence is available (Figma JSON/PNG, user story/Confluence screenshots, or manual uploads).

**PURPOSE**: Technical Specifier is the **only agent** that reads Figma JSON/PNG files or screenshots. This section documents how design details are extracted and incorporated into spec.md so downstream agents (Plan, Implementation) never need to re-parse design artifacts.

**Screenshot-based screens (no Figma link)**: Use `Screen ID: SCR-<nnn>` in place of `Node ID`, reference the screenshot path as stored in `png/screens/`, add `Design Source: Manual upload (no Figma link)` to the section, and extract components, layout, and states visually from the screenshot. Mark visual values that cannot be measured exactly (for example, exact hex colors or pixel spacing) as `APPROXIMATE_FROM_SCREENSHOT` and map them to the nearest project design token; this is not a blocker.

### Per-Screen Template

For each effective screen in `figma_report.md`, create a dedicated section in `spec.md`:

```markdown
### Screen: {screen_name} (Node ID: {node_id})

**Overview**: [2-3 sentence description of purpose, context in user flow]

**Visual Reference**: 
![{screen_name}](../figma/png/screens/{screen_name}__{node_id}.png)

**Components**:
| Component | Type | Variant | Label | Action/Property |
|---|---|---|---|---|
| Button | Interactive | primary | "Scan" | Triggers camera access |
| TextField | Form | default | "Document ID" | Required, placeholder "Enter ID" |
| Icon | Display | toggleable | "Flash" | Toggle on/off, default off |

**Layout**:
- Structure: [Grid/Flex, direction, alignment]
- Spacing: [Padding, gaps between elements]
- Typography: [Font sizes, weights, line heights - if non-standard]

**Interactive Elements & Actions**:
- Tap "Scan" → execute camera capture workflow
- Toggle "Flash" icon → toggle device flashlight on/off
- [List all user-triggerable actions]

**Component States**:
- **Default**: [Appearance and behavior]
- **Error**: [Condition, appearance, message]
- **Disabled**: [When, appearance]
- [Additional states if applicable: loading, success, etc.]

**Integration Notes**:
- API calls required: [none/list endpoints]
- Data model fields exposed: [list]
- Permission requirements: [camera, microphone, etc.]
```

### Component Detail Extraction Checklist

For each component in the JSON file (`output/{RUN_ID}/specify/figma/json/screens/{screen_name}__{node_id}.json`), extract:

- ✓ **Name**: Exact component name from Figma
- ✓ **Type**: Interactive (Button, TextField, etc.) or Display (Icon, Text, Image, etc.)
- ✓ **Variant**: If present (e.g., "primary", "error", "disabled"). Source: `componentProperties.state`
- ✓ **Label/Text**: Visible text or placeholder
- ✓ **Action**: What happens on interaction (for interactive components)
- ✓ **Constraints**: Required field, min/max length, allowed values, pattern
- ✓ **Size/Style**: Size (small/medium/large), color (from design tokens), icon (if applicable)

### Artifact File References

When referencing extracted artifacts in spec.md:

- **Full-page flow diagram**: Reference `output/{RUN_ID}/specify/figma/png/0-*.png` early in spec (e.g., under "User Journey" section)
- **Per-screen visual**: Reference `output/{RUN_ID}/specify/figma/png/screens/{screen_name}__{node_id}.png` in each screen section
- **Component details source**: Internal extraction from `output/{RUN_ID}/specify/figma/json/screens/{screen_name}__{node_id}.json` (do NOT reference the JSON file path in final spec.md; all details should be documented inline)

### Data Flow Guarantee

Once spec.md is complete with all per-screen design sections:

- **Spec.md is self-contained**: All design information is explicitly documented in the spec sections
- **Plan Agent reads only spec.md**: Not the JSON or PNG files
- **Implementation Agent reads only plan.md**: Not the JSON or PNG files
- **No downstream re-parsing**: Design artifacts are consumed only by Technical Specifier

### Validation Checklist for Per-Screen Design Documentation

1. **Coverage**: Every effective screen from `figma_report.md` or `extracted_screenshots.md` has a dedicated spec.md section
2. **Components Complete**: Every interactive and significant display component is listed with type, variant, label, action
3. **Layout Documented**: Grid/flex structure, spacing, alignment are described
4. **States Covered**: All supported states (default, error, disabled, loading, etc.) are documented
5. **Interactive Actions Clear**: Each user action maps to a documented outcome or API call
6. **Visual References Correct**: PNG paths are valid and screenshots exist
7. **No JSON References**: Final spec.md contains no references to `json/screens/*.json`—all information is extracted and documented inline
8. **Design Tokens Used**: Colors, sizes, and styles reference project design tokens where applicable
9. **Traceability**: Each screen section links to relevant `SPEC-*` IDs and `FR-*` references
10. **No Ambiguity**: Component interactions, validations, and error states are explicit (no "as designed" or "TBD" placeholders)

