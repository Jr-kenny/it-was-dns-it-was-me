#!/usr/bin/env python3
"""Write the competition entry line to entry.txt.

The program holds one funny developer excuse, checks it fits the
gate (a single sentence, 76 characters, 1 to 200 allowed, one line, no dash),
writes it to the output file, and reads it back to prove that the
file holds exactly that line and nothing else.
"""

import os
from pathlib import Path

EXCUSE = "I blamed DNS for the outage because nobody ever questions DNS, including me."
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def gate_problems(text):
    problems = []
    if text != text.strip():
        problems.append("leading or trailing space")
    if not 1 <= len(text) <= 200:
        problems.append("length outside 1 to 200 characters")
    if text.count(".") != 1:
        problems.append("must be exactly one sentence")
    if "\n" in text:
        problems.append("must be a single line")
    if "\u2014" in text or "\u2013" in text:
        problems.append("must not contain a dash")
    return problems


def main():
    problems = gate_problems(EXCUSE)
    if problems:
        raise SystemExit("entry line fails the gate: " + "; ".join(problems))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")
    # The read-back is the proof: whatever lands in entry.txt must be
    # byte for byte the excuse, with no trailing newline added.
    if OUTPUT_PATH.read_text(encoding="utf-8") != EXCUSE:
        raise SystemExit("entry.txt does not match the excuse")


if __name__ == "__main__":
    main()
