ALL_CATS = {key: False for key in range(1, 101)}

# Get the number of rounds and number of cats from the user as input.
ROUNDS = int(input("Write number of rounds: "))
NUM_CATS = int(input("Write number of cats: "))


def cats_rounds(all_cats: dict, iteration: int) -> int:
    for key in all_cats:
        if key % iteration == 0:
            all_cats[key] = not all_cats[key]
    count_hats = sum(all_cats.values())
    return count_hats


# Main task
# Function to count the number of cats with hats after 100 rounds for 100 cats.
def count_hats_100_round() -> int:
    for i in range(1, 101):
        count_hats = cats_rounds(ALL_CATS, i)
    return count_hats


# Optional task
# Function to count the number of cats with hats after each round for any number of rounds and cats.
def count_hats_every_round(rounds: int, num_cats: int) -> list:
    all_cats = {key: False for key in range(1, num_cats + 1)}
    count_hats = []
    for i in range(1, rounds + 1):
        hats_count = cats_rounds(all_cats, i)
        count_hats.append(hats_count)
    return count_hats


def main():
    result = count_hats_100_round()
    print(f"Count of hats on cats after 100 rounds: {result}")
    count_hats = count_hats_every_round(ROUNDS, NUM_CATS)
    for i, count in enumerate(count_hats, 1):
        print(f"Count of hats after {i} round: {count}")


if __name__ == "__main__":
    main()
