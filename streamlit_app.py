import streamlit as st
import pandas as pd

st.write("""
# Universal Orlando Waittimes
""")

locations = pd.read_excel('locations.xlsx')

st.write(locations)
st.map(locations, size=8)

df = pd.read_csv('wait.csv')

attractions = list(locations['attraction'].unique())
attraction = st.selectbox('Attraction', attractions)

st.write(df[attraction].describe())
