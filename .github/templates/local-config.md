# local-config.md — Workspace Configuration

Fill in this file in place at `.github/templates/local-config.md` and fill in every field marked
`[FILL IN]`. Fields marked `[SUGGESTED DEFAULT]` work as-is but can be changed.
Fields marked `[LEAVE BLANK]` are filled in during the project by a person, not by an agent.

Every agent in the scbx-design-agent package reads this file before starting work.
If any required field is empty, the agent will stop and ask you to complete it.

---

## 1. Project

```
project-name: [FILL IN — plain words, no organisation or client name]
project-id:   [FILL IN — short code, e.g. PRJ-001]
phase:        [FILL IN — Discover | Define | Design]
sensitivity:  [FILL IN — Standard | Elevated | Restricted]
```

---

## 2. ID formats

Used by: skills 01, 02, 03, 05, 06, 07, 08, 09, 10, 12, 13, 14, 15, 16, 19, 20, 22, s2.

```
assumption-id-prefix:        A
assumption-id-format:        A-NNN           [example: A-001, A-002]

research-question-id-prefix: RQ
research-question-id-format: RQ-NN           [example: RQ-01, RQ-02]

aim-id-prefix:               AIM
aim-id-format:               AIM-NN          [example: AIM-01]

evidence-item-id-prefix:     E
evidence-item-id-format:     E-NNNN          [example: E-0001]

source-id-prefix:            SRC
source-id-format:            SRC-NNN         [example: SRC-001]

participant-id-prefix:       P
participant-id-format:       P-NN            [example: P-01, P-02]

insight-id-prefix:           INS
insight-id-format:           INS-NNN         [example: INS-001]

need-id-prefix:              ND
need-id-format:              ND-NNN          [example: ND-001]

job-id-prefix:               JOB
job-id-format:               JOB-NNN         [example: JOB-001]

pain-point-id-prefix:        PP
pain-point-id-format:        PP-NNN          [example: PP-001]

decision-id-prefix:          DEC
decision-id-format:          DEC-NNN         [example: DEC-001]

screen-id-prefix:            SCR
screen-id-format:            SCR-NNN         [example: SCR-001]

component-id-prefix:         CMP
component-id-format:         CMP-NNN         [example: CMP-001]
```

---

## 3. Risk and confidence scales

Used by: skills 02, 10, 18, 19.

```
risk-scale:        High | Medium | Low
risk-criteria:
  High:   Wrong outcome changes the project direction or invalidates key decisions.
  Medium: Wrong outcome affects one workstream or one decision.
  Low:    Wrong outcome is recoverable with minor rework.

confidence-scale:  High | Medium | Low
confidence-criteria:
  High:   Three or more independent sources; direct evidence; recent.
  Medium: Two sources; some inference; may be dated.
  Low:    One source; mostly inference; or aged data.

severity-scale:    Critical | Major | Minor | Cosmetic
severity-criteria:
  Critical:  Blocks task completion. User cannot proceed.
  Major:     Significant friction. Workaround exists but burdensome.
  Minor:     Noticeable but does not block the user.
  Cosmetic:  Polish issue with no effect on usability.
```

---

## 4. Caps and thresholds

Used by: skills 03, 06, 08, 09, 10, 15, 18, 19.

```
question-cap:             12        [maximum research questions per plan — SUGGESTED DEFAULT]
feature-cap:              6         [maximum features per future-state concept — SUGGESTED DEFAULT]
evidence-threshold:       2         [minimum independent sources to assert a finding — SUGGESTED DEFAULT]
minimum-usability-sample: 5         [minimum participants for a usability test — SUGGESTED DEFAULT]
findability-success-rate: 80%       [pass threshold for findability tasks — SUGGESTED DEFAULT]
```

---

## 5. Sensitivity and privacy rules

Used by: skills 01, 02, 05, 11, 12, 16.

```
sensitivity-level-definitions:
  Standard:   No personally identifiable information (PII). No client-identifiable
              operational detail. All outputs may be shared within the project team.
  Elevated:   Contains aggregated participant data. Share within the project team only.
              Do not share externally without research lead approval.
  Restricted: Contains raw participant data, recordings, or operationally sensitive
              content. Share only with named approvers.

clearance-required-before-reading: [FILL IN — list content types that need a person to
                                    clear them before an agent reads them, e.g.
                                    "raw interview recordings, verbatim notes with
                                    participant names, consent forms"]

recordings-and-contact-details-location: [FILL IN — folder or system where raw recordings
                                          and participant contact details are stored,
                                          separate from the project workspace.
                                          Agents must NOT read from this location.]

product-names-in-outputs: [FILL IN — Permitted | Not permitted]
organisation-names-in-outputs: Not permitted
unit-designations-in-outputs:  Not permitted
```

---

## 6. Language and content rules

Used by: skills 01, 06, 07, 08, 09, 15, s1.

```
plain-language-rules:
  - Write in plain words. Avoid jargon unless defined.
  - Use active voice.
  - One idea per sentence.
  - Cite the source of every statement.

domain-terms:
  [FILL IN — list terms that have specific meaning in this project and their definitions.
   Leave empty if none. Example:
   - "DEX: Digital Employee Experience — the design and delivery of internal digital tools
     for employees."
   - "PDLC: Product Design and Delivery Lifecycle."]

solution-word-list:
  [FILL IN — words that signal a solution or technology that MUST NOT appear in problem
   statements or needs statements. Example: "app, platform, dashboard, portal, system,
   integration, API, automation, AI, chatbot". Leave empty if not applicable.]

feature-word-list:
  [FILL IN — words that are not permitted in need statements (they describe solutions,
   not needs). Example: "button, screen, filter, search, notification, alert". Leave empty
   if not applicable.]

need-statement-pattern:  When [situation], I need [capability], so that [outcome].
job-statement-pattern:   Help me [verb] [object] [context] [outcome].
```

