import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data for a given ticker."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if data.empty:
            print("No data found for the given ticker and date range.")
        else:
            print(f"Data fetched for {ticker}.")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Function to plot stock price trends
def plot_stock_data(data, ticker):
    """Plot stock price trends."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
    plt.title(f"{ticker} Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

# Function to calculate and plot moving averages
def plot_moving_averages(data, ticker, window=20):
    """Plot moving averages for the stock."""
    data[f"MA_{window}"] = data['Close'].rolling(window=window).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
    plt.plot(data.index, data[f"MA_{window}"], label=f"{window}-Day Moving Average", color='orange')
    plt.title(f"{ticker} {window}-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

# Function to calculate daily returns
def calculate_daily_returns(data):
    """Calculate and return daily percentage changes."""
    data['Daily Returns'] = data['Close'].pct_change() * 100
    print("\nDaily Returns:")
    print(data[['Close', 'Daily Returns']].head())

# Main Program
def main():
    print("Welcome to the Stock Market Analysis Tool!")
    
    ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    if stock_data is not None and not stock_data.empty:
        # Display fetched data
        print(stock_data.head())

        # Menu for analysis
        while True:
            print("\nAnalysis Options:")
            print("1. Plot stock price trends")
            print("2. Plot moving averages")
            print("3. Calculate daily returns")
            print("4. Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                plot_stock_data(stock_data, ticker)
            elif choice == "2":
                window = int(input("Enter the moving average window (e.g., 20 for 20 days): "))
                plot_moving_averages(stock_data, ticker, window)
            elif choice == "3":
                calculate_daily_returns(stock_data)
            elif choice == "4":
                print("Exiting the Stock Market Analysis Tool. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

