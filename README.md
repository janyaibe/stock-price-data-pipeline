# stock-price-data-pipeline
A Python-based data engineering project that collects, stores, processes, and visualizes real-time stock price data using Alpha Vantage API, SQLite, and Matplotlib.
# Stock Price Data Pipeline

## Project Overview
This project demonstrates a complete data engineering pipeline that extracts stock price data using the Alpha Vantage API, stores it in an SQLite database, performs basic analysis, and visualizes trends. The pipeline is automated using GitHub Actions, ensuring the ETL process runs hourly to update the stock data.

### Features:
- Hourly stock data ingestion from Alpha Vantage API.
- Data stored in a lightweight SQLite database.
- Basic data analysis (price differences, moving averages).
- Stock price visualization with Matplotlib.
- Automated workflow using GitHub Actions.

---

## Prerequisites
### Tools and Libraries
Before you begin, ensure you have the following installed:
- **Python 3.x**
- **SQLite3** (comes pre-installed with Python)
- Python packages:
  - `requests`
  - `python-dotenv`
  - `pandas`
  - `matplotlib`

You can install the required packages using:
```bash
pip install requests python-dotenv pandas matplotlib


API Key
To fetch stock data, you'll need to sign up for an Alpha Vantage API key:

Visit Alpha Vantage.
Obtain your API key and store it in a file named .env in the root directory of your project.

Example .env file:
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key


