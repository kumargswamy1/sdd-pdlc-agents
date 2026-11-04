#!/usr/bin/env python3
"""Extract candidate design values from saved CSS or HTML files.

Use it on a saved copy of a live product's stylesheets and pages, or on a
design system's CSS. It reads files. It never fetches anything.

Usage:
    python3 extract_css_values.py --files FILE [FILE ...] --out CANDIDATES.csv

Each FILE is a .css file, or an .html file whose <style> blocks and inline
style="" attributes are read. Give each file an ID by naming it in the form
ID=path, for example P01=home.html. Without an ID the file name is used.

The output CSV has these columns:
    kind      color, font-family, font-size, font-weight, line-height,
              letter-spacing, radius, spacing, border-width, shadow,
              duration, easing or custom-property
    value     the value as written, with colours lower-cased as hex
    count     how many declarations use it
    sources   the file IDs where it appears, separated by semicolons
    property  an example property that uses it
    name      for custom-property rows, the name, such as --color-primary

The script reports counts and nothing else. It does not choose tokens. A
person does that.

Exit code: 0 on success, 2 on a usage or file error.
"""
import argparse
import csv
import re
import sys
from collections import OrderedDict

HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RGB = re.compile(r"rgba?\(\s*(\d{1,3})\s*[, ]\s*(\d{1,3})\s*[, ]\s*(\d{1,3})\s*(?:[,/]\s*([\d.]+%?))?\s*\)")
LEN = re.compile(r"-?\d*\.?\d+(?:px|rem|em)\b|\b0\b")

KIND = {
    "color": "color", "background-color": "color", "border-color": "color", "fill": "color",
    "stroke": "color", "outline-color": "color",
    "font-family": "font-family", "font-size": "font-size", "font-weight": "font-weight",
    "line-height": "line-height", "letter-spacing": "letter-spacing",
    "border-radius": "radius", "gap": "spacing", "row-gap": "spacing", "column-gap": "spacing",
    "margin": "spacing", "padding": "spacing", "border-width": "border-width",
    "box-shadow": "shadow", "transition-duration": "duration", "animation-duration": "duration",
    "transition-timing-function": "easing", "animation-timing-function": "easing",
}


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def hex_of(text):
    m = HEX.search(text)
    if m:
        h = m.group(0).lower()
        if len(h) == 4:
            h = "#" + "".join(c * 2 for c in h[1:])
        return h
    m = RGB.search(text)
    if m:
        r, g, b = (min(255, int(m.group(i))) for i in (1, 2, 3))
        h = "#%02x%02x%02x" % (r, g, b)
        if m.group(4) and m.group(4) not in ("1", "1.0", "100%"):
            a = m.group(4)
            a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
            h += "%02x" % int(round(max(0.0, min(1.0, a)) * 255))
        return h
    return None


def blocks(text, is_html):
    """Yield (selector_or_label, declarations_text)."""
    if is_html:
        css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", text, re.S | re.I))
        for m in re.finditer(r'style\s*=\s*"([^"]*)"', text, re.I):
            yield "(inline)", m.group(1)
    else:
        css = text
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        yield m.group(1).strip().split("\n")[-1].strip()[:60], m.group(2)


def main():
    parser = argparse.ArgumentParser(description="Extract candidate design values.")
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    found = OrderedDict()

    def add(kind, value, source, prop, name=""):
        key = (kind, value, name)
        row = found.setdefault(key, {"count": 0, "sources": OrderedDict(), "property": prop})
        row["count"] += 1
        row["sources"][source] = True

    for spec in args.files:
        source, _, path = spec.partition("=") if "=" in spec else (spec, "", spec)
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError as error:
            fail("Cannot read " + path + ": " + str(error))
        for _, body in blocks(text, path.lower().endswith((".html", ".htm"))):
            for decl in body.split(";"):
                if ":" not in decl:
                    continue
                prop, _, value = decl.partition(":")
                prop, value = prop.strip().lower(), re.sub(r"\s*!important\s*$", "", value.strip(), flags=re.I)
                if not prop or not value:
                    continue
                if prop.startswith("--"):
                    add("custom-property", value, source, prop, prop)
                    continue
                kind = KIND.get(prop)
                if not kind:
                    continue
                if kind == "color":
                    h = hex_of(value)
                    if h:
                        add(kind, h, source, prop)
                elif kind == "shadow":
                    if value.lower() != "none":
                        add(kind, re.sub(r"\s+", " ", value), source, prop)
                elif kind in ("font-family",):
                    add(kind, re.sub(r"\s+", " ", value), source, prop)
                elif kind in ("font-weight", "easing", "duration"):
                    add(kind, re.sub(r"\s+", " ", value), source, prop)
                elif kind == "line-height" and re.fullmatch(r"\d*\.?\d+", value):
                    add(kind, value, source, prop)
                else:
                    for token in LEN.findall(value):
                        add(kind, token, source, prop)
                    if kind == "font-size" and not LEN.findall(value):
                        add(kind, value, source, prop)

    try:
        with open(args.out, "w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["kind", "value", "count", "sources", "property", "name"])
            for (kind, value, name), row in sorted(found.items(), key=lambda kv: (kv[0][0], -kv[1]["count"], kv[0][1])):
                writer.writerow([kind, value, row["count"], ";".join(row["sources"]), row["property"], name])
    except OSError as error:
        fail("Cannot write " + args.out + ": " + str(error))
    kinds = {}
    for (kind, _, _), row in found.items():
        kinds[kind] = kinds.get(kind, 0) + 1
    print("Read %d files. Candidate values by kind: %s" % (len(args.files), ", ".join("%s %d" % kv for kv in sorted(kinds.items())) or "none"))
    print("These are counts only. A person chooses the tokens.")


if __name__ == "__main__":
    main()
