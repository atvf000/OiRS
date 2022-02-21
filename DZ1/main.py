# import numpy as np
import pandas as pd
import collections

import matplotlib.pyplot as plt


def task1(data):
    print("Task 1")
    print(f'male = {len(data[data["Sex"] == "male"])} \n'
          f'female = {len(data[data["Sex"] == "female"])} ')


def task2(data):
    print("\nTask 2")
    data["Pclass"].hist()
    plt.show()

    data[data["Sex"] == "male"].Pclass.hist()
    plt.show()

    data[data["Sex"] == "female"].Pclass.hist()
    plt.show()

    print(f'male in 2nd class ='
          f' {len(data[(data["Pclass"] == 2) & (data["Sex"] == "male")])}')


def task3(data):
    print("\nTask 3")
    fare_data = data["Fare"].describe()
    print(f'mean = {fare_data["50%"]:.2f} \n'
          f'std = {fare_data["std"]:.2f}')


def task4(data):
    print("\nTask 4")
    print(f'30: {data[data["Age"] < 30]["Survived"].mean() * 100:.1f}% \n'
          f'60: {data[data["Age"] > 60]["Survived"].mean() * 100:.1f}%')


def task5(data):
    print("\nTask 5")
    print(f'female: {data[data["Sex"] == "female"]["Survived"].mean() * 100:.1f}% \n'
          f'male: {data[data["Sex"] == "male"]["Survived"].mean() * 100:.1f}%')


def task6(data):
    print("\nTask 6")

    def count_name(names: str):
        splitted_name = names.split(' ')[2:]
        for name in splitted_name:
            dictionary[name] += 1

    dictionary = collections.defaultdict(int)
    data["Name"].apply(count_name)
    most_popular_name = max(dictionary, key=dictionary.get)
    print(f'most popular name - {most_popular_name}')


def task8(data):
    print("\nTask 8")


def main():
    data = pd.read_csv("titanic_train.csv", index_col="PassengerId")
    task1(data)
    task2(data)
    task3(data)
    task4(data)
    task5(data)
    task6(data)


main()
