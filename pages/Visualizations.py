import streamlit as st
from utils import search_apps
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualisations des applications Google Play")

query = st.text_input("Entrez un mot-clé pour analyser les applications :", value="note taking ai")
n = st.slider("Nombre d'applications à analyser :", min_value=5, max_value=30, value=10)

if st.button("Générer les graphiques"):
    with st.spinner("Chargement des données..."):
        df = search_apps(query, n)

        if df.empty:
            st.warning("Aucune application trouvée.")
        else:
            st.success(f"{len(df)} applications trouvées.")

            # Bar chart : Score des apps
            st.subheader("Distribution des scores (notes)")
            fig1, ax1 = plt.subplots()
            df['score'].value_counts().sort_index().plot(kind='bar', ax=ax1)
            ax1.set_xlabel("Note")
            ax1.set_ylabel("Nombre d'applications")
            st.pyplot(fig1)

            # Pie chart : Free vs Paid
            st.subheader("Répartition : Gratuit vs Payant")
            pie_data = df['free'].value_counts()
            fig2, ax2 = plt.subplots()
            labels = pie_data.index.map(lambda x: "Gratuit" if x else "Payant")
            ax2.pie(pie_data, labels=labels, autopct='%1.1f%%', startangle=90)            
            ax2.axis('equal')
            st.pyplot(fig2)

            # Bar chart : Répartition par genre
            st.subheader("Répartition par catégorie (genre)")
            fig3, ax3 = plt.subplots()
            df['genre'].value_counts().plot(kind='barh', ax=ax3)
            ax3.set_xlabel("Nombre d'applications")
            st.pyplot(fig3)