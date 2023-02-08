import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/yaboidimsum/100-Days-of-Python/main/kcv/depression_anxiety_data.csv")

# Replace "Not available" values with NaN
df = df.replace("Not Availble", np.nan)

# Replace 0 values with NaN
columns_to_replace = ['bmi', 'anxiety_severity', 'epworth_score']
# Replace 0 values in the specified columns with NaN
df[columns_to_replace] = df[columns_to_replace].replace(0, np.nan)

# df = df.replace(int(0), np.nan)

# Replace NA values with NaN
df = df.replace("NA", np.nan)

df = df.dropna()

# Compute the mean of each column
mean_values = df.mean(numeric_only=True)

# Use the mean values to fill in the missing values
df.fillna(mean_values, inplace=True)

# One-hot encode the 'gender' column
df = pd.get_dummies(df, columns=['gender'])

def depression_accuracy(df):
  #------------------------------------------------------------------------------
  # Select the relevant columns
  X = df[['phq_score', 'depression_severity', 'depressiveness', 'suicidal']]
  y = df['depression_diagnosis']

  # Split the data into training and testing sets
  # Convert the categorical variable "depression_severity" into numerical data using one-hot encoding
  X = pd.get_dummies(X, columns=['depression_severity'])

  y = y.astype('int')


  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  # Train the logistic regression model
  model = LogisticRegression(solver='lbfgs')
  model.fit(X_train, y_train)

  # Make predictions on the testing set
  y_pred = model.predict(X_test)

  # Evaluate the model's performance
  acc = accuracy_score(y_test, y_pred)
  print('Depression Accuracy: {:.2f}%'.format(acc * 100))

def anxiety_accuracy(df):
  # Select the relevant columns
  X = df[['gad_score', 'anxiety_severity', 'anxiousness']]
  y = df['anxiety_diagnosis']

    # Split the data into training and testing sets
  # Convert the categorical variable "depression_severity" into numerical data using one-hot encoding
  X = pd.get_dummies(X, columns=['anxiety_severity'])

  y = y.astype('int')

  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  # Train the logistic regression model
  model = LogisticRegression(solver='lbfgs')
  model.fit(X_train, y_train)

  # Make predictions on the testing set
  y_pred = model.predict(X_test)

  # Evaluate the model's performance
  acc = accuracy_score(y_test, y_pred)
  print('Anxiety Accuracy: {:.2f}%'.format(acc * 100))

depression_accuracy(df)
anxiety_accuracy(df)
