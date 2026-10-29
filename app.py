import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from pathlib import Path

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide",
)

HERE = Path(__file__).parent

# ── Carregamento e pré-processamento ─────────────────────────────────────────

@st.cache_data
def load_data():
    candidates = [
        HERE / "data" / "netflix_tratado.csv",
        HERE / "data" / "netflix_titles.csv",
        HERE / "../datasetnetflix/netflix_titles.csv",
        HERE / "netflix_titles.csv",
    ]
    csv_path = next((p for p in candidates if p.exists()), None)
    if csv_path is None:
        st.error("Arquivo netflix_titles.csv não encontrado. Verifique o caminho.")
        st.stop()
    df = pd.read_csv(csv_path)

    df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)
    df["duration_unit"] = df["duration"].str.extract(r"([A-Za-z\s]+)")[0].str.strip()

    df["date_added_parsed"] = pd.to_datetime(
        df["date_added"].str.strip(), format="%B %d, %Y", errors="coerce"
    )
    df["year_added"] = df["date_added_parsed"].dt.year
    df["month_added"] = df["date_added_parsed"].dt.month

    df = df.dropna(subset=["rating", "date_added"]).reset_index(drop=True)
    df["director"] = df["director"].fillna("Não informado")
    df["cast"] = df["cast"].fillna("Não informado")
    df["country"] = df["country"].fillna("Desconhecido")

    df["country_first"] = df["country"].str.split(",").str[0].str.strip()
    df["genre_first"] = df["listed_in"].str.split(",").str[0].str.strip()

    GENEROS_PT = {
        "Action & Adventure": "Ação e Aventura",
        "Anime Features": "Anime — Filmes",
        "Anime Series": "Anime — Séries",
        "British TV Shows": "Séries Britânicas",
        "Children & Family Movies": "Filmes Infantis e Família",
        "Classic & Cult TV": "TV Clássica e Cult",
        "Classic Movies": "Filmes Clássicos",
        "Comedies": "Comédias",
        "Crime TV Shows": "Séries de Crime",
        "Cult Movies": "Filmes Cult",
        "Documentaries": "Documentários",
        "Docuseries": "Documentários em Série",
        "Dramas": "Dramas",
        "Faith & Spirituality": "Fé e Espiritualidade",
        "Horror Movies": "Filmes de Terror",
        "Independent Movies": "Filmes Independentes",
        "International Movies": "Filmes Internacionais",
        "International TV Shows": "Séries Internacionais",
        "Kids' TV": "TV Infantil",
        "Korean TV Shows": "Séries Coreanas",
        "LGBTQ Movies": "Filmes LGBTQ+",
        "Movies": "Filmes",
        "Music & Musicals": "Música e Musicais",
        "Nature & Ecology": "Natureza e Ecologia",
        "Reality TV": "Reality Shows",
        "Romantic Movies": "Filmes Românticos",
        "Romantic TV Shows": "Séries Românticas",
        "Sci-Fi & Fantasy": "Ficção Científica e Fantasia",
        "Science & Nature TV": "Ciência e Natureza",
        "Spanish-Language TV Shows": "Séries em Espanhol",
        "Sports Movies": "Filmes de Esporte",
        "Stand-Up Comedy": "Stand-Up Comedy",
        "Stand-Up Comedy & Talk Shows": "Stand-Up e Talk Shows",
        "Talk Show TV Shows": "Talk Shows",
        "Teen TV Shows": "Séries para Adolescentes",
        "Thrillers": "Thrillers",
        "TV Action & Adventure": "Séries de Ação e Aventura",
        "TV Comedies": "Comédias de TV",
        "TV Dramas": "Dramas de TV",
        "TV Horror": "Terror de TV",
        "TV Mysteries": "Mistérios de TV",
        "TV Sci-Fi & Fantasy": "Ficção Científica de TV",
        "TV Thrillers": "Thrillers de TV",
    }
    df["genre_first"] = df["genre_first"].replace(GENEROS_PT)

    # Coluna de tipo em português para exibição
    df["tipo_pt"] = df["type"].map({"Movie": "Filme", "TV Show": "Série"})

    return df


df = load_data()

VARS_QUANT = ["release_year", "year_added", "duration_num"]
LABELS = {
    "release_year": "Ano de Lançamento",
    "year_added":   "Ano de Adição",
    "duration_num": "Duração em min. (filmes)",
}

# Mapa tipo PT → valor no CSV
TIPO_MAP = {"Todos": None, "Filme": "Movie", "Série": "TV Show"}

