# QA Test Case Generator Instructions

This file defines the step-by-step workflow for the QA Test Case Generator agent.

## Step 1 - Initialize Inputs and Resolve the Template

1. Check the `TEMPLATE SOURCE` and `SAMPLE SETUP` markers in the template. When setup is `PENDING`, use any story and sample details already supplied, and ask only for missing story information. Invite the QA to provide an optional sample test-case ID/key. The story may be a Jira issue key/URL or full story content. The sample body may be provided with its ID/key.
2. If the sample has a test-case ID/key, use only that supplied sample as the template reference. If the user supplied its full content, use that content directly. If the user supplied only an identifier, fetch only that issue; for a `TC-###` label, resolve it within the story's project and stop if it is missing or ambiguous.
3. If no sample ID/key is provided, use the existing template content. Do not search Jira for a substitute sample, even if sample content without an ID/key was pasted.
4. If an identified sample is selected, derive a reusable template from its structure and formatting. Preserve section names, order, tables, and relevant instructions, but replace sample-specific IDs, story details, test data, values, and assertions with clear placeholders. Do not copy sample-specific facts into generated cases.
5. Before replacing the workspace template with a derived template, create a timestamped UTC backup beside it using the name `qa-test-case-template.<YYYYMMDDTHHmmssZ>.md`. Add or update the template-source marker in its usage comment to record whether it is the project default or a user sample.
6. Replace `.github/templates/qa-test-case-template.md` with the derived reusable template and use that same file for the current generation and all later runs. If no sample ID/key was provided, keep the current template content, change its `SAMPLE SETUP` marker to `COMPLETE`, and proceed. Do not ask for another sample on subsequent runs unless the QA explicitly supplies a new identified sample.
7. A sample test-case ID/key is for identifying the template reference only. It is not the ID of any newly generated case. If no sample ID/key is given, the current template remains in effect; generated case IDs are still assigned by Step 6.

## Step 2 - Accept and Validate the User Story

1. Accept one user story as either a Jira issue key/URL or full story content. Prefer the user-provided story content as the source when supplied; do not fetch additional story content in that case.
2. For a Jira key or URL, normalize the key to uppercase `PROJECT-NNNN` and validate it against `^[A-Z][A-Z0-9]+-[0-9]+$`. If invalid, explain the required format and stop.
3. For a Jira story, fetch only that issue using the direct `jira_get_issue` tool with `fields="*all"` and confirm it is a Story. If it is not a Story, warn the QA and ask for confirmation before continuing.
4. For pasted story content, extract its story key, summary, priority, labels, and all relevant requirements. If the story key is missing, ask for it before assigning Jira test-case IDs, writing story-keyed output files, or creating/linking Jira issues.
5. Preserve the story's complete content. Do not fetch linked issues; record linked issue keys as reference text only.
6. Convert Jira rich content (ADF/wiki markup) to clean Markdown when fetching the issue. Do not summarize or truncate the story.

## Template Reference (Resolved in Step 1)

1. If the QA supplied an identified sample case by Jira issue key or TC label, use that one case as the reference. Do not fetch `TC-001` unless that is the identifier the QA supplied.
2. If no sample ID/key was provided, the project template resolved in Step 1 is the reference; do not perform a `TC-001` lookup.
3. Extract the selected sample's structure and use it for section order, formatting, step granularity, and depth. Keep sample content separate from story-derived requirements.

## Step 3 - Extract Story Requirements

1. From the single story accepted in Step 2, extract every field without omission: summary, description (including User Story Statement and screen layout details), priority, labels, status, components, Figma reference links, API table, Business Logic table, Exception / Error Handling table, and Acceptance Criteria table.
2. Do not fetch or read linked issues. Record linked issue keys as reference text only in Related Artefacts.
3. Do not summarize or truncate any extracted content.

### 3a - Extract Acceptance Criteria

