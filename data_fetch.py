import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

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

# Example usage
stock_symbol = "AAPL"
stock_data = get_stock_data(stock_symbol)

if stock_data:
    print(json.dumps(stock_data, indent=4))
