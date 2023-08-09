import random
import csv

PLAYERS = ["Josh", "Luke", "Kate", "Mark", "Mary"]


def generate_rate() -> list:
    rate = []
    for i in range(0, 100):
        for name in PLAYERS:
            score = random.randint(1, 1000)
            rate.append([name, score])
    return rate


def save_in_csv(rate: list) -> csv:
    rate_csv = "Projector-practise\Lec10_HW\scores.csv"
    with open(rate_csv, "w") as csvfile:
        csvfile = csv.writer(csvfile)
        csvfile.writerow(["Name", "Score"])
        for i in rate:
            csvfile.writerow(i)
    return rate_csv


def generate_high_scores(rate_csv: csv) -> dict:
    high_scores = {}
    with open(rate_csv, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"]
            score = int(row["Score"])
            if name not in high_scores or score > high_scores[name]:
                high_scores[name] = score
        return high_scores


def save_highscore_in_csv(high_dict: dict) -> csv:
    high_scores = "Projector-practise/Lec10_HW/high_scores.csv"
    with open(high_scores, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Player name", "Highest score"])
        for name, highest_score in sorted(
            high_dict.items(), key=lambda item: item[1], reverse=True
        ):
            csv_writer.writerow([name, highest_score])
    return high_scores


if __name__ == "__main__":
    rate_data = generate_rate()
    rate_csv = save_in_csv(rate_data)
    high_dict = generate_high_scores(rate_csv)
    save_highscore_in_csv(high_dict)
