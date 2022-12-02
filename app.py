import streamlit as st
from main import show_predict_page

st.set_page_config(
    page_title='Car Price Prediction', 
    page_icon='assets/free-car-icon-1057-thumb.png',  
    initial_sidebar_state = 'auto')

st.title('Car Price Prediction')

show_predict_page()