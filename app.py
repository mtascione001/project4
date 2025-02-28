import os
from altair import themes
import streamlit as st
import pandas as pd
import plotly.express as px

data_car_sales=pd.read_csv('vehicles_us.csv')


#data_car_sales['manufacturer']=data_car_sales['model'].apply(lambda x: x.split()[0])
#st.header('Data Viewer', divider=True, color='black')
data_car_sales['manufacturer']=data_car_sales['model'].apply(lambda x: x.split()[0])
st.header('Data Viewer', divider=True)
st.dataframe(data_car_sales)


st.header('Vehicle types by manufacturer')
fig=px.histogram(data_car_sales, x='manufacturer', color='type')
st.write(fig)

st.header("Histogram of condition vs model_year")
fig=px.histogram(data_car_sales,'model_year', color='condition')
st.write(fig)

st.header('Compare price distribution between manuafacturers')
manufac_list=sorted(data_car_sales['manufacturer'].unique())
manufacturer_1=st.selectbox(label='Select manufacturer 1',
                            options=manufac_list,
                            index=manufac_list.index('chevrolet')
)
manufacturer_2=st.selectbox(label='Select manufacturer 2',
                            options=manufac_list,
                            index=manufac_list.index('hyundai')
                            )
mask_filter=((data_car_sales['manufacturer']==manufacturer_1) | (data_car_sales['manufacturer']==manufacturer_2))
df_filtered=data_car_sales[mask_filter]


normalize=st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm='percent'
else:
    histnorm=None
fig=px.histogram(df_filtered,
                     x='price',
                     nbins=30,
                     color='manufacturer',
                     histnorm=histnorm,
                     barmode='overlay')
    
st.write(fig)
