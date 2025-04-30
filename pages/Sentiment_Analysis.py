import streamlit as st
from utils import search_apps, get_reviews, analyze_reviews
import pandas as pd

st.title(" Analyse de sentiment des avis utilisateurs")

# Entrée utilisateur
query = st.text_input("Entrez un mot-clé pour chercher des applications :", value="note taking ai")
n = st.slider("Nombre d'applications à analyser :", min_value=5, max_value=20, value=5)

if st.button("Analyser les sentiments"):
    with st.spinner("Chargement des données et des avis..."):
        df = search_apps(query, n)

        if df.empty:
            st.warning("Aucune application trouvée.")
        else:
            app_sentiments = []

            for _, row in df.iterrows():
                app_id = row['app_id']
                reviews = get_reviews(app_id, count=10)

                if not reviews:
                    app_sentiments.append({
                        'App': row['title'],
                        'Positifs': 0,
                        'Négatifs': 0
                    })
                    continue

                results = analyze_reviews(reviews)

                # Compte des avis positifs et négatifs
                pos = sum(1 for r in results if r['label'] == 'POSITIVE')
                neg = sum(1 for r in results if r['label'] == 'NEGATIVE')

                app_sentiments.append({
                    'App': row['title'],
                    'Positifs': pos,
                    'Négatifs': neg
                })

            # Affichage sous forme de tableau et graphique
            sentiment_df = pd.DataFrame(app_sentiments)
            st.subheader(" Score de sentiment par application")
            st.dataframe(sentiment_df)
            st.bar_chart(sentiment_df.set_index("App"))