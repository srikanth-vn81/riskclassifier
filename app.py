import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Please choose a Excel file", accept_multiple_files=True)
for file in uploaded_files:
  df=pd.read_excel(file))
  st.write(df)

