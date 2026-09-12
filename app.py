import streamlit as st
import pandas as pd
dic={"age":[10,20,30]}
code='''
#include <math.h>
'''

st.code(code,language="c")
df=pd.DataFrame(dic)
st.title("Sales dashboard")
st.markdown("Revenue is  up 12%  this quarter.")
st.write({"users": 1280, "growth": 0.12}) # auto-formats
st.dataframe(df)
st.metric("Revenue", "$48.2k", "+12%")
st.line_chart(df)