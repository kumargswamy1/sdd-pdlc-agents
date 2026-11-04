---
name: 13-package-for-handoff
description: Versions, links, annotates and sends approved work so the next stage can act without asking. Use when a human gate approves an artifact for handoff. Not for the handoff file format, use s2-handoff-standard. Not for detecting designer edits in Figma, use figma-handoff.
allowed-tools: Read Grep Glob Write
---

# 13. Package for handoff

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 13, CAP-13 Package for handoff |
| Phase or scope | Cross cutting. Used at the end of registers, experience principles, the information architecture, the design language system and the detailed design |
| Work nature mix | Mechanical 10; Judgment 0 (rows in the to-be breakdown). This skill has 10 Mechanical steps, one of which waits for a person |
| Authority level | Does. It prepares and, after a person confirms, sends |
| Handoffs in | H20 |
| Handoffs out | H08, H13, H14, H19 |
| Human gate after | A person confirms recipients, content and timing before anything is sent. The artifact owner then reviews the package. Approver role: artifact owner |
| Used by | AG-04 Handoff keeper. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Turns approved work into a package the receiver can use without asking: versioned, dated, linked to its evidence, annotated and listing what is still open. It enables the receiver's decision about what to do with the work.

## 3. When to use

Use when a person has approved an artifact and it must pass to another stage, a person or a team.

