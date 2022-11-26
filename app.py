

import pandas as pd
import streamlit as st

file_list = st.file_uploader("Upload Style Reco File", accept_multiple_files=True)
excl_list = []
for file in file_list:
	excl_list.append(pd.read_excel(file))
excl_merged = pd.DataFrame()

for excl_file in excl_list:
	excl_merged = excl_merged.append(excl_file, ignore_index=True)

else:
	st.info(
            f"""
                👆 Upload a .xlsx file)
                """

       )



