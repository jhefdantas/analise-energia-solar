import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Certifique-se de que o arquivo CSV está no diretório correto
df = pd.read_csv("data_atualizado.csv", sep=",", decimal=",")

# Seleção da geração
ger = st.sidebar.selectbox("Geração", df["GERACAO"].unique())

# Filtragem do DataFrame com base na geração selecionada
df_filtered = df[df["GERACAO"] == ger]

# Criação de colunas para exibição dos gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


df_filtered

# Contagem de projetos por tipo de telhado
df_telhado_count = df_filtered.groupby('TELHADO').size().reset_index(name='TOTAL')

# Contagem de projetos por orientação
df_orientacao_count = df_filtered.groupby('ORIENTACAO').size().reset_index(name='TOTAL')

# Cálculo da média da produtividade por tipo de telhado e orientação
df_produtividade_max = df_filtered.groupby(['TELHADO', 'ORIENTACAO'])['PRODUTIVIDADE'].max().reset_index()

# Criação dos gráficos
fig_tel = px.bar(df_telhado_count, x="TELHADO", y="TOTAL", title="Projetos por Tipo de Telhado")
col1.plotly_chart(fig_tel)

fig_orien = px.bar(df_orientacao_count, x="ORIENTACAO", y="TOTAL", title="Projetos por Tipo de Orientação")
col2.plotly_chart(fig_orien)

fig_produtividade = px.scatter(df_produtividade_max, x="TELHADO", y="PRODUTIVIDADE", color="ORIENTACAO", title="Produtividade Máxima por Tipo de Telhado e Orientação")
col3.plotly_chart(fig_produtividade)
