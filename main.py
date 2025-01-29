import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data_loader import load_data
from pages import *
import sys
import os

# Page layout
st.set_page_config(page_title="Money Movement App", layout="wide")

with st.sidebar:
    st.header("Filter Options")
    # Custom Date Range Picker
    st.subheader("Select Date Range")

    # Define year range
    years = list(range(2010, 2025))  # 2010 to 2024 inclusive

    # Define month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Mapping month names to numbers
    month_mapping = {month: index for index, month in enumerate(months, start=1)}

    # Select Start Year and Month
    st.subheader("Select Start Date")
    start_year = st.selectbox("Start Year", years, index=years.index(2010))
    start_month = st.selectbox("Start Month", months, index=0)

    # Select End Year and Month
    st.subheader("Select End Date")
    end_year = st.selectbox("End Year", years, index=years.index(2024))
    end_month = st.selectbox("End Month", months, index=11)

    # Display selected dates
    st.markdown("## Selected Date Range")
    st.write(f"**Start Date:** {start_month} {start_year}")
    st.write(f"**End Date:** {end_month} {end_year}")


    # # Ensure that start_date is before end_date
    # if start_date > end_date:
    #     st.error("Error: Start date must be before end date.")
    # else:
    #     # Print selected dates
    #     st.write(f"**Selected Start Date:** {start_date}")
    #     st.write(f"**Selected End Date:** {end_date}")


# Top bar with Quit button
col1, col2 = st.columns([9, 1])
with col2:
    if st.button("Quit"):
        st.cache_data.clear()
        st.stop()
        


# Load data
df = load_data()



# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Top Losers", "Top Gainers", "Client Analysis"])

if page == "Top Losers":
    show_top_losers()
elif page == "Top Gainers":
    show_top_gainers()
elif page == "Client Analysis":
    show_client_analysis()