def check(array, target, possible):
    if target == 0 or (target in possible and possible[target]):
        return True
    if target < 0 or (target in possible and not possible[target]):
        return False
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
