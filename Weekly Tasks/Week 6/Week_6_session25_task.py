##########################################
# Time Series
##########################################

import pandas as pd

# # 1. Load and tell pandas the data column is a date not text
# df = pd.read_csv(r'C:\Users\HP ZBOOK\Desktop\NIAI-NAVTTC-CohorotII(AI-ML)\Course Material\Datasets\shop_sales_daily.csv', parse_dates=['date'])
# print (df.head(3))
# print("From", df["date"].min().date(), "to", df["date"].max().date(), "|", len(df), "days")

# # 2. Pull useful parts out of each date
# df["daysofweek"] = df["date"].dt.dayofweek # 0 = Monday, 6 = Sunday
# df["month"] = df["date"].dt.month

# # 3. Look for patterns in the data
# print ("Average sales by day of week:")
# print(df.groupby("daysofweek")["sales"].mean().round())
# print("\nAverage sales by years:")
# print(df.groupby(df["date"].dt.year)["sales"].mean().round())  

# ##########################################
# # Lag features, time split & baselines
# ##########################################

import pandas as pd
from sklearn.metrics import mean_absolute_error

df = pd.read_csv(r'C:\Users\HP ZBOOK\Desktop\NIAI-NAVTTC-CohorotII(AI-ML)\Course Material\Datasets\shop_sales_daily.csv', parse_dates=['date'])

# Lag features = the past becomes the input
df['lag_1'] = df['sales'].shift(1)                       # yesterday
df['lag_7'] = df['sales'].shift(7)                       # same day last week
df['roll_7'] = df['sales'].shift(1).rolling(7).mean()    # last 7 days average
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df = df.dropna()                                         # first 7 days have no history

# Split by TIME, never randomly
train = df[df['date'] < '2025-10-01']
test = df[df['date'] >= '2025-10-01']
print('Train days:', len(train), '| Test days:', len(test))

# Baselines: simple guesses every model must beat
for name, col in [('Naive (yesterday)', 'lag_1'), ('7-day average', 'roll_7'),
                  ('Seasonal naive (lag 7)', 'lag_7')]:
    print(f'{name:24s} MAE: {mean_absolute_error(test["sales"], test[col]):.1f}')

##########################################
# Train & compare forecasting models
##########################################

# (continues from Code 2: df, train and test already built)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

features = ['lag_1', 'lag_7', 'roll_7', 'dayofweek', 'month']
X_train, y_train = train[features], train['sales']
X_test, y_test = test[features], test['sales']

for name, model in [('Linear Regression', LinearRegression()),
                    ('Random Forest', RandomForestRegressor(300, random_state=42))]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(f'{name:18s} MAE: {mean_absolute_error(y_test, pred):.1f}')

# Which past value helped the most?
rf = RandomForestRegressor(300, random_state=42).fit(X_train, y_train)
print(pd.Series(rf.feature_importances_, index=features).round(2))


##########################################
# Plot the Forecast vs Actual
##########################################

import matplotlib.pyplot as plt
lr = LinearRegression().fit(X_train, y_train)
plt.figure(figsize=(12, 4))
plt.plot(test['date'], y_test, label='Actual', color='black')
plt.plot(test['date'], lr.predict(X_test), label='Forecast', color='orange')
plt.legend(); plt.title('Forecast vs actual (Oct–Dec 2025)'); plt.show()