#!/usr/bin/env python3
"""Check that wired screen flows have no dead ends.

Usage:
    python3 check_flows.py --screens SCREENS.csv --links LINKS.csv

SCREENS.csv needs a header row: screen,role
    role is start, end or step.
LINKS.csv needs a header row: from,to
    one row for each way a person can move from one screen to another.

Findings:
    DEAD END     a screen that is not an end screen and has no link out
    UNREACHABLE  a screen that no path from a start screen reaches
    UNKNOWN      a link that names a screen missing from SCREENS.csv
    NO START     there is no start screen
    NO END       there is no end screen

The script reports. It never edits a file.

Exit code: 0 if there is no finding, 1 if there is, 2 on a data or usage error.
"""
import argparse
import csv
import sys
from collections import defaultdict, deque


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def read(path, columns):
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


def main():
    parser = argparse.ArgumentParser(description="Check wired flows for dead ends.")
    parser.add_argument("--screens", required=True)
    parser.add_argument("--links", required=True)
    args = parser.parse_args()

    screens = {}
    for number, row in enumerate(read(args.screens, ("screen", "role")), 2):
        name, role = row["screen"].strip(), row["role"].strip().lower()
        if not name or name in screens:
            fail("Blank or repeated screen on data line " + str(number) + ".")
        if role not in ("start", "end", "step"):
            fail("Unknown role '" + role + "' on data line " + str(number) + ". Use start, end or step.")
        screens[name] = role

    out = defaultdict(set)
    findings = []
    for number, row in enumerate(read(args.links, ("from", "to")), 2):
        a, b = row["from"].strip(), row["to"].strip()
        for name in (a, b):
            if name not in screens:
                findings.append(("UNKNOWN", name, "named in the links on data line " + str(number) + ", missing from the screens file"))
        if a in screens and b in screens:
            out[a].add(b)

    starts = [s for s, r in screens.items() if r == "start"]
    ends = [s for s, r in screens.items() if r == "end"]
    if not starts:
        findings.append(("NO START", "-", "no screen has the role start"))
    if not ends:
        findings.append(("NO END", "-", "no screen has the role end"))

    reached = set(starts)
    queue = deque(starts)
    while queue:
        for nxt in out[queue.popleft()]:
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)

    for name, role in screens.items():
        if role != "end" and not out[name]:
            findings.append(("DEAD END", name, "not an end screen and no link out"))
        if starts and name not in reached:
            findings.append(("UNREACHABLE", name, "no path from a start screen"))

    for kind, name, detail in findings:
        print(kind + " | " + name + " | " + detail)
    print("Checked %d screens and %d links: %d findings." % (len(screens), sum(len(v) for v in out.values()), len(findings)))
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
