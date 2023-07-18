#!/usr/bin/python3

import time

def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    so = {}
    to = {}

    for c in s:
        if not c in so:
            so[c] = 1
        else:
            so[c] += 1

    for c in t:
        if not c in to:
            to[c] = 1
        else:
            to[c] += 1

    for key, value in so.items():
        if not to.get(key) or to[key] != so[key]:  
            return False
 
    return True

start = time.perf_counter()
#print(isAnagram("car", "rat"))
#print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "crate"))
end = time.perf_counter()
print(f'Time: {end - start}')
#print(isAnagram("anagram", "nagaram"))

