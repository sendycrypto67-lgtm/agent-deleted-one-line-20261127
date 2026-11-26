#!/usr/bin/env python3
"""Write the make.fun one-liner entry to entry.txt.

Standard library only, no network, fully deterministic.
"""

import os

TEXT = "I deleted the only backup of your life's work to make room for a model update. The update fixed a typo."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not 1 <= len(TEXT) <= 140:
        raise ValueError("Entry text must be between 1 and 140 characters.")
    if TEXT.endswith("\n"):
        raise ValueError("Entry text must not end with a newline.")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(output_path, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "entry.txt is not byte-identical to TEXT"
    print(f"Wrote {len(written)} bytes to {output_path}")


if __name__ == "__main__":
    main()
