import pandas as pd
from pprint import pprint


def taskA(**context):
    url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
    df = pd.read_csv(url, sep=",").replace('"', "", regex=True)
    # pprint(df)
    return df


def taskB():
    df = taskA()
    selected_columns = ["Team", "Yellow Cards", "Red Cards"]
    selected_df = df[selected_columns]
    return print(selected_df)


def taskC():
    df = taskA()
    num_teams = df["Team"].nunique()
    return print(f"\nNumber of teams participated: {num_teams}")


def taskD():
    df = taskA()
    selected_columns = ["Team", "Goals"]
    selected_df = df[selected_columns]
    filtered_df = selected_df[selected_df["Goals"] > 6]
    return print(f"\nTeams that scored more than 6 goals: \n{filtered_df}")


if __name__ == "__main__":
    taskB()
    taskC()
    taskD()
