import streamlit as st

# -- Set page config
apptitle = 'Dice Roller'
st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# Title the app
st.title('About Page')

st.markdown(
    """
    This page describes the use and structure of this app.
    
    ### Odds API
    """
)