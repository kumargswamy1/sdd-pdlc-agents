---
name: 16-define-the-design-language
description: Establishes the design language system and DTCG token files. Checks first for an existing system or live product and whether it is current, then adopts, derives or builds. Use when principles and IA are approved. Not for upkeep, use 21-maintain-the-design-language.
allowed-tools: Read Grep Glob Write Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/extract_css_values.py *) Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/build_dtcg.py *)
---

# 16. Define the design language

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 16, CAP-16 Define the design language |
| Phase or scope | Design in the capability list. Run at step 5 of the main process |
| Work nature mix | Mechanical 3; Judgment 8 (rows in the to-be breakdown). This skill has 10 Mechanical steps and 12 Judgment steps, because it adds the existing system check, the live product route and the token file, none of which are rows in the breakdown. To verify whether rows should be added |
| Authority level | Prepares. People decide every route, rule, token, component and standard. The skill surveys, extracts, lists, builds the token file and checks |
| Handoffs in | None. Inputs come from people and other skills and are internal |
| Handoffs out | H13, H14 |
| Human gate after | A person decides each Judgment step, and a designer reviews each agent step. Approver role: design lead |
| Used by | AG-03 Experience agent. Information only |
| Version and date | 0.2, 2026-10-13, draft |

## 2. Purpose

Gives every screen one shared set of foundations, tokens, components and standards, each traced to a principle, starting from what already exists whenever something does. It enables the decision to design at scale with consistent parts.

## 3. When to use

Use when the experience principles and the information architecture are approved and a person asks for the design language system, or when an existing system or live product is available to start from.

Not for: owning, versioning or changing the system after release. Use 21-maintain-the-design-language. Not for checking screens against it, use 17-check-designs-against-principles-and-standards. Not for recording why a rule was chosen, use 22-record-decisions-and-rationale.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Whether an existing design system or a live product exists, and how to view it: a link or connection, or a view such as a design file, a code library or package, a documentation site, a token export, saved pages or screenshots. The platform does not matter | None. A person answers in step 1 | Required. The answer may be none | If none exists, record that and take the build from scratch route |
| Access to read it: only what the person provides for this purpose | None. A person | Required for steps 2, 3 and 6 | Stop and ask. Never work around a login or a block, and never use access given for another purpose |
| Source of the latest edition of an existing system: release notes, a changelog, a version number or a publish date | None. From the source | Required for step 3 | Mark the edition To verify and ask |
| Experience principles: 04_Insights/vision/experience-principles.md | None. Internal, from 06-draw-out-insights-and-needs | Required | Stop and ask |
| Screen inventory: ia/screen-inventory.md | None. Internal | Required for steps 3 and 20 | Stop at that step and ask |
| Client brand and platform standards | None. To verify where they are recorded | Required for step 8 | Stop and ask |
| The delivery team's technology choices | None. To verify | Optional | Proceed and mark To verify |
| Terminology and the list of common components | None. To verify | Optional | Proceed and list under Gaps |
| Applicable accessibility standard and level | None. To verify | Required for step 16 | Stop at step 16 and ask |
| Feedback from the delivery team, and component, token and pattern requests: screens/component-requests.md from 12-design-the-detailed-screens | None. People and internal | Optional | Proceed and list under Gaps |
| Templates: templates/design-language-templates.md | None | Required | Stop and ask |

## 5. Method

Every rule, token and component cites the principle it serves or the place it was observed. Keep organisation names and product addresses out of every shared file. Refer to systems and pages by ID, and keep the addresses in the restricted file the local config file names. Save no user data and no credentials. Upkeep after release belongs to 21-maintain-the-design-language. The contrast check belongs to 17-check-designs-against-principles-and-standards. Recording why each rule was chosen belongs to 22-record-decisions-and-rationale.

### Part A: what exists and where to start

