import streamlit as st 
import pandas as pd 


name = st.text_input("Enter your Name")
age = st.slider("Choose your age:",1,100,25)
options=["python","java","c","rust"]
choice =st.selectbox("Choose your favourite language:",options)

data = {
    'Name':['Sam','Lam','Kam','Mam'],
    'Age':[12,23,34,54],
    'City':['a','b','c','d']
}

df = pd.DataFrame(data)
df.to_csv('sample.csv')

uploaded_file = st.file_uploader("Upload your file here",type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)