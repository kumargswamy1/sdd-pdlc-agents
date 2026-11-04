---
name: 15-structure-the-experience
description: Builds the experience principles and the information architecture, from candidate qualities to a tested structure, each traced to evidence. Use when the future-state journey exists. Not for visual style, use 16-define-the-design-language.
allowed-tools: Read Grep Glob Write
---

# 15. Structure the experience

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 15, CAP-15 Structure the experience |
| Phase or scope | Design in the capability list. Run at step 5 of the main process, in the Define phase |
| Work nature mix | Mechanical 8; Judgment 18 (rows in the to-be breakdown, counting each as-is step). This skill has 8 Mechanical steps and 18 Judgment steps, because it groups steps and adds a guard step and a final write step |
| Authority level | Drafts. It collects, lists and maps. People decide every grouping, name, principle and structure |
| Handoffs in | H11 |
| Handoffs out | H13, H14 |
| Human gate after | A person decides each Judgment step. A researcher or designer reviews each agent step. A person confirms before the findability test runs. Approver role: design lead |
| Used by | AG-03 Experience agent. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Sets the rules for how the experience must feel and behave, and the structure that organises its content, both traced to evidence. It enables the decisions about what to design and how people will find their way.

## 3. When to use

Use when the future-state blueprint and feature list exist and a person has asked for experience principles or an information architecture.

Not for: colour, type, components or content rules. Use 16-define-the-design-language. Not for testing a prototype, use 18-test-usability. This skill covers two outputs that may later need to split. To verify.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| To-be journey blueprint and prioritised features | H11 | Required | Stop and ask |
| Vision and objectives | None. To verify where they are recorded | Required for step 2 | Stop and ask |
| Pain point and user need registers: registers/ | None. Internal | Required for step 2 | Stop and ask |
| Jobs-to-be-done matrix: jobs/jobs-to-be-done-matrix.md | None. Internal | Required | Stop and ask |
| Known constraints and dependencies | None. Step 2 of the main process is optional | Optional | Proceed and write that none were recorded |
| Existing systems and content | None. To verify | Optional | Proceed and list under Gaps |
| A real screen or flow, to test principles on | None. To verify | Required for step 8 | Stop at step 8 and ask |
| Card sort or interview data on how users group things | None | Optional | Proceed. Mark the grouping Assumption |
| Stakeholders, for agreement | None. People | Required for steps 10 and 25 | Stop and ask |
| Local config file: .github/templates/local-config.md (principle pattern, content standard, ID formats, approver roles, success rate for findability) | None | Required | Stop and ask |
| Templates: templates/structure-templates.md | None | Required | Stop and ask |

## 5. Method

Every candidate, principle, item and screen cites IDs. Experience principles are made here and nowhere else.

### Part A: experience principles

1. **Mechanical.** Check the inputs. List each source and mark any that is draft or missing. If a source is skipped for lack of time, say so under Gaps.
2. **Mechanical.** Collect what each source implies about how the experience must feel and behave. For each input, write each implied quality as one candidate, cited by source ID. Evidence tag: Inference. Save as principles/candidate-qualities.md.
3. **Judgment.** Group the candidates. Options to produce: clusters, each with its candidates. Criteria: shared meaning, and evidence IDs behind every candidate. A person decides.
4. **Mechanical.** Remove duplicates. Remove a candidate only when its wording is identical to another's, and list each removal. Near duplicates stay for step 3 and step 5.
5. **Judgment.** Test each cluster against the evidence. Options to produce: keep, reword or cut each cluster, with the evidence that supports it. Criteria: evidence meets the threshold in the local config file, and the theme is not opinion. A person decides. Save as principles/clustered-themes.md.
6. **Judgment.** Write the principle statements in one consistent pattern. Options to produce: two wordings of each principle in the pattern from the local config file. Criteria: one pattern throughout, short, specific, able to reject a design. A person decides.
7. **Judgment.** Add a reason and an example to each principle. Options to produce: a reason citing evidence IDs, and an example of what the principle means in practice, taken from a real flow. Criteria: the reason cites evidence, the example is concrete. A person decides.
8. **Judgment.** Apply each principle to a real screen or flow. Options to produce: for each principle, meets, breaks or unclear, with the feature of the example behind it. Criteria: the verdict can be defended from the example. A person decides.
9. **Judgment.** Cut any principle that cannot say no to a design. Options to produce: keep, rewrite or cut each principle, with one design the principle would reject. Criteria: at least one plausible design is rejected. A person decides.
10. **Judgment.** Agree the final set with stakeholders. Options to produce: the final set, a playback of the evidence behind each principle, the owner role and where the set is checked again. Criteria: every principle has evidence, an owner and a place where it is checked. People agree. Save as principles/experience-principles.md.

