#!/usr/bin/python3

def permutation(arr):
    perm = []
    i = 0

    while i < len(arr):
        starter = arr[i]
        subs = [n for n in arr if arr.index(n) != i]
        j = 0
        k = 0
        Tperm = [starter]
        for n in subs:
            Tperm.append(n)
        perm.append(Tperm)

        if len(subs) > 1:
            Tperm = [starter]
            for n in reversed(subs):
                Tperm.append(n)
            perm.append(Tperm)
        i += 1

    return (perm)

print(permutation([1, 2, 3]))
print(permutation([1, 2]))
print(permutation([1]))
