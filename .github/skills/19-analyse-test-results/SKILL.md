---
name: 19-analyse-test-results
description: Scores, counts and reads concept test and usability test results against agreed criteria, giving rates, SUS scores, benchmarks and ranked issues. Use when the tagged feedback log and test plan are ready. Not for logging or tagging results, use 05-organise-the-evidence.
allowed-tools: Read Grep Glob Write Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/rate_levels.py *) Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/score_sus.py *)
---

# 19. Analyse test results

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 19, CAP-19 Analyse test results |
| Phase or scope | Cross cutting. Concept tests in Define and usability tests in Design |
| Work nature mix | Mechanical 10; Judgment 9 (rows in the to-be breakdown). This skill groups them into 7 Mechanical steps and 4 Judgment steps |
| Authority level | Does. It scores and compares. It Prepares options for people on patterns, assumptions, severity and priority |
| Handoffs in | H07, H18 |
| Handoffs out | H16, H22, H24 |
| Human gate after | Researcher recomputes a sample of scores by hand, then people decide each Judgment step. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Turns logged test results into numbers a team can trust and issues a team can rank, each with its evidence. It enables the decision about what to carry forward, what to fix and whether results meet the criteria agreed before testing.

## 3. When to use

Use when a concept test or usability test has been run, results are logged and tagged, and the test plan holds the success criteria.

Not for: logging, tagging or numbering results. Use 05-organise-the-evidence. Not for setting pass criteria before testing, use 18-test-usability. Not for assembling the backlog or telling stakeholders, use 14-share-and-align-with-stakeholders.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Tagged feedback log: evidence/tagged-feedback-log.md | None. Internal, from 05-organise-the-evidence | Required | Stop and ask |
| Test plan with success criteria and level definitions: tests/test-plan.md | None. To verify where it is recorded | Required for steps 1, 2 and 6 | Stop and ask |
| Task or feature outcome data: tests/task-results.csv | None | Required for steps 1, 2 and 6 | Stop and ask |
| SUS responses: tests/sus-responses.csv | None | Required for step 7 | Skip step 7 and list it under Gaps |
| Assumptions and open questions log | H07 | Required for step 4 | Proceed and mark To verify |
| Hi-fi prototype link and version | H18 | Optional | Proceed and mark To verify |
| Pass criteria, signed off by a person: analysis/usability-pass-criteria.md | None. Internal, from 18-test-usability | Required for step 10 | Stop and ask |
| Prior measurements and targets from the OKRs | None. To verify | Optional | Proceed. Write that no baseline exists |
| Local config file: local-config.md (confidence level, minimum sample, severity scale, ID formats) | None | Required | Stop and ask |
| Templates: templates/results-templates.md | None | Required | Stop and ask |

## 5. Method

Show n beside every rate and score. Never average outcome levels. Run the scripts for every calculation and paste their output. Do not calculate by hand in prose.

