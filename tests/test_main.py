import pytest
import yfinance as yf
# test_ui.py
import streamlit.testing.v1 as st_test

def test_valid_ticker_download():
    data = yf.download("AAPL", period="1mo", interval="1d", auto_adjust=True)
    assert not data.empty, "Expected data for valid ticker 'AAPL'"

def test_invalid_ticker_download():
    data = yf.download("APL", period="1mo", interval="1d", auto_adjust=True)
    assert data.empty, "Expected no data for invalid ticker 'APL'"

def test_manual_ticker_valid():
    data = yf.download("MSFT", period="1mo", interval="1d", auto_adjust=True)
    assert not data.empty, "Expected data for valid ticker 'MSFT'"

def test_manual_ticker_invalid():
    data = yf.download("XXXXX", period="1mo", interval="1d", auto_adjust=True)
    assert data.empty, "Expected no data for invalid ticker 'XXXXX'"

def test_chart_renders_with_valid_data():
    import yfinance as yf
    import datetime

    ticker = "AAPL"
    start_date = datetime.date.today() - datetime.timedelta(days=30)
    end_date = datetime.date.today()
    interval = "1d"

    data = yf.download(ticker, start=start_date, end=end_date, interval=interval, auto_adjust=True)

    assert not data.empty, "Data should not be empty for a valid ticker"
    assert "Close" in data.columns, "Data should contain 'Close' column"

def test_ui_components():
    app = st_test.AppTest.from_file("your_app.py")

    # Simulates text input
    app.text_input("Enter stock ticker symbol:").set_value("AAPL")

    # Simulates period selection
    app.selectbox("Select period:").set_value("Last 1 Month")

    # Simulates button clic
    app.button("Load Data").click()

    # Verifies graphic render
    assert app.line_chart().exists(), "Chart should be rendered"
