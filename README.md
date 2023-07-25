# Projector-practise
### Welcome to my first Python tasks repository! 🐍


Homework tasks from Projector Institute Python Beginning course - [Link for course](https://prjctr.com/course/python-beginning) 

- This Git repository houses the Python tasks I completed during the Projector Python Beginning Course. 
Here, you will find a collection of Python scripts and code snippets that showcase my progress and learning journey as I delved into the fundamentals of Python programming.

## Folder Lec8_HW: 

### **<p align="center">Algo-Riddles: The Coding Conundrum Task</p>**
- **Main task:** You have 100 cats. One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on. In the first round, you stop at every cat, placing a hat on each one. In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.). In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.). You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). Write a program that simply outputs which cats have hats at the end.
- **Optional task:** Make a function that can calculate hats with any amount of rounds and cats.

## Folder Lec9_HW: 
### **<p align="center">HW: Modules</p>**
- **First task - main:** Create a file called `hello.py` that contains a single `function hello()`. This function should accept a single string parameter name print the text `Hello {name}!` to the interactive window with `{name}` replaced with the function argument. Add a file called `main.py` that imports the `hello()` function from `hello.py` and calls the function with your name.
### **<p align="center">Optional -  Medical Terminology Guessing Game</p>**

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
