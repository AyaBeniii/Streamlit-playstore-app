from google_play_scraper import search, app, reviews, Sort
import pandas as pd
from transformers import pipeline

#  Fonction de recherche d'apps
def search_apps(query, n=10):
    """
    Recherche les applications liées à un mot-clé sur le Play Store
    et retourne un DataFrame avec les informations principales.
    """
    results = search(query, lang='en', country='us')

    data = []
    for a in results[:n]:
        app_id = a['appId']
        details = app(app_id, lang='en', country='us')
        data.append({
            'app_id': app_id,
            'title': details['title'],
            'description': details['description'],
            'score': details['score'],
            'installs': details['installs'],
            'free': details['free'],
            'genre': details['genre']
        })
    
    return pd.DataFrame(data)

#  Chargement du modèle de sentiment HuggingFace (une seule fois)
sentiment_analyzer = pipeline("sentiment-analysis")

#  Récupération des avis d'une application
def get_reviews(app_id, count=10):
    """
    Récupère une liste d'avis (contenu texte) pour une app donnée.
    """
    result, _ = reviews(app_id, lang='en', country='us', count=count, sort=Sort.NEWEST)
    return [r['content'] for r in result]

#  Analyse de sentiment d'une liste de textes
def analyze_reviews(review_list):
    """
    Applique le modèle de sentiment HuggingFace sur une liste de textes.
    Retourne une liste de résultats avec label (POSITIVE / NEGATIVE) et score.
    """
    sentiments = sentiment_analyzer(review_list)
    return sentiments