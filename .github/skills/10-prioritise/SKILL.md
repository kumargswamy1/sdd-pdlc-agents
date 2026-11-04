---
name: 10-prioritise
description: Prepares the options for deciding which jobs matter most and which features go forward, change or drop, with the criteria written down first. Use when the jobs matrix or concept test results are ready for a decision. Not for scoring test results, use 19-analyse-test-results.
allowed-tools: Read Grep Glob Write
---

# 10. Prioritise

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 10, CAP-10 Prioritise |
| Phase or scope | Define |
| Work nature mix | Mechanical 0; Judgment 3 (rows in the to-be breakdown, all human gates). This skill has 2 Mechanical steps and 3 Judgment steps, because it adds a guard step and a final write step |
| Authority level | Prepares. It lays out options and criteria. People decide |
| Handoffs in | None. Inputs come from other skills and are internal |
| Handoffs out | H08, H16 |
| Human gate after | A person decides every ranking, link and feature decision. Approver role: product owner |
| Used by | None. A person leads this work, and an agent may prepare material. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Makes the choice of what matters most explicit: the criteria first, then the ranking, with the evidence beside it. It enables the decisions about which jobs the work serves and which features go forward.

## 3. When to use

Use when the jobs-to-be-done matrix is ready for a shortlist, and again when concept test results are ready for a decision on each feature.

Not for: scoring or counting test results. Use 19-analyse-test-results. Not for story mapping, estimation or release slicing, which happen in the story mapping workshop. The breakdown has no rows for that workshop, so this skill covers the two decisions it does break down. To verify who owns the rest.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Jobs-to-be-done matrix: jobs/jobs-to-be-done-matrix.md | None. Internal, from 06-draw-out-insights-and-needs | Required for steps 2 and 3 | Stop and ask |
| Objectives from step 1 | None. To verify where they are recorded | Required for step 3 | Stop and ask |
| Feature acceptance and validated assumptions: analysis/concept-test-analysis.md | None. Internal, from 19-analyse-test-results | Required for step 4 | Stop at step 4 and ask |
| Prioritisation criteria, written down before ranking | None. Held in the local config file or agreed by people | Required | Stop and ask |
| Acceptance threshold from the test plan: tests/test-plan.md | None. Internal | Required for step 4 | Stop at step 4 and ask |
| Local config file: local-config.md (criteria, thresholds, who signs, approver roles) | None | Required | Stop and ask |
| Templates: templates/prioritisation-templates.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Check the inputs and the criteria. Confirm the criteria are written down and dated before any ranking starts. If they are not, stop and ask a person to write them. List any input that is draft or missing.
2. **Judgment.** Propose the jobs that matter most and are served worst. Options to produce: a shortlist built from the matrix columns for importance, how well the job is served today, and strength of evidence, with the working shown. Criteria: the written criteria, importance high, served poorly, evidence meets the threshold. A person decides the shortlist. Save in jobs/priority-jobs.md.
3. **Judgment.** Propose the objective each shortlisted job ties to. Options to produce: for each job, one or two candidate objectives with the measure each one uses. Criteria: the job directly affects the measure, and the link can be explained in a sentence. A person decides. List every shortlisted job with no objective.
4. **Judgment.** Propose a decision for each feature: goes forward, changes or is dropped. Options to produce: for each feature, the three choices with the consequence of each, the acceptance result against the threshold in the test plan, the validated or rejected assumptions behind it and the gaps found. Criteria: acceptance meets the threshold set before the test, no rejected assumption carries the feature, effort and gaps are stated. A person decides, names who signs feature acceptance, and records the threshold used. Save in decisions/feature-decisions.md.
5. **Mechanical.** Write the priority jobs and the feature decisions from the templates, with the criteria used, the evidence tables and the Gaps and open questions section. List what was not checked. Set status draft until the approver signs.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Priority jobs, tied to objectives | H08 | Markdown table | jobs/ | priority-jobs.md |
| Decision per feature | H16 | Markdown table | decisions/ | feature-decisions.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to lay out the options, how to show the working, the order of items before a person ranks.
- Must not decide: the criteria, the shortlist, the objective link, a feature decision, the acceptance threshold, or who signs.
- Escalate when: no written criteria exist, the threshold was set after the test, a shortlisted job has no objective, or a feature decision contradicts a rejected assumption.
- Approver role: product owner. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: each output names the decision and the options.
- [ ] Test 3, Traceable: every option cites the matrix row, result or assumption it rests on.
- [ ] Test 6, Owned and statused: signer role, date and status are present.
- [ ] Test 7, Honest about gaps: jobs with no objective and features with thin evidence are listed.
- [ ] Criteria are dated before the first ranking.
- [ ] The threshold used was set before the test.
- [ ] No ranking or decision was made by the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| The shortlist is filed and forgotten | Breakdown gap note on J5: "Does this shortlist feed prioritization in step 4, or is it filed and forgotten?" | The shortlist is a named output with a handoff ID, H08 |
| Criteria not written down | Main process file gap note on step 4: "Are the prioritization criteria written down?" | Step 1 refuses to start without written, dated criteria |
| No clear signer or threshold for feature acceptance | Breakdown gap note on T5: "Who signs off feature acceptance, and at what threshold?" | Step 4 records the signer and the threshold, and checks the threshold predates the test |
| Ranking by whoever argues loudest | Hypothesis from how workshops run | Criteria first, then options with the working shown |
| Priorities set after seeing results | Hypothesis from the as-is audit: no step fixes criteria before ranking | Step 1 and the quality checks on dates |

## 10. Principles applied

- Prioritise human control: people write the criteria, rank and decide, and the skill only lays out options.
- Build trust through visible evidence: every option shows the evidence it rests on.
- Start simple: two outputs and the criteria that drive them.

## 11. References

- design-stories SKILL.md, read in full (276 lines). Kept: the idea of prioritising vertically within each task and cutting slices with an MVP boundary, which this skill does not yet cover. Not carried: backbone, walking skeleton, release slices and the BRD steps, which belong to the story mapping workshop. The breakdown has no rows for it.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-10: J5 and T5.
- Standard practice, not checked against a source: the options and criteria in steps 2, 3 and 4.
- Supporting file: templates/prioritisation-templates.md.
