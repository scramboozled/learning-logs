# streamlit run streamlit/app.py 

import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Welcome!")

st.write("Hello,world")

df = pd.DataFrame({
    'First':[1,2,3,4,5],
    'Second':[6,7,8,9,10]
})


st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)