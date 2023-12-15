import streamlit as st
import pandas as pd

df = pd.read_excel('locations.xlsx')

st.write("""
# Universal Orlando Waittimes
""")

st.write(df)

st.map(df, size=20)
