#Created on Tue Jan 21 00:21:40 2025

#@author: Deepak Dalal


# Import necessary libraries
import numpy as np
import pandas as pd
import datetime as dt 
import yfinance as yf
from scipy.stats import norm
import os

# Define the date range for stock data
end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=10000)

# List of stocks to analyze
stocks = ['ABB.NS', 'ADANIENSOL.NS', 'ADANIENT.NS', 'ADANIGREEN.NS', 'ADANIPORTS.NS']

# Loop through each stock and calculate its range
for stock in stocks:
    # Download monthly and daily stock data
    monthly_data = yf.download(stock, start=start_date, end=end_date, interval="1mo")

    # Calculate daily returns
    monthly_data["Daily_return"] = monthly_data["Adj Close"].pct_change()

    # Calculate mean and standard deviation of daily returns
    stock_mean = monthly_data["Daily_return"].mean()
    stock_std = monthly_data["Daily_return"].std()

    # Calculate the stock's 65% and 95% confidence intervals
    range_65_lower = stock_mean - stock_std
    range_65_upper = stock_mean + stock_std

    true_range_65_lower = ((monthly_data["Adj Close"].iloc[-1]) * (1 + range_65_lower)).round(2)
    true_range_65_upper = ((monthly_data["Adj Close"].iloc[-1]) * (1 + range_65_upper)).round(2)

    range_95_lower = stock_mean - 2 * stock_std
    range_95_upper = stock_mean + 2 * stock_std

    true_range_95_lower = ((monthly_data["Adj Close"].iloc[-1]) * (1 + range_95_lower)).round(2)
    true_range_95_upper = ((monthly_data["Adj Close"].iloc[-1]) * (1 + range_95_upper)).round(2)

    # Print results
    print("------------------------------")
    print("65% chance stock will remain in this range:")
    print(f"{stock} will remain in {true_range_65_lower} -- {true_range_65_upper}")

    print("95% chance stock will remain in this range:")
    print(f"{stock} will remain in {true_range_95_lower} -- {true_range_95_upper}")