import pandas as pd
import streamlit as st
# import pyttsx3
import os
from data_maker import calculate_data

@st.cache_data
def load_data(file_path='example.csv'):
    if not os.path.exists(file_path):
        with st.spinner("Calculating data..."):
            calculate_data(file_path)

    with st.spinner("Loading data..."):
        df = pd.read_csv(file_path, index_col=None)
        df.reset_index(drop=True, inplace=True)
        df['FCLICODE'] = df['FCLICODE'].astype(str)

        print("Data loaded successfully.")
        # engine = pyttsx3.init()
        # engine.say("Data loaded successfully.")
        # engine.runAndWait()
    return df