---
name: 18-test-usability
description: Sets usability pass criteria before testing, from prior rounds, targets and reference scores, for a person to sign off. Use when a prototype is ready to test with users. Not for scoring or reading results, use 19-analyse-test-results.
allowed-tools: Read Grep Glob Write
---

# 18. Test usability

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 18, CAP-18 Test usability |
| Phase or scope | Design |
| Work nature mix | Mechanical 1; Judgment 1 (rows in the to-be breakdown). This skill has 4 Mechanical steps and 1 Judgment step, because it adds two guard steps |
| Authority level | Prepares. It drafts options. A person signs the criteria |
| Handoffs in | H18 |
| Handoffs out | None. The signed criteria are internal and feed 19-analyse-test-results |
| Human gate after | A person sets and signs off the pass criteria before the first session. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Fixes what counts as a pass before anyone sees a result, so results cannot be judged to fit. It enables the decision about whether the design is ready to build or needs rework.

## 3. When to use

Use when a prototype is ready to test with users and before the first session starts.

Not for: scoring, counting or reading results. Use 19-analyse-test-results. Not for running the sessions, which people do. The to-be breakdown has no rows for session planning or running, so this skill covers the pass criteria only. To verify whether more is wanted.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Test plan: tests/test-plan.md, with the tasks and the success definition for each task | None. To verify where it is recorded | Required | Stop and ask |
| Hi-fi prototype link and version | H18 | Required | Stop and ask |
| OKR targets that relate to usability | None. To verify | Optional | Proceed. Write that no target exists |
| Prior usability measurements: analysis/usability-benchmark.md from a prior round | None. Internal, from 19-analyse-test-results | Optional | Proceed. Write that no baseline exists |
| Published reference scores, with source and date | None | Optional | Proceed. Write that none were used |
| Local config file: local-config.md (confidence level, minimum sample, who signs, how criteria are versioned) | None | Required | Stop and ask |
| Template: templates/pass-criteria-template.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Check the test plan. Confirm it lists each task, a success definition for each task and the outcome levels. Confirm no session has started. If a session has started, stop and tell a person. Pass criteria set after a session are not criteria.
2. **Mechanical.** Gather the reference numbers. List every OKR target, prior measurement and published reference score that applies. Record each with its source file or page and its date. List what is missing. Evidence tag: Evidence for a measured number, Assumption for a target nobody has confirmed.
3. **Mechanical.** Draft candidate pass thresholds for task success and for SUS. Build each candidate from one source: a prior round, a target, or a published reference score. State the source beside every threshold. Describe a published average as a reference point, never as a pass mark. For each candidate, write what result would count as a pass and what result would not. Evidence tag: Assumption.
4. **Judgment.** Set and sign off the pass criteria. Options to produce: the candidate sets from step 3, each with its source and what it would have counted as a pass in the last round if one exists. Criteria: tied to the decision the test supports, a source a stakeholder would accept, set before the first session, stated in a way a script can check. A person chooses, signs, and records the signer role and the date.
5. **Mechanical.** Write the signed criteria into analysis/usability-pass-criteria.md with the version, the date, the sources and the signer role. Record the date of the first session beside it so the order is visible. After sign-off, change nothing in this version. A change before the next round is a new version with a stated reason. Write the evidence table and the Gaps and open questions section. Set status draft until the signer signs.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Usability pass criteria, signed before testing | None. Internal, read by 19-analyse-test-results | Markdown with an evidence table | analysis/ | usability-pass-criteria.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to lay out the candidates, which sources to list, how to phrase a threshold so a script can check it.
- Must not decide: the pass criteria, which candidate is chosen, a change to signed criteria, or whether to start testing. Must not use a published average as a pass mark.
- Escalate when: a session has already started, the test plan has no success definitions, no source exists for a threshold, or anyone asks to change signed criteria.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: the file names the decision the test supports.
- [ ] Test 3, Traceable: every threshold names its source and date.
- [ ] Test 6, Owned and statused: signer role, date and status are present.
- [ ] Test 7, Honest about gaps: missing targets, baselines and reference scores are listed.
- [ ] Test 8, Versioned and dated: version, date and the first session date are present.
- [ ] Criteria are dated before the first session.
- [ ] No published average is used as a pass mark.
- [ ] Each threshold is stated so a script or a person can check it.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Nobody signs the criteria, or they are not fixed before the first session | Breakdown gap note on G4: "Who signs the pass criteria, and are they fixed before the first session?" | Steps 1, 4 and 5 |
| No pass mark for SUS | Breakdown gap note on U4: "What SUS score counts as a pass? The NN/g page reports an average of 68, which is a reference point, not a pass mark. Who sets the bar?" | Step 3 labels the average as a reference point. A person sets the bar in step 4 |
| Success defined after the test | Breakdown gap note on U3: "Are success definitions set before the test or after? What sample size makes the rate worth reporting?" | Step 1 checks the success definitions exist before the first session |
| Criteria tuned to fit the results | Hypothesis from the as-is audit: no step sets criteria before testing | Step 5 freezes the signed version |
| Sessions and session planning not in the process | Breakdown: no sub steps for them | Listed as a gap. To verify |

## 10. Principles applied

- Prioritise human control: a person sets and signs the criteria, and the skill only offers options.
- Build trust through visible evidence: every threshold shows its source and date.
- Prevent errors: criteria are frozen before the first session, so they cannot be bent afterwards.

## 11. References

- design-validation SKILL.md, read in full (293 lines). Kept: the test plan metrics table with a target for each metric, and the analysis plan question "what score triggers redesign". Dropped: heuristic evaluation, scenario scripts and the design review checklist, which belong to other capabilities. Not used: its recommended participant count, which this pass did not check against a source.
- design-research SKILL.md (Phase A), read in full (229 lines). Kept: success thresholds taken from stated metrics. Dropped: project paths and the scenario script format.
- NN/g "Beyond NPS: SUS, NASA-TLX, and the Single Ease Question", read about 70 to 80 percent: the average of 68 is a reference point and not a pass mark.
- NN/g "Success Rate: The Simplest Usability Metric", read about 85 to 90 percent: it sets no pass threshold.
- NN/g "7 Steps to Benchmark Your Product's UX", read about 60 to 65 percent: keep the method consistent between rounds.
- Standard practice, not checked against a source: freezing the criteria at sign-off.
- Supporting file: templates/pass-criteria-template.md.
