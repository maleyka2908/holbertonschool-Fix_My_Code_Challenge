#!/usr/bin/python3
"""
FizzBuzz implementation in Python
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
