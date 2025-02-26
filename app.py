import os
import streamlit as st
import pandas as pd
import plotly_express as px

df=pd.read_csv('vehicles_us.csv')

st.header('Analyzing Car Sales',divider=True)
st.write('streamlit exercise')
st.title('Streamlit App')