1. **Mechanical.** Check the inputs and ask the person two questions. Is there an existing design system, and in which platform? Is there a live product, a website or an app, that shows the current look and behaviour? For each, ask how it can be viewed: a link or connection, a view, a token export, saved pages or screenshots. Record each in language/existing-system-survey.md with an ID (S-01, S-02), a generic name, the platform, the way it can be viewed, the owner role, the edition and the date. If a login is needed and none was provided for this purpose, stop and ask.
2. **Mechanical.** Survey what exists. For each system or product, list what it holds: tokens (colour, type, spacing, radius, elevation, motion), components, patterns, content rules, accessibility rules and documentation. List how it is structured: token levels, names and modes. If a token file exists, run `python3 ${CLAUDE_SKILL_DIR}/scripts/build_dtcg.py --check <token file>` and record the result. Tag each finding Evidence and cite where it was seen. List anything out of reach under Gaps.
3. **Mechanical.** If a system exists, check whether it is current. Record the edition in use: its version, its date and its source. Find the latest published edition from the source the person gave. List the changes between the two. List drift: values and components seen on the live product that the system does not hold, and system items the product no longer uses. List components the screens in the inventory need that the system lacks, and any rule that conflicts with the experience principles. Report only. If the source gives no edition information, write To verify. Save as language/currency-report.md.
4. **Judgment.** Decide the route. Options to produce: adopt the existing system as it is, update it to the latest edition, adapt it, derive a system from the live product, or build from scratch, each with fit to the principles and the brand and platform standards, cost, upkeep effort and where the team would depart from an inherited system. Criteria: a system exists and can be reached, how current it is (step 3), fit to the principles, the delivery team's technology, effort to maintain. If no system and no live product exist, the only option is to build from scratch, and a person confirms it. A person decides, names the role that approves departures from an inherited system, and records the date. Save as language/design-language-decision.md.

### Part B: foundations and tokens

5. **Judgment.** For the derive route, choose the sample. Options to produce: candidate pages or screens of the live product, each with why it is included. Criteria: covers the key journeys in the screen inventory, shows each component type and state the product has, is permitted to be read. A person chooses the sample and confirms that capture is permitted.
6. **Mechanical.** For the derive route, capture and extract. Save for each sampled page its source and linked stylesheets, or screenshots where the source cannot be read, with a page ID, the capture date and the method. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/extract_css_values.py --files P01=<file> P02=<file> --out language/observed-values.csv`. The script counts values. It chooses nothing. List the components and patterns seen on each page, each cited by page ID. Where values are set by scripts and cannot be read, say so and ask for an export. Tag everything seen Evidence.
7. **Judgment.** For the derive route, normalise the observed values into scales. Options to produce: for each kind of value, candidate scales that merge near duplicates, with the counts behind each, and a list of values seen once. Criteria: counts, a regular step between values, the accessibility target. A person decides. Tag each derived scale Inference.
8. **Judgment.** Set the foundations: colour, type, spacing, grid, icon and motion rules. Take the starting values from the existing system for the adopt, update and adapt routes, from step 7 for the derive route, and from the principles and the brand and platform standards for the scratch route. Options to produce: for each foundation, candidate rules with the principle each serves. Criteria: serves a principle, follows the brand and platform standards, can be checked. A person decides. Save as language/foundations.md.
9. **Judgment.** Decide the token structure. The default follows the figma-tokens structure. There are three levels. Primitives hold the only raw values. Semantic tokens alias primitives and are named by purpose. Component tokens alias semantic or primitive tokens. There is one collection for each domain: colour primitives, colour semantic and component tokens, spacing, typography, icon sizes, radius, stroke, elevation and motion. Each collection has one naming pattern. Colour and elevation have light and dark modes. Spacing and typography have large, medium and small modes. Radius and stroke have one mode. Colour primitives are anchored to contrast steps, so a step is never used for a purpose beyond its clearance. Options to produce: the default structure as written, and a version adapted to the names and modes of the existing system, each with the effect on the screens. Criteria: raw values only at the primitive level, one naming pattern for each collection, modes that match how the product behaves. A person decides. Save as language/token-structure.md.
10. **Mechanical.** Build the token table. Write one row for each token in language/tokens.csv with the columns path, level, type, value, mode, description, source, evidence and confidence. Check that a token does not already exist before adding one. Primitive rows hold raw values. Semantic and component rows hold aliases only, never raw values. Create the token before any component uses its value. Set a value for every mode in the collection. Write the colour pairs that the design uses to language/contrast-pairs.csv, for skill 17 to check.
11. **Mechanical.** Export and validate the DTCG token files. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/build_dtcg.py --csv language/tokens.csv --out tokens`. The script writes one `.tokens.json` file for each mode and writes nothing when it finds an error. For an existing token file, run it with `--check`. Paste the report into language/token-validation.md. Send each error back to step 10 or to a person. Fix nothing silently.

    After validation passes, ask the person: "Would you like me to push these tokens directly into Figma as variables? If yes, share the Figma file URL and confirm the Desktop Bridge plugin is running (right-click Figma → Plugins → Development → Figma Desktop Bridge)." If yes, call `figma_navigate(url)` then `figma_import_tokens` with the DTCG JSON using `merge` strategy. Report the result. If no, proceed to step 12.

