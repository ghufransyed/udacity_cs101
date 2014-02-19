# 06_fibonacci.py


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)



# 0, 1, 1, 2, 3, 5, 8, 13, ..
# 0  1  2  3  4  5  6  7
# 1, 1, 2, 3, 5, 8,13
