import streamlit as st
import pandas as pd

st.title("Nacimientos en Colombia en los Últimos 10 años, segun DANE")

data = {
    "Año": [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    "Nacimientos": [647521,656704,649115,642660,629402,616914,573625,515549,453901,433678]
}

df = pd.DataFrame(data)
df = df.set_index("Año")

st.line_chart(df) 