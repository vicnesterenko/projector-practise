import functools


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # key - unique identifier for each set of input arguments
        key = (
            args,
            frozenset(kwargs.items()),
        )
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


# Example usage
@memoize
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    return n * 2


print(expensive_calculation(5))
print(expensive_calculation(5))  # Should return the cached result
print(expensive_calculation(10))
print(expensive_calculation(10))  # Should return the cached result
