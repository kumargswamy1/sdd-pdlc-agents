---
name: 03-plan-the-research
description: Turns ranked gaps and assumptions into research questions, aims, participant criteria and supporting documents, assembled into one plan for sign-off. Use when the ranked assumptions log exists and research must be planned. Not for logging assumptions, use 02-surface-assumptions.
allowed-tools: Read Grep Glob Write
---

# 03. Plan the research

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 03, CAP-03 Plan the research |
| Phase or scope | Discover |
| Work nature mix | Mechanical 6; Judgment 5 (rows in the to-be breakdown, counting each as-is step). This skill has 6 Mechanical steps and 5 Judgment steps |
| Authority level | Drafts. It writes drafts and options. People decide |
| Handoffs in | H01 |
| Handoffs out | None. The research plan reaches the interviews and persona scoping with no handoff ID. To verify |
| Human gate after | Researcher reviews the drafts, then people decide each Judgment step. The sponsor and stakeholders agree the scope. Approver role: research lead |
| Used by | AG-01 Research planner. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Turns what the team does not know into a plan that says what to ask, whom to ask, why, and what finding would stop the work. It enables the sponsor's decision to approve the research and its scope.

## 3. When to use

Use when the ranked assumptions log exists and the team must decide how to learn what it needs to know.

Not for: logging or ranking assumptions. Use 02-surface-assumptions. Not for running the interviews or sessions, which people do. Not for planning a usability test, use 18-test-usability.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Ranked gaps, assumptions and issues log: assumptions/assumptions-log.md | None. Internal, from 02-surface-assumptions | Required | Stop and ask |
| Agreed objectives | H01 | Required | Stop and ask |
| Time and budget | None. To verify where they are recorded | Required for step 5 | Proceed and mark To verify |
| Access to users, schedule and constraints | None. To verify | Required for step 7 | Proceed, mark To verify and escalate |
| Sponsor, stakeholders and project team, for the walk-through | None. People | Required for steps 9 and 10 | Stop and ask |
| Templates: templates/research-plan-templates.md | None | Required | Stop and ask |

## 5. Method

Never put a participant's name or contact details in any file this skill writes. Describe participants by criteria only.

1. **Judgment.** Propose research questions before any method is chosen. Options to produce: for each ranked gap, two wordings of an open question about users, not about the product. Criteria: about users' behaviour, needs or context, answerable by research, tied to a gap or assumption ID. A person decides.
2. **Mechanical.** Record each assumption beside the question that tests it, with its source and the next step. Keep the assumption IDs from the log. Save in research-plan/research-questions.md.
3. **Judgment.** Propose cuts and merges. Options to produce: keep, merge or cut each question, with a reason. Criteria: research can answer it with the access available, it overlaps another question, it stays within the 12-question cap. A person decides.
4. **Mechanical.** Rank the questions by the decisions they inform. For each question, list the decisions in the objectives that depend on its answer. Order by number of decisions, then by the risk ranking in the log. Show the working.
5. **Mechanical.** Write each aim as the decision the research will inform. Use one aim per decision, in the form "so that <role> can decide <decision>", and cite the question IDs it covers. Save in research-plan/aims.md.
6. **Mechanical.** Define who to speak to, how many, and the inclusion and exclusion criteria, from the aims, the questions, access and constraints. State the participant mix that persona scoping will use. Prepare the supporting documents as drafts from the templates: discussion guide, screener and consent form. Save in research-plan/participants.md and research-plan/documents/.
7. **Mechanical.** Assemble the purpose, aims, questions, participants, method and schedule into one plan from the template. The breakdown has no step that chooses methods, so write To verify under Method and name the role that will choose them. Set status draft. Save as research-plan/research-plan.md.
8. **Judgment.** Prepare the walk-through for the sponsor and stakeholders. Options to produce: for each section of the plan, the question to put to them and the choice they are being asked to make. Criteria: serves an aim, fits the time and budget, within the access confirmed. People walk through the plan and collect changes.
9. **Judgment.** Propose a resolution for each change collected. Options to produce: accept, decline or ask for more evidence, each with its effect on the scope. Criteria: serves an aim, within time, budget and access, does not widen scope without a decision. People resolve the changes and agree the scope. Record the signer role and the date.
10. **Mechanical.** Write the evidence table and the Gaps and open questions section for every output. List what was not checked. Set status draft until the approver signs.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Research questions linked to assumptions, ranked | None. Internal | Markdown table | research-plan/ | research-questions.md |
| Research aims | None. Internal | Markdown | research-plan/ | aims.md |
| Participant plan | None. Internal | Markdown | research-plan/ | participants.md |
| Supporting documents: discussion guide, screener, consent form | None. Internal | Markdown, drafts | research-plan/documents/ | discussion-guide.md, screener.md, consent-form.md |
| Research plan, signed | None. To verify how it reaches the interviews and persona scoping | Markdown | research-plan/ | research-plan.md |

Every output follows the file format requirements, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to word drafts, the order of questions by the stated rule, the layout of documents.
- Must not decide: which questions stay, participant access, the scope, the methods, or the wording of a consent form. Must not record any participant's identity or contact details.
- Escalate when: access to participants is not confirmed, the question count exceeds the cap, no objectives exist, the sponsor's changes widen the scope, or no role is named to choose methods.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: every aim names the decision it informs.
- [ ] Test 3, Traceable: every question cites a gap or assumption ID.
- [ ] Test 6, Owned and statused: signer role, date and status are present.
- [ ] Test 7, Honest about gaps: missing methods, unconfirmed access and unsigned scope are listed.
- [ ] Test 8, Versioned and dated: version and date on every file.
- [ ] Questions were written before any method was chosen.
- [ ] No participant names or contact details appear.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| The plan starts from a chosen method rather than questions | Questions are written before any method is chosen — step 1 |
| Questions fitted to a method, and too many questions | Steps 1 and 3 and the 12-question cap |
| Access unconfirmed and the participant mix unowned | Step 6 states the mix and escalates unconfirmed access |
| No sign-off, and a plan locked after findings change the questions | Step 9 records the signer. The revisit trigger is To verify |
| Methods never matched to questions | Step 7 writes To verify and names a role |
| Identity data stored with plan files | The rule at the head of the method, and step 6 |

## 10. Principles applied

- Prioritise human control: people decide the questions, the scope and the sign-off.
- Build trust through visible evidence: each question cites its gap or assumption, and each aim cites its questions.
- Prevent errors: identity data stays out of plan files, and the consent form is a draft until approved.

## 11. References

- design-research SKILL.md (Phase A), read in full (229 lines). Kept: participant criteria and the habit of stating success thresholds up front. Dropped: scenario scripts, project paths and sync scripts. Conflict: it plans a usability test, not discovery research, so the aims, questions and exit steps here have no equivalent in it.
- NN/g "Research Plans: Organize, Document, Inform", read about 70 to 75 percent: a plan holds purpose and goals, participants, method and procedure, and relevant documents, and is shared with stakeholders for buy-in and scope.
- NN/g "Tracking Research Questions, Assumptions, and Facts in Agile", read about 85 to 90 percent: record each assumption beside the question that tests it, with its source and next step.
- NN/g "Discovery: Definition", read about 70 to 75 percent: a kickoff aligns the objective and the end point, a session generates research questions, and discovery can end in a decision not to proceed.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-03: R3, R4, R5 and R6.
- Standard practice, not checked against a source: the options and criteria in steps 1, 3, 6, 9 and 10.
- Supporting file: templates/research-plan-templates.md.
