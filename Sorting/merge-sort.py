
def merge(left, right):
    if not left and not right: return []
    if not left: return right
    if not right: return left
    sorted, l, r = [], 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1
    while l < len(left):
        sorted.append(left[l])
        l += 1
    while r < len(right):
        sorted.append(right[r])
        r += 1
    return sorted

def divide(arr, l, r):
    if l < r:
        m = (l + r) // 2
        left = divide(arr, l, m)
        right = divide(arr, m + 1, r)
        return merge(left, right)
    return arr[l: r + 1]

def mergeSort(arr):
    l, r = 0, len(arr) - 1
    return divide(arr, l, r)

# Driver code
array = [ 10, 7, 8, 9, 1, 5, 17, 13, 15, 18, 19, 20, 22, 11]
print(mergeSort(array))



