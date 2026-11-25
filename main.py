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


def validate_excuse(text: str) -> bytes:
    """Validate the excuse and return its exact output bytes.

    Gate checks: a single line, valid UTF-8, 1-200 characters long,
    and not whitespace-only. Returns the payload bytes (text plus one
    trailing newline) so the write below is byte-exact.
    """
    if not isinstance(text, str):
        raise ValueError("excuse must be a string")
    if not text or text.strip() == "":
        raise ValueError("excuse must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1-200 characters")
    payload = (text + "\n").encode("utf-8")  # raises if not encodable
    if payload.decode("utf-8") != text + "\n":
        raise ValueError("excuse is not valid UTF-8")
    return payload


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = validate_excuse(EXCUSE)
    # Byte-exact deterministic write: binary mode, no newline translation,
    # no encoding surprises — exactly the validated bytes go to disk.
    with open(path, "wb") as f:
        f.write(payload)


if __name__ == "__main__":
    main()
