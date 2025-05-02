import streamlit as st

st.title("Test : Entrée utilisateur")

nom = st.text_input("Quel est ton prénom ?")

if nom:
    st.write(f"Bonjour *{nom}* Bienvenue sur Streamlit !")