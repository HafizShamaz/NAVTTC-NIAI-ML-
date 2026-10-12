import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("Books_Data_Clean.csv")

############# Task 1 #############

print (df.shape) # tell the total rows and coloumns

############# Task 2 #############

print (df.isnull().sum()) # returns total no of null values in each coloumn 

############# Task 3 #############

print (df["Book_average_rating"].mean()) # calculate the mean of book average rating

############# Task 4 #############

print (df["gross sales"].sum()) # shows the sum of the gross sales

############# Task 5 #############

print(df["genre"].value_counts().idxmax()) # returns the most use genre

############# Task 6 #############

print(df.groupby("Publisher ")["units sold"].sum().idxmax(),end="  ") # returns the max unit sold by a publisher
print (df.groupby("Publisher ")["units sold"].sum().max())

############# Task 7 #############
co = df[["gross sales","publisher revenue"]].corr() # coorelation between grosss sales and publisher revenue
sns.heatmap(co, annot= True)
plt.show()

co = df["gross sales"].corr(df["publisher revenue"])
print (co)

############ Task 8 #############

print(df[df["Publishing Year"] > 0].sort_values("Publishing Year", ascending=True)) # show only valid publishing years greater than 0, then sort from smallest to largest

############# Task 9 (Round 2) #############

cols = ["Book Name", "language_code", "Publishing Year"]
print(df[cols].isnull().sum())

df[cols] = df[cols].fillna({
    "Book Name": "N/A",
    "language_code": "N/A",
    "Publishing Year": df["Publishing Year"].mode
})

print(df[cols].isnull().sum())


############# Task 10 (Round 2) #############

from sklearn.preprocessing import OneHotEncoder
import numpy as np

x = df["genre"].unique()
X = np.array(x.reshape(-1,1)) # .reshape(1, -1)   # one row, many columns
                              # .reshape(-1, 1)   # many rows, one column
                              # .reshape(3, 2)    # 3 rows, 2 columns
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X).toarray()
print(X_encoded)

############# Task 11 (Round 2) #############

from sklearn.preprocessing import LabelEncoder
import numpy as np

values = ["Novice", "Intermediate", "Excellent", "Famous"]

mapping = {
    "Novice": 3,
    "Intermediate": 2,
    "Excellent": 1,
    "Famous": 0
}

encoded = [mapping[v] for v in values]
le = LabelEncoder()
encoded = le.fit_transform(encoded)

for value, code in zip(values, encoded):
    print(value, "->", code)


########### version 2 of (11) ###########

ratings = df["Author_Rating"].dropna().unique()
mapping = {
    "Novice": 0,
    "Intermediate": 1,
    "Excellent": 2,
    "Famous": 3
}


encoded = [mapping[v] for v in ratings]
print (mapping)

for value, code in zip(ratings, encoded):
    print(value, "->", code)

############# Task 12 (Round 2) #############

resultskew = df["gross sales"].skew()
print (resultskew)

finalresult = np.log(resultskew)
print (finalresult)

############# Task 13 (Round 2) #############

from sklearn.preprocessing import StandardScaler

vals = df["units sold"]
vals = np.array(vals).reshape(-1,1)
standard = StandardScaler().fit_transform(vals).flatten()
print (standard)
print (f"Transformed mean is: {round(standard.mean(),)}")