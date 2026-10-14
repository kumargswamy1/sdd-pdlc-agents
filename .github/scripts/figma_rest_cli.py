#!/usr/bin/env python3
"""Simple Figma REST CLI for JSON context and screenshot PNG exports.

Usage examples:
    python .github/scripts/figma_rest_cli.py file --file-key ABC123
    python .github/scripts/figma_rest_cli.py node --file-key ABC123 --node-id 1:2
    python .github/scripts/figma_rest_cli.py screenshot --file-key ABC123 --node-id 1:2 --out frame.png

Auth:
  - Pass --api-key, or
  - Set FIGMA_API_KEY in your environment.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Tuple

BASE_URL = "https://api.figma.com/v1"


def _repo_root() -> Path:
    # Script path: <repo>/.github/scripts/figma_rest_cli.py
    return Path(__file__).resolve().parents[2]


def _find_dotenv(explicit_path: str | None = None) -> Path | None:
    if explicit_path:
        explicit = Path(explicit_path)
        if explicit.exists() and explicit.is_file():
            return explicit

    # Fast-path: common locations.
    direct_candidates = [
        _repo_root() / ".env",
        Path.cwd() / ".env",
    ]
    for candidate in direct_candidates:
        if candidate.exists() and candidate.is_file():
            return candidate

    # Fallback: scan project tree for first .env.
    root = _repo_root()
    skip_dirs = {".git", "node_modules", "dist", "build", "output"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        if ".env" in filenames:
            return Path(dirpath) / ".env"
    return None


def _load_dotenv(path: str | None = None) -> Path | None:
    """Load FIGMA_API_KEY from a .env file (repo root preferred)."""
    env_path = _find_dotenv(path)
    if env_path is None:
        return None

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
    return env_path


def _normalize_node_id(node_id: str) -> str:
    # Figma links often use 1-2; REST API expects 1:2.
    return node_id.replace("-", ":")


def _get_api_key(explicit_api_key: str | None) -> str:
    _load_dotenv()
    api_key = explicit_api_key or os.getenv("FIGMA_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing API key. Provide --api-key, set FIGMA_API_KEY, "
            "or place FIGMA_API_KEY in a .env file at repo root/current directory."
        )
    return api_key


def _extract_file_key_from_path(path: str) -> str | None:
    parts = [p for p in path.split("/") if p]
    if not parts:
        return None

    # Remote links commonly include /design/<fileKey>/..., /file/<fileKey>/..., /board/<fileKey>/...
    for prefix in ("design", "file", "board", "slides"):
        if prefix in parts:
            idx = parts.index(prefix)
            if idx + 1 < len(parts):
                file_key = parts[idx + 1]
                # If URL has branch, Figma often expects branch key.
                if "branch" in parts:
                    bidx = parts.index("branch")
                    if bidx + 1 < len(parts):
                        return parts[bidx + 1]
                return file_key

    return None


def _parse_figma_url(url: str) -> Tuple[str, str | None]:
    parsed = urllib.parse.urlparse(url)
    if not parsed.netloc or "figma.com" not in parsed.netloc:
        raise RuntimeError("Invalid Figma URL.")

    file_key = _extract_file_key_from_path(parsed.path)
    if not file_key:
        raise RuntimeError("Unable to extract file key from URL.")

    query = urllib.parse.parse_qs(parsed.query)
    node_id = None
    if "node-id" in query and query["node-id"]:
        node_id = _normalize_node_id(query["node-id"][0])
    elif "node_id" in query and query["node_id"]:
        node_id = _normalize_node_id(query["node_id"][0])

    return file_key, node_id


def _request_json(path: str, api_key: str, query: Dict[str, Any] | None = None) -> Dict[str, Any]:
    query_string = ""
    if query:
        filtered = {k: v for k, v in query.items() if v is not None}
        query_string = "?" + urllib.parse.urlencode(filtered)

    url = f"{BASE_URL}{path}{query_string}"
    req = urllib.request.Request(url)
    req.add_header("X-Figma-Token", api_key)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {err.code} for {url}\n{body}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Network error for {url}: {err}") from err


def _download_file(url: str, out_path: Path, api_key: str) -> None:
    req = urllib.request.Request(url)
    req.add_header("X-Figma-Token", api_key)

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(resp.read())
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {err.code} while downloading {url}\n{body}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Network error while downloading {url}: {err}") from err


def cmd_me(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    data = _request_json("/me", api_key)
    print(json.dumps(data, indent=2))
    return 0


def cmd_file(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    data = _request_json(f"/files/{args.file_key}", api_key, {"depth": args.depth})
    print(json.dumps(data, indent=2))
    return 0


def cmd_node(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    node_id = _normalize_node_id(args.node_id)
    data = _request_json(
        f"/files/{args.file_key}/nodes",
        api_key,
        {"ids": node_id, "depth": args.depth},
    )
    print(json.dumps(data, indent=2))
    return 0


def cmd_image_fills(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    data = _request_json(f"/files/{args.file_key}/images", api_key)
    print(json.dumps(data, indent=2))
    return 0


def cmd_parse_url(args: argparse.Namespace) -> int:
    file_key, node_id = _parse_figma_url(args.url)
    print(
        json.dumps(
            {
                "url": args.url,
                "fileKey": file_key,
                "nodeId": node_id,
            },
            indent=2,
        )
    )
    return 0


def cmd_node_from_url(args: argparse.Namespace) -> int:
    file_key, parsed_node_id = _parse_figma_url(args.url)
    node_id = _normalize_node_id(args.node_id) if args.node_id else parsed_node_id
    if not node_id:
        raise RuntimeError("No node id found in URL. Provide --node-id.")

    ns = argparse.Namespace(
        api_key=args.api_key,
        file_key=file_key,
        node_id=node_id,
        depth=args.depth,
    )
    return cmd_node(ns)


def cmd_screenshot_from_url(args: argparse.Namespace) -> int:
    file_key, parsed_node_id = _parse_figma_url(args.url)
    node_id = _normalize_node_id(args.node_id) if args.node_id else parsed_node_id
    if not node_id:
        raise RuntimeError("No node id found in URL. Provide --node-id.")

    ns = argparse.Namespace(
        api_key=args.api_key,
        file_key=file_key,
        node_id=node_id,
        scale=args.scale,
        out=args.out,
    )
    return cmd_screenshot(ns)


def cmd_screenshot(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    node_id = _normalize_node_id(args.node_id)

    image_data = _request_json(
        f"/images/{args.file_key}",
        api_key,
        {
            "ids": node_id,
            "format": "png",
            "scale": args.scale,
        },
    )

    image_url = (image_data.get("images") or {}).get(node_id)
    if not image_url:
        print(json.dumps(image_data, indent=2))
        raise RuntimeError("No screenshot URL returned for this node. Check fileKey/nodeId permissions.")

    out_path = Path(args.out)
    _download_file(image_url, out_path, api_key)

    print(
        json.dumps(
            {
                "fileKey": args.file_key,
                "nodeId": node_id,
                "scale": args.scale,
                "imageUrl": image_url,
                "savedTo": str(out_path),
            },
            indent=2,
        )
    )
    return 0


def _fetch_paginated(path: str, api_key: str, page_size: int = 100) -> List[Dict[str, Any]]:
    cursor = None
    results: List[Dict[str, Any]] = []

    while True:
        payload = _request_json(
            path,
            api_key,
            {
                "page_size": page_size,
                "cursor": cursor,
            },
        )

        # Team endpoints usually return one collection key.
        collection = []
        for key in ("meta", "components", "styles"):
            value = payload.get(key)
            if isinstance(value, list):
                collection = value
                break

        if not collection and isinstance(payload.get("meta"), dict):
            for value in payload["meta"].values():
                if isinstance(value, list):
                    collection = value
                    break

        results.extend(collection)
        cursor = payload.get("cursor")
        if not cursor:
            break

    return results


def _infer_team_id_from_file(file_key: str, api_key: str) -> str:
    file_data = _request_json(f"/files/{file_key}", api_key)
    team_id = file_data.get("teamId")
    if not team_id:
        raise RuntimeError(
            "Unable to infer teamId from file. Provide --team-id explicitly."
        )
    return str(team_id)


def cmd_design_system(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    team_id = args.team_id
    if not team_id:
        if not args.file_key:
            raise RuntimeError("Provide --team-id or --file-key to infer team id.")
        team_id = _infer_team_id_from_file(args.file_key, api_key)

    components = _fetch_paginated(f"/teams/{team_id}/components", api_key, args.page_size)
    styles = _fetch_paginated(f"/teams/{team_id}/styles", api_key, args.page_size)

    if args.query:
        query = args.query.lower()
        components = [c for c in components if query in str(c.get("name", "")).lower()]
        styles = [s for s in styles if query in str(s.get("name", "")).lower()]

    out = {
        "teamId": team_id,
        "query": args.query,
        "componentCount": len(components),
        "styleCount": len(styles),
        "components": components,
        "styles": styles,
    }
    print(json.dumps(out, indent=2))
    return 0


def cmd_screenshot_batch(args: argparse.Namespace) -> int:
    api_key = _get_api_key(args.api_key)
    node_ids = [_normalize_node_id(n.strip()) for n in args.node_ids.split(",") if n.strip()]
    if not node_ids:
        raise RuntimeError("Provide at least one node id in --node-ids.")

    image_data = _request_json(
        f"/images/{args.file_key}",
        api_key,
        {
            "ids": ",".join(node_ids),
            "format": "png",
            "scale": args.scale,
        },
    )
    image_map = image_data.get("images") or {}

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    for node_id in node_ids:
        image_url = image_map.get(node_id)
        if not image_url:
            saved.append({"nodeId": node_id, "saved": False, "reason": "no image URL"})
            continue

        safe_name = node_id.replace(":", "-")
        out_path = out_dir / f"{safe_name}.png"
        _download_file(image_url, out_path, api_key)
        saved.append(
            {
                "nodeId": node_id,
                "saved": True,
                "savedTo": str(out_path),
                "imageUrl": image_url,
            }
        )

    print(
        json.dumps(
            {
                "fileKey": args.file_key,
                "scale": args.scale,
                "requested": node_ids,
                "results": saved,
            },
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Figma REST CLI (JSON + screenshot PNG)")
    parser.add_argument("--api-key", help="Figma personal access token. If omitted, uses FIGMA_API_KEY env var.")

    sub = parser.add_subparsers(dest="command", required=True)

    me_p = sub.add_parser("me", help="Get current API user profile")
    me_p.set_defaults(func=cmd_me)

    file_p = sub.add_parser("file", help="Get raw file JSON")
    file_p.add_argument("--file-key", required=True, help="Figma file key")
    file_p.add_argument("--depth", type=int, help="Optional depth to limit traversal")
    file_p.set_defaults(func=cmd_file)

    node_p = sub.add_parser("node", help="Get node JSON")
    node_p.add_argument("--file-key", required=True, help="Figma file key")
    node_p.add_argument("--node-id", required=True, help="Node id like 1:2 (or 1-2)")
    node_p.add_argument("--depth", type=int, help="Optional depth to limit traversal")
    node_p.set_defaults(func=cmd_node)

    fills_p = sub.add_parser("image-fills", help="Get image fill refs/URLs for a file")
    fills_p.add_argument("--file-key", required=True, help="Figma file key")
    fills_p.set_defaults(func=cmd_image_fills)

    parse_p = sub.add_parser("parse-url", help="Extract file key and node id from a Figma URL")
    parse_p.add_argument("--url", required=True, help="Figma URL")
    parse_p.set_defaults(func=cmd_parse_url)

    nodeu_p = sub.add_parser("node-from-url", help="Get node JSON directly from a Figma URL")
    nodeu_p.add_argument("--url", required=True, help="Figma URL")
    nodeu_p.add_argument("--node-id", help="Optional override node id")
    nodeu_p.add_argument("--depth", type=int, help="Optional depth to limit traversal")
    nodeu_p.set_defaults(func=cmd_node_from_url)

    shot_p = sub.add_parser("screenshot", help="Export one node screenshot as PNG")
    shot_p.add_argument("--file-key", required=True, help="Figma file key")
    shot_p.add_argument("--node-id", required=True, help="Node id like 1:2 (or 1-2)")
    shot_p.add_argument("--scale", type=float, default=2.0, help="PNG scale factor (default: 2)")
    shot_p.add_argument("--out", required=True, help="Output PNG path")
    shot_p.set_defaults(func=cmd_screenshot)

    shotu_p = sub.add_parser("screenshot-from-url", help="Export screenshot PNG directly from a Figma URL")
    shotu_p.add_argument("--url", required=True, help="Figma URL")
    shotu_p.add_argument("--node-id", help="Optional override node id")
    shotu_p.add_argument("--scale", type=float, default=2.0, help="PNG scale factor (default: 2)")
    shotu_p.add_argument("--out", required=True, help="Output PNG path")
    shotu_p.set_defaults(func=cmd_screenshot_from_url)

    shotb_p = sub.add_parser("screenshot-batch", help="Export multiple node screenshots as PNG files")
    shotb_p.add_argument("--file-key", required=True, help="Figma file key")
    shotb_p.add_argument("--node-ids", required=True, help="Comma-separated node ids, e.g. 1:2,1:3")
    shotb_p.add_argument("--scale", type=float, default=2.0, help="PNG scale factor (default: 2)")
    shotb_p.add_argument("--out-dir", required=True, help="Output directory for PNGs")
    shotb_p.set_defaults(func=cmd_screenshot_batch)

    ds_p = sub.add_parser("design-system", help="List/search team components and styles")
    ds_p.add_argument("--team-id", help="Figma team id")
    ds_p.add_argument("--file-key", help="Optional file key to infer team id")
    ds_p.add_argument("--query", help="Optional case-insensitive name filter")
    ds_p.add_argument("--page-size", type=int, default=100, help="Pagination size per API call (default: 100)")
    ds_p.set_defaults(func=cmd_design_system)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    _load_dotenv()
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
