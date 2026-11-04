---
name: 11-test-concepts
description: Plans and records concept tests: proposes concepts, aligns them with a person, and on that person's instruction hands to 12-design-the-detailed-screens for a rapid prototype, then pilots, recruits and records. Use when features need user reaction. Not for analysis, use 19-analyse-test-results.
allowed-tools: Read Grep Glob Write
---

# 11. Test concepts

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 11, CAP-11 Test concepts |
| Phase or scope | Define |
| Work nature mix | Mechanical 6; Judgment 5 (rows in the to-be breakdown, counting each as-is step). This skill has 8 Mechanical steps and 7 Judgment steps, because it adds concept alignment, the instruction to prototype and the brief for 12-design-the-detailed-screens, and groups other steps |
| Authority level | Prepares. It proposes concepts and prepares the plan, the brief for the prototype, the pilot and the bookings. People choose what to test, align the concepts, instruct the prototype, set the criteria and run the sessions |
| Handoffs in | H07, H10, H13 |
| Handoffs out | None. Recordings and notes go to 05-organise-the-evidence |
| Human gate after | A person aligns the concepts and gives the instruction to prototype before any prototype is made, and confirms every booking and pilot before it happens. A researcher reviews the kit, then people decide each Judgment step. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.3, 2026-10-14, draft |

## 2. Purpose

Gets concepts that a person has aligned and instructed, as rapid prototypes built from the design system, in front of the right users with criteria fixed in advance, and captures what happens. It enables the decision about which features to take into detailed design.

## 3. When to use

Use when the feature list exists and the team needs users' reaction to concepts before detailed design. This skill and 12-design-the-detailed-screens work together: this skill proposes and aligns the concepts, and 12-design-the-detailed-screens builds the prototype only after the person's instruction.

Not for: reading or scoring the results. Use 19-analyse-test-results. Not for deciding what to do with the results, use 10-prioritise. Not for building the prototype, use 12-design-the-detailed-screens. Not for testing a hi-fi prototype for usability, use 18-test-usability.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| High level feature list: features/feature-list.md | None. Internal, from 09-ideate-the-future-state | Required | Stop and ask |
| Assumptions and open questions log | H07 | Required for step 2 | Stop at step 2 and ask |
| Risks | None. To verify where they are recorded | Optional | Proceed and mark To verify |
| To-be journey blueprint: journeys/to-be-journey-blueprint.md | None. Internal | Required for step 6 | Stop at step 6 and ask |
| Concept prototype, returned by 12-design-the-detailed-screens | None. Internal | Required for steps 10 and 11 | Stop and wait. Do not build a prototype in this skill |
| The person leading the work, to align the concepts and give the instruction | None. A person | Required for steps 7 and 8 | Stop and ask |
| Experience principles | H13 | Required for step 6 | Proceed and mark To verify |
| Personas | H10 | Required for step 12 | Stop at step 12 and ask |
| Participant pool, criteria and schedule | None. To verify | Required for steps 5 and 12 | Stop and ask |
| A colleague as pilot participant | None. A person | Required for step 11 | Stop and ask |
| Local config file: local-config.md (where raw recordings and contact details are kept, confirmation roles, approver roles) | None | Required | Stop and ask |
| Templates: templates/concept-test-templates.md | None | Required | Stop and ask |

## 5. Method

Participants appear by ID in every shared file. Contact details stay in one restricted file named in the local config file, and no other file holds them.

