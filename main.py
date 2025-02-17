import streamlit as st
from data_loader import load_data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
import calendar
from total_deposit_overview import show_total_deposit_overview
from clients_flow_monitoring import show_clients_flow_monitoring


# path = 'data/productMoneyMovementsByCurrency-20231231-20241231.csv'

# Page layout
st.set_page_config(page_title="Money Movement App", layout="wide")

with st.sidebar:
    st.header("Filter Options")
    

    st.subheader("Select Page")
    page = st.sidebar.selectbox('', ["Total Deposit Overview", "Clients Flow Monitoring" ])
    
    
    st.subheader("")
    st.subheader("Select Date Range")
    
    years = list(range(2025, 2020, -1))
    months = list(calendar.month_name)[1:]  

    # Create side-by-side columns
    col1, col2 = st.columns(2)

    # Select start and end dates
    with col1:
        start_year = st.selectbox("Start Year", years, index=2)
        end_year = st.selectbox("End Year", years, index=1)

    with col2:
        start_month = st.selectbox("Start Month", months, index=11)
        end_month = st.selectbox("End Month", months, index=11)

    # Convert selected values to numerical format
    start_month_num = months.index(start_month) + 1
    end_month_num = months.index(end_month) + 1

    # Get first day of start month and last day of end month
    start_date = datetime(start_year, start_month_num, calendar.monthrange(start_year, start_month_num)[1])
    end_date = datetime(end_year, end_month_num, calendar.monthrange(end_year, end_month_num)[1])

    
    # Ensure that start_date is before end_date
    if start_date >= end_date:
        st.error("Error: Start date must be before end date.")
    else:
        # Print selected dates
        st.write(f"**Selected Start Date:** {start_date.strftime('%Y-%m-%d')}")
        st.write(f"**Selected End Date:** {end_date.strftime('%Y-%m-%d')}")
        path = f"data/productMoneyMovementsByCurrency-{start_date.strftime('%Y%m%d')}-{end_date.strftime('%Y%m%d')}.csv"


       




if page == "Total Deposit Overview":
    show_total_deposit_overview(path)
elif page == "Clients Flow Monitoring":
    show_clients_flow_monitoring(path)
# elif page == "Top Losers":
#     show_top_losers(path)
# elif page == "Top Gainers":
#     show_top_gainers(path)
# elif page == "Client Analysis":
#     show_client_analysis(path)
# elif page == 'Waterfall Chart':
#     show_waterfall_chart(path)