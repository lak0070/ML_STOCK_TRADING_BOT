# Stock Trading Backtesting Script

This repository contains a Python script for backtesting a stock trading strategy using machine learning (Random Forest classifier) on Indian stocks (RELIANCE.NS and INFY.NS). The script downloads historical data from Yahoo Finance, calculates technical indicators (SMA, RSI), trains a model, and simulates trading with risk management.

## Prerequisites

- Python 3.x
- Required libraries: pandas, numpy, yfinance, scikit-learn, matplotlib

Install dependencies using pip:
```
pip install pandas numpy yfinance scikit-learn matplotlib
```

## Usage

1. Ensure dependencies are installed.
2. Run the script:
   ```
   python Stock.py
   ```
   This will process the specified stocks, perform backtesting, and display results including return, Sharpe ratio, max drawdown, and an equity curve plot.

## Notes

- The stock backtesting script uses historical data and is for educational purposes only. Not financial advice.
- The script backtests on RELIANCE.NS and INFY.NS stocks from 2020-01-01 to today.