### Part B: information architecture

11. **Mechanical.** List every piece of content and every function the experience needs, from the to-be blueprint and prioritised features, and note the source and owner of each. Mark content that does not exist yet as having no owner. Save as ia/content-function-inventory.md.
12. **Judgment.** Mark what to keep, change or drop. Options to produce: a choice for each item, with the job it serves. Criteria: serves a job, is in scope. A person decides.
13. **Judgment.** Group the items by how users think, not by how the organisation is structured. Options to produce: groupings from card sort or interview data, with the data behind each. Criteria: matches users' mental models, evidence cited. A person decides, including when users and stakeholders disagree.
14. **Judgment.** Set the hierarchy and depth. Options to produce: two or three hierarchies, with how many steps each task takes. Criteria: key tasks stay reachable in few steps, groups are balanced. A person decides.
15. **Judgment.** Agree one name for each concept. Options to produce: candidate names in the users' words, with where the users used them. Criteria: users' words, one name per concept, consistent with the content standard. A person decides. Save as ia/taxonomy.md.
16. **Judgment.** Choose the navigation model: global, local and in-page. Options to produce: two or three models, with the tasks each one serves. Criteria: fits the structure and the main jobs per persona. A person decides.
17. **Judgment.** Write the labels in the users' words. Options to produce: two wordings per label, with the evidence for each. Criteria: users' words, checked against the content standard. A person decides.
18. **Judgment.** Set the search and wayfinding rules. Options to produce: rules for search, orientation and return, with the tasks they help. Criteria: a user can tell where they are and how to get back. A person decides. Save as ia/navigation-model.md.
19. **Mechanical.** List each screen and what it holds, and draw how screens connect for each key journey. Save as ia/sitemap.md, ia/screen-inventory.md and ia/flow-diagrams.md.
20. **Judgment.** Tie every screen to a story, job or pain point. Options to produce: for each screen, the candidate story, job or pain point IDs. Criteria: every screen traces to at least one, with no orphan screens. A person decides.
21. **Mechanical.** Stop and wait for a person to confirm the tasks, the participants and the timing. After confirmation, run a tree test or a closed card sort on the key tasks, using the task list drawn from the jobs matrix.
22. **Mechanical.** Record where people go wrong. Have this step done by a person, or by a separate run whose output a person reviews, and not by the run that did step 21. Name who did it. Save the results with participant IDs only.
23. **Judgment.** Revise the labels and structure. Options to produce: for each place people went wrong, a revision or none, with the result behind it. Criteria: the success rate meets the level in the local config file, and the revision does not break another task. A person decides.
24. **Judgment.** Check the structure against the experience principles and constraints. Options to produce: for each principle and constraint, meets, breaks or unclear, with the screen or flow behind it. Criteria: the verdict can be defended from the structure. A person decides.
25. **Judgment.** Agree the information architecture with stakeholders. Options to produce: the final structure, a playback of the evidence, the owner role and the sign-off role. Criteria: every screen traces to evidence, and the sign-off role is named. People agree.
26. **Mechanical.** Write the evidence table and the Gaps and open questions section for every file. List what was not checked. Set status draft until the approver signs. Packaging and sharing the final principles and architecture belong to 13-package-for-handoff.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Candidate qualities, with clustered themes | None. Internal | Markdown tables | principles/ | candidate-qualities.md, clustered-themes.md |
| Experience principles, final | H13, H14 | Markdown, one pattern, each with reason, example and evidence IDs | principles/ | experience-principles.md |
| Content and function inventory | None. Internal | Markdown table | ia/ | content-function-inventory.md |
| Taxonomy and navigation model | None. Internal | Markdown | ia/ | taxonomy.md, navigation-model.md |
| Sitemap, screen inventory and flow diagrams | H14 | Markdown | ia/ | sitemap.md, screen-inventory.md, flow-diagrams.md |
| Findability results and revised structure | None. Internal | Markdown | ia/ | findability-results.md |
| Information architecture, final | H14 | Markdown | ia/ | information-architecture.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to word candidates from sources, how to lay out the inventory, how to draw a flow from an agreed structure.
- Must not decide: any grouping, name, principle, hierarchy, navigation, label, screen link or revision, or whether a principle stays. Must not run the findability test without confirmation. Must not record test results with names.
- Escalate when: a principle has no evidence, a screen traces to nothing, users and stakeholders disagree on a grouping, findability falls below the agreed level, or a principle rejects no design.
- Approver role: design lead. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every principle and screen cites evidence or a story, job or pain point.
- [ ] Test 4, Single source: registers are cited by ID and not copied.
- [ ] Test 6, Owned and statused: owner role, signer role and status are present.
- [ ] Test 7, Honest about gaps: skipped inputs, content with no owner and failing tasks are listed.
- [ ] Test 8, Versioned and dated: version and date on every file.
- [ ] One pattern for every principle statement.
- [ ] Every principle can reject at least one design.
- [ ] No screen is an orphan.
- [ ] Step 22 was done by a person, or by a separate run a person reviewed, and not by the run that did step 21.
- [ ] Experience principles are written only in this skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Inputs skipped when time is short | Breakdown gap note on X1: "Which inputs are always used, and which are skipped when time is short?" | Steps 1 and 2 list every source used or skipped |
| Themes resting on opinion | Breakdown gap note on X2: "Is every theme linked to evidence, or only to opinion?" | Step 5 |
| Principles written in different patterns | Breakdown gap note on X3: "Is there a standard pattern for writing principles?" | Step 6 |
| Principles that always agree | Breakdown gap note on X4: "Can a principle ever reject a design, or are they all agreeable?" | Steps 8 and 9 |
| No owner and no place where principles are checked again | Breakdown gap note on X5: "Who owns the principles, and where are they checked again later?" | Step 10 |
| Inventory copied from the old system, content with no owner | Breakdown gap note on I1: "Is the inventory built from the to-be blueprint or copied from the old system? Who owns content that does not exist yet?" | Step 11 |
| Grouping by instinct | Breakdown gap note on I2: "Is user input used to group the content, or does the team group by instinct? Who decides when users and stakeholders disagree?" | Step 13 |
| Labels checked against nothing | Breakdown gap note on I3: "Who checks labels against the content standard, and which standard applies?" | Steps 15 and 17 name the standard in the local config file |
| Screens that trace to nothing, or story mapping done twice | Breakdown gap note on I4: "Does each screen trace to evidence? Step 7 also maps screens to user stories, so is the mapping done twice?" | Step 20 |
| Structure never tested apart from layout | Breakdown gap note on I5: "The slide shows no test of the structure. Concept testing uses lo-fi prototypes, so is structure ever tested apart from layout? What success rate is enough?" | Steps 21 to 23, and the success rate in the local config file |
| Principles filed and never used to judge the architecture | Breakdown gap note on I6: "Are experience principles used to judge the IA, or only filed? Who signs off?" | Steps 24 and 25 |
| Principles written in three places | Resolved 2026-10-12 against the to-be breakdown | The principles are made here only |

