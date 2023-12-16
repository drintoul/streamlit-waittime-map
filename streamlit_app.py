import streamlit as st
import pandas as pd

locations = pd.read_excel('locations.xlsx')

#st.write(df)

st.write("""
# Universal Orlando Waittimes
""")

st.map(locations, size=8)

df = pd.read_csv('wait.csv')

attractions = list(locations.unique())
attraction = st.selectbox('Attraction', attractions)

st.write(df[attraction].describe())
