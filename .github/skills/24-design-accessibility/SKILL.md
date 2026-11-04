---
name: 24-design-accessibility
description: Defines accessibility requirements per component type and per screen, mapped to WCAG 2.2 AA. Output feeds skills 25, 26, and 27 so every canvas brief, Figma page, and component build carries explicit accessibility specs.
allowed-tools: Read Write Edit Glob
---

# 24. Design accessibility

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 24, CAP-24 Design accessibility |
| Phase or scope | Design |
| Work nature mix | Mechanical 6; Judgment 6 |
| Authority level | Prepares. A person reviews and approves every accessibility requirement. The skill documents, proposes, and flags gaps. |
| Handoffs in | H14 (design language), H16 (IA and screen inventory), output of skills 15 and 16 |
| Handoffs out | Consumed by skills 25, 26, and 27 |
| Human gate after | Design lead reviews and approves the accessibility spec before it is used in canvas briefs or component builds |
| Used by | AG-03 Experience agent |
| Version and date | 0.1, 2026-10-14, draft |

## 2. Purpose

Produces a component-level and screen-level accessibility specification, mapped explicitly to WCAG 2.2 AA success criteria. Every component and every screen carries requirements a designer and developer can act on — role, name, state, focus order, touch target, contrast. This document is the accessibility contract consumed by skills 25, 26, and 27.

## 3. When to use

Use after the component library (skill 16) and screen inventory (skill 15) are approved. Run before skill 25 (design canvas), skill 26 (Figma page setup), and skill 27 (build Figma components). Not for contrast-checking token pairs — use the contrast-check process in skill 16 for that. Not for running automated accessibility tests — use skill 17 for that.

## 4. Inputs

| Input | Source | Required or optional | If missing |
|---|---|---|---|
| Component library: `08_Design_Language/component-library.md` | Skill 16 | Required | Stop and ask |
| Screen inventory: `07_Architecture/screen-inventory/screen-inventory.md` | Skill 15 | Required | Stop and ask |
| Accessibility standard: WCAG 2.2 AA (hardcoded) | — | Required | Use WCAG 2.2 AA. No config file needed |
| Contrast pairs already checked: `08_Design_Language/contrast-check.md` | Skill 16 | Optional | Proceed and note that contrast check is pending |
| Interaction spec: `08_Design_Language/interaction/interaction-spec.md` | Skill 23 | Optional | Proceed without interaction detail; flag in Gaps |

## 5. Method

### Step 1 — Component accessibility matrix

**Mechanical.** For each component in the component library, document the accessibility requirements in a matrix. Columns: Component name, ARIA role, Accessible name source (label, aria-label, aria-labelledby), Required states (focus, disabled, error, selected, expanded), Keyboard interaction (Tab, Enter, Space, Arrow keys, Escape), Touch target minimum (44×44 px per WCAG 2.5.8), WCAG 2.2 AA criteria met. Flag any component with no defined role or with a touch target below 24×24 px (minimum) or below 44×44 px (recommended). Save as `08_Design_Language/accessibility/component-accessibility-matrix.md`.

### Step 2 — Focus order per screen

**Judgment.** For each screen in the screen inventory, propose the reading and focus order. Options to produce: two or three candidate focus orders per screen, with the rationale each serves (task completion, left-to-right top-to-bottom, landmark order). Criteria: follows the visual hierarchy from the IA, every interactive element is reachable, no trap. A person decides. Record in `08_Design_Language/accessibility/focus-order.md`.

### Step 3 — Colour and contrast requirements

**Mechanical.** Produce a requirements table from the contrast pairs already checked in `08_Design_Language/contrast-check.md`. For each pair: token pair, contrast ratio, WCAG criterion (1.4.3 for text, 1.4.11 for non-text), pass or fail, and the corrective action if failed. If no contrast check exists, flag as a gap and proceed. Save as `08_Design_Language/accessibility/contrast-requirements.md`.

### Step 4 — Non-text accessibility requirements

