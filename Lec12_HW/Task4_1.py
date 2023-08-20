def make_pretty(func):
    # Define the inner function
    cache = {}  # Initialize a dictionary to store cached results

    def inner():
        # Check if the result is in the cache
        if "result" in cache:
            print("Returning result from cache:", cache["result"])
        else:
            # Call the original function
            result = func()
            print("Calculating and caching result:", result)
            # Store the result in the cache
            cache["result"] = result

    # Return the inner function
    return inner


@make_pretty
# Define the ordinary function
def ordinary():
    return "I am ordinary"


ordinary()
