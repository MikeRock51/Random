#!/usr/bin/env python3
"""
    Problem 1: Generating All Possible Subsets
    Instructions: Given a set of distinct integers, generate all possible subsets.

    Example: Set: {1, 2}
    Expected Output: {{}, {1}, {2}, {1, 2}}
"""

from typing import Set


def possibleSubsets(inputSet: Set[int]) -> Set[Set[int]]:

