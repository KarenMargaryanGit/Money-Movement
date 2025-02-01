import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data_loader import load_data
import plotly.graph_objects as go
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def show_waterfall_chart(df):
    categories = df['Category'].unique()
    print(df['End Balance'].sum(), '--------------------------------------------------------')  
    for category in categories:
        category_data = df[df['Category'] == category]
        
        # Extracting the relevant columns for the waterfall chart
        values = category_data[['Start Balance', 'New Client', 'Closed Clients', 'From other', 'Own Resources', 'End Balance']].sum().values
        labels = ['Start Balance', 'New Client', 'Closed Clients', 'From other', 'Own Resources', 'End Balance']
        
        # Configure measures: first value as absolute, next ones as relative, and final as total
        new_measure = ["absolute"] + ["relative"] * (len(values) - 2) + ["total"]

        fig = go.Figure(go.Waterfall(
            measure=new_measure,
            x=labels,
            y=values,
            connector={"line": {"color": "rgb(63, 63, 63)"}}
        ))
        fig.update_layout(title=f"Waterfall Chart for {category}")
        st.plotly_chart(fig)


def show_top_losers(df):
    # df = load_data()
    top_losers = df.nsmallest(100, 'End Balance')
    st.header('Top 100 Losers')
    st.dataframe(top_losers)
    fig1, ax1 = plt.subplots()
    ax1.bar(top_losers['FCLICODE'], top_losers['End Balance'])
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    tick_positions = ax1.get_xticks()
    tick_labels = top_losers['FCLICODE'].iloc[:len(tick_positions)]
    ax1.set_xticklabels(tick_labels, rotation=90)
    st.pyplot(fig1)

def show_top_gainers(df):
    # df = load_data()
    top_gainers = df.nlargest(100, 'End Balance')
    st.header('Top 100 Gainers')
    st.dataframe(top_gainers)
    fig2, ax2 = plt.subplots()
    ax2.bar(top_gainers['FCLICODE'], top_gainers['End Balance'])
    ax2.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    tick_positions = ax2.get_xticks()
    tick_labels = top_gainers['FCLICODE'].iloc[:len(tick_positions)]
    ax2.set_xticklabels(tick_labels, rotation=90)
    st.pyplot(fig2)

def show_client_analysis(df):
    # df = load_data()

    st.header('Client Analysis')
    
    # Filter for FCLICODE
    fclico_options = df['FCLICODE'].unique()
    fclico_filter = st.multiselect('Filter by FCLICODE', options=fclico_options, default=None)
    
    if fclico_filter:
        filtered_df = df[df['FCLICODE'].isin(fclico_filter)]
        st.dataframe(filtered_df)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        for fclico in fclico_filter:
            client_data = filtered_df[filtered_df['FCLICODE'] == fclico]
            ax.plot(client_data.index, client_data['End Balance'], label=fclico)
        
        ax.set_xlabel('Index')
        ax.set_ylabel('End Balance')
        ax.set_title('End Balance per Client')
        ax.legend(title='FCLICODE')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info('No FCLICODE selected. Displaying total End Balance per Category.')
        total = df.groupby('Category')['End Balance'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(total['Category'], total['End Balance'], marker='o')
        ax.set_xlabel('Category')
        ax.set_ylabel('Total End Balance')
        ax.set_title('Total End Balance by Category')
        plt.xticks(rotation=45)
        st.pyplot(fig)

def main():
    df = load_data()  # load data

    # First row: Waterfall Chart and Top Losers
    col1, col2 = st.columns(2)
    with col1:
        show_waterfall_chart(df)
    with col2:
        show_top_losers(df)

    # Second row: Top Gainers and Client Analysis
    col3, col4 = st.columns(2)
    with col3:
        show_top_gainers(df)
    with col4:
        show_client_analysis(df)

if __name__ == "__main__":
    main()