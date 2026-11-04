---
name: 08-frame-the-problem
description: Condenses pain points, needs and jobs into candidate problem statements, each citing its evidence IDs, for a person to choose, edit and own. Use when the registers, jobs matrix and current-state blueprint are ready. Not for need statements, use 06-draw-out-insights-and-needs.
allowed-tools: Read Grep Glob Write
---

# 08. Frame the problem

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 08, CAP-08 Frame the problem |
| Phase or scope | Define |
| Work nature mix | Mechanical 1; Judgment 1 (rows in the to-be breakdown). This skill has 3 Mechanical steps and 1 Judgment step, because it adds a guard step and a final write step |
| Authority level | Drafts. It writes candidates. A person chooses, edits and owns the statement |
| Handoffs in | H08 |
| Handoffs out | None. The agreed problem statement has no handoff ID yet. To verify |
| Human gate after | Researcher reviews the candidates, then a person chooses, edits and owns the problem statement. Approver role: project lead |
| Used by | None. A person leads this work, and an agent may prepare material. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

States the problem the work will solve, in terms of users and the organisation, grounded in the registers and owned by a named person. It enables the decision about what the team designs for, and what evidence would change that.

## 3. When to use

Use when the pain point register, the user need register, the jobs matrix and the validated current-state blueprint are ready, and before ideas for the future state are shaped.

Not for: writing need statements or jobs. Use 06-draw-out-insights-and-needs. Not for deciding what matters most, which is a human step in 10-prioritise.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Pain point register: registers/pain-point-register.md | H08 | Required | Stop and ask |
| User need register: registers/user-need-register.md | H08 | Required | Stop and ask |
| Jobs-to-be-done matrix: jobs/jobs-to-be-done-matrix.md | H08 | Required | Stop and ask |
| Validated as-is journey blueprint: journeys/as-is-journey-blueprint-validated.md | H08 | Required | Stop and ask |
| Objectives from step 1 | None. To verify where they are recorded | Required | Stop and ask |
| Local config file: local-config.md (evidence threshold, ID formats, solution word list, approver roles) | None | Required | Stop and ask |
| Template: templates/problem-statement-template.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Check the inputs. List the pain points, needs and jobs by ID, and the objectives. Confirm each register is approved or say it is draft. Mark any input thinner than the evidence threshold in the local config file. If an input is missing, stop.
2. **Mechanical.** Draft candidate problem statements. Group related pain points, needs and jobs into issues, by shared persona and job. Condense each issue into one statement with four parts: who is affected and what goes wrong, why it happens, the cost to users, and the cost to the organisation. Cite the pain point, need and job IDs behind it, and the objective it serves. Name no solution. Check each statement against the solution word list in the local config file. Propose a measurable signal that would show improvement, and write To verify beside any signal that cannot be measured today. Draft three to five candidates. Evidence tag: Inference.
3. **Judgment.** Choose, edit and own the problem statement. Options to produce: the candidates from step 2, each with the evidence IDs behind it and the importance to users and to the organisation. Criteria: grounded in registers that meet the evidence threshold, linked to an objective, no solution inside it, matters to users and to the organisation, small enough for the team to act on. A person chooses, edits and names the owner role. The person also states what evidence would change the statement. Record the date.
4. **Mechanical.** Write the problem statement file from the template: the agreed statement, the owner role, the evidence IDs, the change trigger, the candidates not chosen, the evidence table, and the Gaps and open questions section. Set status draft until the owner signs. Save as problem/problem-statement.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Problem statement, with evidence IDs, a named owner and a change trigger | None. To verify how it reaches experience architecture | Markdown with an evidence table | problem/ | problem-statement.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to group evidence into issues, how to word candidates, which measurable signal to propose.
- Must not decide: which statement stands, who owns it, what would change it, or whether a solution may be named in it. Must not invent an evidence ID.
- Escalate when: a register is missing or draft, evidence is below the threshold, candidates conflict with an objective, or the problem seems to be a solution in disguise.
- Approver role: project lead. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: the file names the decision it enables.
- [ ] Test 3, Traceable: every candidate cites pain point, need and job IDs and an objective.
- [ ] Test 4, Single source: registers are cited by ID and not copied.
- [ ] Test 6, Owned and statused: owner role, date and status are present.
- [ ] Test 7, Honest about gaps: thin evidence and unmeasurable signals are listed.
- [ ] No candidate names a solution.
- [ ] The change trigger is written.
- [ ] The statement was chosen by a person, not by the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| No problem statement anywhere in the process | Main process file gap note on step 4: "No problem statement or needs statement appears on the slide. Where is the problem framed, and who owns it?" | This skill exists to frame it, and step 3 names the owner |
| The statement has no owner and no trigger for change | Breakdown gap note on G1: "Who owns the problem statement, and what evidence would change it?" | Step 3 records the owner role and the change trigger |
| A solution written as a problem | Hypothesis from the needs guidance of the IBM toolkit, which asks for needs and not features | Step 2 checks each candidate against a solution word list |
| A statement resting on thin evidence | Hypothesis from the roster design check | Steps 1 and 2 apply the evidence threshold |
| The skill picks the statement | Hypothesis from the roster design check | Step 3 is a Judgment step. A person decides |

## 10. Principles applied

- Prioritise human control: a person chooses, edits and owns the statement.
- Build trust through visible evidence: every candidate cites its IDs and objective.
- Start simple: one agreed statement, with the candidates kept on file.

## 11. References

- NN/g "From Research Goals to Usability-Testing Scenarios: A 7-Step Method", read in full: problem statements focus the team and tie research to issues everyone wants solved, are written by condensing grouped issues, record the cost to people and to the organisation, and suggest metrics to track improvement.
- design-discovery SKILL.md, read in full (380 lines). Kept: the problem statement section of the design brief, and the rule that discovery proposes no interface solutions. Dropped: the design principles section, which belongs to 15-structure-the-experience, and project paths and sync scripts. Conflict: it builds the statement from documents, while this skill builds it from the registers.
- IBM Enterprise Design Thinking Toolkit, Needs Statements, read in full (11 pages): write needs and not features. Source: ibm.com/downloads/documents/us-en/137a1e253e5bac0b.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-08: G1, which is new in the to-be and closes an audit gap.
- Standard practice, not checked against a source: the four part structure of a statement in step 2, and the options and criteria in step 3.
- Supporting file: templates/problem-statement-template.md.
