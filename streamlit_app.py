import streamlit as st
import pandas as pd

st.write("""
# Universal Orlando Waittimes
""")

locations = pd.read_excel('locations.xlsx')

#st.write(locations)
st.map(locations, size=8)

df = pd.read_csv('wait.csv')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

chart_data = df[attraction]
st.line_chart(chart_data)

st.write(df[attraction].describe())