1. **Mechanical.** Check the inputs. List the features, the logged assumptions, the personas and the participant pool, and any input that is draft or missing. If a test plan or a set of success criteria already exists for this round, load it.
2. **Judgment.** Pick the riskiest assumptions and the features that carry them. Options to produce: assumptions ranked by risk from the log, each with the features that depend on it. Criteria: risk to the outcome if wrong, can a rough concept test it, written down before testing and not rebuilt afterwards. A person decides.
3. **Judgment.** Decide what the test must be able to show. Options to produce: for each chosen assumption, a hypothesis and the result that would confirm it and the result that would reject it. Criteria: observable in a session, set before any session. A person decides. Save as tests/test-scope.md.
4. **Judgment.** Define the goals and the success criteria. Options to produce: goals, the outcome levels (for example accepted, changed, not accepted) and the threshold for each feature. Criteria: set before the first session, stated so a script can check it, and tied to the hypotheses. A person decides and signs. After sign-off, change nothing in this version.
5. **Judgment.** Choose the participants, the method, the tasks or scenarios and the questions. Options to produce: participant groups matching the personas, two or three methods, tasks written in the user's words, and the questions. Criteria: each question has a task or hypothesis behind it, participants match the personas, the method can answer the question. A person decides. Save as tests/test-plan.md with the criteria from step 4.
6. **Mechanical.** Propose the concepts. For each feature that carries a chosen assumption, draft a concept proposal from the feature list, the to-be blueprint and the experience principles. Each proposal states the idea in plain words, the feature IDs it maps to, the user need or pain point behind it, the hypothesis it tests, and what a participant would need to be able to do to test it. Add no feature that is not on the feature list. Evidence tag: Inference. Save as tests/concept-proposals.md.
7. **Judgment.** Align the concept ideas with the person leading the work. Options to produce: for each proposal, approve, revise, hold or drop, with the hypothesis it serves and the effect on the test. Criteria: tests a chosen hypothesis, maps to a feature, fits the time and the number of concepts the test can carry. A person decides and records the date. In this skill, the user who gives instructions is the person leading the work. End users react to the concepts later, in the sessions.
8. **Judgment.** Give the instruction to prototype. Options to produce: for each approved concept, instruct now, hold, or send back for revision, with what the prototype must let a participant do. Criteria: the concept is approved in step 7, the test plan and success criteria are signed, the tasks it must support are known. The person states the concepts to prototype, what each must support and the date, in their own words. No prototype is made without this instruction. Save as tests/prototype-instruction.md, with the role of the person who gave it.
9. **Mechanical.** Prepare the brief for 12-design-the-detailed-screens, and hand over. Write tests/concept-prototype-brief.md from the signed instruction, the approved proposals, the test plan tasks and the feature and principle IDs. State that 12-design-the-detailed-screens builds the concept prototype from the design system, in its concept prototype mode, and that it starts only from the instruction. Stop until the concept prototype is returned.
10. **Mechanical.** Have this step done by a person, or by a separate run whose output a person reviews, and not by the run that did step 6. Name who did it. Record which concept maps to which feature, by ID, and check each concept prototype screen against the approved proposals. List every concept with no feature, every feature with no concept, and every prototype screen that is not in an approved proposal. Save as tests/concept-feature-map.md.
11. **Mechanical.** Prepare the dry session. Draft a pilot script from the test plan. Stop and wait for a person to confirm the colleague and the time. After confirmation, run the dry session with the colleague on the concept prototype, record where tasks were unclear or the prototype broke, and fix the task wording. Send any breakage back to 12-design-the-detailed-screens. Save the result as the test-ready kit in tests/test-ready-kit.md.
12. **Mechanical.** Find and screen participants who match the personas, and book the sessions. Work from the criteria in the test plan. Stop and wait for a person to confirm the recipients, the content and the timing. After confirmation, book. Give each participant an ID. Keep names and contact details only in the restricted file. Save the confirmed list by ID and the schedule in tests/participants-and-schedule.md.
13. **Judgment.** Prepare the facilitation. Options to produce: who facilitates, who observes, and the rule for who may intervene and when, with the reason for each. Criteria: independence from the people who designed the concepts, experience, and enough observers to record. A person decides, and a person facilitates. This skill does not facilitate. Because the concept prototype may look finished, the facilitation guidance must also say how to keep reactions on the idea and not the finish: tell each participant at the start that it is a concept with simulated content and that the idea is being tested, ask about the task and the idea before the look, and tag comments on appearance separately from comments on the concept.
14. **Mechanical.** Record the sessions and note the reactions, questions and confusion. Save recordings and notes with participant IDs only, in the raw data location named in the local config file. Only the evidence agent (AG-02) reads raw recordings, and only after a person has cleared them. Tag any comment about polish or appearance 'appearance' so it is kept apart from reactions to the concept. Hand them to 05-organise-the-evidence.
15. **Mechanical.** Write the evidence table and the Gaps and open questions section for every file. List what was not checked. Set status draft until the approver signs the criteria and the plan.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Test scope and hypotheses | None. Internal | Markdown | tests/ | test-scope.md |
| Test plan, with success criteria | None. Internal | Markdown | tests/ | test-plan.md |
| Concept proposals and the alignment record | None. Internal | Markdown table | tests/ | concept-proposals.md |
| Instruction to prototype, in the person's words | None. Internal. Starts 12-design-the-detailed-screens | Markdown | tests/ | prototype-instruction.md |
| Concept prototype brief for 12-design-the-detailed-screens | None. Internal | Markdown | tests/ | concept-prototype-brief.md |
| Concept to feature map | None. Internal | Markdown table | tests/ | concept-feature-map.md |
| Test-ready kit | None. Internal | Markdown | tests/ | test-ready-kit.md |
| Confirmed participants by ID, and schedule | None. Internal | Markdown | tests/ | participants-and-schedule.md |
| Recordings and session notes | None. Internal, read by 05-organise-the-evidence | Raw files | The raw data location in the local config file | By participant ID and session |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to lay out the plan, how to word a concept proposal and a pilot script, how to name files.
- Must not decide: which assumptions to test, which concepts are approved, the instruction to prototype, the success criteria, the participants, the method, who facilitates, or anything about a booking or pilot without confirmation. Must not build a prototype or hand over to 12-design-the-detailed-screens without the signed instruction. Must not add features to a concept. Must not hold participant contact details outside the restricted file.
- Escalate when: success criteria would be set after a session, a concept has no feature, a prototype screen is not in an approved proposal, a prototype was started without the instruction, participant criteria cannot be met, access is unconfirmed, or a recording contains sensitive content.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 2, Decision led: the plan names the decision the test supports.
- [ ] Test 3, Traceable: every hypothesis cites an assumption ID and every concept cites a feature ID.
- [ ] Test 6, Owned and statused: signer role, date and status are present.
- [ ] Test 7, Honest about gaps: unlinked concepts, unconfirmed access and skipped pilots are listed.
- [ ] Test 8, Versioned and dated: success criteria dated before the first session.
- [ ] Concept proposals were aligned with the person leading the work, and the instruction to prototype is recorded and dated before any prototype was made.
- [ ] Step 10 was done by a person, or by a separate run a person reviewed, and not by the run that did step 6.
- [ ] Every prototype screen is in an approved proposal.
- [ ] No booking or pilot happened before a person confirmed it.
- [ ] No participant name or contact detail appears outside the restricted file.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Assumptions rebuilt after the test | Breakdown gap note on C2: "Are assumptions written down before testing, or reconstructed afterwards?" | Steps 2 and 3 fix them first |
| Success criteria set after the test | Breakdown gap note on C3: "Are success criteria set before the test or after?" | Step 4 requires sign-off before the first session |
| No agreed standards for the concept prototype | Breakdown gap note on C4 (row removed 2026-10-14): "Which standards (content, accessibility, design language) apply at lo-fi, and who checks them?" | The prototype is built by 12-design-the-detailed-screens from the design system, so the design language standards apply. How much of the accessibility standard applies to a rapid prototype is To verify |
| A prototype built before the concepts were aligned | Team instruction, 2026-10-14: concept ideas are proposed and aligned first, then the person instructs the prototype | Steps 7 and 8 require approval and a recorded instruction before step 9 |
| Pilot skipped under time pressure | Breakdown gap note on C5: "Is a pilot always run, or skipped under time pressure?" | Step 8 is a required step with a person's confirmation |
| Participants who do not match the personas | Breakdown gap note on C6: "How are participants recruited, and do they match the personas?" | Step 9 screens against the plan criteria |
| Unclear roles in the session | Breakdown gap note on T1: "Who facilitates, who observes, and who is allowed to intervene?" | Step 10 sets them, and a person decides |
| A concept with no feature, or an invented feature | Hypothesis from the roster design check | Steps 6 and 10 |
| Contact details leaking into shared files | Hypothesis from the roster design check | The rule at the head of the method |

