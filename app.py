import yfinance as yf

# Define the ticker symbol
ticker_symbol = 'COIN'  # Replace with your desired ticker

# Define the start and end dates
start_date = '2024-05-23'
end_date = '2025-05-23'

# Download the data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save to CSV
data.to_csv(f'{ticker_symbol}_historical_data.csv')
