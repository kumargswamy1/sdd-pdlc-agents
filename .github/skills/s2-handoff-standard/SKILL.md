---
name: s2-handoff-standard
description: Defines what a good handoff file holds and how to write one: file name, front matter, evidence table, ten tests. Use when reading or writing a handoff between stages. Not for the work inside a stage, use the capability skill for that.
---

# S2. Handoff standard

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | S2, shared skill. Applies to every handoff in the register |
| Phase or scope | Cross cutting, every stage |
| Work nature mix | Mechanical 7; Judgment 1 |
| Authority level | Does (writes the file) and Checks (runs the ten tests). Never approves |
| Handoffs in | All handoffs in the handoff register |
| Handoffs out | All handoffs in the handoff register |
| Human gate after | The named approver in the file front matter confirms the acceptance checklist. Role: owner of the sending stage |
| Used by | AG-01, AG-02, AG-03 and AG-04, where they read or write handoffs. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

A handoff is the note one stage leaves for the next. A good one lets a reader with no chat history act on it, check its claims and know who approved it.

## 3. When to use

Use when a stage finishes work that another stage, a person or an agent will pick up, and when reading any handoff before acting on it.

Not for: producing the artifact itself. Use the capability skill. Not for packaging a set of finished work for release, use 13-package-for-handoff.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| The artifact to hand over, by file name | The handoff ID being written | Required | Stop and ask |
| Handoff register row for this handoff (from step, to step, decision, minimum contents) | The handoff ID being written | Required | Stop and ask |
| Handoff file template: handoff-template.md | None | Required | Stop and ask |
| Evidence log for the artifact | None | Required | Proceed and mark every claim To verify |
| Local config file: local-config.md (ID prefixes, approver roles, repository location) | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** Name the file `H<ID>_<artifact>_v<version>.md`, where the ID comes from the register and the artifact name is lowercase with hyphens. Save it in the shared repository location named in the local config file.
2. **Mechanical.** Fill the front matter: handoff ID, title, from step, to step (number and name, exactly as in the process file), version, date, changes (what changed since the prior version, or first version), status, author, approver and supersedes. Set status to draft. Leave the approver name blank unless a person has given it.
3. **Judgment.** Draft the summary. Options to produce: one summary of 150 words or fewer, and one alternative that leads with the decision requested. Criteria: names the decision the receiver must make, covers scope, reads cold. A person chooses.
4. **Mechanical.** In Contents, give the artifact or a link to it. Give every item a stable ID. Cite shared lists, such as pain points or user needs, by ID. Never copy a list.
5. **Mechanical.** Fill the evidence table: item ID, claim, source, evidence tag and confidence. Use the tags Evidence, Inference and Assumption. Use High, Medium or Low with one phrase why.
6. **Mechanical.** In Gaps and open questions, list what was not covered, who was missing from the evidence and what is unresolved. In Decision and next step, name the decision, who makes it and what follows.
7. **Mechanical.** Run the ten tests (section 8) and tick the acceptance checklist only for tests that pass. Do not tick the approver line. Only the approver does.
8. **Mechanical.** When reading a handoff, check the status first. Treat a draft as unapproved input. Report anything that fails a test instead of working around it.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Handoff file | The register ID of the handoff | Markdown with YAML front matter | Shared repository, per local config | H<ID>_<artifact>_v<version>.md |

Every handoff file has status draft until the approver signs off.

## 7. Authority and gates

- May decide: file name, section order within the template, which items need IDs.
- Must not decide: approval, the status approved, the decision the receiver makes, or whether a failing test is acceptable.
- Escalate when: the register row is missing, an evidence log is absent, a claim has no source, or two handoffs describe the same list.
- Approver role: owner of the sending stage. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: someone with no chat history can act on it.
- [ ] Test 2, Decision led: it names the decision and what is needed to make it.
- [ ] Test 3, Traceable: every claim has a source and an evidence tag.
- [ ] Test 4, Single source: shared lists are cited by ID and not copied.
- [ ] Test 5, Small front, deep back: the summary is 150 words or fewer and detail is linked.
- [ ] Test 6, Owned and statused: a named human approver and a status.
- [ ] Test 7, Honest about gaps: open questions, what was not covered and confidence.
- [ ] Test 8, Versioned and dated: version, date and what changed since last time.
- [ ] Test 9, Findable and readable: fixed file name pattern, stable IDs, Markdown with YAML front matter.
- [ ] Test 10, Checkable: an acceptance checklist a reviewer can tick.
- [ ] From and to steps match the process file exactly.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Receiver cannot tell what to decide | Main process file gap notes on steps 5 and 7: "Are they used later to judge designs, or only filed?" | Step 3 and test 2 require the decision to be named |
| Pain point, need and assumption lists copied and drifting | Breakdown gap note on the registers: "Do personas, empathy maps, the blueprint and the jobs matrix cite the register by ID, or does each keep its own pain point list?" | Step 4 and test 4 |
| Findings with no source | Breakdown gap note: "Can each entry be traced back to a quote or session?" | Step 5 and test 3 |
| Test 8 asks what changed since last time, but the template had no field for it | Handoff template, read in full | Resolved 2026-10-12: a changes field was added to the front matter, and step 2 fills it |
| Handoff files are paused | Team instruction, 2026-10-12 | Treat the template and register as draft |

## 10. Principles applied

- Build trust through visible evidence: steps 4 and 5 and test 3.
- Prioritise human control: status draft, approver is a person, steps 3 and 7.
- Start simple: one file, one template, ten tests.

## 11. References

- handoff-harness.md, read in full: the ten tests, the file standard and the evidence tags.
- handoff-template.md, read in full.
- Handoff register: sheet "Handoff register" in as-is-breakdown.xlsx, read in full.
- Standard practice, not checked against a source: the 150 word summary limit.
