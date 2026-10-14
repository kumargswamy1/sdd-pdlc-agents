# .github/scripts — Figma Extraction Tools

## Active Scripts

### `figma_requirements_pipeline.py` (MAIN — v2 Parent-Crop Approach)
**Status:** ✅ Active  
**Purpose:** Extract Figma design artifacts using the parent-crop workflow

**Workflow:**
1. Fetch ONE parent JSON (complete tree, depth=4)
2. Fetch ONE parent PNG (full screenshot at scale 2.0)
3. Crop child screens locally from parent PNG using bounding boxes
4. Result: 2 API calls (90% reduction vs per-child extraction)

**Usage:**
```bash
python3 .github/scripts/figma_requirements_pipeline.py \
  --requirements-file requirement/{ProjectName}_Requirements.md \
  --out-dir output/{RUN_ID}/specify/figma \
  --download-screenshots \
  --throttle 1.5 \
  --max-retries 5
```

### Dependency Handling (Auto)
- The script checks configured Python dependencies at startup and auto-installs missing ones once.
- Installed dependencies are automatically skipped on future runs.
- Current configured dependency: `Pillow` (module `PIL`) for image cropping.
- If auto-install fails, macOS uses native `sips` fallback for cropping.
- Disable auto-install explicitly with `--no-auto-install-deps`.

**Output:**
```
output/{RUN_ID}/specify/figma/
├── json/0-*.json                    # Parent JSON only
├── png/
│   ├── 0-*.png                      # Parent PNG only
│   └── screens/
│       ├── screen1__node-id.png     # Cropped locally
│       └── ... (N child crops)
├── figma_report.md
├── effective_screens.md
└── summary.json
```

**Invoked By:**
- Figma Extractor Agent (`.github/agents/figma-extractor.agent.md`)

---

### `figma_rest_cli.py` (UTILITY)
**Status:** ✅ Active  
**Purpose:** Figma REST API wrapper with throttling and retry logic

**Key Functions:**
- `_parse_figma_url()` — Parse file key and node ID from Figma URL
- `_request_json()` — GET JSON from Figma API
- `_download_file()` — Download PNG files
- `_get_api_key()` — Load API key from env/args
- `_request_with_retry()` — Retry wrapper with exponential backoff

**Used By:**
- `figma_requirements_pipeline.py` (imports all functions)

---

## Folder Structure

```
.github/scripts/
├── figma_requirements_pipeline.py        ✅ ACTIVE (main)
├── figma_rest_cli.py                    ✅ ACTIVE (utility)
└── README.md                            (this file)
```

---

## API Call Efficiency

| Scenario | API Calls |
|----------|-----------|
| 1 Figma file (7 screens) | 2 |
| 5 Figma files | 10 |
| Daily quota (~1000) | ~50 files max |

**Previous approach:** Same 1 file = 14+ calls (now 86% reduction) ✅

---

## Rate Limit Handling

**Automatic:** Exponential backoff (1s, 2s, 4s, 8s...)  
**Manual:** Increase `--throttle` if hitting limits

```bash
# Conservative extraction
python3 .github/scripts/figma_requirements_pipeline.py \
  --requirements-file <REQ_FILE> \
  --out-dir <OUT_DIR> \
  --throttle 3.0 \
  --max-retries 8
```

---

## Development Notes

### Testing
```bash
# Syntax check
python3 -m py_compile .github/scripts/figma_requirements_pipeline.py

# Test extraction (Scan Camera)
python3 .github/scripts/figma_requirements_pipeline.py \
  --requirements-file /tmp/test_req.md \
  --out-dir output/test-scan-camera \
  --download-screenshots
```

### Dependencies
- Python 3.7+
- PIL/Pillow (auto-installed by default if missing)
- Standard library: json, re, sys, time, pathlib, typing

### Environment
```bash
# Required in .env or environment
# Get your FIGMA_API_KEY from https://www.figma.com/developers/api#access-tokens
# Store token in .env file, DO NOT commit to repository
export FIGMA_API_KEY=<your_figma_api_key_here>
```

---

## Maintenance

### When to Update
- **figma_requirements_pipeline.py:** When Figma API changes or extraction logic needs improvement
- **figma_rest_cli.py:** When API wrapper needs enhancement (throttling, retries, etc.)

### Versioning
- **Current Version:** v2 (parent-crop, 2 API calls)
- **Previous Version:** v1 (per-child, 14+ API calls) — archived in git history

---

## Data Flow (End-to-End)

```
Requirements File
    ↓
Figma Extractor Agent
  ├─→ Run: .github/scripts/figma_requirements_pipeline.py
    ├─→ Calls: figma_rest_cli.py functions
    ├─→ Output: parent JSON + parent PNG + cropped PNGs
    └─→ API Calls: 2 only ✅
         ↓
Spec Agent
    └─→ Read: parent JSON
         ↓
Plan Agent → Implement Agent
    └─→ Read: spec.md (no Figma files needed)
```

---

**Last Updated:** 2026-06-09  
**Status:** Ready for Production ✅
