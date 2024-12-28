import streamlit as st
import pandas as pd

st.title('budget optimizer')

st.write('Hellow World!')

df = pd.read_csv('DataSet_Streamlit.csv')

df
