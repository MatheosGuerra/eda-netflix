# Rascunho — Dashboard 2: KPIs do Catálogo Netflix

## Objetivo
Painel executivo com métricas-chave e visuais voltados a **gestores de conteúdo e estrategistas de plataformas de streaming**, com foco em composição do catálogo, crescimento histórico e distribuição de públicos-alvo.

## Público-alvo
Gestores de conteúdo e produto que precisam entender rapidamente o perfil do catálogo Netflix: volume, mix de formatos, mercados mais representados e classificação etária do portfólio.

## Wireframe (layout)

```
┌─────────────────────────────────────────────────────────────────────┐
│  TAB: Dashboard 2 — KPIs do Catálogo Netflix                        │
│                                                                     │
│  Caption: Dataset · N títulos · Tipo · Intervalo de ano            │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  Total   │ │  Filmes  │ │  Séries  │ │ Duração  │ │  País #1 │ │
│  │  6.234   │ │  4.265   │ │  1.969   │ │  99 min  │ │  United  │ │
│  │          │ │  68,4%   │ │  31,6%   │ │  (média) │ │  States  │ │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ┌────────────────────────────┐  ┌────────────────────────────────┐ │
│  │  TOP 10 GÊNEROS            │  │  CONTEÚDO POR ANO              │ │
│  │  (barras horizontais)      │  │  (barras empilhadas Movie/Show) │ │
│  │                            │  │                                │ │
│  │  International Movies ████ │  │  2021 ████████████████         │ │
│  │  Dramas           ███████  │  │  2020 ████████████             │ │
│  │  Comedies         ██████   │  │  2019 ████████                 │ │
│  │  ...                       │  │  ...                           │ │
│  └────────────────────────────┘  └────────────────────────────────┘ │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │  DISTRIBUIÇÃO POR CLASSIFICAÇÃO INDICATIVA                      │ │
│  │  (barras verticais — todas as ratings: TV-MA, TV-14, PG-13...)  │ │
│  │                                                                  │ │
│  │   TV-MA  ████████████████████  2.027                            │ │
│  │   TV-14  ████████████          1.698                            │ │
│  │   TV-PG  ██████                 701                             │ │
│  │   R       █████                 508                             │ │
│  │   PG-13   ████                  370                             │ │
│  │   ...                                                           │ │
│  │                                                                  │ │
│  │  Caption: TV-MA=adulto | TV-14=maiores de 14 | G=livre          │ │
│  └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Métricas (KPIs)
| # | Métrica | Justificativa |
|---|---|---|
| 1 | Total de Títulos | Dimensão do catálogo avaliado |
| 2 | Nº de Filmes (%) | Composição do portfólio por formato |
| 3 | Nº de Séries (%) | Complementar ao KPI 2 |
| 4 | Duração Média (filmes, min) | Referência de comprometimento do espectador |
| 5 | País mais prolífico | Origem dominante do conteúdo produzido |

## Visuais além das métricas
| # | Visual | Tipo | Ferramenta |
|---|---|---|---|
| 1 | Top 10 Gêneros | Barras horizontais | Altair |
| 2 | Conteúdo por Ano de Adição | Barras empilhadas (Movie vs TV Show) | Altair |
| 3 | Distribuição por Classificação Indicativa | Barras verticais | Altair |

## Decisões de design
- Paleta Netflix: vermelho `#E50914` (Movie) e vinho `#831010` (TV Show)
- Fundo escuro via `.streamlit/config.toml`
- Gráficos interativos (tooltip on hover) via Altair
- Sidebar compartilhada com o Dashboard 1 para consistência dos filtros
