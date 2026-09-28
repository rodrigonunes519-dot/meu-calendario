import streamlit as st
import random

st.set_page_config(page_title="Matrix - Adivinhação", page_icon="🎮", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; }
    h1, h3, p, label { color: #00FF00 !important; font-family: 'Courier New', monospace !important; }
    div.stButton > button { 
        background-color: #00FF00 !important; color: black !important; 
        font-weight: bold !important; font-family: 'Courier New', monospace !important;
        border-radius: 8px !important; width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("==========================")
st.title("   ADIVINHAÇÃO MATRIX     ")
st.title("==========================")
st.subheader("Pensei em um número de 1 a 10. Você tem 3 chances!")

if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 10)
    st.session_state.tentativas = 3
    st.session_state.jogo_finalizado = False
    st.session_state.mensagem = "Estou aguardando o seu palpite..."

if not st.session_state.jogo_finalizado:
    st.write(f"Chances restantes: {st.session_state.tentativas}")
    palpite = st.number_input("Digite seu palpite (1 a 10):", min_value=1, max_value=10, step=1, key="palpite_input")
    
    if st.button("CONFERIR PALPITE"):
        if palpite == st.session_state.numero_secreto:
            st.session_state.mensagem = f"🎉 PARABÉNS! Você acertou! O número era {st.session_state.numero_secreto}."
            st.session_state.jogo_finalizado = True
            st.rerun()
        else:
            st.session_state.tentativas -= 1
            if st.session_state.tentativas > 0:
                dica = "MAIOR" if palpite < st.session_state.numero_secreto else "MENOR"
                st.session_state.mensagem = f"❌ Errou! O número secreto é {dica}."
            else:
                st.session_state.mensagem = f"💀 GAME OVER! O número secreto era {st.session_state.numero_secreto}."
                st.session_state.jogo_finalizado = True
            st.rerun()

st.write(st.session_state.mensagem)

if st.session_state.jogo_finalizado:
    if st.button("🔄 JOGAR NOVAMENTE"):
        st.session_state.numero_secreto = random.randint(1, 10)
        st.session_state.tentativas = 3
        st.session_state.jogo_finalizado = False
        st.session_state.mensagem = "Novo jogo iniciado! Dê o seu palpite..."
        st.rerun()