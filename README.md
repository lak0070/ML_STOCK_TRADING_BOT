# Coding Projects

This repository contains coding examples and projects in C++ and Python.

## Files

- `Stock.py`: A Python script for backtesting a stock trading strategy using machine learning (Random Forest classifier) on Indian stocks (RELIANCE.NS and INFY.NS). It downloads historical data from Yahoo Finance, calculates technical indicators (SMA, RSI), trains a model, and simulates trading with risk management.

- `1.cpp`: A basic C++ program (currently incomplete).

## Prerequisites

### Python (for Stock.py)
- Python 3.x
- Required libraries: pandas, numpy, yfinance, scikit-learn, matplotlib

Install dependencies using pip:
```
pip install pandas numpy yfinance scikit-learn matplotlib
```

### C++ (for 1.cpp)
- A C++ compiler (e.g., g++ from MinGW)

## Usage

### Running Stock.py
1. Ensure dependencies are installed.
2. Run the script:
   ```
   python Stock.py
   ```
   This will process the specified stocks, perform backtesting, and print results.

### Building and Running 1.cpp
1. Use the provided build task in VS Code or compile manually:
   ```
   g++ 1.cpp -o 1.exe
   ```
2. Run the executable:
   ```
   ./1.exe
   ```
   Note: The program is currently incomplete and may not produce output.

## Notes
- The stock backtesting script uses historical data and is for educational purposes only. Not financial advice.
- The C++ file is a starting point and needs completion.