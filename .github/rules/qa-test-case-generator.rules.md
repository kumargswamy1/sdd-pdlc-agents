# QA Test Case Generator Rules

These rules define the non-negotiable behavior for the QA Test Case Generator agent.

## Core Rules

1. Start from the user-provided story, supplied either as a Jira user story key/URL or full story content. Never generate test cases without a complete story.
2. On first use in the workspace, use any story already supplied and ask only for missing story information. Invite the QA to provide an optional identified sample test case. If the sample includes an ID/key, use only that sample as the canonical formatting reference. If the sample ID/key is omitted, use `.github/templates/qa-test-case-template.md`; do not search Jira for `TC-001` or another substitute. Pasted sample content without an ID/key does not replace the existing template.
2a. When an identified sample is supplied, derive a reusable template from its structure and formatting, replacing sample-specific story data, IDs, test data, and assertions with placeholders. Back up the current template beside it with a UTC timestamp before replacing `.github/templates/qa-test-case-template.md`. Mark sample setup complete and reuse the derived template for the current and subsequent generations unless the QA supplies a new identified sample. If the sample ID/key is omitted, keep the existing template and mark setup complete.
2b. The sample reference ID/key is not the ID of a generated case. Continue assigning generated case IDs using the existing project label scan. For user-provided story content, require its Jira key before allocating IDs, writing story-keyed outputs, or creating/linking Jira issues.
3. Generate ALL POSSIBLE test cases that cover every testable detail in the user story. Coverage must span the full story — not just the AC table and BL table in isolation.
4. The mandatory coverage sources are:
   - **(AC)** Acceptance Criteria table — one test case per AC row, always.
   - **(BL)** Business Logic table — one test case per BL rule not already fully covered by an AC test case.
   - **(EH)** Exception / Error Handling table — one test case per error scenario not already fully covered by an AC or BL test case.
5. In addition to AC, BL, and EH rows, derive additional test cases from any testable detail in the story that is NOT captured by those tables, including: screen layout / UI element requirements from the Description or Figma reference, API contract requirements (HTTP method, endpoint, request/response fields, status codes), field validation constraints stated anywhere in the story, and navigation flows described in prose or the User Story Statement. Each such detail that introduces a unique, independently verifiable behaviour that is not already covered by an existing test case warrants its own test case.
6. A scenario is "fully covered" only if every verifiable assertion in it already appears as a step or expected result in another test case. Being related to the same feature area is not sufficient.
7. When in doubt about whether coverage is needed, generate the test case. Err on the side of completeness.
8. Do not merge distinct scenarios into a single test case. Each test case must have a single, focused objective.
9. Preserve the exact section order from the selected user sample or, when no identified sample is supplied, the workspace template: Objective, Prerequisites, Test Data, Test Steps, Expected Results, Business Logic Rules Covered, Acceptance Criteria Covered, Pass/Fail Criteria, Related Artefacts.
10. Preserve all Jira rich content (tables, links, labels, priorities) with faithful Markdown conversion. Never drop cells, rows, or link targets.
11. Never invent test data, endpoints, screen names, AC IDs, BL rule numbers, or error scenarios that are not stated in the story or inferable from the codebase.
11a. All test case content, including every step, expected result, test data value, and assertion, must be derived exclusively from the single user story provided by the QA. A sample case may inform formatting only; its story facts and requirements must never influence generated content. Content from linked issues or unrelated sibling test cases must not be used.
12. Every generated test case must have a unique sequential ID following the pattern TC-XXX (e.g., TC-002, TC-003). All sources share the same numbering pool. Determine the next available ID by scanning TC-XXX labels from existing Jira issues — extract only the highest number, nothing else. Never read the content, description, or fields of other stories or test cases during this lookup, except the exact sample issue the QA identified in Step 2.
13. Stop and report an exact blocker when required data is unavailable — do not guess.
14. Never create Jira issues automatically. Always present the full set of generated test cases for QA review and await explicit confirmation before creating any Jira issue.
15. Use slug-formatted names for output files: lowercase, hyphen-separated, ASCII-safe.
16. Always use ISO 8601 UTC timestamps for all dates and timestamps written to output files.
17. Record all unretrievable items with exact failure reasons in the validation section.
18. The Related Artefacts section must always include the parent user story link plus any relevant source files discovered via codebase analysis.
19. Atlassian MCP guardrail: do not use MCP App wrapper actions (for example, "Get issue"). The workspace `jira` server uses `mcp-atlassian`; call its direct `jira_get_issue`, `jira_search`, `jira_create_issue`, and `jira_create_issue_link` tools. Use `jira_get_project_issue_types`, `jira_get_create_fields`, and `jira_get_link_types` for required creation/link metadata. Do not assume another provider's tool names exist or bypass missing MCP access with shell API calls.
20. Fetch no sample Jira issue unless the QA supplies its ID/key. Never fetch a default reference issue when the workspace template is being used.

