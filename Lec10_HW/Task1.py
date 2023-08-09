import random
import string
import os
import shutil

LOCAL_PATH = "Projector-practise\\Lec10_HW"


# Generate upper letter from string.ascii_uppercase
def generate_name_files():
    return [letter for letter in string.ascii_uppercase]


# Generate random number from 1 - 100
def generate_random_numbers():
    return random.randint(1, 100)


# Create folder where generation files will be
def create_folder_for_generation():
    new_folder = os.path.join(LOCAL_PATH, "Test1")
    if not os.path.exists(
        new_folder
    ):  # if i add deleting folder (shutil.rmtree(new_folder)), maybe this doesn't have sence
        os.mkdir(new_folder)
    return new_folder


# About generate_summary_file:
# Create new folder -> push gen_files to new_folder ->
# keep info in summary_content -> make summary_file
# -> write in summary_file summary_content -> delete new_folder
def generate_summary_file(summary_content: str):
    new_folder = create_folder_for_generation()
    summary_content = ""
    for file_name in generate_name_files():
        gen_files = os.path.join(new_folder, f"{file_name}.txt")
        file_content = str(generate_random_numbers())
        with open(gen_files, "w") as file:
            file.write(file_content)
        summary_content += f"{file_name}.txt: {file_content}\n"
    summary_file = os.path.join(LOCAL_PATH, "summary.txt")
    with open(summary_file, "w") as file:
        file.write(summary_content)
    shutil.rmtree(new_folder)  # delete folder Test1


if __name__ == "__main__":
    generate_summary_file()
