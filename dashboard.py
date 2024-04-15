import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data_atualizado.csv", sep=",", decimal=",")

ger = st.sidebar.selectbox("Geração", df["GERACAO"].unique())

df_filtered = df[df["GERACAO"] == ger]
df_filtered 

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


fig_ger = px.bar(df, x="ORIENTACAO", y=df_filtered, color="GERACAO", title="Projetos por geração")
col1.plotly_chart(fig_ger)