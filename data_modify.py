import pandas as pd

# --- I. Leitura da base --- #
df = pd.read_excel('base_dantas.xlsx')

# Imprimir primeiras 5 linhas
print(df.head())


# --- II. Criar colunas MÉDIA (KWH_MEAN) e PROD - PRODUTIVIDADE (KWH_MEDIA / KWP) --- #

# Selecionar colunas de janeiro a dezembro
meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

# Verificar se qualquer valor nas colunas dos meses é 0, NaN ou None
mask = df[meses].isin([0, pd.NA, None]).any(axis=1)

# Excluir as linhas onde qualquer valor nas colunas dos meses é 0, NaN ou None
df = df[~mask]

# Calcular a média dos meses para cada linha e adicionar como nova coluna 'KWH_MEDIA'
df['KWH_MEDIA'] = df[meses].mean(axis=1).round(2)

# Calcular a coluna 'PROD' dividindo 'KWH_MEAN' por 'KWP'
df['PRODUTIVIDADE'] = (df['KWH_MEDIA'] / df['KWP']).round(2)

# Imprime as primeiras linhas após a adição das novas colunas
print(df.head())

def preencher_valores_faltantes(grupo):
    # Para cada coluna:
    for coluna in ['ORIENTACAO', 'KWP', 'TELHADO']:
        # Encontra o primeiro valor válido na coluna
        primeiro_valor_valido = grupo[coluna].first_valid_index()
        if primeiro_valor_valido is not None:
            # Preenche os valores faltantes com o valor do primeiro valor válido encontrado no grupo
            grupo[coluna].fillna(grupo.loc[primeiro_valor_valido, coluna], inplace=True)
    return grupo

def replicar_potencia(df):
    # Primeiro, vamos garantir que o DataFrame esteja ordenado pelo ID da usina e pela Geração
    df.sort_values(by=['ID USINA', 'GERACAO'], inplace=True)
    
    # Agora, vamos preencher os valores faltantes para cada grupo de ID USINA
    df = df.groupby('ID USINA').apply(preencher_valores_faltantes).reset_index(drop=True)
    
    return df

# 'df' é o DataFrame
df = replicar_potencia(df)

# Imprime as primeiras linhas após a replicação
print(df.head())

# Criar um novo arquivo (.csv) com os dados atualizados
df.to_csv('data_atualizado.csv', index=False)

# Criar um novo arquivo (.xlsx) com os dados atualizados
df.to_excel('data_atualizado.xlsx', index=False)
