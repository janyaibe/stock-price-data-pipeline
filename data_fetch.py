import sqlite3
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the API key from .env
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Connect to SQLite database (stocks.db)
conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()

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

# Example usage: Fetch and store stock data for Apple (AAPL)
stock_symbol = "AAPL"
stock_data = get_stock_data(stock_symbol)

# If data was retrieved, insert it into the database
if stock_data:
    insert_stock_data(stock_symbol, stock_data)
    print(f"Stock data for {stock_symbol} has been inserted into the database.")

# Close the connection to the database
conn.close()
