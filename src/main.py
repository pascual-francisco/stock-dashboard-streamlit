import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Title of the dashboard
st.title("📈 Stock Dashboard")

# Input field for the stock ticker
ticker = st.text_input("Enter Stock Ticker Symbol", "AAPL")

# Download data
if ticker:
    data = yf.download(ticker, period="1mo", interval="1d", auto_adjust=True)
    if not data.empty:
        st.success(f"Data loaded for {ticker}")
        st.write(data.tail())
    else:
        st.error("No data found. Please check the ticker symbol.")

# Create a line chart of the closing prices
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price'))

# Display the chart in the Streamlit app
st.plotly_chart(fig)