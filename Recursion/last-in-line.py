line = [1, 2, 3, 4, 5, 6]


def last(line):
    if len(line) == 1:
        return line[0]
    lastInLine = last(line[1:])
    return lastInLine
