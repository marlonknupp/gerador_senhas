import streamlit as st
from gerador_senha.utils import gerar_senha

# Fundo azul claro
st.markdown("""
    <style>
    .stApp {
        background-color: #DCEEFB;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Gerador de Senhas Seguras")

tamanho = st.slider("Escolha o tamanho da senha:", 6, 30, 12)

usar_maiusculas = st.checkbox("Incluir letras MAIÚSCULAS", value=True)
usar_minusculas = st.checkbox("Incluir letras minúsculas", value=True)
usar_simbolos = st.checkbox("Incluir símbolos (ex: @#$%)", value=True)
usar_numeros = st.checkbox("Incluir números (0–9)", value=True)

if st.button("🔄 Gerar Senha"):
    senha = gerar_senha(
        tamanho=tamanho,
        maiusculas=usar_maiusculas,
        minusculas=usar_minusculas,
        simbolos=usar_simbolos,
        numeros=usar_numeros
    )
    st.success(f'**Senha gerada com sucesso:** {senha}')
