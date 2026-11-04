---
name: 17-check-designs-against-principles-and-standards
description: Checks screens and components against the experience principles and the content, accessibility and system standards, with contrast by script and a breach list for a person to decide. Use when screens are ready for checking. Not for making or fixing screens.
allowed-tools: Read Grep Glob Write Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/contrast_ratio.py *)
---

# 17. Check designs against principles and standards

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 17, CAP-17 Check designs against principles and standards |
| Phase or scope | Design |
| Work nature mix | Mechanical 5; Judgment 2 (rows in the to-be breakdown, counting each as-is step). This skill has 7 Mechanical steps and 3 Judgment steps, because it splits grouped steps and adds a guard step and a final write step |
| Authority level | Checks. It reports. People decide every verdict and every breach |
| Handoffs in | None. Inputs come from other skills and are internal |
| Handoffs out | None. The check log is internal |
| Human gate after | A person verifies accessibility, decides each principle verdict and decides each breach. Approver role: design lead |
| Used by | AG-03 Experience agent. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Finds where screens and components break the principles and standards, with the evidence for each finding, before the design reaches users or developers. It enables the decision to accept, fix or escalate each breach.

## 3. When to use

Use when screens, components or a prototype are marked ready for checking, and before any design review or handover.

Not for: making or fixing screens. Use 12-design-the-detailed-screens. Not for setting the standards, use 16-define-the-design-language. A checker never checks its own work. Run this skill on work made by someone else, or have a person review the result. In the roster the same agent makes and checks, so a person reviews the result and verifies the accessibility items.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Screens and specifications: screens/ | None. Internal, from 12-design-the-detailed-screens | Required | Stop and ask |
| Experience principles and evidence links | None. Internal, from 15-structure-the-experience | Required | Stop and ask |
| Content standard, terminology, accessibility standard and foundations | None. Internal, from 16-define-the-design-language | Required | Stop and ask |
| Component library at the approved version | None. Internal | Required for step 5 | Stop at step 5 and ask |
| Colour pairs used, with kind (text, large text or ui): language/contrast-pairs.csv from 16-define-the-design-language, or pairs listed by the design team | None. Internal | Required for step 2 | Stop at step 2 and ask |
| Current versions: ia-and-dls-current-version.md | None | Required | Stop and ask |
| Local config file: local-config.md (accessibility level, check list, approver roles) | None | Required | Stop and ask |
| Templates: templates/check-templates.md | None | Required | Stop and ask |

## 5. Method

Report findings only. Never fix a screen or a component. Cite screen, component and principle IDs in every finding.

