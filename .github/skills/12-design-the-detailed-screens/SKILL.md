---
name: 12-design-the-detailed-screens
description: Prepares screens from the design system: readiness check first, existing designs compared, options, a reference record, wired flows. In concept mode an agent assembles a coded prototype for review. Use when the system is ready. Not for checking, use 17-check-designs-against-principles-and-standards.
allowed-tools: Read Grep Glob Write Edit Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/check_references.py *) Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/check_flows.py *) Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/tokens_to_css.py *) Bash(python3 ${CLAUDE_SKILL_DIR}/../16-define-the-design-language/scripts/build_dtcg.py *)
---

# 12. Design the detailed screens

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 12, CAP-12 Design the detailed screens |
| Phase or scope | Design |
| Work nature mix | Mechanical 5; Judgment 7 (rows in the to-be breakdown). This skill has 10 Mechanical steps and 9 Judgment steps, because it adds the design system readiness check, the existing design comparison, the reference record and the coded prototype build, which are not rows in the breakdown. To verify whether rows should be added |
| Authority level | Prepares. A person designs every screen. The skill checks readiness, compares, lists, flags, records references and wires. In concept prototype mode it also assembles the coded prototype from approved components, and a designer reviews it before testing |
| Handoffs in | H14, H16, H20, H22 in detailed design mode. None in concept prototype mode, which starts from a person's instruction |
| Handoffs out | H18, H19 |
| Human gate after | A person decides each Judgment step, and a designer reviews each agent step. Approver role: design lead |
| Used by | AG-03 Experience agent. Information only |
| Version and date | 0.4, 2026-10-14, draft |

## 2. Purpose

Makes every detailed screen and every rapid concept prototype a use of the design system, so screens are consistent with each other and with what already exists. It enables the decision that a prototype is ready for concept testing, or for checking and usability testing.

## 3. When to use

Use when a person asks to plan, compose or wire screens, and the design language system is approved and available. The skill has two modes. In concept prototype mode it builds a rapid prototype of concepts for testing, and it starts only from the signed instruction to prototype that 11-test-concepts records after a person has aligned the concept ideas. In detailed design mode it works from the validated features after concept testing.

Not for: setting the design language. Use 16-define-the-design-language. Not for checking screens against principles and standards, use 17-check-designs-against-principles-and-standards. Not for recording why a screen exists, use 22-record-decisions-and-rationale. This skill never originates a design, and no screen is designed outside the design system unless a person approves an exception. In concept prototype mode it assembles the coded prototype from decisions a person made and components the system already holds.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Design language system: the current-version file ia-and-dls-current-version.md, the foundations, the component library, the content standard, the accessibility standard and the DTCG token files in tokens/ | H14 | Required | Stop. Go to step 1 and step 2 |
| Information architecture and experience principles, at the versions named in ia-and-dls-current-version.md | H14 | Required | Stop and ask |
| Validated features and gaps, and the decision per feature | H16 | Required in detailed design mode | Stop and ask |
| In concept prototype mode: the instruction to prototype, the approved concept proposals and the brief: tests/prototype-instruction.md, tests/concept-proposals.md and tests/concept-prototype-brief.md | None. Internal, from 11-test-concepts and a person | Required in concept prototype mode | Stop. Never start a concept prototype without the signed instruction |
| Review feedback and decision log | H20 | Optional | Proceed and mark To verify |
| Usability findings from prior rounds | H22 | Optional | Proceed and note that none exist |
| Existing designs in any form: design files in any tool, screenshots or images, a live product, code prototypes or older versions, with a link, a connection or a view the person provides | None. A person provides | Required to ask in step 3. The answer may be none | Record that none exist and continue |
| Access to read them: only what the person provides for this purpose | None. A person | Required for step 3 | Stop and ask. Never work around a login or a block |
| Screen inventory: ia/screen-inventory.md | None. Internal, from 15-structure-the-experience | Required | Stop and ask |
| Subject matter experts, for content | None. People | Required for step 11 | Stop at step 11 and ask |
| Interaction rules, business rules and exception cases | None. To verify where they are recorded | Required for step 14 | Stop at step 14 and ask |
| Usability test tasks | None. To verify | Required for step 18 | Proceed. Wire the key flows only and mark To verify |
| Templates: templates/screen-templates.md | None | Required | Stop and ask |

