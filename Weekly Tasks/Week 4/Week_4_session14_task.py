##########################################
# feature Engineering - creating New features
##########################################
import pandas as pd

df = pd.DataFrame({
    "height_cm": [170,180,160],
    "weight_kg": [65,80,55]
})

df ["bmi"] = df ["weight_kg"] / (df["height_cm"]/100) **2
print (f"{round((df),2)}")

############ practice examples ###########

df = pd.DataFrame({
    "price": [170,180,160],
    "quantity": [5,8,25]
})

df ["total_cost"] = df ["price"] * df["quantity"]
print (f"{round((df),2)}")


df = pd.DataFrame({
    "total_income": [170000,180000,160000],
    "total_expanse": [17000,80000,25000]
})

df ["savings_rate"] = df ["total_income"] - df["total_expanse"]
df ["savings_rate"] = df ["savings_rate"] / df ["total_income"]*100
print (f"{round((df),2)}")

##########################################
# Feature Selection & Bining
##########################################

df = pd.DataFrame({
    "study_hrs": [1,2,3,4,5],
    "sleep_hrs": [8,7,6,8,7], 
    "marks": [50,50,65,70,85]
})

print (df.corr()["marks"])

ages = pd.Series ([5,17,25,45,68,80])
print (pd.cut(ages, bins = [0,12,19,59,100], labels= ["Child","Teen","Adult","Senior"]))

############ practice examples ###########

df = pd.DataFrame({
    "Sales": [100,200,300,400,500],
    "quantities": [8,7,6,8,7], 
    "price": [500,1000,605,7000,850]
})

print (df.corr()["price"])

exam_score = pd.Series ([50,8,90,44,30,21,51])
print (pd.cut(exam_score, bins = [0,33,50,100], labels= ["fail","pass","Merit"]))

##########################################
# ETL & Batch vs Stream Processing
##########################################

# ETL example - Conceptual
# Extract: read raw sales data from a CSV/database

raw = pd.read_csv ("daily_sales.csv")

# Transform: Clean and engineer features

clean = raw.dropna().assign()(
    revenue = raw["price"] * raw ["qty"]
)

# Load: Save the processed result
clean.to_csv ("processed_sales.csv", index = False)


#OLTP , OLAP (Data field lies on these 2 concepts)

##########################################
# Automation with sklearn Pipeline
##########################################

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib as plt

# Data - Study hours vs exam score

X = np.array ([[1],[2],[3],[4],[5],[6],[7],[8]]) # study hours
y = np.array([40,45,52,60,68,75,82,90]) # exam score

pipe = Pipeline ([
    ("scalar", StandardScaler()),
    ("model", LinearRegression())
    ]
)

pipe.fit(X,y)
print(pipe.predict([[9]]))


