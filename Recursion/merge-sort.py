def merge(array, start, middle, end):
    leftArray = array[start:middle + 1]
    rightArray = array[middle + 1:end + 1]
    left, right, sorted, limit = 0, 0, [], min(len(leftArray), len(rightArray))
    while left < limit and right < limit:
        if leftArray[left] <= rightArray[right]:
            sorted.append(leftArray[left])
            left += 1
        else:
            sorted.append(rightArray[right])
            right += 1
    while left < len(leftArray):
        sorted.append(leftArray[left])
        left += 1
    while right < len(rightArray):
        sorted.append(rightArray[right])
        right += 1
    array[start:end + 1] = sorted


def mergeSort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)
    return array


l = [4, 2, 6, 3, 1, 5, 12, 14, 53, 23, 41, 51, 16, 26, 9, 31]
print(mergeSort(l, 0, len(l) - 1))
