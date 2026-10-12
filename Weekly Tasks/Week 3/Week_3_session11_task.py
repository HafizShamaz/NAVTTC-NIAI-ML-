import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# # Load the tips dataset into a pandas DataFrame
df = sns.load_dataset("tips")

# Display the first few rows
print(df.head())
print (df["day"].value_counts(['Friday','Saturday','Sunday']))


#######################################
# Task 1 (Look at the Dataset of Tips)
#######################################

print (df.shape)
print (df.head())
print(df.tail())
print (df.dtypes)

#######################################
# Task 2 (Summary Statistics)
#######################################
print (df.describe())

#######################################
# Task 3 (Univariate: Count Categories)
#######################################

print (df["day"].value_counts())

#######################################
# Task 4 (Histogram task on Total_bill)
#######################################

sns.histplot(data=df, x="total_bill", bins=10)
plt.title("Distribution of Total Bills")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

sns.histplot(df["total_bill"])
plt.show()

#######################################
# Task 5 (Bivariate: Compare a Number Across Categories)
#######################################

temp = df.groupby("day")["total_bill"].mean()
highest_day = temp.idxmax()
highest_mean = temp.max()
print("Highest average bill comes on:", highest_day)
print("Highest mean total bill is", highest_mean)

#######################################
# Task 6 (Bivariate: (Visualize a Relationship))
#######################################

sns.scatterplot(x="total_bill", y="tip", data = df)
plt.show()

#######################################
# Task 7 (Multivariate: (Coorelation Heatmap))
#######################################

temp = df[["total_bill","tip","size"]].corr()
sns.heatmap(temp, annot= True)
plt.show()

#######################################
# Task 8 (Write Your EDA Summary)
#######################################

# 1: Univariate Finding
# 2: Bivariate Finding
# 3: Multivariate Finding

"""1. Saturday is the busiest day (87 records).
2. Weekend bills average higher (~$20-21)
   than weekdays (~$17).
3. total_bill and tip are strongly correlated
   (0.68) — bigger bills get bigger tips."""



