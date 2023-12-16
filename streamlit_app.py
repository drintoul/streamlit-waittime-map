import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.info('Averages for July past 3 years (2021-2023). Data from thrill-data.com', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

jan_data = pd.read_csv('wait_jan.csv').round(0)
jan_data = jan_data[['time', f'{attraction}']]

jul_data = pd.read_csv('wait_jul.csv').round(0)
jul_data = jul_data[['time', f'{attraction}']]

col1, col2 = st.columns(2)
with col1:
  st.dataframe(jul_data[['time', f'{attraction}']], hide_index=True)
with col2:
  st.line_chart(data = jul_data, x='time')

locations.loc['attraction' == f'attraction', 'color'] = '#00FF00'

col1, col2 = st.columns(2)
with col1:
  st.map(locations, size=8, color='color')
with col2:
  st.write(jul_data[f'{attraction}'].describe())
