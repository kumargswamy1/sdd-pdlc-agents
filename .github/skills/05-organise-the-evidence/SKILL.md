---
name: 05-organise-the-evidence
description: Logs, tags, links and numbers what was said and observed so every claim traces to a source. Use when raw notes, transcripts, recordings or test results arrive, or when draft claims need evidence links. Not for drawing out themes, use 06-draw-out-insights-and-needs.
allowed-tools: Read Grep Glob Write Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/check_quotes.py *)
---

# 05. Organise the evidence

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 05, CAP-05 Organise the evidence |
| Phase or scope | Discover. Also used on concept test and usability test results in Define and Design |
| Work nature mix | Mechanical 16; Judgment 4 (from the to-be breakdown). This skill has 11 Mechanical steps and 4 Judgment steps, because several steps are grouped |
| Authority level | Does. It logs, tags and numbers. It Prepares proposals for a person on merges, persona and job, confidence and ownership |
| Handoffs in | None. Raw capture (CAP-04) is not broken down and has no handoff ID. To verify |
| Handoffs out | H08, H10 |
| Human gate after | Researcher reviews the evidence log, then decides each proposal. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Turns raw material into a numbered, tagged log where every item names its source and its place in that source. It lets a reader check any claim in a persona, map or register in one step.

## 3. When to use

Use when raw notes, transcripts, recordings or test results are cleared for use, when a draft contains claims that need evidence links, or when a register needs numbering.

