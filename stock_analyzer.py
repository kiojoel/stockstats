import yfinance as yf
import sys

stock_ticker = input("Please enter a stock ticker: ").upper()

start_date = '2023-01-01'
end_date = '2023-12-31'

stock_data = yf.download(stock_ticker,start=start_date, end=end_date, progress=False)

if stock_data.empty:
    print(f"Error: No data found for ticker '{stock_ticker}'.")
    print("Please check the ticker symbol and your internet connection.")
    sys.exit()


highest_price = stock_data['High'].max().iloc[0]
avg_close_price = stock_data['Close'].mean().iloc[0]
total_volume = stock_data['Volume'].sum().iloc[0]

print("\nStock Analysis ")
print(f"Highest Price:         ${highest_price:.2f}")
print(f"Average Closing Price: ${avg_close_price:.2f}")
print(f"Total Volume Traded:   {total_volume:,}")