---
name: 27-figma-component
description: Builds Figma components using atomic sequence (atoms → molecules → organisms) following the component library and canvas briefs. Adds state variants (Default/Hover/Pressed/Disabled/Focus) and binds design variables. Requires Desktop Bridge plugin.
allowed-tools: Read Write Edit Glob figma_execute figma_navigate figma_get_status figma_capture_screenshot figma_create_component_set figma_set_fills figma_batch_create_variables figma_import_tokens
---

# 27. Build Figma components

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 27, CAP-27 Build Figma components |
| Phase or scope | Design — Figma canvas |
| Work nature mix | Mechanical 7; Judgment 5 |
| Authority level | Prepares and assembles. Every component is built from the approved component library and design tokens — no new components, no new token values. A designer reviews each built component. |
| Handoffs in | Skills 25 (canvas briefs), 26 (Figma page structure), 16 (tokens and component library) |
| Handoffs out | Skill 12 (screens use the built components) |
| Human gate after | Designer reviews each atom, molecule, and organism before it is placed on screen artboards |
| Used by | AG-03 Experience agent |
| Version and date | 0.1, 2026-10-14, draft |

## 2. Purpose

Builds the Figma component set that the screens will use. Follows the atomic sequence — atoms first, then molecules (atoms composed), then organisms (molecules composed) — so every higher-level component is built from verified lower-level parts. Binds Figma variables to every fill, stroke, spacing, and text property so the component automatically responds to token changes.

## 3. When to use

Use after skill 26 has set up the page structure and skill 25 canvas briefs are approved. Before running, tokens must already be in the Figma file as variables — either pushed by skill 16 via `figma_import_tokens`, or present from a prior session. Do not build components without confirmed variable bindings.

**Before running any Figma steps:** confirm with the user that the Desktop Bridge plugin is running. Ask for the Figma file URL if not already provided.

## 4. Inputs

| Input | Source | Required or optional | If missing |
|---|---|---|---|
| Canvas briefs: `09_Screens/canvas-briefs/` | Skill 25 | Required | Stop and ask |
| Component library: `08_Design_Language/component-library.md` | Skill 16 | Required | Stop and ask |
| DTCG token files: `08_Design_Language/tokens/` | Skill 16 | Required | Stop and ask |
| Figma variables (already in the file) | Skill 16 via `figma_import_tokens`, or confirmed by user | Required | Stop. Ask user to run skill 16 Figma token push first |
| Figma page structure from skill 26 | Skill 26 | Required | Stop and ask |
| Accessibility spec: `08_Design_Language/accessibility/accessibility-spec.md` | Skill 24 | Optional | Proceed; flag missing accessibility annotations |
| Figma file URL | Person provides | Required | Stop and ask |

## 5. Method

### Step 1 — Token verification

**Mechanical.** Call `figma_execute` to list the variable collections in the file. Confirm that at least one collection exists and has variables. If no variables are found, stop and ask the user to run skill 16's Figma token push step first. Report which collections exist.

### Step 2 — Component library read

**Mechanical.** Read `08_Design_Language/component-library.md`. Build a list of all components, grouped by tier: atoms (basic — buttons, inputs, labels, icons, chips), molecules (composed — form fields, cards, list items, navigation items), organisms (complex — navigation bars, forms, data tables, modals). Flag any component with no defined states or no token bindings.

### Step 3 — Atom build

**Mechanical and Judgment.** For each atom in the component library, build a Figma component on the `_Components / Atoms` section of the staging page. Follow this sequence for each atom:

1. Create a frame, set its name to the CMP-NNN component name.
2. Set fill, stroke, padding, radius using `figma_set_fills` and `figma_execute` with variable bindings — no hardcoded values.
3. Add any text layers and bind their colour and style to the appropriate variable.
4. If the atom has states: create state variants (Default, Hover, Pressed, Disabled, Focus) using `figma_create_component_set`. Add variant properties for each state.
5. Call `figma_capture_screenshot` on the component set and verify it looks correct. Iterate up to three times.
6. Record the Figma node ID and component name in the build log.

For judgment: propose any value that the component library does not specify (e.g. padding not listed). Options: two values consistent with the token scale. A person decides. Mark in the build log as To verify.

### Step 4 — Molecule build

**Mechanical.** For each molecule, build it by composing the atoms already created. Use `figma_execute` to create a new component frame and place instances of the atom components inside it. Bind layout (auto-layout, gap, padding) to spacing tokens. Add state variants. Screenshot and verify. Record in the build log.

Never create a molecule from scratch if the required atom has not been built. If an atom is missing, stop at that molecule, log the gap, and proceed to the next.

### Step 5 — Organism build

**Mechanical.** For each organism, compose it from the molecules and atoms already created. Follow the same pattern: auto-layout, variable binding, state variants, screenshot. Record in the build log.

### Step 6 — Accessibility annotation

**Mechanical.** For each built component, add a Figma annotation (using `figma_set_annotations` if available, or a sticky note layer) with the ARIA role, accessible name source, and keyboard interaction from the accessibility spec. If the accessibility spec is missing, mark each component annotation as To verify.

### Step 7 — Component placement on artboards

**Judgment.** For each screen artboard set up by skill 26, place component instances according to the canvas brief. Use `figma_execute` to create instances and position them within the Header, Content, or Footer sub-frame. Apply the correct variant for the screen's initial state (from the canvas brief's States section). Propose the layout arrangement per the grid from `foundations.md`. A designer confirms the placement before the screen is considered built.

### Step 8 — Build log

**Mechanical.** Record the complete component build log: each component (CMP-NNN), its Figma node ID, which variables are bound, which states were created, any gap or To verify item, and the designer review status. Save as `09_Screens/figma-component-build-log.md`. Set status draft.

## 6. Outputs

| Output | Format | Location | File name |
|---|---|---|---|
| Figma components (atoms, molecules, organisms) in the `_Components` staging page | Figma components | Figma file | — |
| Component instances placed on screen artboards | Figma layers | Figma file | — |
| Component build log | Markdown | `09_Screens/` | figma-component-build-log.md |

## 7. Authority and gates

- May decide: how to structure the build sequence, the order atoms are built in, how to layer frame children.
- Must not decide: token values, component names, variant states, accessibility roles — all come from the component library and the accessibility spec. Must not create a new component not in the library without a person's approval.
- Escalate when: a required atom or molecule is not in the component library, a canvas brief references a component not built yet, variable bindings are not available in the file.

## 8. Quality checks

- [ ] Token verification ran and variables were confirmed before any component was built.
- [ ] Every component is named by its CMP-NNN ID.
- [ ] Every fill, stroke, spacing, and radius value is bound to a Figma variable — no hardcoded values.
- [ ] Every component has state variants: Default, Hover, Pressed, Disabled, Focus.
- [ ] Screenshot verification ran for every component and every artboard.
- [ ] Build log records every component, its node ID, bound variables, gaps, and review status.
- [ ] No component was invented — all come from the approved component library.

## 9. References

- Figma Plugin API — `figma.createComponent()`, `figma.combineAsVariants()`, variable binding API
- `figma_create_component_set` — creates component sets with variant properties
- `figma_set_fills` — binds fill colours to Figma variables
- `figma_capture_screenshot` — used after every component and artboard build for visual verification
- Skill 16 SKILL.md — component library and token definitions
- Skill 24 SKILL.md — accessibility annotations
- Skill 25 SKILL.md — canvas briefs that drive placement
- Skill 26 SKILL.md — page structure this skill builds into
