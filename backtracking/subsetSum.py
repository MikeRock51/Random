#!/usr/bin/env python3
"""
    Problem 1: Finding a Subset Sum
    Instructions:
        Given an array of positive integers and a target sum,
        find a subset of the array elements that adds up to the target sum.

    Example:
        Array: [2, 4, 6, 8, 10]
        Target Sum: 14
        Expected Output: A valid subset that adds up to the target sum, e.g., [2, 4, 8]
"""

from typing import List


def subsetSum(fullSet: List[int], target: int) -> List[int]:
    """Returns a list of array element that sums up to target"""
    setLen = len(fullSet)

    def backtrack(start: int, currSum, subSet) -> None:
        """Finds the first subset that sums up to target"""
        if currSum == target:
            return True, subSet

        for i in range(start, setLen):
            n = fullSet[i]
            if currSum + n <= target:
                subSet.append(n)
                found = backtrack(i + 1, currSum + n, subSet)
                if found:
                    return subSet
                subSet.remove(n)

        return []

    return backtrack(0, 0, [])

if __name__ == "__main__":
    fullSet = [5, 10, 12, 13, 15, 18]
    target = 30
    subSet = subsetSum(fullSet, target)
    print(subSet)
    fullSet = [2, 4, 6, 8, 10]
    target = 14
    print(subsetSum(fullSet, target))
