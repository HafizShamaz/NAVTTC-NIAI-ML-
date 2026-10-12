##########################################
# Decision tree
##########################################

# Import pandas to read and manipulate tabular data from CSV files.
import pandas as pd

# Import train_test_split to split the dataset into training and testing sets.
from sklearn.model_selection import train_test_split

# Import DecisionTreeClassifier to build the classification model and export_text
# to display the learned decision tree as text rules.
from sklearn.tree import DecisionTreeClassifier, export_text

# Load the student dataset from the specified CSV file into a DataFrame.
# Each row represents a student record, and each column is a feature or label.
df = pd.read_csv("C:\\Users\\HP ZBOOK\\Desktop\\NIAI-NAVTTC-CohorotII(AI-ML)\\Course Material\\Datasets\\students_week5.csv")

# Create the feature matrix X by dropping the columns that are not useful as inputs:
# 'student_id' is an identifier, 'final_score' is a direct outcome-related value,
# 'result' is the target label, and 'performance' is a derived label that should not be used as a feature.
X = df.drop(columns=["student_id", "final_score", "result", "performance"])

# Create the target array y containing the label to predict: whether the student passed or failed.
y = df["result"]

# Split data into training and testing sets.
# test_size=0.2 means 20% of the data is reserved for evaluation.
# random_state=42 ensures the split is reproducible every time.
# stratify=y keeps the class distribution balanced in both subsets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Trees do not require feature scaling because splitting thresholds are based on feature values directly.
# Scaling is usually unnecessary for decision trees and other tree-based algorithms.

# Loop over two different maximum tree depths:
# 3 means a small, simpler tree;
# None means a fully grown tree (until leaves are pure or no further split is possible).
for depth in [3, None]:  # None = grow until every leaf is pure

    # Create a decision tree classifier with the current max_depth value.
    # random_state=42 keeps the tree deterministic.
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)

    # Train the model on the training data using the feature matrix X_train and labels y_train.
    tree.fit(X_train, y_train)

    # Print the model accuracy on both the training and testing datasets.
    # The format specifier .3f prints the score to three decimal places.
    # Example output for this dataset:
    # max_depth = 3: train = 0.831 | test = 0.785
    # max_depth = None: train = 1.000 | test = 0.790
    print(f"max_depth = {depth}: train = {tree.score(X_train, y_train): .3f}"
          f" | test = {tree.score(X_test, y_test):.3f}")

# Train a smaller tree with max_depth=2 to make the learned rules easier to read.
# This helps us inspect what the model is actually learning.
small = DecisionTreeClassifier(max_depth=1, random_state=42).fit(X_train, y_train)

# Convert the trained decision tree into a human-readable text representation.
# This prints the rule structure in a format similar to a decision tree diagram.
# Example output for this dataset:
# |--- feature_0 <= 2.35
# |   |--- feature_2 <= 76.50
# |   |   |--- class: 0
# |   |--- feature_2 >  76.50
# |   |   |--- class: 1
# |--- feature_0 >  2.35
# |   |--- feature_3 <= 5.05
# |   |   |--- class: 0
# |   |--- feature_3 >  5.05
# |   |   |--- class: 1

print(export_text(small))

# This line is commented out because the tree uses default feature names like feature_0, feature_1, etc.
# If you want to print more readable column names instead, uncomment the following line:
# print(export_text(small, feature_names=list(X.columns)))

##########################################
# Random Forest + Feature Importance
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
 
df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
 
# 200 trees, each trained on a random sample of rows + features
forest = RandomForestClassifier(n_estimators=200, random_state=42)
forest.fit(X_train, y_train)
print('Random Forest test accuracy:', round(forest.score(X_test, y_test), 3))
 
# Which features mattered most?
importance = pd.Series(forest.feature_importances_, index=X.columns)
print(importance.sort_values(ascending=False).round(3))


##########################################
# Boosting & the Big Comparison 
##########################################


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
 
df = pd.read_csv('students_week5.csv')
X = df.drop(columns=['student_id', 'final_score', 'result', 'performance'])
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
 
models = {'Single Tree (full)': DecisionTreeClassifier(random_state=42),
          'Random Forest':      RandomForestClassifier(200, random_state=42),
          'Gradient Boosting':  GradientBoostingClassifier(random_state=42),
          'SVM (Week 5 best)':  make_pipeline(StandardScaler(), SVC())}
for name, m in models.items():
    m.fit(X_train, y_train)
    print(f'{name:20s} train = {m.score(X_train, y_train):.3f}'
          f' | test = {m.score(X_test, y_test):.3f}')
