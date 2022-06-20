def check(array, target, possible):
    if target == 0:
        return True
    if target < 0:
        return False
    if target in possible:
        return possible[target]
    for number in array:
        remainder = target - number
        if check(array, remainder, possible):
            possible[remainder] = True
            return possible[remainder]
    possible[target] = False
    return possible[target]


def canSum(array, target):
    possible = {}
    if check(array, target, possible):
        return True
    return False


print(canSum([2, 3], 7))
print(canSum([5, 3, 4, 7], 7))
print(canSum([2, 4], 7))
print(canSum([2, 3, 5], 8))
print(canSum([7, 14], 300))
