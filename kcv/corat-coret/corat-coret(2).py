import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/yaboidimsum/100-Days-of-Python/main/kcv/depression_anxiety_data.csv")

# Replace "Not available" values with NaN
df = df.replace("	Not Availble", np.nan)

# Replace 0 values with NaN
df = df.replace(0, np.nan)

# Compute the mean of each column
mean_values = df.mean(numeric_only=True)

# Use the mean values to fill in the missing values
df.fillna(mean_values, inplace=True)
print(df)
