from os import name
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data_loader import load_data
import plotly.graph_objects as go
import warnings
from total_deposit_overview import show_waterfall_chart


warnings.filterwarnings("ignore", category=FutureWarning)

def show_clients_flow_monitoring(path):
    df = load_data(path)

    st.header("Clients Flow Monitoring")

    fclico_all = df['FCLICODE'].unique()
    search_fclico = st.text_input('Search FCLICODE')
    if search_fclico:
        fclico_options = [code for code in fclico_all if search_fclico in str(code)]
    else:
        fclico_options = list(fclico_all)
    fclico_filter = st.multiselect('Filter by FCLICODE', options=fclico_options)

    if fclico_filter:
        filtered_df = df[df['FCLICODE'].isin(fclico_filter)]
        filtered_df = filtered_df.reset_index(drop=True)
        # Add data bars to the grouped data
        filtered_df_ = filtered_df.copy()
        for col in filtered_df.columns[1:-1]:   
            if pd.api.types.is_numeric_dtype(filtered_df[col]):
                max_value = filtered_df[col].max()
                filtered_df_[col] = filtered_df[col].apply(lambda x: f'<div style="background: linear-gradient(90deg, rgba(0, 123, 255, 0.5) {x/max_value*100}%, transparent 50%); ">{x}</div>')
        
        # Write grouped data with data bars
        st.write(filtered_df_.to_html(escape=False), unsafe_allow_html=True)

        # Show waterfall charts

       
        categories = filtered_df['Category'].unique()
        for category in categories:
            category_data = filtered_df[filtered_df['Category'] == category]
            
            # Extracting the relevant columns for the waterfall chart
            values = category_data[['Start Balance', 'New Client', 'Closed Clients', 'From other', 'Own Resources', 'End Balance']].sum().values
            labels = ['Start Balance', 'New Client', 'Closed Clients', 'From other', 'Own Resources', 'End Balance']
            
            # Configure measures: first value as absolute, next ones as relative, and final as total
            new_measure = ["absolute"] + ["relative"] * (len(values) - 2) + ["total"]

            fig = go.Figure(go.Waterfall(
                measure=new_measure,
                x=labels,
                y=values,
                connector={"line": {"color": "rgb(63, 63, 63)"}}  # Removed name parameter
            ))
            fig.update_layout(title=f"Waterfall Chart for {category}")
            st.plotly_chart(fig)  # Removed subheader          
        