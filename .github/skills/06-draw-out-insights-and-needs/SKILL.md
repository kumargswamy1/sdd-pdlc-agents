---
name: 06-draw-out-insights-and-needs
description: Turns tagged evidence into a product vision, experience principles, personas, empathy maps, need statements and jobs, each line citing evidence IDs. Use when the evidence log and pain point register are reviewed and ready for synthesis. Not for logging or tagging evidence, use 05-organise-the-evidence.
allowed-tools: Read Grep Glob Write
---

# 06. Draw out insights and needs

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 06, CAP-06 Draw out insights and needs |
| Phase or scope | Define |
| Work nature mix | Mechanical 13; Judgment 10 (rows in the to-be breakdown). This skill groups them into 10 Mechanical steps and 7 Judgment steps |
| Authority level | Drafts. It writes drafts and proposals. People decide |
| Handoffs in | None. Inputs are outputs of 05-organise-the-evidence and are internal |
| Handoffs out | H08 |
| Human gate after | Researcher reviews each chain of drafts, then people decide each Judgment step. Approver role: research lead |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Turns reviewed evidence into the shared pictures a team designs from: a product vision, experience principles, who the users are, what they think and feel, what they need and what they are trying to get done. It enables the decision about what the product should achieve, how it should feel, and which users, needs and jobs the work serves.

## 3. When to use

Use when the evidence log is reviewed, the pain point register exists, and a person has asked for personas, empathy maps, need statements or jobs. Build or refresh an empathy map directly after an observation session or before an important decision.

Not for: logging, tagging or numbering evidence. Use 05-organise-the-evidence. Not for deciding which jobs matter most, which is a human gate in 10-prioritise.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Evidence log: evidence/evidence-log.md | None. Internal, from 05-organise-the-evidence | Required | Stop and ask |
| Source index: evidence/source-index.md | None. Internal | Required | Stop and ask |
| Pain point register: registers/pain-point-register.md | None. Internal | Required for steps 9 to 12 | Stop at step 9. Run 05-organise-the-evidence first |
| Research plan: objectives, interview sample and participant mix | None. To verify where it is recorded | Required for step 1 | Stop and ask |
| Affinity themes from the interview notes | None. To verify | Optional | Proceed and mark To verify |
| Local config file: .github/templates/local-config.md (evidence threshold, ID formats, need statement pattern, feature word list, job statement pattern, rating scales, role wording rules) | None | Required | Stop and ask |
| Templates: templates/synthesis-templates.md | None | Required | Stop and ask |

## 5. Method

Every line you write cites item IDs from evidence/evidence-log.md. Tag each claim Evidence or Inference. Copy a quote by item ID. Never retype it, and never write a quote that is not in the log.

Draft the product vision and experience principles first, before any persona work. Then draft personas and need statements in one pass without stopping between them.

**0a. Mechanical.** Draft the product vision. Write a single statement (1–2 sentences) expressing what the product should achieve for users and why it matters. Derive it from the highest-confidence insights in the evidence log and from the project brief. Cite the evidence item IDs and brief sections that support it. Evidence tag: Inference. Write to `04_Insights/vision/product-vision.md`.

**0b. Mechanical.** Draft the experience principles. Write 3–5 principles expressing how the product should make users feel and how they should experience interacting with it. Each principle must include:
- A short name (2–4 words)
- A one-sentence description of what it means in practice
- The persona IDs, need statement IDs, or evidence item IDs that motivated it
- One "do / don't" pair to make it actionable

Derive principles from the product vision, persona goals, frustrations, and behavioural patterns in the evidence. Do not invent principles without evidence support. Evidence tag: Inference. Write to `04_Insights/vision/experience-principles.md`.

