import pandas as pd

# Ler arquivo
df = pd.read_excel('base_dantas.xlsx')

# Imprime as primeiras linhas para verificar
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

