# 06_fibo_while.py


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_array = [0, 1]
        for i in range(2, n + 1):
            fib_array.append(fib_array[-2] + fib_array[-1])
        return fib_array[-1]
