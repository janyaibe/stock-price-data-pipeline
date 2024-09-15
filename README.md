
# Stock Price Data Pipeline

## Project Overview

This project demonstrates a complete data engineering pipeline that extracts real-time stock price data using the **Alpha Vantage API**, stores it in an **SQLite** database, performs basic analysis, and visualizes trends using **Matplotlib**. The pipeline is automated with **GitHub Actions**, ensuring that the ETL (Extract, Transform, Load) process runs hourly to update the stock data.

### Key Features:
- **Hourly stock data ingestion** from Alpha Vantage API.
- Data is stored in a lightweight **SQLite** database.
- Basic data analysis, such as **price differences** and **moving averages**.
- Stock price **visualization** using **Matplotlib**.
- Automated **ETL process** using **GitHub Actions**.

---

## Prerequisites

### Tools and Libraries
Before starting, ensure you have the following tools installed:

- **Python 3.x**
- **SQLite3** (pre-installed with Python)
- Python packages:
  - `requests`
  - `python-dotenv`
  - `pandas`
  - `matplotlib`

To install the required Python packages, run:
```bash
pip install requests python-dotenv pandas matplotlib
```

### API Key Setup
You'll need an **Alpha Vantage API key** to fetch stock data:

1. Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key) to obtain your API key.
2. Create a `.env` file in the root directory of the project and add the following line:

```bash
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
```

---

## Project Setup

### 1. Clone the Repository
To get started, clone the repository and navigate into the project directory:
```bash
git clone https://github.com/your-username/stock-price-data-pipeline.git
cd stock-price-data-pipeline
```

### 2. Configure API Key
Ensure your **Alpha Vantage API key** is properly set in the `.env` file as described in the **API Key Setup** section.

### 3. Running the ETL Pipeline

The core ETL process is defined in the `data_fetch.py` script.

#### How It Works:
- The script fetches stock data for specified symbols (e.g., AAPL, GOOGL, MSFT) from the **Alpha Vantage API**.
- The data is stored in a local **SQLite** database (`stocks.db`).
- If the `stock_prices` table does not already exist, it is created and stock data is inserted on an hourly basis using **GitHub Actions**.

#### Running Locally:
To run the ETL process locally, execute the following command:
```bash
python data_fetch.py
```

### 4. GitHub Actions Automation

The ETL process is automated using **GitHub Actions**, which runs hourly to fetch new stock data.

#### GitHub Actions Workflow:
- The workflow is defined in `.github/workflows/etl.yml`.
- **Cron Job**: It is scheduled to run every hour (`cron: '0 * * * *'`).
- **Artifacts**: After each run, the SQLite database (`stocks.db`) is saved as an artifact.

---

## Data Analysis

Once the ETL process is complete, you can analyze the stock data using the `data_analysis.py` script.

### Example Analyses:
- **Daily Price Difference**: Calculate the difference between opening and closing prices.
- **5-Day Moving Average**: Compute the simple moving average over the last 5 days of closing prices.

#### Running the Analysis:
Execute the following command to run the analysis:
```bash
python data_analysis.py
```

---

## Data Visualization

The `data_visualization.py` script generates visualizations using **Matplotlib** to plot stock price trends, such as closing prices and moving averages.

#### Running the Visualization:
To generate the visualizations, run:
```bash
python data_visualization.py
```

---

## Troubleshooting

- **Database Not Found**: Ensure the database is created by checking the working directory in the **GitHub Actions** logs.
- **API Rate Limits**: Alpha Vantage allows up to 5 requests per minute. For multiple stock symbols, implement a delay between API calls to avoid hitting this limit.
- **Visualization Issues**: Ensure **Matplotlib** is installed and functioning correctly. To install or update Matplotlib, run:
  ```bash
  pip install matplotlib
  ```

---
