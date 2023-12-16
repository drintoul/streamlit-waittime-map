import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.subheader("""Averages from July 2021-2023
Data from thrill-data.com""")

st.info('Purpose of this project was to get experience using interactive streamlit controls, specifically with map and time widgets', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

#st.dataframe(locations[locations['attraction'] == attraction], hide_index=True)

#st.map(locations, size=8)

df = pd.read_csv('wait.csv')
df['time'] = df['time'].round(0)

st.dataframe(df[['time', attraction]], hide_index=True)

#chart_data = df[attraction]
#st.line_chart(chart_data)

#st.write(df[attraction].describe())
