#!/usr/bin/env python3
"""
    You are given a 0-indexed 1-dimensional (1D) integer array original,
    and two integers, m and n. You are tasked with creating a 2-dimensional
    (2D) array with  m rows and n columns using all the elements from original.

    The elements from indices 0 to n - 1 (inclusive) of original should form
    the first row of the constructed 2D array, the elements from indices n to 2
    * n - 1 (inclusive) should form the second row of the constructed 2D array,
    and so on.

    Return an m x n 2D array constructed according to the above procedure,
    or an empty 2D array if it is impossible.
"""


from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        twoD = []

        if len(original) / n != m:
            return []

        nTracker = 0
        for i in range(m):
            oneD = []
            for j in range(nTracker, nTracker + n):
                oneD.append(original[j])
                nTracker += 1
            twoD.append(oneD)

        return twoD

#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         ans = []
#         if len(original) == m*n:
#             for i in range(0, len(original), n):
#                 ans.append(original[i:i+n])
#         return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.construct2DArray([1,2,3,4], 2, 2))
    print(solution.construct2DArray([1,2,3], 1, 3)) 
    print(solution.construct2DArray([1,2], 1, 1))
    print(solution.construct2DArray([3], 1, 2))
