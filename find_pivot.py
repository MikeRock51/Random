def find_pivot(arr, arrLen):
    if arrLen < 1:
        return (-1)

    if arr[0] == arr[arrLen - 1]:
        return (1)
    sum = 0
    for n in arr:
        sum += n
        if sum == arr[arrLen - 1]:
            return (arr.index(n) + 1)

    return (-1)

print(find_pivot([1, 2, 3, 4, 0, 6], 6))
print(find_pivot([-5, 10, 2, 5], 4))
print(find_pivot([1, 100, 0, 0, 1], 5))
print(find_pivot([7, 9, 8], 3))
print(find_pivot([1 , 2], 2))
