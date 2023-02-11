import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
# df = pd.get_dummies(df, columns=['gender'])

def depression_accuracy(df):
    # Select relevant columns for model
    X = df[['phq_score', 'depression_severity', 'depressiveness', 'suicidal']]
    y = df['depression_diagnosis']

    # Convert categorical column to numerical using one-hot encoding
    X = pd.get_dummies(X, columns=['depression_severity'])

    # Convert target column to integer
    y = y.astype('int')

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train logistic regression model
    model = LogisticRegression(solver='lbfgs')
    model.fit(X_train, y_train)

    # Make predictions on testing set
    y_pred = model.predict(X_test)

    # Evaluate model performance
    acc = accuracy_score(y_test, y_pred)
    print('Depression Accuracy: {:.2f}%'.format(acc * 100))

    # Classify depression level based on PHQ-9 score
    phq_score_cutoff = [0, 4, 9, 14, 23]
    phq_score_labels = ['None-Minimal', 'Mild', 'Moderate', 'Moderately Severe']
    df['depression_level_phq'] = pd.cut(df['phq_score'], bins=phq_score_cutoff, labels=phq_score_labels)
    print(df['depression_level_phq'])

    # Classify depression level based on depression severity
    depression_level_mapping = {'None-minimal': 5, 'Mild': 10, 'Moderate': 15, 'Moderately severe': 20}
    df['depression_severity_int'] = df['depression_severity'].map(depression_level_mapping)
    depression_severity_int_cutoff = [0, 5, 10, 15, 20]
    depression_severity_int_labels = ['Very low', 'Low', 'Medium', 'High']
    df['depression_level_severity'] = pd.cut(df['depression_severity_int'], bins=depression_severity_int_cutoff, labels=depression_severity_int_labels)
    print(df['depression_level_severity'])

    # Classify depression level based on depressiveness
    depression_level_mapping = {False: 5, True: 10}
    df['depressiveness'] = df['depressiveness'].map(depression_level_mapping)
    depressiveness_cutoff = [0, 5, 10]
    depressiveness_labels = ['Not depressive', 'Depressive']
    df['depression_level_depressiveness'] = pd.cut(df['depressiveness'].astype(float), bins=depressiveness_cutoff, labels=depressiveness_labels)
    print(df['depression_level_depressiveness'])


    # Classify depression level based on suicidal
    depression_level_mapping = {False: 5, True: 10}
    df['suicidal'] = df['suicidal'].map(depression_level_mapping)
    suicidal_cutoff_values = [0, 5, 10]
    suicidal_labels = ['Not Suicidal', 'Suicidal']
    df['Depression Level (Suicidal)'] = pd.cut(df['suicidal'].astype(float), bins=suicidal_cutoff_values, labels=suicidal_labels)
    print(df['Depression Level (Suicidal)'])

    # Plot bar plots for each depression level
    # plt.figure(figsize=(10, 6))
    df['depression_level_phq'].value_counts().plot(kind='bar', color='blue', alpha=0.5)
    plt.title('Depression Level based on PHQ-9 Score')
    plt.xlabel('Depression Level')
    plt.ylabel('Number of Patients')
    plt.show()

    # plt.figure(figsize=(10, 6))
    df['depression_level_severity'].value_counts().plot(kind='bar', color='red', alpha=0.5)
    plt.title('Depression Level based on Depression Severity')
    plt.xlabel('Depression Level')
    plt.ylabel('Number of Patients')
    plt.show()

    # plt.figure(figsize=(10, 6))
    df['depression_level_depressiveness'].value_counts().plot(kind='bar', color='green', alpha=0.5)
    plt.title('Depression Level based on Depressiveness')
    plt.xlabel('Depression Level')
    plt.ylabel('Number of Patients')
    plt.show()

    # plt.figure(figsize=(10, 6))
    df['Depression Level (Suicidal)'].value_counts().plot(kind='bar', color='orange', alpha=0.5)
    plt.title('Depression Level based on Suicidal Tendencies')
    plt.xlabel('Depression Level')
    plt.ylabel('Number of Patients')
    plt.show()

                                    