Not for: finding themes, needs or jobs in the evidence. Use 06-draw-out-insights-and-needs. Not for checking a finished output across the whole repository, use 20-update-evidence-repository.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Raw source files, one file per session or document: transcripts, notes, recordings, test results | None. To verify | Required | Stop and ask |
| Clearance record: a person has checked each source for sensitive content | None. To verify where it is recorded | Required | Stop and ask |
| Participant ID list. Participants appear by ID only | None. To verify | Required | Stop and ask |
| Draft whose claims need links, such as a persona set, an empathy map or a register | None. It is internal to the output being built | Optional | Skip step 13 and list the claims as gaps |
| Local config file: .github/templates/local-config.md (tag vocabulary, ID format, source ID format, repository location) | None | Required | Stop and ask |
| Evidence log template: templates/evidence-log-template.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Check the clearance record. List every source without one. Stop and ask a person before reading any of them.
2. **Mechanical.** Build the source index. Add one row per source to `evidence/source-index.md`: source ID, type (interview, focus group, concept test, usability test, document), date, participant ID and file name. Source IDs follow the format in the local config file.
3. **Mechanical.** Pull the items. From each cleared source, pull goals, behaviours, tasks, pain points, context, constraints, direct quotes, observed actions, stated thoughts and apparent feelings. Write one item per row. Record the source ID and the location in the source (timestamp, page or line). Evidence tag: Evidence.
4. **Mechanical.** Verify the quotes. Put every quote in a text file, one per line, and run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_quotes.py --source <source file> --quotes <quotes file>`. Keep a quote only if it passes. Rewrite a failed quote as a paraphrase with no quotation marks, or drop it. A paraphrase is never shown in quotation marks.
5. **Mechanical.** Tag each item as said, did, thought or felt. Keep inferred thoughts and feelings apart from what the participant said. Mark an inferred thought or feeling as Inference.
6. **Mechanical.** Tag each item for the work at hand: feature, task and theme for concept tests, or screen, task, theme and issue type for usability tests. Use only the vocabulary in the local config file. Keep a link to the moment in the session.
7. **Mechanical.** Log the items per participant and per concept or task, so a reader can see all of one participant's items, or all items for one task, in one view.
8. **Mechanical.** Check drafts written by someone else. Cross-check each entry of a draft (empathy map, persona set, register) against the items. Tag each entry Evidence, Inference or Assumption. Flag every entry that is inference, not evidence. Never tag or flag an entry you wrote.
9. **Mechanical.** Give every item and every register entry a stable ID, in the format from the local config file. Generate IDs, never type them. Never reuse an ID. In a register table, put the ID in the first column and the item text in the second, so 20-update-evidence-repository can check the table.
10. **Judgment.** Propose merges for duplicate and near duplicate entries. Options to produce: merge, keep apart, split. Criteria: same user need, same source or different sources, wording difference only. List each proposal with both item IDs. A person decides.
11. **Judgment.** Propose the persona and the job for each entry. Options to produce: up to two candidate persona and job pairs per entry, each with the item IDs behind it. Criteria: how directly the items show the persona's goal, and whether more than one participant shows it. A person decides.
12. **Judgment.** Propose a confidence for each entry. Options to produce: High, Medium or Low, with one phrase why. Criteria: number of independent sources, how direct the evidence is, how recent it is. A person decides.
13. **Mechanical.** Link claims to evidence. For each claim in the draft, record the item IDs that support it. List claims with no item as gaps. Never delete a claim to close a gap.
14. **Judgment.** Propose an owner role for each register. Options to produce: two or three roles. Criteria: can keep the list current, can answer questions about it, is not the author of the entries. A person names the owner.
15. **Mechanical.** Write the evidence log from the template. Add the proposals, the gaps and open questions, and a list of what was not checked. Set status draft.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Source index | None. Internal | Markdown table | evidence/ | source-index.md |
| Evidence log (items, tags, IDs, links) | None. Internal | Markdown table, evidence table | evidence/ | evidence-log.md |
| Tagged feedback log for a concept test or usability test | None. Internal to the analysis step | Markdown table | evidence/ | tagged-feedback-log.md |
| Evidence index for a persona set | H08, H10 | Markdown table | evidence/ | evidence-index.md |
| Pain point register with IDs | H08 | Markdown table | registers/ | pain-point-register.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to split a source into items, which tag vocabulary term fits, the order of items, ID generation.
- Must not decide: a merge, a persona and job, a confidence rating, an owner, or whether sensitive content may be read. Must not tag or flag its own entries.
- Escalate when: a source has no clearance record, a quote fails the check, a source cannot be read, an item cannot be placed in its source, or two sources contradict.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: inputs named by file name, readable without chat history.
- [ ] Test 3, Traceable: every item has a source ID, a location and an evidence tag.
- [ ] Test 4, Single source: registers are cited by ID and not copied into other files.
- [ ] Test 7, Honest about gaps: failed quotes, uncleared sources and unlinked claims are listed.
- [ ] Test 8, Versioned and dated: version and date on every file.
- [ ] Test 9, Findable and readable: fixed file names, stable IDs, Markdown.
- [ ] Test 10, Checkable: reviewer can tick the checklist in the handoff template.
- [ ] Every quotation mark in the log passed the quote check.
- [ ] Participants appear by ID only. No names, no organisation names.
- [ ] No entry was tagged or flagged by the agent that wrote it.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Entries that cannot be traced to a quote or session | Breakdown gap note on P2: "Can each entry be traced back to a quote or session?" | Step 3 records source ID and location for every item |
| Inferred thoughts mixed with what users said | Breakdown gap note on E2: "Are inferred thoughts and feelings kept separate from what users actually said?" | Steps 5 and 8 |
| No line between evidence and team assumption | Breakdown gap note on E5: "Where is the line between evidence and team assumption, and is it marked?" | Step 8 tags every entry and flags inference |
| Findings that cannot be traced to a moment in a session | Breakdown gap note on T2: "Is every finding traceable to a participant and a moment in a session?" | Step 6 keeps a link to the moment |
| No agreed rule for duplicates | Breakdown gap note on N2: "Who decides what counts as a duplicate, and who can add a pain point later?" | Step 10 proposes, a person decides. The owner in step 14 controls additions |
| Each output keeps its own pain point list | Breakdown gap note on N5: "Do personas, empathy maps, the blueprint and the jobs matrix cite the register by ID, or does each keep its own pain point list?" | Steps 9 and 13 |
| A quote that the participant never said | Hypothesis from the roster design check | Step 4 checks every quote by exact match |
| Sensitive content read without clearance | Hypothesis from the project's sensitivity guidance | Step 1 stops until a person has cleared the source |

## 10. Principles applied

- Build trust through visible evidence: steps 3, 8, 13 and 15 give every claim a source, a tag, a confidence and a not-checked list.
- Prevent errors: step 4 uses an exact match check, and step 9 generates IDs.
- Prioritise human control: steps 1 and 10 to 14 stop for a person.

## 11. References

- design-discovery SKILL.md, read in full (380 lines). Its Tier 1 per-input cleaning, extraction radar and rule "Never skip Tier 1" are the pattern this skill follows. Its project paths and sync scripts are not carried over.
- NN/g "Tracking Research Questions, Assumptions, and Facts in Agile", read about 85 to 90 percent: the practice of recording each assumption with its source and turning validated assumptions into facts.
- As-is and to-be breakdown workbooks, read in full, for the step order and natures. To-be rows tagged CAP-05: P2, P6, E2, E5, N1, N2, N4, N5 (step 1), T2, U1.
- Claude Code skills documentation (code.claude.com/docs/en/skills), read about 60 to 70 percent: the allowed-tools syntax that limits Bash to one script.
- Standard practice, not checked against a source: the confidence criteria in step 12 and the owner criteria in step 14.
- Supporting files: templates/evidence-log-template.md, scripts/check_quotes.py.
