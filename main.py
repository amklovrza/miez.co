# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos

# pip install streamlit pandas plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Passo 1: Criar a tela do sistema
st.write("Miez & Co.")

tabela = pd.read_csv("DBsales.csv")

# Passo 2: Criar o formulário de cadastro
st.sidebar.write("## Add sale")
data = st.sidebar.date_input("Date")
vendedor = st.sidebar.selectbox("Salesperson", ["Anabelle", "Leticia", "Fernanda"])
produto = st.sidebar.selectbox("Product", ["Bloquinho", "Marca página", "Caneta", "Livro de Receitas","Adesivos"])
modelo_produto = st.sidebar.selectbox("Product Model", ["Yellow", "White_japan", "White_pretzel","Grey"])
quantidade = st.sidebar.number_input("Quantity", step=1)
valor_unitario = st.sidebar.number_input("Unit Value", step=0.01)
valor_total = st.sidebar.number_input("Total Value", step=0.01)
botao = st.sidebar.button("Register Sale")

# Passo 3: Salvar a venda na base de dados
if botao:
    nova_venda = [data, vendedor, produto, modelo_produto, quantidade, valor_unitario, valor_total]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv("DBsales.csv", index=False)
    st.success("Sale registered!")

# Passo 4: Mostrar a base de dados na tela
st.write("## Sales registered")
st.dataframe(tabela)

# Passo 5: Criar o dashboard
st.write("## Dashboard")
soma = tabela["valor_total"].sum()
st.metric("Total Revenue", f"R${soma}")

grafico = px.bar(tabela, x="vendedor", y="valor_total", color="produto")
st.plotly_chart(grafico)

grafico2 = px.pie(tabela, names="produto", values="valor_total")
st.plotly_chart(grafico2)