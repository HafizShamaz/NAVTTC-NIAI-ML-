##########################################
# Data Cleaning (Duplicates & Outliers)
##########################################
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
    'name': ["Ali","Ahsan","Ali"],
    "marks": [85,92,85]
    }
    )

print (df.duplicated())
print(df.drop_duplicates())

############ practice examples ###########

df = pd.DataFrame(
    {
    'department': ["IT","HR","IT"],
    "sales": [85000,92000,85000]
    }
    )

print (df.duplicated())
print(df.drop_duplicates())

prices = pd.range .Series ()
log_prices = np.log(prices)
print (log_prices)

##########################################
# Data Transformation
##########################################

prices = pd.Series ([100,500,1000,50000])
log_prices = np.log(prices)
print (log_prices)



prices = pd.Series ([100,500,1000,50000])
log_prices = np.log(prices)
print (log_prices)

########### practice examples ###########

prices = pd.Series ([10000,500,10,50000,100000,20000])
log_prices = np.log(prices)
print (log_prices)


##########################################
# Encoding Categorical Variables
##########################################

import pandas 
from sklearn.preprocessing import LabelEncoder

sizes = ["small", "Medium", "Large", "Medium"]
le = LabelEncoder()
print (le.fit_transform(sizes))

sizes = ["Red", "Yellow", "Blue", "red"]
le = LabelEncoder()
print (le.fit_transform(sizes))


##########################################
# Feature Scaling (Standard & MinMax)
##########################################

from sklearn.preprocessing import StandardScaler, MinMaxScaler

vals = np.array ([[10],[20],[30],[40],[50]])

# print (StandardScaler().fit_transform(vals).flatten())

print(MinMaxScaler().fit_transform(vals).flatten())


############ practice examples ###########

# Example data
X = np.array([
    [10, 1000],
    [20, 2000],
    [30, 3000],
    [40, 4000]
])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Original data:")
print(X)

print("\nScaled data:")
print(X_scaled)