def my_sort(arr, order):
    if order == 'asc':
        return (sorted(arr))
    elif order == 'desc':
        return (sorted(arr, reverse=True))
    else:
        return (arr)

print(my_sort([1, 2, 1], 'asc'))
