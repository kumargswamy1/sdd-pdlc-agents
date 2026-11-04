---
name: 25-design-canvas
description: Produces a per-screen canvas brief that bridges the IA, tokens, interaction model, and accessibility spec into a precise instruction for building each screen in Figma (skill 26 and 27) or as an HTML prototype (skill 12).
allowed-tools: Read Write Edit Glob
---

# 25. Design canvas brief

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 25, CAP-25 Design canvas brief |
| Phase or scope | Design |
| Work nature mix | Mechanical 5; Judgment 7 |
| Authority level | Prepares. A person reviews and approves each canvas brief before it is handed to skill 26 or 27. The skill collects, synthesises, and flags gaps. |
| Handoffs in | Skills 15, 16, 23, 24 |
| Handoffs out | Skills 26 and 27 (Figma), skill 12 (HTML prototype) |
| Human gate after | Design lead reviews and approves all canvas briefs before Figma setup or component build begins |
| Used by | AG-03 Experience agent |
| Version and date | 0.1, 2026-10-14, draft |

## 2. Purpose

Translates everything the upstream skills have produced — the IA, the design tokens, the interaction model, and the accessibility spec — into one actionable brief per screen. Each brief is the single source of truth a designer or an agent uses to set up the Figma artboard and build the components on it. A brief with gaps is better than a brief with invented values: flag every gap clearly.

## 3. When to use

Use after skills 15 and 16 are approved, and after skills 23 and 24 if they have been run. Run before skill 26 (Figma page setup) and skill 27 (build Figma components). Also consumed by skill 12 when the HTML path is chosen, to drive the screen layout and state definitions.

## 4. Inputs

| Input | Source | Required or optional | If missing |
|---|---|---|---|
| Screen inventory: `07_Architecture/screen-inventory/screen-inventory.md` | Skill 15 | Required | Stop and ask |
| IA flows: `07_Architecture/ia/` | Skill 15 | Required | Stop and ask |
| Design language: `08_Design_Language/foundations.md`, `08_Design_Language/component-library.md`, DTCG token files in `08_Design_Language/tokens/` | Skill 16 | Required | Stop and ask |
| Interaction spec: `08_Design_Language/interaction/interaction-spec.md` | Skill 23 | Optional | Proceed; mark interaction fields To verify |
| Accessibility spec: `08_Design_Language/accessibility/accessibility-spec.md` | Skill 24 | Optional | Proceed; mark accessibility fields To verify |

## 5. Method

**Screen sizes:** Mobile 390×844 px. Tablet 768×1024 px. Desktop 1440×900 px.

### Step 1 — Source inventory

**Mechanical.** List every source file that exists: screen inventory, IA flows, token files, component library, interaction spec, accessibility spec. For each, confirm it can be read and has status approved. List any file that is missing, draft, or unreachable. Proceed only if the screen inventory and design language are available.

### Step 2 — Brief per screen

**Mechanical.** For each screen in the screen inventory, produce a canvas brief with the following sections:

**Screen ID and name** (from screen inventory, SCR-NNN format)

**Purpose** — one sentence: the story, job, or pain point this screen addresses, with IDs.

**Breakpoints to build** — Mobile 390×844, Tablet 768×1024, Desktop 1440×900. Flag any breakpoint the design language does not support.

**Layout** — grid columns, gutters, and margins from `foundations.md` at each breakpoint. Content zones: header, content, footer — with their height rules.

**Components** — list each component from the component library by CMP-NNN ID, its position in the layout, and its variant or state to start from.

**Tokens** — list the semantic token IDs used on this screen: surface, text, border, interactive colours; spacing; radius; shadow. No raw hex values — token IDs only.

**Interaction** — for each control: the gesture from the gesture inventory, the transition to the next screen (from transition-patterns.md), and the feedback pattern (from feedback-patterns.md). If interaction spec is missing, mark To verify.

**Accessibility** — focus order from focus-order.md; ARIA roles and names for each component; landmark regions; heading hierarchy. If accessibility spec is missing, mark To verify.

**States** — empty, loading, populated, error, success. One sentence per state: what triggers it, what the user sees, and the recovery path.

**Content** — final strings from the content standard for labels, headings, error messages, and placeholder text. No invented copy.

**Gaps** — every field marked To verify, every component not in the library, every token not in the DTCG files.

Save each brief as `09_Screens/canvas-briefs/SCR-NNN-canvas-brief.md`.

### Step 3 — Conflict resolution

**Judgment.** Where the IA, the interaction spec, and the accessibility spec conflict (e.g. an IA transition that violates a focus order rule), document both sides and propose a resolution. Options to produce: two resolution options with the implication of each. Criteria: accessibility takes precedence over visual preference; IA hierarchy takes precedence over motion. A person decides. Record decisions in `09_Screens/canvas-briefs/brief-conflicts.md`.

### Step 4 — Brief review

**Mechanical.** Check every brief for completeness: no blank required field, no raw hex value, no invented copy, no component not in the library. List every deficiency. A person reviews and approves before skills 26 and 27 proceed. Save the review checklist as `09_Screens/canvas-briefs/brief-review.md`.

## 6. Outputs

| Output | Format | Location | File name |
|---|---|---|---|
| Canvas brief per screen | Markdown | `09_Screens/canvas-briefs/` | SCR-NNN-canvas-brief.md |
| Conflict log | Markdown | `09_Screens/canvas-briefs/` | brief-conflicts.md |
| Brief review checklist | Markdown | `09_Screens/canvas-briefs/` | brief-review.md |

## 7. Authority and gates

- May decide: how to structure the brief, how to organise the conflict log.
- Must not decide: which tokens a screen uses, which layout a breakpoint uses, what copy a label carries, how a conflict is resolved. Those are judgment steps or come from approved upstream sources.
- Escalate when: a screen in the inventory cannot be mapped to any IA flow, a required component is not in the library, a token the screen needs is not in the DTCG files.

## 8. Quality checks

- [ ] Every screen in the screen inventory has a canvas brief.
- [ ] Every brief cites its source IDs (SCR-NNN, CMP-NNN, ND-NNN, E-NNNN).
- [ ] No raw hex value appears in any brief — token IDs only.
- [ ] Every gap or missing value is marked To verify.
- [ ] Conflict log lists every conflict and a person has decided the resolution.
- [ ] Brief review checklist has no open deficiencies before skills 26 and 27 proceed.

## 9. References

- Skill 15 SKILL.md — screen inventory and IA flows
- Skill 16 SKILL.md — design language and tokens
- Skill 23 SKILL.md — interaction model
- Skill 24 SKILL.md — accessibility spec
- Skill 26 SKILL.md — consumes this skill's output for Figma setup
- Skill 27 SKILL.md — consumes this skill's output for component build
- Skill 12 SKILL.md — consumes this skill's output for HTML prototype
