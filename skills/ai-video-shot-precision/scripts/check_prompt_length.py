#!/usr/bin/env python3
"""Check that a final AI-video prompt stays inside the required character range."""

from __future__ import annotations

import argparse
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="UTF-8 prompt file; omit to read stdin")
    parser.add_argument("--min", dest="minimum", type=int, default=1500,
                        help="minimum Unicode character count (default: 1500)")
    parser.add_argument("--max", dest="maximum", type=int, default=5000,
                        help="maximum Unicode character count (default: 5000)")
    parser.add_argument("--limit", type=int, dest="legacy_limit",
                        help="deprecated alias for --max; kept for older workflows")
    args = parser.parse_args()

    if args.legacy_limit is not None:
        args.maximum = args.legacy_limit
    if args.minimum < 0 or args.maximum < args.minimum:
        parser.error("--min must be non-negative and no greater than --max")

    if args.file:
        text = pathlib.Path(args.file).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    count = len(text.strip())
    print(f"{count}/{args.minimum}–{args.maximum} characters")
    if count < args.minimum:
        print("FAIL: prompt is shorter than the hard minimum", file=sys.stderr)
        return 1
    if count > args.maximum:
        print("FAIL: prompt exceeds the hard maximum", file=sys.stderr)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
