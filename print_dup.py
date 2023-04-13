def print_duplicates(arr1, arrLen1, arr2, arrLen2):
    if arrLen1 < 1 or arrLen2 < 1:
        return []

    dups = []

    for n in arr1:
        if n in arr2:
            dups.append(n)

    return (dups)

print(print_duplicates([1, 2, 10, 15], 4, [2, 20, 40, 70], 4))
print(print_duplicates([-5,  2, 10, 15, 50, 70, 100, 200, 300, 1200, 5000], 11, [2, 4, 5, 6, 7, 10, 40, 70], 8))
print(print_duplicates([100, 200, 300], 3, [1, 2, 3, 4], 4))
print(print_duplicates([], 0, [], 0))
