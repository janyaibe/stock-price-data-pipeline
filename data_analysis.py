import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('stocks.db')

# Query stock data from the database
query = "SELECT * FROM stock_prices"
df = pd.read_sql_query(query, conn)

# Calculate daily price difference (close - open)
df['price_difference'] = df['close'] - df['open']

# Calculate a 5-day moving average for the closing price
df['5_day_moving_avg'] = df['close'].rolling(window=5).mean()

# Print the DataFrame with the new columns
print(df.head())

# Close the database connection
conn.close()
