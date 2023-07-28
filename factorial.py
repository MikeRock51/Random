#!/usr/bin/env python3

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return factorial(n - 1) * n


if __name__ == '__main__':
    print(factorial(5))
