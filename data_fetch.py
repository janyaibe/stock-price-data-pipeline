import sqlite3
import requests
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env
load_dotenv()

# Get the API key from .env or GitHub Actions secret
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

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

# Function to insert stock data into the database
def insert_stock_data(symbol, stock_data):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

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

# ETL Process: Fetch and store data for multiple stock symbols
def run_etl(symbols):
    for symbol in symbols:
        stock_data = get_stock_data(symbol)
        if stock_data:
            insert_stock_data(symbol, stock_data)
            print(f"Stock data for {symbol} inserted into the database.")
        time.sleep(60)  # Sleep for 1 minute between API calls to avoid exceeding the rate limit

# List of stock symbols to track
symbols = ["AAPL", "GOOGL", "MSFT"]

# Run the ETL process
run_etl(symbols)