1. **Mechanical.** Check the inputs and the versions. Confirm the checks run on the versions named in ia-and-dls-current-version.md. Record who made the work and who is checking it. If the same executor made and checks the work, say so on the report and stop for a person to review.
2. **Mechanical.** Check colour contrast. Write each colour pair as one row in a CSV file with the columns id, foreground, background and kind. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/contrast_ratio.py --data <pairs file> --level <AA or AAA, from the accessibility standard>`. Paste the table. Mark each result as a calculation, never as an accessibility pass.
3. **Mechanical.** Check the evidence trace for each screen. List every screen with no story, job or pain point ID, no evidence ID or no principle ID.
4. **Mechanical.** Check content. Compare labels and messages with the terminology and the names never to use, and with the error and button label patterns in the content standard. List every mismatch with its screen and string.
5. **Mechanical.** Check consistency with the system. Read the design system reference record from 12-design-the-detailed-screens (screens/design-system-references.csv and reference-check.md). List every component used that is not in the library at the approved version, every local variant, every value fixed instead of drawn from a token, and every screen whose reference record is missing or stale.
6. **Mechanical.** Compare each screen with each experience principle. Write a table of screens by principles. For each pair, propose meets, breaks or ignores, citing the screen feature and the principle text. Save as checks/principle-comparison.md.
7. **Judgment.** Check each screen against the experience principles. Options to produce: for each pair in step 6, confirm the proposal or change it to meets, breaks, ignores or unclear, with the reason. Criteria: the verdict can be defended from the screen and the principle, and a principle that can say no is applied as written. A person decides.
8. **Judgment.** Verify accessibility. Options to produce: the list of accessibility checks from the accessibility standard, each with the screens and components it applies to and what to look at, such as focus, keyboard use, alt text and tab order. Criteria: the accessibility target and the checks set in the design language system. A person verifies and marks each pass. Nothing is recorded as passing before a person does.
9. **Judgment.** Decide which breaches to accept, fix or escalate. Options to produce: for each breach, the three choices with the consequence of each. Criteria: severity, how many screens it affects, whether a principle can block the design, effort. A person decides, and names who can block a design.
10. **Mechanical.** Log the fixes the person decided on, with the owner role, and write the check log with the evidence table, the Gaps and open questions section and a list of what was not checked. Set status draft. Save as checks/check-log.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Contrast results | None. Internal | Markdown table | checks/ | contrast-results.md |
| Evidence trace, content and consistency findings | None. Internal | Markdown tables | checks/ | trace-content-consistency.md |
| Principle comparison and verdicts | None. Internal | Markdown table | checks/ | principle-comparison.md |
| Accessibility verification record | None. Internal | Markdown table | checks/ | accessibility-verification.md |
| Check log: breaches, decisions and fixes | None. Internal. Read by design review and 13-package-for-handoff | Markdown table | checks/ | check-log.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to lay out findings, which strings to compare, how to run the scripts.
- Must not decide: any verdict, an accessibility pass, a breach decision, a fix, or whether a principle can block a design. Must not fix a screen. Must not check its own work.
- Escalate when: the executor made the work, versions differ from the approved ones, a principle has no way to say no, a contrast failure affects a foundation, or a person cannot be reached to verify accessibility.
- Approver role: design lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: versions and files named.
- [ ] Test 3, Traceable: every finding names a screen or component ID and a principle or standard ID.
- [ ] Test 6, Owned and statused: approver role, decider roles and status are present.
- [ ] Test 7, Honest about gaps: checks that could not run and items not verified are listed.
- [ ] Test 8, Versioned and dated: the versions checked are named.
- [ ] Contrast came from the script, and each result is labelled a calculation.
- [ ] No accessibility item is marked as passing before a person verified it.
- [ ] No screen or component was changed by this skill.
- [ ] The maker and the checker are named, and they differ or a person reviewed.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| The check is left to the stakeholder review, and nobody holds the checklist | Breakdown gap note on H5: "Does this check happen, or is it left to the stakeholder review in step 8? Who holds the checklist?" | The skill runs before any review and the checklist is in the accessibility standard and the templates |
| Principles used only for filing, with no power to block | Breakdown gap note on G2: "Can a principle block a design, and who decides?" | Step 9 records who can block a design |
| No written way to check accessibility | Breakdown gap note on D4: "How are content, standards and accessibility checked, by whom and at which step? Is an accessibility target written down?" | Steps 2 and 8 and the standard from 16-define-the-design-language |
| A false accessibility pass | Roster entry for AG-03 and the roster design check | A script reports a calculation only, and a person verifies |
| The maker checks its own work | Roster design check | Step 1 records both and stops when they match |
| Arithmetic errors in contrast | Hypothesis from how contrast is computed | The ratio comes from a script |

## 10. Principles applied

- Prioritise human control: people decide every verdict and breach, and accessibility passes only after a person verifies.
- Prevent errors: contrast is computed by a tested script, and the skill reports and never edits.
- Build trust through visible evidence: every finding names the screen, the principle or standard and the version checked.

## 11. References

- design-validation SKILL.md, read in full (293 lines). Kept: the post-build review checklist areas (hierarchy, interaction, consistency, content, accessibility, completeness), the honest evaluation rule and the routing of findings to the owning skill. Dropped: the heuristic evaluation, test plan and scenario scripts. Conflict: it checks values against Figma tokens, which the breakdown does not name.
- design-accessibility SKILL.md, read in full (218 lines). Kept: the contrast audit tables, the contrast thresholds of 4.5 to 1 for text and 3 to 1 for large text and interface elements, and colour never as the only signal. Dropped: the aria, keyboard and screen reader specification steps, which have no breakdown rows. To verify who owns them.
- NN/g "Design-System Maturity", read about 70 percent: parity between design and code and baked-in accessibility practices.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-17: D2 (contrast), H5 and G2, which is new in the to-be.
- Standard practice, not checked against a source: the WCAG relative luminance formula and the AA and AAA thresholds used in contrast_ratio.py.
- Supporting files: templates/check-templates.md, scripts/contrast_ratio.py.
