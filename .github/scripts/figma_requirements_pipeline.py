#!/usr/bin/env python3
"""Extract Figma URLs from requirement files using parent-crop approach.

NEW WORKFLOW (v2):
  1. Fetch ONE parent JSON (depth=4, full tree)
  2. Fetch ONE parent PNG (screenshot)
  3. Crop child screens locally from parent PNG using bounding boxes
  4. No per-child API calls → no rate limits

Example:
    python3 .github/scripts/figma_requirements_pipeline.py \
    --requirements-file requirementICTEST-17122_Requirements.md \
    --out-dir output/ICTEST-17122_20260609/specify/figma \
    --download-screenshots

Auth:
  Set FIGMA_API_KEY in environment or pass --api-key.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Set

from figma_rest_cli import (  # type: ignore
    _load_dotenv,
    _parse_figma_url,
    _request_json,
    _download_file,
    _get_api_key,
)

FIGMA_URL_RE = re.compile(r"https?://(?:www\.)?figma\.com/[^\s)\]>\"']+", re.IGNORECASE)

EXCLUDE_NAME_RE = re.compile(
    r"(section\s*title|header|connector|area\s*label|decorative|wrapper|handoff|doc(umentation)?|guide)",
    re.IGNORECASE,
)

INTERNAL_COMPONENT_RE = re.compile(
    r"(icon-button|jira\s*link|\blink\b|bottom\s*navigation|lower-action|select-zoom-scale|\bbody\b)",
    re.IGNORECASE,
)

INTERACTIVE_NAME_RE = re.compile(
    r"(button|btn|input|textfield|dropdown|select|radio|checkbox|toggle|tab|link|cta|search|chip|switch)",
    re.IGNORECASE,
)


def _ensure_python_dependency(module_name: str, pip_package: str, auto_install: bool = True) -> bool:
    """Ensure a Python dependency exists. Install via pip once if missing and allowed."""
    if importlib.util.find_spec(module_name) is not None:
        return True

    if not auto_install:
        return False

    print(f"[Info] Missing dependency '{module_name}'. Installing '{pip_package}'...", file=sys.stderr)
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        pip_package,
        "--disable-pip-version-check",
        "--quiet",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        return importlib.util.find_spec(module_name) is not None

    print(f"[Warn] Auto-install failed for '{pip_package}'.", file=sys.stderr)
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    return False


def _bootstrap_optional_dependencies(download_screenshots: bool, auto_install_deps: bool) -> None:
    """Install optional runtime dependencies when needed.

    Keep this list small and explicit. Add future third-party deps here.
    """
    if not download_screenshots:
        return

    # Pillow is preferred for image handling. If it is unavailable, macOS sips fallback still works.
    _ensure_python_dependency("PIL", "Pillow", auto_install=auto_install_deps)


def _request_with_retry(
    endpoint: str,
    api_key: str,
    params: Dict[str, object],
    max_retries: int = 3,
    throttle: float = 0.5,
) -> Dict[str, object]:
    """Wrapper around _request_json with retry logic for rate limits (429)."""
    time.sleep(throttle)

    for attempt in range(max_retries):
        try:
            return _request_json(endpoint, api_key, params)
        except Exception as exc:
            error_str = str(exc).lower()
            is_rate_limit = "429" in error_str or "rate" in error_str
            is_last_attempt = attempt == max_retries - 1

            if is_rate_limit and not is_last_attempt:
                wait_time = 2 ** attempt
                print(
                    f"  [Throttle] Rate limit (429) - retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})",
                    file=sys.stderr,
                )
                time.sleep(wait_time)
                continue

            raise


def _walk_nodes(node: Dict[str, object]) -> List[Dict[str, object]]:
    out = [node]
    children = node.get("children")
    if isinstance(children, list):
        for child in children:
            if isinstance(child, dict):
                out.extend(_walk_nodes(child))
    return out


def _walk_nodes_with_depth(
    node: Dict[str, object],
    depth: int = 0,
    parent_frame_name: str = "",
) -> List[tuple[Dict[str, object], int, str]]:
    node_type = str(node.get("type", "")).upper()
    current_frame_name = parent_frame_name
    if node_type == "FRAME" and depth <= 2:
        candidate_name = str(node.get("name", "")).strip()
        if candidate_name and not EXCLUDE_NAME_RE.search(candidate_name):
            current_frame_name = candidate_name
    out = [(node, depth, current_frame_name)]
    children = node.get("children")
    if isinstance(children, list):
        for child in children:
            if isinstance(child, dict):
                out.extend(_walk_nodes_with_depth(child, depth + 1, current_frame_name))
    return out


def _build_sibling_label_map(root_node: Dict[str, object]) -> Dict[str, str]:
    label_map: Dict[str, str] = {}
    children = root_node.get("children")
    if not isinstance(children, list):
        return label_map
    last_text_label = ""
    for child in children:
        if not isinstance(child, dict):
            continue
        node_type = str(child.get("type", "")).upper()
        if node_type == "TEXT":
            last_text_label = str(child.get("name", child.get("characters", ""))).strip()
        elif node_type in {"FRAME", "INSTANCE", "COMPONENT"}:
            node_id = str(child.get("id", "")).strip()
            if node_id and last_text_label:
                label_map[node_id] = last_text_label
    return label_map


def _is_interactive_node(node: Dict[str, object]) -> bool:
    node_type = str(node.get("type", "")).upper()
    name = str(node.get("name", ""))
    if INTERACTIVE_NAME_RE.search(name):
        return True
    if node_type in {"INSTANCE", "COMPONENT"} and INTERACTIVE_NAME_RE.search(name):
        return True
    reactions = node.get("reactions")
    if isinstance(reactions, list) and len(reactions) > 0:
        return True
    return False


def _screen_metrics(node: Dict[str, object]) -> Dict[str, int | bool]:
    descendants = _walk_nodes(node)
    text_count = 0
    interactive_count = 0
    for item in descendants:
        node_type = str(item.get("type", "")).upper()
        if node_type == "TEXT":
            text_count += 1
        if _is_interactive_node(item):
            interactive_count += 1

    children = node.get("children")
    child_count = len(children) if isinstance(children, list) else 0
    return {
        "textCount": text_count,
        "interactiveCount": interactive_count,
        "childCount": child_count,
        "hasInteractive": interactive_count > 0,
        "hasCompleteInfo": text_count >= 3 and child_count >= 2,
    }


def _variant_suffix(node: Dict[str, object]) -> str:
    props = node.get("componentProperties")
    if not isinstance(props, dict):
        return ""
    parts = []
    for val in props.values():
        if isinstance(val, dict) and val.get("type") == "VARIANT":
            v = str(val.get("value", "")).strip()
            if v and v.lower() not in ("default", ""):
                parts.append(v)
    return "_".join(parts)


def _get_node_size(node: Dict[str, object]) -> tuple[float | None, float | None]:
    box = node.get("absoluteBoundingBox")
    if isinstance(box, dict):
        width = box.get("width")
        height = box.get("height")
        if isinstance(width, (int, float)) and isinstance(height, (int, float)):
            return float(width), float(height)
    return None, None


def _is_screen_level_candidate(node_id: str, depth: int, width: float | None, height: float | None) -> bool:
    if ";" in node_id:
        return False
    if depth > 2:
        return False
    if width is not None and height is not None:
        if width < 240 or height < 320:
            return False
    return True


def _build_node_link(file_key: str, node_id: str) -> str:
    return f"https://www.figma.com/design/{file_key}/auto?node-id={node_id.replace(':', '-')}"


def _extract_effective_screens(file_key: str, root_node: Dict[str, object]) -> List[Dict[str, object]]:
    sibling_labels = _build_sibling_label_map(root_node)
    candidates: List[Dict[str, object]] = []
    for node, depth, parent_frame_name in _walk_nodes_with_depth(root_node):
        node_type = str(node.get("type", "")).upper()
        name = str(node.get("name", "")).strip()
        node_id = str(node.get("id", "")).strip()
        if not node_id:
            continue

        if node_type not in {"FRAME", "INSTANCE", "COMPONENT"}:
            continue
        if EXCLUDE_NAME_RE.search(name):
            continue
        if INTERNAL_COMPONENT_RE.search(name):
            continue

        width, height = _get_node_size(node)
        if not _is_screen_level_candidate(node_id=node_id, depth=depth, width=width, height=height):
            continue

        metrics = _screen_metrics(node)
        if not (metrics["hasInteractive"] or metrics["hasCompleteInfo"]):
            continue

        variant = _variant_suffix(node)
        candidates.append(
            {
                "nodeId": node_id,
                "name": name,
                "variantSuffix": variant,
                "parentFrameName": sibling_labels.get(node_id, parent_frame_name),
                "type": node_type,
                "link": _build_node_link(file_key, node_id),
                "textCount": metrics["textCount"],
                "interactiveCount": metrics["interactiveCount"],
                "childCount": metrics["childCount"],
            }
        )

    seen_ids: Set[str] = set()
    name_counts: Dict[str, int] = {}
    effective = []
    for item in candidates:
        node_id = str(item["nodeId"])
        if node_id in seen_ids:
            continue
        seen_ids.add(node_id)
        parent = str(item.get("parentFrameName", "")).strip()
        base = str(item.get("name", "")).strip()
        variant = str(item.get("variantSuffix", "")).strip()
        display_parts = [p for p in [base, variant] if p]
        display_name = "_".join(display_parts)
        count = name_counts.get(display_name, 0) + 1
        name_counts[display_name] = count
        if count > 1:
            item["displayName"] = f"{display_name}_{count}"
        else:
            item["displayName"] = display_name
        effective.append(item)
    return effective


def _crop_child_pngs_from_parent(
    parent_png_path: Path,
    root_node: Dict[str, object],
    effective_screens: List[Dict[str, object]],
    out_dir: Path,
    auto_install_deps: bool = True,
) -> List[Dict[str, object]]:
    """Crop child screen PNGs from parent PNG using bounding boxes from JSON."""
    image_module = None
    using_sips_fallback = False

    def load_image_module() -> object | None:
        try:
            from PIL import Image as pil_image

            return pil_image
        except ImportError:
            if _ensure_python_dependency("PIL", "Pillow", auto_install=auto_install_deps):
                try:
                    from PIL import Image as pil_image

                    return pil_image
                except ImportError:
                    return None
            return None

    try:
        image_module = load_image_module()
        if image_module is None:
            raise ImportError("Pillow unavailable")
    except ImportError:
        if shutil.which("sips"):
            using_sips_fallback = True
            print(
                "[Info] Pillow is not installed; using macOS 'sips' fallback for screen cropping.",
                file=sys.stderr,
            )
        else:
            print(
                "ERROR: Pillow is not installed and 'sips' is unavailable. "
                "Install Pillow or run on macOS with sips.",
                file=sys.stderr,
            )
            return []

    def get_png_dimensions(png_path: Path) -> tuple[int, int] | None:
        if image_module is not None:
            img = image_module.open(png_path)
            return int(img.size[0]), int(img.size[1])

        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(png_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            return None

        width = None
        height = None
        for line in result.stdout.splitlines():
            line = line.strip()
            if "pixelWidth:" in line:
                width = int(line.split(":", 1)[1].strip())
            elif "pixelHeight:" in line:
                height = int(line.split(":", 1)[1].strip())
        if width is None or height is None:
            return None
        return width, height

    def crop_with_sips(
        source_png: Path,
        target_png: Path,
        left_px: int,
        top_px: int,
        width_px: int,
        height_px: int,
    ) -> bool:
        cmd = [
            "sips",
            "-c",
            str(height_px),
            str(width_px),
            str(source_png),
            "--cropOffset",
            str(top_px),
            str(left_px),
            "--out",
            str(target_png),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode == 0

    # Compute canvas bounds from all child nodes
    all_x, all_y = [], []
    all_x_max, all_y_max = [], []

    def collect_bounds(node: Dict[str, object]) -> None:
        if not isinstance(node, dict):
            return
        box = node.get("absoluteBoundingBox")
        if isinstance(box, dict):
            x, y, w, h = box.get("x"), box.get("y"), box.get("width"), box.get("height")
            if all(isinstance(v, (int, float)) for v in [x, y, w, h]):
                all_x.append(x)
                all_y.append(y)
                all_x_max.append(x + w)
                all_y_max.append(y + h)
        children = node.get("children")
        if isinstance(children, list):
            for child in children:
                collect_bounds(child)

    collect_bounds(root_node)
    if not all_x:
        print("ERROR: No bounding boxes found in JSON", file=sys.stderr)
        return []

    canvas_x_min = min(all_x)
    canvas_y_min = min(all_y)
    canvas_x_max = max(all_x_max)
    canvas_y_max = max(all_y_max)
    canvas_w = canvas_x_max - canvas_x_min
    canvas_h = canvas_y_max - canvas_y_min

    # Load parent PNG and compute scale
    dims = get_png_dimensions(parent_png_path)
    if dims is None:
        print("ERROR: Unable to read parent PNG dimensions for cropping", file=sys.stderr)
        return []
    img_w, img_h = dims
    scale_x = img_w / canvas_w if canvas_w > 0 else 1
    scale_y = img_h / canvas_h if canvas_h > 0 else 1

    # Crop each effective screen from parent PNG
    cropped = []
    crops_dir = out_dir / "png" / "screens"
    crops_dir.mkdir(parents=True, exist_ok=True)

    def find_node(node: Dict[str, object], target_id: str) -> Dict[str, object] | None:
        if not isinstance(node, dict):
            return None
        if str(node.get("id", "")).strip() == target_id:
            return node
        children = node.get("children")
        if isinstance(children, list):
            for child in children:
                found = find_node(child, target_id)
                if found:
                    return found
        return None

    for screen in effective_screens:
        screen_id = str(screen.get("nodeId", "")).strip()
        if not screen_id:
            continue

        node = find_node(root_node, screen_id)
        if not node:
            continue

        box = node.get("absoluteBoundingBox")
        if not box:
            continue

        x, y, w, h = box.get("x"), box.get("y"), box.get("width"), box.get("height")
        if not all(isinstance(v, (int, float)) for v in [x, y, w, h]):
            continue

        left = int(round((float(x) - canvas_x_min) * scale_x))
        top = int(round((float(y) - canvas_y_min) * scale_y))
        right = int(round(left + float(w) * scale_x))
        bottom = int(round(top + float(h) * scale_y))

        left = max(0, min(left, img_w))
        top = max(0, min(top, img_h))
        right = max(left, min(right, img_w))
        bottom = max(top, min(bottom, img_h))

        if right <= left or bottom <= top:
            continue

        crop_w = right - left
        crop_h = bottom - top
        if crop_w <= 0 or crop_h <= 0:
            continue

        name = str(screen.get("displayName", screen.get("name", "screen")))
        safe = "".join(ch if ch.isalnum() or ch in ("_", "-") else "_" for ch in name).strip("_") or screen_id.replace(":", "-")
        out_path = crops_dir / f"{safe}__{screen_id.replace(':', '-')}.png"

        if using_sips_fallback:
            ok = crop_with_sips(
                source_png=parent_png_path,
                target_png=out_path,
                left_px=left,
                top_px=top,
                width_px=crop_w,
                height_px=crop_h,
            )
            if not ok:
                continue
            crop_size = [crop_w, crop_h]
        else:
            crop = image_module.open(parent_png_path).crop((left, top, right, bottom))
            crop.save(out_path)
            crop_size = [crop.size[0], crop.size[1]]

        cropped.append({
            "nodeId": screen_id,
            "name": name,
            "png": str(out_path),
            "cropBox": [left, top, right, bottom],
            "cropSize": crop_size,
        })

    return cropped


def _safe_filename(name: str, node_id: str) -> str:
    safe_name = re.sub(r"[^\w\s-]", "", name).strip()
    safe_name = re.sub(r"[\s/\\]+", "_", safe_name)
    safe_id = node_id.replace(":", "-").replace(";", "__")
    return f"{safe_name}__{safe_id}" if safe_name else safe_id


def extract_figma_urls(text: str) -> List[str]:
    seen = set()
    ordered = []
    for match in FIGMA_URL_RE.findall(text):
        url = match.strip().rstrip(".,;")
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    return ordered


def collect_for_url(
    api_key: str,
    url: str,
    out_dir: Path,
    download_screenshots: bool = True,
    screenshot_scale: float = 2.0,
    throttle: float = 1.5,
    max_retries: int = 5,
    auto_install_deps: bool = True,
) -> Dict[str, object]:
    """Collect Figma artifacts using parent-crop approach."""
    result: Dict[str, object] = {"url": url}
    file_key, node_id = _parse_figma_url(url)
    result["fileKey"] = file_key
    result["nodeId"] = node_id

    if not node_id:
        result["status"] = "skipped"
        result["reason"] = "No node-id in URL"
        return result

    print(f"[1/3] Fetching parent JSON...", file=sys.stderr)
    try:
        node_data = _request_with_retry(
            f"/files/{file_key}/nodes",
            api_key,
            {"ids": node_id, "depth": 4},
            max_retries=max_retries,
            throttle=throttle,
        )
    except Exception as exc:
        result["status"] = "error"
        result["error"] = f"Failed to fetch parent JSON: {exc}"
        return result

    node_json_path = out_dir / "json" / f"{node_id.replace(':', '-')}.json"
    node_json_path.parent.mkdir(parents=True, exist_ok=True)
    node_json_path.write_text(json.dumps(node_data, indent=2), encoding="utf-8")
    result["nodeJson"] = str(node_json_path)
    print(f"✓ Saved parent JSON: {node_json_path}", file=sys.stderr)

    node_map = node_data.get("nodes") or {}
    node_obj = node_map.get(node_id) or {}
    root = node_obj.get("document")
    if not isinstance(root, dict):
        result["status"] = "error"
        result["error"] = "Missing root document in node response"
        return result

    print(f"[2/3] Extracting effective screens...", file=sys.stderr)
    effective_screens = _extract_effective_screens(file_key=file_key, root_node=root)
    result["effectiveScreens"] = effective_screens
    print(f"✓ Found {len(effective_screens)} effective screens", file=sys.stderr)

    if download_screenshots:
        print(f"[3/3] Fetching parent PNG...", file=sys.stderr)
        try:
            image_data = _request_with_retry(
                f"/images/{file_key}",
                api_key,
                {"ids": node_id, "format": "png", "scale": screenshot_scale},
                max_retries=max_retries,
                throttle=throttle,
            )
        except Exception as exc:
            result["status"] = "error"
            result["error"] = f"Failed to fetch parent PNG: {exc}"
            return result

        image_url = (image_data.get("images") or {}).get(node_id)
        if not image_url:
            result["status"] = "error"
            result["error"] = "No screenshot URL returned for parent node"
            return result

        parent_png_path = out_dir / "png" / f"{node_id.replace(':', '-')}.png"
        parent_png_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            _download_file(image_url, parent_png_path, api_key)
        except Exception as exc:
            result["status"] = "error"
            result["error"] = f"Failed to download parent PNG: {exc}"
            return result

        result["screenshotPng"] = str(parent_png_path)
        result["screenshotUrl"] = image_url
        print(f"✓ Saved parent PNG: {parent_png_path}", file=sys.stderr)

        print(f"[4/3] Cropping child screens locally...", file=sys.stderr)
        cropped = _crop_child_pngs_from_parent(
            parent_png_path=parent_png_path,
            root_node=root,
            effective_screens=effective_screens,
            out_dir=out_dir,
            auto_install_deps=auto_install_deps,
        )
        result["croppedScreens"] = cropped
        print(f"✓ Cropped {len(cropped)} screens from parent PNG", file=sys.stderr)
    else:
        result["croppedScreens"] = []

    result["status"] = "ok"
    result["apiCallsTotal"] = 2 if download_screenshots else 1
    print(f"✓ Total API calls: {result['apiCallsTotal']} (no per-child calls)", file=sys.stderr)

    return result


def _write_figma_report(summary: Dict[str, object], out_path: Path) -> None:
    results = summary.get("results") if isinstance(summary.get("results"), list) else []
    errors: List[str] = []
    for item in results:
        if isinstance(item, dict) and item.get("status") in {"error", "skipped"}:
            reason = item.get("error") or item.get("reason") or "Unknown error"
            errors.append(f"- {item.get('url', 'unknown-url')}: {reason}")

    status = "SUCCESS" if not errors else "FAILED"

    lines = [
        "# Figma Extraction Report (Parent-Crop v2)",
        "",
        f"Status: {status}",
        "",
        "## Extraction Method",
        "- ONE parent JSON call (complete tree, depth=4)",
        "- ONE parent PNG call (full screenshot)",
        "- Local PNG cropping of child screens (no per-child API calls)",
        "",
        "## Parent Figma URL(s)",
    ]

    for item in results:
        if isinstance(item, dict):
            url = item.get("url")
            if url:
                lines.append(f"- {url}")

    if errors:
        lines.extend([
            "",
            "## Failure Reason(s)",
            *errors,
        ])

    effective_rows = summary.get("effectiveScreens") if isinstance(summary.get("effectiveScreens"), list) else []

    lines.extend([
        "",
        "## Effective Screens",
        "| Node ID | Screen Name | Link |",
        "|---|---|---|",
    ])

    if not effective_rows:
        lines.append("| - | - | - |")
    else:
        for row in effective_rows:
            if not isinstance(row, dict):
                continue
            node_id = str(row.get("nodeId", "")).replace("|", "\\|")
            display = str(row.get("displayName", row.get("name", ""))).replace("|", "\\|")
            link = str(row.get("link", ""))
            lines.append(f"| {node_id} | {display} | {link} |")

    lines.extend([
        "",
        "## Totals",
        f"- total effective screens: {summary.get('effectiveScreenCount', 0)}",
        f"- total API calls: {summary.get('totalApiCalls', 0)}",
    ])

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_effective_screens_table(rows: List[Dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Effective Screen Nodes",
        "",
        "| Node ID | Screen | Name | Link |",
        "|---|---|---|---|",
    ]
    for row in rows:
        node_id = str(row.get("nodeId", "")).replace("|", "\\|")
        display = str(row.get("displayName", row.get("name", ""))).replace("|", "\\|")
        link = str(row.get("link", ""))
        lines.append(f"| {node_id} | {display} | {link} |")

    if len(rows) == 0:
        lines.append("| - | - | - |")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract Figma artifacts using parent-crop approach (v2)"
    )
    parser.add_argument("--requirements-file", required=True, help="Path to requirement markdown file")
    parser.add_argument("--out-dir", required=True, help="Output directory for artifacts")
    parser.add_argument("--api-key", help="Figma API key (fallback: FIGMA_API_KEY env var)")
    parser.add_argument("--download-screenshots", action="store_true", default=True, help="Download parent PNG and crop children")
    parser.add_argument("--screenshot-scale", type=float, default=2.0, help="PNG scale (default 2)")
    parser.add_argument("--throttle", type=float, default=1.5, help="Throttle between API requests (default 1.5s)")
    parser.add_argument("--max-retries", type=int, default=5, help="Max retries for rate limit errors (default 5)")
    parser.add_argument(
        "--auto-install-deps",
        dest="auto_install_deps",
        action="store_true",
        default=True,
        help="Auto-install missing dependencies like Pillow (default: enabled)",
    )
    parser.add_argument(
        "--no-auto-install-deps",
        dest="auto_install_deps",
        action="store_false",
        help="Disable automatic dependency installation",
    )

    args = parser.parse_args()
    _load_dotenv()

    _bootstrap_optional_dependencies(
        download_screenshots=args.download_screenshots,
        auto_install_deps=args.auto_install_deps,
    )

    try:
        api_key = _get_api_key(args.api_key)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    req_path = Path(args.requirements_file)
    if not req_path.exists():
        print(f"Error: requirements file not found: {req_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    text = req_path.read_text(encoding="utf-8")
    urls = extract_figma_urls(text)

    if not urls:
        print(f"Error: no Figma URLs found in {req_path}", file=sys.stderr)
        return 1

    summary = {
        "requirementsFile": str(req_path),
        "urlCount": len(urls),
        "results": [],
        "totalApiCalls": 0,
    }

    all_effective_screens: List[Dict[str, object]] = []

    for url in urls:
        print(f"\n{'='*70}", file=sys.stderr)
        print(f"Extracting: {url}", file=sys.stderr)
        print(f"{'='*70}", file=sys.stderr)
        try:
            item = collect_for_url(
                api_key=api_key,
                url=url,
                out_dir=out_dir,
                download_screenshots=args.download_screenshots,
                screenshot_scale=args.screenshot_scale,
                throttle=args.throttle,
                max_retries=args.max_retries,
                auto_install_deps=args.auto_install_deps,
            )
        except Exception as exc:
            item = {
                "url": url,
                "status": "error",
                "error": str(exc),
            }
            print(f"ERROR: {exc}", file=sys.stderr)

        summary["results"].append(item)
        if isinstance(item.get("effectiveScreens"), list):
            for screen in item["effectiveScreens"]:
                if isinstance(screen, dict):
                    all_effective_screens.append(screen)
        
        if isinstance(item.get("apiCallsTotal"), int):
            summary["totalApiCalls"] += item["apiCallsTotal"]

    # Deduplicate
    deduped: List[Dict[str, object]] = []
    seen_node_ids: Set[str] = set()
    for screen in all_effective_screens:
        node_id = str(screen.get("nodeId", ""))
        if not node_id or node_id in seen_node_ids:
            continue
        seen_node_ids.add(node_id)
        deduped.append(screen)

    summary["effectiveScreenCount"] = len(deduped)
    summary["effectiveScreens"] = deduped

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    table_path = out_dir / "effective_screens.md"
    _write_effective_screens_table(deduped, table_path)

    figma_report_path = out_dir / "figma_report.md"
    _write_figma_report(summary, figma_report_path)

    print(
        json.dumps(
            {
                "summary": str(summary_path),
                "effectiveScreensTable": str(table_path),
                "figmaReport": str(figma_report_path),
                "urlCount": len(urls),
                "effectiveScreenCount": len(deduped),
                "totalApiCalls": summary["totalApiCalls"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
