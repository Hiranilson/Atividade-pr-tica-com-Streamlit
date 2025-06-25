
import streamlit as st
import networkx as nx
from pyvis.network import Network
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

@st.cache_data
def carregar_rede():
    with open("rede.gpickle", "rb") as f:
        return pickle.load(f)

def plot_pyvis(grafo):
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(grafo)
    net.show_buttons(filter_=['physics'])
    net.repulsion(node_distance=200, central_gravity=0.3)
    net.save_graph("graph.html")
    with open("graph.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html

def plot_degree_distribution(grafo):
    graus = [grafo.degree(n) for n in grafo.nodes()]
    plt.figure(figsize=(8,6))
    sns.histplot(graus, bins=20, kde=False)
    plt.title("Distribuição de Grau dos Nós")
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    st.pyplot(plt.gcf())

def calcular_métricas(g):
    densidade = nx.density(g)
    try:
        assort = nx.degree_assortativity_coefficient(g)
    except:
        assort = None
    clustering = nx.average_clustering(g.to_undirected())
    wcc = nx.number_weakly_connected_components(g) if g.is_directed() else nx.number_connected_components(g)
    scc = nx.number_strongly_connected_components(g) if g.is_directed() else None
    return {
        "Densidade": densidade,
        "Assortatividade": assort,
        "Coeficiente de Clustering": clustering,
        "Componentes Fortemente Conectados": scc,
        "Componentes Fracamente Conectados": wcc
    }

def calcular_centralidades(g):
    centralidade = {
        "Degree": nx.degree_centrality(g),
        "Closeness": nx.closeness_centrality(g),
        "Betweenness": nx.betweenness_centrality(g)
    }
    try:
        centralidade["Eigenvector"] = nx.eigenvector_centrality(g)
    except:
        centralidade["Eigenvector"] = {n: 0 for n in g.nodes()}
    return centralidade

st.set_page_config(page_title="Análise de Redes - Wikipédia", layout="wide")
st.title("🌐 Análise de Redes Complexas com Pyvis e NetworkX")

st.sidebar.header("Configurações")
grafo = carregar_rede()
st.sidebar.write(f"🔗 Nós: {grafo.number_of_nodes()} | Arestas: {grafo.number_of_edges()}")

subgrafo_tipo = st.sidebar.selectbox("Selecione Subgrafo", ["Sub-rede Completa", "Maior Componente Conectado", "Top 10 por Grau"])
if subgrafo_tipo == "Maior Componente Conectado":
    componentes = nx.weakly_connected_components(grafo) if grafo.is_directed() else nx.connected_components(grafo)
    maior = max(componentes, key=len)
    g_sub = grafo.subgraph(maior).copy()
elif subgrafo_tipo == "Top 10 por Grau":
    graus = dict(grafo.degree())
    top10 = sorted(graus, key=graus.get, reverse=True)[:10]
    g_sub = grafo.subgraph(top10).copy()
else:
    g_sub = grafo.copy()

st.subheader("🔍 Visualização Interativa da Rede")
html = plot_pyvis(g_sub)
st.components.v1.html(html, height=600, scrolling=True)

st.subheader("📊 Métricas Estruturais da Rede")
metricas = calcular_métricas(g_sub)
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col1.metric("Densidade", round(metricas["Densidade"], 4))
col2.metric("Assortatividade", round(metricas["Assortatividade"], 4) if metricas["Assortatividade"] is not None else "N/A")
col3.metric("Clustering", round(metricas["Coeficiente de Clustering"], 4))
col4.metric("Componentes Fortemente Conectados", metricas["Componentes Fortemente Conectados"] if metricas["Componentes Fortemente Conectados"] is not None else "N/A")
col5.metric("Componentes Fracamente Conectados", metricas["Componentes Fracamente Conectados"])

st.subheader("🎯 Distribuição de Grau dos Nós")
plot_degree_distribution(g_sub)

st.subheader("🏆 Centralidade dos Nós")
centralidades = calcular_centralidades(g_sub)
tipo_centralidade = st.selectbox("Selecione a Métrica de Centralidade", list(centralidades.keys()))
ordenado = sorted(centralidades[tipo_centralidade].items(), key=lambda x: x[1], reverse=True)
df_centralidade = pd.DataFrame(ordenado, columns=["Nó", "Centralidade"])
st.dataframe(df_centralidade)
st.bar_chart(df_centralidade.set_index("Nó").head(10))

st.caption("Desenvolvido por Hiranilson Andrade ✨")
