---
name: 09-ideate-the-future-state
description: Redraws the journey with prioritised features in place, shows which pain each change addresses, and consolidates workshop ideas into a manageable, evidence-linked feature list. Use when the validated current-state map exists. Not for ranking features, use 10-prioritise.
allowed-tools: Read Grep Glob Write
---

# 09. Ideate the future state

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 09, CAP-09 Ideate the future state |
| Phase or scope | Define |
| Work nature mix | Mechanical 5; Judgment 1 (rows in the to-be breakdown, counting each as-is step). This skill has 7 Mechanical steps and 1 Judgment step, because it adds a guard step and a final write step |
| Authority level | Drafts. It redraws and lists. A person decides what merges or drops |
| Handoffs in | H13 |
| Handoffs out | H11, H12 |
| Human gate after | Researcher reviews the redraw and the links, and a person decides which ideas merge or drop. Approver role: research lead |
| Used by | None. A person leads this work, and an agent may prepare material. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Shows how the user's journey changes once the prioritised features exist, ties every change to the pain it fixes, and reduces the pile of ideas to a feature list the team can test. It enables the decision about which features go into concept testing.

## 3. When to use

Use when the validated current-state blueprint exists and the story mapping workshop has produced prioritised features, and again when ideas from workshops must be consolidated into features.

Not for: deciding which features matter most. Use 10-prioritise. Not for mapping today's journey, use 07-map-the-current-state.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Validated as-is blueprint: journeys/as-is-journey-blueprint-validated.md | None. Internal, from 07-map-the-current-state | Required | Stop and ask |
| Prioritised features and effort estimates from the story mapping workshop | None. Step 4 of the main process is not broken down. To verify where it is recorded | Required for step 2 | Stop and ask |
| Ideas from workshops | None. To verify | Required for step 5 | Stop and ask |
| Experience principles | H13 | Optional | Proceed and mark To verify |
| Pain point register: registers/pain-point-register.md | None. Internal | Required for step 3 | Stop at step 3 and ask |
| Jobs-to-be-done matrix: jobs/jobs-to-be-done-matrix.md | None. Internal | Required for step 7 | Stop at step 7 and ask |
| Local config file: local-config.md (feature cap, ID formats, language rules, approver roles) | None | Required | Stop and ask |
| Templates: templates/future-state-templates.md | None | Required | Stop and ask |

## 5. Method

Write what the user does and experiences, never screens or other interface elements. Every change and feature cites IDs. Refer to the pain point register by ID and never copy its text.

1. **Mechanical.** Check the inputs. List the prioritised features, the phases of the validated blueprint, and any input that is draft or missing. If the blueprint is not validated, stop and tell a person.
2. **Mechanical.** Redraw the journey with the prioritised features in place. Keep the phases of the validated blueprint. For each phase, place the features that change it, and label the phase unchanged, changed, removed or merged. Keep one answer per cell. Save as journeys/to-be-journey-blueprint.md.
3. **Mechanical.** Show which pain each change addresses. For each change, cite the pain point IDs from the register. List every change with no pain point as unlinked. Never invent a pain point to close a gap.
4. **Mechanical.** Remove or merge steps. List each step the features make unnecessary and each pair of steps that collapses into one, with the feature that causes it and the reason. Never remove a step silently. Save the list in journeys/to-be-changes.md.
5. **Judgment.** Propose a manageable set of features from the workshop ideas. Options to produce: for each cluster of related ideas, merge into one feature, keep apart, or drop, with the ideas involved. Criteria: serves a pain point or job, fits the experience principles, keeps the total within the feature cap in the local config file. A person decides what merges or drops. Keep the dropped ideas on file with the reason.
6. **Mechanical.** Drop duplicates. Remove an idea only when its wording or feature ID is identical to another's, and list each removal. Near duplicates go to step 5, because a person decides those.
7. **Mechanical.** Have this step done by a person, or by a separate run whose output a person reviews, and not by the run that did steps 5 and 6. Name who did it. Link each feature to the pain point or job it serves, by ID. List every feature with no link as unlinked. Never delete a feature to close a gap.
8. **Mechanical.** Write the high level feature list and the evidence tables. Add the Gaps and open questions section and a list of what was not checked. Set status draft. Save as features/feature-list.md.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| To-be journey blueprint | H11, H12 | Markdown table | journeys/ | to-be-journey-blueprint.md |
| Changes, removals and merges | None. Internal | Markdown table | journeys/ | to-be-changes.md |
| High level feature list | None. Internal, read by 11-test-concepts | Markdown table | features/ | feature-list.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to lay out the redraw, how to word a change, which exact duplicates to remove.
- Must not decide: which ideas merge or drop, which features exist, or whether a step may be removed. Must not run the linking step on features it drafted.
- Escalate when: a change has no pain point, a feature has no link, the blueprint is not validated, the feature count exceeds the cap, or a feature names an interface element.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every change cites pain point IDs, and every feature cites a pain point or job.
- [ ] Test 4, Single source: registers are cited by ID and not copied.
- [ ] Test 7, Honest about gaps: unlinked changes, unlinked features and dropped ideas are listed.
- [ ] Test 8, Versioned and dated: version and date on every file.
- [ ] No step was removed without a listed reason.
- [ ] Step 7 was done by a person, or by a separate run a person reviewed, and not by the run that did steps 5 and 6.
- [ ] No screen, button or other interface element is named.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Changes that fix no known pain | Breakdown gap note on B6: "Is every change tied to a pain point it fixes?" | Step 3 cites register IDs and lists unlinked changes |
| Features with no evidence, and no clear owner of merge decisions | Breakdown gap note on C1: "Is each feature linked to evidence, and who decides what gets merged or dropped?" | Step 7 links every feature. Step 5 leaves the decision to a person |
| Ideas dropped with no record | Hypothesis from how consolidation works | Step 5 keeps dropped ideas on file with the reason |
| Near duplicates removed by the skill | Hypothesis from the roster design check | Step 6 removes exact duplicates only |
| The linker links its own features | Hypothesis from the roster design check | Step 7 is done by a person or a reviewed separate run |

## 10. Principles applied

- Build trust through visible evidence: each change and each feature shows the IDs behind it.
- Prioritise human control: people decide what merges or drops, and nothing is removed without a listed reason.
- Prevent errors: duplicate removal is limited to identical items.

## 11. References

- design-journeys SKILL.md, read in full (198 lines). Kept: stages, the opportunities field and the rule to note what context is lost at each handoff. Dropped: task flows, which have no breakdown rows. Conflict: it treats the current and the future journey as one map, while the breakdown separates them.
- design-stories SKILL.md, read in full (276 lines). Not carried: backbone, walking skeleton and release slices, which belong to the story mapping workshop. The breakdown has no rows for that workshop. To verify who owns it.
- IBM Enterprise Design Thinking Toolkit lists the To-be Scenario Map (one line description read, as recorded in the breakdown). The To-be Scenario Map deck itself was not read, so no output is checked against it.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-09: B6 and C1.
- Standard practice, not checked against a source: the options and criteria in step 5.
- Supporting file: templates/future-state-templates.md.
