# Declaração de Uso de Inteligência Artificial Generativa
**Atividade Streamlit AVD – 2026.2 - Dashboards com Streamlit — Aulas 21 a 23**

---

## 1. Identificação

| Campo | Preenchimento |
|---|---|
| **Turma** | ☑ 5A &nbsp;&nbsp; ☐ 5B |
| **Nome Completo** | Matheos Guerra |
| **E-mail** | matheos.guerra@equipeblue.com.br |
| **Repositório** | https://github.com/MatheosGuerra/eda-netflix |
| **Data de entrega** | 29/10/2026 |

---

## 2. Diretrizes

_(Lidas e compreendidas antes do uso.)_

---

## 3. Declaração geral

☐ Não utilizei nenhuma ferramenta de IA generativa em nenhuma etapa do projeto.

☑ **Utilizei IA generativa, somente nas situações permitidas, e registro todos os usos nas Seções 4 a 6.**

---

## 4. Ferramentas utilizadas

| Ferramenta | Versão / plano | Em que parte da atividade |
|---|---|---|
| Claude Code (Anthropic) | claude-sonnet-4-6 / Pro | Sintaxe dos gráficos (Seaborn, Altair), depuração de erros de deploy, configuração do Git, otimização da interface |

> **Observação:** Claude Code é uma ferramenta de linha de comando (CLI). Não gera links de conversa compartilháveis. Por isso utilizo a **Opção B — registro bloco a bloco** na Seção 5.

---

## 5. Registro de usos

---

### Uso nº 1

| Campo | Descrição |
|---|---|
| **Data** | 22/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | `app.py` — estrutura base (esqueleto) |
| **Finalidade (Permitido §2)** | Gerar o esqueleto do app.py a partir do rascunho de layout definido por mim |
| **O que foi pedido** | Estrutura do app com `st.tabs`, sidebar com selectbox e slider, carregamento do CSV com `@st.cache_data` e tema Netflix via `config.toml` |
| **O que foi aproveitado / o que modifiquei** | Aproveitei a estrutura geral; ajustei as variáveis escolhidas (`release_year`, `year_added`, `duration_num`), os rótulos em português e as cores da identidade Netflix que eu mesmo defini |
| **Como verifiquei que estava correto** | Rodei o app localmente com `streamlit run app.py` e conferí que o layout correspondia ao meu rascunho em `entregas/rascunho-dashboard1.md` |

---

### Uso nº 2

| Campo | Descrição |
|---|---|
| **Data** | 22/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | Dashboard 1 — sintaxe do heatmap e histograma |
| **Finalidade (Permitido §2)** | Apoio com sintaxe de bibliotecas de visualização (Seaborn): o código que desenha o gráfico |
| **O que foi pedido** | Código do `sns.heatmap` com `annot=True` e do `sns.histplot` com `kde=True`, separados por tipo (Filme/Série) |
| **O que foi aproveitado / o que modifiquei** | Aproveitei a chamada das funções; a escolha de quais variáveis correlacionar, a paleta de cores (`#E50914` / `#831010`) e a decisão de usar KDE foram minhas |
| **Como verifiquei que estava correto** | Comparei visualmente os gráficos com o que eu havia esboçado no rascunho; confirmei os valores de correlação com o que havia explorado no notebook de EDA |

---

### Uso nº 3

| Campo | Descrição |
|---|---|
| **Data** | 22/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | Dashboard 2 — sintaxe dos gráficos Altair |
| **Finalidade (Permitido §2)** | Apoio com sintaxe de biblioteca de visualização (Altair): o código que desenha os gráficos |
| **O que foi pedido** | Código dos gráficos de barras horizontais (Top 10 Gêneros), barras empilhadas (conteúdo por ano) e barras verticais (classificação indicativa) em Altair |
| **O que foi aproveitado / o que modifiquei** | Aproveitei a sintaxe Altair (`.mark_bar()`, `.encode()`, `alt.Color`); a escolha dos 3 gráficos, o que cada um representa e por que são relevantes para o público-alvo (gestores de conteúdo) foi minha, documentada em `entregas/justificativa-metricas.md` |
| **Como verifiquei que estava correto** | Conferi que os dados exibidos correspondiam às contagens do dataset que eu já conhecia pela EDA; testei com diferentes filtros da sidebar |

---

### Uso nº 4

| Campo | Descrição |
|---|---|
| **Data** | 29/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | Depuração de erros no deploy (Streamlit Cloud) |
| **Finalidade (Permitido §2)** | Entender mensagens de erro e depurar código do deploy |
| **O que foi pedido** | Correção dos erros: `AttributeError` em `str.extract()` (incompatibilidade com pandas novo) e `ValueError` em `idxmax()` com Series vazia ao filtrar anos extremos no slider |
| **O que foi aproveitado / o que modifiquei** | Aproveitei as correções pontuais (`[0].str.strip()` e guarda de `.empty`); entendi a causa de cada erro e confirmei que faziam sentido antes de aceitar |
| **Como verifiquei que estava correto** | Acompanhei os logs do Streamlit Cloud após o redeploy e confirmei que os erros sumiram; testei manualmente o slider nos valores extremos |

