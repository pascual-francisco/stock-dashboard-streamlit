import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Title of the dashboard
st.title("📈 Stock Dashboard")

# Input field for the stock ticker
ticker = st.text_input("Enter Stock Ticker Symbol", "AAPL")

# Download stock data from Yahoo Finance
data = yf.download(ticker, period="1mo", interval="1d")

# Create a line chart of the closing prices
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price'))

# Display the chart in the Streamlit app
st.plotly_chart(fig)
