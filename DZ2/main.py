import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def task1(train_df):
    if 'male' in set(train_df['Sex']):
        train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})

    if 'S' in set(train_df['Embarked']):
        train_df['Embarked'] = train_df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    sns.pairplot(train_df[["Age", "Fare", "Pclass", "Sex", "SibSp", "Parch", "Embarked", "Survived"]])
    plt.show()


def task2(train_df):
    sns.boxplot(data=train_df[["Fare", "Pclass"]], x=train_df["Pclass"], y=train_df["Fare"])
    plt.show()

    train_df['Fare_no_out'] = train_df['Fare']
    fare_pclass1 = train_df[train_df['Pclass'] == 1]['Fare']
    fare_pclass2 = train_df[train_df['Pclass'] == 2]['Fare']
    fare_pclass3 = train_df[train_df['Pclass'] == 3]['Fare']
    fare_pclass1_no_out = (
            ((fare_pclass1.mean() - 1 * fare_pclass1.std()) <= fare_pclass1) &
            ((fare_pclass1.mean() + 1 * fare_pclass1.std()) >= fare_pclass1)
    )
    fare_pclass2_no_out = (
            ((fare_pclass2.mean() - 1 * fare_pclass2.std()) <= fare_pclass2) &
            ((fare_pclass2.mean() + 1 * fare_pclass2.std()) >= fare_pclass2)
    )
    fare_pclass3_no_out = (
            ((fare_pclass3.mean() - 1 * fare_pclass3.std()) <= fare_pclass3) &
            ((fare_pclass3.mean() + 1 * fare_pclass3.std()) >= fare_pclass3)
    )

    train_df['Fare_no_out'] = fare_pclass1_no_out.append(fare_pclass2_no_out) \
        .append(fare_pclass3_no_out)

    sns.boxplot(x='Pclass', y='Fare', data=train_df[train_df['Fare_no_out']])
    plt.show()


def task3(train_df):
    if 0 in set(train_df['Survived']):
        train_df['Survived'] = train_df['Survived'].map({0: 'Dead', 1: 'Survived'})

    sns.countplot(x="Survived", hue="Sex", data=train_df)
    plt.show()


def task4(train_df):
    if 0 in set(train_df['Survived']):
        train_df['Survived'] = train_df['Survived'].map({0: 'Dead', 1: 'Survived'})

    sns.countplot(x="Survived", hue="Pclass", data=train_df)
    plt.show()


def age_category(age):
    if age < 30:
        return "Young"
    elif age > 60:
        return "Old"
    else:
        return "None"


def task5(train_df):
    if 0 in set(train_df['Survived']):
        train_df['Survived'] = train_df['Survived'].map({0: 'Dead', 1: 'Survived'})

    age_categories = [age_category(age) for age in train_df.Age]
    train_df["AgeCategory"] = age_categories
    train_df_filtered = train_df[train_df["AgeCategory"] != "None"]

    sns.countplot(x="Survived", hue="AgeCategory", data=train_df_filtered)
    plt.show()


if __name__ == '__main__':
    train_df = pd.read_csv("titanic_train.csv", index_col='PassengerId')
    train_df = train_df.drop('Cabin', axis=1).dropna()

    # task1(train_df)
    # task2(train_df)
    # task3(train_df)
    # task4(train_df)
    task5(train_df)