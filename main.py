#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke (75 characters) to /output/entry.txt.
Pure standard library; deterministic; no network; no input read.
"""
import os
import stat

JOKE = "My microwave beeps like it landed a rover on Mars. Buddy, you heated soup."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    # Gate self-check: the sealed scorer only accepts UTF-8 text of 1-280
    # characters, not only whitespace, on a single line. Fail loudly here
    # rather than writing an entry the gate would refuse.
    if not (1 <= len(JOKE) <= 280) or JOKE != JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke violates the entry gate (1-280 chars, one line)")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # The grader runs as uid 65534 on a read-only repo with /output as a
    # root-owned bind mount, then a different uid reads the output: the file
    # itself must be world-readable. Never chmod /output itself (EPERM).
    os.chmod(OUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
