#!/usr/bin/env python3
"""Turn DTCG token files into CSS custom properties for a coded prototype.

Usage:
    python3 tokens_to_css.py --tokens FILE.tokens.json [FILE...] --out tokens.css

The first file is the default mode and goes in :root. Each later file goes in
a [data-theme="MODE"] block, with MODE taken from a name like
design-tokens.Dark.tokens.json. Every token becomes one custom property.
The name is the token path in lower case with spaces and dots changed to
hyphens, joined by double hyphens between groups, for example
color_text/primary becomes --color_text--primary. An alias becomes
var(--name), so the prototype keeps the same levels as the design system.

Typography and border values become one property for each part. A shadow
becomes one box-shadow value. Nothing is chosen, rounded or invented. An
alias that does not resolve, a name that collides or a value the script
cannot convert is an error, and nothing is written when there is an error.
Standard library only.
"""
import argparse, json, re, sys

def slug(part):
    return re.sub(r"[^a-z0-9_-]+", "-", part.strip().lower()).strip("-")

def name_of(path):
    return "--" + "--".join(slug(p) for p in path)

def walk(node, path, out):
    if isinstance(node, dict) and "$value" in node:
        out.append((path, node.get("$type"), node["$value"]))
    elif isinstance(node, dict):
        gtype = node.get("$type")
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and gtype and "$type" not in v:
                v = dict(v); v["$type"] = gtype
            walk(v, path + [k], out)

def num(x):
    return str(int(x)) if float(x) == int(x) else str(x)

ALIAS = re.compile(r'^\{([^{}"]+)\}$')

def conv(value, typ, errors, where, names):
    """Return a CSS string, or None after recording an error."""
    if isinstance(value, str):
        m = ALIAS.match(value)
        if m:
            target = tuple(m.group(1).split("."))
            if target not in names:
                errors.append(f"{where}: alias {value} does not resolve")
                return None
            return f"var({names[target]})"
    if typ == "color":
        if isinstance(value, dict):
            if value.get("hex"):
                h = value["hex"]
                a = value.get("alpha", 1)
                return h if a == 1 or len(h) == 9 else (
                    h + format(round(a * 255), "02x"))
            c = value["components"]
            return "rgb(%s %s %s / %s)" % tuple(
                [num(round(x * 255)) for x in c[:3]] + [num(value.get("alpha", 1))])
        return str(value)
    if typ in ("dimension", "duration"):
        return num(value["value"]) + value["unit"]
    if typ == "cubicBezier":
        return "cubic-bezier(" + ",".join(num(x) for x in value) + ")"
    if typ == "fontFamily":
        return ", ".join(value) if isinstance(value, list) else str(value)
    if typ in ("fontWeight", "number"):
        return num(value)
    if typ == "strokeStyle":
        return str(value)
    errors.append(f"{where}: type {typ} cannot be converted")
    return None

def build(files):
    errors, blocks = [], []
    for i, f in enumerate(files):
        data = json.load(open(f))
        flat = []
        walk(data, [], flat)
        names, seen = {}, {}
        for path, typ, val in flat:
            n = name_of(path)
            if n in seen and seen[n] != tuple(path):
                errors.append(f"{f}: {'/'.join(path)} and {'/'.join(seen[n])} give the same name {n}")
            seen[n] = tuple(path)
            names[tuple(path)] = n
            names[tuple(p for p in path)] = n
        decls = []
        for path, typ, val in flat:
            n, where = names[tuple(path)], f"{f} {'/'.join(path)}"
            if typ in ("typography", "border") and isinstance(val, dict):
                for k, v in val.items():
                    t = {"fontFamily": "fontFamily", "fontSize": "dimension",
                         "fontWeight": "fontWeight", "lineHeight": "number",
                         "letterSpacing": "dimension", "color": "color",
                         "width": "dimension", "style": "strokeStyle"}.get(k)
                    c = conv(v, t, errors, where + "." + k, names)
                    if c is not None:
                        decls.append((f"{n}--{slug(k)}", c))
            elif typ == "shadow":
                items = val if isinstance(val, list) else [val]
                parts = []
                for s in items:
                    if isinstance(s, str):
                        parts.append(conv(s, "color", errors, where, names)); continue
                    bits = [conv(s.get(k), "dimension", errors, where + "." + k, names)
                            for k in ("offsetX", "offsetY", "blur", "spread") if k in s]
                    col = conv(s.get("color"), "color", errors, where + ".color", names)
                    pre = "inset " if s.get("inset") else ""
                    parts.append(pre + " ".join(b for b in bits if b) + " " + (col or ""))
                decls.append((n, ", ".join(parts)))
            else:
                c = conv(val, typ, errors, where, names)
                if c is not None:
                    decls.append((n, c))
        mode = re.search(r"\.([^./]+)\.tokens\.json$", f)
        sel = ":root" if i == 0 else '[data-theme="%s"]' % (mode.group(1) if mode else i)
        blocks.append(sel + " {\n" + "\n".join(f"  {a}: {b};" for a, b in decls) + "\n}\n")
    return errors, blocks

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokens", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    errors, blocks = build(a.tokens)
    if errors:
        print("\n".join("ERROR " + e for e in errors))
        print(f"{len(errors)} errors. Nothing written.")
        sys.exit(1)
    open(a.out, "w").write("/* Generated from the DTCG token files. Do not edit by hand. */\n" + "\n".join(blocks))
    print(f"Wrote {a.out}: {len(blocks)} block(s) from {len(a.tokens)} file(s). 0 errors.")

main()
