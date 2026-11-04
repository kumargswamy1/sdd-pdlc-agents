---
name: 02-surface-assumptions
description: Logs what stakeholders and documents state as fact, belief or open question, marks beliefs with no evidence behind them, and prepares a risk ranking for a person. Use when kickoff or stakeholder material arrives. Not for turning gaps into research questions, use 03-plan-the-research.
allowed-tools: Read Grep Glob Write
---

# 02. Surface assumptions

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 02, CAP-02 Surface assumptions |
| Phase or scope | Discover |
| Work nature mix | Mechanical 3; Judgment 1 (rows in the to-be breakdown, counting each as-is step). This skill has 3 Mechanical steps and 1 Judgment step, because it groups two steps and adds a final write step |
| Authority level | Drafts. It logs and marks. A person ranks |
| Handoffs in | H01 |
| Handoffs out | None. The ranked log is internal and feeds 03-plan-the-research |
| Human gate after | Researcher reviews the log and the marks, then a person ranks the assumptions by risk. Approver role: research lead |
| Used by | AG-01 Research planner. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Brings the beliefs a project rests on into view, with their sources, before any research is designed. It enables the decision about which assumptions to test first.

## 3. When to use

Use when kickoff sessions, briefs or stakeholder material arrive and before research questions are written.

Not for: turning gaps into research questions. Use 03-plan-the-research. Not for deciding after a test whether an assumption held, which is a human step in 19-analyse-test-results.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Agreed reading of the vision and objectives | H01 | Required | Stop and ask |
| Stakeholder views from interviews with stakeholders and experts | None. Step 2 of the main process is optional and may happen informally | Optional | Proceed and write that no stakeholder views were recorded |
| Existing policies, systems and prior solutions, as documents | None | Optional | Proceed and list under Gaps |
| Briefs and prior material | None | Optional | Proceed and list under Gaps |
| Assumptions and questions log from stakeholder interviews, if one exists | None. To verify | Optional | Proceed. Never start a second list when one exists |
| Evidence log: evidence/evidence-log.md, for checking beliefs | None. Internal, from 05-organise-the-evidence | Optional | Proceed and mark every belief To verify |
| Template: templates/assumptions-log-template.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Log each stated fact, belief and open question with its source. Write one entry per row. Give each a generated ID in A-NNN format (e.g. A-001), the source file and location, and the role of the person or document that stated it. Tag the entry as stated: Fact, Belief or Open question. Do not judge it here. If a log of assumptions and questions already exists from the stakeholder interviews, load its entries and keep their IDs. Do not start a second list.
2. **Mechanical.** Have this step done by a person, or by a separate run whose output a person reviews, and not by the run that did step 1, because a checker never checks its own log. Name who did it. Mark which beliefs are assumptions with no evidence behind them. For each belief, look in the evidence log and the documents. If nothing supports it, tag it Assumption and list what you looked at. Mark where stakeholders disagree or the brief contradicts itself. List each pair of entries with both sources. Never reconcile a contradiction. Note it.
3. **Judgment.** Propose a risk ranking for every assumption and open issue. Options to produce: High, Medium or Low risk to the project outcome, each with one phrase why. Criteria: what happens to the project if it is wrong, how many decisions depend on it, how cheaply it can be checked, whether stakeholders disagree about it. A person decides the ranking.
4. **Mechanical.** Write the log from the template: entries, marks, contradictions, the proposed and decided ranking, and the evidence table. Add the Gaps and open questions section, listing missing inputs and anything not checked. Set status draft. Save as assumptions/assumptions-log.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Gaps, assumptions and issues log, ranked by risk | None. Internal, read by 03-plan-the-research | Markdown table with an evidence table | assumptions/ | assumptions-log.md |

Every output follows the file format requirements, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to word an entry, which evidence to look at, how to list contradictions.
- Must not decide: the risk ranking, whether a contradiction is resolved, whether an assumption is true, or which assumption to test. Must not mark entries it logged itself.
- Escalate when: no evidence sources exist to check beliefs against, a sponsor statement contradicts a document, a source holds sensitive content that has not been cleared, or two logs of assumptions exist.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: every input named by file name or handoff ID.
- [ ] Test 3, Traceable: every entry has a source file, a location and an evidence tag.
- [ ] Test 4, Single source: one log of assumptions. Entries keep their IDs.
- [ ] Test 7, Honest about gaps: missing inputs and unchecked beliefs are listed.
- [ ] Test 9, Findable and readable: fixed file name, stable IDs.
- [ ] Step 2 was done by a person, or by a separate run a person reviewed, and not by the run that did step 1.
- [ ] No contradiction was reconciled.
- [ ] The ranking column comes from a person, not from the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| No stakeholder views, so assumptions have no source | Breakdown gap note on R2: "Step 2 (added, unconfirmed) is where stakeholder views would come from. If it does not happen, where do assumptions come from?" | Step 1 reads documents and briefs when interviews do not exist, and writes that no stakeholder views were recorded |
| Disputes settled quietly | Breakdown gap note on R2: "Are disputed issues resolved or only noted?" | Step 2 lists contradictions and never resolves them |
| A belief written down as a fact | Hypothesis from how stakeholder material is stated | Step 1 tags entries as stated, and step 2 tags them again against evidence |
| The same assumption logged twice, once here and once in the stakeholder interview log | Breakdown gap note on R2 and the register of handoffs H05 and H07 | Step 1 loads the existing log and keeps its IDs |
| The logger marks its own entries | Hypothesis from the roster design check | Step 2 is done by a person or a reviewed separate run |

## 10. Principles applied

- Build trust through visible evidence: every entry cites its source, and every mark shows what was checked.
- Prioritise human control: a person ranks, and contradictions are noted, not settled.
- Start simple: one log, one ranking.

## 11. References

- design-discovery SKILL.md, read in full (380 lines). Kept: the rule to note contradictions and never reconcile them silently, and the practice of recording gaps as evidence limits. Dropped: project paths, sync scripts and the project relevance filter.
- NN/g "Tracking Research Questions, Assumptions, and Facts in Agile", read about 85 to 90 percent: record each assumption with its source and the next step to test it, so assumptions can become facts through research.
- NN/g "Discovery: Definition", read about 70 to 75 percent: an assumption mapping session questions stated facts, finds deep-rooted assumptions and ranks them by risk to the project outcome.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-02: R2.
- Standard practice, not checked against a source: the options and criteria in step 3.
- Supporting file: templates/assumptions-log-template.md.
