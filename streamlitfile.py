import streamlit as st
import pandas as pd

st.title('budget optimizer')

st.write('Hellow World!')

# Create number input with min and max values
number = st.number_input('Enter your budget between $100,000 and $100,000,000:',
    min_value=100_000,
    max_value=100_000_000,
    value=100_000,  # Default value
    step=1000,      # Step size for increment/decrement
    format="%d"    # Added $ to the format string
)

# Display the entered value
st.write(f'You entered: ${number:,.2f}')  # Adding $ symbol, thousand separators, and 2 decimal places

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
