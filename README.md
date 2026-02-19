# 📈 Real-Time Market Movement Tracker

A powerful Streamlit-based trading analysis tool that provides real-time market insights using technical analysis indicators.

## ✨ Features

- **Real-time Market Data**: Fetches live price data from Yahoo Finance for any ticker (stocks, crypto, forex, etc.)
- **Technical Analysis**: Implements Simple Moving Average (SMA) crossover strategy
- **Trading Signals**: Generates BUY, SELL, and HOLD signals based on market conditions
- **Risk Management**: Includes stop loss (-2%) and take profit (+5%) recommendations
- **Interactive Visualizations**: Charts displaying price action, moving averages, and buy/sell signals
- **Multi-Asset Support**: Works with stocks, cryptocurrencies, forex pairs, and more

## 🎯 How It Works

The app uses a **Simple Moving Average (SMA) Crossover Strategy**:
- **Short SMA**: 20-period moving average (fast-moving)
- **Long SMA**: 50-period moving average (slow-moving)
- **Buy Signal**: When Short SMA crosses above Long SMA (bullish crossover)
- **Sell Signal**: When Short SMA crosses below Long SMA (bearish crossover)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/romarionoble17-droid/app.py.git
   cd app.py
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## ⚙️ Configuration

You can customize the app by modifying these variables in the code:

- **TICKER**: Change the asset to analyze (e.g., "BTC-USD", "AAPL", "TSLA", "EUR-USD")
- **INTERVAL**: Set the time interval ("1m", "5m", "1h", "1d")
- **SHORT_WINDOW**: Fast moving average period (default: 20)
- **LONG_WINDOW**: Slow moving average period (default: 50)

Example:
```python
TICKER = "AAPL"      # Change to your desired ticker
INTERVAL = "1h"      # Change to your preferred interval
SHORT_WINDOW = 20    # Customize SMA period
LONG_WINDOW = 50     # Customize SMA period
```

## 📊 Supported Tickers

- **Cryptocurrencies**: BTC-USD, ETH-USD, XRP-USD, etc.
- **Stocks**: AAPL, TSLA, GOOGL, MSFT, AMZN, etc.
- **Forex**: EUR-USD, GBP-USD, JPY-USD, etc.
- Any ticker supported by Yahoo Finance

## 📋 Output Metrics

The dashboard displays:
- **Current Price**: Real-time asset price
- **Trading Signal**: BUY, SELL, or HOLD recommendation
- **Target Price**: Take profit level (+5% from entry)
- **Stop Loss**: Risk management level (-2% from entry)
- **Price Chart**: Visual representation with technical indicators
- **Buy/Sell Markers**: Visual indicators on the chart

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. It does not constitute financial advice. Always:
- Conduct your own research
- Manage your risk appropriately
- Never invest more than you can afford to lose
- Consult with a financial advisor for professional guidance

## 🔄 Continuous Monitoring (24/7)

To run this app continuously:
- Deploy on Streamlit Cloud: https://streamlit.io/cloud
- Set up a server with automatic refresh using Streamlit's autorefresh component
- Current version uses manual refresh button

## 📦 Requirements

See `requirements.txt` for all dependencies:
- yfinance
- pandas
- matplotlib
- streamlit

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📝 License

This project is open source and available under the MIT License.

---

**Last Updated**: February 19, 2026
**Maintained by**: romarionoble17-droid