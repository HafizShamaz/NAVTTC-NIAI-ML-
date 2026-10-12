"""Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008."""


import pandas as pd
import matplotlib.pyplot as plt

##########################################
# Introduction to Pandas & Creating a Dataframe
##########################################

mydataset = {
  'name': ["Ali", "Sara", "Zain"],
  'passings': [85, 92, 78]
}

df = pd.DataFrame(mydataset)
print (df)
print (pd.__version__) # display pandas installed version

############ practice examples ###########

mydataset = {
  'name': ["Ali", "Sara", "Zain","Shamaz"],
  'city': ["Lahore","Karachi", "Islamabad","Lahore"],
  'score': [85,92,78,99],
  'any':["","","",""]
}

df = pd.DataFrame(mydataset)
print ("Total nbumber of rows and coloumns are:",len(df),"\n",df)

##########################################
# series vs DataFrame
##########################################

s = pd.Series([10,20,30], index=["a","b","c"])
print(s)

df = pd.DataFrame(
    {
    "name": ["Ali","Sara"],
    "marks":[85,92]
    }
)

print(df["name"]) # a series


############ practice examples ###########

s = pd.Series(["Lahore","Karachi","Peshawar","Rawalpindi","Skardu"], index=["c1","c2","c3","c4","c5"])
print(s)

df = pd.DataFrame(
    {
    "name": ["Ali","Sara"],
    "marks":[85,92]
    }
)

print("\n",df,"\n and the data type of name is", type (df["name"])) # a series

##########################################
# Selection & Indexing
##########################################

df = pd.DataFrame(
    {
    "name": ["Ali","Sara"],
    "marks":[85,92]
    }
)

print (df[df["marks"] > 80])

############ practice examples ###########

df = pd.DataFrame (
    {
    "name": ["Ali","Sara","Shamaz","Mateen","Arslan"],
    "marks":[85,92,99,56,78]
    }
)

print (df[df["marks"] > 75])
print (df[["name","marks"]])

##########################################
# DataFrame Operations (sort,unique,apply)
##########################################

df = pd.DataFrame (
    {
    "name": ["Ali","Sara","Shamaz","Mateen","Arslan"],
    "marks":[85,92,99,56,78]
    }
)

df["grade"] = df ["marks"].apply(
    lambda x: "pass" if x >= 80 else "Fail"
)
print(df.sort_values("marks", ascending = False))

############ practice examples ###########

df = pd.DataFrame (
    {
    "name": ["Ali","Sara","Shamaz","Mateen","Arslan"],
    "marks":[85,92,99,56,78]
    }
)

df["grade"] = df ["marks"].apply(
    lambda x: "High" if x >= 80 else "Low"
)

print(df)
print(df.value_counts("grade"))

########### *Self Practice* #############

df = pd.read_csv("iris.csv")
df = pd.read_csv("iris.csv")
print (df)

df["new_col"] = df ["petal.width"].apply(
    lambda x: "High" if x >= 1.2 else "Low"
)

# print (df)
print(df.value_counts("new_col"))


##########################################
# Handling Missing Data
##########################################

df = pd.DataFrame(
    {
        "a": [1,2,None],
        "b":[4,None,6]
    }
    )

print (df.isnull())
# print(df.fillna(0))
print(df.fillna(df.median))

############ practice examples ###########

df = pd.DataFrame(
    {
        "a": [None,3,2,None],
        "b":[4,None,None,6]
    }
    )

print (df.isnull())
print(df.fillna(0))
print(df.dropna())

##########################################
# GroupBy
##########################################

sales = pd.DataFrame({
    "dept":["IT","IT","HR","HR"],
    "sales":[100,150,80,90]
})

print (sales.groupby("dept")["sales"].sum())

########### practice examples ###########

sales = pd.DataFrame({
    "category":["Kitchen","Cleanliness","Beverages","Footwear"],
    "price":[100,150,300,150]
})
print (sales.groupby("category")["price"].count())

##########################################
# Merging & Concatenation
##########################################

a = pd.DataFrame({
    "id":[1,2,3],
    "name":["Ali","Sara","Zain"]
})

b = pd.DataFrame({
    "id":[1,2,4],
    "marks":[85,92,70]
})

print (pd.merge(a,b, on="id", how="inner"))

############ practice examples ###########

a = pd.DataFrame({
    "id":[1,2,3],
    "name":["Ali","Sara","Zain"]
})

b = pd.DataFrame({
    "id":[1,2,4],
    "marks":[85,92,70]
})

# print (pd.merge(a,b, on="id", how="left"))
concat_df = pd.concat([a,b])
print (concat_df)

##########################################
# Pandas Plotting (Quick Charts)
##########################################

df = pd.DataFrame({
    "dept":["IT","HR","Sales"],
    "revenue":[250,170,300]
})

df.plot(x="dept", y="revenue", kind = "bar")
plt.show()


############ practice examples ###########

df = pd.DataFrame({
    "dept":["IT","HR","Sales"],
    "sales":[25000,1700,300000]
})

df.plot(x="dept", y="sales", kind = "line")
plt.show()


df.plot(x="dept", y="sales", kind = "bar")
plt.show()
