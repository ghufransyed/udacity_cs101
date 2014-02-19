# q2 triangular numbers


def triangular(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