## 10. Principles applied

- Prioritise human control: 18 steps stop for a person, and the test and the send wait for confirmation.
- Build trust through visible evidence: every principle, item and screen cites its evidence.
- Prevent errors: duplicate removal is limited to identical wording, and the recording step is done by a person or a reviewed separate run.

## 11. References

- design-ia SKILL.md, read in full (203 lines). Kept: the screen inventory, navigation model, content hierarchy and taxonomy, and the rule that every screen traces to a story or flow, with no orphan screens. Dropped: the Figma bridge, BRD steps, project paths and sync scripts. Not carried: its three level content hierarchy, which has no breakdown rows. Conflict: it assumes story IDs that no capability produces now.
- design-discovery and design-governance SKILL.md: each also writes principles. The to-be breakdown is the source of truth, so principles are made here. Their principle sections are not carried. design-governance was read for its headings only.
- NN/g "Information Architecture vs. Sitemaps", read about 70 percent: IA work includes a content inventory and audit, taxonomy, structure planning with a sitemap, and research such as card sorting and tree testing.
- NN/g "Card Sorting vs. Tree Testing", read about 60 percent: card sorting generates ideas for structure, and tree testing evaluates a proposed structure.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-15: X1 to X5 and I1 to I6.
- Standard practice, not checked against a source: the options and criteria in the Judgment steps.
- Supporting file: templates/structure-templates.md.