1. Extract the complete Acceptance Criteria table — every row with its AC ID, Title, Given, When, and Then columns.
2. If the story has no Acceptance Criteria table, stop and inform the QA; suggest adding ACs to the story before continuing.
3. Record the exact count of AC rows found.

### 3b - Extract Business Logic Rules

1. Extract the complete Business Logic table — every row with its Rule # and full Rule description exactly as written.
2. If no Business Logic table is present, record "Business Logic table: not present" and continue.
3. Record the exact count of BL rules found.

### 3c - Extract Exception / Error Handling Scenarios

1. Extract the complete Exception / Error Handling table — every row with its scenario number (#), Scenario description, and Expected Behaviour exactly as written.
2. If no Exception / Error Handling table is present, record "Exception / Error Handling table: not present" and continue.
3. Record the exact count of EH scenarios found.

### 3d - Identify Additional Testable Details

1. Read the full story description, User Story Statement, screen layout section, API table, and any Figma reference notes. Identify every independently testable detail that is NOT already captured as a row in the AC, BL, or EH tables. Examples:
    - A specific UI element or layout requirement named in the Description (e.g., "eye icon toggles password visibility")
    - An API or integration contract detail not covered by any AC (e.g., a token stored under a specified key in secure storage)
    - A navigation or workflow transition described only in prose (e.g., replace the current view instead of adding a new history entry)
    - A field validation constraint stated in the Description but not in the BL table
2. Record each such detail with a short label (DETAIL-N) and a one-line description.
3. Record the exact count of additional testable details found.

## Step 4 - Build the Full Coverage Map

Before generating any test case, build a single coverage map for all sources:

1. For each BL rule: determine whether all of its assertions are already exercised by a planned AC test case.
   - Status: `NEEDS-TC` or `COVERED-BY-AC` (with AC ID as evidence).
2. For each EH scenario: determine whether all of its assertions are already exercised by a planned AC or BL test case.
   - Status: `NEEDS-TC` or `COVERED` (with TC reference as evidence).
3. For each additional testable detail (DETAIL-N): determine whether it is fully covered by any planned test case.
   - Status: `NEEDS-TC` or `COVERED` (with TC reference as evidence).
4. When in doubt, set status to `NEEDS-TC`. Err on the side of completeness.
5. Log the coverage map as a table before generating any test case:
   `Source | Ref # | Summary | Status | Covered By`

## Step 5 - Analyze the Codebase for Related Artefacts

1. Search the repository for source files relevant to the story's feature area (screen/widget file, service file, backend route file).
2. Use the story's API endpoints, screen names, widget names, and service names as search terms.
3. Collect exact file paths. These will be cited in the Related Artefacts section of every test case.
4. If no matching files are found, note "Not found in codebase" and continue.

## Step 6 - Determine the Next Available Test Case ID

1. Search Jira with the direct `jira_search` tool for existing test cases in the project using JQL:
   `labels = "test-case" AND project = <project-key> ORDER BY created ASC`
   Request `fields="labels"` only — no descriptions or other issue content. For Server/Data Center paginate with `start_at` and `limit`; for Cloud follow the returned `page_token` when provided. Continue until all results are scanned; do not infer the highest ID from the first page.
2. From the returned labels arrays, extract all values matching the pattern `TC-\d+`. Identify the highest number found.
3. The next available ID is that highest number plus one (e.g., highest found is TC-001 → next is TC-002).
4. Assign sequential IDs across all sources (AC, BL, EH, GEN) as a single shared pool before writing any output.
5. **Do not read, open, or process the content of any existing test-case issue except the exact sample issue the QA supplied as the template reference.** This step is otherwise a label scan only. All test case content is derived solely from the story provided in Step 2.

## Step 7 - Generate AC-Sourced Test Cases (One per AC row)

For each Acceptance Criterion row extracted in Step 3a:

1. Create one test case using the template at `.github/templates/qa-test-case-template.md` exactly.
2. Assign the next sequential TC-XXX ID.
3. **Objective**: "Verify that [actor] [action per AC title] [outcome from AC Then clause]."
4. **Prerequisites**: Required application or service environment available; backend API from the story's API table when applicable; account or system state from the AC's Given clause; any additional preconditions from BL or EH that apply.
5. **Test Data**: Fields and values relevant to this AC from the story's BL, EH, or Description (e.g., exact email, password, MFA flag, HTTP status, response fields).
6. **Test Steps**: Derive steps from the AC's Given → When → Then flow. Reference exact UI element names from the story's Description or Figma notes. Each step must have an Action and an Expected Result.
7. **Expected Results**: One assertion per verifiable outcome. Cite BL rule numbers inline where a BL rule directly governs the Then clause (e.g., "Per BL-6: Login button is disabled during the API call").
8. **Business Logic Rules Covered**: List every BL rule whose assertions are fully exercised by this test case, or "N/A".
9. **Acceptance Criteria Covered**: The AC ID and Title this test case derives from.
10. **Pass/Fail Criteria**: PASS = the Then clause is satisfied with no errors; FAIL = any deviation, unexpected error, wrong navigation, or crash.
11. **Related Artefacts**: Parent story link + file paths from Step 5.
12. **Labels**: `["TC-XXX", "tc-ac", "<story-key-lowercase>", "test-case"] + all story labels`.

## Step 8 - Generate BL-Sourced Test Cases (One per BL rule with status NEEDS-TC)

For each BL rule with status `NEEDS-TC` in the coverage map:

1. Create one test case using the template exactly.
2. Assign the next sequential TC-XXX ID.
3. **Objective**: "Verify that [the system] enforces [the BL rule description exactly as stated in the story]."
4. **Prerequisites**: Required application or service environment available; backend API from the story's API table when applicable; minimum account or system state required to observe this BL rule.
5. **Test Data**: Data that directly targets the boundary or condition the BL rule defines. For min-length or format rules: include a value below the threshold AND a value at/above the threshold.
6. **Test Steps**: Steps that navigate directly to the rule's trigger point. Include the full prerequisite flow only to the extent needed to reach the trigger.
7. **Expected Results**: Assertions that confirm the rule is enforced exactly as written — no paraphrase.
8. **Business Logic Rules Covered**: The BL rule number(s) and their exact text.
9. **Acceptance Criteria Covered**: Any AC that references this BL rule, or "N/A".
10. **Pass/Fail Criteria**: PASS = system behavior matches the BL rule exactly; FAIL = rule not enforced, wrong boundary, unexpected message, or crash.
11. **Related Artefacts**: Parent story link + file paths from Step 5.
12. **Labels**: `["TC-XXX", "tc-bl", "<story-key-lowercase>", "test-case"] + all story labels`.

## Step 9 - Generate EH-Sourced Test Cases (One per EH scenario with status NEEDS-TC)

For each EH scenario with status `NEEDS-TC` in the coverage map:

1. Create one test case using the template exactly.
2. Assign the next sequential TC-XXX ID.
3. **Objective**: "Verify that [the system] handles [the EH scenario description] with [Expected Behaviour from the story]."
4. **Prerequisites**: Required application or service environment and backend API available when applicable; system state required to trigger this specific error scenario.
5. **Test Data**: Input values or conditions that cause the error (e.g., empty field, too-short value, incorrect credentials, network offline). Include both the invalid input and any valid baseline fields required to complete the form.
6. **Test Steps**: Steps that reproduce the exact error condition described in the EH row.
7. **Expected Results**: Assertions that confirm the Expected Behaviour from the EH row is displayed exactly as stated — inline validation message wording, button state, form state.
8. **Business Logic Rules Covered**: Any BL rule that governs this error condition, or "N/A".
9. **Acceptance Criteria Covered**: Any AC that references this EH scenario, or "N/A".
10. **Pass/Fail Criteria**: PASS = the system responds with the exact Expected Behaviour from the EH table; FAIL = no error shown, wrong message, form submits anyway, or crash.
11. **Related Artefacts**: Parent story link + file paths from Step 5.
12. **Labels**: `["TC-XXX", "tc-eh", "<story-key-lowercase>", "test-case"] + all story labels`.

## Step 10 - Generate GEN Test Cases (One per additional testable detail with status NEEDS-TC)

For each additional testable detail (DETAIL-N) with status `NEEDS-TC` in the coverage map:

1. Create one test case using the template exactly.
2. Assign the next sequential TC-XXX ID.
3. **Objective**: "Verify that [the detail's testable behaviour — e.g., the specific UI element, API contract detail, or navigation behaviour]."
4. **Prerequisites**: Required application or service environment available; any specific system state required to observe this detail.
5. **Test Data**: Only the data directly relevant to verifying this detail.
6. **Test Steps**: Minimal steps needed to reach and verify the specific detail. Do not include full flows unless required.
7. **Expected Results**: Assertion(s) that confirm the detail behaves exactly as stated in the story.
8. **Business Logic Rules Covered**: Any BL rule that governs this detail, or "N/A".
9. **Acceptance Criteria Covered**: Any AC that references this detail, or "N/A".
10. **Pass/Fail Criteria**: PASS = detail behaves exactly as stated in the story; FAIL = detail missing, incorrect, or not matching story description.
11. **Related Artefacts**: Parent story link + file paths from Step 5.
12. **Labels**: `["TC-XXX", "tc-gen", "<story-key-lowercase>", "test-case"] + all story labels`.

## Step 11 - Write Output Files

1. Write each test case as a Markdown file at `output/test-cases/<story-key>/TC-XXX-<slug-title>.md` from the repository root.
   - Slug title = test case title lowercased, spaces replaced with hyphens, ASCII-only.
2. Write the index file at `output/test-cases/<story-key>/index.md` from the repository root with a Markdown table:
   `TC ID | Title | Source | AC/BL/EH/Detail Reference | Priority | Status`
3. Re-read each written file and confirm its section order matches the template.
4. If a file already exists, create a timestamped backup before overwriting.

## Step 12 - Validation and Review Summary

1. Run the structured self-check from the Validation Rules in `qa-test-case-generator.rules.md`.
2. Print the validation table: TC ID | Source | Reference | Status | Notes.
3. Present the full list of generated test cases to the QA, grouped by source: AC first, then BL, then EH, then GEN.
4. State exact counts: ACs found, BL rules found, EH scenarios found, additional details identified, test cases generated per source, scenarios skipped as COVERED.
5. Flag any MISSING items and ask the QA whether to defer them or generate the missing test cases before proceeding.
6. Ask the QA for explicit written confirmation before creating Jira issues.

## Step 13 - Create Jira Issues (Only After QA Approval)

1. Wait for explicit written approval from the QA.
   Use `jira_get_project_issue_types` and `jira_get_create_fields` to confirm the Task type and required fields in the parent project. Use `jira_get_link_types` to confirm the Tests link type and direction; do not invent a link type or silently substitute another relationship. Report missing required metadata as a blocker.
2. For each approved test case, create a Jira Task in the same project as the parent story:
   Use the direct `jira_create_issue` tool; use `jira_create_issue_link` only after successful creation and with the confirmed link type/direction.
   - **Summary**: `<TC-XXX> - <test case title>`
   - **Description**: Full test case body in Jira wiki-markup format (Markdown tables → `||header||` / `|cell|` syntax).
   - **Issue type**: Task
   - **Priority**: Matching the parent story priority
   - **Labels**: As defined in Steps 7–10 (item 12 in each step)
   - **Link**: Add a "Tests" link from the new issue to the parent story
3. Report the new Jira issue key after each successful creation.
4. If Jira creation fails for any issue, report the exact error and continue with the remaining issues.
