import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.info('Averages for July past 3 years (2021-2023). Data from thrill-data.com', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

df = pd.read_csv('wait.csv')
df = df.round(0)

chart_data = df[f'{attraction}']

col1, col2 = st.columns(2)
col1.dataframe(df[['time', f'{attraction}']], hide_index=True)
col2.line_chart(chart_data)

col1, col2 = st.columns(2)
col1.map(locations, size=8)
col2.dataframe(locations[locations['attraction'] == f'{attraction}'], hide_index=True)
col2.write(df[f'{attraction}'].describe().T)
