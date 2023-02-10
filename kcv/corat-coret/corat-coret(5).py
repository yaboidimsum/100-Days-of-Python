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
    #------------------------------------------------------------------------------
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

    # Classify the level of depression based on the PHQ-9 score
    phq_score_cutoff = [0, 4, 9, 14, 23]
    phq_score_labels = ['None-Minimal', 'Mild', 'Moderate', 'Moderately Severe']
    df['depression_level_phq'] = pd.cut(df['phq_score'], bins=phq_score_cutoff, labels=phq_score_labels)
    print(df['depression_level_phq'])

    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------

    print(df["depressiveness"])

    # Classify the level of depression based on the depression_severity
    # Create a dictionary that maps each label to an integer value
    depression_level_mapping = {'None-minimal': 5, 'Mild': 10, 'Moderate': 15, 'Moderately severe': 20}

    # Apply the mapping to the 'depression_severity' column
    df['depression_severity_int'] = df['depression_severity'].map(depression_level_mapping)

    # Print the result
    # print(df['depression_severity_int'])

    
    depression_severity_int_cutoff = [0, 5, 10, 15, 20]
    depression_severity_int_labels = ['Very low', 'Low', 'Medium', 'High']
    df['depression_level_severity'] = pd.cut(df['depression_severity_int'], bins=depression_severity_int_cutoff, labels=depression_severity_int_labels)
    print(df['depression_level_severity'])


    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------

    # Definisikan skala untuk mengubah string ke angka
    # Define a scale to map string to number
    depression_level_mapping = { False : 5, True: 10}

    # Convert the "depressiveness" column using the map function
    df['depressiveness'] = df['depressiveness'].map(depression_level_mapping)


    # Classify the level of depression based on the depressiveness
    depressiveness_cutoff = [0, 5, 10]
    depressiveness_labels = ['Not depressive', 'Depressive']
    df['depression_level_depressiveness'] = pd.cut(df['depressiveness'].astype(float), bins=depressiveness_cutoff, labels=depressiveness_labels)
    print(df['depression_level_depressiveness'])

    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------

    depression_level_mapping = { False : 5, True: 10}

    # Convert the "depressiveness" column using the map function
    df['suicidal'] = df['suicidal'].map(depression_level_mapping)


    # Classify the level of depression based on the depressiveness
    suicidal_cutoff = [0, 5, 10]
    suicidal_labels = ['Not suicidal', 'Suicidal']
    df['depression_level_suicidal'] = pd.cut(df['suicidal'].astype(float), bins=suicidal_cutoff, labels=suicidal_labels)
    print(df['depression_level_suicidal'])

                                    
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
  
  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  gad_score_cutoff = [0, 4, 9, 14, 21]
  gad_score_labels = ['None-minimal', 'Mild', 'Moderate', 'Moderate Severely']

  df['anxiety_level_gad'] = pd.cut(df['gad_score'], bins=gad_score_cutoff, labels=gad_score_labels)

  print(df['anxiety_level_gad'])

  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  anxiety_level_mapping = {'None-minimal': 5, 'Mild': 10, 'Moderate': 15, 'Moderately severe': 20}
  df['anxiety_severity_int'] = df['depression_severity'].map(anxiety_level_mapping)
  
  anxiety_severity_cutoff = [0, 5, 10, 15, 20]
  anxiety_severity_labels = ['Very low', 'Low', 'Medium', 'High']

  df['anxiety_level_severity'] = pd.cut(df['anxiety_severity_int'], bins=gad_score_cutoff, labels=gad_score_labels)

  print(df['anxiety_level_severity'])  

  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  #------------------------------------------------------------------------------
  anxiety_level_mapping = { False : 5, True: 10}

  # Convert the "depressiveness" column using the map function
  df['anxiousness'] = df['anxiousness'].map(anxiety_level_mapping)


  # Classify the level of depression based on the depressiveness
  suicidal_cutoff = [0, 5, 10]
  suicidal_labels = ['Not anxiousness', 'anxiousness']
  df['anxiety_level_suicidal'] = pd.cut(df['anxiousness'].astype(float), bins=suicidal_cutoff, labels=suicidal_labels)
  print(df['anxiety_level_suicidal'])


anxiety_accuracy(df)
depression_accuracy(df)



