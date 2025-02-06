from os import name
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data_loader import load_data
import plotly.graph_objects as go
import warnings


warnings.filterwarnings("ignore", category=FutureWarning)

@st.cache_data
def get_top_bottom(df, category, column):
    # Filter once and sort for top10 and bottom10, then remove indexes
    df_category = df[df['Category'] == category]
    top10 = df_category.sort_values(by=column, ascending=False).head(10).reset_index(drop=True)
    bottom10 = df_category.sort_values(by=column, ascending=True).head(10).reset_index(drop=True)
    return top10, bottom10

def show_waterfall_chart(df):
    categories = df['Category'].unique()
    for category in categories:
        category_data = df[df['Category'] == category]
        
        # Extracting the relevant columns for the waterfall chart
        values = category_data[['Start Balance', 'New Client', 'Closed Clients', 'Net Flow', 'End Balance']].sum().values
        labels = ['Start Balance', 'New Client', 'Closed Clients', 'Net Flow', 'End Balance']
        
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

def show_total_deposit_overview(path):
    df = load_data(path)

    st.header("Total Deposit Overview")

    df['Own Resources'] = df['Own Resources'] + df['From other']
    df = df.drop(columns=['From other'])
    df = df.rename(columns={'Own Resources': 'Net Flow'})
    grouped = df.groupby(['Category'])[df.columns[1:-1]].sum()
    grouped_ = grouped.copy()

    # Add data bars to the grouped data
    for col in grouped.columns:
        max_value = grouped[col].max()
        grouped_[col] = grouped[col].apply(lambda x: f'<div style="background: linear-gradient(90deg, rgba(0, 123, 255, 0.5) {x/max_value*100}%, transparent 50%); ">{x}</div>')
    
    grouped = grouped.reset_index()
    # Write grouped data with data bars
    st.write(grouped_.to_html(escape=False), unsafe_allow_html=True)
    
    show_waterfall_chart(grouped)

    # New UI to select category and numeric column (assumes df has a "User" column)
    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox("Select Product", options=df['Category'].unique())
    with col2:
        numeric_cols = [col for col in df.select_dtypes(include='number').columns]
        selected_column = st.selectbox("Select Column", options = numeric_cols)
    
    # Use cached helper to get sorted results
    top10, bottom10 = get_top_bottom(df, selected_category, selected_column)
    
    st.subheader("Top 10 Users")
    st.write(top10)
    st.subheader("Bottom 10 Users")
    st.write(bottom10)



