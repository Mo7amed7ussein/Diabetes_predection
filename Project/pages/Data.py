# importing neede libraries
import streamlit as st
import sys
import pandas as pd

# Title
st.markdown(" <center>  <h1> Diabetes Dataset </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

# Link of Data
st.markdown('<a href="https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset"> <center> Link to Dataset  </center> </a> ', unsafe_allow_html=True)

# Load data
df = pd.read_csv("../Project/sources/Diabetes_clean.csv")

# Show data
st.write(df.head())

