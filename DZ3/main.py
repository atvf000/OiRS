import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def make_bmi(height_inch, weight_pound):
    METER_TO_INCH, KILO_TO_POUND = 39.37, 2.20462
    return (weight_pound / KILO_TO_POUND) / (height_inch / METER_TO_INCH) ** 2


def task01(data):
    sns.pairplot(data[["Height", "Weight", "BMI"]])
    plt.show()

def task02(data):
    def weight_category(weight):
        if weight < 120:
            return 1
        elif weight >= 150:
            return 3
        else:
            return 2

    data["weight_category"] = data["Weight"].apply(weight_category)
    sns.boxplot(data=data, y="Height", x="weight_category")
    plt.show()

def task03(data):
    data.plot(kind="scatter", x="Weight", y="Height")
    plt.show()

if __name__ == '__main__':
    data = pd.read_csv("weights_heights.csv", index_col="Index")
    data["BMI"] = data.apply(lambda row: make_bmi(row["Height"], row["Weight"]), axis=1)
    task01(data)
    task02(data)
    task03(data)
