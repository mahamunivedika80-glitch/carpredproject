import streamlit as st
import pandas as pd
import pickle as pkl
import math

pipe = pkl.load(open("CPP.pkl","rb+"))
st.title('car price prediction project')
df = pd.read_csv('clean_data.csv')
arr = sorted(df['company'].unique())
company = st.selectbox("enter company",arr)
names = sorted(df[df['company']==company]['name'].unique())
name = st.selectbox("enter car name",names)
year = st.number_input("enter year",min_value=2005,max_value=2026)
kms_driven= st.number_input("enter kilometers",min_value=500)
fuel_types=sorted(df[df['name']==name]['fuel_type'].unique())
fuel_type= st.selectbox("enter fuel type",fuel_types)
if(st.button("submit")):
    inputdata=pd.DataFrame(data=[[name,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type'])
    result=pipe.predict(inputdata)
    result=result[0,0]
    value=math.ceil(result)
    st.text(f"${value:,}")