## 10. Principles applied

- Prioritise human control: people choose what to test, align the concepts, give the instruction to prototype, set the criteria and facilitate, and nothing is booked or piloted without a person's confirmation.
- Prevent errors: criteria are fixed before the first session, and identity data stays in one restricted file.
- Build trust through visible evidence: every hypothesis and concept cites its assumption or feature.

## 11. References

- design-wireframe SKILL.md, read in full (197 lines). Kept: review framing that asks about structure and flow, and stakeholder feedback captured in a structured way. Conflict: it builds deliberately rough, disposable wireframes from canvas briefs. The team instruction of 2026-10-14 is that concept tests use rapid prototypes built from the design system by 12-design-the-detailed-screens, so the roughness rule is not carried. The to-be breakdown row C4 still says low fidelity. To verify.
- design-validation SKILL.md, read in full (293 lines). Kept: the test plan structure with objectives, participants, method, metrics and an analysis plan. Dropped: heuristic evaluation, scenario scripts and the post-build checklist.
- design-research SKILL.md (Phase A), read in full (229 lines). Kept: participant criteria from personas and stated success thresholds.
- IBM Enterprise Design Thinking Toolkit lists Assumptions and Questions, Research Plan, Paper Prototypes and Wireframes (one line descriptions read, as recorded in the breakdown). The decks were not read.
- NN/g "Research Plans: Organize, Document, Inform", read about 70 to 75 percent: a plan holds goals, participants, method and procedure, and documents.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-11: C2, C3, C5, C6 and T1. Row C4 was removed on 2026-10-14.
- Standard practice, not checked against a source: the options and criteria in steps 2 to 5, 7, 8 and 13.
- Supporting file: templates/concept-test-templates.md.
