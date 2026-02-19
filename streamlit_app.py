import import streamlit as st
import pandas as pd
import numpy as np
yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta

# --- CONFIGURATION ---
TICKER = "BTC-USD"  # Change to "AAPL", "TSLA", "EUR-USD" etc.
INTERVAL = "1m"     # 1m, 5m, 1h, 1d
SHORT_WINDOW = 20   # Fast moving average
LONG_WINDOW = 50    # Slow moving average

# --- LOGIC ---
def get_data(ticker, interval, period='1d'):
    # Fetch data from Yahoo Finance
    df = yf.download(ticker, period=period, interval=interval, progress=False)
    return df

def calculate_indicators(df):
    # Calculate Simple Moving Averages (SMA)
    df['SMA_Short'] = df['Close'].rolling(window=SHORT_WINDOW).mean()
    df['SMA_Long'] = df['Close'].rolling(window=LONG_WINDOW).mean()
    
    # Generate Signals
    df['Signal'] = 0
    df['Signal'][SHORT_WINDOW:] = \
        pd.Series(1 if s > l else -1 for s, l in zip(df['SMA_Short'][SHORT_WINDOW:], df['SMA_Long'][SHORT_WINDOW:]))
    
    # Determine Buy/Sell positions
    df['Position'] = df['Signal'].diff()
    return df

def analyze_trade(df):
    # Get the last row for real-time advice
    last_row = df.iloc[-1]
    prev_row = df.iloc[-2]
    
    price = last_row['Close']
    signal = "HOLD"
    color = "white"
    
    # Buy Signal: Short SMA crosses above Long SMA
    if prev_row['SMA_Short'] <= prev_row['SMA_Long'] and last_row['SMA_Short'] > last_row['SMA_Long']:
        signal = "STRONG BUY"
        color = "green"
        
    # Sell Signal: Short SMA crosses below Long SMA
    elif prev_row['SMA_Short'] >= prev_row['SMA_Long'] and last_row['SMA_Short'] < last_row['SMA_Long']:
        signal = "STRONG SELL"
        color = "red"
        
    # Stop Loss / Take Profit Logic (Example: 2% Stop Loss, 5% Take Profit)
    # Note: In a real app, you track the *entry price* of the trade.
    # This is a simplified dynamic calculation.
    
    return signal, color, price

# --- UI (Streamlit) ---
st.set_page_config(page_title="Market Predictor 24/7", layout="wide")
st.title("ðŸ“ˆ Real-Time Market Movement Tracker")

# Auto-refresh logic (simulated 24/7)
st.markdown("---")
st.subheader(f"Live Analysis: {TICKER}")

# Fetch Data
try:
    df = get_data(TICKER, INTERVAL)
    df = calculate_indicators(df)
    
    # Get current status
    signal, color, current_price = analyze_trade(df)
    
    # Display Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${current_price:.2f}")
    col2.metric("Signal", signal, delta_color="normal")
    
    # Dynamic Advice
    if signal == "STRONG BUY":
        st.success(f"âœ… ADVICE: BUY NOW! \nTarget: +5% (${current_price * 1.05:.2f}) \nStop Loss: -2% (${current_price * 0.98:.2f})")
    elif signal == "STRONG SELL":
        st.error(f"âŒ ADVICE: SELL NOW! \nProtect your capital.")
    else:
        st.info("âš–ï¸ MARKET STATUS: WAIT / HOLD")

    # --- VISUALIZATION ---
    st.subheader("Chart Analysis")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Price
    ax.plot(df['Close'], label='Price', color='blue', alpha=0.5)
    
    # Plot SMAs
    ax.plot(df['SMA_Short'], label=f'{SHORT_WINDOW} SMA', color='orange')
    ax.plot(df['SMA_Long'], label=f'{LONG_WINDOW} SMA', color='purple')
    
    # Plot Buy Signals (Green)
    buy_signals = df[df['Position'] == 2]
    ax.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', s=100, label='Buy Signal', zorder=5)
    
    # Plot Sell Signals (Red)
    sell_signals = df[df['Position'] == -2]
    ax.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', s=100, label='Sell Signal', zorder=5)
    
    ax.legend()
    st.pyplot(fig)

    # Auto-refresh button
    if st.button('Refresh Data'):
        st.rerun()

except Exception as e:
    st.error(f"Error fetching data: {e}")

# Note: To make this truly 24/7 on a server, you would remove the button 
# and use Streamlit's autorefresh component or a loop.
