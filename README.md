
# EFICIÊNCIA ENERGÉTICA EM PLACAS SOLARES: ANÁLISE PARA REDUÇÃO DE CUSTOS
 
Este projeto acadêmico é um script Python para análise e visualização de dados de produtividade energética. Ele utiliza bibliotecas como pandas, seaborn e matplotlib para processar e visualizar dados de um arquivo CSV.


## Primeiros Passos

Para obter uma cópia local e rodar o projeto, siga estes passos simples.

### Pré-requisitos

Este projeto requer Python e as seguintes bibliotecas Python instaladas:

* pandas
* seaborn
* matplotlib

Você pode instalar esses pacotes usando pip:



```bash
  pip install pandas seaborn matplotlib
```

## Instalação

#### 1. Clone o repositório:

```bash
  git clone https://github.com/jhefdantas/analise-energia-solar.git
```

#### 2. Execute o script:

```bash
  python jupyter-project.py
```

### Uso
O script realiza as seguintes tarefas:

* #### Carregamento de Dados: 
    Carrega um arquivo CSV chamado 'data_prod.csv' em um DataFrame do pandas.

* #### Pré-processamento de Dados:
    Calcula a média e o desvio padrão para cada mês. Subtrai o desvio padrão da média para cada mês. Identifica e remove as linhas onde o valor de qualquer mês é igual ou inferior ao valor resultante da subtração.
* #### Processamento de Dados: 
    Calcula uma nova média para cada mês sem as linhas removidas.Substitui os valores nas linhas identificadas pela nova média. Concatena o DataFrame original (sem as linhas removidas) com o DataFrame das linhas substituídas. Preenche valores nulos com a nova média.

* #### Limpeza de Dados: 
    Remove linhas com valores nulos em 'Orientação' e/ou 'Telhado'.
* #### Análise de Dados:
    Agrupa por 'Telhado' e 'Orientação' e calcula a média de 'Produtividade'.
    Conta o número de projetos em cada categoria.
    Cria um novo DataFrame com 'Média de Produtividade' e 'Número de Projetos'.
    Filtra dados onde 'Número de Projetos' é 10 ou mais e 'Média de Produtividade' é maior que 100.

* #### Visualização de Dados: 
    Cria gráficos de barras e heatmaps para visualizar a média de produtividade e o número de projetos por 'Telhado' e 'Orientação'.


## Autores

- [@jhefdantas](https://www.github.com/jhefdantas)

