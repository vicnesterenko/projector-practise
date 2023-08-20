import functools


@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


print(factorial(10))
print(factorial(5))
print(factorial(1))
print(factorial(5))
print(factorial(10))