COLOR_FILME  = "#E50914"
COLOR_SERIE  = "#831010"

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Filtros")

    tipo_sel = st.selectbox(
        "Tipo de conteúdo",
        options=["Todos", "Filme", "Série"],
        help="Filtra todos os gráficos e métricas pelo tipo de conteúdo.",
    )

    vars_corr = st.multiselect(
        "Variáveis para correlação",
        options=VARS_QUANT,
        default=["release_year", "year_added"],
        format_func=lambda v: LABELS[v],
        help="Selecione ao menos 2 variáveis para gerar o mapa de calor.",
    )

    ano_min = int(df["release_year"].min())
    ano_max = int(df["release_year"].max())
    intervalo_ano = st.slider(
        "Intervalo de ano de lançamento",
        min_value=ano_min,
        max_value=ano_max,
        value=(ano_min, ano_max),
        help="Arraste as extremidades para excluir outliers.",
    )

# ── Filtros aplicados ─────────────────────────────────────────────────────────

df_f = df.copy()
tipo_csv = TIPO_MAP[tipo_sel]
if tipo_csv:
    df_f = df_f[df_f["type"] == tipo_csv]
df_f = df_f[df_f["release_year"].between(intervalo_ano[0], intervalo_ano[1])]

caption_base = (
    f"Dataset: Netflix Movies and TV Shows  ·  "
    f"**{len(df_f):,}** títulos após filtros  ·  "
    f"Tipo: {tipo_sel}  ·  "
    f"Ano: {intervalo_ano[0]}–{intervalo_ano[1]}"
)

# ── Tabs ──────────────────────────────────────────────────────────────────────

