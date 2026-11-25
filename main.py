#!/usr/bin/env python3
"""Make the AI Judge Laugh -- make.fun entry.

Writes one funny line (<= 200 characters) about office life to
<output>/entry.txt: they cancelled team-building to save money, then
hired a consultant for twice as much to explain why morale is low.
"""

import os
import sys

# The line: cost-cutting that costs more is a universal office truth, and
# the last words -- a consultant hired for twice as much to explain why
# morale is low -- are a specific, surprising absurdity. One sentence,
# no wasted setup, reads cleanly aloud.
LINE = "They cancelled team-building to save money, then hired a consultant for twice as much to explain why morale is low."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    assert len(data) == len(text), "byte length differs from char length"
    print(f"wrote {len(text)} chars to {path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
