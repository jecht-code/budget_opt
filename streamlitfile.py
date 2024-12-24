import streamlit as st
import pandas as pd

st.title('budget optimizer')

st.write('Hellow World!')

df = pd.read_excel('https://github.com/jecht-code/budget_opt/blob/main/DataSet_Streamlit.xlsx')
df