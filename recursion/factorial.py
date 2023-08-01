#!/usr/bin/env python3

memo = {}

def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    x = factorial(n - 1) * n
    memo[n] = x

    return x


if __name__ == '__main__':
    print(factorial(7))
    print(factorial(10))
    print(memo)
