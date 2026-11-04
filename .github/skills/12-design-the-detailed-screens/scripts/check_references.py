#!/usr/bin/env python3
"""Check that every screen references the design system, and that each reference exists.

Usage:
    python3 check_references.py --usage USAGE.csv --tokens FILE [FILE ...]
        --components COMPONENTS.csv [--patterns PATTERNS.csv]
        [--screens SCREENS.csv] [--version VERSION]

USAGE.csv needs a header row: screen,kind,ref,version
    kind     component, token or pattern
    ref      a component ID, a token path written with / between group names
             (for example color_text/primary), or a pattern ID
    version  the design language version the screen was built against

COMPONENTS.csv and PATTERNS.csv need a header row with an id column.
--tokens takes one or more DTCG .tokens.json files. A token exists if it is
in any of them.
SCREENS.csv needs a header row with a screen column. It lists every screen
that must have references.
--version is the current approved design language version.

Findings:
    MISSING        a reference that is not in the design system
    NO REFERENCE   a screen in SCREENS.csv with no row in USAGE.csv
    STALE          a reference built against a version other than --version

Only existence and version are checked. Whether a screen uses the right
component is a person's call. The script reports. It never edits a file.

Exit code: 0 if there is no finding, 1 if there is, 2 on a usage or file error.
"""
import argparse
import csv
import json
import sys


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def read_csv(path, columns):
    try:
        with open(path, newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail("Cannot read " + path + ": " + str(error))
    if not rows:
        fail("No data rows in " + path + ".")
    for column in columns:
        if column not in rows[0]:
            fail("Missing column " + column + " in " + path + ".")
    return rows


def token_paths(tree, prefix=()):
    for name, node in tree.items():
        if name.startswith("$") or not isinstance(node, dict):
            continue
        if "$value" in node:
            yield "/".join(prefix + (name,))
        else:
            yield from token_paths(node, prefix + (name,))


def main():
    parser = argparse.ArgumentParser(description="Check design system references.")
    parser.add_argument("--usage", required=True)
    parser.add_argument("--tokens", nargs="+", required=True)
    parser.add_argument("--components", required=True)
    parser.add_argument("--patterns")
    parser.add_argument("--screens")
    parser.add_argument("--version")
    args = parser.parse_args()

    tokens = set()
    for path in args.tokens:
        try:
            with open(path, encoding="utf-8") as handle:
                tokens.update(token_paths(json.load(handle)))
        except (OSError, json.JSONDecodeError) as error:
            fail("Cannot read " + path + ": " + str(error))
    components = {r["id"].strip() for r in read_csv(args.components, ("id",))}
    patterns = {r["id"].strip() for r in read_csv(args.patterns, ("id",))} if args.patterns else set()
    usage = read_csv(args.usage, ("screen", "kind", "ref", "version"))

    known = {"component": components, "token": tokens, "pattern": patterns}
    findings, seen_screens = [], set()
    for number, row in enumerate(usage, 2):
        screen, kind, ref, version = (row[c].strip() for c in ("screen", "kind", "ref", "version"))
        if kind not in known:
            fail("Unknown kind '" + kind + "' on data line " + str(number) + ". Use component, token or pattern.")
        seen_screens.add(screen)
        if ref not in known[kind]:
            findings.append(("MISSING", screen, kind + " " + ref + " is not in the design system"))
        if args.version and version != args.version:
            findings.append(("STALE", screen, kind + " " + ref + " built against version '" + version + "', current is " + args.version))
    if args.screens:
        for row in read_csv(args.screens, ("screen",)):
            name = row["screen"].strip()
            if name not in seen_screens:
                findings.append(("NO REFERENCE", name, "the screen has no reference to the design system"))

    for kind, screen, detail in findings:
        print(kind + " | " + screen + " | " + detail)
    print("Checked %d references on %d screens against %d tokens, %d components and %d patterns: %d findings."
          % (len(usage), len(seen_screens), len(tokens), len(components), len(patterns), len(findings)))
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
