import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/yaboidimsum/100-Days-of-Python/main/kcv/depression_anxiety_data.csv")

#----------------------------------------------------------------------------
# Check for missing values
print("Number of missing values: ", df.isnull().sum().sum())

# Handle missing values by imputing them with the mean or median of the column
from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
df[features] = imp.fit_transform(df[features])

#---------------------------------------------------------------------------

# Check for outlier values
for feature in features:
    q1, q3 = df[feature].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    print("Outliers for feature '{}': {}".format(feature, outliers))
#--------------------------------------------------------------------------

# Handle outlier values by replacing them with the median of the column
for feature in features:
    q1, q3 = df[feature].quantile([0.25, 0.75])
    iqr = q3 - q1
    median = df[feature].median()
    df[feature] = df[feature].apply(lambda x: median if x < q1 - 1.5 * iqr or x > q3 + 1.5 * iqr else x)

#--------------------------------------------------------------------------

# Check for infinite values
print("Number of infinite values: ", df[features].isin([np.inf, -np.inf]).sum().sum())

# Handle infinite values by replacing them with the median of the column
for feature in features:
    median = df[feature].median()
    df[feature] = df[feature].apply(lambda x: median if x == np.inf or x == -np.inf else x)

#------------------------------------------------------------------------


# Define features and target variables
features = ['age', 'bmi', 'phq_score', 'gad_score', 'epworth_score']
target = 'depression_diagnosis'

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=0)

# Fit the logistic regression model
clf = LogisticRegression(random_state=0)
y_train = y_train.astype(float)
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))

