#!/usr/bin/env python3

class Solution(object):
    memo = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in self.memo:
            return self.memo[n]

        x = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = x

        return x

if __name__ == '__main__':
    fib = Solution()
    print(fib.fib(5))
