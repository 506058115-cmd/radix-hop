#!/usr/bin/env python3
"""Convert an integer between bases 2 and 36."""

import argparse
import sys


DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def format_number(value, base):
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    value = abs(value)
    result = []
    while value:
        value, remainder = divmod(value, base)
        result.append(DIGITS[remainder])
    return sign + "".join(reversed(result))


def main():
    parser = argparse.ArgumentParser(description="Convert an integer between bases 2 and 36.")
    parser.add_argument("number", help="digits in the input base; an optional leading minus is allowed")
    parser.add_argument("--from-base", type=int, required=True, metavar="N", help="input base from 2 to 36")
    parser.add_argument("--to-base", type=int, required=True, metavar="N", help="output base from 2 to 36")
    args = parser.parse_args()
    for name, base in (("input", args.from_base), ("output", args.to_base)):
        if not 2 <= base <= 36:
            parser.error(f"{name} base must be between 2 and 36")
    digits = args.number[1:] if args.number.startswith("-") else args.number
    if not digits or any(not char.isascii() or char.lower() not in DIGITS[:args.from_base] for char in digits):
        parser.error(f"number contains a digit not valid in base {args.from_base}")
    try:
        value = int(args.number, args.from_base)
    except ValueError:
        parser.error("number is too large to parse")
    print(format_number(value, args.to_base))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
