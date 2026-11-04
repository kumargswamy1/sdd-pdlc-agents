---
name: 07-map-the-current-state
description: Maps how a user does something today, by phase, with what they do, think and feel, the pain points, the highs and lows and what supports each phase behind the scenes. Use when personas and evidence are ready. Not for the future journey, use 09-ideate-the-future-state.
allowed-tools: Read Grep Glob Write
---

# 07. Map the current state

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 07, CAP-07 Map the current state |
| Phase or scope | Define (the map is built in the as-is part of the process, and the work leans on Discover outputs) |
| Work nature mix | Mechanical 4; Judgment 4 (rows in the to-be breakdown, counting each as-is step). This skill has 5 Mechanical steps and 4 Judgment steps, because it adds a final write step |
| Authority level | Drafts. It fills the map from evidence. People choose the scope, mark highs and lows, and validate |
| Handoffs in | None. Inputs come from other skills and are internal |
| Handoffs out | H08 |
| Human gate after | Researcher reviews the drafts, then people decide each Judgment step and validate the blueprint with participants and experts. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Shows the user's current experience as a team can check it: what they do, think and feel, where it hurts, and what supports each phase. It enables the decision about where the experience most needs to change.

## 3. When to use

Use when personas, the evidence log and the pain point register exist, and a person has asked for a current-state map or blueprint.

Not for: designing the future journey. Use 09-ideate-the-future-state. Not for drawing out themes and needs, use 06-draw-out-insights-and-needs.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Personas: personas/persona-<segment-slug>.md | None. Internal, from 06-draw-out-insights-and-needs | Required | Stop and ask |
| Jobs-to-be-done matrix: jobs/jobs-to-be-done-matrix.md | None. Internal | Required for step 1 | Stop and ask |
| Objectives | None. To verify where they are recorded | Required for step 1 | Stop and ask |
| Evidence log: evidence/evidence-log.md | None. Internal, from 05-organise-the-evidence | Required | Stop and ask |
| Empathy maps: empathy-maps/empathy-map-<persona-slug>.md | None. Internal | Required for step 4 | Proceed and use evidence items only |
| Pain point register: registers/pain-point-register.md | None. Internal | Required for step 4 | Stop at step 4 and ask |
| Subject matter expert and stakeholder input, with policy and system documents | None. Step 2 of the main process is optional | Optional | Proceed. Mark the backstage layer Assumption |
| Participants and experts, to validate the blueprint | None. People | Required for step 8 | Stop and ask |
| Local config file: .github/templates/local-config.md (language rules, whether product names may appear, ID formats, approver roles) | None | Required | Stop and ask |
| Templates: templates/journey-templates.md | None | Required | Stop and ask |

## 5. Method

Write what the user does and experiences, never screens, buttons or other interface elements. Every cell holds one answer and cites item IDs. Doing entries are Evidence. Thinking and feeling entries are Inference. Refer to the pain point register by ID. Never copy its text.

