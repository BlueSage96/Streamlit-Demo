import streamlit as st  
import pandas as pd     # Used to work with tabular data
import numpy as np      # Helps generate random numbers
import plotly.express as px  # For interactive charts

from navigate import center_nav as cn

# sample data for demo
np.random.seed(42) # setting a seed so results are consistent for each run

sample_data = {
    'Pollutants': ['CO', 'NO', 'NO2', 'O3', 'SO2', 'NH3', 'PM2.5', 'PM10'],
    'Raw': np.random.randint(100,500, size=8),
    'Gold': np.random.randint(20,100, size=8)
}

df = pd.DataFrame(sample_data)

st.title("Air Quality Demo")
tab1, tab2 = st.tabs(["Option 1", "Option 2"])

with tab1:
    cn("tab1")
    # figure out how to show days of the week!! 
    # Hint: will need - an list, day columns & a loop & st.markdown!!
    
with tab2:
    cn("tab2")