---

## 7. Approver roles

Used by: all skills.

Fill in the role title for each approver. Leave the name column blank — a person fills in
the name on each output file when they approve it.

```
research-lead:          [FILL IN — role title, e.g. "Lead UX Researcher"]
project-sponsor:        [FILL IN — role title, e.g. "Programme Director"]
consent-approver:       [FILL IN — role who approves consent form wording before use]
design-lead:            [FILL IN — role title, e.g. "Lead Interaction Designer"]
product-owner:          [FILL IN — role title, e.g. "Product Owner"]
naming-authority:       [FILL IN — role who resolves naming conflicts in the design language]
register-owner:         [FILL IN — role responsible for keeping the evidence register current]
release-blocker-role:   [FILL IN — role who may block a design language release]
```

---

## 8. Repository and workspace structure

Used by: skills 05, 13, 20, 22, s2.

```
workspace-root:           [FILL IN — absolute or relative path to the workspace root,
                           e.g. "./project" or leave as "." for the repo root]

repository-location:      [FILL IN — URL or path of the shared repository, e.g.
                           "https://github.com/org/project-repo"]

skills-folder:            process-flows/skills/       [SUGGESTED DEFAULT]
templates-folder:         process-flows/skills/        [SUGGESTED DEFAULT — each skill has
                                                        its own templates/ subfolder]

output-folders:
  alignment:              alignment/
  assumptions:            assumptions/
  research-plan:          research-plan/
  evidence:               evidence/
  registers:              registers/
  insights:               insights/
  journeys:               journeys/
  problem-statements:     problem-statements/
  concepts:               concepts/
  decisions:              decisions/
  screens:                screens/
  design-language:        design-language/
  handoff:                handoff/

decision-log-location:    decisions/decision-log.md   [SUGGESTED DEFAULT]
```

---

## 9. Tag vocabulary

Used by: skill 05 (organise the evidence).

These tags are the only ones agents may use when tagging evidence items.

```
observation-type-tags:    said | did | thought | felt
evidence-type-tags:       Evidence | Inference | Assumption
context-tags:             [FILL IN — add tags relevant to your project, e.g.
                           "task, pain-point, goal, behaviour, constraint, context,
                           workaround, quote"]
concept-test-tags:        feature | task | theme | issue-type
usability-test-tags:      screen | task | theme | issue-type
```

---

## 10. Design-specific settings

Used by: skills 12, 15, 16, 17, 21.

```
design-tool:              [FILL IN — Figma | Sketch | Adobe XD | other]
prototype-folder:         [FILL IN — URL or path to the design file or prototype]

screen-sizes:
  mobile:   375 × 812 px
  tablet:   768 × 1024 px
  desktop:  1440 × 900 px
  [Edit or add sizes to match your project.]

accessibility-standard:   WCAG 2.2 AA       [SUGGESTED DEFAULT]

token-structure:
  [FILL IN — describe any overrides to the default token structure, or write "default".
   Example: "Use three tiers: primitive, semantic, component. Primitive names are colour
   codes. Semantic names use the pattern property/variant/state."]

design-language-version-scheme: [FILL IN — e.g. "semver: MAJOR.MINOR.PATCH"
                                  or "date-based: YYYY-MM-DD"]

design-language-review-period:  [FILL IN — e.g. "every sprint" or "monthly"]
```

---

## 11. Process-specific settings

Used by: skills 10, 11, 13, 14, 18.

```
prioritisation-criteria:
  [FILL IN — the criteria used to rank features or problem statements. Example:
   "impact-on-user-need: High | Medium | Low
    strategic-fit: High | Medium | Low
    delivery-effort: High | Medium | Low
    risk-if-not-addressed: High | Medium | Low"]

prioritisation-thresholds:
  [FILL IN — the minimum score to include an item in scope, or write "human decision".]

handoff-recipients:
  [FILL IN — list the roles who receive handoff packages, e.g.
   "Engineering lead, Product owner, QA lead"]

handoff-medium:            [FILL IN — e.g. "Figma link + Markdown file in repo"]

comment-window:            [FILL IN — how long reviewers have to comment on a handoff,
                            e.g. "5 business days"]

concept-test-confirmation-role: [FILL IN — role who confirms participant access and
                                  session schedule for concept testing]

usability-criteria-versioning:  [FILL IN — how pass criteria are versioned between
                                  test rounds, e.g. "date-stamped in filename"]

how-often-to-run-evidence-check: [FILL IN — e.g. "after every synthesis run" or "weekly"]
```

---

## 12. Handoff standard reference

Used by: all skills, s2.

```
handoff-standard-location: process-flows/skills/s2-handoff-standard/SKILL.md
id-prefixes-to-check:      [FILL IN — list ID prefixes the evidence repository check
                             should scan for, e.g. "A-, RQ-, E-, PP-, ND-, DEC-"]
```

---

*Template version: 0.1 — 2026-10-15. Fill in all [FILL IN] fields before running any agent.*
*Keep at `.github/templates/local-config.md`; agents and skills read it from this path.*
