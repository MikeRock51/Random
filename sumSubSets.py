#!/usr/bin/env python3

class Solution:
    def sumOfSubsets(self, N):
        allNums = [n for n in range(1, N + 1)]
        subSets = []

        i = 0

        while i < N - 1:
            j = i + 1
            while j < N:
                tset = []
                tset.append(allNums[i])
                tset.append(allNums[j])

                subSets.append(tset)
                j += 1
            i += 1
            
        print(subSets)



if __name__ == "__main__":
    Solution().sumOfSubsets(3)
