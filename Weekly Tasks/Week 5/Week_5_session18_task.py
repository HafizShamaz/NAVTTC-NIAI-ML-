##########################################
# Multivariate & Polynomial Regression
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

# # 1: Load the ready made dataset already cleaned

df =pd.read_csv("students_week5.csv")
features = [
    "study_hours", "attendance_pct", "previous_score", "sleep_hours",
    "assignments_done", "internet_access", "extra_tuition", "part_time_job", "parent_education"
    ]

x = df[features] # many inputs -> multivariate
y = df['final_score'] # number to predict

# 2: Split, Train, Predict

x_train, x_test, y_train, y_test = train_test_split (x,y,test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit (x_train, y_train)
pred = model.predict(x_test)

# 3: Evaluate and see what the model learned

print ("R2 :", round(r2_score(y_test,pred), 3))

print ("RMSE :", round (mean_squared_error(y_test, pred) ** 0.5, 2))

print (pd.Series (model.coef_, index = features).round(2))


##########################################
# Polynomial Regression
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df =pd.read_csv("students_week5.csv")

x = df.drop(columns= ["student_id", "final_score", "result", "performance"])
y = df["final_score"]

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42)

# Try degree 1, 2 and 3 -- watch train vs test score

train = []
test = []
degrees = []

for degree in range(1,5):
    model = make_pipeline (PolynomialFeatures(degree), LinearRegression())
    model.fit(x_train, y_train)
    train_r2 = r2_score (y_train, model.predict(x_train))
    test_r2 = r2_score (y_test, model.predict(x_test))
    print(f"Degree {degree}: train R2 = {train_r2:.3f} | test R2 = {test_r2 :.3f}")
    train.append(train_r2)
    test.append(test_r2)
    degrees.append(degree)

plt.plot( degrees, train, marker = "|")
plt.plot( degrees, test, marker = "|")
plt.show()

##########################################
# Logistic Regression (Binary : Pass/Fail)
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"])
y = df["result"]

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

scalar = StandardScaler() # fit on train only

x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

model = LogisticRegression(max_iter = 1000)
model.fit(x_train, y_train)
pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))
print("Classification Report:")
print(classification_report(y_test, pred))

##########################################
# Logistic Regression (Multiclass : High/Medium/Low Performance)
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"])
y = df["performance"] # 0 = Low, 1 = Medium, 2 = High

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

scalar = StandardScaler() # fit on train only

x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

model = LogisticRegression(max_iter = 1000)
model.fit(x_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(x_test)))
print("Confusion Matrix:")
print(confusion_matrix(y_test, model.predict(x_test)))
print("Classification Report:")
print(classification_report(y_test, model.predict(x_test)))
print("Predicted Probabilities:")
print(model.predict_proba(x_test[:3]).round(2))  # Show predicted probabilities for the first 3 test samples