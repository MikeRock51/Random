#!/usr/bin/env python3

memo = {}
def fibo(n):
    if n <= 2:
        return 1
    
    if n in memo:
        return memo[n]
    
    f =  fibo(n - 1) + fibo(n - 2)
    memo[n] = f

    return f

print(fibo(20))
