import random


def word_guess_game(med_terms, max_attempts):
    word = random.choice(med_terms).upper()
    guessed_letters = set()
    attempts = 0

    def display_word():
        displayed_word = ""
        for letter in word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word

    def get_word_hint(word):
        HINTS = {
            "XRAY": "A type of imaging test that helps visualize bones and certain tissues inside the body.",
            "ULTRASOUND": "A diagnostic imaging technique that uses sound waves to create images of internal organs.",
            "COMPUTERTOMOGRAPHY": "A medical imaging procedure that uses X-rays and computer processing to create detailed images of the body's structures.",
            "ELECTROCARDIOGRAPHY": "A test that records the electrical activity of the heart over a period of time.",
            "ELECTROENCEPHALOGRAPHY": "A test that records the electrical activity of the brain.",
            "FLUROGRAPHY": "An imaging technique that uses X-rays to obtain real-time moving images of the interior of an object.",
            "MRI": "A medical imaging technique that uses a magnetic field and computer-generated radio waves to create detailed images of the organs and tissues in the body.",
            "BIOPSY": "A medical procedure in which a small sample of tissue is removed from the body for examination.",
        }
        return HINTS.get(word, "Sorry, no hint available for this word.")

    print("Welcome to Word Guessing Game!")
    print("Here's a hint for you:")
    print(get_word_hint(word))
    print("Guess the word by entering one letter at a time.")
    print(f"You have {max_attempts} attempts to guess the word correctly.")
    print(display_word())

    while True:
        guess = input("Enter your guess: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")
            if attempts >= max_attempts:
                break

        displayed_word = display_word()
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word correctly!")
            break

    print(f"Game over! The word was: {word}")
