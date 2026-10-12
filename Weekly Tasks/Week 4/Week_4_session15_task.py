import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load the house dataset from the CSV file.
df = pd.read_csv("House Price Prediction Dataset.csv")

# Select Area as the input feature and Price as the value to predict.
X = df[["Area"]]
y = df["Price"]

# Keep 80% of the data for learning and 20% for testing the model.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train scikit-learn's linear regression model.
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate the average Area and average Price from the training data.
area_mean = X_train["Area"].mean()
price_mean = y_train.mean()

# Calculate how far each value is from its corresponding average.
deviation_area = X_train["Area"] - area_mean
deviation_price = y_train - price_mean

# Calculate the two totals used in the manual slope formula.
sum_of_products = (deviation_area * deviation_price).sum()
sum_of_area_squares = (deviation_area ** 2).sum()

# Calculate slope and intercept using: m = sum((X-Xmean)(Y-Ymean)) / sum((X-Xmean)^2).
manual_slope = sum_of_products / sum_of_area_squares

# Calculate the intercept using: c = Ymean - (m * Xmean).
manual_intercept = price_mean - (manual_slope * area_mean)

# Apply the regression equation: predicted Price = (slope * Area) + intercept.
manual_predictions = manual_slope * X_test["Area"] + manual_intercept

# Generate predictions using the scikit-learn model for comparison.
predictions = model.predict(X_test)

# Display the manual and library model coefficients and evaluation scores.
print("Manual slope:", manual_slope)
print("Manual intercept:", manual_intercept)
print("Library slope:", model.coef_[0])
print("Library intercept:", model.intercept_)
print("Manual MAE:", mean_absolute_error(y_test, manual_predictions))
print("Manual RMSE:", mean_squared_error(y_test, manual_predictions) ** 0.5)
print("Manual R² score:", r2_score(y_test, manual_predictions))

# Ask the user for a new area and predict its price.
user_area = float(input("Enter house area in square feet: "))
user_input = pd.DataFrame({"Area": [user_area]})

# Predict the new price using the manual formula.
# user_manual_prediction = manual_slope * user_area + manual_intercept

# Predict the same new price using the trained scikit-learn model.
user_model_prediction = model.predict(user_input)[0]

# print("Manual predicted price:", user_manual_prediction)
print("Model predicted price:", user_model_prediction)

# Combine test areas, actual prices, and predictions for an ordered plot.

plot_data = pd.DataFrame({
    "Area": X_test["Area"].to_numpy(),
    "Actual Price": y_test.to_numpy(),
    "Predicted Price": manual_predictions.to_numpy()
}).sort_values("Area")

# Plot the actual test prices as blue points.
plt.scatter(plot_data["Area"], plot_data["Actual Price"],
            color="blue", alpha=0.5, label="Actual prices")

# Plot the manual regression predictions as a red line.
plt.plot(plot_data["Area"], plot_data["Predicted Price"],
         color="red", linewidth=2, label="Regression line")

# Add labels, a title, a legend, and display the graph.
plt.xlabel("Area (square feet)")
plt.ylabel("Price")
plt.title("Area vs Price Linear Regression")
plt.legend()
plt.show()