#!/usr/bin/env python3
import argparse
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_upto(limit: int):
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            for multiple in range(p*p, limit+1, p):
                sieve[multiple] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

def main() -> None:
    parser = argparse.ArgumentParser(description="Prime checker and generator")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", "-c", type=int, help="Check if number is prime")
    group.add_argument("--list", "-l", type=int, metavar="LIMIT", help="List primes up to LIMIT")
    args = parser.parse_args()

    if args.check is not None:
        print(f"{args.check} is prime: {is_prime(args.check)}")
    elif args.list is not None:
        nums = primes_upto(args.list)
        print(", ".join(map(str, nums)) if nums else "None")
    else:
        try:
            n = int(input("Enter a number to check: "))
        except Exception:
            print("Invalid input")
            return
        print(is_prime(n))

if __name__ == "__main__":
    main()
