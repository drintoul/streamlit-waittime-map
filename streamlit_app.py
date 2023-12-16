import streamlit as st
import pandas as pd

df = pd.read_excel('locations.xlsx')

#st.write(df)

st.write("""
# Universal Orlando Waittimes
""")

st.map(df, size=8)