1. **Judgment.** Propose the persona brief. Options to produce: up to three segmentation bases (goals, behaviours or roles), each with the number of personas it would give and the decision those personas would support. Criteria: supports a named decision, fits the participant mix, keeps the number small. A person chooses the basis and caps the number. Save the choice in personas/persona-brief.md.
2. **Mechanical.** Group participants into segments by shared goals and behaviours, not demographics. Use only items in the evidence log. Give each segment a plain label. List the participant IDs behind it, and list participants who fit no segment under Gaps. Evidence tag: Inference. Save in personas/segments.md.
3. **Mechanical.** Draft one profile per segment from the persona template: goals, tasks, pain points, context, constraints, one scenario, each line cited. For the representative quote, copy a verbatim quote of Kind said from the evidence log, with participant ID and source. If none fits, write that no verbatim quote fits. Use a generic role description with no organisation or unit names. Save as personas/persona-<segment-slug>.md. Review the chain of steps 2 and 3 together.
4. **Judgment.** Prepare the persona review. Options to produce: a list of claims with no item ID, segments resting on fewer participants than the threshold in the local config file, groups the evidence suggests are missing, and wording that stereotypes (tag each Assumption). Criteria: evidence threshold from the local config file (default: two participants unless marked as an outlier), every claim traces to an item, no demographic stand-ins. People walk through the drafts with stakeholders and experts, check them, and revise. Save each revision as a new version.
5. **Judgment.** Propose which personas get an empathy map. Options to produce: one map per persona, one map for the whole group, maps for the personas with the most evidence. Criteria: evidence per persona, the decision the maps support, effort. A person decides. Save in empathy-maps/maps-to-build.md.
6. **Mechanical.** Place observations on a draft empathy map for each chosen persona. Says and Does come from items of Kind said and did, with verbatim quotes. Thinks and Feels come from items of Kind thought and felt, tagged Inference. Note every entry where items support different readings. Write one answer per entry. Put the persona label at the centre with a two sentence description of who they are and what they do. Cluster related entries within each quadrant. Note what each cluster suggests the user needs, tagged Inference. These notes feed step 10 and are not need statements. List each quadrant with no items or thin items under Blank areas, as places where the team still needs to learn more. Save as empathy-maps/empathy-map-<persona-slug>.md.
7. **Judgment.** Prepare the challenge of the readings. Options to produce: for each Thinks or Feels entry, keep, reword, move to Assumption, or drop. Criteria: number of items, how directly they show it, whether any item contradicts it. The team, including someone outside the research team where possible, challenges the readings and decides. Prepare a playback of what the team is certain of (Evidence entries) and where gaps remain (Inference entries and Blank areas). Label every entry that is an assumption, and every question for later inquiry or validation. Pass those labels to 02-surface-assumptions.
8. **Judgment.** Propose the gaps between what users say and what they do. Options to produce: candidate gaps, each citing a Says item and a Does item. Criteria: both sides are evidenced, more than one participant shows it (threshold from the local config file). People decide which gaps are real.
9. **Mechanical.** Name the pains and gains from the gaps people accepted. Cite item IDs. Compare each pain with registers/pain-point-register.md. Cite the register ID when it exists. List pains with no register entry as proposals for 05-organise-the-evidence. Do not create pain point IDs here. Save in empathy-maps/pains-gains-contradictions.md.
10. **Judgment.** Propose need statements. Cluster similar pain points first. Options to produce: for each cluster, two wordings in the same pattern, one in the user's own words and one more general. The pattern is: <user> needs a way to <need> so that they <benefit>. Criteria: every statement uses the same pattern, names a benefit, holds no feature word (a word naming the machine, such as a screen element or an action on one, is a clue that the idea is a feature, and the word list is in the local config file), cites the pain point IDs, rests on real observation and can be tested. People decide, with users or sponsor users in the room where possible.
11. **Judgment.** Propose merges of overlapping needs. Options to produce: merge, keep apart. Criteria: same outcome wanted, same persona. A person decides.
12. **Mechanical.** Give each agreed need a stable ID in the format from the local config file. Generate the ID. Never reuse one. Link each need to the pain point IDs behind it. Save in registers/user-need-register.md with the ID in the first column and the text in the second. Check that every need statement follows the pattern and holds no word from the feature word list. List failures under Gaps.
13. **Mechanical.** Pull the jobs: what users are trying to get done, in their own words, regardless of current tools. Cite item IDs. Put quotation marks only around verbatim words. Save in jobs/jobs-raw.md.
14. **Mechanical.** Phrase each job in the single pattern in the local config file. Default: "When <situation>, I want to <motivation>, so I can <outcome wanted>." Save in jobs/job-statements.md.
15. **Mechanical.** Group the jobs into main jobs and supporting jobs. Separate functional jobs from emotional and social jobs. Save in jobs/job-hierarchy.md.
16. **Mechanical.** Map jobs against personas. Record importance and how well today's process serves each job, using the scales in the local config file. Record the strength of evidence as the number of participants behind each job. If no scale exists, write To verify in those columns. Save as jobs/jobs-to-be-done-matrix.md. Review the chain of steps 13 to 16 together.
17. **Mechanical.** For every output, write the evidence table and the Gaps and open questions section from the templates. Under Gaps, list the new questions the work raised. Set status draft.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Product vision | None. Internal | Markdown | 04_Insights/vision/ | product-vision.md |
| Experience principles | None. Internal | Markdown | 04_Insights/vision/ | experience-principles.md |
| Persona brief | None. Internal | Markdown | personas/ | persona-brief.md |
| Segments | None. Internal | Markdown | personas/ | segments.md |
| Draft persona profiles | None. The reviewed set leaves through 05-organise-the-evidence (evidence index), under H08 | Markdown, one file per segment | personas/ | persona-<segment-slug>.md |
| Maps to build | None. Internal | Markdown | empathy-maps/ | maps-to-build.md |
| Empathy maps | None. Internal | Markdown | empathy-maps/ | empathy-map-<persona-slug>.md |
| Pains, gains and contradictions | None. Internal | Markdown table | empathy-maps/ | pains-gains-contradictions.md |
| User need register | H08 | Markdown table | registers/ | user-need-register.md |
| Raw jobs, job statements, job hierarchy | None. Internal | Markdown | jobs/ | jobs-raw.md, job-statements.md, job-hierarchy.md |
| Jobs-to-be-done matrix | H08 | Markdown table | jobs/ | jobs-to-be-done-matrix.md |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: how to word a draft from the items, the order of entries, labels taken from the evidence.
- Must not decide: the segmentation basis or number of personas, which personas get maps, which readings or gaps stand, the final need wording, merges, or whether a persona set is final. Must not invent a quote, a participant or an item.
- Escalate when: a claim has no item, fewer participants than the threshold support a segment, two items contradict, an input is missing, or a pain has no register entry.
- Review: the chain of steps 2 and 3, steps 6 and 9, step 12, and the chain of steps 13 to 16 are each reviewed once, after the last step in the chain.
- Approver role: research lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: every input named by file name.
- [ ] Test 3, Traceable: every line has item IDs and an evidence tag.
- [ ] Test 4, Single source: pains cite the register ID. No output keeps its own pain point list.
- [ ] Test 7, Honest about gaps: participants fitting no segment, thin segments and missing registers are listed.
- [ ] Test 9, Findable and readable: fixed file names, stable IDs, Markdown.
- [ ] Test 10, Checkable: reviewer can tick the checklist in the handoff template.
- [ ] Every quotation mark is a verbatim quote copied by item ID.
- [ ] Every need statement follows the one pattern, names a benefit and holds no feature word.
- [ ] Every empathy map has one answer per entry, a centre description, clusters within each quadrant, a Blank areas list, and a playback that lists what is certain, the assumptions and the questions for later validation.
- [ ] Every empathy map entry comes from the evidence items and not from the team's own view of the user.
- [ ] No segment rests on fewer participants than the threshold unless marked as an outlier.
- [ ] No organisation names or unit names appear.
- [ ] Every Judgment step lists options and criteria and names who decides.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Personas built because the process lists them | Breakdown gap note on P1: "Are personas built to support a specific decision, or because the process lists them? Who agrees the brief?" | Step 1 names the decision and a person agrees the brief |
| A segment resting on too few participants | Breakdown gap note on P3: "How many participants make a segment credible, and who decides the cut?" | Steps 2 and 4 apply the threshold from the local config file |
| Each author writes personas differently | Breakdown gap note on P4: "Is there a standard template, and does everyone use it the same way?" | Step 3 uses templates/synthesis-templates.md |
| Personas never checked with anyone | Breakdown gap note on P5: "Who validates, and are users ever consulted again before the personas are final?" | Step 4 prepares the review. Whether users are consulted again is To verify |
| One map for everyone, or one per persona, with no rule | Breakdown gap note on E1: "Is there one map per persona, or one for the whole user group?" | Step 5 |
| Readings never challenged | Breakdown gap note on E3: "Who attends, and does anyone outside the research team challenge the reading?" | Step 7 |
| Pains kept in a second list | Breakdown gap note on E4: "Do these pains feed the same pain point list used by personas and the journey blueprint?" | Step 9 cites the register |
| Needs written as features | Breakdown gap note on N3: "Are needs written from the user's view or from the product's features?" | Step 10 criteria and the step 12 check |
| Jobs written as features | Breakdown gap note on J1: "Are jobs described from the user's view or from the product's features?" | Step 13 |
| No standard job pattern | Breakdown gap note on J2: "Is there a standard statement pattern, and does everyone use it?" | Step 14 |
| No agreed rule for main jobs | Breakdown gap note on J3: "Who decides what counts as a main job?" | Step 15 drafts. A person decides at the review of the chain |
| Ratings with no basis | Breakdown gap note on J4: "How are importance and satisfaction rated, and from what evidence?" | Step 16 uses the local scale, or writes To verify |
| Drafting steps labelled Mechanical (personas, jobs) run without a decision between them | Hypothesis from the team relabelling in the breakdown | Chain review after the last step. Every line cites an item |
| An invented persona quote | Team rule: quotes must be verbatim from transcripts | Step 3 copies quotes by item ID |

