import requests
import pandas as pd
from config import API_KEY, SYMBOL

url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": SYMBOL,
    "apikey": API_KEY,
    "outputsize": "compact"
}

response = requests.get(url, params=params)
data = response.json()

time_series = data["Time Series (Daily)"]

df = pd.DataFrame.from_dict(time_series, orient="index")
df = df.astype(float)
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)

df.to_csv("data/stock_data.csv")

print("Data saved successfully!")
