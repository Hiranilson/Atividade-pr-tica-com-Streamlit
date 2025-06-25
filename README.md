# 🌐 Análise de Redes com Streamlit e Pyvis

Este projeto implementa uma aplicação interativa para **análise de redes complexas**, utilizando dados extraídos da Wikipédia com base no termo "Artificial Neural Network".

Devido ao tamanho elevado, foi selecionada uma **sub-rede composta pelos 1.249 nós com grau maior que 24**, que representam os termos mais conectados da rede original. Isso garante desempenho e visualização adequada na aplicação.

A interface foi construída com **Streamlit** e a visualização interativa com **Pyvis**.

## 🔗 Repositório

[GitHub - Hiranilson/Atividade-pr-tica-com-Streamlit](https://github.com/Hiranilson/Atividade-pr-tica-com-Streamlit)

## 🌍 Aplicação Online (Streamlit Cloud)

✅ Acesse aqui:  
[https://atividade-pr-tica-com-app-g847jneeqceezufiqpg7st.streamlit.app](https://atividade-pr-tica-com-app-g847jneeqceezufiqpg7st.streamlit.app)

## 🚀 Funcionalidades

- 🔍 Visualização interativa da rede com Pyvis
- 📊 Cálculo de métricas estruturais:
  - Densidade
  - Assortatividade
  - Coeficiente de Clustering
  - Componentes Fortemente e Fracamente Conectados
- 🎯 Distribuição de grau dos nós
- 🏆 Rankings de centralidade:
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
 ┣ 📜 rede.gpickle         ← Sub-rede com os 1.249 nós mais conectados
 ┣ 📜 requirements.txt     ← Dependências do projeto
 ┗ 📜 README.md            ← Este arquivo
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