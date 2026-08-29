#!/usr/bin/env python3
"""Check that a final AI-video prompt stays within a hard character limit."""

from __future__ import annotations

import argparse
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="UTF-8 prompt file; omit to read stdin")
    parser.add_argument("--limit", type=int, default=5000)
    args = parser.parse_args()

    if args.file:
        text = pathlib.Path(args.file).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    count = len(text.strip())
    print(f"{count}/{args.limit} characters")
    if count > args.limit:
        print("FAIL: prompt exceeds the hard limit", file=sys.stderr)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
