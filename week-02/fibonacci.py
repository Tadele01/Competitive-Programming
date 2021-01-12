def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        tmp = a
        a = b
        b = tmp + a
    return b

