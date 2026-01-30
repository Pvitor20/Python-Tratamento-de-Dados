# 📊 Dashboard de Salários na Área de Dados

## 📌 Visão Geral

Este projeto tem como objetivo a análise de salários anuais na área de dados, explorando como diferentes fatores — como cargo, senioridade, tipo de contrato, regime de trabalho, tamanho da empresa e país de residência — influenciam a remuneração.

O projeto foi desenvolvido como exercício prático de **tratamento de dados, análise exploratória e visualização**, utilizando Python e a biblioteca Streamlit para construção de um dashboard interativo.

---

## 🎯 Objetivos do Projeto

* Explorar dados salariais da área de dados ao longo dos anos
* Identificar cargos com maiores salários médios
* Analisar a distribuição salarial
* Comparar remuneração por país para o cargo de Cientista de Dados
* Praticar boas práticas de análise e comunicação de dados

---

## 🗂️ Fonte dos Dados

Os dados utilizados são provenientes de uma base pública de salários na área de dados, disponibilizada em formato CSV e hospedada no GitHub.

* Os valores representam **salários anuais brutos em USD**
* Os dados agregam informações de diferentes países, cargos e tipos de contrato
* A base passou por tratamento prévio para padronização de colunas e tipos de dados

Arquivo utilizado:

* `Dados_Salarios.csv`

---

## 🧱 Estrutura dos Dados

Principais colunas da base:

* `ano` — Ano de referência do salário
* `cargo` — Cargo ocupado pelo profissional
* `senioridade` — Nível de senioridade (ex: Junior, Pleno, Senior)
* `contrato` — Tipo de contrato de trabalho
* `tamanho_empresa` — Porte da empresa
* `remoto` — Regime de trabalho (presencial, híbrido ou remoto)
* `residencia_iso3` — Código ISO do país de residência
* `usd` — Salário anual em dólares americanos (USD)

---

## 🔎 Metodologia de Análise

* As análises utilizam **salário anual em USD** como métrica principal
* Para comparações entre cargos e países, foi utilizada a **média salarial**, salvo indicação contrária
* Os dados podem ser filtrados dinamicamente por:

  * Ano
  * Senioridade
  * Tipo de contrato
  * Tamanho da empresa

> ⚠️ Observação: a média salarial pode ser influenciada por valores extremos (outliers). O uso dessa métrica foi escolhido para facilitar comparações gerais.

---

## 📈 Visualizações do Dashboard

O dashboard apresenta os seguintes componentes:

### 🔹 Métricas Principais (KPIs)

* Salário médio anual (USD)
* Salário máximo anual (USD)
* Total de registros analisados
* Cargo mais frequente na base

### 🔹 Gráficos

* **Top 10 cargos por salário médio anual**
* **Distribuição dos salários anuais**
* **Proporção dos tipos de regime de trabalho**
* **Mapa de salários médios de Cientistas de Dados por país**

Cada visualização foi desenvolvida para responder a uma pergunta específica de análise.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* Plotly

---

## ▶️ Como Executar o Projeto

1. Clone este repositório:

```bash
git clone https://github.com/Pvitor20/Python-Tratamento-de-Dados.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o dashboard:

```bash
streamlit run app.py
```

---

## 🚀 Considerações Finais

Este projeto tem caráter educacional e foi desenvolvido com foco no aprendizado de análise de dados, visualização e boas práticas de comunicação analítica. Melhorias futuras podem incluir novas métricas, análises estatísticas mais robustas e otimizações visuais.

Feedbacks e sugestões são bem-vindos!
