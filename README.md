# Mini-projeto_Claudineia_Turma-Analise_de_Dados_T1
## Mini-Projeto Avaliativo - Módulo 1 - Semana 07

Auna: Claudineia Ferrira
Turma: Análise De Dados T1

## Fonte: kaggle - Base Varejo
<>https://www.kaggle.com/datasets/namespaiva/base-varejo/data

## Objetivo
Este Mini-Projeto realiza uma **Análise Exploratória de Dados (AED)** utilizando as bibliotecas **Python, Pandas e NumPy**, com o objetivo de compreender a estrutura da base de dados, identificar problemas de qualidade, realizar tratamentos necessários e preparar os dados para futuras análises.

## Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy



---

## Arquivos do Projeto

```text
Base_Varejo.csv     -> Base de dados original
aed.py              -> Script principal da análise
df_limpo.csv        -> Base tratada e exportada
README.md           -> Documentação do projeto
```

---

## Etapas Desenvolvidas

### 1. Carregamento dos Dados

Leitura da base utilizando Pandas.

```python
df = pd.read_csv("Base_Varejo.csv", sep=";")
```

---
### Lista de campos existentes na base de dados 

1. DATA: Data da compra; 
2. CO_ID: Identificação do número de compra (número da nota fiscal); 
3. CL_ID: Identificação do cliente (número do cliente); 
4. CL_GENERO: Sexo biológico informado pelo cliente; 
2 
5. CL_EC: Estado civil do cliente: 
1: Casado ou união estával; 
2: Divorciado; 
3: Separado; 
4. Solteiro; 
5: Viúvo. 
6. CL_FHL: Número de filhos do cliente; 
7. CL_SEG: Segmentação econômica do cliente (classe A, B ou C); 
8. PR_ID: Código do produto (SKU) adquirido; 
9. PR_CAT: Categoria do produto adquirido; 
10. PR_NOME: Nome do produto adquirido.


---

### 2. Exploração Inicial

Foram analisados:

- Quantidade de registros;
- Quantidade de colunas;
- Tipos de dados;
- Primeiras linhas da base;
- Últimas linhas da base.

Funções utilizadas:

```python
df.info()
df.head()
df.tail()
df.shape
df.dtypes
```

---

### 3. Diagnóstico da Qualidade dos Dados

Foram identificados:

- Valores nulos;
- Registros duplicados;
- Colunas vazias (Unnamed);
- Valores inconsistentes representados por "#N/D".

---

### 4. Tratamento dos Dados

Foram realizadas as seguintes etapas:

#### Remoção de colunas vazias

```python
df.dropna(axis=1, how="all")
```

#### Remoção de duplicatas

```python
df.drop_duplicates()
```

#### Conversão de "#N/D" para NaN

```python
df.replace("#N/D", np.nan)
```

#### Tratamento da coluna CL_FHL

Os valores ausentes foram preenchidos utilizando a mediana.

```python
df["CL_FHL"].fillna(mediana_filhos)
```

#### Conversão da coluna DATA

```python
pd.to_datetime(df["DATA"])
```

#### Padronização dos identificadores

As colunas CO_ID e CL_ID foram convertidas para texto para evitar perda de informação.

#### Padronização de textos

Foram removidos espaços extras e aplicada formatação padrão.

```python
str.strip()
str.title()
```

---

### 5. Exportação da Base Tratada

Após a limpeza e padronização dos dados, foi gerado um novo arquivo:

```python
df.to_csv("df_limpo.csv", index=False, encoding="utf-8-sig")
```

Arquivo gerado:

```text
df_limpo.csv
```

---

### 6. Estatística Descritiva

Foram calculadas estatísticas gerais da base através de:

```python
df.describe()
```

Também foram calculadas medidas específicas para a variável **CL_FHL**:

- Média;
- Mediana;
- Moda;
- Desvio padrão;
- Mínimo;
- Máximo;
- Quartis.

---

## Resultados Obtidos

Durante a análise foi possível identificar:

- Existência de registros duplicados;
- Presença de valores ausentes;
- Colunas vazias geradas por problemas de importação;
- Necessidade de padronização de tipos de dados;
- Necessidade de tratamento de dados inconsistentes.

Após a limpeza, a base ficou adequada para análises futuras.

---

## Conclusão

A Análise Exploratória de Dados permitiu identificar e corrigir problemas de qualidade presentes na base de varejo.

Os tratamentos aplicados melhoraram a consistência dos dados, possibilitando a utilização da base em análises estatísticas, dashboards e futuros projetos de Ciência de Dados.

