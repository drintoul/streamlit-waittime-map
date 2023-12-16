import streamlit as st
import pandas as pd

df = pd.read_excel('locations.xlsx')

#st.write(df)

st.write("""
# Universal Orlando Waittimes
""")

st.map(df, size=8)

attraction = st.sidebar.selectbox('Attraction', df.unique())

st.write(df[attraction].describe())
