def check_types(func):
    def wrapper(*args):
        for el in args:
            if type(el) != int:
                try:
                    raise TypeError(
                        f"Argument {el} must be int, not {type(el).__name__}"
                    )
                except TypeError as e:
                    print(e)
                    return
        return func(*args)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
# 3
add("1", "2")
# Argument 1 must be int, not str
add(1, "2")
# Argument 2 must be int, not str
add(1.023, 1)
# Argument 1.023 must be int, not float
add(True, 1)
# Argument True must be int, not bool
