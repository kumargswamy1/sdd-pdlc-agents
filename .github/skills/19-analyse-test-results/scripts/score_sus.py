#!/usr/bin/env python3
"""Score System Usability Scale questionnaires.

Usage:
    python3 score_sus.py --data SUS.csv

SUS.csv needs a header row: participant,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10
Each answer is a whole number from 1 to 5.

Scoring: odd items score the answer minus 1. Even items score 5 minus the
answer. The sum of the ten item scores is multiplied by 2.5, so each
questionnaire gives a score from 0 to 100.

The report gives each score, then n, the mean, the sample standard deviation,
the lowest and the highest. A SUS score is not a percentage.

Exit code: 0 on success, 2 on a data or usage error.
"""
import argparse
import csv
import sys
from statistics import mean, stdev

COLUMNS = ["participant"] + ["q" + str(i) for i in range(1, 11)]


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def score(answers):
    total = 0
    for index, value in enumerate(answers, 1):
        total += (value - 1) if index % 2 == 1 else (5 - value)
    return total * 2.5


def main():
    parser = argparse.ArgumentParser(description="Score SUS questionnaires.")
    parser.add_argument("--data", required=True)
    args = parser.parse_args()
    try:
        with open(args.data, newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail("Cannot read " + args.data + ": " + str(error))
    if not rows:
        fail("No data rows in " + args.data + ".")
    for column in COLUMNS:
        if column not in rows[0]:
            fail("Missing column: " + column)

    scores = []
    seen = set()
    lines = ["| Participant | SUS score |", "|---|---|"]
    for number, row in enumerate(rows, 2):
        person = row["participant"].strip()
        if not person or person in seen:
            fail("Blank or repeated participant ID on data line " + str(number) + ".")
        seen.add(person)
        answers = []
        for column in COLUMNS[1:]:
            try:
                value = int(row[column])
            except (TypeError, ValueError):
                fail("Answer " + column + " on data line " + str(number) + " is not a whole number.")
            if value < 1 or value > 5:
                fail("Answer " + column + " on data line " + str(number) + " is outside 1 to 5.")
            answers.append(value)
        result = score(answers)
        scores.append(result)
        lines.append("| %s | %.1f |" % (person, result))

    print("\n".join(lines))
    print("")
    spread = stdev(scores) if len(scores) > 1 else float("nan")
    print("n = %d" % len(scores))
    print("Mean = %.1f" % mean(scores))
    print("Standard deviation = " + ("%.1f" % spread if len(scores) > 1 else "not defined for one questionnaire"))
    print("Lowest = %.1f, highest = %.1f" % (min(scores), max(scores)))
    print("A SUS score is not a percentage.")


if __name__ == "__main__":
    main()
