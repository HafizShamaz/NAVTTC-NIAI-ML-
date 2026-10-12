##########################################
# Naive Bayes + Model Lab
##########################################

## Formula : P (x1,x2,.....xn | Y) = P (x1 | Y) , P (x2 | Y) ...... P (xn|Y)

############ Code ###############

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
y = df["result"]  # output feature

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

model = GaussianNB() # no scaling needed
model.fit(x_train, y_train)
pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))

new_student = x_test.iloc[[1]] # one student from the test set
print(new_student)
print ("Pass Probability:", model.predict_proba(new_student)[0][1].round(2))

############ Code 2: All 4 classifiers Head to Head ###############

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
y = df["result"]  # output feature

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

models = {
          "Logistic Regression": LogisticRegression(max_iter=1000),
          "SVM (RBF)": SVC(),
          "KNN (k=5)": KNeighborsClassifier(5),
          "Naive Bayes": GaussianNB()
          }
for name, m in models.items():
    # print (name, m)
    pipe = make_pipeline(StandardScaler(),m).fit(x_train,y_train)
    print(f"{name:20s} accuracy = {pipe.score(x_test,y_test):.3f}")