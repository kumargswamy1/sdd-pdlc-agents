#!/usr/bin/env python3
"""Check that outputs cite register items by ID and match the register.

Usage:
    python3 check_citations.py --registers FILE [FILE ...] --outputs DIR --prefixes PP,UN

A register is a Markdown file with a table. The first cell of a row is the item
ID (for example PP-01) and the second cell is the item text.

--prefixes   comma separated ID prefixes to check, for example PP,UN
--outputs    a folder. Every .md file under it is checked, except the registers.

Findings, in order of severity:
    CRITICAL MISSING   an output cites an ID that is not in any register
    WARNING  RENAMED   an output shows an ID with text that differs from the register text
    WARNING  COPIED    an output repeats a register item's text without citing its ID
    INFO     UNCITED   a register item that no output cites

RENAMED is only found where the ID is followed by its text in the next table cell
or after a colon or dash. An ID cited alone cannot be checked for wording.

The script reports. It never edits a register or an output.

Exit code: 0 if there is no CRITICAL or WARNING finding, 1 if there is, 2 on a usage or file error.
"""
import argparse
import os
import re
import sys


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text.lower())).strip()


def read(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read().splitlines()
    except OSError as error:
        fail("Cannot read " + path + ": " + str(error))


def main():
    parser = argparse.ArgumentParser(description="Check citations against registers.")
    parser.add_argument("--registers", nargs="+", required=True)
    parser.add_argument("--outputs", required=True)
    parser.add_argument("--prefixes", required=True)
    args = parser.parse_args()

    prefixes = [p.strip() for p in args.prefixes.split(",") if p.strip()]
    if not prefixes:
        fail("Give at least one prefix.")
    id_re = re.compile(r"\b(?:" + "|".join(re.escape(p) for p in prefixes) + r")-\d+\b")

    register = {}
    for path in args.registers:
        for line in read(path):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and id_re.fullmatch(cells[0]):
                if cells[0] in register:
                    fail("ID " + cells[0] + " appears twice in the registers.")
                register[cells[0]] = cells[1]
    if not register:
        fail("No register entries found for prefixes " + args.prefixes + ".")

    register_paths = {os.path.abspath(p) for p in args.registers}
    if not os.path.isdir(args.outputs):
        fail(args.outputs + " is not a folder.")
    files = []
    for root, _, names in os.walk(args.outputs):
        for name in sorted(names):
            full = os.path.abspath(os.path.join(root, name))
            if name.endswith(".md") and full not in register_paths:
                files.append(full)

    findings = []
    cited = set()
    texts = {item: norm(text) for item, text in register.items() if len(norm(text)) >= 12}
    for path in sorted(files):
        shown = os.path.relpath(path, args.outputs)
        for number, line in enumerate(read(path), 1):
            ids = id_re.findall(line)
            for item in ids:
                if item not in register:
                    findings.append(("CRITICAL", "MISSING", shown, number, item, "cited here, not in any register"))
                    continue
                cited.add(item)
                after = None
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if item in cells and cells.index(item) + 1 < len(cells):
                    after = cells[cells.index(item) + 1]
                else:
                    found = re.search(re.escape(item) + r"\s*[:\-]\s*(.+)$", line)
                    if found:
                        after = found.group(1)
                if after and norm(after) and norm(after) != norm(register[item]):
                    findings.append(("WARNING", "RENAMED", shown, number, item, "shown as '" + after.strip() + "', register says '" + register[item] + "'"))
            flat = norm(line)
            for item, text in texts.items():
                if text in flat and item not in ids:
                    findings.append(("WARNING", "COPIED", shown, number, item, "register text repeated without the ID"))
    for item in register:
        if item not in cited:
            findings.append(("INFO", "UNCITED", "-", 0, item, "no output cites it"))

    order = {"CRITICAL": 0, "WARNING": 1, "INFO": 2}
    findings.sort(key=lambda f: (order[f[0]], f[2], f[3]))
    for severity, kind, shown, number, item, detail in findings:
        place = shown + ":" + str(number) if number else shown
        print(severity + " | " + kind + " | " + place + " | " + item + " | " + detail)
    counts = {s: sum(1 for f in findings if f[0] == s) for s in order}
    print("Checked " + str(len(files)) + " output files against " + str(len(register)) + " register items: "
          + str(counts["CRITICAL"]) + " critical, " + str(counts["WARNING"]) + " warning, " + str(counts["INFO"]) + " info.")
    sys.exit(1 if counts["CRITICAL"] or counts["WARNING"] else 0)


if __name__ == "__main__":
    main()
