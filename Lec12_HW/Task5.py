"""
def turn_off(func):
    return lambda *args, **kwargs: None
"""

import time


def rate_limiter(limit, interval):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove call times that are outside the interval
            call_times[:] = [t for t in call_times if t >= now - interval]

            if len(call_times) >= limit:
                print(f"Rate limit exceeded. Try again later.")
                return

            call_times.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limiter(limit=3, interval=60)
def my_function():
    print("Function called")


for _ in range(5):
    my_function()
    time.sleep(10)
