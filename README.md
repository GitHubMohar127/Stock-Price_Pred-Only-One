# 📈 Real-Time Stock Price Prediction Using Daily API Data

## 1. Project Overview

This project builds an **end-to-end machine learning pipeline** that:

* Fetches **real-time stock market data** daily from an external API
* Stores and updates the dataset automatically
* Performs feature engineering on time-series data
* Trains a **Random Forest regression model**
* Predicts the **next day’s closing stock price**

The data changes every day, and the model can be retrained daily, making this a **real-world ML system**, not a static demo project.

---

## 2. Tech Stack

* **Language:** Python 3.x
* **Data Handling:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **API:** Alpha Vantage (Stock Market API)
* **Model Storage:** joblib

---

## 3. Project Structure

```
STOCK PRICE PREDICTION/
│
├── data/
│   ├── stock_data.csv              # Raw daily stock data from API
│   └── processed_stock_data.csv    # Feature-engineered ML dataset
│
├── notebooks/
│   ├── preprocessing.ipynb         # Data preprocessing (exploration)
│   └── train_ML.ipynb               # Model training (exploration)
│
├── fetch_data.py                    # API data fetch script
├── preprocessing.py                 # Production preprocessing script
├── train_ML.py                      # Production ML training script
├── run_daily_pipeline.py            # End-to-end automation pipeline
├── config.py                        # API key & stock symbol config
├── stock_price_model.pkl            # Trained ML model
└── README.md
```

---

## 4. How to Get the API Key (Step-by-Step)

We use **Alpha Vantage**, a free and reliable stock market API.

### Step 1: Create an Alpha Vantage account

1. Go to: [https://www.alphavantage.co](https://www.alphavantage.co)
2. Click **Get Free API Key**
3. Sign up using your email
4. Verify your email

You will receive a **free API key** (example: `ABCD1234XYZ`).

---

### Step 2: Add API key to the project

Open `config.py` and update it as shown below:

```python
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
SYMBOL = "AAPL"  # Example: AAPL, TSLA, MSFT, INFY
```

📌 Notes:

* `SYMBOL` can be changed to any valid stock ticker
* Indian stocks work depending on Alpha Vantage support

---

## 5. API Data Details (What Data We Fetch)

The API endpoint used:

* **Function:** `TIME_SERIES_DAILY`
* **Frequency:** Daily stock prices

### Raw API Fields

Each trading day provides:

| Column | Description              |
| ------ | ------------------------ |
| open   | Opening price            |
| high   | Highest price of the day |
| low    | Lowest price of the day  |
| close  | Closing price            |
| volume | Total traded volume      |

This raw data is saved as:

```
data/stock_data.csv
```

---

## 6. Data Preprocessing & Feature Engineering

From the raw data, we generate ML-friendly features.

### Engineered Features

| Feature       | Description                           |
| ------------- | ------------------------------------- |
| daily_return  | Percentage change from previous close |
| ma_5          | 5-day moving average                  |
| ma_10         | 10-day moving average                 |
| high_low_diff | Daily price range                     |
| prev_close    | Previous day’s closing price          |

### Target Variable

```
Target = Next day closing price
```

Processed data is stored as:

```
data/processed_stock_data.csv
```

---

## 7. Machine Learning Model

* **Model Used:** Random Forest Regressor
* **Why Random Forest?**

  * Handles non-linearity well
  * Works well on tabular financial data
  * Less sensitive to noise

### Training Strategy

* Time-based split (80% train, 20% test)
* No random shuffling (important for time series)

### Evaluation Metric

* **RMSE (Root Mean Squared Error)**

---

## 8. Automation Pipeline

The entire workflow is automated using:

```
run_daily_pipeline.py
```

### Pipeline Steps

1. Fetch latest stock data from API
2. Update the dataset
3. Preprocess data & create features
4. Train ML model
5. Save model & predict tomorrow’s price

Run with:

```bash
python run_daily_pipeline.py
```

---

## 9. How This Project Is Used in Real Life

This project simulates:

* Real-time data ingestion
* Daily ML retraining
* Time-series prediction systems

Similar pipelines are used in:

* Algorithmic trading
* Financial forecasting
* Business analytics
* ML engineering roles

---

## 10. Future Improvements

* Convert to **price direction prediction (up/down)**
* Add **LSTM / deep learning**
* Create a **Streamlit dashboard**
* Deploy using **Docker**