---

### Uso nº 5

| Campo | Descrição |
|---|---|
| **Data** | 29/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | Configuração do repositório Git e deploy |
| **Finalidade (Permitido §2)** | Apoio na parte técnica repetitiva de configuração (Git init, remote, commit, push) — tarefa mecânica e demorada |
| **O que foi pedido** | Inicialização do repositório local, conexão com o GitHub e primeiro push |
| **O que foi aproveitado / o que modifiquei** | Aproveitei os comandos Git gerados; criei o repositório no GitHub e fiz o deploy no Streamlit Community Cloud eu mesmo (processo de login e configuração via interface web) |
| **Como verifiquei que estava correto** | Acessei `github.com/MatheosGuerra/eda-netflix` e `eda-netflix.streamlit.app` e confirmei que os arquivos e o app estavam no ar |

---

### Uso nº 6

| Campo | Descrição |
|---|---|
| **Data** | 29/10/2026 |
| **Ferramenta** | Claude Code (claude-sonnet-4-6) |
| **Parte da atividade** | Interface — tradução para português e correções visuais |
| **Finalidade (Permitido §2)** | Apoio na criação de identidade visual e otimização da interface do dashboard |
| **O que foi pedido** | Tradução dos rótulos da interface para português (tipos de conteúdo, legendas dos gráficos, nomes de gêneros), ajuste de títulos das abas e correção de truncamento de labels no Altair (`labelLimit`) |
| **O que foi aproveitado / o que modifiquei** | Aproveitei as alterações de código; todas as decisões de design (quais termos usar em português, ordem das colunas, estilo dos títulos) foram minhas — eu identifiquei os problemas e pedi as correções específicas |
| **Como verifiquei que estava correto** | Acessei o app publicado em aba anônima e conferi visualmente cada elemento |

---

## 6. Trechos de código feitos com apoio de IA

| Arquivo / parte | Teve apoio de IA? | Tipo de apoio |
|---|---|---|
| `app.py` (esqueleto) | ☑ Sim | Esqueleto gerado a partir do meu rascunho de layout |
| Dashboard 1 (correlação + distribuição) | ☑ Sim | Sintaxe Seaborn (heatmap e histplot); escolha das variáveis e gráficos foi minha |
| Dashboard 2 (KPIs) | ☑ Sim | Sintaxe Altair (3 gráficos); escolha das 5 métricas e dos 3 gráficos foi minha |
| Deploy / configuração | ☑ Sim | Comandos Git (repetitivo); deploy no Streamlit Cloud foi feito por mim via interface web |
| Depuração de erros | ☑ Sim | Correção de 2 erros de incompatibilidade com pandas 2.x no Streamlit Cloud |
| Interface / tradução | ☑ Sim | Otimização de rótulos, tradução de termos e correção de truncamentos visuais |

---

## 7. Reflexão individual

Durante o desenvolvimento dos dashboards, utilizei a ferramenta Claude Code como apoio à implementação técnica, especialmente nas partes mais mecânicas e na sintaxe das bibliotecas de visualização. Toda a parte analítica e de decisão — escolha do dataset Netflix, definição do público-alvo do Dashboard 2 (gestores de conteúdo de plataformas de streaming), seleção das 5 métricas e dos 3 gráficos — foi realizada por mim com base na EDA que desenvolvi no notebook `EDA_Netflix.ipynb`.

A IA não sugeriu nem justificou nenhuma métrica: ela implementou o que eu já havia decidido e documentado em `entregas/justificativa-metricas.md` antes de iniciar o código. Em nenhum momento a IA interpretou os dados ou tirou conclusões sobre o catálogo Netflix em meu lugar.

Houve momentos em que a IA sugeriu abordagens que eu avaliei e ajustei: por exemplo, a forma de exibir o país mais prolífico foi adaptada por mim para mostrar apenas a primeira palavra com tooltip, e a ordem das colunas no Dashboard 1 foi invertida por decisão minha depois de ver o resultado. Identifiquei os bugs (slider com ano único, texto truncado, interface em inglês) e direcionei as correções.

Garanti que as métricas do Dashboard 2 refletem minha escolha ao revisá-las contra a justificativa que escrevi previamente, e ao confirmar que os números exibidos batiam com o que eu havia explorado na EDA. Todo o código entregue é compreensível para mim e sei explicar cada bloco.

---

## 8. Termo de responsabilidade

Declaro que as informações deste documento são verdadeiras e completas; que compreendo e sei explicar todo o código, as saídas e as análises entregues, inclusive os trechos feitos com apoio de IA; e que estou ciente de que uso não declarado, uso proibido ou incapacidade de explicar o trabalho resultam nas consequências da Seção 2.

| Campo | Preenchimento |
|---|---|
| **Nome** | Matheos Guerra |
| **Assinatura** | _(assinar manuscrita ou via gov.br antes de exportar para PDF)_ |
| **Data** | 29/10/2026 |
