import streamlit as st  
import pandas as pd     # Used to work with tabular data
import numpy as np      # Helps generate random numbers
import plotly.express as px  # For interactive charts

# sample data for demo
np.random.seed(42) # setting a seed so results are consistent for each run

sample_data = {
    'Pollutants': [ 'CO', 'NO', 'NO2', 'O3', 'SO2', 'NH3', 'PM2.5', 'PM10'],
    'Raw': np.random.randint(100,500, size=8),
    'Gold': np.random.randint(20,100, size=8)
}

df = pd.DataFrame(sample_data)

st.title("Air Quality Demo")
tab1, tab2 = st.tabs(["Option 1", "Option2"])

with tab1:
    container = st.container(border=True)
    
    with container:
        left, center, right = st.columns([1,2,1])
        with center:
            options = ["City", "Daily", "Air Quality", "Condition"]
            selection = st.segmented_control(
                "", options
            )
            
            if selection == "City":
                # st.write("City name", text_alignment="center")
                st.markdown("City name", text_alignment="center")
                
            elif selection == "Daily":
                st.markdown("Daily forecast", text_alignment="center")
            
            elif selection == "Air Quality":
                st.markdown("Air quality", text_alignment="center")
                
            elif selection == "Condition":
                st.markdown("Condition", text_alignment="center")
                
            else:
                st.markdown("Please select an option.", text_alignment="center")