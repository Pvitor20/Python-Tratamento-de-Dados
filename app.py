import streamlit as st
import pandas as pd
import plotly.express as px

#Configuração da página
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide"
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://github.com/Pvitor20/Python-Tratamento-de-Dados/blob/main/Dados_Salarios.csv?raw=true")

# --- Barra lateral ---
st.sidebar.header("Filtros")

# Filtro por Ano
ano_disponivel = sorted(df["ano"].unique())
ano_selecionado = st.sidebar.multiselect("Ano", options=ano_disponivel, default=ano_disponivel)

# Filtro por Senioridade
senioridade_disponivel = sorted(df['senioridade'].unique())
senioridade_selecionada = st.sidebar.multiselect("Senioridade", options=senioridade_disponivel, default=senioridade_disponivel)

# Filtro por Tipo de Contrato
tipo_contrato_disponivel = sorted(df['contrato'].unique())
tipo_contrato_selecionado = st.sidebar.multiselect("Tipo de Contrato", options=tipo_contrato_disponivel, default=tipo_contrato_disponivel)

# Filtro por Tamanho da Empresa
tamanho_disponivel = sorted(df['tamanho_empresa'].unique())
tamanho_selecionado = st.sidebar.multiselect("Tamanho da Empresa", tamanho_disponivel, default=tamanho_disponivel)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
df_filtrado = df[
    (df['ano'].isin(ano_selecionado)) &
    (df['senioridade'].isin(senioridade_selecionada)) &
    (df['contrato'].isin(tipo_contrato_selecionado)) &
    (df['tamanho_empresa'].isin(tamanho_selecionado))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")

st.markdown("""
Este dashboard tem como objetivo analisar **salários anuais na área de dados**, 
considerando fatores como cargo, senioridade, tipo de contrato, regime de trabalho,
tamanho da empresa e país de residência.

Os valores apresentados referem-se a **salários anuais brutos em USD**.
""")

st.markdown("""
### 🔎 Metodologia de Análise
- As análises utilizam **salário anual em USD** como métrica principal  
- Para comparações entre cargos e países, foi utilizada a **média salarial**  
- Os dados exibidos respeitam os filtros selecionados na barra lateral
""")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio anual (USD)", f"${salario_medio:,.0f}")
col2.metric("Salário máximo anual (USD)", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# --- Análises Visuais com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:

        st.markdown("""
        **Pergunta de análise:**  
        Quais cargos apresentam os **maiores salários médios anuais**, considerando os filtros aplicados?
        """)


        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio anual (USD)",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
            
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")
    
    st.caption("Os valores representam a **média salarial anual** por cargo.")

with col_graf2:
    if not df_filtrado.empty:

        st.markdown("""
        **Pergunta de análise:**  
        Como os salários anuais se distribuem na base de dados?
        """)

        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    st.caption("Este gráfico mostra a distribuição dos salários anuais na base analisada.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:

        st.markdown("""
        **Pergunta de análise:**  
        Qual a proporção entre os diferentes regimes de trabalho na base analisada?
        """)

        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

    st.caption("Distribuição dos regimes de trabalho considerando os filtros aplicados.")
with col_graf4:
    if not df_filtrado.empty:
        st.markdown("""
        **Pergunta de análise:**  
        Como varia o **salário médio anual de Cientistas de Dados** entre os países?
        """)
        df_data_science = df_filtrado[df_filtrado['cargo'].str.contains('Data Scientist', case=False)]
        df_data_science_media_salario = df_data_science.groupby('residencia_iso3')['usd'].mean().sort_values(ascending=False).reset_index()
        grafico_paises = px.choropleth(df_data_science_media_salario,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")
    
    st.caption("Países exibidos em branco não possuem registros na base para o cargo de Cientista de Dados.")

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
     