12. **Judgment.** Review the token set. Options to produce: for each token flagged as used once, a near duplicate, or outside the pattern, keep, rename, merge or drop, with the counts or the principle behind it. Criteria: serves a principle, one naming pattern, within the structure decided in step 9. A person decides, and step 10 and step 11 run again on the result.

### Part C: components and standards

13. **Judgment.** Decide the components. For the adopt, update, adapt and derive routes, list the components found in the existing system or observed on the product, with the states seen, and propose which to keep, rename or add. For the scratch route, propose each component with a name, purpose, attributes and states (default, hover, focus, disabled and error). Options to produce: a candidate definition for each component and the screens that need it. Criteria: needed by a screen in the inventory, built from tokens, covers the states. A person decides.
14. **Mechanical.** Check that each component is reusable. For each component, list whether it has a name, a purpose, attributes and every state, and whether any value is fixed in the component instead of aliasing a token. List every gap. Never fix a component. Save in language/component-checks.md.
15. **Judgment.** Write the voice, tone, terminology and microcopy rules. For the adopt, update, adapt and derive routes, start from the wording seen in the existing system or product. Options to produce: two wordings of each rule, with an example from the screens. Criteria: matches the audience, uses the users' words, includes the pattern for errors (what happened, then what to do) and for button labels (a specific verb). A person decides. Save as language/content-standard.md.
16. **Judgment.** Set the accessibility target. Options to produce: candidate targets, such as WCAG 2.1 level AA and WCAG 2.2 level AA, with what each requires. Criteria: the client's requirements, applicable regulation, the users' needs. A person decides. Never lower a target once set without a person's approval.
17. **Judgment.** Set the checks each component must pass. Options to produce: a checklist for each component type, taken from the accessibility target, the content standard and the token structure. Criteria: each check can be done and its result recorded. A person decides. Save as language/accessibility-standard.md.
18. **Mechanical.** Add context of use, do's and don'ts, and examples for each component, from the approved definitions and the screens that use it. Never write a rule that a person did not approve. Save as language/usage-guidelines.md.
19. **Judgment.** Group repeat layouts into patterns. Options to produce: layouts that appear on three or more screens, each with its components. Criteria: repeats on several screens, built from the components and tokens. A person decides. Save as language/pattern-library.md.
20. **Mechanical.** Apply the system to the sample screens. For each sample screen, list every place the system has no token, component or rule. Never design around a gap. Save as language/application-gaps.md.
21. **Judgment.** Fix the gaps. Options to produce: for each gap, add a token or component, make an exception, or raise a request, with the effect on consistency and effort. Criteria: serves a principle, reusable, effort. A person decides, and names who approves changes after release.
22. **Mechanical.** Write the evidence table, the Gaps and open questions section and a list of what was not checked for every file. Set status draft until the approver signs. Versioning and the release belong to 21-maintain-the-design-language.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Existing system survey and currency report | None. Internal | Markdown | language/ | existing-system-survey.md, currency-report.md |
| Design language decision: route, owner of departures | H13, H14 | Markdown | language/ | design-language-decision.md |
| Observed values and pages sampled (derive route only) | None. Internal | CSV and Markdown | language/ | observed-values.csv, pages-sampled.md |
| Foundations specification and token structure | H13, H14 | Markdown | language/ | foundations.md, token-structure.md |
| Token table | None. Internal | CSV | language/ | tokens.csv |
| **DTCG token files**, one for each mode | H13, H14 | JSON, DTCG 2025.10, extension .tokens.json | tokens/ | design-tokens.<mode>.tokens.json, or design-tokens.tokens.json for one mode |
| Token validation report | None. Internal | Markdown | language/ | token-validation.md |
| Contrast pairs, for skill 17 | None. Internal | CSV | language/ | contrast-pairs.csv |
| Component library with checks | H13, H14 | Files in the team's design tool, linked, and a list | language/ | component-library.md, component-checks.md |
| Content standard and accessibility standard | H13, H14 | Markdown | language/ | content-standard.md, accessibility-standard.md |
| Usage guidelines and pattern library | H13, H14 | Markdown | language/ | usage-guidelines.md, pattern-library.md |
| Application gaps and decisions | None. Internal | Markdown table | language/ | application-gaps.md |

