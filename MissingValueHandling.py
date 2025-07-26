# Scenario 3: Missing Value Handling
# Task: A dataset has missing values in the "income" column. Write code to:

# 1. Replace missing values with the median if the data is normally distributed.

# 2. Replace with the mode if skewed.
# Use Pandas and a skewness threshold of 0.5.


import pandas as pd
import numpy as np

# def fill_income(df):
#     if abs(df['income'].skew()) < 0.5:
#         df['income'].fillna(df['income'].median(), inplace=True)
#     else:
#         df['income'].fillna(df['income'].mode()[0], inplace=True)
#     return df

data = {
    'name': ['max', 'Bob', 'Charu', 'Dev', 'Emli'],
    'income': [50000, np.nan, 52000, 50000, np.nan]
}

df = pd.DataFrame(data)

print("before filling:")
print(df)


def fill_income(df):
    skew_val = df['income'].skew()
    print("\nSkewness of 'income':", round(skew_val, 2))
    
    if abs(skew_val) < 0.5:
        fill_value = df['income'].median()
        print("Filling missing values with median:", fill_value)
        df['income'].fillna(fill_value, inplace=True)
    else:
        fill_value = df['income'].mode()[0]
        print("Filling missing values with mode:", fill_value)
        df['income'].fillna(fill_value, inplace=True)
    return df


df_filled = fill_income(df)

print("\n after filling:")
print(df_filled)
