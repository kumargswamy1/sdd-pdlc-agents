#!/usr/bin/env python3
"""Build and check Design Tokens Community Group (DTCG) JSON files.

Two uses.

Build:
    python3 build_dtcg.py --csv TOKENS.csv --out DIR [--name design-tokens]

Check an existing file:
    python3 build_dtcg.py --check FILE.tokens.json

TOKENS.csv needs a header row with these columns:
    path         group names and the token name, separated by /
                 for example Colour Styles/Primary Colour/Blue/Blue 60
    level        primitive, semantic or component
    type         color, dimension, fontFamily, fontWeight, duration,
                 cubicBezier, number, strokeStyle, typography, shadow or border
    value        a literal, or an alias written as {path/of/token}
                 typography, shadow and border take a JSON object or list
    mode         all, or a mode name such as Light, Dark, Lg, Md, Sm
    description  optional
    source       optional, where the value was observed or decided
    evidence     optional, Evidence, Inference or Assumption
    confidence   optional

Rules checked, from the figma-tokens skill:
    A semantic or component token holds no raw value. Its value is an alias.
    A semantic token aliases a primitive. A component token aliases a
    semantic or a primitive token. A primitive may alias another primitive.
Rules checked, from the DTCG 2025.10 format module:
    Names do not start with $ and do not contain { } or a full stop.
    Colour is {colorSpace, components, alpha, hex}. Dimension is
    {value, unit} with unit px or rem. Duration is {value, unit} with unit
    ms or s. Cubic bezier is four numbers. Aliases resolve and do not loop.

Output: one file per mode, named NAME.MODE.tokens.json, or NAME.tokens.json
when every token has the mode all. A token with the mode all is written to
every file. Modes are not part of the format module this script was written
from, so the file split is a convention. Nothing is written if any error is
found.

Exit code: 0 on success, 1 if errors were found, 2 on a usage or file error.
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import OrderedDict

TYPES = ("color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier",
         "number", "strokeStyle", "typography", "shadow", "border")
LEVELS = ("primitive", "semantic", "component")
STROKES = ("solid", "dashed", "dotted", "double", "groove", "ridge", "outset", "inset")
ALIAS = re.compile(r'^\{([^{}"]+)\}$')
# keys inside composite values that may hold a literal even at semantic or component level
LITERAL_OK = ("inset", "style")


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def valid_name(name):
    return bool(name) and not name.startswith("$") and not any(c in name for c in "{}.")


def alias_to_dtcg(text):
    m = ALIAS.match(text.strip())
    return "{" + ".".join(p.strip() for p in m.group(1).split("/")) + "}" if m else None


def convert(kind, raw, errors, where):
    """Convert a literal to a DTCG value. Returns None and records an error if it cannot."""
    if isinstance(raw, str):
        al = alias_to_dtcg(raw)
        if al:
            return al
        raw = raw.strip()
    try:
        if kind == "color":
            m = re.fullmatch(r"#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", raw)
            if not m:
                raise ValueError("a colour is written as #rgb, #rrggbb or #rrggbbaa")
            h = m.group(1)
            if len(h) in (3, 4):
                h = "".join(c * 2 for c in h)
            r, g, b = (int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
            out = OrderedDict([("colorSpace", "srgb"), ("components", [round(r, 6), round(g, 6), round(b, 6)])])
            out["alpha"] = round(int(h[6:8], 16) / 255.0, 6) if len(h) == 8 else 1
            out["hex"] = "#" + h[:6].lower()
            return out
        if kind == "dimension":
            if raw in ("0", 0):
                return OrderedDict([("value", 0), ("unit", "px")])
            m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem)", str(raw))
            if not m:
                raise ValueError("a dimension is a number with px or rem, for example 16px")
            return OrderedDict([("value", float(m.group(1)) if "." in m.group(1) else int(m.group(1))), ("unit", m.group(2))])
        if kind == "duration":
            m = re.fullmatch(r"(\d*\.?\d+)(ms|s)", str(raw))
            if not m:
                raise ValueError("a duration is a number with ms or s, for example 200ms")
            return OrderedDict([("value", float(m.group(1)) if "." in m.group(1) else int(m.group(1))), ("unit", m.group(2))])
        if kind == "cubicBezier":
            nums = [float(x) for x in re.sub(r"[\[\]]", "", str(raw)).split(",")]
            if len(nums) != 4:
                raise ValueError("a cubic bezier is four numbers")
            return nums
        if kind == "fontFamily":
            names = [n.strip().strip("\"'") for n in str(raw).split(",") if n.strip()]
            if not names:
                raise ValueError("a font family needs at least one name")
            return names[0] if len(names) == 1 else names
        if kind == "fontWeight":
            n = float(raw)
            if not 1 <= n <= 1000:
                raise ValueError("a font weight is a number from 1 to 1000")
            return int(n) if n == int(n) else n
        if kind == "number":
            n = float(raw)
            return int(n) if n == int(n) else n
        if kind == "strokeStyle":
            if str(raw) not in STROKES:
                raise ValueError("a stroke style is one of " + ", ".join(STROKES))
            return str(raw)
        if kind in ("typography", "shadow", "border"):
            data = json.loads(raw) if isinstance(raw, str) else raw
            return convert_composite(kind, data, errors, where)
    except (ValueError, json.JSONDecodeError) as error:
        errors.append(where + ": " + str(error))
        return None
    errors.append(where + ": unknown type " + str(kind))
    return None


PART_TYPES = {
    "typography": {"fontFamily": "fontFamily", "fontSize": "dimension", "fontWeight": "fontWeight",
                   "letterSpacing": "dimension", "lineHeight": "number"},
    "shadow": {"color": "color", "offsetX": "dimension", "offsetY": "dimension", "blur": "dimension",
               "spread": "dimension", "inset": None},
    "border": {"color": "color", "width": "dimension", "style": "strokeStyle"},
}
REQUIRED = {"typography": ("fontFamily", "fontSize", "fontWeight", "lineHeight"),
            "shadow": ("color", "offsetX", "offsetY", "blur", "spread"),
            "border": ("color", "width", "style")}


def convert_composite(kind, data, errors, where):
    if kind == "shadow" and isinstance(data, list):
        return [convert_composite(kind, item, errors, where) for item in data]
    if not isinstance(data, dict):
        errors.append(where + ": a " + kind + " value is a JSON object")
        return None
    for key in REQUIRED[kind]:
        if key not in data:
            errors.append(where + ": " + kind + " is missing " + key)
    out = OrderedDict()
    for key, val in data.items():
        if key not in PART_TYPES[kind]:
            errors.append(where + ": " + kind + " has an unknown part " + key)
            continue
        part = PART_TYPES[kind][key]
        out[key] = val if part is None else convert(part, val, errors, where + " " + key)
    return out


def leaf_values(value):
    """Yield (key, leaf) for every string leaf of a converted composite or simple value."""
    if isinstance(value, dict):
        for k, v in value.items():
            for key, leaf in leaf_values(v):
                yield (k if key is None else key), leaf
    elif isinstance(value, list):
        for v in value:
            for key, leaf in leaf_values(v):
                yield key, leaf
    else:
        yield None, value


def flatten(tree, prefix=()):
    """Yield (path tuple, token dict) for every token in a DTCG tree."""
    for name, node in tree.items():
        if name.startswith("$") or not isinstance(node, dict):
            continue
        if "$value" in node:
            yield prefix + (name,), node
        else:
            yield from flatten(node, prefix + (name,))


def find_errors(tree):
    """Structural check of a DTCG tree. Returns a list of errors."""
    errors = []
    tokens = OrderedDict(flatten(tree))
    paths = {".".join(p): t for p, t in tokens.items()}

    def check_names(node, trail):
        for name, child in node.items():
            if name.startswith("$"):
                continue
            if not valid_name(name):
                errors.append("name '" + name + "' at " + ".".join(trail) + " breaks the naming rules")
            if isinstance(child, dict) and "$value" not in child:
                check_names(child, trail + (name,))
    check_names(tree, ())

    def inherited_type(path):
        node = tree
        found = tree.get("$type")
        for part in path[:-1]:
            node = node[part]
            found = node.get("$type", found)
        return found

    def resolve_type(path, seen):
        token = tokens[path]
        if "$type" in token:
            return token["$type"]
        value = token["$value"]
        if isinstance(value, str) and ALIAS.match(value):
            target = tuple(ALIAS.match(value).group(1).split("."))
            if target in seen:
                return None
            if target in tokens:
                return resolve_type(target, seen | {path})
            return None
        return inherited_type(path)

    for path, token in tokens.items():
        label = ".".join(path)
        if resolve_type(path, frozenset()) is None:
            errors.append(label + ": no type, and none can be inherited or resolved")
        for _, leaf in leaf_values(token["$value"]):
            if isinstance(leaf, str) and ALIAS.match(leaf):
                target = tuple(ALIAS.match(leaf).group(1).split("."))
                if target not in tokens:
                    errors.append(label + ": alias " + leaf + " does not resolve")
    for path in tokens:
        seen, current = [path], path
        while True:
            value = tokens[current]["$value"]
            if isinstance(value, str) and ALIAS.match(value):
                nxt = tuple(ALIAS.match(value).group(1).split("."))
                if nxt not in tokens:
                    break
                if nxt in seen:
                    errors.append(".".join(path) + ": alias loop through " + ".".join(nxt))
                    break
                seen.append(nxt)
                current = nxt
            else:
                break
    return errors


def main():
    parser = argparse.ArgumentParser(description="Build and check DTCG JSON.")
    parser.add_argument("--csv")
    parser.add_argument("--out")
    parser.add_argument("--name", default="design-tokens")
    parser.add_argument("--check")
    args = parser.parse_args()

    if args.check:
        try:
            with open(args.check, encoding="utf-8") as handle:
                tree = json.load(handle, object_pairs_hook=OrderedDict)
        except (OSError, json.JSONDecodeError) as error:
            fail("Cannot read " + args.check + ": " + str(error))
        errors = find_errors(tree)
        for e in errors:
            print("ERROR | " + e)
        print("Checked %d tokens: %d errors." % (sum(1 for _ in flatten(tree)), len(errors)))
        sys.exit(1 if errors else 0)

    if not args.csv or not args.out:
        fail("Give --csv and --out, or --check.")
    try:
        with open(args.csv, newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail("Cannot read " + args.csv + ": " + str(error))
    if not rows:
        fail("No data rows in " + args.csv + ".")
    for column in ("path", "level", "type", "value", "mode"):
        if column not in rows[0]:
            fail("Missing column: " + column)

    errors, entries = [], OrderedDict()   # entries[(mode, path)] -> dict
    modes = OrderedDict()
    for number, row in enumerate(rows, 2):
        where = "line " + str(number)
        path = tuple(p.strip() for p in row["path"].split("/") if p.strip())
        level, kind, mode = row["level"].strip(), row["type"].strip(), (row["mode"].strip() or "all")
        if not path or not all(valid_name(p) for p in path):
            errors.append(where + ": the path '" + row["path"] + "' has an empty part or a name with $, { } or a full stop")
            continue
        if level not in LEVELS:
            errors.append(where + ": level must be primitive, semantic or component")
            continue
        if kind not in TYPES:
            errors.append(where + ": type '" + kind + "' is not supported")
            continue
        key = (mode, path)
        if key in entries:
            errors.append(where + ": " + "/".join(path) + " appears twice for mode " + mode)
            continue
        value = convert(kind, row["value"], errors, where + " " + "/".join(path))
        if value is None:
            continue
        if level in ("semantic", "component"):
            for part, leaf in leaf_values(value):
                if part in LITERAL_OK:
                    continue
                if not (isinstance(leaf, str) and ALIAS.match(leaf)):
                    errors.append(where + ": " + level + " token " + "/".join(path) + " holds a raw value. Use an alias to a token.")
                    break
        entries[key] = {"level": level, "type": kind, "value": value, "row": row}
        modes[mode] = True

    for (mode, path) in list(entries):
        if mode != "all" and ("all", path) in entries:
            errors.append("/".join(path) + " has the mode all and also the mode " + mode)

    named = [m for m in modes if m != "all"]
    file_modes = named if named else ["all"]
    trees = OrderedDict()
    for fm in file_modes:
        tree = OrderedDict()
        for (mode, path), entry in entries.items():
            if mode != "all" and mode != fm:
                continue
            node = tree
            for part in path[:-1]:
                node = node.setdefault(part, OrderedDict())
            row = entry["row"]
            token = OrderedDict([("$type", entry["type"]), ("$value", entry["value"])])
            if row.get("description", "").strip():
                token["$description"] = row["description"].strip()
            prov = OrderedDict((k, row[k].strip()) for k in ("source", "evidence", "confidence") if row.get(k, "").strip())
            prov["level"] = entry["level"]
            token["$extensions"] = OrderedDict([("skill.provenance", prov)])
            if path[-1] in node and not ("$value" in node[path[-1]]):
                errors.append("/".join(path) + " is both a token and a group")
            node[path[-1]] = token
        trees[fm] = tree

    # level and alias checks, per file
    for fm, tree in trees.items():
        errors.extend("[" + fm + "] " + e for e in find_errors(tree))
        flat = {".".join(p): t for p, t in flatten(tree)}
        for path_t, tok in flatten(tree):
            level = tok["$extensions"]["skill.provenance"]["level"]
            targets = {leaf for _, leaf in leaf_values(tok["$value"]) if isinstance(leaf, str) and ALIAS.match(leaf)}
            for al in targets:
                target = flat.get(ALIAS.match(al).group(1))
                if not target:
                    continue
                tl = target["$extensions"]["skill.provenance"]["level"]
                ok = {"primitive": ("primitive",), "semantic": ("primitive",), "component": ("semantic", "primitive")}[level]
                if tl not in ok:
                    errors.append("[" + fm + "] " + ".".join(path_t) + ": a " + level + " token cannot alias a " + tl + " token (" + al + ")")
                if tok["$type"] in ("color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier", "number", "strokeStyle") \
                        and isinstance(tok["$value"], str) and target["$type"] != tok["$type"]:
                    errors.append("[" + fm + "] " + ".".join(path_t) + ": type " + tok["$type"] + " aliases a " + target["$type"] + " token")

    if errors:
        for e in sorted(set(errors)):
            print("ERROR | " + e)
        print("%d errors. No file was written." % len(set(errors)))
        sys.exit(1)

    try:
        os.makedirs(args.out, exist_ok=True)
        for fm, tree in trees.items():
            fname = args.name + (".tokens.json" if fm == "all" else "." + re.sub(r"[^A-Za-z0-9_-]+", "-", fm) + ".tokens.json")
            with open(os.path.join(args.out, fname), "w", encoding="utf-8") as handle:
                json.dump(tree, handle, indent=2)
                handle.write("\n")
            n = sum(1 for _ in flatten(tree))
            by = {}
            for _, t in flatten(tree):
                by[t["$type"]] = by.get(t["$type"], 0) + 1
            print("Wrote %s: %d tokens (%s)" % (fname, n, ", ".join("%s %d" % kv for kv in sorted(by.items()))))
    except OSError as error:
        fail("Cannot write in " + args.out + ": " + str(error))
    print("0 errors. Modes are a file split convention, not part of the format module read for this script.")


if __name__ == "__main__":
    main()
