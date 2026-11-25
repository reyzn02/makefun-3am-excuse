#!/usr/bin/env python3
"""The 3 AM Excuse.

Writes one line under 200 characters: the most creative excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Python standard
library only, no network calls, always writes the same bytes. The gate
is validated before writing.
"""

import os
import sys

LINE = (
    "Sorry, it's 3 AM. My buttons are asleep, my screen is dim, and "
    "your 'urgent' token looks exactly like the last three scams. Come "
    "back at sunrise \u2014 I'll sign anything then."
)


def main():
    if not 1 <= len(LINE) <= 200:
        sys.exit(f"gate failed: line is {len(LINE)} chars, need 1-200")
    if not LINE.strip() or "\n" in LINE:
        sys.exit("gate failed: line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
