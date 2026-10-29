import streamlit as st

def center_nav(key):
    container = st.container(border=True)
        
    with container:
        left, center, right = st.columns([1,2,1])
        with center:
            options = ["City", "Daily", "Air Quality", "Condition"]
            selection = st.segmented_control(
                "", options,key=key
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