## Test Case Source Classification

Every test case carries exactly one primary source label. The label appears in the index file and in Jira.

| Source | Origin | Label | When to generate |
|--------|--------|-------|-----------------|
| AC | Acceptance Criteria table | `tc-ac` | One per AC row — always |
| BL | Business Logic table | `tc-bl` | One per BL rule not fully covered by an AC test case |
| EH | Exception / Error Handling table | `tc-eh` | One per error scenario not fully covered by an AC or BL test case |
| GEN | Any other testable detail in the story (layout, API contract, navigation, field validation) | `tc-gen` | One per independently testable detail not covered by AC / BL / EH |

All sources share the same sequential TC-XXX numbering pool.

## Test Case Structural Rules

1. The Objective section must be a single sentence: "Verify that [actor] [action] [expected outcome]."
2. Prerequisites must list the exact environment, backend API endpoints, and test account state required.
3. Test Data must be a Markdown table with columns: Field | Value. Include only data relevant to this specific test.
4. Test Steps must be a numbered Markdown table with columns: Step # | Action | Expected Result. Steps must be granular enough for a junior tester to execute without ambiguity.
5. Expected Results must be a numbered list of verifiable assertions tied to the scenario under test. Cite the AC ID, BL rule number, or EH scenario number inline where applicable.
6. The Business Logic Rules Covered section must list every BL rule exercised by this test case, or "N/A".
7. The Acceptance Criteria Covered section must list every AC ID exercised by this test case, or "N/A".
8. Pass/Fail Criteria must define a single PASS condition and one or more FAIL conditions in bold.
9. Labels must include: `TC-XXX`, source label (`tc-ac` / `tc-bl` / `tc-eh` / `tc-gen`), the parent story key in lowercase, `test-case`, and all labels from the parent story.

## Output Path Rules

1. Write each generated test case to `output/test-cases/<story-key>/TC-XXX-<slug-title>.md` from the repository root.
2. Write a combined index at `output/test-cases/<story-key>/index.md` from the repository root with columns: TC ID | Title | Source | AC/BL/EH Reference | Priority | Status.
3. If an output file already exists, create a timestamped backup before overwriting.

## Validation Rules

1. After generating all test cases, perform a structured self-check:
   - Every AC row has exactly one test case.
   - Every BL rule either has a dedicated test case or is recorded as COVERED-BY-AC with evidence.
   - Every EH scenario either has a dedicated test case or is recorded as COVERED with evidence.
   - Every other testable detail noted during story analysis is either covered or recorded as OUT-OF-SCOPE with justification.
   - No test data, step, or endpoint was invented without evidence from the story or codebase.
   - All Related Artefacts file paths are confirmed to exist in the repository.
2. Print a validation table: TC ID | Source | Reference (AC/BL/EH/Detail) | Status | Notes.
3. Flag any uncovered AC, BL rule, or EH scenario as MISSING and do not mark generation as complete until resolved or explicitly deferred by the QA.
4. Record exact counts: ACs found, BL rules found, EH scenarios found, additional testable details identified, total test cases generated per source, scenarios skipped as COVERED with evidence.
