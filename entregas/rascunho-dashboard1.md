# Rascunho — Dashboard 1: Correlação e Distribuição

## Objetivo
Laboratório interativo para explorar a relação entre variáveis quantitativas do catálogo Netflix e a distribuição de cada uma delas.

## Público
Analistas e pesquisadores de dados interessados em padrões de lançamento e adição de conteúdo.

## Wireframe (layout)

```
┌─────────────────────────────────────────────────────────────────────┐
│  SIDEBAR                                                            │
│  ┌───────────────────────────────┐                                  │
│  │ Tipo de conteúdo [selectbox]  │                                  │
│  │  Todos / Movie / TV Show      │                                  │
│  ├───────────────────────────────┤                                  │
│  │ Variáveis para correlação     │                                  │
│  │  [multiselect]                │                                  │
│  │  ✓ release_year               │                                  │
│  │  ✓ year_added                 │                                  │
│  │  □ duration_num               │                                  │
│  ├───────────────────────────────┤                                  │
│  │ Intervalo de ano [slider]     │                                  │
│  │  ──●──────────────────────●── │                                  │
│  │  1925                    2021 │                                  │
│  └───────────────────────────────┘                                  │
├─────────────────────────────────────────────────────────────────────┤
│  TAB: Dashboard 1 — Correlação e Distribuição                       │
│                                                                     │
│  Caption: Dataset · N títulos · Tipo · Intervalo de ano            │
│                                                                     │
│  ┌──────────────────────────┐  ┌──────────────────────────────────┐ │
│  │  CORRELAÇÃO              │  │  DISTRIBUIÇÃO                    │ │
│  │                          │  │  Variável [selectbox]            │ │
│  │  Heatmap (seaborn)       │  │                                  │ │
│  │  ┌────────────────────┐  │  │  Histograma + KDE (seaborn)      │ │
│  │  │  var1  var2        │  │  │  ┌──────────────────────────┐   │ │
│  │  │  var1 [1.00][0.85] │  │  │  │  ████ Movie              │   │ │
│  │  │  var2 [0.85][1.00] │  │  │  │  ▓▓▓▓ TV Show            │   │ │
│  │  └────────────────────┘  │  │  │  curva KDE sobreposta    │   │ │
│  │                          │  │  └──────────────────────────┘   │ │
│  │                          │  │                                  │ │
│  │                          │  │  [▼ Estatísticas descritivas]    │ │
│  │                          │  │   Registros | Média | Mediana    │ │
│  └──────────────────────────┘  └──────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Variáveis quantitativas avaliadas
| Variável | Descrição |
|---|---|
| `release_year` | Ano de lançamento do título |
| `year_added` | Ano em que o título foi adicionado ao catálogo |
| `duration_num` | Duração em minutos (apenas filmes) |

## Hipóteses a explorar
- Títulos mais recentes tendem a ser adicionados mais rapidamente ao catálogo?
- Filmes mais longos são lançados em determinados períodos?
- A correlação release_year × year_added diminui para conteúdo mais antigo?

## Stack utilizada
- `seaborn.heatmap` para a matriz de correlação
- `seaborn.histplot` com `kde=True` para o histograma
- `st.pyplot` para renderização no Streamlit
- Filtros via `st.sidebar`: `st.selectbox`, `st.multiselect`, `st.slider`
