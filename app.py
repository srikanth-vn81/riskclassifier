

import pandas as pd
import streamlit as st

file_list = st.file_uploader("Upload Style Reco File", accept_multiple_files=True)
excl_list = []
for file in file_list:
	excl_list.append(pd.read_excel(file))
excl_merged = pd.DataFrame()

excl_merged[]
for excl_file in excl_list:
	excl_merged = excl_merged.append(excl_file, ignore_index=True)

	
excl_merged = excl_merged.iloc[: , 3:]



df1=pd.read_excel(excl_merged)

df1.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx')

df2 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx")

grouper12 = excl_merged.groupby(['Item Group','Item Code','Proc Group','Description','Colour Size'])

stylereco = grouper12['Tot Req','Order Qty','GRN Qty','PUT Qty','REC in Qty','REC out Qty','MO Issue Quantity','RO Issue Quantity','Balance Qty','Balance Value'].sum().reset_index()

stylereco['Tot Req']=pd.to_numeric(stylereco["Tot Req"],errors="ignore")
stylereco['Order Qty']=pd.to_numeric(stylereco["Order Qty"],errors="ignore")
stylereco['GRN Qty']=pd.to_numeric(stylereco["GRN Qty"],errors="ignore")
stylereco['PUT Qty']=pd.to_numeric(stylereco["PUT Qty"],errors="ignore")
stylereco['REC in Qty']=pd.to_numeric(stylereco["REC in Qty"],errors="ignore")
stylereco[' REC out Qty']=pd.to_numeric(stylereco["REC out Qty"],errors="ignore")
stylereco['MO Issue Quantity']=pd.to_numeric(stylereco["MO Issue Quantity"],errors="ignore")
stylereco['RO Issue Quantity']=pd.to_numeric(stylereco["RO Issue Quantity"],errors="ignore")


stylereco = stylereco[(stylereco["Proc Group"]=="FAB")]
stylereco = stylereco[(stylereco["Order Qty"] > 0)]
stylereco = stylereco[(stylereco["Tot Req"] > 0)]

stylereco['Total Input'] = stylereco['PUT Qty'] + stylereco['REC in Qty'] + stylereco['REC out Qty']
stylereco['Excess Order'] = stylereco['Order Qty']-stylereco['Tot Req']
stylereco['Excess Recieved'] = stylereco['GRN Qty']-stylereco['Order Qty']
stylereco['Production Savings'] = stylereco['Tot Req']-stylereco['MO Issue Quantity']+stylereco['RO Issue Quantity']
stylereco['Net Reclassification'] = stylereco['Balance Qty']-(stylereco['Excess Order']+stylereco['Excess Recieved']+stylereco['Production Savings'])

stylereco.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\output_final.xlsx')

def convert_df(stylereco):
    return stylereco.to_csv().encode('utf-8')


csv = convert_df(stylereco)

st.download_button(
    "Download Style Reco",
    csv,
    "stylerecoappend.csv",
    "text/csv",
    key='browser-data'
)		

