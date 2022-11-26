import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader("Choose Stylereco file",accept_multiple_files=True)
if uploaded_file is not None:
        #file_container = st.expander("Check your uploaded .excel")
        shows = pd.read_excel(uploaded_file)
        uploaded_file.seek(0)
        st.write(shows)
else:
        st.info(
            f"""
                👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
                """
        )

        st.stop()