Every output follows the handoff standard, carries an evidence table and has status draft until signed.

## 7. Authority and gates

- May decide: how to lay out files, how to write usage context from approved definitions, which values to count, how to list gaps and token errors.
- Must not decide: the route, any rule, token, component, standard or pattern, the accessibility target, or an exception. Must not fix a gap or a token error silently. Must not release or version the system. Must not use access that was not given for this purpose, and must not save credentials or user data.
- Escalate when: no principles exist, a login or a block stands in the way, the existing system is out of date and no one owns it, a rule serves no principle, a semantic or component token would hold a raw value, brand preference and a principle conflict, or the target would be lowered.
- Approver role: design lead. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every rule and component cites a principle, and every observed value cites a page ID.
- [ ] Test 4, Single source: principles are cited by ID and not copied.
- [ ] Test 6, Owned and statused: owner role, approver role and status are present.
- [ ] Test 7, Honest about gaps: application gaps, unreachable sources and missing inputs are listed.
- [ ] Test 8, Versioned and dated: version and date on every file, and the edition checked for an existing system.
- [ ] The existing system question was asked first, and the answer is recorded.
- [ ] If a system exists, the currency report exists.
- [ ] The token files validate with no errors, and no semantic or component token holds a raw value.
- [ ] No product address or organisation name appears outside the restricted file.
- [ ] No rule was added by the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Unclear whether the system is built here or inherited, and who approves departures | Breakdown gap note on D1: "Is the design language system built here or inherited? If inherited, where does the team depart from it and who approves that?" | Steps 1 to 4 ask first, check the existing system and record the route and the approver |
| An existing system used without checking whether it is current | Team instruction, 2026-10-13 | Step 3 compares the edition in use with the latest and lists drift |
| The live product shows many near duplicate values | Hypothesis from how products accumulate styles | Steps 6 and 7 count values and a person merges them |
| A source that cannot be read, or a login | Hypothesis from how products are protected | Step 1 stops and asks. The skill never works around access |
| Saved pages that hold user data | Hypothesis from how pages are captured | The rule at the head of the method: styles and structure only |
| Raw values at the semantic or component level | Rule in the figma-tokens skill: only primitives hold raw values | Step 10 and the build script reject them |
| A token file that breaks the format | DTCG 2025.10 format module: naming and value rules | Step 11 validates, and writes nothing on an error |
| Foundations that follow brand preference alone | Breakdown gap note on D2: "Do the foundations trace to the experience principles or to brand preference alone?" | Step 8 ties every rule to a principle |
| Components built up front versus as needed, and not matched to code | Breakdown gap note on D3: "Which components are built up front and which as detailed design needs them? Is the design library matched to code?" | Step 13 builds from the inventory. The match to code is To verify |
| No accessibility target, and checks nobody runs | Breakdown gap note on D4: "How are content, standards and accessibility checked, by whom and at which step? Is an accessibility target written down?" | Steps 16 and 17 write them. The check itself is skill 17 |
| Guidance a developer cannot find | Breakdown gap note on D5: "Where is it published, and can a developer find an answer without asking a designer?" | Step 18 writes usage guidance. The publishing place is To verify |
| Unclear ownership and versions after release | Breakdown gap note on D6: "Who owns changes after release? Steps 6 and 7 both use it, so which version does each use?" | Handed to 21-maintain-the-design-language |
| The agent writes rules or fixes gaps | Roster design check | The authority section |

