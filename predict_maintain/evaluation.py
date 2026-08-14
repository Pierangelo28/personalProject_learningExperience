
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("PM_train.csv")
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
"""check number of missing values"""
# print(df.isnull().sum())
print(df.describe())

"""
perform datacleaning 
identify relevant modules or columns to their relevant faults 
    identified based on the colums df.columns
have different functions prediting maintenance for different faults

"""
df["RUL"] = df.groupby("id")['cycle'].transform('max') - df['cycle']
df.insert(2,'RUL',df.pop('RUL'))
print(df.columns)
# print(df.head())
df = df.dropna()
df = df.sort_values(["id", "cycle"])

LNR = LinearRegression()
X = df[['cycle','setting1', 'setting2', 'setting3', 's1', 's2', 's3', 's4',
       's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15',
       's16', 's17', 's18', 's19', 's20', 's21']]
y = df["RUL"]

LNR = LNR.fit(X,y)

testing = pd.read_csv ('PM_test.csv')

x_test = testing[['cycle','setting1', 'setting2', 'setting3', 's1', 's2', 's3', 's4',
                  's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
                  's15', 's16', 's17', 's18', 's19', 's20', 's21']]
y_pred = LNR.predict(x_test)

print(y_pred)
testing['Predicted_RUL'] = y_pred
last_rows = testing.groupby("id").tail(1)
print(last_rows[["id", "cycle", "Predicted_RUL"]])

# Load actual RUL values
truth = pd.read_csv("PM_truth.csv")

# Rename cycle column to Actual_RUL
truth = truth.rename(columns={"cycle": "Actual_RUL"})

# Add actual RUL to the prediction table
last_rows["Actual_RUL"] = truth["Actual_RUL"].values

# Evaluation metrics
mae = mean_absolute_error(last_rows["Actual_RUL"], last_rows["Predicted_RUL"])
mse = mean_squared_error(last_rows["Actual_RUL"], last_rows["Predicted_RUL"])
rmse = np.sqrt(mse)
r2 = r2_score(last_rows["Actual_RUL"], last_rows["Predicted_RUL"])

print("\nModel Evaluation")
print("----------------")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)

# Compare predictions with actual values
print("\nPredictions vs Actual:")
print(last_rows[["id", "Predicted_RUL", "Actual_RUL"]])