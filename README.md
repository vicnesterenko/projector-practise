# Projector-practise
### Welcome to my first Python tasks repository! 🐍


Homework tasks from Projector Institute Python Beginning course - [Link for course](https://prjctr.com/course/python-beginning) 

- This Git repository houses the Python tasks I completed during the Projector Python Beginning Course. 
Here, you will find a collection of Python scripts and code snippets that showcase my progress and learning journey as I delved into the fundamentals of Python programming.

# Folder Lec8_HW - Algo-Riddles: The Coding Conundrum 

### Main task
-  You have 100 cats. One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on. In the first round, you stop at every cat, placing a hat on each one. In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.). In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.). You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). Write a program that simply outputs which cats have hats at the end.
### Optional task
-  Make a function that can calculate hats with any amount of rounds and cats.

# Folder Lec9_HW - Modules 
## **First task**
- Main: Create a file called `hello.py` that contains a single `function hello()`. This function should accept a single string parameter name print the text `Hello {name}!` to the interactive window with `{name}` replaced with the function argument. Add a file called `main.py` that imports the `hello()` function from `hello.py` and calls the function with your name.
### Optional -  Medical Terminology Guessing Game

### Description

- This is a simple Word Guessing Game implemented in Python. The game randomly selects a medical terminology word from a predefined list and provides the player with a hint related to that word. The player then has to guess the word by entering one letter at a time. The game provides feedback on correct and incorrect guesses and gives the player a limited number of attempts to guess the word correctly.

### How to Play

1. Run the `main.py` file to start the game.
2. The game will display a hint related to the medical terminology word to be guessed.
3. Guess the word by entering one letter at a time.
4. You have a limited number of attempts to guess the word correctly (default is 6 attempts).
5. The game will display the current progress of the word, showing the correctly guessed letters and placeholders for the remaining letters.
6. Continue guessing until you correctly guess the word or run out of attempts.
7. The game will inform you of the outcome and reveal the word after the game ends.

### Word List and Hints

- The game uses a predefined list of medical terminology words with corresponding hints. These hints provide a brief explanation of the term, helping players learn more about medical terminology while having fun.

### Flexibility

- The game is flexible and allows you to customize the list of medical terminology words and the maximum number of attempts. Simply modify the `MED_TERMINOLOGY` and `MAX_ATTEMPTS` variables in the `main.py` file to add or remove words from the list or change the number of attempts allowed per game.

### Play Again

- After each game, the game will prompt you if you want to play again. Type "yes" to start a new game, or "no" to exit the game.
  
## **Second task**

To complete the task of installing the custom library (numpy) in a virtual environment, generating a requirements.txt file, and running the numpy code, follow these steps:


### Custom Library Installation and Execution

1. Create a virtual environment using the command `python -m venv myenv`.
2. Activate the virtual environment:
   - On Windows: `myenv\Scripts\activate`
   - On macOS/Linux: `source myenv/bin/activate`
3. Install the numpy package (version 1.22.4 or higher but lower than 2.0.0) within the virtual environment using `pip install "numpy>=1.22.4,<2.0.0"`.
4. Generate the `requirements.txt` file using `pip freeze > requirements.txt`.
5. Write the script (`numpy_example.py`) that imports numpy and executes code from the numpy website.
6. Run the script within the virtual environment using `python numpy_example.py`.
<div align="center">
  <img width="534" alt="vicv" src="https://github.com/vicnesterenko/Projector-practise/assets/136901590/07e60086-27b5-4cd8-9f65-164b7844a5ce">
</div>


# Folder Lec10_HW - Context Manager and Files 
## First task - Task1.py

This Python script is designed to generate random numbers and store them in individual text files. The generated files are then organized into a folder called "Test1". The script also generates a summary file named "summary.txt" that lists the filenames and their corresponding randomly generated numbers. Once the summary file is created, the "Test1" folder is deleted.

### Functionality

1. `generate_name_files()`: Generates a list of uppercase letters from the English alphabet.

2. `generate_random_numbers()`: Generates a random integer between 1 and 100 (inclusive).

3. `create_folder_for_generation()`: Creates a folder named "Test1" in the directory specified by `LOCAL_PATH` if it does not already exist.

4. `generate_summary_file(summary_content: str)`: This function orchestrates the entire process. It creates the "Test1" folder, generates random numbers for each letter of the alphabet (file name is letter.txt), saves them in individual text files, and then creates the "summary.txt" file containing the filenames and their respective generated numbers. Finally, it deletes the "Test1" folder.

### Usage

1. Set the `LOCAL_PATH` variable to the desired directory where you want the "Test1" folder and the "summary.txt" file to be created.

2. Execute the script to generate random numbers and the summary file. The summary file will be located in the specified `LOCAL_PATH`.

Note: Make sure you have the necessary permissions to create and delete files and folders in the specified `LOCAL_PATH`.
## Second task - Task2.py

This Python script is designed to read the content of a text file named "Task2_1.txt" located in the directory specified by `LOCAL_PATH`. It then converts the text to uppercase and saves the result in a new text file named "Task2_2.txt" in the same directory.

### Functionality

The script performs the following steps:

1. Reads the content of "Task2_1.txt" located in the directory specified by `LOCAL_PATH`.

2. Converts the text to uppercase.

3. Creates a new text file named "Task2_2.txt" in the same directory (`LOCAL_PATH`).

4. Writes the converted uppercase text into the newly created "Task2_2.txt" file.

### Usage

1. Set the `LOCAL_PATH` variable to the desired directory where the "Task2_1.txt" and "Task2_2.txt" files should be located.

2. Place the text you want to convert to uppercase inside the "Task2_1.txt" file.

3. Execute the script to read the content from "Task2_1.txt", convert it to uppercase, and save it in "Task2_2.txt" in the same directory.

Note: Ensure that you have the necessary permissions to read and write files in the specified `LOCAL_PATH`. The script will overwrite the content of "Task2_2.txt" if it already exists.

## Third and fourth task - Task3_4.py

This Python script generates random scores for a list of players and saves the data in a CSV file. It then analyzes the generated scores to find the highest score achieved by each player and stores this information in another CSV file.

### Functionality

The script performs the following steps:

1. Generates random scores for a list of players defined in the `PLAYERS` list.

2. Saves the generated scores along with player names in a CSV file named "scores.csv" in the directory "Projector-practise/Lec10_HW".

3. Analyzes the scores and identifies the highest score achieved by each player.

4. Stores the highest scores in a new CSV file named "high_scores.csv" in the same directory "Projector-practise/Lec10_HW".

### Usage

1. Ensure that the `PLAYERS` list contains the names of players for whom you want to generate random scores.

2. Execute the script to generate random scores for the players and save the data in "scores.csv".

3. The script will analyze the scores and store the highest scores for each player in "high_scores.csv".

4. Review the "scores.csv" and "high_scores.csv" files in the "Projector-practise/Lec10_HW" directory to see the generated scores and the highest scores for each player, respectively.

Note: The script uses Python's built-in `csv` module to handle CSV file operations. Ensure that you have the necessary permissions to read and write files in the specified directory. The script will overwrite the content of "scores.csv" and "high_scores.csv" if these files already exist.
