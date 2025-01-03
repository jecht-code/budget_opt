import streamlit as st
import pandas as pd

st.title('budget optimizer')

st.write('Hellow World!')

#Show case DataFrame - to ensure data is ingested into Streamlit.
df = pd.read_csv('DataSet_Streamlit.csv')

#Make a drop down that filters said dataframe.
# Create the dropdown
# Added "All" so it views all lists in the data frame.
options = ['All'] + sorted(df['Brand'].unique().tolist())
selected_category = st.selectbox('Select Brand:', options)

#follow AI, Added if statement to add filter to dataframe.
if selected_category == 'All':
        filtered_df = df
else:
        filtered_df = df[df['Brand'] == selected_category]

# Display the filtered DataFrame
st.dataframe(filtered_df, hide_index=True)