def anxiety_accuracy(df):
  # Select the relevant columns for the model
  X = df[['gad_score', 'anxiety_severity', 'anxiousness']]
  y = df['anxiety_diagnosis']
  
  # One-hot encode the categorical variable "anxiety_severity"
  X = pd.get_dummies(X, columns=['anxiety_severity'])

  # Convert the target variable to integer type
  y = y.astype('int')

  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  # Train a logistic regression model
  model = LogisticRegression(solver='lbfgs')
  model.fit(X_train, y_train)

  # Make predictions on the testing data
  y_pred = model.predict(X_test)

  # Evaluate the model's accuracy
  acc = accuracy_score(y_test, y_pred)
  print('Anxiety Accuracy: {:.2f}%'.format(acc * 100))

  # Classify the level of anxiety based on the GAD score
  gad_score_cutoff = [0, 4, 9, 14, 21]
  gad_score_labels = ['None-minimal', 'Mild', 'Moderate', 'Moderate Severely']
  df['anxiety_level_gad'] = pd.cut(df['gad_score'], bins=gad_score_cutoff, labels=gad_score_labels)
  print(df['anxiety_level_gad'])

  # Convert the anxiety severity to numerical data
  anxiety_level_mapping = {'None-minimal': 5, 'Mild': 10, 'Moderate': 15, 'Moderately severe': 20}
  df['anxiety_severity_int'] = df['depression_severity'].map(anxiety_level_mapping)
  
  # Classify the level of anxiety based on the anxiety severity
  anxiety_severity_cutoff = [0, 5, 10, 15, 20]
  anxiety_severity_labels = ['Very low', 'Low', 'Medium', 'High']
  df['anxiety_level_severity'] = pd.cut(df['anxiety_severity_int'], bins=gad_score_cutoff, labels=gad_score_labels)
  print(df['anxiety_level_severity'])

  # Convert the "anxiousness" column to numerical data
  anxiety_level_mapping = { False : 5, True: 10}
  df['anxiousness'] = df['anxiousness'].map(anxiety_level_mapping)

  # Classify the level of anxiety based on the anxiousness
  anxiousness_cutoff = [0, 5, 10]
  anxiousness_labels = ['Not anxiousness', 'anxiousness']
  df['anxiety_level_anxiousness'] = pd.cut(df['anxiousness'].astype(float), bins=anxiousness_cutoff, labels=anxiousness_labels)
  print(df['anxiety_level_anxiousness'])

  gad_level_counts = df['anxiety_level_gad'].value_counts().plot(kind='bar', color='red', alpha=0.5)

  # Plot the count of each anxiety level
  # plt.bar(gad_level_counts.index, gad_level_counts.values)
  plt.xlabel('GAD Score')
  plt.ylabel('Number of Patients')
  plt.title('Anxiety Level based on GAD Score')
  plt.show()

  # Count the number of instances for each anxiety level based on the anxiety severity
  severity_level_counts = df['anxiety_level_severity'].value_counts().plot(kind='bar', color='green', alpha=0.5)

  # Plot the count of each anxiety level
  # plt.bar(severity_level_counts.index, severity_level_counts.values)
  plt.xlabel('Anxiety Severity')
  plt.ylabel('Number of Patients')
  plt.title('Anxiety Level based on Anxiety Severity')
  plt.show()

  # Count the number of instances for each anxiety level based on anxiousness
  anxiousness_level_counts = df['anxiety_level_anxiousness'].value_counts().plot(kind='bar', color='orange', alpha=0.5)

  # Plot the count of each anxiety level
  # plt.bar(anxiousness_level_counts.index, anxiousness_level_counts.values)
  plt.xlabel('Anxiousness')
  plt.ylabel('Number of Patients')
  plt.title('Anxiety Level based on Anxiousness')
  plt.show()

def depression_anxiety_count(df):
    # Run the depression_accuracy function to get the depression diagnosis
    depression_accuracy(df)

    # Run the anxiety_accuracy function to get the anxiety diagnosis
    anxiety_accuracy(df)

    # Categorize the data based on school year, age, gender, bmi, and who_bmi

    school_year_counts = df.groupby('school_year').size().reset_index(name='counts')
    age_counts = df.groupby('age').size().reset_index(name='counts')
    gender_counts = df.groupby('gender').size().reset_index(name='counts')
    # bmi_counts = df.groupby('bmi').size().reset_index(name='counts')
    who_bmi_counts = df.groupby('who_bmi').size().reset_index(name='counts')

    # Get the number of people with depression and anxiety
    depression_counts = df.groupby('depression_diagnosis').size().reset_index(name='counts')
    anxiety_counts = df.groupby('anxiety_diagnosis').size().reset_index(name='counts')

    # Print the results
    print('Depression Counts:')
    print(depression_counts)
    print('Anxiety Counts:')
    print(anxiety_counts)
    print('School Year Counts:')
    print(school_year_counts)
    print('Age Counts:')
    print(age_counts)
    print('Gender Counts:')
    print(gender_counts)
    # print('BMI Counts:')
    # print(bmi_counts)
    print('WHO BMI Counts:')
    print(who_bmi_counts)

