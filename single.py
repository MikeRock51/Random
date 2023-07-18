#!/usr/bin/python3


def singleNumber(arr=[]):

    for num in arr:
        if arr.count(num) == 1:
            return (num)

def singleNumber2(arr=[]):
    numsDict = {}

    for num in arr:
        if str(num) in numsDict.keys():
            numsDict[str(num)] = numsDict.get(str(num)) + 1
        else:
            numsDict[str(num)] = 1

    for key, value in numsDict.items():
        if value == 1:
            return key


print(singleNumber2([4,1,2,1,2]))
print(singleNumber2([2,1,2]))
