import pandas as pd

print("Starting preprocessing...")

df = pd.read_csv("data/stock_data.csv", index_col=0, parse_dates=True)

df.columns = ["open", "high", "low", "close", "volume"]

df["daily_return"] = df["close"].pct_change()
df["ma_5"] = df["close"].rolling(5).mean()
df["ma_10"] = df["close"].rolling(10).mean()
df["high_low_diff"] = df["high"] - df["low"]
df["prev_close"] = df["close"].shift(1)

df["target"] = df["close"].shift(-1)

df.dropna(inplace=True)

df.to_csv("data/processed_stock_data.csv")

print("Preprocessing completed.")
