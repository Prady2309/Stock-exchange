import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App       

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol 
tickerSymbol1 = 'AAPL'       # abbr
tickerSymbol2 = 'HPQ'
tickerSymbol3 = 'WMT'

#get data on this ticker
tickerData1 = yf.Ticker(tickerSymbol1)       # gets real time stock data and informations
tickerData2 = yf.Ticker(tickerSymbol2)
tickerData3 = yf.Ticker(tickerSymbol3)

#get the historical prices for this ticker
tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end='2020-5-31')     # 1d = daily
tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf3 = tickerData3.history(period='1d', start='2010-5-31', end='2020-5-31')


# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
Shown are the stock **Opening** and **Closing** of ***Apple***!
         """)
#FOR Apple
st.line_chart(tickerDf1.Open)    # closing value
st.line_chart(tickerDf1.Close)   # volume of stocks

#FOR HP
st.write("""
Shown are the stock **Opening** and **Closing** of ***Hewlett-Packard***!
         """)
st.line_chart(tickerDf2.Open)    # closing value
st.line_chart(tickerDf2.Close)   # volume of stocks

#FOR Walmart
st.write("""
Shown are the stock **Opening** and **Closing** of ***Walmart***!
         """)
st.line_chart(tickerDf3.Open)    # closing value
st.line_chart(tickerDf3.Close)   # volume of stocks