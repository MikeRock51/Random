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
    subSets = []
    currSum = 0
    fullSum = sum(fullSet)
    setLength = len(fullSet)

    def backtrack(index: int) -> None:
       """"""
       nonlocal currSum
       if currSum >= target or fullSum - currSum < target or index == setLength:
           print("Not enough left to sum")
           currSum -= fullSet[index]
           return

       print("Backtraacking...")
       
       while currSum < target:
           currSum += fullSet[index]
           subSets.append(fullSet[index])

           backtrack(index + 1)

    backtrack(0)
    return subSets


if __name__ == "__main__":
    fullSet = [5, 10, 12, 13, 15, 18]
    target = 30
    subSet = subsetSum(fullSet, target)
    print(subSet)
