import streamlit as st

st.title("Competitor Analysis App – Google Play AI Note-Taking Apps")

st.markdown("""
Bienvenue sur l'application d'analyse de la concurrence des applications de prise de notes basées sur l'IA .

###  Objectifs du projet :
- Explorer automatiquement les applications concurrentes via l'API Google Play
- Visualiser les tendances, notes, avis et autres données clés
- Analyser les **sentiments des utilisateurs** à partir des avis collectés

---

###  Fonctionnalités disponibles :
- **Recherche dynamique** d'applications selon un mot-clé
- **Affichage des résultats** dans un tableau
- **Visualisations interactives** (bar charts, pie charts, word cloud…)
- **Analyse de sentiment** à partir des avis utilisateurs (via un modèle HuggingFace)

---

###  Outils utilisés :
- Python 
- Streamlit
- Google Play Scraper API
- HuggingFace Transformers
- Pandas, Matplotlib, Seaborn

---

###  Améliorations possibles :
- Ajouter d'autres sources (GitHub, ProductHunt…)
- Ajouter des graphiques avancés (boxplots, heatmaps…)
- Intégrer des modèles IA pour recommandations ou résumé automatique

---
""")