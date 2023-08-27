import numpy as np

a = np.zeros((4, 3))
b = np.ones((4, 3))
c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])


if __name__ == "__main__":
    print(a.shape)  # (4,3)
    print(a)
    print(b.shape)  # (4,3)
    print(b)
    print(c.shape)  # (4,3)
    print(c)
