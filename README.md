# Netflix Dashboard — EDA & Visualização

Aplicação interativa com dois dashboards construída sobre o dataset **Netflix Movies and TV Shows** (Kaggle, ~8.800 títulos).

## Link do App

**https://eda-netflix.streamlit.app/**

## Descrição

Projeto desenvolvido para a disciplina **Análise e Visualização de Dados** — CESAR School.

A partir de uma EDA completa do catálogo da Netflix, foram criados dois dashboards interativos com filtros dinâmicos e visualizações que exploram padrões de conteúdo, distribuições e KPIs executivos.

## Dashboards

### Dashboard 1 — Correlação e Distribuição
Laboratório analítico para explorar relações entre variáveis quantitativas do catálogo:
- **Heatmap de correlação** entre `release_year`, `year_added` e `duration_num`
- **Histograma + KDE** por variável, separado por tipo de conteúdo (Movie / TV Show)
- Filtros: tipo de conteúdo, seleção de variáveis e intervalo de ano de lançamento

### Dashboard 2 — KPIs do Catálogo
Painel executivo voltado a gestores de conteúdo e produto:
- **5 métricas**: total de títulos, nº de filmes (%), nº de séries (%), duração média e país mais prolífico
- **Top 10 Gêneros** — barras horizontais interativas
- **Conteúdo por Ano de Adição** — barras empilhadas (Movie vs TV Show)
- **Distribuição por Classificação Indicativa** — perfil etário do catálogo

## Estrutura do Repositório

```
EDA_Netflix/
├── app.py                        ← aplicação Streamlit
├── requirements.txt
├── .streamlit/
│   └── config.toml               ← tema Netflix dark
├── data/
│   └── netflix_titles.csv
├── notebooks/
│   └── EDA_Netflix.ipynb
├── entregas/
│   ├── rascunho-dashboard1.md    ← wireframe Dashboard 1
│   ├── rascunho-dashboard2.md    ← wireframe Dashboard 2
│   └── justificativa-metricas.md
└── prompts/
    └── declaracao-uso-ia.md
```

## Stack

| Ferramenta | Uso |
|---|---|
| Python 3.11 | Linguagem base |
| Streamlit | Framework de dashboard |
| Pandas | Manipulação de dados |
| Seaborn + Matplotlib | Heatmap e histograma |
| Altair | Gráficos interativos |

## Como executar localmente

```bash
# Criar e ativar venv
python -m venv venv
venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar o app
streamlit run app.py
```

## Dataset

[Netflix Movies and TV Shows — Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Arquivo: `data/netflix_titles.csv` (~8.800 linhas, 12 colunas)

## Declaração de Uso de IA

Consulte [`prompts/declaracao-uso-ia.md`](prompts/declaracao-uso-ia.md).
