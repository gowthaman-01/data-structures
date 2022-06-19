def naturalSum(number):
    if number == 0:
        return 0
    return number + naturalSum(number - 1)
