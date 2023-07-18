#!/usr/bin/python3

import time

def isAnagram(s: str, t: str) -> bool:
    start = time.time()

    if len(s) != len(t):
        return False

    so = {}
    to = {}

    for c in s:
        if not so[c]:
            so[c] = 1
        else:
            so[c] += 1

        if not to[c]:
            to[c] = 1
        else:
            to[c] += 1

    for key, value in so:
        if to[key] != so[key]:
            return False

    end = time.time()
    print(f'Time: {end - start}')

    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))