## 10. Principles applied

- Prioritise human control: people decide the route, every rule and every token, and the skill never fixes a gap.
- Build trust through visible evidence: every value cites where it was seen, and the token files are validated.
- Start simple: an existing system is checked first, so no effort goes into what can be inherited.

## 11. References

- figma-tokens SKILL.md, read in full (628 lines, locally and at the GitHub address given on 2026-10-13). Kept: the three levels, the alias chain rule (only primitives hold raw values), the resolution order (component, then semantic, then primitive), one collection for each domain, one naming pattern for each collection, the mode strategy, contrast anchored colour steps, and the checklist for adding a token. Dropped: the Figma Console steps, the Figma styles phase, the variable types FLOAT and STRING, and the list of tokens still to create. Conflict: it stores motion as text strings, while DTCG has duration and cubic bezier types, so the DTCG types are used.
- Design Tokens Community Group format module, version 2025.10, read in full across two fetches (designtokens.org/TR/2025.10/format/) and its colour module read in full: the file extension .tokens.json, media type application/design-tokens+json, tokens with $value and optional $type, $description, $extensions and $deprecated, the naming rules, aliases written {group.token}, and the value shapes for colour, dimension, font family, font weight, duration, cubic bezier, number, typography, shadow, border and gradient. Not read: any module that defines modes or themes, so the one file per mode is a convention. To verify. The build script's checks are not an official validator. To verify with a DTCG compliant tool.
- Ch 08 design-visual SKILL.md, rules read: every colour needs a rationale, the spacing scale is mathematical, and dark mode is a strategy and not an inversion.
- Ch 09 design-content SKILL.md, read in full (130 lines). Kept: the terminology guide, the error message pattern, specific verb button labels and sentence case.
- Ch 10 design-accessibility SKILL.md, read in full (218 lines). Kept: WCAG AA as the minimum, never lowering the target without approval. The contrast audit belongs to skill 17.
- Ch 12 design-governance SKILL.md, Phase A read: the quality gate list and naming authority. Versioning belongs to skill 21.
- NN/g "Design Systems 101", read about 70 percent: adopt, adapt or create, and the parts of a system.
- NN/g "Design Systems vs. Style Guides", read about 60 to 70 percent, and NN/g "Design-System Maturity", read about 70 percent: upkeep, governance and parity with code.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-16: D1 (step 1), D2 (step 1), D3, D4, D5 and D6 (steps 1 and 2).
- Standard practice, not checked against a source: the options and criteria in the Judgment steps, and reading values from a product's stylesheets.
- Supporting files: templates/design-language-templates.md, scripts/extract_css_values.py, scripts/build_dtcg.py.
