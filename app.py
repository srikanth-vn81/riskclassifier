import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Please choose a Excel file", accept_multiple_files=True)
st.dataframe(uploaded_files)

