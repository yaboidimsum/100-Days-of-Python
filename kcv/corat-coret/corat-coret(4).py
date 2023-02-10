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

    # Classify the level of depression based on the PHQ-9 score
    phq_score_cutoff = [0, 5, 10, 15, 20]
    phq_score_labels = ['Low', 'Moderate', 'Moderately Severe', 'Severe']
    df['depression_level'] = pd.cut(df['phq_score'], bins=phq_score_cutoff, labels=phq_score_labels)
    print(df['depression_level'])

    # Contoh dataframe
    data = {'depressiveness': ['TRUE', 'FALSE']}
    df = pd.DataFrame(data)

    # Definisikan skala untuk mengubah string ke angka
    scale = {'TRUE': 1, 'FALSE': 0}

    # Ubah kolom depression_severity menggunakan fungsi map()
    df['depressiveness'] = df['depressiveness'].map(scale)

    # Classify the level of depression based on the PHQ-9 score
    depressiveness_cutoff = [0, 5, 10, 15, 20]
    depressiveness_labels = ['Low', 'Moderate', 'Moderately Severe', 'Severe']
    df['depression_level'] = pd.cut(df['depressiveness'], bins=depressiveness_cutoff, labels=depressiveness_labels)
    print(df['depression_level'])

    # Contoh dataframe
    data = {'suicidal': ['TRUE', 'FALSE']}
    df = pd.DataFrame(data)
    # Definisikan skala untuk mengubah string ke angka
    scale = {'TRUE': 1, 'FALSE': 0}
    # Ubah kolom depression_severity menggunakan fungsi map()
    df['suicidal'] = df['suicidal'].map(scale)

    # Classify the level of depression based on the PHQ-9 score
    suicidal_cutoff = [0, 5, 10, 15, 20]
    suicidal_labels = ['Low', 'Moderate', 'Moderately Severe', 'Severe']
    df['depression_level'] = pd.cut(df['suicidal'], bins=suicidal_cutoff, labels=suicidal_labels)
    print(df['depression_level'])

    # Contoh dataframe
    data = {'depression_severity': ['mild', 'moderate', 'severe', 'very severe']}
    df = pd.DataFrame(data)

    # Definisikan skala untuk mengubah string ke angka
    scale = {'mild': 1, 'moderate': 2, 'severe': 3, 'very severe': 4}

    # Ubah kolom depression_severity menggunakan fungsi map()
    df['depression_severity'] = df['depression_severity'].map(scale)

    # Classify the level of depression based on the PHQ-9 score
    depression_severity_cutoff = [0, 5, 10, 15, 20]
    depression_severity_labels = ['Low', 'Moderate', 'Moderately Severe', 'Severe']
    df['depression_level'] = pd.cut(df['depression_severity'], bins=depression_severity_cutoff, labels=depression_severity_labels)
    print(df['depression_level'])

depression_accuracy(df)
                                    
# def anxiety_accuracy(df):
#   # Select the relevant columns
#   X = df[['gad_score', 'anxiety_severity', 'anxiousness']]
#   y = df['anxiety_diagnosis']

#     # Split the data into training and testing sets
#   # Convert the categorical variable "depression_severity" into numerical data using one-hot encoding
#   X = pd.get_dummies(X, columns=['anxiety_severity'])

#   y = y.astype('int')

#   # Split the data into training and testing sets
#   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#   # Train the logistic regression model
#   model = LogisticRegression(solver='lbfgs')
#   model.fit(X_train, y_train)

#   # Make predictions on the testing set
#   y_pred = model.predict(X_test)

#   # Evaluate the model's performance
#   acc = accuracy_score(y_test, y_pred)
#   print('Anxiety Accuracy: {:.2f}%'.format(acc * 100))

#   gad_score_cutoff = [0, 5, 10, 15, 20]
#   gad_score_labels = ['Low', 'Moderate', 'Moderately Severe', 'Severe']

#   df['anxiety_level'] = pd.cut(df['gad_score'], bins=gad_score_cutoff, labels=gad_score_labels)

#   print(df['anxiety_level'])

# anxiety_accuracy(df)



