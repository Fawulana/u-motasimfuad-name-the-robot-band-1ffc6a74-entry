#!/usr/bin/env python3
"""Name the Robot Band - deterministic one-liner entry.

Writes exactly one line to the output directory's entry.txt.
Offline, stdlib only, no randomness: the same line every run.
"""

import os
from pathlib import Path

LINE = (
    "Fleetwood Mac Address - their hit 'Go Your Own Way "
    "(Firmware Update Required)' plays on repeat because "
    "nobody can find the drummer to stop it."
)


def main() -> None:
    # Honour ENTRY_OUTPUT_DIR when set; otherwise the kit's /output.
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