## 10. Principles applied

- Build trust through visible evidence: every line cites item IDs, tagged Evidence or Inference.
- Prioritise human control: seven steps stop for a person, and all outputs are draft.
- Prevent errors: quotes are copied by ID and never retyped, and IDs are generated.

## 11. References

- design-user-models SKILL.md, read in full (264 lines). Kept: the persona, empathy map and jobs-to-be-done structures, and the job statement pattern "When [situation], I want to [motivation], so I can [outcome]". Dropped: the fictional persona quote, project paths and sync scripts. Not carried: behavioural dimensions and archetypes (its steps 5 to 7), because neither breakdown has steps for them. To verify whether they belong. Not carried: its four confidence tiers, replaced by High, Medium and Low from the handoff standard. To verify.
- IBM Enterprise Design Thinking Toolkit, Needs Statements (August 2018), read in full (11 pages, text extracted from the PDF): one prompt format for every statement, write needs and not features, ground them in defensible observed data, include users where possible, play back with new questions. Source: ibm.com/downloads/documents/us-en/137a1e253e5bac0b.
- IBM Enterprise Design Thinking Toolkit, As-is Scenario Map (August 2018), read in full (11 pages): one answer per sticky, blank areas where more learning is needed, a playback of what is certain and where gaps remain. Applies to the empathy map here, and to the journey map in 07-map-the-current-state. Source: ibm.com/downloads/documents/us-en/137a1e2551dbac29.
- IBM Enterprise Design Thinking Toolkit, Empathy Map (August 2018), read in full (14 pages, text extracted from the PDF): four quadrants (Says, Does, Thinks, Feels), the user at the centre with a name and brief description, one observation per note, clusters within each quadrant, imagining how the user's life shapes what they need, and a playback that labels assumptions and questions for later validation. Use it before an important decision or directly after an observation session, and remember that the team is not the user. Source: ibm.com/downloads/documents/us-en/137a1e2551dbac17.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-06: P1, P3, P4, P5, E1, E3, E4, N3, J1, J2, J3, J4.
- Standard practice, not checked against a source: the options and criteria in steps 4, 7 and 8.
- Supporting file: templates/synthesis-templates.md.
