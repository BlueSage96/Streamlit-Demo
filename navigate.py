import streamlit as st

def center_nav(key):
    container = st.container(border=True)
        
    with container:
        left, center, right = st.columns([1,2,1])
        
        # options menu
        with center:
            options = ["City", "Daily", "Air Quality", "Condition"]
            selection = st.segmented_control(
                "", options,key=f"{key}_nav"
            )
            
            if selection == "City":
                st.markdown("City name", text_alignment="center")
                
            elif selection == "Daily":
                st.markdown("Daily forecast", text_alignment="center")
            
            elif selection == "Air Quality":
                st.markdown("Air quality", text_alignment="center")
                
            elif selection == "Condition":
                st.markdown("Condition", text_alignment="center")
                
            else:
                st.markdown("Please select an option.", text_alignment="center")
        
        # Account button
        with right:
            st.space("small")
            account = st.button("Log in", key=f"{key}_button")  
            if account: 
                st.write(account)
                
        with left:
            st.space("small")
            left_container = st.container(border=True)
            with left_container:
                poll_list = ['CO', 'NO', 'NO2', 'O3', 'SO2', 'NH3', 'PM2.5', 'PM10']
                pollutants = [row for row in poll_list]
                poll_select = st.selectbox("View pollutants", options=pollutants, key=f"{key}_poll")

                # can add facts for each pollutants
     