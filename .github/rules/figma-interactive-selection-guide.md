---
description: User-guided screen scope selection from parent-crop Figma artifacts.
---

# Figma Interactive Selection Guide

## When to Use Interactive Mode

**Use interactive selection when:**
- Figma file is large and hits HTTP 429 rate limit errors
- You need user control over design scope (banking compliance requirement)
- Requirement only uses subset of available screens (avoid over-extraction)
- You want audit trail of what was selected and why

**Use auto-extraction when:**
- Figma file is small (< 10 screens)
- No rate limit issues
- You need all screens in design

---

## Screen Selection Workflow

### Stage 1: Extract Parent Artifacts and Local Screen Crops

Selection controls which screens enter the specification, not which children are fetched individually. The current pipeline does not implement metadata-only, depth-selection, or node-selection CLI modes. Use its supported parent-crop command; do not invent flags.

**Command:**
```bash
python3 .github/scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --download-screenshots \
  --throttle 1.5 \
  --max-retries 5
```

**Output:**
- `figma_report.md`, `effective_screens.md`, and `summary.json` with per-URL status and artifact paths
- Parent JSON at each `results[].nodeJson` path, and parent PNG at `results[].screenshotPng`
- Local child crops under `png/screens/`; no per-screen JSON

**Example parent-crop summary entry (paths are illustrative):**
```json
{
  "status": "ok",
  "nodeJson": "output/example/specify/figma/json/2555-1044188.json",
  "screenshotPng": "output/example/specify/figma/png/2555-1044188.png",
  "apiCallsTotal": 2
}
```

---

### Stage 2: User Reviews & Selects Nodes (Chat Interface)

**Present list to user in checklist format:**

```
📋 EFFECTIVE CHILD NODES - SELECT ONES TO EXTRACT:

Based on requirement: "Feature requirement description", AI suggests:

Requirement mentions:
- Status workflow & visual progression
- Update button interaction
- Dialog/popup confirmation

AI Pre-selected: ✅ (checked)
```

| Pre-selected | Node ID | Name | Type | AI Rationale |
|---|---|---|---|---|
| ☑️ | 2555:1044189 | status-bar | FRAME | Displays status progression |
| ☑️ | 2555:1044190 | update-button | COMPONENT | User action to update status |
| ☑️ | 2555:1044191 | status-dialog | FRAME | Popup for status selection |
| ☐ | 2555:1044192 | close-button | COMPONENT | Optional confirmation |
| ☐ | 2555:1044193 | legend-component | COMPONENT | Decorative legend |
| ☐ | 2555:1044194 | help-text | TEXT | Informational only |
| ☑️ | 2555:1044195 | error-state | FRAME | Error handling UI |

**User reviews and adjusts selections, then confirms:**

> "I reviewed against the requirement. I need 2555:1044189, 2555:1044190, 2555:1044191, and 2555:1044195. Ready to download."

---

### Stage 3: Document Confirmed Screen Scope

Record selected and excluded screen IDs, requirement references, and rationale in spec.md. Read the selected screens' subtrees from the existing parent JSON and link the existing local crops. Do not download individual child nodes or request per-screen JSON.

**Output:**
- Four selected screen sections in spec.md for this example
- References to four existing crops in `png/screens/`
- Explicit exclusion reasons for other extracted screens
- Unchanged extraction report with its actual per-URL status; selection does not relabel extraction failures as success

---

## AI Suggestion Algorithm

When presenting node list, AI analyzes:

1. **Requirement keywords** (extract from requirement file):
   - Search for: button, dialog, form, status, bar, update, popup, modal, field, label
   - Match against node names

2. **Node type filtering**:
   - `FRAME` nodes: Usually screens or major UI sections → **candidate**
   - `COMPONENT` nodes: Reusable UI pieces → **candidate** if named as interactive
   - `TEXT`, `SHAPE`, `ELLIPSE`: Usually decorative → **lower priority** unless specifically named
   - `GROUP`: Often containers → **candidate** if named meaningfully

3. **Exclude patterns**:
   - "section", "header", "divider", "spacer", "grid", "label", "legend"
   - "annotation", "reference", "guide", "helper"

4. **Scoring**:
   - Full match (e.g., requirement says "status bar" → node named "status-bar"): **+2 points**
   - Partial match (e.g., requirement says "update" → node named "update-button"): **+1 point**
   - Type is FRAME or interactive COMPONENT: **+1 point**
   - Type is TEXT or decorative: **-1 point**

5. **Pre-select** nodes with score ≥ 1

---

## Chat Interface Integration

**Example conversation flow:**

```
User: "Run ICTEST-17122 extraction"

Agent: "Starting parent-crop extraction..."
[Runs the supported parent-crop command]

Agent: "✅ Found 15 effective child nodes.

📋 PLEASE SELECT NODES TO EXTRACT:

Requirement ICTEST-17122 mentions: status workflow, update button, 
confirmation dialog.

AI Pre-selected (based on requirement analysis):

☑️ status-bar (FRAME) — matches 'status workflow'
☑️ update-button (COMPONENT) — interactive element
☑️ status-dialog (FRAME) — matches 'confirmation dialog'
☐ close-button (COMPONENT)
☐ legend-component (COMPONENT)
...

Reply with: 'extract' to confirm, or edit selection.
"

User: "extract"

Agent: "Documenting 3 selected screen scopes from existing artifacts..."
[Records confirmed selections and exclusions in spec.md]

Agent: "Selected screen sections reference the parent JSON and local crops.
Proceeding to Spec writing..."
```

---

## Checklist for Quality Assurance

When using interactive mode:

- ✅ **Audit trail**: Chat history shows what was selected
- ✅ **Traceability**: Selection linked to requirement and specification
- ✅ **Scope control**: Only approved screens documented
- ✅ **No over-extraction**: Unnecessary complexity excluded
- Parent-crop avoids per-child calls, but retries and rate limits remain possible

---

## Troubleshooting

**Q: Still hitting rate limits during extraction?**
- Increase `--throttle` to 2.0 or 3.0
- Reuse existing parent artifacts when valid instead of repeating extraction for scope selection

**Q: Forgot which nodes were selected?**
- Check chat history for confirmed selection
- Check the selected/excluded screen decisions in spec.md
- Query `figma_report.md` for effective-screens table

**Q: Need to add more nodes later?**
- Review existing parent artifacts and compare with the previous selection
- Update confirmed screen scope and exclusions in spec.md
- Re-run the supported extraction command only if required source artifacts are missing or stale

**Q: Not sure if node is needed?**
- Check requirement file for matching keywords
- Ask: "Does this node contribute to requirement logic or just decoration?"
- If decorative → skip it
- If required → include it

---

## Example: Full Workflow

**Step 1: Extract parent artifacts**
```bash
python3 .github/scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --download-screenshots
```

**Output in chat:**
- List of effective nodes
- AI suggests relevant ones based on requirement
- User confirms selection

**Step 2: Document selected screens**

Use confirmed IDs to select subtrees from parent JSON and reference existing crops in spec.md. Preserve extraction status and report missing data; no additional child-download command is required.

**Output:**
- Self-contained screen sections with component, layout, state, and visual evidence
- All screenshot references resolve to existing local crops
- Logical API counts are per URL, not fixed at two per run. `totalApiCalls` excludes retries, image downloads, and potentially operations before failed results; it is not measured HTTP-attempt usage.

---
