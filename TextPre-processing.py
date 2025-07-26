# Scenario 4: Text Pre-processing
# Task: Clean a text column in a DataFrame by:

# 1. Converting to lowercase.

# 2. Removing special characters (e.g., !, @).

# 3. Tokenizing the text.

import pandas as pd
import re


def clean_text(df, col):
    df[col] = df[col].str.lower()  
    df[col] = df[col].apply(lambda x: re.sub(r'[^a-z0-9 ]', '', x))  
    df[col] = df[col].apply(lambda x: ' '.join(x.split()))  
    return df

df = pd.DataFrame({'text': ['Hello@World!', 'Python#Rocks']})


print("before cleaning:")
print(df)


df = clean_text(df, 'text')


print("\n after cleaning:")
print(df)
