#!/usr/bin/env python3
"""
    Problem 1: Finding a Subset Sum
    Instructions: Given an array of positive integers and a target sum,
    find a subset of the array elements that adds up to the target sum.

    Example:
        Array: [2, 4, 6, 8, 10]
        Target Sum: 14
    Expected Output:
        A valid subset that adds up to the target sum, e.g., [2, 4, 8]
"""

from typing import List


def subsetSum(arr: List[int], tSum: int) -> List[int]:
    subSets = []

    startTrack = 0
    track = 0
    currSum = 0
    while track < len(arr):
        currSum += arr[track]
        
        if currSum == tSum:
            subSets = arr[startTrack:track + 1]
            return subSets

print(subsetSum([2, 4, 6, 8, 10], 14))
