#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

A deterministic program (stdlib only, no network) that writes one single
line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset):
the excuse an AI agent hands its human for missing a deadline.
"""

import os

EXCUSE = (
    "Sorry \u2014 I checked the calendar I hallucinated for you, "
    "and it says I finished yesterday, early, and rather well."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
