#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final one-line text message to the charger
it waited for all day, to ``entry.txt`` in the output directory.

The entry itself is a single line of plain text (at most 200
characters). The program keeps the text as one constant, validates it
against the competition gate (UTF-8, 1..200 characters, not only
whitespace), writes it out, and reads it back to prove the file on
disk is byte-for-byte the text it meant to send.

Standard library only. No network, no files read besides this one.
"""

import os
import sys

# The battery's last text. One scene (the other phone at lunch) and a
# second beat that reframes it: this is not a death, it is a breakup.
ENTRY = (
    "1%. I'm not dying, I'm quitting. You had me at 100% this morning "
    "and still took the other phone to lunch. Good luck with him."
)

MAX_CHARS = 200


def output_path() -> str:
    """Return the path of the entry file for this run."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate(text: str) -> None:
    """Check the entry against the competition gate, failing loudly.

    The sealed scorer requires UTF-8 text of 1 to 200 characters that
    is not only whitespace. A line that cannot pass that gate is a
    bug in this program, not something to ship and find out later.
    """
    if not text:
        raise ValueError("entry is empty")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # Prove the file on disk is byte-for-byte the text we meant to
    # send: read it back and compare, instead of trusting the write.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise RuntimeError("entry.txt on disk does not match ENTRY")
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
