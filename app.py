import streamlit as st
import networkx as nx
from pyvis.network import Network
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from networkx.algorithms.community import label_propagation_communities

@st.cache_data
def carregar_rede():
    with open("rede.gpickle", "rb") as f:
        return pickle.load(f)

def plot_pyvis(grafo, solver, central_gravity, node_distance, spring_length):
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(grafo)

    # Aplica parâmetros de física de acordo com o algoritmo escolhido
    if solver == "barnesHut":
        net.barnes_hut(gravity=-2000, central_gravity=central_gravity)
    elif solver == "forceAtlas2Based":
        net.force_atlas_2based(gravity=-50)
    elif solver == "repulsion":
        net.repulsion(node_distance=node_distance, central_gravity=central_gravity, spring_length=spring_length)
    elif solver == "hierarchicalRepulsion":
        net.hrepulsion(spring_length=spring_length)

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

# Streamlit config
st.set_page_config(page_title="Análise de Redes - Wikipédia", layout="wide")
st.title("🌐 Análise de Redes Complexas com Pyvis e NetworkX")

# Carregamento
grafo = carregar_rede()

# Painel lateral de configurações
st.sidebar.header("⚙️ Configurações da Visualização")
st.sidebar.write(f"🔗 Nós: {grafo.number_of_nodes()} | Arestas: {grafo.number_of_edges()}")

subgrafo_tipo = st.sidebar.selectbox("Selecione Subgrafo", [
    "Sub-rede Completa",
    "Maior Componente Conectado",
    "Top 10 por Grau",
    "Conceitos de Aprendizado",
    "Conceitos Aplicados",
    "Biologia & Neurociência",
    "Ética e Controvérsias",
    "Vizinhança de 'Artificial Neural Network'",
    "Comunidade Detectada"
])

solver = st.sidebar.selectbox("Algoritmo de Física", ["repulsion", "barnesHut", "forceAtlas2Based", "hierarchicalRepulsion"])
central_gravity = st.sidebar.slider("Gravidade Central", 0.0, 1.0, 0.3)
node_distance = st.sidebar.slider("Distância entre Nós", 10, 500, 200)
spring_length = st.sidebar.slider("Comprimento da Mola", 10, 300, 100)

# Subgrafo selecionado
if subgrafo_tipo == "Maior Componente Conectado":
    componentes = nx.weakly_connected_components(grafo) if grafo.is_directed() else nx.connected_components(grafo)
    maior = max(componentes, key=len)
    g_sub = grafo.subgraph(maior).copy()

elif subgrafo_tipo == "Top 10 por Grau":
    graus = dict(grafo.degree())
    top10 = sorted(graus, key=graus.get, reverse=True)[:10]
    g_sub = grafo.subgraph(top10).copy()

elif subgrafo_tipo == "Conceitos de Aprendizado":
    chaves = ["learning", "network", "neuron", "deep", "supervised", "unsupervised"]
    familia = [n for n in grafo.nodes if any(p in n.lower() for p in chaves)]
    g_sub = grafo.subgraph(familia).copy()

elif subgrafo_tipo == "Conceitos Aplicados":
    chaves = ["robot", "vision", "speech", "recognition", "diagnosis", "application"]
    aplicacoes = [n for n in grafo.nodes if any(p in n.lower() for p in chaves)]
    g_sub = grafo.subgraph(aplicacoes).copy()

elif subgrafo_tipo == "Biologia & Neurociência":
    chaves = ["neuro", "synap", "brain", "cortex"]
    bio = [n for n in grafo.nodes if any(p in n.lower() for p in chaves)]
    g_sub = grafo.subgraph(bio).copy()

elif subgrafo_tipo == "Ética e Controvérsias":
    chaves = ["bias", "ethic", "privacy", "fairness"]
    etica = [n for n in grafo.nodes if any(p in n.lower() for p in chaves)]
    g_sub = grafo.subgraph(etica).copy()

elif subgrafo_tipo == "Vizinhança de 'Artificial Neural Network'":
    if "Artificial Neural Network" in grafo:
        vizinhos = list(nx.single_source_shortest_path_length(grafo, "Artificial Neural Network", cutoff=2).keys())
        g_sub = grafo.subgraph(vizinhos).copy()
    else:
        st.error("Nó 'Artificial Neural Network' não encontrado na rede.")
        g_sub = nx.DiGraph()

elif subgrafo_tipo == "Comunidade Detectada":
    comunidades = list(label_propagation_communities(grafo.to_undirected()))
    comunidade_escolhida = comunidades[0] if comunidades else []
    g_sub = grafo.subgraph(comunidade_escolhida).copy()

else:
    g_sub = grafo.copy()

# Visualização
st.subheader("🔍 Visualização Interativa da Rede")
html = plot_pyvis(g_sub, solver, central_gravity, node_distance, spring_length)
st.components.v1.html(html, height=600, scrolling=True)

# Métricas
st.subheader("📊 Métricas Estruturais da Rede")
metricas = calcular_métricas(g_sub)
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col1.metric("Densidade", round(metricas["Densidade"], 4))
col2.metric("Assortatividade", round(metricas["Assortatividade"], 4) if metricas["Assortatividade"] is not None else "N/A")
col3.metric("Clustering", round(metricas["Coeficiente de Clustering"], 4))
col4.metric("Componentes Fortemente Conectados", metricas["Componentes Fortemente Conectados"] if metricas["Componentes Fortemente Conectados"] is not None else "N/A")
col5.metric("Componentes Fracamente Conectados", metricas["Componentes Fracamente Conectados"])

# Grau
st.subheader("🎯 Distribuição de Grau dos Nós")
plot_degree_distribution(g_sub)

# Centralidade
st.subheader("🏆 Centralidade dos Nós")
centralidades = calcular_centralidades(g_sub)
tipo_centralidade = st.selectbox("Selecione a Métrica de Centralidade", list(centralidades.keys()))
ordenado = sorted(centralidades[tipo_centralidade].items(), key=lambda x: x[1], reverse=True)
df_centralidade = pd.DataFrame(ordenado, columns=["Nó", "Centralidade"])
st.dataframe(df_centralidade)
st.bar_chart(df_centralidade.set_index("Nó").head(10))

st.caption("Desenvolvido por Hiranilson Andrade ✨")