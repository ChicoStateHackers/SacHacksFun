import pandas as pd
import numpy as np
csv_url = 'https://www.hudexchange.info/resources/documents/2007-2014-PIT-Counts-by-State.xlsx'
df = pd.ExcelFile(csv_url)
sheet_num1 = '2013'
sheet_num2 = '2014'
State1 = 'CA'
State2 = 'CA'
df1 = pd.read_excel(df,sheet_num1)
df2 = pd.read_excel(df,sheet_num2)
States_1 = df1.ix[:,0]
States_2 = df2.ix[:,0]
Pop_1 = df1.ix[:,1]
Pop_2 = df2.ix[:,1]
usable1 = {'States': df1.ix[:,0], 'Population': df1.ix[:,1]}
df_usable1 = pd.DataFrame(data=usable1)
usable2 = {'States': df2.ix[:,0], 'Population': df2.ix[:,1]}
df_usable2 = pd.DataFrame(data=usable2)
data1 = df_usable1.loc[df_usable1['States'] == State1]
data2 = df_usable2.loc[df_usable2['States'] == State2]
print(data1)
print(data2)
