#!/usr/bin/env python3
"""Check that each quote appears verbatim in a source text.

Usage:
    python3 check_quotes.py --source SOURCE_FILE --quotes QUOTES_FILE

QUOTES_FILE holds one quote per line, without surrounding quotation marks.
Blank lines and lines that start with # are ignored.

Match rule: exact text after two changes only. Runs of whitespace collapse to
one space, and curly quotes and apostrophes become straight ones. Letter case
must match. Nothing else is changed.

Exit code: 0 if every quote matches, 1 if any quote fails, 2 on a file error.
"""
import argparse
import re
import sys

CURLY = {
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u201f": '"',
}


def normalise(text):
    for curly, straight in CURLY.items():
        text = text.replace(curly, straight)
    return re.sub(r"\s+", " ", text).strip()


def read(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError as error:
        print("Cannot read " + path + ": " + str(error), file=sys.stderr)
        sys.exit(2)


def main():
    parser = argparse.ArgumentParser(description="Check quotes against a source text.")
    parser.add_argument("--source", required=True, help="source text file")
    parser.add_argument("--quotes", required=True, help="file with one quote per line")
    args = parser.parse_args()

    source = normalise(read(args.source))
    quotes = [line for line in read(args.quotes).splitlines()
              if line.strip() and not line.lstrip().startswith("#")]

    failed = 0
    for number, quote in enumerate(quotes, 1):
        ok = bool(normalise(quote)) and normalise(quote) in source
        print(("PASS" if ok else "FAIL") + " | line " + str(number) + " | " + quote)
        if not ok:
            failed += 1
    print("Checked " + str(len(quotes)) + " quotes: " + str(len(quotes) - failed) + " passed, " + str(failed) + " failed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
