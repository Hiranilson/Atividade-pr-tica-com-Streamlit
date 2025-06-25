# 🌐 Análise de Redes com Streamlit e Pyvis

Este projeto implementa uma aplicação interativa para **análise de redes complexas**, utilizando dados extraídos da Wikipédia com base no termo "Artificial Neural Network".

A rede completa contém milhares de nós, então foi utilizada uma **sub-rede com os 100 nós de maior grau**, garantindo desempenho e visualização adequados.

A interface interativa foi desenvolvida com **Streamlit** e a visualização da rede com **Pyvis**. Os usuários podem navegar, explorar métricas e identificar os nós mais importantes da rede.

## 🔗 Repositório

[GitHub - Hiranilson/Atividade-pr-tica-com-Streamlit](https://github.com/Hiranilson/Atividade-pr-tica-com-Streamlit)

## 🌍 Aplicação Online (Streamlit Cloud)

✅ Acesse aqui:  
[https://atividade-pr-tica-com-app-g847jneeqceezufiqpg7st.streamlit.app](https://atividade-pr-tica-com-app-g847jneeqceezufiqpg7st.streamlit.app)

## 🚀 Funcionalidades

- 🔍 **Visualização interativa da rede** com Pyvis
- 📌 **Seleção de Subgrafos**:
  - Sub-rede completa
  - Top 10 nós por grau
  - Conceitos de aprendizado
  - Conceitos aplicados
  - Biologia & neurociência
  - Vizinhança de "Artificial Neural Network"
  - Comunidade detectada automaticamente
- 📊 **Métricas Estruturais da Rede**:
  - Densidade
  - Assortatividade
  - Coeficiente de Clustering
  - Componentes Fortemente e Fracamente Conectados
- 🎯 **Distribuição de grau dos nós**
- 🏆 **Rankings de centralidade**:
  - Degree
  - Eigenvector
  - Closeness
  - Betweenness

## 🧠 Tecnologias utilizadas

- Python 3
- Streamlit
- NetworkX
- Pyvis
- Matplotlib
- Seaborn
- Wikipedia API

## 📁 Estrutura do Projeto

```
📦 Atividade-pr-tica-com-Streamlit
 ┣ 📜 app.py               ← Código principal da aplicação
 ┣ 📜 rede.gpickle         ← Subgrafo salvo da rede da Wikipédia
 ┣ 📜 requirements.txt     ← Dependências do projeto
 ┗ 📜 README.md            ← Este documento
```

## 💻 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/Hiranilson/Atividade-pr-tica-com-Streamlit.git
cd Atividade-pr-tica-com-Streamlit
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

4. Acesse no navegador:

```
http://localhost:8501
```

---

## ✨ Autor

Desenvolvido por **Hiranilson Andrade**  
Este projeto faz parte da Atividade Prática com Streamlit sobre Análise de Redes Complexas.
