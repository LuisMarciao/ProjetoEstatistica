import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Saúde Mental dos Estudantes", layout="wide")

st.title("Dashboard - Uso de Redes Sociais e Saúde Mental")

@st.cache_data
def load_data():
    df = pd.read_csv("Social_media_impact_on_life.csv")
    return df

df = load_data()

# remover duplicados
df = df.drop_duplicates()

# padronizar nomes das colunas
df.columns = df.columns.str.lower().str.strip()

# padronizar textos
colunas_texto = ["gender", "academic_level", "country", "most_used_platform"]

for col in colunas_texto:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.capitalize()

# tratamento de nulos
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# converter colunas numericas
colunas_numericas = [
    "age",
    "avg_daily_usage_hours",
    "sleep_hours_per_night",
    "mental_health_score"
]

for col in colunas_numericas:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# remover valores invalidos
df = df[(df["sleep_hours_per_night"] >= 0) & (df["sleep_hours_per_night"] <= 24)]
df = df[(df["avg_daily_usage_hours"] >= 0) & (df["avg_daily_usage_hours"] <= 24)]

def remover_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]

for col in colunas_numericas:
    df = remover_outliers(df, col)

df["usage_level"] = pd.cut(
    df["avg_daily_usage_hours"],
    bins=[0, 3, 6, 12],
    labels=["Baixo", "Médio", "Alto"]
)

df["sleep_category"] = pd.cut(
    df["sleep_hours_per_night"],
    bins=[0, 5, 7, 10],
    labels=["Pouco", "Normal", "Bom"]
)

st.sidebar.header("Filtros")

genero = st.sidebar.multiselect(
    "Gênero",
    df["gender"].unique(),
    default=df["gender"].unique()
)

nivel = st.sidebar.multiselect(
    "Nível Acadêmico",
    df["academic_level"].unique(),
    default=df["academic_level"].unique()
)

plataforma = st.sidebar.multiselect(
    "Plataforma",
    df["most_used_platform"].unique(),
    default=df["most_used_platform"].unique()
)

impacto = st.sidebar.multiselect(
    "Impacto Geral",
    df["overall_impact"].unique(),
    default=df["overall_impact"].unique()
)

pais = st.sidebar.multiselect(
    "País",
    df["country"].unique(),
    default=df["country"].unique()
)

df_filtrado = df[
    (df["gender"].isin(genero)) &
    (df["academic_level"].isin(nivel)) &
    (df["most_used_platform"].isin(plataforma)) &
    (df["overall_impact"].isin(impacto)) &
    (df["country"].isin(pais))
]

st.subheader("Indicadores")

col1, col2, col3 = st.columns(3)

col1.metric("Total de estudantes", len(df_filtrado))
col2.metric("Uso médio (h/dia)", round(df_filtrado["avg_daily_usage_hours"].mean(), 2))
col3.metric("Saúde mental média", round(df_filtrado["mental_health_score"].mean(), 2))

# uso de celularXsaude mental
st.subheader("Uso de redes vs Saúde Mental")

fig1, ax1 = plt.subplots()
sns.scatterplot(
    data=df_filtrado,
    x="avg_daily_usage_hours",
    y="mental_health_score",
    hue="usage_level",
    ax=ax1
)
plt.xlabel("Horas de uso diário")
plt.ylabel("Pontuação de saúde mental")
st.pyplot(fig1)

# sonoXsaude mental
st.subheader("Sono vs Saúde Mental")

fig2, ax2 = plt.subplots()
sns.boxplot(
    data=df_filtrado,
    x="sleep_category",
    y="mental_health_score",
    ax=ax2
)
plt.xlabel("Categoria de sono")
plt.ylabel("Pontuação de saúde mental")
st.pyplot(fig2)

# impacto geral
st.subheader("Impacto Geral")

fig3, ax3 = plt.subplots()
sns.countplot(
    data=df_filtrado,
    x="overall_impact",
    ax=ax3
)
plt.xlabel("Impacto geral")
plt.ylabel("Quantidade de estudantes")
st.pyplot(fig3)

# apps mais usados
st.subheader("Plataformas mais utilizadas")

fig4, ax4 = plt.subplots()
sns.countplot(
    data=df_filtrado,
    x="most_used_platform",
    ax=ax4
)
plt.xlabel("Plataforma")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
st.pyplot(fig4)

# paisXsaude mental
st.subheader("Saúde mental por país")

fig5, ax5 = plt.subplots()
sns.barplot(
    data=df_filtrado,
    x="country",
    y="mental_health_score",
    ax=ax5
)
plt.xlabel("País")
plt.ylabel("Média da saúde mental")
plt.xticks(rotation=45)
st.pyplot(fig5)

# nivel academico
st.subheader("🎓 Uso por nível acadêmico")

fig6, ax6 = plt.subplots()
sns.boxplot(
    data=df_filtrado,
    x="academic_level",
    y="avg_daily_usage_hours",
    ax=ax6
)
plt.xlabel("Nível acadêmico")
plt.ylabel("Horas de uso")
st.pyplot(fig6)

# heatmap
st.subheader("Correlação entre variáveis")

fig7, ax7 = plt.subplots()
sns.heatmap(
    df_filtrado.select_dtypes(include="number").corr(),
    annot=True,
    ax=ax7
)
plt.xlabel("Variáveis")
plt.ylabel("Variáveis")
st.pyplot(fig7)

st.subheader("Insights automáticos")

media_sono = df_filtrado["sleep_hours_per_night"].mean()
media_uso = df_filtrado["avg_daily_usage_hours"].mean()

if media_sono < 7:
    st.warning("Estudantes estão dormindo pouco → possível impacto na saúde mental")

if media_uso > 5:
    st.warning("Alto uso de redes sociais detectado")

if df_filtrado["mental_health_score"].mean() < 6:
    st.error("Baixa saúde mental média")

if media_sono >= 7 and media_uso <= 5 and df_filtrado["mental_health_score"].mean() >= 6:
    st.success("Situação geral estável")

st.subheader("Dados filtrados")
st.dataframe(df_filtrado)