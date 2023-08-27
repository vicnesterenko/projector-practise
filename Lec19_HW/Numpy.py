import numpy as np
from tabulate import tabulate


def taskA():
    a = np.zeros((4, 3))
    b = np.ones((4, 3))
    c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

    arrays = [(a, "a"), (b, "b"), (c, "c")]
    for arr, name in arrays:
        print(f"{name}:\n{arr}\nShape: {arr.shape}\n")


def taskB():
    def F(x):
        return 2 * x**2 + 5

    x_range = np.arange(1, 101, 1)
    table_data = [(F(x)) for x in x_range]
    data = {"x": x_range, "F(x)": table_data}
    table = tabulate(data, headers="keys", tablefmt="pretty")
    print(table)


def taskC():
    def F(x):
        return np.exp(-x)

    x_range = np.arange(-10, 11, 1)
    table_data = [(F(x)) for x in x_range]
    data = {"x": x_range, "F(x)": table_data}
    table = tabulate(data, headers="keys", tablefmt="pretty")

    print(table)


if __name__ == "__main__":
    taskA()
    taskB()
    taskC()
