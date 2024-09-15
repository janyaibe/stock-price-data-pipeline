import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('stocks.db')

# Query stock data from the database
query = "SELECT * FROM stock_prices WHERE symbol = 'AAPL'"
df = pd.read_sql_query(query, conn)

# Plot the closing price over time
plt.plot(df['date'], df['close'], label='Closing Price')

# Plot the 5-day moving average
df['5_day_moving_avg'] = df['close'].rolling(window=5).mean()
plt.plot(df['date'], df['5_day_moving_avg'], label='5-Day Moving Avg', linestyle='--')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL Stock Prices')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Close the database connection
conn.close()
