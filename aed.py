# ==============================================================================
# MINI-PROJETO: ANÁLISE EXPLORATÓRIA DE DADOS (AED)
# Aluna: Claudinéa Ferreira
# Turma: Análise de Dados - T1
# ==============================================================================
import numpy as np
import pandas as pd

# ==============================================================================
# CARREGAMENTO DOS DADOS
# ==============================================================================
print("=" * 60)
print("BASE DE DADOS VAREJO")
print("=" * 60)

# Carrega o arquivo original da base de dados
df = pd.read_csv("Base_Varejo.csv", sep=";")

# ==============================================================================
# INFORMAÇÕES GERAIS DA BASE
# ==============================================================================
print("\n" + "=" * 60)
print("INFORMAÇÕES GERAIS DA BASE")
print("=" * 60)

# Apresenta informações gerais do DataFrame
df.info()

# Visualiza as primeiras e últimas 8 linhas
print("\nPrimeiras 8 linhas da base:")
print(df.head(8))

print("\nÚltimas 8 linhas da base:")
print(df.tail(8))

# ==============================================================================
# ESTRUTURA E TIPOS DE DADOS
# ==============================================================================
print("\n" + "=" * 60)
# Exibe a forma (shape) e estrutura dos dados
print(f"Quantidade de linhas: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\nNomes das colunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

# ==============================================================================
# ANÁLISE DOS DADOS (NULOS E DUPLICADOS)
# ==============================================================================
print("\n" + "=" * 60)
print("VALORES NULOS")
print("=" * 60)
print(df.isnull().sum())

print("\n" + "=" * 60)
print("DUPLICATAS")
print("=" * 60)
total_duplicados = df.duplicated().sum()
print(f"Quantidade de duplicatas: {total_duplicados}")

# ==============================================================================
# ESTATÍSTICA DESCRITIVA
# ==============================================================================
print("\n" + "=" * 60)
print("ESTATÍSTICAS DAS COLUNAS NUMÉRICAS")
print("=" * 60)
print(df.describe())

# ==============================================================================
# DIAGNÓSTICO DE QUALIDADE E TRATAMENTO DOS DADOS
# ==============================================================================
print("\n" + "=" * 80)
print("DIAGNÓSTICO DE QUALIDADE DOS DADOS")
print("=" * 80)

# ------------------------------------------------------------------------------
# 1. Identificação e Remoção de Colunas Fantasmas (Delimitadores Extras)
# ------------------------------------------------------------------------------
colunas_fantasmas = [col for col in df.columns if "Unnamed" in col]
print(f"Colunas inúteis/fantasmas detectadas: {colunas_fantasmas}")

# Remoção automática de colunas 100% vazias
df = df.dropna(axis=1, how="all")
print(f"Quantidade de colunas após limpeza estrutural: {df.shape[1]}")

# ------------------------------------------------------------------------------
# 2. Remoção de Linhas Duplicadas
# ------------------------------------------------------------------------------
linhas_antes = df.shape[0]
df = df.drop_duplicates()
linhas_depois = df.shape[0]

print("\n--- REMOÇÃO DE DUPLICATAS ---")
print(f"Linhas antes: {linhas_antes}")
print(f"Linhas depois: {linhas_depois}")
print(f"Total de duplicadas removidas: {linhas_antes - linhas_depois}")

# ------------------------------------------------------------------------------
# 3. Tratamento de Valores Nulos Ocultos (#N/D)
# ------------------------------------------------------------------------------
print("\n--- ANÁLISE DE VALORES NULOS E OCULTOS ---")
print("Nulos nativos por coluna antes da padronização:")
print(df.isnull().sum())

# Transforma o texto '#N/D' em valores nulos reais (NaN)
df.replace("#N/D", np.nan, inplace=True)

# Trata a coluna de número de filhos (CL_FHL) com a mediana
if "CL_FHL" in df.columns:
    mediana_filhos = df["CL_FHL"].median()
    df["CL_FHL"] = df["CL_FHL"].fillna(mediana_filhos)
    print("\nValores nulos da coluna 'CL_FHL' tratados com a mediana.")

# ------------------------------------------------------------------------------
# 4. Ajuste e Padronização de Tipos de Dados
# ------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PADRONIZAÇÃO DE TIPOS E TEXTOS")
print("=" * 80)

# Conversão da coluna DATA para datetime nativo
if "DATA" in df.columns:
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
    print("Coluna 'DATA' convertida para datetime de forma bem-sucedida.")

# Força IDs como texto (String/Object) para evitar perda de zeros à esquerda
colunas_id = ["CO_ID", "CL_ID"]
for col_id in colunas_id:
    if col_id in df.columns:
        df[col_id] = df[col_id].astype(str)
print("Identificadores (IDs) convertidos e padronizados como texto.")

# Limpeza e padronização de formatação de strings 
# As  colunas de texto no Pandas geralmente possuem o tipo 'object'
for coluna in df.select_dtypes(include=["object", "string"]).columns:
    if coluna not in colunas_id:  # Evita aplicar transformações de texto em IDs
        df[coluna] = df[coluna].astype(str).str.strip().str.title()
print("Strings limpas (sem espaços extras) e padronizadas em formato Título.")

# =========================
# EXPORTAÇÃO DA BASE LIMPA
# =========================

df.to_csv("df_limpo.csv", index=False, encoding="utf-8-sig")

print("\nBase limpa exportada com sucesso!")

# ==============================================================================
# RESUMO FINAL E ESTATÍSTICA DESCRITIVA
# ==============================================================================

print("\n" + "=" * 80)
print("RESUMO DO DATASET LIMPO")
print("=" * 80)
print(f"Dimensões finais: {df.shape[0]} linhas e {df.shape[1]} colunas.")

print("\nTipos de dados atuais:")
print(df.dtypes)

if "CL_FHL" in df.columns:
    print("\n" + "-" * 80)
    print("ESTATÍSTICA DESCRITIVA BÁSICA: FILHOS (CL_FHL)")
    print("-" * 80)
    dados_filhos = df["CL_FHL"].dropna()

    print(f"Média:         {dados_filhos.mean():.2f}")
    print(f"Mediana:       {dados_filhos.median():.2f}")
    print(f"Moda:          {dados_filhos.mode()[0]}")
    print(f"Desvio Padrão: {dados_filhos.std():.2f}")
    print(f"Mínimo:        {dados_filhos.min()}")
    print(f"Máximo:        {dados_filhos.max()}")

    print("\nQuartis:")
    print(dados_filhos.quantile([0.25, 0.50, 0.75]))

# ---------------------------------------------------------
# 7. AGRUPAMENTOS
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("AGRUPAMENTOS")
print("=" * 60)

# ---------------------------------------------------------
# AGRUPAMENTO POR GÊNERO
# ---------------------------------------------------------

if (
    'CL_GENERO' in df.columns and
    'CO_ID' in df.columns
):

    genero = (
        df.groupby('CL_GENERO')['CO_ID']
        .count()
        .reset_index()
    )

    genero.columns = [
        'Genero',
        'Quantidade_Compras'
    ]

    print("\nCompras por gênero:")
    print(genero)

# ---------------------------------------------------------
# DEFINIR COLUNA DE VALOR
# ---------------------------------------------------------
# AJUSTE O NOME CASO NECESSÁRIO

coluna_valor = 'CO_TOTAL'

# ---------------------------------------------------------
# AGRUPAMENTO POR ESTADO CIVIL
# ---------------------------------------------------------

if (
    'CL_EC' in df.columns and
    coluna_valor in df.columns
):

    estado_civil = (
        df.groupby('CL_EC')[coluna_valor]
        .mean()
        .reset_index()
    )

    estado_civil.columns = [
        'Estado_Civil',
        'Media_Compra'
    ]

    print("\nMédia de compra por estado civil:")
    print(estado_civil)

# ---------------------------------------------------------
# PIVOT TABLE
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("PIVOT TABLE")
print("=" * 60)

if (
    'CL_GENERO' in df.columns and
    'CL_EC' in df.columns and
    coluna_valor in df.columns
):

    pivot = pd.pivot_table(
        df,
        values=coluna_valor,
        index='CL_GENERO',
        columns='CL_EC',
        aggfunc='mean'
    )

    print(pivot)

# ---------------------------------------------------------
# 8. CONCLUSÕES
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("CONCLUSÕES")
print("=" * 60)

print("""
1. A base possuía valores nulos,
   campos vazios e registros #N/D.

2. As colunas PR_CAT e PR_NOME
   foram tratadas e padronizadas.

3. Registros duplicados foram removidos.

4. A coluna DATA foi convertida
   para datetime.

5. Foram identificados padrões
   de compras por gênero
   e estado civil.

6. A base limpa foi salva
   em um novo arquivo CSV.
""")

# ---------------------------------------------------------
# 9. EXPORTAR BASE LIMPA
# ---------------------------------------------------------

print("\nPROJETO FINALIZADO!")



