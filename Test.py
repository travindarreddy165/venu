#!/usr/bin/env python3
import argparse

def is_armstrong(n: int) -> bool:
    s = str(n)
    power = len(s)
    return n == sum(int(d) ** power for d in s)

def armstrong_numbers(limit: int):
    for i in range(limit + 1):
        if is_armstrong(i):
            yield i

def main() -> None:
    parser = argparse.ArgumentParser(description="Armstrong number checker/generator")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", "-c", type=int, help="Check if number is Armstrong")
    group.add_argument("--list", "-l", type=int, metavar="LIMIT", help="List Armstrong numbers up to LIMIT")
    args = parser.parse_args()

    if args.check is not None:
        print(f"{args.check} is Armstrong: {is_armstrong(args.check)}")
    elif args.list is not None:
        nums = list(armstrong_numbers(args.list))
        print(", ".join(map(str, nums)) if nums else "None")
    else:
        try:
            n = int(input("Enter a number to check: "))
        except Exception:
            print("Invalid input")
            return
        print(is_armstrong(n))

if __name__ == "__main__":
    main()