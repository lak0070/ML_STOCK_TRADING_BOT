import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from datetime import datetime
stocks = ["RELIANCE.NS", "INFY.NS"]
initial_balance = 100000
risk_per_trade = 0.1   
stop_loss_pct = 0.02   
today = datetime.today().strftime('%Y-%m-%d')
def add_indicators(df):
    df['Return'] = df['Close'].pct_change()
    df['SMA_10'] = df['Close'].rolling(10).mean()
    df['SMA_50'] = df['Close'].rolling(50).mean()
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['Target'] = np.where(df['Return'].shift(-1) > 0, 1, 0)
    return df.dropna()
def backtest(df):
    df = df.reset_index(drop=True)
    features = ['SMA_10', 'SMA_50', 'RSI']
    X = df[features]
    y = df['Target']
    split = int(len(df) * 0.7)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]
    model = RandomForestClassifier(n_estimators=200, max_depth=5)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    balance = initial_balance
    shares = 0
    buy_price = 0
    equity_curve = []
    for i in range(len(preds)):
        price = float(df['Close'].iloc[split + i])
        position_size = balance * risk_per_trade
        if int(preds[i]) == 1 and shares == 0:
            shares = position_size // price
            buy_price = price
            balance -= shares * price
        elif shares > 0 and price < buy_price * (1 - stop_loss_pct):
            balance += shares * price
            shares = 0
        elif int(preds[i]) == 0 and shares > 0:
            balance += shares * price
            shares = 0
        equity = balance + shares * price
        equity_curve.append(equity)
    return equity_curve
def calculate_metrics(equity):
    equity = pd.Series(equity)
    returns = equity.pct_change().dropna()
    total_return = (equity.iloc[-1] - equity.iloc[0]) / equity.iloc[0]
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    drawdown = (equity / equity.cummax()) - 1
    max_dd = drawdown.min()
    return total_return, sharpe, max_dd
portfolio_results = {}
for stock in stocks:
    print(f"\nProcessing {stock}...")
    df = yf.download(stock, start="2020-01-01", end=today)
    df = add_indicators(df)
    equity = backtest(df)
    portfolio_results[stock] = equity
for stock, equity in portfolio_results.items():
    total_return, sharpe, max_dd = calculate_metrics(equity)
    print(f"\n📊 {stock}")
    print("Return:", round(total_return * 100, 2), "%")
    print("Sharpe Ratio:", round(sharpe, 2))
    print("Max Drawdown:", round(max_dd * 100, 2), "%")
plt.figure(figsize=(10,5))
for stock, equity in portfolio_results.items():
    plt.plot(equity, label=stock)
plt.title("Portfolio Equity Curve (Till Today)")
plt.xlabel("Time")
plt.ylabel("Portfolio Value")
plt.legend()
plt.show()