## 5. Method

There are two modes. Concept prototype mode builds a rapid prototype of the approved concepts for testing, scoped to the concepts and tasks in the signed instruction and nothing more. Detailed design mode builds the screens for the features that testing validated. Every screen cites its story, job or pain point IDs, its evidence IDs, its principle IDs, and the design system version it was built against. In detailed design mode a person designs the screens in the team's design tool. In concept prototype mode a person makes the decisions in steps 8 to 15 and step 16 assembles them as a coded prototype. In both modes only the components, tokens and patterns of the approved design system are used. This skill prepares, assembles and checks, and it adds no screen, component, token or feature of its own. A rapid prototype may look finished and must meet the usability and accessibility standards of the design language system. Keep organisation names and product addresses out of every shared file.

### Part A: the design system and what already exists

1. **Mechanical.** Ask the person: "What output do you need from skill 12 — a Figma file, an HTML prototype, or both?" Wait for the answer before continuing. If **Figma**: ask for the Figma file URL and confirm the Desktop Bridge plugin is running (right-click Figma → Plugins → Development → Figma Desktop Bridge), then proceed using skills 25, 26, and 27 to set up the canvas and build components. If **HTML**: proceed with the HTML/CSS/JS prototype flow and write files to `prototype/` organised by section (e.g. `prototype/01-task-creation/`). If **both**: run the Figma path first, then the HTML path. Then check that the design system is ready and available — nothing else starts before that check. Confirm the mode. Concept prototype mode needs the signed instruction from 11-test-concepts, dated after the concepts were aligned. Detailed design mode needs the validated features in H16. If the needed input is missing, stop and tell a person. Read ia-and-dls-current-version.md and confirm the design language system has a version, a date and the status approved. Confirm the token files exist, and run `python3 ${CLAUDE_SKILL_DIR}/../16-define-the-design-language/scripts/build_dtcg.py --check <each token file>`. Confirm the component library, the foundations, the content standard and the accessibility standard exist and can be read. List what is missing, draft or unreachable. Write the result and the version used in screens/design-system-readiness.md. If the system is not ready, say that skill 16 must be run, or skill 21 if a release is pending, and go to step 2.
2. **Judgment.** Decide how to proceed when the system is not ready. If it is ready, record that and skip this step. Options to produce: wait for the design language system to be approved, proceed on the approved part only with the list of parts that are approved, or proceed as an exploratory spike with every output labelled exploratory and not referenced to the design system. Criteria: how much is missing, the cost of waiting, the risk of inconsistency. A person decides and names who approves an exception. Nothing made as an exploratory spike is passed on in H18 or H19.
3. **Mechanical.** Ask whether designs already exist, in any form: design files in any tool, screenshots or images, a live product, code prototypes or older versions. Ask how each can be viewed: a link, a connection or a view. Record each in screens/existing-designs.md with an ID (D-01, D-02), a generic name, the form, the way it can be viewed, the owner role, the date and the screens or flows it covers. Keep product addresses in the restricted file named in the local config file. Keep product addresses outside any shared file. If a login is needed that was not provided for this purpose, stop and ask.
4. **Mechanical.** Compare each existing design with the design system. For each design, list the components, tokens and patterns it matches, by ID. List where it deviates: a value that differs from a token, a component not in the library, a layout that breaks a pattern. For a screenshot or an image, record what can be seen and tag any value read from the image Inference. Evidence for a design file or product read directly. Save as screens/design-reference-comparison.md.
5. **Judgment.** Decide how to use each existing design. Options to produce: use it as a reference for layout only, bring it into the system as it is, standardise it to match the system with the list of changes, or leave it out, each with the effect on consistency. Criteria: matches the system, serves the stories in the screen inventory, fits the information architecture. A person decides. Record the standardisation decisions in screens/standardisation-decisions.md.

### Part B: the screens

