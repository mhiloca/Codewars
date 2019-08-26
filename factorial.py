from functools import reduce


def factorial(num):
    return reduce(lambda x, y: x * y, range(1, num+1))


print(factorial(4))