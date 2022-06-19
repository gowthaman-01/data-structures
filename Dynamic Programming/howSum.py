def check(target, array, possible, store):
    if target == 0:
        return []
    if target < 0:
        return None
    if target in store:
        return store[target]
    for number in array:
        remainder = target - number
        if check(remainder, array, possible, store) != None:
            possible.append(number)
            store[target] = True
            return store[target]
    store[target] = None
    return store[target]


def howSum(target, array):
    possible, store = [], {}
    check(target, array, possible, store)
    return possible


print(howSum(7, [2, 1]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [3, 5, 2]))
print(howSum(300, [7, 14]))
