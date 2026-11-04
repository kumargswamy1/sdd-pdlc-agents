---
name: 14-share-and-align-with-stakeholders
description: Turns ranked findings into backlog items and prepares the decisions and design brief for people to take to stakeholders. Use when results are analysed and a person must decide what to fix, hand over or accept. Not for scoring results, use 19-analyse-test-results.
allowed-tools: Read Grep Glob Write
---

# 14. Share and align with stakeholders

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 14, CAP-14 Share and align with stakeholders |
| Phase or scope | Cross cutting. Covered today by the usability loop back only |
| Work nature mix | Mechanical 1; Judgment 2 (rows in the to-be breakdown). This skill has 2 Mechanical steps and 2 Judgment steps, because it adds a final write step and a findings report |
| Authority level | Prepares. It writes the backlog and the options. People decide and hold the conversations |
| Handoffs in | None. Inputs are outputs of 19-analyse-test-results and are internal |
| Handoffs out | H22, H24 |
| Human gate after | A person decides each issue and briefs design. Approver role: product owner |
| Used by | AG-04 Handoff keeper. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Gets analysed results in front of the people who must act, in a form they can decide on: a single backlog, a recommended next action for each issue, and a brief for the people who change the design. It enables the decision to fix now, hand over or accept.

## 3. When to use

Use when test results are analysed and ranked, and a person must decide what happens to each finding.

Not for: scoring or ranking results. Use 19-analyse-test-results. Not for packaging approved work for the next stage, use 13-package-for-handoff. Steps 8 and 10 of the main process are not broken down, so this skill covers the usability loop back only. To verify whether more is wanted.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Ranked findings: analysis/ranked-findings.md | None. Internal, from 19-analyse-test-results | Required | Stop and ask |
| Usability findings with severity: analysis/usability-findings.md | None. Internal | Required | Stop and ask |
| Pass criteria comparison: analysis/pass-criteria-comparison.md | None. Internal | Required for step 2 | Stop at step 2 and ask |
| Usability benchmark: analysis/usability-benchmark.md | None. Internal | Optional | Proceed and list under Gaps |
| Delivery constraints | None. To verify where they are recorded | Optional | Proceed and mark To verify |
| Local config file: .github/templates/local-config.md (ID formats, approver roles, where rework may go) | None | Required | Stop and ask |
| Templates: templates/backlog-and-decisions-templates.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Write each ranked finding as a backlog item with its evidence link. Give each item a generated ID, its type (fix, wishlist or defer), the finding ID, severity, rank and the evidence item IDs. Keep fixes, wishlist ideas and deferred items in one backlog with a type column, because the wishlist goes into the backlog. Leave status and owner blank. Save as backlog/backlog.md.
2. **Judgment.** Propose the next action for each issue. Options to produce: fix now, hand to the product team, or accept, each with its consequence. Criteria: severity, whether the pass criteria were met (from the comparison file), reach and effort from the ranked findings, how strong the evidence is. A person decides. Record the decision, the deciding role and the date. Save in analysis/loop-back-decisions.md.
3. **Judgment.** Prepare the brief on what to change. Options to produce: for each issue to fix now, where the rework goes. The two places the team has named are the prototype used for the next usability sessions, and the design file that goes to development. Criteria: severity, whether another test round is planned, whether the change has been reviewed. Flag one open question for the person: rework made directly in the design file for development may skip the formal design review. A person briefs design. Prepare the material and do not hold the conversation. Save as analysis/design-brief-for-rework.md.
4. **Mechanical.** Assemble the findings report: ranked findings, benchmark, pass criteria comparison and the decisions. Write the evidence table, the Gaps and open questions section and a list of what was not checked. Set status draft. Save as reports/usability-findings-report.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Backlog with fixes, wishlist and deferred items | H24 | Markdown table | backlog/ | backlog.md |
| Decision per issue | H22, H24 | Markdown table | analysis/ | loop-back-decisions.md |
| Design brief for rework | H22 | Markdown | analysis/ | design-brief-for-rework.md |
| Findings report for the product team and detailed design | H22, H24 | Markdown | reports/ | usability-findings-report.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to lay out the backlog, how to word an item, the order of items within a rank.
- Must not decide: the type of a finding, the next action for an issue, where rework goes, whether a review is needed, or priority. Must not brief design in place of a person.
- Escalate when: an issue has no evidence link, the pass criteria comparison is missing, rework would go straight into the development design file with no review, or the product team is not identified.
- Approver role: product owner. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: every issue shows the decision a person must make.
- [ ] Test 3, Traceable: every backlog item links to a finding ID and evidence item IDs.
- [ ] Test 4, Single source: one backlog. Findings are cited by ID and not copied.
- [ ] Test 6, Owned and statused: approver role and status are present.
- [ ] Test 7, Honest about gaps: open questions, including the review question, are listed.
- [ ] Wishlist, fixes and deferred items sit in one list with a type column.
- [ ] No decision, rank or type was set by the skill. Those columns come from people or from 19-analyse-test-results.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Nobody owns priority, and the wishlist is kept apart from fixes | Breakdown gap note on U6: "Who sets priority? Does the wishlist stay apart from the fix list?" | Step 1 keeps one list with a type column. Team answer, 2026-10-12: the wishlist goes into the backlog |
| No defined loop back when results fall short | Breakdown gap note on U7: "Is there a defined loop back when results fall short? Who decides ship or fix, and does rework return to step 7 or step 8?" | Steps 2 and 3 record who decided and where rework goes. Team answer, 2026-10-12: rework may go into the prototype for later sessions or straight into the design file for development |
| Rework skips the design review | Hypothesis from that team answer | Step 3 flags it as an open question for a person |
| The brief replaces the conversation | Hypothesis from the roster design check | Step 3 prepares material and never briefs |
| Product team not known | Team answer, 2026-10-12: the product team is the wider working team and may or may not include a designer | Escalated when it cannot be identified |

## 10. Principles applied

- Prioritise human control: people decide every issue, and the skill proposes only.
- Build trust through visible evidence: each backlog item links to its finding and evidence.
- Start simple: one backlog, one decision file and one brief.

## 11. References

- design-validation SKILL.md, read in full (293 lines). Its handoff triggers table routes each finding to the upstream skill and says to update the upstream artifact first. Kept: routing findings to a named receiver with evidence. Conflict: the team answer lets rework go straight into the prototype or the development design file, while this existing rule and the canvas brief rule in design-wireframe say to change the upstream artifact first. To verify which rule wins.
- design-wireframe SKILL.md, Steps 5 and 6 read: structured feedback capture, and changes made to the source artifact first. The wireframe specifics are not carried.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-14: U6 (step 3) and U7 (steps 2 and 3).
- Standard practice, not checked against a source: the criteria in steps 2 and 3.
- Supporting file: templates/backlog-and-decisions-templates.md.
