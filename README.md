# Dashboard de Saúde Mental de Estudantes

## Sobre o Projeto

Este projeto consiste em um **dashboard interativo desenvolvido com Python e Streamlit**, com o objetivo de analisar a relação entre:

- Uso de redes sociais  
- Qualidade do sono   
- Saúde mental   

A aplicação permite explorar os dados de forma dinâmica por meio de filtros e visualizações, auxiliando na identificação de padrões e possíveis impactos no bem-estar dos estudantes.

---

## Objetivo

O projeto foi desenvolvido para aplicar conceitos de:

- Estatística  
- Análise exploratória de dados (EDA)  
- Tratamento de dados com Pandas  
- Visualização de dados com Matplotlib e Seaborn  
- Desenvolvimento de dashboards interativos  

---

## Dataset

O dataset utilizado contém informações sobre estudantes, incluindo:

- Idade e gênero  
- Nível acadêmico  
- País  
- Tempo de uso de redes sociais  
- Plataforma mais utilizada  
- Qualidade do sono  
- Pontuação de saúde mental  
- Impacto geral das redes sociais  

---

## Tecnologias Utilizadas

- Python 
- Pandas  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## Funcionalidades

### Filtros Interativos

- País  
- Gênero  
- Nível acadêmico  
- Plataforma  
- Impacto geral  

---

### Visualizações

O dashboard apresenta diversos gráficos, incluindo:

- Uso de redes sociais vs saúde mental  
- Sono vs saúde mental  
- Distribuição do impacto geral  
- Uso por nível acadêmico  
- Comparação entre países  
- Heatmap de correlação  

---

### Indicadores (KPIs)

- Total de estudantes  
- Média de uso diário  
- Média de sono  
- Média de saúde mental  

---

### Insights Automáticos

O sistema analisa os dados e gera alertas automaticamente, como:

- Baixa média de sono  
- Uso excessivo de redes sociais  
- Níveis preocupantes de saúde mental  

---

## Tratamento de Dados

Foram aplicadas as seguintes técnicas:

- ✔ Remoção de dados duplicados  
- ✔ Tratamento de valores ausentes (média e moda)  
- ✔ Padronização de colunas  
- ✔ Remoção de outliers (IQR)  
- ✔ Criação de novas variáveis (feature engineering)  

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/LuisMarciao/ProjetoEstatistica.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o projeto

```bash
streamlit run app.py
```

## Resultado

O dashboard permite uma análise visual clara e interativa dos dados, facilitando a identificação de padrões e tomada de decisão.

### Possíveis Melhorias Futuras
- Machine Learning para previsão de saúde mental  
- Deploy online do dashboard  
- Gráficos interativos com Plotly  
- Interface mais avançada  
