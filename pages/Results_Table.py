import streamlit as st
from utils import search_apps
import pandas as pd

st.title("Résultats de recherche – Google Play Apps")

# Champ de saisie utilisateur
query = st.text_input("Entrez un mot-clé pour rechercher des applications :", value="note taking ai")

# Nombre d’apps à récupérer
n = st.slider("Nombre d'applications à afficher :", min_value=5, max_value=30, value=10)

# Lancer la recherche
if st.button("Rechercher"):
    with st.spinner("Recherche en cours..."):
        df = search_apps(query, n)
        if not df.empty:
            st.success(f"{len(df)} applications trouvées pour : '{query}'")
            st.dataframe(df)
        else:
            st.warning("Aucune application trouvée.")