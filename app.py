

import pandas as pd
import streamlit as st


uploaded_file = st.file_uploader(
        "",key="1"
        )
				
if uploaded_file is not None:
	#file_container = st.expander("Check your uploaded .csv")
	df = pd.read_excel(uploaded_file)
	uploaded_file.seek(0)
	head = df.head()
	st.write(head)
	
	excl_list = []
	
	for uploaded_file in df:
    		df.append(pd.read_excel(uploaded_file))
		
else:
	st.info(
            f"""
                👆 Upload a .xlsx file)
                """

        )

	st.stop()


# import glob
# import pandas as pd

# # specifying the path to csv files
# path = r""

# # csv files in the path
# file_list = glob.glob(path + r"C:\Users\srikanthve\Desktop\Style Reco\*.xlsx")

# excl_list = []

# for file in file_list:
#     excl_list.append(pd.read_excel(file))

# # create a new dataframe to store the
# excl_merged = pd.DataFrame()

# for excl_file in excl_list:

#     # appends the data into the excl_merged
#     # dataframe.
#     excl_merged = excl_merged.append(
#       excl_file, ignore_index=True)

# excl_merged.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend.xlsx')

# df1 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend.xlsx",skiprows=5)

# df1 = df1.iloc[: , 3:]

# df1.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx')

# df2 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\stylerecoappend_final.xlsx")

# grouper12 = df1.groupby(['Item Group','Item Code','Proc Group','Description','Colour Size'])

# stylereco = grouper12['Tot Req','Order Qty','GRN Qty','PUT Qty','REC in Qty','REC out Qty','MO Issue Quantity','RO Issue Quantity','Balance Qty','Balance Value'].sum().reset_index()

# stylereco['Tot Req']=pd.to_numeric(stylereco["Tot Req"],errors="ignore")
# stylereco['Order Qty']=pd.to_numeric(stylereco["Order Qty"],errors="ignore")
# stylereco['GRN Qty']=pd.to_numeric(stylereco["GRN Qty"],errors="ignore")
# stylereco['PUT Qty']=pd.to_numeric(stylereco["PUT Qty"],errors="ignore")
# stylereco['REC in Qty']=pd.to_numeric(stylereco["REC in Qty"],errors="ignore")
# stylereco[' REC out Qty']=pd.to_numeric(stylereco["REC out Qty"],errors="ignore")
# stylereco['MO Issue Quantity']=pd.to_numeric(stylereco["MO Issue Quantity"],errors="ignore")
# stylereco['RO Issue Quantity']=pd.to_numeric(stylereco["RO Issue Quantity"],errors="ignore")


# stylereco = stylereco[(stylereco["Proc Group"]=="FAB")]
# stylereco = stylereco[(stylereco["Order Qty"] > 0)]
# stylereco = stylereco[(stylereco["Tot Req"] > 0)]

# stylereco['Total Input'] = stylereco['PUT Qty'] + stylereco['REC in Qty'] + stylereco['REC out Qty']
# stylereco['Excess Order'] = stylereco['Order Qty']-stylereco['Tot Req']
# stylereco['Excess Recieved'] = stylereco['GRN Qty']-stylereco['Order Qty']
# stylereco['Production Savings'] = stylereco['Tot Req']-stylereco['MO Issue Quantity']+stylereco['RO Issue Quantity']
# stylereco['Net Reclassification'] = stylereco['Balance Qty']-(stylereco['Excess Order']+stylereco['Excess Recieved']+stylereco['Production Savings'])

# stylereco.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\output_final.xlsx')

# import glob
# import pandas as pd

# # specifying the path to csv files
# path = r""

# # csv files in the path
# file_list = glob.glob(path + r"C:\Users\srikanthve\Desktop\YY\yy*.xlsx")

# excl_list = []

# for file in file_list:
#     excl_list.append(pd.read_excel(file))

# # create a new dataframe to store the
# excl_merged1 = pd.DataFrame()

# for excl_file in excl_list:

#     # appends the data into the excl_merged
#     # dataframe.
#     excl_merged1 = excl_merged1.append(
#       excl_file, ignore_index=True)


# excl_merged1.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\yyappend.xlsx')

# df2 = pd.read_excel(r"C:\Users\srikanthve\Desktop\Style Reco Output\yyappend.xlsx",skiprows=14)

# df2.rename(columns = {'Material Item':'Item Code'}, inplace = True)

# df2["Wastage %"] = df2["Wastage %"].str.rstrip("%").astype("float") / 100

# yy = df2.groupby(['Item Code','Unit of Measure']).agg({'CO Qty':'sum','Cut Qty':'sum','Shipped Qty':'sum','Standard Consumption':'mean','Actual Consumption':'mean','Wastage %':'mean'}).reset_index()

# yy_merge =  pd.merge(stylereco,yy , how='inner', on='Item Code')

# yy_merge.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\finaloutput.xlsx')

# df3 = pd.read_excel(r"C:\Users\srikanthve\Desktop\SWRM\swrm.xlsm",skiprows=1,sheet_name='Data')

# df3.rename(columns = {'MATERIAL_ITEM':'Item Code'}, inplace = True)

# df4=df3[(df3['LTYPE']=='MOP')]

# grouper4 = df4.groupby(['STYLE','Item Code','LTYPE','UOM'])

# df3_swrm = grouper4['REQUIRED_'].sum().reset_index()

# swrm_merge=pd.merge( yy_merge,df3_swrm ,how='left', on='Item Code')

# swrm_merge.to_excel(r'C:\Users\srikanthve\Desktop\Style Reco Output\finaloutput_swrm.xlsx')

# head=swrm_merge

# st.write(head)


# def convert_df(swrm_merge):
#     return swrm_merge.to_csv().encode('utf-8')


# csv = convert_df(swrm_merge)

# st.download_button(
#     "Download",
#     csv,
#     "riskassess.csv",
#     "text/csv",
#     key='browser-data'
# )




