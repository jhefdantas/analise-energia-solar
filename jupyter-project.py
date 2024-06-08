# Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
base_prod = pd.read_csv('data_prod.csv')

# Visualizando estatísticas descritivas dos dados
base_prod.describe().round(2)

# Pré-processamento dos dados
## Calculando a média e o desvio padrão para cada mês
media = base_prod.loc[:, 'Janeiro': 'Dezembro'].mean()
std = base_prod.loc[:, 'Janeiro': 'Dezembro'].std()

## Subtraindo a média pelo desvio padrão para cada mês
resultado = media - std

## Identificando as linhas onde o valor de qualquer mês é igual ou abaixo do valor correspondente em 'resultado'
mask = base_prod.loc[:, 'Janeiro': 'Dezembro'].le(resultado)

## Removendo essas linhas do dataframe
base_prod_new = base_prod.loc[~mask.any(axis=1)]

# Processamento dos dados
## Calculando a nova média para cada mês sem as linhas removidas
new_media = base_prod_new.loc[:, 'Janeiro': 'Dezembro'].mean()

## Selecionando as linhas que precisam ser substituídas
rows_to_replace = base_prod[mask.any(axis=1)]

## Substituindo os valores nessas linhas pela nova média
rows_to_replace.loc[:, 'Janeiro': 'Dezembro'] = rows_to_replace.loc[:, 'Janeiro': 'Dezembro'].apply(lambda x: new_media, axis=1)

## Concatenando o dataframe original (sem as linhas substituídas) com o dataframe das linhas substituídas
base_prod_final = pd.concat([base_prod_new, rows_to_replace])

## Preenchendo os valores nulos com a nova média
base_prod_final_filled = base_prod_final.fillna(new_media)

# Visualizando estatísticas descritivas dos dados processados
base_prod_final_filled.describe().round(2)

# Limpeza dos dados
## Removendo as linhas com valores nulos em 'Orientação' e/ou 'Telhado'
base_prod_final_filled_clean = base_prod_final_filled.dropna(subset=['Orientação', 'Telhado'])

# Análise dos dados
## Agrupando por 'Telhado' e 'Orientação' e calculando a média de 'Produtividade'
media_prod = base_prod_final_filled.groupby(['Telhado', 'Orientação'])['Produtividade'].mean().round(2)

## Contando o número de projetos em cada categoria
count_projetos = base_prod_final_filled.groupby(['Telhado', 'Orientação']).size()

## Criando um novo DataFrame com 'media_prod' e 'count_projetos'
df_final = pd.concat([media_prod, count_projetos], axis=1)

## Renomeando as colunas
df_final.columns = ['Média de Produtividade', 'Número de Projetos']

## Criando novos DataFrames com linhas onde 'Número de Projetos' é 10 ou mais e 'Média de Produtividade' é maior que 100
df_final_10 = df_final[df_final['Número de Projetos'] >= 10]
df_final_prod_100 = df_final[df_final['Média de Produtividade'] > 100]

# Visualização dos dados
## Resetando o índice para usar 'Telhado' e 'Orientação' como colunas
df_final_prod_100_reset = df_final_prod_100.reset_index()
df_final_reset = df_final.reset_index()

## Gráfico de barras para 'Média de Produtividade'
plt.figure(figsize=(10, 6))
sns.barplot(x='Telhado', y='Média de Produtividade', hue='Orientação', data=df_final)
plt.title('Média de Produtividade por Telhado e Orientação')
plt.show()

## Gráfico de barras para 'Número de Projetos'
plt.figure(figsize=(10, 6))
sns.barplot(x='Telhado', y='Número de Projetos', hue='Orientação', data=df_final)
plt.title('Número de Projetos por Telhado e Orientação')
plt.show()

## Heatmap para 'Média de Produtividade'
prod_pivot = df_final_reset.pivot(index='Telhado', columns='Orientação', values='Média de Produtividade')
sns.heatmap(prod_pivot, annot=True, fmt=".1f")
plt.title('Média de Produtividade por Telhado e Orientação')
plt.show()

## Heatmap para 'Número de Projetos'
proj_pivot = df_final_reset.pivot(index='Telhado', columns='Orientação', values='Número de Projetos')
sns.heatmap(proj_pivot, annot=True, fmt=".0f")
plt.title('Número de Projetos por Telhado e Orientação')
plt.show()