# import yfinance as yf
#
# print(yf.__version__)  # should print 1.1.0
#
# data = yf.download("AAPL", period="5d")
# print(data.head())  # prints the last 5 days of Apple stock prices


"""
Here are the key functionalities of your Stock Market Data Explorer with regression-based prediction:
1. Load Data - Download historical stock data (10 years up to yesterday) from Yahoo Finance.
2. Clean Data - Handle missing values, format dates, adjust for splits/dividends.
3. Compute Statistics - Mean, median, min/max, daily returns, volume analysis, detect outliers.
            : percentage change over given timeframe
            volatility-standard deviaiton
            moving averages
            max drawdown
            price range
4. Visualize Data - Line charts (price trends), bar charts (volume), scatter plots (returns vs volume).
5. Generate Reports - Text summaries of key stats and trends.
6. Multi-Ticker Support - Analyze multiple stocks simultaneously.
7. Future Price Prediction - Forecast next-day/next-week prices using regression models (Linear
Regression, Random Forest, etc.).
8. Prediction Visualization - Plot predicted vs actual stock prices.
9. Optional Interactive Exploration - Filter by date range, ticker, or metrics.

"""

import yfinance as yf
import pandas as pd

# data = yf.download("WMT", start="2022-01-01", end="2024-01-01", auto_adjust=False,progress=False)
# data.to_csv("tesla_data.csv")
# new_data = pd.read_csv("tesla_data.csv")
# new_data.head()
# print(new_data.head())
# print(new_data.columns)

def get_stock_information(ticker):
    ticker_dict = {
        "AAPL" : "Apple",
        "WMT":"Walmart",
        "AMZN"  : "Amazon",
        "UNH" : "UnitedHealth Group",
        "CVS": "CVS Health",
        "XOM": "ExxonMobil",
        "GOOGL": "Alphabet(Google)",
        "MCK": "McKesson",
        "CVX": "Chevron",
    }
    ticker_list = list(ticker_dict.keys())
    if ticker not in ticker_dict:
        print("Sticker not found")
        raise ValueError("Ticker not in list")

    else:

        data = yf.download(ticker , start="2022-01-01", end="2024-01-01", auto_adjust=False,progress=False)
        data.to_csv(f"{ticker}.csv")
        stck_data = data
        print(stck_data.head())
        return stck_data

#get_stock_information("AAPL")
def data_cleaning(df):
    df = df.reset_index()
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    df = df.dropna(subset = ["Open","High","Close","Low"])
    df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]] = \
        df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]].apply(pd.to_numeric)
    df = df.sort_values("Date")
    return df




# data = yf.download("AAPL" , start="2012-01-01", end="2025-01-01", auto_adjust=False,progress=False)
# data.to_csv("AAPL.csv")
# pd.set_option('display.max_rows', None)
# stck_data = data
# print(stck_data)

def updated_stck_data(df):
    df["Daily range"] = df["Close"]-df["Open"]
    df["Daily return"] = df["Adj Close"].pct_change()
    df["Volatility"] = df["Daily return"].rolling(50).std()
    df["Moving average"] = df["Adj Close"].rolling(50).mean()
    max_draw = df.sort_values("Date")
    running_peak = df["Adj Close"].cummax()
    df["Drawdown"] = running_peak - df["Adj Close"]
    df["Max Drawdown"] = df["Drawdown"].max()
    return df


stck_data = get_stock_information("AAPL")
cleaned_data = data_cleaning(stck_data)
updated_data = updated_stck_data(cleaned_data)

print("-------------new_df---------")
pd.set_option("display.max_columns",None)
print(updated_data.head())
