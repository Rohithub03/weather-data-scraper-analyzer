import pandas as pd

def analyze():
    df = pd.read_csv("data/weather_data.csv")

    print("\nBasic Stats:")
    print(df.describe())

    print("\nHottest Day:")
    print(df.loc[df["temp_max"].idxmax()])

    print("\nColdest Day:")
    print(df.loc[df["temp_min"].idxmin()])

    print("\nRainy Days:")
    print(df[df["precipitation"] > 0])
