import pytest
import yfinance as yf

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

