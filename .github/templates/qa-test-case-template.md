# Test Case Template

<!--
  USAGE: One file per test case. Filename: TC-XXX-<slug-title>.md
  Replace every <PLACEHOLDER> with real data. Do not leave unresolved placeholders.
  Section order is mandatory — do not add, remove, or reorder sections.
  Source: AC = Acceptance Criteria | BL = Business Logic | EH = Exception/Error Handling | GEN = Other story detail
  TEMPLATE SOURCE: PROJECT DEFAULT.
  SAMPLE SETUP: COMPLETE. The project-default template is in use.
-->

## Test Case: <TC-ID>

**User Story:** <STORY-KEY> - <STORY-SUMMARY>
**Priority:** <PRIORITY> | **Type:** Functional | **Source:** <AC | BL | EH | GEN> | **Component:** <COMPONENT>

---

## Objective

<One sentence: "Verify that [actor] [action] [expected outcome].">

---

## Prerequisites

- The application or service under test is available in the required test environment.
- <BACKEND-API-PRECONDITION, when applicable>
- <ACCOUNT-OR-SYSTEM-STATE-PRECONDITION>
- <ANY-ADDITIONAL-PRECONDITION>

---

## Test Data

| Field | Value |
|-------|-------|
| <FIELD-1> | <VALUE-1> |
| <FIELD-2> | <VALUE-2> |
| <API RESPONSE OR OTHER EXPECTED VALUE, WHEN APPLICABLE> | <VALUE> |

---

## Test Steps

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | <ACTION-1> | <EXPECTED-1> |
| 2 | <ACTION-2> | <EXPECTED-2> |
| 3 | <ACTION-3> | <EXPECTED-3> |

---

## Expected Results

1. <VERIFIABLE-ASSERTION-1>
2. <VERIFIABLE-ASSERTION-2>
3. <VERIFIABLE-ASSERTION-3>

---

## Business Logic Rules Covered

<!-- List every BL rule exercised by this test case. Write "N/A" if none. -->

| BL Rule # | Rule Description |
|-----------|-----------------|
| <BL-N> | <RULE-TEXT-EXACTLY-AS-IN-STORY> |

---

## Acceptance Criteria Covered

<!-- List every AC ID exercised by this test case. Write "N/A" if none. -->

| AC ID | Title |
|-------|-------|
| <AC-ID> | <AC-TITLE> |

---

## Pass / Fail Criteria

- **PASS:** <Single condition that confirms the objective is satisfied with no unexpected behaviour>
- **FAIL:** <Rule not enforced / AC Then clause not met / wrong error message / wrong navigation / app crash>

---

## Related Artefacts

- User Story: [<STORY-KEY>](<STORY-JIRA-URL>)
- Relevant implementation or test files: `<RELATIVE-FILE-PATHS, OR "Not found in codebase">`
- Other relevant artefacts, such as screens, services, routes, or API contracts: `<REFERENCES, WHEN APPLICABLE>`
