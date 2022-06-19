def decToBin(number):
    if number == 0:
        return ''
    return decToBin(number // 2) + str(number % 2)