def depression_breakdown(df):
    # Run the depression_accuracy function to get the depression diagnosis
    depression_accuracy(df)

    # Get the number of people with depression
    depression_counts = df.groupby('depression_diagnosis').size().reset_index(name='counts')
    print('Depression Counts:')
    print(depression_counts)

    # Categorize the data based on depression severity, PHQ-9 score, depressiveness, and suicidal thoughts
    severity_counts = df.groupby(['depression_diagnosis', 'depression_severity']).size().reset_index(name='counts')
    phq_counts = df.groupby(['depression_diagnosis', 'phq_score']).size().reset_index(name='counts')
    depressiveness_counts = df.groupby(['depression_diagnosis', 'depressiveness']).size().reset_index(name='counts')
    suicidal_counts = df.groupby(['depression_diagnosis', 'suicidal']).size().reset_index(name='counts')

    # Print the results
    print('Depression Severity Counts:')
    print(severity_counts)
    print('PHQ-9 Counts:')
    print(phq_counts)
    print('Depressiveness Counts:')
    print(depressiveness_counts)
    print('Suicidal Thoughts Counts:')
    print(suicidal_counts)

# def depression_breakdown_age(df):
#     depression_diagnosis = df[['phq_score', 'depression_severity', 'depressiveness', 'suicidal']]

#     depression_diagnosis['total'] = depression_diagnosis.sum(axis=1)
#     depression_diagnosis['depression_diagnosis'] = depression_diagnosis['total'] >= 6
    
#     # Separate the age into the 4 groups
#     df['age_group'] = pd.cut(df['age'], bins=[17, 21, 25, 29, 100], labels=['18-21', '22-25', '26-29', '30 and above'])
    
#     # Count the number of people with depression for each age group
#     depression_counts = depression_diagnosis.groupby(['depression_diagnosis', 'age_group']).size().reset_index(name='counts')
    
#     # Print the results
#     print('Depression Counts by Age Group:')
#     print(depression_counts)

# def depression_age_group_count(df):
#     # Create the age_group column
#     df['age_group'] = pd.cut(df['age'], bins=[17, 21, 25, 29, 100], labels=['18-21', '22-25', '26-29', '30 above'])

#     # Group the data by the age_group column
#     age_group_counts = df.groupby('age_group').size().reset_index(name='counts')

#     # Get the number of people with depression
#     depression_counts = df.groupby('depression_diagnosis').size().reset_index(name='counts')

#     # Print the results
#     print('Depression Counts:')
#     print(depression_counts)
#     print('Age Group Counts:')
#     print(age_group_counts)

def depression_age_group_count(df):
    # Create the age_group column
    df['age_group'] = pd.cut(df['age'], bins=[17, 21, 25, 29, 100], labels=['18-21', '22-25', '26-29', '30 above'])
    df = df[df['depression_diagnosis'] == True]
    # Create the depression_level column
    df['depression_level'] = 'None-minimal'
    df.loc[df['phq_score'] >= 9, 'depression_level'] = 'Mild'
    df.loc[df['phq_score'] >= 14, 'depression_level'] = 'Moderate'
    df.loc[df['phq_score'] >= 23, 'depression_level'] = 'Moderately severe'
    df.loc[df['phq_score'] >= 20, 'depression_level'] = 'Severe'
    
    phq_score_cutoff = [0, 4, 9, 14, 23]
    phq_score_labels = ['None-Minimal', 'Mild', 'Moderate', 'Moderately Severe']

    # Group the data by the age_group and depression_diagnosis columns
    age_group_depression_counts = df.groupby(['age_group', 'depression_diagnosis']).size().reset_index(name='counts')
    
    # Group the data by the depression_level and depression_diagnosis columns
    depression_level_counts = df.groupby(['depression_level', 'depression_diagnosis']).size().reset_index(name='counts')
    
    # Print the results
    # print('Depression Level Counts:')
    # print(depression_level_counts)
    print('Age Group and Depression Counts:')
    print(age_group_depression_counts)

def depression_age_group_level_mode(df):
    # Create the age_group column
    df['age_group'] = pd.cut(df['age'], bins=[17, 21, 25, 29, 100], labels=['18-21', '22-25', '26-29', '30 above'])
    
    # Get the number of people with depression for each age group
    depression_age_group_counts = df[df['depression_diagnosis'] == True].groupby(['age_group']).size().reset_index(name='counts')
    
    # Get the mode depression level for each age group
    depression_level_mode = df[df['depression_diagnosis'] == True].groupby(['age_group'])['depression_level'].apply(lambda x: x.mode()[0]).reset_index(name='depression_level_mode')
    
    # Merge the two dataframes on the 'age_group' column
    result = pd.merge(depression_age_group_counts, depression_level_mode, on='age_group')
    
    # Print the results
    print('Depression Counts and Depression Level Mode by Age Group:')
    print(result)




# depression_breakdown(df)
# depression_breakdown_age(df)
depression_age_group_level_mode(df)
depression_age_group_count(df)


