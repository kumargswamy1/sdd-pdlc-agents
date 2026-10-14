---
description: Interactive workflow for user-guided Figma node selection when auto-extraction hits rate limits
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

## Two-Stage Interactive Workflow

### Stage 1: Extract Metadata Only (No Downloads)

**Command:**
```bash
python3 scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --depth 2 \
  --metadata-only
```

**Output:**
- `output/{RUN_ID}/specify/figma/figma_report.md` with status
- `childNodes` array listing all node IDs and names
- No PNG downloads (fast, one cheap API call)

**Example output structure:**
```json
{
  "status": "metadata_extracted",
  "childNodes": [
    {"id": "2555:1044189", "name": "status-bar", "type": "FRAME"},
    {"id": "2555:1044190", "name": "update-button", "type": "COMPONENT"},
    {"id": "2555:1044191", "name": "status-dialog", "type": "FRAME"},
    ...
  ],
  "childNodeCount": 15
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

### Stage 3: Download Selected Nodes Only

**Command (after user confirms):**
```bash
python3 scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --depth 4 \
  --download-screenshots \
  --node-ids "2555:1044189,2555:1044190,2555:1044191,2555:1044195"
```

**Output:**
- Only 4 nodes extracted (vs. 15 total)
- 4 JSON files in `json/screens/`
- 4 PNG files in `png/screens/`
- `figma_report.md` with SUCCESS status
- No rate limit issues (minimal API calls)

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

Agent: "🔍 Starting Stage 1: Metadata extraction..."
[Runs --metadata-only]

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

Agent: "✅ Extracting 3 nodes: status-bar, update-button, status-dialog..."
[Runs --node-ids with selected IDs]

Agent: "✅ SUCCESS! 3 JSON files + 3 PNG files ready.
Proceeding to Spec writing..."
```

---

## Checklist for Quality Assurance

When using interactive mode:

- ✅ **Audit trail**: Chat history shows what was selected
- ✅ **Traceability**: Selection linked to requirement and specification
- ✅ **Scope control**: Only approved screens documented
- ✅ **No over-extraction**: Unnecessary complexity excluded
- ✅ **Rate limit safe**: Targeted downloads avoid API errors

---

## Troubleshooting

**Q: Still hitting rate limits in Stage 3?**
- Increase `--throttle` to 2.0 or 3.0
- Reduce selected nodes (pick only highest-priority ones)

**Q: Forgot which nodes were selected?**
- Check chat history for confirmed selection
- Look for `--node-ids` command in terminal output
- Query `figma_report.md` for effective-screens table

**Q: Need to add more nodes later?**
- Re-run Stage 1: `--metadata-only` to get full list
- Compare with previous selection
- Run Stage 3 with expanded `--node-ids` list

**Q: Not sure if node is needed?**
- Check requirement file for matching keywords
- Ask: "Does this node contribute to requirement logic or just decoration?"
- If decorative → skip it
- If required → include it

---

## Example: Full Workflow

**Step 1: Get metadata**
```bash
python3 scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --metadata-only
```

**Output in chat:**
- List of effective nodes
- AI suggests relevant ones based on requirement
- User confirms selection

**Step 2: Download selected**
```bash
python3 scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --depth 4 \
  --download-screenshots \
  --node-ids "2555:1044189,2555:1044190,2555:1044191,2555:1044195"
```

**Output:**
- Node JSON files (components, layout, states)
- 4 PNG files (visual evidence)
- Ready for Spec Agent

---
