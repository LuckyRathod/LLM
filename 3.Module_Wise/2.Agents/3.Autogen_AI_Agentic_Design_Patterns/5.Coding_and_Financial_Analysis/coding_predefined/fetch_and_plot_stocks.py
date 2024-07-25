# filename: fetch_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices
import pandas as pd
from datetime import datetime

# Get today's date as string
today_date = "2024-07-25"

# Start date for Year-To-Date (from January 1st of current year)
start_date = "2024-01-01"

# Stock symbols for which to get the prices
stock_symbols = ["NVDA", "TSLA"]

# Fetch stock prices YTD
stock_prices = get_stock_prices(stock_symbols, start_date, today_date)

# Plot the stock prices and save to file
plot_stock_prices(stock_prices, "stock_prices_YTD_plot.png")

print("Stock prices downloaded and plot saved.")