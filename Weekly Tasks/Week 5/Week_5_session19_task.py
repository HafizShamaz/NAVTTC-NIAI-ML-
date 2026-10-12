##########################################
# Support Vector Machine (SVM)
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
y = df["result"]  # output feature

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

scaler = StandardScaler() # SVM needs feature scaling for better performance

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

for kernel in ['linear', 'rbf', 'poly', 'sigmoid']:
    model = SVC(kernel= kernel, C = 1.0)  
    model.fit(x_train, y_train)
    acc = accuracy_score(y_test, model.predict(x_test))
    print(f"SVM ({kernel}) accuracy {acc:.3f}")
    
##########################################
# K-Nearest Neighbors (KNN)
##########################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("students_week5.csv")
x = df.drop(columns= ["student_id", "final_score", "result", "performance"]) # input features
y = df["result"]  # output feature

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

# Without scaling first -- then with scaling -- to see the difference in accuracy
raw = KNeighborsClassifier(n_neighbors=5).fit(x_train, y_train)
print("KNN without scaling:", accuracy_score(y_test, raw.predict(x_test)))

scaler = StandardScaler() # KNN needs feature scaling for better performance
x_train_s, x_test_s = scaler.fit_transform(x_train), scaler.transform(x_test)

for k in [1,3,5,7,9,15,25]: # find the best k
    knn = KNeighborsClassifier(n_neighbors=k).fit(x_train_s, y_train)
    acc = accuracy_score(y_test, knn.predict(x_test_s))
    print(f"KNN (k={k:>2}) accuracy {acc:.3f}")