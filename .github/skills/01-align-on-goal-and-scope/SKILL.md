---
name: 01-align-on-goal-and-scope
description: Restates the project vision and objectives in plain words, with sources and stated measures, and prepares what the sponsor must confirm. Use when kickoff material arrives and before research is planned. Not for logging or ranking assumptions, use 02-surface-assumptions.
allowed-tools: Read Grep Glob Write
---

# 01. Align on goal and scope

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 01, CAP-01 Align on goal and scope |
| Phase or scope | Discover |
| Work nature mix | Mechanical 1; Judgment 2 (rows in the to-be breakdown). This skill has 3 Mechanical steps, 2 Judgment steps and 1 Relational step, because it splits the sponsor check and adds a guard step and a final write step |
| Authority level | Prepares. People collect the material and agree the reading. The skill drafts and prepares |
| Handoffs in | None. Inputs come from kickoff sessions and are people's material |
| Handoffs out | H01 |
| Human gate after | The sponsor confirms the reading. Approver role: project sponsor |
| Used by | None. A person leads this work, and an agent may prepare material. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Gets the sponsor, stakeholders and team to read the vision and objectives the same way before research starts. It enables the decision about what the research must help decide.

## 3. When to use

Use when kickoff and induction sessions have produced a vision, objectives or briefs, and before the assumptions are logged or the research is planned.

Not for: logging or ranking assumptions. Use 02-surface-assumptions. Not for writing research questions or aims, use 03-plan-the-research. Not for stating the problem to solve, use 08-frame-the-problem.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Notes from the kickoff and induction sessions with the sponsor, stakeholders and team | None. People | Required | Stop and ask |
| Draft vision and objectives and key results | None. People | Required | Stop and ask |
| Briefs and prior material | None. To verify where they are kept | Optional | Proceed and list under Gaps |
| Sponsor, for the confirmation | None. A person | Required for steps 5 and 6 | Stop and ask |
| Local config file: .github/templates/local-config.md (plain language rules, sensitivity rules, ID formats, approver roles) | None | Required | Stop and ask |
| Template: templates/vision-objectives-templates.md | None | Required | Stop and ask |

## 5. Method

Write in plain words. Cite the source of every statement. Keep organisation names and unit names out of every file, as the local config file requires.

1. **Mechanical.** Check the inputs. List the session notes, the draft vision and objectives, and the briefs, and mark any that is draft or missing. Note whether the vision and objectives were agreed before this work began or are being drafted alongside it.
2. **Judgment.** Collect the vision, objectives and any existing briefs. Options to produce: a list of candidate sources, each with what it says about the vision and the objectives, and any conflict between sources. Criteria: written by someone with authority, current, stated rather than implied. A person decides which sources count and collects what is missing. Never reconcile a conflict between sources. List it.
3. **Mechanical.** Restate the vision and objectives in plain words. For each statement, write the plain version beside the original wording and cite the source. List any measure the source states for an objective. Where none is stated, write To verify. Add no objective that no source states. Evidence tag: Inference. Save as alignment/vision-objectives-draft.md.
4. **Relational.** Prepare the sponsor playback. For each statement, prepare the question the sponsor must answer: is this what we mean, and what is missing. List the conflicts between sources and the objectives with no measure. Prepare the material for the conversation and do not hold it. People lead the session.
5. **Judgment.** Prepare the handling of the sponsor's changes. Options to produce: for each change the sponsor asks for, accept and update the wording, keep the wording and note the disagreement, or mark it open. Criteria: the sponsor stated it, it is consistent with the sources, it does not widen the scope without a decision. A person decides, and the sponsor confirms the final reading.
6. **Mechanical.** Write the agreed reading and the objectives list from the template, with the sponsor's confirmation, the signer role, the date, the evidence table, the Gaps and open questions section and a list of what was not checked. Set status draft until the sponsor confirms. Save as alignment/agreed-reading.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Draft restatement of the vision and objectives | None. Internal | Markdown table | alignment/ | vision-objectives-draft.md |
| Agreed reading of the vision and objectives, with measures where stated | H01 | Markdown with an evidence table | alignment/ | agreed-reading.md |

Every output follows the handoff standard, carries an evidence table and has status draft until the sponsor confirms.

## 7. Authority and gates

- May decide: how to word a plain restatement from a source, how to lay out the list, which questions to prepare.
- Must not decide: which sources count, what the objectives are, whether a conflict is resolved, the scope, or whether the reading is agreed. Must not add an objective. Must not hold the sponsor conversation.
- Escalate when: no vision or objectives exist, sources conflict, an objective has no measure, the sponsor and the stakeholders disagree, or the scope grows.
- Approver role: project sponsor. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: the file names the decision the research must support.
- [ ] Test 3, Traceable: every statement cites its source.
- [ ] Test 6, Owned and statused: the signer role, date and status are present.
- [ ] Test 7, Honest about gaps: conflicts, objectives with no measure and missing sources are listed.
- [ ] Test 8, Versioned and dated: version and date are present.
- [ ] No objective appears that no source states.
- [ ] No conflict was reconciled by the skill.
- [ ] The confirmation came from the sponsor.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| The vision and objectives are drafted alongside the research and never agreed | Breakdown gap note on R1: "Are the vision and OKRs agreed before research starts, or drafted alongside it? Who on the sponsor side confirms the reading?" | Step 1 notes which it is, and steps 5 and 6 record the sponsor's confirmation and the signer role |
| An objective that depends on what users need is not marked as such | Hypothesis from the to-be breakdown: the step that noted which objectives depend on what users need was removed | Not covered by this skill. To verify whether the step should return |
| Conflicting sources settled quietly | Existing rule in Ch 01 design-discovery: note contradictions and never reconcile them silently | Steps 2 and 4 list conflicts and never resolve them |
| Objectives with no measure | Hypothesis from how objectives are written | Step 3 writes To verify and step 4 prepares the question |
| The skill invents an objective | Roster design check | Step 3 adds no objective that no source states |

## 10. Principles applied

- Prioritise human control: people choose sources, hold the conversation and agree the reading.
- Speak the user's language: statements are written in plain words, beside the original wording.
- Build trust through visible evidence: every statement cites its source, and gaps are listed.

## 11. References

- NN/g "Discovery: Definition", read about 70 to 75 percent: a kickoff workshop aligns the team on the objective of the work and when it will be complete, and stakeholder interviews give insight into the business objectives.
- Ch 01 design-discovery SKILL.md, read in full (380 lines). Kept: the extraction of constraints, success criteria and scope signals from project documents, and the rule to note contradictions and never reconcile them silently. Dropped: the value framework, design brief and project paths. Conflict: it assumes a design brief as the output, which the breakdown does not have.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-01: R1, two steps. The as-is step "Note which objectives depend on what users need and which do not" has no row in the to-be.
- Standard practice, not checked against a source: the options and criteria in steps 2 and 5, and the format of objectives and key results.
- Supporting file: templates/vision-objectives-templates.md.
