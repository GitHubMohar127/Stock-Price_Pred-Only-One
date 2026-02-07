import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

print("Training model...")

df = pd.read_csv("data/processed_stock_data.csv", index_col=0, parse_dates=True)

X = df.drop(columns=["target"])
y = df["target"]

split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("RMSE:", rmse)

joblib.dump(model, "stock_price_model.pkl")

tomorrow = model.predict(X.iloc[-1:].values)[0]
print("Tomorrow's predicted close:", tomorrow)

print("Training completed.")
