import pandas as pd
import matplotlib.pyplot as plt

def visualize():
    df = pd.read_csv("data/weather_data.csv")

    plt.figure()
    plt.plot(df["date"], df["temp_max"], label="Max Temp")
    plt.plot(df["date"], df["temp_min"], label="Min Temp")
    plt.xticks(rotation=45)
    plt.legend()
    plt.title("Temperature Trend")
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.bar(df["date"], df["precipitation"])
    plt.xticks(rotation=45)
    plt.title("Rainfall Trend")
    plt.tight_layout()
    plt.show()
