# Justificativa das Métricas — Dashboard 2

## Métrica 1: Total de Títulos

- **Variável:** contagem de linhas do dataset filtrado
- **O que mede:** volume total do catálogo após filtros aplicados
- **Por que foi escolhida:** é a métrica âncora; qualquer outra proporção ou média se apoia nela
- **Público-alvo:** gestores de catálogo / analistas de conteúdo
- **Decisão apoiada:** avaliar se o volume filtrado é representativo o suficiente para tirar conclusões
- **O que comunica:** tamanho atual do catálogo sob as condições selecionadas

---

## Métrica 2: Proporção de Filmes

- **Variável:** `type == "Movie"` / total
- **O que mede:** participação percentual dos filmes no catálogo
- **Por que foi escolhida:** a divisão Movie vs. TV Show é a principal segmentação do dataset e impacta todas as outras métricas
- **Público-alvo:** equipe de conteúdo e planejamento estratégico
- **Decisão apoiada:** decidir se o catálogo está balanceado ou excessivamente voltado para um tipo de conteúdo
- **O que comunica:** qual tipo de conteúdo domina o catálogo sob os filtros ativos

---

## Métrica 3: Proporção de Séries (TV Show)

- **Variável:** `type == "TV Show"` / total
- **O que mede:** participação percentual das séries no catálogo
- **Por que foi escolhida:** complementa a Métrica 2; juntas somam 100% e mostram o mix de conteúdo
- **Público-alvo:** equipe de conteúdo e planejamento estratégico
- **Decisão apoiada:** mesma da Métrica 2 — visão do lado oposto da proporção
- **O que comunica:** peso relativo das séries em comparação aos filmes

---

## Métrica 4: Duração Média dos Filmes

- **Variável:** `duration_num` (filmes apenas, em minutos)
- **O que mede:** tempo médio de duração dos filmes no catálogo filtrado
- **Por que foi escolhida:** duração impacta experiência do usuário e estratégia de licenciamento; filmes muito curtos ou muito longos têm perfis de engajamento diferentes
- **Público-alvo:** curadoria de conteúdo e UX
- **Decisão apoiada:** verificar se o perfil de duração muda por período ou gênero ao ajustar os filtros
- **O que comunica:** o filme típico desse catálogo dura X minutos

---

## Métrica 5: País Mais Prolífico

- **Variável:** `country_first` (primeiro país listado em `country`)
- **O que mede:** o país que mais contribuiu com títulos no catálogo filtrado
- **Por que foi escolhida:** a origem geográfica do conteúdo revela a estratégia de diversificação da plataforma ao longo dos anos
- **Público-alvo:** equipe de parcerias internacionais e expansão de mercado
- **Decisão apoiada:** identificar concentração geográfica e oportunidades de diversificação regional
- **O que comunica:** de onde vem a maior parte do conteúdo no recorte selecionado
