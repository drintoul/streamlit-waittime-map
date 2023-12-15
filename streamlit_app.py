import streamlit as st
import pandas as pd

df = pd.read_excel('locations.xlsx')

st.write("""
# Universal Orlando Waittimes
""")

#st.write(df)

st.map(df, size=10)

#st.map(data=None, latitude=28.358, longitude=81.59, color=None, size=None, zoom=None, use_container_width=True)
