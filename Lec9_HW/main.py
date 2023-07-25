import hello
from guess_word import word_guess_game

result = hello.hello("Vic")  # main task

if __name__ == "__main__":  # optional task - my own
    MED_TERMINOLOGY = [
        "XRAY",
        "ULTRASOUND",
        "COMPUTERTOMOGRAPHY",
        "ELECTROCARDIOGRAPHY",
        "ELECTROENCEPHALOGRAPHY",
        "FLUROGRAPHY",
        "MRI",
        "BIOPSY",
    ]
    MAX_ATTEMPTS = 6

    while True:
        word_guess_game(MED_TERMINOLOGY, MAX_ATTEMPTS)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