1. **Judgment.** Propose the journey scope. Options to produce: two or three candidate scopes, each a persona, a journey, its trigger (where it starts) and its outcome (where it ends). Criteria: the persona's main jobs, the objectives, how much evidence exists, a clear trigger and a clear outcome. A person chooses and agrees the scope with the others. Save in journeys/journey-scope.md.
2. **Mechanical.** Lay out the phases and what the user does in each. Cluster similar entries, order them as they happen, and draw rough columns, one per phase. Name each phase in the user's words, as the names become clear, not in the organisation's words. Save in journeys/stage-action-grid.md.
3. **Mechanical.** Mark the touchpoints and the tools used in each phase. Name tools by type, such as spreadsheet, email or paper form, unless the local config file allows product names. Add to journeys/stage-action-grid.md.
4. **Mechanical.** Add what users think and feel in each phase, from items of Kind thought and felt and from the empathy map. Add the pain points by register ID. List each phase with no thinking or feeling entries as a blank area, a place where the team still needs to learn more. Save as journeys/as-is-journey-map.md.
5. **Judgment.** Propose the highs and lows. Options to produce: for each phase, labelled as a high, a low or neither, with the items behind it. Criteria: how strongly the items show positive or negative feeling, how many participants show it, whether pain point IDs apply. A person decides which areas to circle and label.
6. **Mechanical.** Add the roles, systems, rules and handoffs that support each phase, from expert and stakeholder input and from policy and system documents. Note what information passes at each handoff and what context is lost. If no expert input exists, tag the layer Assumption and say so. Save as journeys/as-is-journey-blueprint.md.
7. **Judgment.** Prepare the walk-through. Options to produce: a playback that names what the team is certain of (Evidence entries) and where gaps remain (Inference entries, Assumption entries and blank areas), and the claims to check with participants and experts. Criteria: each claim cites items, and each gap is listed. People walk through the blueprint with participants and experts.
8. **Judgment.** Propose corrections. Options to produce: for each error or gap found, correct the entry, keep it and mark it open, or remove it, with the evidence. Criteria: supported by an item or by what a participant or expert said, consistent with the register. A person decides. Save the corrected map as journeys/as-is-journey-blueprint-validated.md and record the signer role, the date and the refresh trigger.
9. **Mechanical.** For every output, write the evidence table and the Gaps and open questions section. List what was not checked. Set status draft until the approver signs.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Journey scope statement | None. Internal | Markdown | journeys/ | journey-scope.md |
| Stage by action grid | None. Internal | Markdown table | journeys/ | stage-action-grid.md |
| Annotated as-is journey map | None. Internal | Markdown table | journeys/ | as-is-journey-map.md |
| As-is journey blueprint | None. Internal | Markdown table | journeys/ | as-is-journey-blueprint.md |
| Validated as-is journey blueprint | H08 | Markdown table | journeys/ | as-is-journey-blueprint-validated.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to cluster and order entries, the wording of cells from the items, the layout.
- Must not decide: the journey scope, which areas are highs or lows, whether the blueprint is correct, who signs it, or how often it is refreshed. Must not fill a cell with an invented entry.
- Escalate when: a cell cannot be traced to an item, the pain points disagree with the register, the backstage layer has no expert input, an input is missing, or the scope is disputed.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every cell cites item IDs and an evidence tag.
- [ ] Test 4, Single source: pain points are cited by register ID and not copied.
- [ ] Test 6, Owned and statused: signer role, date and status are present.
- [ ] Test 7, Honest about gaps: blank areas and Assumption entries are listed.
- [ ] Test 8, Versioned and dated: version, date and refresh trigger are present.
- [ ] One answer per cell.
- [ ] Phases are named from the user's view.
- [ ] No screen, button or other interface element is named.
- [ ] A playback lists what is certain and where gaps remain.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Nobody agrees the scope before mapping | Breakdown gap note on B1: "Who agrees the scope before mapping starts?" | Step 1 offers options, and a person chooses and agrees |
| Phases named from the organisation's view | Breakdown gap note on B2: "Are stages named from the user's view or the organization's view?" | Step 2 names phases in the user's words |
| Pain points that differ from the shared list | Breakdown gap note on B3: "Do the pain points match the list used in personas and empathy maps?" | Step 4 cites the register by ID |
| A backstage layer built on team guesses | Breakdown gap note on B4: "Is the backstage layer based on expert input or on team guesses? The slide shows no stakeholder interview step." | Step 6 tags the layer Assumption when no expert input exists |
| No sign-off or refresh | Breakdown gap note on B5: "Who signs it off, and how often is it refreshed?" | Step 8 records the signer and the refresh trigger |
| The map names interface elements | Existing rule in design-journeys: journeys are technology and interface agnostic | The rule at the head of the method, and step 3 names tools by type |
| Touchpoints and tools versus agnostic language | Conflict: the breakdown asks for tools used, and design-journeys bans interface references | Step 3 names tools by type unless the local config file allows product names. To verify with the team |

## 10. Principles applied

- Build trust through visible evidence: every cell cites items, and the playback separates what is certain from what is not.
- Prioritise human control: people choose the scope, mark highs and lows, and validate.
- Start simple: one map per scope, with the backstage layer added only where expert input exists.

## 11. References

- IBM Enterprise Design Thinking Toolkit, As-is Scenario Map (August 2018), read in full (11 pages): rows for phases, doing, thinking and feeling, one answer per note, clusters named as phases become clear, highs and lows circled and labelled, blank areas where more learning is needed, and a playback of what is certain and where gaps remain. Source: ibm.com/downloads/documents/us-en/137a1e2551dbac29.
- design-journeys SKILL.md, read in full (198 lines). Kept: stages with actions, thoughts, feelings and pain points, the service blueprint lanes (frontstage, backstage, support, physical evidence), the agnostic language rules, and the rule to note what context is lost at each handoff. Dropped: opportunities and task flows, which belong to the future state or have no breakdown rows, and project paths and sync scripts. Conflict: it treats the current and future journey as one map, and the breakdown separates them.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-07: B1, B2, B3, B4 and B5.
- Standard practice, not checked against a source: the options and criteria in steps 1, 5, 7 and 8.
- Supporting file: templates/journey-templates.md.
