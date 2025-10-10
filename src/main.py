import streamlit as st
import yfinance as yf
import datetime
import plotly.graph_objs as go

# Title of the dashboard
st.title("📈 Stock Dashboard")

popular_tickers = {
    "Apple Inc. (AAPL)": "AAPL",
    "Microsoft Corp. (MSFT)": "MSFT",
    "Amazon.com Inc. (AMZN)": "AMZN",
    "Alphabet Inc. (GOOGL)": "GOOGL",
    "Tesla Inc. (TSLA)": "TSLA",
    "Meta Platforms Inc. (META)": "META",
    "Nvidia Corp. (NVDA)": "NVDA",
    "Advanced Micro Devices (AMD)": "AMD",
    "Netflix Inc. (NFLX)": "NFLX",
    "Broadcom Inc. (AVGO)": "AVGO",
    "JPMorgan Chase & Co. (JPM)": "JPM",
    "Visa Inc. (V)": "V",
    "Walmart Inc. (WMT)": "WMT",
    "Procter & Gamble Co. (PG)": "PG",
    "Johnson & Johnson (JNJ)": "JNJ"}

# Ticker Selector
selected_name = (st.selectbox("Select a popular company:", ["Other (type manually)"] + list(popular_tickers.keys())))

if selected_name == "Other (type manually)":
    ticker = st.text_input("Enter custom ticker symbol:", "AAPL").upper()
else:
    ticker = popular_tickers[selected_name]

#Quick period options
period_option = st.selectbox("Select period:", ("Last 7 Days", "Last 1 Month", "Last 1 Year", "Custom Range"))
today = datetime.date.today()

if period_option == "Last 7 Days":
    start_date = today - datetime.timedelta(days=7)
    end_date = today
elif period_option == "Last 1 Month":
    start_date = today - datetime.timedelta(days=30)
    end_date = today
elif period_option == "Last 1 Year":
    start_date = today - datetime.timedelta(days=365)
    end_date = today
else:
    start_date = st.date_input("Start date", value=today - datetime.timedelta(days=30))
    end_date = st.date_input("End date", value=today)

#Interval selection
interval = st.selectbox("Select data interval:", ("1d", "1wk", "1mo"))

# Download data
if st.button("Load Data"):
    if start_date <= end_date:
        try:
            data = yf.download(ticker, start=start_date, end=end_date, interval=interval, auto_adjust=True)

            if data.empty:
                st.error(f"No data found for ticker '{ticker}'. Please check the symbol and try again.")
            else:
                st.subheader(f"{ticker} Closing Price")
                st.line_chart(data["Close"])
        except Exception as e:
            st.error(f"An error occurred while fetching data: {e}")
    else:
        st.error("Start date must be before end date.")
