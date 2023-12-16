import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.info('Averages for July past 3 years (2021-2023). Data from thrill-data.com', icon='ℹ️')

# Read Locations' GPS coordinates and default marker colors
locations = pd.read_excel('locations.xlsx')

# Build list of Attractions for drop-down
attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

# Load data for January and July for past 3 years
jan_data = pd.read_csv('wait_jan.csv').round(0)
jan_data = jan_data[['time', f'{attraction}']]

jul_data = pd.read_csv('wait_jul.csv').round(0)
jul_data = jul_data[['time', f'{attraction}']]

# Display wait time dataframe and line chart side-by-side
col1, col2 = st.columns(2)
with col1:
  st.dataframe(jul_data[['time', f'{attraction}']], hide_index=True)
with col2:
  st.line_chart(data = jul_data, x='time')

# Change marker color on map depending on which Attraction is selected
locations[locations['attraction'] != f'attraction']['color'] = '#000000'
locations[locations['attraction'] == f'attraction']['color'] = '#FF0000'

# Display map and statistics side-by-side
col1, col2 = st.columns(2)
with col1:
  st.map(locations, size=8, color='color')
with col2:
  st.write(jul_data[f'{attraction}'].describe())

# Inform user that work is incomplete
st.info('Interactivity with map and timetable still to come!', icon='ℹ️')
