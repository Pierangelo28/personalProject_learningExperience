
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
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
RFR = RandomForestRegressor(n_estimators=500,random_state=42,oob_score=True)
X = df[['cycle','setting1', 'setting2', 'setting3', 's1', 's2', 's3', 's4',
       's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15',
       's16', 's17', 's18', 's19', 's20', 's21']]
y = df["RUL"]

LNR = LNR.fit(X,y)
RFR = RFR.fit(X,y)

testing = pd.read_csv ('PM_test.csv')

x_test = testing[['cycle','setting1', 'setting2', 'setting3', 's1', 's2', 's3', 's4',
                  's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
                  's15', 's16', 's17', 's18', 's19', 's20', 's21']]
y_pred = RFR.predict(x_test)
y_pred_2 = LNR.predict(x_test)

# print(y_pred)
testing['RUL_Forest'] = y_pred
testing['RUL_Linear'] = y_pred_2
last_rows = testing.groupby("id").tail(1)
print(last_rows[["id", "cycle", "RUL_Forest",'RUL_Linear']])

# Load the true RUL values for each test engine
true_rul = pd.read_csv(
    "PM_truth.csv",
    
)

# The test dataset contains multiple cycles for each engine.
# The final cycle represents the point at which we make our prediction.
last_rows = testing.groupby("id").tail(1).reset_index(drop=True)

# True RUL for each engine at its final observed cycle
y_test = true_rul["cycle"]

# Random Forest predictions
y_pred_forest = last_rows["RUL_Forest"]

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred_forest)
mse = mean_squared_error(y_test, y_pred_forest)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_forest)

print("\nRandom Forest Model Evaluation")
print("------------------------------")
print(f"MAE:  {mae:.2f}")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")
