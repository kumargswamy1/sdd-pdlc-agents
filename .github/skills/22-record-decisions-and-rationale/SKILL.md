---
name: 22-record-decisions-and-rationale
description: Appends each decision to an append-only log with who decided, the options, the reason, and the story, evidence and principle behind it. Use when a person decides something that later work will rely on. Not for packaging approved work, use 13-package-for-handoff.
allowed-tools: Read Grep Glob Write
---

# 22. Record decisions and rationale

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 22, CAP-22 Record decisions and rationale |
| Phase or scope | Cross cutting. Today covers design foundations and screens only |
| Work nature mix | Mechanical 2; Judgment 0 (rows in the to-be breakdown). This skill has 5 Mechanical steps, because it adds a guard step, a check step and a final write step |
| Authority level | Does. It writes entries from what people decided. It never decides or invents a reason |
| Handoffs in | None. Inputs come from other skills and from people and are internal |
| Handoffs out | None. The step 8 decision log has its own handoff, H20, whose producer is not broken down. To verify whether this skill writes it |
| Human gate after | The decider confirms each entry says what they decided and why. Approver role: artifact owner |
| Used by | AG-04 Handoff keeper. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Keeps the reason behind every design decision where the next person can find it, so work is not redone and decisions can be questioned with the facts. It enables a later reader to judge whether a decision still holds.

## 3. When to use

Use when a person decides something that later work relies on: a design rule, a screen, a breach, a gap fix or an exception.

Not for: making or ratifying decisions. People decide. Not for packaging approved work for handoff, use 13-package-for-handoff. Not for checking designs, use 17-check-designs-against-principles-and-standards.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| The decision, stated by the person who made it, with their role and the date | None. A person | Required | Stop and ask |
| The reason the person gave | None. A person | Required | Stop and ask. Never write a reason the person did not give |
| Options considered and rejected, with the reasons | None. A person or the file that listed the options | Optional | Write To verify |
| Story, job or pain point, evidence and principle IDs behind the decision | None. Internal | Required for screens and foundations | Stop and ask |
| Screen plan with the story, evidence and principle IDs for each screen: screens/screen-plan.md, and the design language foundations: language/foundations.md | None. Internal, from 12-design-the-detailed-screens and 16-define-the-design-language | Required for steps 3 and 4 | Stop at those steps and ask |
| The existing decision log: decisions/decision-log.md | None. Internal | Required | Create it from the template |
| Local config file: .github/templates/local-config.md (ID format, approver roles, where the log lives) | None | Required | Stop and ask |
| Template: templates/decision-log-template.md | None | Required | Stop and ask |

## 5. Method

The log is append-only. Never edit or delete an entry. A correction is a new entry that cites and supersedes the old one.

1. **Mechanical.** Check each decision. Confirm it names a person's role as the decider and a date, and that the reason was stated by that person. List decisions missing either. Stop and ask a person for each. Never infer a decider or a reason.
2. **Mechanical.** Append one entry per decision. Give it a generated ID in the format from the local config file. Write the topic, the decision in the person's words, the decider's role, the date, the options considered and rejected with the reasons, the evidence, story and principle IDs, and what it affects. Save in decisions/decision-log.md.
3. **Mechanical.** For design foundations, record why each rule was chosen and which principle it serves, from the foundations file and the decider's stated reason. Write one entry for each rule.
4. **Mechanical.** For screens, record the story, evidence and principle behind each screen, from the screen plan. List every screen with no story, evidence or principle as unrecorded. Never fill a gap with a guess.
5. **Mechanical.** Check the log. List entries with no decider role, no date, no stated reason or no cited ID, and any entry that changed a prior one without a superseding entry. Write the evidence table and the Gaps and open questions section. Set status draft until the decider confirms each entry.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Decision log, append-only | None. Internal. H20 carries the step 8 decision log, produced elsewhere. To verify | Markdown | decisions/ | decision-log.md |
| Unrecorded and unconfirmed list | None. Internal | Markdown | decisions/ | decision-gaps.md |

Every output follows the handoff standard, carries an evidence table and has status draft until the decider confirms.

## 7. Authority and gates

- May decide: how to lay out an entry, how to word what a person said as a short statement.
- Must not decide: a decision, a reason, a decider, or whether a decision was right. Must not edit or delete an entry. Must not write a reason the person did not give.
- Escalate when: a decision has no decider, a reason is missing, an entry would change a prior one, or a screen traces to nothing.
- Approver role: artifact owner. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every entry cites story, evidence and principle IDs, or says none exist.
- [ ] Test 6, Owned and statused: decider role, date and status are present.
- [ ] Test 7, Honest about gaps: unrecorded screens and unconfirmed entries are listed.
- [ ] Test 8, Versioned and dated: every entry is dated.
- [ ] Test 9, Findable and readable: stable IDs, one log file.
- [ ] No entry was edited or deleted.
- [ ] Every reason was stated by a person.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Foundations that follow preference with no recorded reason | Breakdown gap note on D2: "Do the foundations trace to the experience principles or to brand preference alone?" | Step 3 records the reason and the principle for each rule |
| Screens with no recorded story, evidence or principle | Breakdown gap note on H1: "Are screens traceable to evidence and experience principles, and where is that recorded?" | Step 4 records them and lists screens that have none |
| The agent invents a reason | Roster design check | The rule at the head of the method, and step 1 |
| The log is rewritten | Existing rule in the infrastructure: the decision log is append-only and corrections are new entries | Step 2 and the authority section |
| The step 8 decision log is not broken down | Main process file note: step 8 is an added step | Handoff H20 is flagged To verify |

## 10. Principles applied

- Build trust through visible evidence: every entry cites its reason and the IDs behind it.
- Prioritise human control: only people decide and give reasons, and the decider confirms the entry.
- Prevent errors: entries are appended and never edited, so history cannot be lost.

## 11. References

- ai-design-infrastructure CLAUDE.md, Decision Log section read: an append-only chronological record of what was decided, why, what was rejected and what it affects, where corrections are new entries that reference the old one. Kept: the entry fields and the append-only rule.
- design-governance SKILL.md, rules read: every change is logged, with no silent updates. Not carried: its principle synthesis, which belongs to the design language owner.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-22: D2 (step 2) and H1 (step 3).
- Standard practice, not checked against a source: the entry fields beyond those in the infrastructure convention.
- Supporting file: templates/decision-log-template.md.
