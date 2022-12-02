import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import plotly.figure_factory as ff

df = pd.read_csv('data.csv')

def show_data_frame():
    st.dataframe(df,use_container_width=True)

# def show_heat_map():
    # fig, ax = plt.subplots()
    # sns.heatmap(df.corr(), ax=ax)
    # st.write(fig)

def rfa():

    col1, col2 = st.columns(2)

    with col1:

        st.write("###### Linear Regression Accuracy")
        st.write("Train set accuracy: ", 0.72)
        st.write("Test set accuracy : ", -6.0)
    
    with col2:

        st.write("###### Decision Tree Accuracy")
        st.write("Train set accuracy: ", 0.7406)
        st.write("Test set accuracy : ", 0.83)

    st.write('')

    col1, col2 = st.columns(2)

    with col1:

        st.write("###### KNN Accuracy")
        st.write("Train set accuracy: ", 0.72)
        st.write("Test set accuracy : ", 0.63)

    with col2:

        st.write("###### PipleLine Model with Decision Tree")
        st.write("Train set accuracy: ",0.89)
        st.write("Test set accuracy : ", 0.83)