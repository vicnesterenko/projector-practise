# Task2
import os

LOCAL_PATH = "Projector-practise\\Lec10_HW"


def read_file():
    with open("Projector-practise\Lec10_HW\Task2_1.txt", "r") as file:
        info = file.read()
    res_file = os.path.join(LOCAL_PATH, "Task2_2.txt")
    with open(res_file, "w") as file:
        file.write(info.upper())


if __name__ == "__main__":
    read_file()
