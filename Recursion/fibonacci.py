def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciOptimised(n, hashMap):
    if n in hashMap:
        return hashMap[n]
    hashMap[n] = fibonacciOptimised(
        n - 1, hashMap) + fibonacciOptimised(n - 2, hashMap)
    return hashMap[n]


hashMap = {0: 0, 1: 1}