Not for: the file format and the ten tests. Use s2-handoff-standard, which this skill follows. Not for detecting edits designers made in a design tool, use figma-handoff. Not for assembling a backlog, use 14-share-and-align-with-stakeholders.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Approved artifact, by file name, with status approved and the approver named | None. Internal, from the sending capability | Required | Stop and ask |
| Handoff register row for this handoff | The handoff ID being written | Required | Stop and ask |
| Decision log from the design review | H20 | Required for detailed design packages | Proceed and mark To verify |
| Evidence log and registers for linking: evidence/evidence-log.md, registers/ | None. Internal | Required for step 3 | Stop at step 3 and ask |
| Stories or jobs the screens serve | None. To verify where they are recorded | Required for step 4 | Stop at step 4 and ask |
| Check log for the screens | None. Internal | Optional | Proceed and list under Gaps |
| Recipients, the medium to send through and the comment window | None. To verify | Required for steps 8 and 9 | Stop and ask |
| Local config file: local-config.md (repository location, ID formats, recipients, comment window, medium) | None | Required | Stop and ask |
| Handoff template: handoff-template.md. Templates: templates/handoff-package-templates.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Confirm the artifact is approved. Check that its status is approved and that a named approver is recorded. If not, stop and tell a person. Never package a draft as if it were final.
2. **Mechanical.** Version and date the artifact. Set the version, the date, the changes since the prior version, and what it supersedes. For the information architecture or the design language system, also update ia-and-dls-current-version.md, so receivers can find the current version.
3. **Mechanical.** Link each item to its evidence. For each principle, register entry or claim, add the evidence item IDs from evidence/evidence-log.md. List items with no evidence under Gaps. Never remove an item to close a gap.
4. **Mechanical.** Annotate the artifact. For each screen or section, add a short note and link it to the story or job it serves, by ID. Call out accessibility needs, such as tab order and alt text, and put real content in the notes, not placeholders.
5. **Mechanical.** List the open issues: anything unresolved, deferred or flagged by a check, each with an ID and an owner role.
6. **Mechanical.** Record where each shared list lives, with its file name and version. Write the rule that other outputs cite items by ID and do not copy the lists.
7. **Mechanical.** Write the handoff file from the handoff template, following s2-handoff-standard. Fill the evidence table, the Gaps and open questions, and the decision the receiver must make. Set status draft. Save it as handoffs/H<ID>_<artifact>_v<version>.md.
8. **Mechanical.** Prepare the send. List the recipients, the content, the medium and the timing, including how long receivers have to comment before any review meeting. Then stop. A person must confirm all four before step 9.
9. **Mechanical.** After a person confirms, send through the medium named in the local config file. Give receivers the comment window set in step 8 before the review meeting. This skill names no sending tool. To verify which tool the team uses.
10. **Mechanical.** Record what was sent: date, recipients, medium, the version and the end of the comment window. Save it in handoffs/send-record.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Handoff file | H08, H13, H14 or H19, as the register row says | Markdown with YAML front matter | handoffs/ | H<ID>_<artifact>_v<version>.md |
| Annotated design documentation and handover pack | H19 | Markdown | design-docs/ | design-documentation.md, handover-pack.md |
| Open issues list | H19 | Markdown table | handoffs/ | open-issues.md |
| Updated version file (when the IA or design language system is packaged) | H14 | Markdown | process root | ia-and-dls-current-version.md |
| Send record | None. Internal | Markdown table | handoffs/ | send-record.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: file layout, how to word annotations, the order of open issues.
- Must not decide: approval, who receives the package, what is left out, when it is sent, or whether a gap is acceptable. Must not send before a person confirms.
- Escalate when: the artifact is not approved, the recipients or comment window are missing, a link is broken, an item has no evidence, or the question of a formal design review before handover is still open.
- Approver role: artifact owner. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: the package can be used without the author.
- [ ] Test 3, Traceable: every item links to evidence or is listed as a gap.
- [ ] Test 4, Single source: shared lists are cited by ID, with their location and version.
- [ ] Test 6, Owned and statused: approver role and status are present.
- [ ] Test 7, Honest about gaps: open issues and missing evidence are listed.
- [ ] Test 8, Versioned and dated: version, date and changes since the prior version are present.
- [ ] Test 9, Findable and readable: fixed file names, stable IDs.
- [ ] Nothing was sent before a person confirmed recipients, content, medium and timing.
- [ ] A send record exists.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Handover folded into detailed design, with no clear approval and no comment time | Breakdown gap note on H7: "The slide folds handover into this step and step 8 is an added step. Is there a formal design review before handover, who holds approval, and do developers comment first?" | Step 1 stops on an unapproved artifact. Steps 8 and 9 set and give a comment window. The review question is escalated |
| Registers shared with no rule on copying | Breakdown gap note on N5: "Do personas, empathy maps, the blueprint and the jobs matrix cite the register by ID, or does each keep its own pain point list?" | Step 6 |
| Nobody owns the principles or knows where they are checked again | Breakdown gap note on X5: "Who owns the principles, and where are they checked again later?" | Step 7 names the owner role in the handoff file |
| Steps 6 and 7 use different versions of the design language | Breakdown gap note on D6: "Who owns changes after release? Steps 6 and 7 both use it, so which version does each use?" | Step 2 updates ia-and-dls-current-version.md |
| Developers build from the wrong design | Team answer, 2026-10-12: developers build from the step 8 signed-off design, but the step 7 handoff row H19 still sends the prototype | Step 2 states the version and its approval. The mismatch with H19 is escalated |
| An unreviewed send | Hypothesis from the roster design check | Steps 8 and 9 separate the preparation from the send |

## 10. Principles applied

- Prioritise human control: nothing is sent until a person confirms, and the send is recorded.
- Build trust through visible evidence: every item links to its evidence, and gaps are listed.
- Prevent errors: the skill refuses an unapproved artifact and names the version.

## 11. References

- handoff-harness.md and handoff-template.md, read in full: the ten tests and the file standard this skill follows.
- NN/g "Creating Design Specs for Development", read about 70 percent: real content in place of placeholders, accessibility needs called out, and time for developers to comment before the review meeting.
- figma-handoff SKILL.md, first 30 lines read: it detects and harmonises designer edits in the design tool, which is a different job.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-13: N5 (steps 2 to 4), X5 (steps 2 and 3), I6 (step 3) and H7 (steps 1 to 4).
- Standard practice, not checked against a source: the ten step order, and the rule to stop before sending.
- Supporting file: templates/handoff-package-templates.md.
