import streamlit as st
import pandas as pd

st.header("""
Universal Orlando Waittimes
""")

st.subheader("""Data from July 1st, 2023""")

st.info('Purpose of this project was to get experience using interactive streamlit controls, specifically with map and time widgets', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

st.write(locations)
st.map(locations, size=8)

df = pd.read_csv('wait.csv')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

#chart_data = df[attraction]
#st.line_chart(chart_data)

st.write(df[attraction].describe())
