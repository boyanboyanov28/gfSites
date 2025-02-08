import streamlit as st
from utils import specialMessage, stylesForValentinePage


def valentineQuestion():
    stylesForValentinePage()


    st.markdown(
        """
        <div class="pink-container">
        <div class="heart">❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️</div>
        <h1 class="big-text">Will you be my valentine?</h1>
        <div class="heart">❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️</div>
        </div>
        """, 
        unsafe_allow_html=True
    )


    col1, col2 = st.columns([1, 1])

    with col1:
        yes_button = st.button("YES")

    with col2:
        placeholder = st.empty() 
        no_button = placeholder.button("NO")
    
    if yes_button:
        st.session_state.askValentine = False
        st.session_state.showGifOnly = True
        st.rerun()

    if no_button:
        placeholder.empty()