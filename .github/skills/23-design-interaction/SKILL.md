---
name: 23-design-interaction
description: Documents the interaction model for a product or flow — gestures, transitions, feedback patterns, timing, and animation. Output feeds skill 25 (design canvas) and skill 27 (build Figma components).
allowed-tools: Read Write Edit Glob
---

# 23. Design interaction model

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 23, CAP-23 Design interaction model |
| Phase or scope | Design |
| Work nature mix | Mechanical 4; Judgment 8 |
| Authority level | Prepares. A person approves every interaction pattern. The skill documents, proposes, and flags gaps. |
| Handoffs in | H14 (design language), H16 (IA and screen inventory), output of skill 15 and skill 16 |
| Handoffs out | Consumed by skill 25 (design canvas) and skill 27 (build Figma components) |
| Human gate after | Design lead reviews and approves the interaction spec before it is used in canvas briefs or component builds |
| Used by | AG-03 Experience agent |
| Version and date | 0.1, 2026-10-14, draft |

## 2. Purpose

Produces a single interaction spec document that defines how the product behaves — how users move through it, what feedback they receive, how transitions feel, and how animation is used. This document is the motion and behaviour contract that all screens and components must follow.

## 3. When to use

Use after the information architecture (skill 15) and design language (skill 16) are approved. Run before skill 25 (design canvas) and skill 27 (build Figma components) so that those skills can reference confirmed interaction patterns. Not for defining visual style or token values — use skill 16 for that. Not for screen layout — use skill 25.

## 4. Inputs

| Input | Source | Required or optional | If missing |
|---|---|---|---|
| Information architecture and screen inventory: `07_Architecture/ia/` and `07_Architecture/screen-inventory/screen-inventory.md` | Skill 15 | Required | Stop and ask |
| Design language: `08_Design_Language/foundations.md`, component library, content standard | Skill 16 | Required | Stop and ask |
| Any existing interaction patterns, animation specs, or motion guidelines the team already uses | Person provides | Optional | Proceed and note that none exist |
| Platform guidelines relevant to the product (e.g. iOS HIG, Material) | Person provides | Optional | Proceed and note which were consulted |

## 5. Method

### Step 1 — Gesture inventory

**Mechanical.** List every gesture and input the product needs, drawn from the screen inventory and the IA flows. For each: name (tap, swipe-left, long-press, drag, pinch, keyboard shortcut), the screen or component it applies to, and the action it triggers. Mark any gesture not supported by the design language component library. Save as `08_Design_Language/interaction/gesture-inventory.md`.

### Step 2 — Navigation and transition patterns

**Judgment.** For each flow in the IA, propose the transition type between each screen pair: push (forward), pop (back), modal overlay, fade, none. Options to produce: two or three patterns per transition type with the rationale each serves (hierarchy, reversibility, user expectation). Criteria: matches the IA hierarchy, consistent within a flow, legible on mobile (390 px). A person decides. Record in `08_Design_Language/interaction/transition-patterns.md`.

### Step 3 — Feedback patterns

**Judgment.** For each control type in the component library, document the feedback the user receives: visual (state change), haptic (mobile only), audio (if applicable), and timing. Options to produce: candidate feedback for each control type, drawn from the design language and platform conventions. Criteria: immediate (under 100 ms for visual feedback), distinguishable, consistent across similar controls. A person approves. Record in `08_Design_Language/interaction/feedback-patterns.md`.

### Step 4 — Animation spec

**Judgment.** Define the animation vocabulary: easing functions, durations, and the rule for when animation is used versus when it is omitted. Options to produce: two or three animation tiers (micro, transition, attention) with candidate easing and duration values. Criteria: purposeful (communicates state or hierarchy), respects `prefers-reduced-motion`, within the token structure (motion tokens if skill 16 defined them). A person decides. Record in `08_Design_Language/interaction/animation-spec.md`.

The `prefers-reduced-motion` rule is non-negotiable: every animation MUST have a reduced-motion alternative that provides the same information without motion.

### Step 5 — Error and empty states

**Mechanical.** For each screen in the screen inventory, confirm that the interaction model covers: how the user reaches an empty state, what triggers an error state, and what the recovery path is. Flag any screen with no defined recovery path. These supplement the states defined in skill 12 step 13. Record gaps in `08_Design_Language/interaction/state-coverage.md`.

### Step 6 — Interaction spec consolidation

**Mechanical.** Consolidate into one master document: `08_Design_Language/interaction/interaction-spec.md`. The spec must cover: gesture inventory, transition patterns per flow, feedback patterns per control type, animation vocabulary, state coverage gaps. Add a Gaps and open questions section. Set status draft.

## 6. Outputs

| Output | Format | Location | File name |
|---|---|---|---|
| Gesture inventory | Markdown table | `08_Design_Language/interaction/` | gesture-inventory.md |
| Transition patterns | Markdown | `08_Design_Language/interaction/` | transition-patterns.md |
| Feedback patterns | Markdown table | `08_Design_Language/interaction/` | feedback-patterns.md |
| Animation spec | Markdown | `08_Design_Language/interaction/` | animation-spec.md |
| State coverage gaps | Markdown table | `08_Design_Language/interaction/` | state-coverage.md |
| Master interaction spec | Markdown | `08_Design_Language/interaction/` | interaction-spec.md |

## 7. Authority and gates

- May decide: how to organise the spec, which platform conventions to reference, how to group gesture types.
- Must not decide: which transition a flow uses, the duration or easing values, whether animation is omitted on a screen. Those are judgment steps requiring a person's decision.
- Escalate when: a screen in the inventory has no reachable state from the IA flows, a required gesture conflicts with a platform convention, an animation cannot meet the reduced-motion requirement.

## 8. Quality checks

- [ ] Every screen in the screen inventory has at least one gesture defined.
- [ ] Every flow transition is named and a person approved it.
- [ ] Every control type in the component library has a feedback pattern.
- [ ] Animation spec includes a `prefers-reduced-motion` rule for every animation defined.
- [ ] State coverage flags any screen with no recovery path.
- [ ] Master interaction spec has a Gaps and open questions section.

## 9. References

- WCAG 2.2 SC 2.5.3 (Label in Name), SC 2.5.8 (Target Size), SC 2.3.3 (Animation from Interactions)
- Apple Human Interface Guidelines — gestures and transitions
- Google Material Design — motion and feedback
- Skill 16 SKILL.md — motion token structure
- Skill 25 SKILL.md — consumes this skill's output