6. **Mechanical.** Turn the screen inventory, or in concept prototype mode the approved concept proposals and the tasks in the test plan, into a build list. In concept prototype mode, list only the screens the instruction calls for, and label them concept prototype. For each screen, list its stories, jobs or pain points, evidence IDs, principle IDs, the components, tokens and patterns it will use from the design system, the existing design it draws on and any standardisation decision, and its states. Mark any screen with no story, job or pain point as an orphan. Features rejected in concept testing stay out. Save as screens/screen-plan.md.
7. **Judgment.** Set the order. Options to produce: two or three build orders, each with the flows it completes first. Criteria: the key journeys, dependencies between screens, the test tasks, risk. A person decides.
8. **Judgment.** Build each screen from design system components. Options to produce: for each screen, candidate components and patterns from the library with the reason each fits, and any need the library does not meet. Criteria: matches the screen plan, uses only components and tokens at the approved version, follows the standardised existing designs, serves the principles. A person builds the screen with no local values. Record the link to each screen in screens/screen-links.md.
9. **Judgment.** Set the layout for each screen size needed. Options to produce: candidate layouts per size taken from the foundations and the grid in the design system. Criteria: the grid and spacing tokens, content priority from the information architecture. A person decides.
10. **Mechanical.** Flag any component, token or pattern the design system lacks. Compare each element used or needed with the design system at its approved version. List each missing item as a request with the screen that needs it. Never create it. Save as screens/component-requests.md.
11. **Judgment.** Replace placeholders with final content. Options to produce: wording for labels, messages, help text and sample data, drawn from the content standard and terminology, with the source of each term. Criteria: uses canonical terms, follows the content standard, fits the audience. A person writes or approves, with subject matter experts. Real content, never placeholders.
12. **Mechanical.** Check that text fits the layout. For each string, compare its length with the maximum length stated for its component. Where no maximum exists, mark To verify for a person to check in the design tool. List every overflow. Save in screens/content-fit.md.
13. **Judgment.** Define the empty, loading, error and success states. In concept prototype mode, define only the states the test needs and list the others as not built. Options to produce: for each screen, the states with their content and recovery step, in the pattern from the content standard. Criteria: every screen has at least empty, loading, populated and error states, and errors say what happened and what to do next. A person decides.
14. **Judgment.** Describe how each control behaves. Options to produce: given, when and then statements for each control. Criteria: testable, covers the business rules and exception cases, matches the states. A person decides.
15. **Judgment.** Call out accessibility needs, such as tab order and alt text. Options to produce: for each screen, the needs taken from the accessibility standard, such as tab order, focus handling, alt text and touch size. Criteria: the accessibility target and the checks set in the design language system. A person decides.
16. **Mechanical.** In concept prototype mode only, assemble the coded prototype. Build an interactive prototype in plain HTML and CSS, at a level of detail a test participant can complete the test tasks in, from the decisions in steps 8 to 15. Use only the components, tokens and patterns of the approved design system. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/tokens_to_css.py --tokens <each DTCG token file, default mode first> --out <prototype folder>/tokens.css` and use only those custom properties for colour, type, spacing, radius, stroke, elevation and motion, with no local values. Make it interactive with links between pages and HTML and CSS features such as the target selector and the details element. If a task cannot be done without scripting, stop and ask a person, and never add a script on your own. Use the real content from step 11, the states from step 13, the behaviour from step 14 and the accessibility needs from step 15. Use semantic HTML, keyboard operation and visible focus, and meet the accessibility target in the accessibility standard. Build only the screens and tasks in the signed instruction. Where the design system lacks an element, stop and log a request in step 10, and never invent one. Data and behaviour may be simulated, but every simulation is listed. Write the code to `prototype/` organised by section (e.g. `prototype/01-task-creation/`), and record what was built, what was simulated and what was not built in screens/prototype-build-log.md. A designer reviews the build before it goes to testing, and 17-check-designs-against-principles-and-standards checks it. In detailed design mode a person builds, and this step is skipped.
17. **Mechanical.** Record the design system references and check them. Write one row for each component, token and pattern used on each screen into screens/design-system-references.csv, with the columns screen, kind, ref and version. Write the component list and the pattern list from the design system into two CSV files. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_references.py --usage screens/design-system-references.csv --tokens <token files> --components <components file> --patterns <patterns file> --screens <screens file> --version <current approved version>`. List every finding. A reference that is missing, stale or absent goes back to a person, or to a component request in step 10.
18. **Mechanical.** Wire screens into the flows to be tested and check that no path dead-ends. Write the screens and the links into two files, then run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_flows.py --screens screens/flow-screens.csv --links screens/flow-links.csv`. List every finding. Wire the test tasks first, then the remaining key flows. In concept prototype mode wire the tasks in the test plan and return the prototype to 11-test-concepts. Save the wired prototype link and version in screens/prototype.md.
19. **Mechanical.** Write the evidence table, the Gaps and open questions section and a list of what was not checked for every file, and name the design system version used. Set status draft. Packaging for handoff belongs to 13-package-for-handoff.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Design system readiness check, with the version used | None. Internal | Markdown | screens/ | design-system-readiness.md |
| Existing designs survey, comparison and standardisation decisions | None. Internal | Markdown | screens/ | existing-designs.md, design-reference-comparison.md, standardisation-decisions.md |
| Screen plan with story, evidence and design system references | None. Internal | Markdown table | screens/ | screen-plan.md |
| Component, token and pattern requests | None. Internal, read by 16-define-the-design-language | Markdown table | screens/ | component-requests.md |
| Hi-fi screens and screens with final content | H19 | Files in the design tool, linked | screens/ | screen-links.md |
| State and interaction specifications | H19 | Markdown | screens/ | state-interaction-specs.md |
| Design system reference record and its check | H18, H19 | CSV and Markdown | screens/ | design-system-references.csv, reference-check.md |
| Content fit and flow check results | None. Internal | Markdown | screens/ | content-fit.md, flow-check.md |
| Coded concept prototype (HTML, CSS and the generated tokens.css) and its build log | None. Goes to 11-test-concepts | Code and Markdown | `prototype/` organised by section, and screens/ | prototype code, prototype-build-log.md |
| Hi-fi prototype link and version, or the concept prototype link and version | H18, H19 for the hi-fi prototype. None for a concept prototype, which goes to 11-test-concepts | Link with a version | screens/ | prototype.md |

Screen sizes for HTML builds: Mobile 390×844 px. Tablet 768×1024 px. Desktop 1440×900 px.

Every output follows the handoff standard, carries an evidence table, names the design system version it used and has status draft.

## 7. Authority and gates

- May decide: how to lay out the screen plan, which strings to compare, how to list findings, which references to record, how to structure the prototype code.
- Must not decide: whether the design system is good enough to proceed, whether a concept is approved, whether to start a concept prototype, an exception to the system, the build order, which components a screen uses, layout, wording, states, behaviour, accessibility needs, or how an existing design is used. Must not create a component, token, screen or feature, and must not send a prototype to testing before a designer has reviewed it. Must not use access that was not given for this purpose.
- Escalate when: a concept prototype is requested with no signed instruction, a screen is not in an approved concept proposal, the design system is not ready or not available, the version a screen used is not the approved one, a screen has no reference to the system, an existing design deviates and nobody decided what to do, a screen has no story, job or pain point, a needed component is missing, a path dead-ends, a rejected feature reappears, the prototype fails an accessibility check, or the build needs something the system lacks.
- Approver role: design lead. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: inputs and versions named by file.
- [ ] Test 3, Traceable: every screen cites story, evidence and principle IDs and its design system references.
- [ ] Test 4, Single source: stories, registers, principles and tokens are cited by ID.
- [ ] Test 7, Honest about gaps: orphan screens, missing components, unverified fits and unreachable existing designs are listed.
- [ ] Test 8, Versioned and dated: the design system version used is named in every output.
- [ ] The readiness check ran first, and the design system was ready or a person approved an exception.
- [ ] A concept prototype started only from the signed instruction, and every screen is in an approved proposal.
- [ ] Existing designs were asked about, and each was compared and decided on.
- [ ] The reference check ran with no finding, or each finding is listed.
- [ ] No placeholder text remains in screens marked final.
- [ ] Every screen has empty, loading, populated and error states.
- [ ] The coded prototype uses token values from the DTCG files, has no local values, works by keyboard and was reviewed by a designer before testing.
- [ ] Simulated data and behaviour are listed in the build log.
- [ ] No component, token, screen or feature was created by the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| A concept prototype built before the concepts were aligned, or beyond what was approved | Team instruction, 2026-10-14: concept ideas are proposed and aligned first, then the person instructs the prototype | Step 1 requires the signed instruction, and step 6 lists only approved concepts |
| Screens designed outside the design system, so they drift from each other | Team instruction, 2026-10-14: detailed design must always reference the design system | Step 1 blocks work until the system is ready. Steps 8, 16 and 17 require and check references |
| Work started before the design system is ready or reachable | Team instruction, 2026-10-14 | Steps 1 and 2 stop, and only a person can approve an exception, which is labelled exploratory |
| New screens inconsistent with designs that already exist | Team instruction, 2026-10-14 | Steps 3 to 5 find, compare and decide on existing designs, in any form |
| Screens built on a stale version | Breakdown gap note on D6: "Who owns changes after release? Steps 6 and 7 both use it, so which version does each use?" | Step 17 records and checks the version for every reference |
| Screens that cannot be traced to evidence or principles | Breakdown gap note on H1: "Are screens traceable to evidence and experience principles, and where is that recorded? How are features rejected in concept testing kept out?" | Steps 6 and 17 cite IDs and exclude rejected features. The rationale is recorded by 22-record-decisions-and-rationale |
| A screen needs something the system lacks, with no rule | Breakdown gap note on H2: "When a screen needs something the system lacks, does the team add a component, make an exception or raise a request?" | Step 10 raises a request. A person decides an exception in 16-define-the-design-language |
| Nobody owns content or checks it | Breakdown gap note on H3: "Who writes the content, who checks it, and against which standard?" | Step 11 uses the content standard, and a person writes or approves. The check belongs to skill 17 |
| Accessibility assumed from the design language | Breakdown gap note on H4: "Are accessibility needs specified per screen or assumed from the design language system? Who reviews them?" | Step 15 specifies them per screen |
| Only the test tasks are wired, and the prototype drifts from the documentation | Breakdown gap note on H6: "Are all flows wired or only the test tasks? Does the prototype match the documentation?" | Step 18 wires the test tasks first, then the key flows, and records the version |
| Values read from an image taken as exact | Hypothesis from how images are used | Step 4 tags values read from an image Inference |
| A prototype that looks finished but drifts from the system or fails accessibility | Team instruction, 2026-10-14: a rapid prototype may look finished and must meet usability and accessibility standards | Step 16 builds only from token files and library components, step 17 checks references, and a designer reviews before testing |
| The agent invents screens or values | Roster entry for AG-03 and the roster design check | The rule at the head of the method and the authority section |

## 10. Principles applied

- Prioritise human control: a person designs every screen, decides every exception and decides how existing designs are used.
- Build trust through visible evidence: every screen cites its story, evidence, principle and design system version, and the references are checked by a script.
- Prevent errors: nothing starts until the system is ready, and references that do not exist are found by the check.

## 11. References

- design-canvas SKILL.md, read in part (headings and rules, 324 lines). Kept: one brief per screen, traceability from stories and rules, states as sections, content taken from the content standard, and the rule to resolve conflicts between upstream artifacts. Dropped: the sync hash, brief to design tool to prototype sync rules, and project paths. Conflict: it assumes the Figma toolchain, which the breakdown does not name.
- design-interaction SKILL.md, rules read: every screen has empty, loading, populated and error states, behaviour is written as given, when and then, and errors say what happened and what to do next.
- design-prototype SKILL.md, rules read: wire the key flow first and trace every prototype screen to its source.
- 11-test-concepts SKILL.md, steps 6 to 9: the concept proposals, the alignment, the instruction to prototype and the brief this skill starts from in concept prototype mode.
- 16-define-the-design-language SKILL.md, this folder: the outputs this skill reads, the DTCG token files and the build script it uses to check them.
- NN/g "Design Systems 101", read about 70 percent: a component library entry holds a name, description, attributes and states, and a system lets teams replicate designs with premade components.
- NN/g "Creating Design Specs for Development", read about 70 percent: real content in place of placeholders, and accessibility needs called out in the spec.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-12: H1, H2, H3, H4 and H6.
- Standard practice, not checked against a source: the options and criteria in the Judgment steps.
- Team instruction, 2026-10-14: the rapid prototype is coded, may look finished, and meets usability and accessibility standards.
- Supporting files: templates/screen-templates.md, scripts/check_references.py, scripts/check_flows.py, scripts/tokens_to_css.py.
