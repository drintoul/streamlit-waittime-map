import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.info('Averages from July 2021-2023. Data from thrill-data.com', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

st.dataframe(locations[locations['attraction'] == attraction], hide_index=True)

st.write(df[attraction].describe())

st.map(locations, size=8)

df = pd.read_csv('wait.csv')
df = df.round(0)

st.dataframe(df[['time', attraction]], hide_index=True)

#chart_data = df[attraction]
#st.line_chart(chart_data)


