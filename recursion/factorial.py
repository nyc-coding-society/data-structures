
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n


def factorial_loop(n):
    f = 1
    for i in range(2, n+1):
        f = f * i
    return f


print(factorial_loop(50000000000))