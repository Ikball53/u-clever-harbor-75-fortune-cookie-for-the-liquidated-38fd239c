#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one fortune-cookie line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt via an atomic temp-file + os.replace.
"""

import os
import tempfile

LINE = "Your lucky numbers are 100x leverage, a margin call, and the exact price where you got liquidated."
# 17 words, 98 chars: under the 20-word / 160-char limits, and written
# with no trailing newline so the output is exactly this line.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
