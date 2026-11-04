#!/usr/bin/env python3
"""Count outcome levels per group and give a confidence interval for each share.

Use it for task success (success, success with issues, failure) or for feature
acceptance (accepted, changed, not accepted). It never averages the levels.

Usage:
    python3 rate_levels.py --data RESULTS.csv [--levels a,b,c] [--confidence 0.95] [--min-n N]

RESULTS.csv needs a header row with these columns:
    group        the task or feature
    participant  the participant ID
    level        the outcome level

Options:
    --levels      comma separated list of allowed levels, in report order. Any
                  other level stops the run. Without it, levels are read from
                  the data.
    --confidence  0.90, 0.95 or 0.99. Default 0.95.
    --min-n       if a group has fewer rows than this, the report marks it.

The interval is the Wilson score interval for a share of n results.

Exit code: 0 on success, 2 on a data or usage error.
"""
import argparse
import csv
import sys
from collections import OrderedDict, Counter
from statistics import NormalDist


def wilson(k, n, confidence):
    z = NormalDist().inv_cdf((1 + confidence) / 2)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def main():
    parser = argparse.ArgumentParser(description="Count levels per group with confidence intervals.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--levels", default="")
    parser.add_argument("--confidence", type=float, default=0.95)
    parser.add_argument("--min-n", type=int, default=0)
    args = parser.parse_args()

    if args.confidence not in (0.90, 0.95, 0.99):
        fail("Confidence must be 0.90, 0.95 or 0.99.")
    try:
        with open(args.data, newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail("Cannot read " + args.data + ": " + str(error))
    if not rows:
        fail("No data rows in " + args.data + ".")
    for column in ("group", "participant", "level"):
        if column not in rows[0]:
            fail("Missing column: " + column)

    allowed = [item.strip() for item in args.levels.split(",") if item.strip()]
    groups = OrderedDict()
    seen = set()
    for number, row in enumerate(rows, 2):
        group, person, level = row["group"].strip(), row["participant"].strip(), row["level"].strip()
        if not group or not person or not level:
            fail("Blank cell on data line " + str(number) + ".")
        if allowed and level not in allowed:
            fail("Unknown level '" + level + "' on data line " + str(number) + ".")
        if (group, person) in seen:
            fail("Participant " + person + " appears twice for " + group + " on data line " + str(number) + ".")
        seen.add((group, person))
        groups.setdefault(group, []).append(level)

    percent = int(round(args.confidence * 100))
    print("| Group | n | Level | Count | Share | Lower " + str(percent) + "% | Upper " + str(percent) + "% |")
    print("|---|---|---|---|---|---|---|")
    for group, levels in groups.items():
        n = len(levels)
        counts = Counter(levels)
        order = allowed if allowed else list(OrderedDict.fromkeys(levels))
        for level in order:
            k = counts.get(level, 0)
            low, high = wilson(k, n, args.confidence)
            print("| %s | %d | %s | %d | %.1f%% | %.1f%% | %.1f%% |" % (group, n, level, k, 100.0 * k / n, 100 * low, 100 * high))
        if args.min_n and n < args.min_n:
            print("| " + group + " | " + str(n) + " | Small sample: fewer than " + str(args.min_n) + " results. Report counts, not shares. | | | | |")
    print("")
    print("Levels are labels, not numbers. Do not average them.")


if __name__ == "__main__":
    main()
