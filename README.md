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
```bash

### API Key
To fetch stock data, you'll need to sign up for an Alpha Vantage API key:
1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. Obtain your API key and store it in a file named `.env` in the root directory of your project.
   
Example `.env` file:
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
Obtain your API key and store it in a file named .env in the root directory of your project.

Example .env file:
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key



---

## Project Setup

### 1. Clone the Repository
First, clone the project repository from GitHub:
```bash
git clone https://github.com/your-username/stock-price-data-pipeline.git
cd stock-price-data-pipeline

ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key


### 3. Running the ETL Pipeline
The core of the project is the **data_fetch.py** script, which handles the ETL process (Extract, Transform, Load).

#### How It Works:
- The script fetches stock data for specified symbols (e.g., AAPL, GOOGL, MSFT) from Alpha Vantage.
- Data is stored in a local SQLite database (`stocks.db`).
- The table `stock_prices` is created if it doesn’t already exist, and data is inserted on an hourly basis using GitHub Actions.

#### Running Locally:
You can run the ETL process locally by executing the script:
```bash
python data_fetch.py


### 4. GitHub Actions Automation
The ETL process is automated using GitHub Actions. The pipeline runs every hour, fetching and inserting new stock data.

#### GitHub Actions Workflow:
The workflow is defined in `.github/workflows/etl.yml`.

- **Cron Job**: The workflow runs every hour (`cron: '0 * * * *'`).
- **Artifacts**: The SQLite database (`stocks.db`) is saved as an artifact at the end of each run.

---

## Data Analysis (Step 5)

After running the ETL process, the data analysis script (`data_analysis.py`) provides basic transformations and insights.

#### Example Analysis:
- **Daily Price Difference**: The difference between the opening and closing prices.
- **5-Day Moving Average**: A simple moving average over the last 5 days of closing prices.

#### Running the Analysis:
```bash
python data_analysis.py


## Data Visualization (Step 6)

The visualization script (`data_visualization.py`) uses **Matplotlib** to plot trends, such as closing prices and moving averages, for each stock symbol.

#### Running the Visualization:
```bash
python data_visualization.py



## Troubleshooting

- Database Not Found: Ensure the database is created properly by checking the working directory in the GitHub Actions logs.
- API Rate Limits: Alpha Vantage has a limit of 5 requests per minute. If you're querying many symbols, ensure there’s a delay between API calls to avoid hitting the rate limit.
- Visualization Issues: Ensure Matplotlib is installed and functioning correctly. You can install it using:
```bash
pip install matplotlib
