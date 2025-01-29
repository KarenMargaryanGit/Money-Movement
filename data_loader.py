import pandas as pd
import streamlit as st
import pyttsx3

@st.cache_data
def load_data(file_path='example.csv'):
    df = pd.read_csv(file_path, index_col=None)
    df.reset_index(drop=True, inplace=True)

    print("Data loaded successfully.")
    engine = pyttsx3.init()
    engine.say("Data loaded successfully.")
    engine.runAndWait()
    return df