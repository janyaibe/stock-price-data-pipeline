import os
import sqlite3
import requests
from dotenv import load_dotenv
import time

# Load environment variables from .env
load_dotenv()

# Get the API key from .env or GitHub Actions secret
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Function to get stock data
def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Time Series (Daily)' in data:
            return data['Time Series (Daily)']
        else:
            print(f"Error: {data.get('Note', 'No data available for this symbol')}")
            return None
    else:
        print(f"Error: Failed to fetch data (status code: {response.status_code})")
        return None

# Function to create the stock_prices table if it doesn't exist
def create_table_if_not_exists(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL,
        date TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER
    )
    ''')

# Function to insert stock data into the database
def insert_stock_data(symbol, stock_data):
    # Connect to SQLite database (this will create 'stocks.db' if it doesn't exist)
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    # Ensure the table exists before inserting data
    create_table_if_not_exists(cursor)

    for date, daily_data in stock_data.items():
        cursor.execute('''
            INSERT INTO stock_prices (symbol, date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            symbol,
            date,
            float(daily_data['1. open']),
            float(daily_data['2. high']),
            float(daily_data['3. low']),
            float(daily_data['4. close']),
            int(daily_data['5. volume'])
        ))
    conn.commit()
    conn.close()
    print(f"Stock data for {symbol} inserted into the database.")

# ETL Process: Fetch and store data for multiple stock symbols
def run_etl(symbols):
    for symbol in symbols:
        print(f"Fetching stock data for {symbol}...")
        stock_data = get_stock_data(symbol)
        if stock_data:
            insert_stock_data(symbol, stock_data)
        else:
            print(f"No data fetched for {symbol}.")
        time.sleep(60)  # Sleep for 1 minute between API calls to avoid exceeding the rate limit

# List of stock symbols to track
symbols = ["AAPL", "GOOGL", "MSFT"]

# Run the ETL process
run_etl(symbols)
