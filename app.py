

import pandas as pd
import streamlit as st

file_list = st.file_uploader("Upload Style Reco File", accept_multiple_files=True)

excl_list = []

for file in file_list:
	excl_list.append(pd.read_excel(file))

# create a new dataframe to store the
excl_merged = pd.DataFrame()

for excl_file in excl_list:

	excl_merged = excl_merged.append(excl_file, ignore_index=True)

else:
	st.info(
            f"""
                👆 Upload a .xlsx file)
                """

       )

excl_merged.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend.xlsx')

df1 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend.xlsx",skiprows=5)
	
	
	
excl_merged = excl_merged.iloc[: , 3:]

excl_merged[]

df1=pd.read_excel(excl_merged)
df1.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx')

df2 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx")

grouper12 = excl_merged.groupby(['Item Group','Item Code','Proc Group','Description','Colour Size'])

stylereco = grouper12['Tot Req','Order Qty','GRN Qty','PUT Qty','REC in Qty','REC out Qty','MO Issue Quantity','RO Issue Quantity','Balance Qty','Balance Value'].sum().reset_index()

