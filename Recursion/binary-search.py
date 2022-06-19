# Iterative
def binarySearchIterative(array, target):
    l, r = 0, len(array) - 1
    while l <= r:
        m = (r - l) // 2 + l
        if array[m] == target:
            return m
        if target > array[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


# Recursive
def binarySearchRecursive(array, target, l, r):
    if l > r:
        return - 1
    middle = (r - l) // 2 + l
    if array[middle] == target:
        return middle
    if target > array[middle]:
        return binarySearchRecursive(array, target, middle + 1, r)
    else:
        return binarySearchRecursive(array, target, l, middle - 1)
