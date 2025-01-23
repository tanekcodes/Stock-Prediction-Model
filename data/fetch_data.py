import yfinance as yf

# Fetch historical data for a specific stock
def get_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv("data/stock_data.csv")  # Save to your data directory
    print("Data saved to data/stock_data.csv")

# Example usage
get_stock_data('AAPL', '2015-01-01', '2023-12-31')