tab1, tab2 = st.tabs(
    ["📊 Correlação e Distribuição", "📈 KPIs do Catálogo"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# DASHBOARD 1
# ═══════════════════════════════════════════════════════════════════════════════

with tab1:
    st.title("Correlação e Distribuição")
    st.caption(caption_base)

    col_dist, col_corr = st.columns(2)

    # ── Mapa de calor ─────────────────────────────────────────────────────────
    with col_corr:
        st.subheader("Mapa de Calor")

        if len(vars_corr) < 2:
            st.warning("Selecione ao menos 2 variáveis na barra lateral para gerar o mapa de calor.")
        else:
            colunas_validas = [v for v in vars_corr if v in df_f.columns]
            corr_data = df_f[colunas_validas].dropna()

            if corr_data.empty:
                st.warning("Nenhum dado disponível para calcular a correlação.")
            else:
                corr_matrix = corr_data.rename(columns=LABELS).corr()

                fig, ax = plt.subplots(figsize=(5, 4))
                sns.heatmap(
                    corr_matrix,
                    annot=True,
                    fmt=".2f",
                    cmap="Reds",
                    linewidths=0.5,
                    ax=ax,
                    vmin=-1,
                    vmax=1,
                )
                plt.xticks(rotation=30, ha="right", fontsize=8)
                plt.yticks(rotation=0, fontsize=8)
                plt.tight_layout()
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)

    # ── Histograma ────────────────────────────────────────────────────────────
    with col_dist:
        st.subheader("Distribuição")

        var_dist = st.selectbox(
            "Variável para o histograma",
            options=vars_corr if vars_corr else VARS_QUANT,
            format_func=lambda v: LABELS[v],
            key="var_dist",
        )

        if var_dist in df_f.columns:
            serie = df_f[var_dist].dropna()

            if serie.empty:
                st.warning("Nenhum dado disponível para a variável selecionada.")
            else:
                fig2, ax2 = plt.subplots(figsize=(5, 4))

                if tipo_sel == "Todos":
                    for tipo_raw, label_pt, cor in [
                        ("Movie",   "Filme", COLOR_FILME),
                        ("TV Show", "Série", COLOR_SERIE),
                    ]:
                        subset = df_f[df_f["type"] == tipo_raw][var_dist].dropna()
                        if not subset.empty:
                            sns.histplot(
                                subset,
                                bins=30,
                                color=cor,
                                label=label_pt,
                                alpha=0.7,
                                ax=ax2,
                                kde=True,
                            )
                    ax2.legend()
                else:
                    cor = COLOR_FILME if tipo_sel == "Filme" else COLOR_SERIE
                    sns.histplot(serie, bins=30, color=cor, alpha=0.85, ax=ax2, kde=True)

                ax2.set_xlabel(LABELS.get(var_dist, var_dist), fontsize=9)
                ax2.set_ylabel("Contagem", fontsize=9)
                plt.tight_layout()
                st.pyplot(fig2, use_container_width=True)
                plt.close(fig2)

                with st.expander("Estatísticas descritivas"):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Registros", f"{len(serie):,}")
                    c2.metric("Média", f"{serie.mean():.1f}")
                    c3.metric("Mediana", f"{serie.median():.1f}")

# ═══════════════════════════════════════════════════════════════════════════════
# DASHBOARD 2 — KPIs
# ═══════════════════════════════════════════════════════════════════════════════

with tab2:
    st.title("KPIs do Catálogo Netflix")
    st.caption(caption_base)

    # ── Métricas ──────────────────────────────────────────────────────────────
    total    = len(df_f)
    n_filmes = int((df_f["type"] == "Movie").sum())
    n_series = int((df_f["type"] == "TV Show").sum())
    pct_filmes = n_filmes / total * 100 if total else 0
    pct_series = n_series / total * 100 if total else 0

    filmes_only  = df_f[df_f["type"] == "Movie"]["duration_num"].dropna()
    avg_duration = filmes_only.mean() if not filmes_only.empty else 0

    _country_counts = df_f[df_f["country_first"] != "Desconhecido"]["country_first"].value_counts()
    top_country = _country_counts.idxmax() if not _country_counts.empty else "—"
    top_country_short = top_country.split()[0] if len(top_country) > 10 else top_country

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Total de Títulos",       f"{total:,}")
    k2.metric("Filmes",                 f"{n_filmes:,}",  f"{pct_filmes:.1f}%")
    k3.metric("Séries",                 f"{n_series:,}",  f"{pct_series:.1f}%")
    k4.metric("Duração Média (filmes)", f"{avg_duration:.0f} min")
    k5.metric("País mais prolífico",    top_country_short,
              help=f"País completo: {top_country}")

    st.divider()

    # ── Gráficos Altair ───────────────────────────────────────────────────────
    col_bar1, col_bar2 = st.columns(2)

    with col_bar1:
        st.subheader("Top 10 Gêneros")

        genre_counts = (
            df_f["genre_first"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        genre_counts.columns = ["Gênero", "Títulos"]

        chart_genre = (
            alt.Chart(genre_counts)
            .mark_bar()
            .encode(
                x=alt.X("Títulos:Q", title="Quantidade"),
                y=alt.Y("Gênero:N", sort="-x", title="",
                        axis=alt.Axis(labelLimit=200)),
                color=alt.value(COLOR_FILME),
                tooltip=["Gênero", "Títulos"],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_genre, use_container_width=True)

    with col_bar2:
        st.subheader("Conteúdo Adicionado por Ano")

        year_df = (
            df_f.dropna(subset=["year_added"])
            .groupby(["year_added", "tipo_pt"])
            .size()
            .reset_index(name="Títulos")
        )
        year_df["year_added"] = year_df["year_added"].astype(int)

        chart_year = (
            alt.Chart(year_df)
            .mark_bar()
            .encode(
                x=alt.X("year_added:O", title="Ano de Adição"),
                y=alt.Y("Títulos:Q"),
                color=alt.Color(
                    "tipo_pt:N",
                    scale=alt.Scale(
                        domain=["Filme", "Série"],
                        range=[COLOR_FILME, COLOR_SERIE],
                    ),
                    legend=alt.Legend(title="Tipo"),
                ),
                tooltip=[
                    alt.Tooltip("year_added:O",  title="Ano"),
                    alt.Tooltip("tipo_pt:N",      title="Tipo"),
                    alt.Tooltip("Títulos:Q",      title="Títulos"),
                ],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_year, use_container_width=True)

    st.divider()

    # ── Classificação indicativa ──────────────────────────────────────────────
    st.subheader("Distribuição por Classificação Indicativa")

    rating_df = (
        df_f["rating"]
        .value_counts()
        .reset_index()
    )
    rating_df.columns = ["Classificação", "Títulos"]

    chart_rating = (
        alt.Chart(rating_df)
        .mark_bar()
        .encode(
            x=alt.X("Classificação:N", sort="-y", title="Classificação"),
            y=alt.Y("Títulos:Q", title="Quantidade"),
            color=alt.condition(
                alt.datum["Classificação"] == "TV-MA",
                alt.value(COLOR_FILME),
                alt.value(COLOR_SERIE),
            ),
            tooltip=["Classificação", "Títulos"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart_rating, use_container_width=True)
    st.caption(
        "TV-MA = adulto | TV-14 = maiores de 14 anos | TV-PG / PG-13 = supervisão recomendada | "
        "G / TV-G = livre | NR = não classificado"
    )