1. **Mechanical.** Compare concept test results with the success criteria. Check that the test plan is dated before the sessions. If it is not, flag every criterion as set after the test. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/rate_levels.py --data tests/task-results.csv --levels <levels from the test plan>` and list each criterion with its result: met, not met or not comparable. Evidence tag: Evidence.
2. **Mechanical.** Count acceptance by feature. Run the same script on the feature outcome data, with the acceptance levels from the test plan. Paste the table into analysis/concept-test-analysis.md.
3. **Judgment.** Propose patterns in desirability and surprises. Options to produce: patterns each with participant count and item IDs, and surprises as results that contradict a stated assumption. Criteria: more than one participant shows it (threshold from the local config file), item IDs cited, direct evidence. People decide which patterns stand. Tag each Inference.
4. **Judgment.** Propose a status for each assumption and list the gaps found. Options to produce: confirmed, rejected or still open, each with item IDs. Criteria: how directly the items address the assumption, number of participants, any contradicting item. A person decides. For each rejected assumption, list the personas, blueprints, principles and registers that cite it, by file name and ID. This list feeds 20-update-evidence-repository.
5. **Judgment.** Propose patterns, root causes and severity for usability issues. Options to produce: patterns across participants, one root cause apart from its symptoms for each problem, and a severity of 0 to 4 as proposed (0 not a usability problem, 1 cosmetic, 2 minor, 3 major, 4 catastrophe). Criteria: frequency, impact on the user, and whether the problem persists or recurs. A person rates. A second person checks the ratings. Save findings with IDs in the RF-NNN format in analysis/usability-findings.md.
6. **Mechanical.** Score each usability task. Use three outcome levels: success, success with issues, failure. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/rate_levels.py --data tests/task-results.csv --levels "success,success with issues,failure" --confidence <from the local config file>`. Report the share at each level per task with its confidence interval. Confirm that the success definitions in the test plan are dated before the sessions. Report n beside every share. Save in analysis/task-success-rates.md.
7. **Mechanical.** Score the SUS questionnaires. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/score_sus.py --data tests/sus-responses.csv`. Report n, the mean and the spread. State that a SUS score is not a percentage, and that a published average is a reference point and not a pass mark. Save in analysis/sus-score.md.
8. **Mechanical.** Record the baseline: measures, method, participants and conditions. Compare with targets, prior rounds or competitors where they exist. If no prior round or target exists, write that no baseline exists. Flag any difference in method between rounds. Save as analysis/usability-benchmark.md.
9. **Judgment.** Propose the split of findings into fixes, wishlist ideas and items to defer, and rank them. Options to produce: a type for each finding, and a rank by severity, reach and effort. Criteria: severity, how many participants are affected, estimated effort. A person decides. Keep all three types in one list with a type column, because the wishlist goes into the backlog. Save as analysis/ranked-findings.md.
10. **Mechanical.** Compare results with the pass criteria. This step is done by a person, or by a separate run whose output a person reviews, and not by the run that produced the scores, because a checker never checks its own work. Name who did it. State met or not met for each criterion, with the source file and version of the criterion. Never state what to do. Save as analysis/pass-criteria-comparison.md.
11. **Mechanical.** For every output, write the evidence table, the Gaps and open questions section and a list of what was not checked. Set status draft.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Concept test analysis: criteria compared, acceptance counts, patterns, assumption statuses, gaps, affected outputs | H16 | Markdown | analysis/ | concept-test-analysis.md |
| Usability findings with severity | H22 | Markdown table | analysis/ | usability-findings.md |
| Success and failure rate per task | None. Internal | Markdown table | analysis/ | task-success-rates.md |
| SUS score | None. Internal | Markdown | analysis/ | sus-score.md |
| Usability benchmark | H24 | Markdown | analysis/ | usability-benchmark.md |
| Ranked findings: fixes, wishlist, defer | H24 | Markdown table | analysis/ | ranked-findings.md |
| Pass criteria comparison | H22, H24 | Markdown table | analysis/ | pass-criteria-comparison.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: which script options come from the test plan, how to lay out tables, the order of findings before ranking.
- Must not decide: whether results are good enough, a severity rating, a priority, an assumption status, the loop back to design, a pass mark, or a criterion. Must not change a criterion after the test. Must not run step 10 on scores it produced.
- Escalate when: success definitions or criteria are dated after the sessions, a script refuses the data, a participant appears twice, n is below the minimum in the local config file, or the method differs from a prior round.
- Review: steps 1 and 2 are reviewed together, steps 6 to 8 are reviewed together after step 8, and step 10 is reviewed after its own run.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: inputs named by file name and handoff ID.
- [ ] Test 3, Traceable: every number comes from a script run on a named data file. Every finding cites item IDs.
- [ ] Test 7, Honest about gaps: small samples, missing baselines and missing SUS data are listed.
- [ ] Test 8, Versioned and dated: test plan version and date on every output.
- [ ] Test 10, Checkable: reviewer can tick the checklist in the handoff template.
- [ ] n appears beside every rate and score.
- [ ] No outcome levels were averaged.
- [ ] A reviewer recomputed a sample of scores by hand.
- [ ] Step 10 was done by a person, or by a separate run a person reviewed, and not by the run that scored. The doer is named.
- [ ] No output states a decision on pass, fix or priority.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Analysis recorded with test preparation | Breakdown gap note on T3: "Where is analysis recorded? The slide lists it under the same row as test preparation." | Outputs go to analysis/, separate from tests/ |
| Rejected assumptions never reach the outputs that cite them | Breakdown gap note on T4: "Do rejected assumptions flow back into personas, blueprints and principles?" | Step 4 lists the affected files and IDs for 20-update-evidence-repository |
| No written severity scale or second rater | Breakdown gap note on U2: "Is a severity scale written down? Who rates, and does a second person check?" | Step 5 uses the 0 to 4 scale and a second person |
| Success defined after the test, or sample too small | Breakdown gap note on U3: "Are success definitions set before the test or after? What sample size makes the rate worth reporting?" | Steps 1 and 6 check dates. The script marks groups below the minimum sample |
| Average SUS read as a pass mark | Breakdown gap note on U4: "What SUS score counts as a pass? The NN/g page reports an average of 68, which is a reference point, not a pass mark. Who sets the bar?" | Step 7 states it is not a pass mark. Criteria come from 18-test-usability |
| No baseline, or a method that changed | Breakdown gap note on U5: "Is there an earlier baseline or an OKR target to compare with? Will later rounds use the same method?" | Step 8 records the method and flags differences |
| Wishlist and fixes in separate lists | Breakdown gap note on U6: "Who sets priority? Does the wishlist stay apart from the fix list?" | Step 9 keeps one list with a type column. Team answer, 2026-10-12: the wishlist goes into the backlog |
| No defined loop back when results fall short | Breakdown gap note on U7: "Is there a defined loop back when results fall short? Who decides ship or fix, and does rework return to step 7 or step 8?" | Step 10 compares only. A person decides, in 14-share-and-align-with-stakeholders |
| Arithmetic mistakes in prose | Hypothesis from the roster design check | All calculations run in scripts |
| A checker comparing against thresholds it drafted | Hypothesis from the roster design check | Step 10 is done by a person or a reviewed separate run, against criteria signed off by a person |

## 10. Principles applied

- Prevent errors: calculations run in scripts, and the scripts stop on bad data.
- Build trust through visible evidence: n, method and the data file are shown beside every number.
- Prioritise human control: severity, priority, assumption status and pass or fail decisions stay with people.

## 11. References

- design-research SKILL.md (Phase B), read in full (229 lines). Kept: findings with frequency, severity, evidence and implication, the RF-NNN stable ID convention, and the rule not to synthesise without evidence. Dropped: project paths and sync scripts, persona and story increment flags (replaced by the affected-outputs list in step 4), and the governance input file, which belongs to governance. Conflict: it rates severity as critical, major, minor or observation, while the breakdown cites the NN/g 0 to 4 scale. This skill uses 0 to 4. To verify whether a mapping is wanted.
- NN/g "Success Rate: The Simplest Usability Metric", read about 85 to 90 percent: three outcome levels, report each level, do not average, give confidence intervals. It sets no pass threshold.
- NN/g "Beyond NPS: SUS, NASA-TLX, and the Single Ease Question", read about 70 to 80 percent: the average of 68 is a reference point, and the score is not a percentage.
- NN/g "7 Steps to Benchmark Your Product's UX", read about 60 to 65 percent: record the measures and method, and keep the method consistent between rounds.
- NN/g "Severity Ratings for Usability Problems", read about 70 to 75 percent: the 0 to 4 scale, built from frequency, impact and persistence.
- Standard practice, not checked against a source: the Wilson score interval used by rate_levels.py, and the SUS scoring in score_sus.py (odd items minus 1, even items 5 minus the answer, sum times 2.5).
- Supporting files: templates/results-templates.md, scripts/rate_levels.py, scripts/score_sus.py.
