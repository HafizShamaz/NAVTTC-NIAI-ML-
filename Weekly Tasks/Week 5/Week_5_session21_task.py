import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB



df = pd.read_csv("Titanic-Dataset.csv")
# print(df.head())
# print(df.shape)
# print(df.columns)
print(df.info())

### Check for missing values ###
print(df.isna().sum())

### Fill missing values in Age column with mean value
print(df["Age"].isna().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
print(f"After tackling empty rows of Age Column: \n {df.isna().sum()}")

### Fill missing values in Cabin column with LabelEncoder
le = LabelEncoder()
df['Cabin'] = le.fit_transform(df['Cabin'])

print(f"After tackling empty rows of Cabin Column: \n {df.isna().sum()}")

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

le = LabelEncoder()
df['Embarked'] = le.fit_transform(df['Embarked'])

x = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin", "Embarked", "Survived"]) # input features
y = df["Survived"]  # output feature

x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.2, random_state = 42, stratify = y)

models = {
          "Logistic Regression": LogisticRegression(max_iter=1000),
          "SVM (RBF)": SVC(),
          "KNN (k=5)": KNeighborsClassifier(5),
          "Naive Bayes": GaussianNB()
          }

for name, model in models.items():
    # print (name, m)
    pipe = make_pipeline(StandardScaler(),model).fit(x_train,y_train)
    print(f"{name:20s} accuracy = {pipe.score(x_test,y_test):.3f}")