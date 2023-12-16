import streamlit as st
import pandas as pd

st.title("""Universal Studios Wait Times""")

st.info('Averages from July 2021-2023. Data from thrill-data.com', icon='ℹ️')

locations = pd.read_excel('locations.xlsx')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

df = pd.read_csv('wait.csv')
df = df.round(0)

col1, col2 = st.columns(2)
col1.write(df[attraction].describe())
col2.dataframe(df[['time', attraction]], hide_index=True)

st.map(locations, size=8)
st.dataframe(locations[locations['attraction'] == attraction], hide_index=True)

#chart_data = df[attraction]
#st.line_chart(chart_data)

style = df.style.hide_index()
style.hide_columns()
st.write(style.to_html(), unsafe_allow_html=True)
