# 🌐 Análise de Redes com Streamlit e Pyvis

Este projeto cria uma aplicação interativa para análise de redes, utilizando dados extraídos da Wikipédia.

## 🚀 Funcionalidades

- 🔍 Visualização interativa da rede (com Pyvis)
- 📊 Cálculo de métricas estruturais:
  - Densidade
  - Assortatividade
  - Clustering
  - Componentes Fortemente e Fracamente Conectados
- 🎯 Distribuição de grau
- 🏆 Centralidades (Degree, Closeness, Betweenness, Eigenvector)

## 💻 Executando localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

## 🌍 Deploy
Use o [Streamlit Cloud](https://streamlit.io/cloud) para publicar online.

## 📁 Estrutura
- `app.py`: Código principal
- `rede.gpickle`: Grafo salvo
- `requirements.txt`: Dependências
- `README.md`: Documentação
