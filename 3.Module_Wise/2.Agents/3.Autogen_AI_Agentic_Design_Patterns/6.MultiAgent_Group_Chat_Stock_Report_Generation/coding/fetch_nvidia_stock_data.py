# filename: fetch_nvidia_stock_data.py
import yfinance as yf
import datetime

# Define the stock symbol and the timeframe you need data for
stock_symbol = "NVDA"
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)  # Data from approximately one month ago

# Fetch historical market data
nvidia_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the data
print(nvidia_data)