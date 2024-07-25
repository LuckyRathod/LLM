# filename: generate_stock_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

# Ensure the file is saved in the local directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Defining the time period
start_date = '2024-01-01'
end_date = '2024-07-25'

# Fetching the stock data using yfinance
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
tsla_data = yf.download('TSLA', start=start_date, end=end_date)

# Calculating YTD gains
nvda_ytd = (nvda_data['Adj Close'] - nvda_data['Adj Close'].iloc[0]) / nvda_data['Adj Close'].iloc[0] * 100
tsla_ytd = (tsla_data['Adj Close'] - tsla_data['Adj Close'].iloc[0]) / tsla_data['Adj Close'].iloc[0] * 100

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(nvda_ytd.index, nvda_ytd.values, label='NVDA YTD Gain %')
plt.plot(tsla_ytd.index, tsla_ytd.values, label='TSLA YTD Gain %')
plt.title('YTD Stock Gains for NVDA and TSLA as of 2024-07-25')
plt.xlabel('Date')
plt.ylabel('Gain %')
plt.legend(loc='upper left')
plt.grid(True)

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.show()