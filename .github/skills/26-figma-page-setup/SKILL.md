---
name: 26-figma-page-setup
description: Creates the Figma file structure for a project — named pages per flow, artboard frames at each breakpoint with auto-layout sub-frames, and a component staging area. Requires the Desktop Bridge plugin and a Figma file URL.
allowed-tools: Read Write Edit Glob figma_execute figma_navigate figma_get_status figma_capture_screenshot
---

# 26. Figma page setup

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 26, CAP-26 Figma page setup |
| Phase or scope | Design — Figma canvas |
| Work nature mix | Mechanical 8; Judgment 4 |
| Authority level | Prepares. Creates the structural scaffolding only — no content, no components, no tokens applied. A designer populates the artboards and a design lead reviews the structure. |
| Handoffs in | Skill 25 (canvas briefs), Skill 15 (IA flows) |
| Handoffs out | Skill 27 (build Figma components) |
| Human gate after | Design lead confirms the page structure before skill 27 begins component build |
| Used by | AG-03 Experience agent |
| Version and date | 0.1, 2026-10-14, draft |

## 2. Purpose

Creates an empty but correctly structured Figma file: one page per flow, artboard frames at every breakpoint with named auto-layout sub-frames (header, content, footer), and a _Components staging page. This scaffold ensures all designers work from the same frame names and hierarchy, and that skill 27 has a predictable structure to build into.

## 3. When to use

Use after the canvas briefs from skill 25 are approved and a Figma file URL has been provided. Run before skill 27. The user must confirm the Desktop Bridge plugin is running before this skill executes any Figma API calls.

**Before running any Figma steps:** confirm with the user that the Desktop Bridge plugin is running in Figma Desktop (right-click Figma → Plugins → Development → Figma Desktop Bridge). If it is not running, stop and provide this instruction. Ask the user for their Figma file URL if not already provided.

## 4. Inputs

| Input | Source | Required or optional | If missing |
|---|---|---|---|
| Canvas briefs: `09_Screens/canvas-briefs/SCR-NNN-canvas-brief.md` | Skill 25 | Required | Stop and ask |
| IA flows: `07_Architecture/ia/` | Skill 15 | Required | Stop and ask |
| Figma file URL | Person provides | Required | Stop and ask. Never guess or construct a URL. |
| Desktop Bridge plugin running | Person confirms | Required | Stop and provide setup instructions |

## 5. Method

**Screen sizes:** Mobile 390×844 px. Tablet 768×1024 px. Desktop 1440×900 px.

### Step 1 — File navigation

**Mechanical.** Call `figma_navigate(url)` with the URL the user provided. Confirm the file is reachable. If navigation fails, stop and report the error.

### Step 2 — Page inventory

**Mechanical.** List the existing pages in the file using `figma_execute`. Ask the user whether to add pages to the existing file or whether to start fresh. Never delete an existing page without explicit confirmation from the user — list what exists and ask.

### Step 3 — Page creation

**Mechanical.** Create one Figma page per flow from the IA. Name each page after the flow using the flow ID and name from the IA (e.g. `Flow 01 — FX Rate Lock`). Add one page named `_Components` for the component staging area. Add one page named `_Tokens` if it does not already exist. Use `figma_execute` to create pages via the Figma Plugin API:

```javascript
const page = figma.createPage();
page.name = 'Flow 01 — FX Rate Lock';
```

### Step 4 — Artboard frames

**Mechanical.** On each flow page, create one artboard frame per screen in that flow, at each breakpoint: Mobile (390×844), Tablet (768×1024), Desktop (1440×900). Name each frame using the screen ID and breakpoint: `SCR-001 / Mobile`, `SCR-001 / Tablet`, `SCR-001 / Desktop`. Use auto-layout (vertical, fill container width) and set the frame background to the surface token colour if tokens have been pushed to the file. Use `figma_execute`:

```javascript
const frame = figma.createFrame();
frame.name = 'SCR-001 / Mobile';
frame.resize(390, 844);
frame.layoutMode = 'VERTICAL';
frame.primaryAxisSizingMode = 'FIXED';
frame.counterAxisSizingMode = 'FIXED';
page.appendChild(frame);
```

### Step 5 — Sub-frame structure

**Mechanical.** Inside each artboard frame, create three named auto-layout sub-frames: `Header`, `Content`, `Footer`. Set `Header` height to 56 px (mobile), 64 px (tablet), 72 px (desktop). Set `Footer` height to 80 px. Set `Content` to fill the remaining height (use `layoutGrow: 1`). All sub-frames fill the full width of the artboard. Use `figma_execute` for each frame.

### Step 6 — Component staging area

**Mechanical.** On the `_Components` page, create a Section named `Atoms`, a Section named `Molecules`, and a Section named `Organisms`. Leave them empty — skill 27 will populate them. Position them left to right with 200 px gaps.

### Step 7 — Screenshot and verification

**Mechanical.** Call `figma_capture_screenshot` on each flow page to confirm the artboard structure looks correct. Report any frame that is missing or incorrectly sized. A designer reviews the page structure before skill 27 begins.

### Step 8 — Page setup log

**Mechanical.** Record what was created: pages, frames per page, sub-frame structure, any gap. Save as `09_Screens/figma-setup-log.md`. Set status draft.

## 6. Outputs

| Output | Format | Location | File name |
|---|---|---|---|
| Figma pages and artboard frames (in Figma) | Figma file structure | Figma file | — |
| Page setup log | Markdown | `09_Screens/` | figma-setup-log.md |

## 7. Authority and gates

- May decide: how to position frames on a page, the gap between artboards.
- Must not decide: whether to delete existing pages (always ask), which flows to create pages for (from the IA), which breakpoints to build (hardcoded: Mobile/Tablet/Desktop).
- Escalate when: the Figma file is not reachable, an existing page conflicts with a new page name, the user asks to skip a breakpoint.

## 8. Quality checks

- [ ] `figma_navigate` succeeded and the file URL was provided by the user.
- [ ] One page exists per IA flow, plus `_Components` and `_Tokens`.
- [ ] Every screen in every flow has three artboard frames: Mobile, Tablet, Desktop.
- [ ] Every artboard has Header, Content, Footer sub-frames at the correct heights.
- [ ] No existing page was deleted without explicit user confirmation.
- [ ] Screenshot confirmed the structure before skill 27 was invoked.
- [ ] Page setup log exists with status draft.

## 9. References

- Figma Plugin API — `figma.createPage()`, `figma.createFrame()`, `figma.createSection()`
- Skill 25 SKILL.md — provides canvas briefs and screen IDs
- Skill 27 SKILL.md — consumes this structure for component build
- Figma Desktop Bridge plugin — required for all `figma_execute` calls
