import yfinance as yf
import pandas as pd
import streamlit as st

st.title("📈 Stock Data Downloader")

ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, MSFT, TSLA)", "AAPL")
start_date = st.date_input("Select Start Date", pd.to_datetime("2024-05-23"))
end_date = st.date_input("Select End Date", pd.to_datetime("2025-05-23"))

if st.button("Download CSV"):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            csv = data.to_csv().encode('utf-8')
            st.download_button(
                label="📥 Click here to download CSV",
                data=csv,
                file_name=f"{ticker}_stock_data.csv",
                mime="text/csv"
            )
        else:
            st.error("No data found for the selected ticker and date range.")
    except Exception as e:
        st.error(f"Error downloading data: {e}")
