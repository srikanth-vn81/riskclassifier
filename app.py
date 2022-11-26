import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Please choose a CSV file", accept_multiple_files=True)

