#!/usr/bin/env python3
"""Check colour pairs against WCAG contrast thresholds.

Usage:
    python3 contrast_ratio.py --data PAIRS.csv [--level AA|AAA]

PAIRS.csv needs a header row with these columns:
    id          a stable ID for the pair
    foreground  a hex colour such as #1A2B3C or 1A2B3C (3 or 6 digits)
    background  a hex colour
    kind        text, large text or ui

Contrast ratio = (L1 + 0.05) / (L2 + 0.05), where L1 is the lighter relative
luminance and L2 the darker, using the WCAG 2.x sRGB formula.

Thresholds:
    AA   text 4.5, large text 3, ui 3
    AAA  text 7, large text 4.5, ui 3

The report gives each ratio to two decimals, the threshold and PASS or FAIL.
A PASS here is a calculation only. A person still verifies accessibility.

Exit code: 0 if every pair passes, 1 if any fails, 2 on a data or usage error.
"""
import argparse
import csv
import re
import sys

THRESHOLDS = {
    "AA": {"text": 4.5, "large text": 3.0, "ui": 3.0},
    "AAA": {"text": 7.0, "large text": 4.5, "ui": 3.0},
}


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def parse_hex(value, line):
    text = value.strip().lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", text):
        fail("Not a hex colour on data line " + str(line) + ": " + value)
    if len(text) == 3:
        text = "".join(ch * 2 for ch in text)
    return tuple(int(text[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def luminance(rgb):
    def channel(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def main():
    parser = argparse.ArgumentParser(description="Check colour pairs against WCAG contrast.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--level", default="AA", choices=["AA", "AAA"])
    args = parser.parse_args()
    try:
        with open(args.data, newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail("Cannot read " + args.data + ": " + str(error))
    if not rows:
        fail("No data rows in " + args.data + ".")
    for column in ("id", "foreground", "background", "kind"):
        if column not in rows[0]:
            fail("Missing column: " + column)

    seen = set()
    failed = 0
    lines = ["| ID | Kind | Contrast | Needs | Result |", "|---|---|---|---|---|"]
    for number, row in enumerate(rows, 2):
        item, kind = row["id"].strip(), row["kind"].strip().lower()
        if not item or item in seen:
            fail("Blank or repeated ID on data line " + str(number) + ".")
        seen.add(item)
        if kind not in THRESHOLDS[args.level]:
            fail("Unknown kind '" + kind + "' on data line " + str(number) + ". Use text, large text or ui.")
        l1 = luminance(parse_hex(row["foreground"], number))
        l2 = luminance(parse_hex(row["background"], number))
        light, dark = max(l1, l2), min(l1, l2)
        ratio = (light + 0.05) / (dark + 0.05)
        need = THRESHOLDS[args.level][kind]
        ok = ratio >= need
        failed += 0 if ok else 1
        lines.append("| %s | %s | %.2f:1 | %.1f:1 | %s |" % (item, kind, ratio, need, "PASS" if ok else "FAIL"))
    print("\n".join(lines))
    print("")
    print("Checked %d pairs at %s: %d passed, %d failed." % (len(rows), args.level, len(rows) - failed, failed))
    print("A pass here is a calculation. A person still verifies accessibility.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
