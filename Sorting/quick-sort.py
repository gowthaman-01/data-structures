def quickSort(arr, start, end):
    if start >= end: return 
    pivot, l, r = end, start, end - 1
    while l <= r:
        if arr[l] <= arr[pivot]:
            l += 1
            continue
        if arr[r] > arr[pivot]:
            r -= 1
            continue
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    arr[l], arr[pivot] = arr[pivot], arr[l]
    quickSort(arr, start, l - 1)
    quickSort(arr, l + 1, end)
# Driver code
array = [ 10, 7, 8, 9, 1, 5, 17, 13, 15, 18, 19, 20, 22, 11]
quickSort(array, 0, len(array) - 1)