**Judgment.** For each image, icon, chart, and data visualisation in the component library and screen inventory, propose the non-text alternative approach: alt text pattern, aria-label strategy, or decorative (role="presentation"). Options to produce: candidate patterns for each type with the WCAG 1.1.1 requirement. Criteria: every non-decorative image has a text alternative, every chart communicates its data via text. A person decides. Record in `08_Design_Language/accessibility/non-text-requirements.md`.

### Step 5 — Motion and animation requirements

**Mechanical.** From the interaction spec (skill 23, if run) or from the design language, list every animation and confirm it has a `prefers-reduced-motion` alternative. Map each to WCAG 2.3.3 (Animation from Interactions, AAA) and flag any animation with no reduced-motion fallback as a gap. Even at AA, reduced-motion support is required for any animation that could cause vestibular issues. Save in `08_Design_Language/accessibility/motion-requirements.md`.

### Step 6 — Screen-level accessibility checklist

**Mechanical.** For each screen in the screen inventory, produce a one-row checklist: screen ID, landmark regions defined, heading hierarchy correct (h1→h2→h3 with no skips), page title unique and descriptive, error messages associated with their fields (aria-describedby), timeout warnings present if session can expire. Flag any screen with a gap. Save as `08_Design_Language/accessibility/screen-checklist.md`.

### Step 7 — Accessibility spec consolidation

**Mechanical.** Consolidate into one master document: `08_Design_Language/accessibility/accessibility-spec.md`. The spec must cover: component matrix summary, focus order decisions, contrast requirements, non-text requirements, motion requirements, screen checklist, and a Gaps and open questions section. Set status draft.

## 6. Outputs

| Output | Format | Location | File name |
|---|---|---|---|
| Component accessibility matrix | Markdown table | `08_Design_Language/accessibility/` | component-accessibility-matrix.md |
| Focus order per screen | Markdown | `08_Design_Language/accessibility/` | focus-order.md |
| Contrast requirements | Markdown table | `08_Design_Language/accessibility/` | contrast-requirements.md |
| Non-text requirements | Markdown table | `08_Design_Language/accessibility/` | non-text-requirements.md |
| Motion requirements | Markdown table | `08_Design_Language/accessibility/` | motion-requirements.md |
| Screen-level checklist | Markdown table | `08_Design_Language/accessibility/` | screen-checklist.md |
| Master accessibility spec | Markdown | `08_Design_Language/accessibility/` | accessibility-spec.md |

## 7. Authority and gates

- May decide: how to structure the matrix, which WCAG criteria to list per component, how to group screens.
- Must not decide: the focus order on a screen, whether a component is decorative, whether a gap is acceptable. Those require a person's decision.
- Escalate when: a component has no viable accessible name, a contrast pair fails and no token alternative exists, a screen has no landmark regions defined.

## 8. Quality checks

- [ ] Every component in the component library has a row in the matrix with role, name, and keyboard interaction.
- [ ] No component has a touch target below 24×24 px; any below 44×44 px is flagged.
- [ ] Every screen has a focus order recorded and a person approved it.
- [ ] Every non-decorative image and icon has an alt text or aria-label pattern.
- [ ] Every animation has a `prefers-reduced-motion` alternative or is flagged as a gap.
- [ ] Accessibility spec has a Gaps and open questions section.

## 9. References

- WCAG 2.2 AA: SC 1.1.1 (Non-text Content), 1.3.1 (Info and Relationships), 1.3.2 (Meaningful Sequence), 1.4.1 (Use of Colour), 1.4.3 (Contrast Minimum), 1.4.11 (Non-text Contrast), 2.1.1 (Keyboard), 2.4.3 (Focus Order), 2.4.6 (Headings and Labels), 2.5.3 (Label in Name), 2.5.8 (Target Size), 3.3.1 (Error Identification), 3.3.2 (Labels or Instructions)
- WCAG 2.2 AAA: SC 2.3.3 (Animation from Interactions)
- Skill 16 SKILL.md — token contrast pairs
- Skill 17 SKILL.md — checks this spec against the built screens
- Skill 25, 26, 27 SKILL.md — consume this skill's output
