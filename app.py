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
    df["country"] = df["country"].fillna("Unknown")

    df["country_first"] = df["country"].str.split(",").str[0].str.strip()
    df["genre_first"] = df["listed_in"].str.split(",").str[0].str.strip()

    return df


df = load_data()

VARS_QUANT = ["release_year", "year_added", "duration_num"]
LABELS = {
    "release_year": "Ano de Lançamento",
    "year_added":   "Ano de Adição",
    "duration_num": "Duração em minutos (filmes)",
}

COLOR_MOVIE = "#E50914"
COLOR_TV    = "#831010"

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Filtros")

    tipo_sel = st.selectbox(
        "Tipo de conteúdo",
        options=["Todos", "Movie", "TV Show"],
    )

    vars_corr = st.multiselect(
        "Variáveis para a correlação",
        options=VARS_QUANT,
        default=["release_year", "year_added"],
        format_func=lambda v: LABELS[v],
        help="Selecione ao menos 2 variáveis para gerar o heatmap.",
    )

    ano_min = int(df["release_year"].min())
    ano_max = int(df["release_year"].max())
    intervalo_ano = st.slider(
        "Intervalo de ano de lançamento",
        min_value=ano_min,
        max_value=ano_max,
        value=(ano_min, ano_max),
        help="Mova os extremos para excluir outliers e ver como isso afeta a correlação.",
    )

# ── Filtros aplicados ─────────────────────────────────────────────────────────

df_f = df.copy()
if tipo_sel != "Todos":
    df_f = df_f[df_f["type"] == tipo_sel]
df_f = df_f[df_f["release_year"].between(intervalo_ano[0], intervalo_ano[1])]

# ── Tabs ──────────────────────────────────────────────────────────────────────

tab1, tab2 = st.tabs(
    ["Dashboard 1 — Correlação e Distribuição", "Dashboard 2 — KPIs"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# DASHBOARD 1
# ═══════════════════════════════════════════════════════════════════════════════

with tab1:
    st.title("Dashboard 1 — Correlação e Distribuição")
    st.caption(
        f"Dataset: Netflix Movies and TV Shows  ·  "
        f"**{len(df_f):,}** títulos após filtros  ·  "
        f"Tipo: {tipo_sel}  ·  "
        f"Ano: {intervalo_ano[0]}–{intervalo_ano[1]}"
    )

    col_corr, col_dist = st.columns(2)

    # ── Heatmap de correlação ─────────────────────────────────────────────────
    with col_corr:
        st.subheader("Correlação")

        if len(vars_corr) < 2:
            st.warning("Selecione ao menos 2 variáveis na sidebar para gerar o heatmap.")
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

    # ── Histograma de distribuição ────────────────────────────────────────────
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
                    for tipo, cor in [("Movie", COLOR_MOVIE), ("TV Show", COLOR_TV)]:
                        subset = df_f[df_f["type"] == tipo][var_dist].dropna()
                        if not subset.empty:
                            sns.histplot(
                                subset,
                                bins=30,
                                color=cor,
                                label=tipo,
                                alpha=0.7,
                                ax=ax2,
                                kde=True,
                            )
                    ax2.legend()
                else:
                    cor = COLOR_MOVIE if tipo_sel == "Movie" else COLOR_TV
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
    st.title("Dashboard 2 — KPIs do Catálogo Netflix")
    st.caption(
        f"Dataset: Netflix Movies and TV Shows  ·  "
        f"**{len(df_f):,}** títulos após filtros  ·  "
        f"Tipo: {tipo_sel}  ·  "
        f"Ano: {intervalo_ano[0]}–{intervalo_ano[1]}"
    )

    # ── Cartões de KPI ────────────────────────────────────────────────────────
    total = len(df_f)
    n_movies = int((df_f["type"] == "Movie").sum())
    n_shows  = int((df_f["type"] == "TV Show").sum())
    pct_movies = n_movies / total * 100 if total else 0
    pct_shows  = n_shows  / total * 100 if total else 0

    movies_only = df_f[df_f["type"] == "Movie"]["duration_num"].dropna()
    avg_duration = movies_only.mean() if not movies_only.empty else 0

    top_country = (
        df_f[df_f["country_first"] != "Unknown"]["country_first"]
        .value_counts()
        .idxmax()
        if total > 0 else "—"
    )

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Total de Títulos", f"{total:,}")
    k2.metric("Filmes", f"{n_movies:,}", f"{pct_movies:.1f}%")
    k3.metric("Séries (TV Show)", f"{n_shows:,}", f"{pct_shows:.1f}%")
    k4.metric("Duração Média (filmes)", f"{avg_duration:.0f} min")
    top_country_short = top_country.split()[0] if len(top_country) > 10 else top_country
    k5.metric("País mais prolífico", top_country_short, help=f"País completo: {top_country}")

    st.divider()

    # ── Gráficos interativos (Altair) ─────────────────────────────────────────
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
        genre_counts["Gênero_completo"] = genre_counts["Gênero"]
        genre_counts["Gênero"] = genre_counts["Gênero"].apply(
            lambda x: x[:20] + "…" if len(x) > 20 else x
        )

        chart_genre = (
            alt.Chart(genre_counts)
            .mark_bar()
            .encode(
                x=alt.X("Títulos:Q", title="Quantidade"),
                y=alt.Y("Gênero:N", sort="-x", title=""),
                color=alt.value(COLOR_MOVIE),
                tooltip=[
                    alt.Tooltip("Gênero_completo:N", title="Gênero"),
                    alt.Tooltip("Títulos:Q"),
                ],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_genre, use_container_width=True)

    with col_bar2:
        st.subheader("Conteúdo Adicionado por Ano")

        year_df = (
            df_f.dropna(subset=["year_added"])
            .groupby(["year_added", "type"])
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
                    "type:N",
                    scale=alt.Scale(
                        domain=["Movie", "TV Show"],
                        range=[COLOR_MOVIE, COLOR_TV],
                    ),
                    legend=alt.Legend(title="Tipo"),
                ),
                tooltip=["year_added:O", "type:N", "Títulos:Q"],
            )
            .properties(height=320)
        )
        st.altair_chart(chart_year, use_container_width=True)

    st.divider()

    # ── Distribuição de classificações indicativas ────────────────────────────
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
                alt.value(COLOR_MOVIE),
                alt.value(COLOR_TV),
            ),
            tooltip=["Classificação", "Títulos"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart_rating, use_container_width=True)
    st.caption(
        "TV-MA = adulto | TV-14 = maiores de 14 | TV-PG / PG-13 = supervisão recomendada | "
        "G / TV-G = livre | NR = não classificado"
    )
