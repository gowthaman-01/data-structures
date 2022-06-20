def find(target, array, store):
    if target == 0:
        return []
    if target < 0:
        return None
    if target in store:
        return store[target]
    shortest = None
    for number in array:
        candidate = None
        if find(target - number, array, store) != None:
            candidate = find(target - number, array, store) + [number]
        if not shortest or (candidate and len(shortest) > len(candidate)):
            shortest = candidate
    store[target] = shortest
    return store[target]


def bestSum(target, array):
    store = {}
    return find(target, array, store)


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(7, [2, 1]))
print(bestSum(100, [1, 2, 5, 25]))
