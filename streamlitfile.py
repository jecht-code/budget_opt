import streamlit as st
import pandas as pd

st.title('budget optimizer')

st.write('Hellow World!')

#Show case DataFrame - to ensure data is ingested into Streamlit.
df = pd.read_csv('DataSet_Streamlit.csv')

#Make a drop down that filters said dataframe.
# Create the dropdown
options = df['Brand'].unique().tolist()
selected_category = st.selectbox('Select Brand:', options)

# Filter the DataFrame
filtered_df = df[df['Brand'] == selected_category]

# Display the filtered DataFrame
st.dataframe(filtered_df)
