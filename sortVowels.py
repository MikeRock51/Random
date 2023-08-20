#!/usr/bin/env python3
"""
    Topic: Sort Vowels in String

    Given a 0-indexed string s, permute s to get a new string t such that:
        - All consonants remain in their original places. More formally, if there
          is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
        - The vowels must be sorted in the nondecreasing order of their ASCII values.
        - More formally, for pairs of indices i, j with 0 <= i < j < s.length such 
          that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
    Return the resulting string.
"""


def sortVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'U', 'O', 'I', 'E', 'A']
    sVowels = []
    outString = ""

    for c in s:
        if c in vowels:
            sVowels.append(c)

    try:
        sVowels[0]
    except IndexError:
        print("No vowels found")
        return s

    sVowels = sorted(sVowels)

    for c in s:
        if c in sVowels or c in vowels:
            outString += sVowels[0]
            sVowels.remove(sVowels[0])
        else:
            outString += c

    return outString


print(sortVowels("lEetcOde"))
print(sortVowels("lYmpH"))
