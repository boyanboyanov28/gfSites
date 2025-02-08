import streamlit as st
import random

def movingButton():

    # Initialize button position in session state
    if "button_x" not in st.session_state:
        st.session_state.button_x = random.randint(100, 600)
    if "button_y" not in st.session_state:
        st.session_state.button_y = random.randint(100, 400)

    # Function to move button
    def move_button():
        st.session_state.button_x = random.randint(100, 600)
        st.session_state.button_y = random.randint(100, 400)

    # Use columns to simulate positioning
    cols = st.columns(10)  # Create 10 columns to help with positioning

    # Determine which column to place the button in
    random_col_index = st.session_state.button_x % 10
    with cols[random_col_index]:
        if st.button("Click me!"):
            move_button()
            st.rerun()  # Refresh page to update position
