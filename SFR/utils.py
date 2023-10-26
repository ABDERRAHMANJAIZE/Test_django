import os

import requests

from SFR.decorators import timing_decorator

# Définir les codes pour les séries et les films
SERIES_CODE = 4
MOVIE_CODE = 3


@timing_decorator
def search_media(title: str, is_series: bool = True):
    """
    Rechercher des médias en fonction du titre et du type (série ou film).

    Args:
    title (str)
    is_series (bool, optional)

    Returns:
    list: Une liste de dictionnaires, chaque dictionnaire contenant les informations d'un média.
    """
    titles = []

    # Récupérer l'URL de l'API et la clé API depuis les variables d'environnement
    API_URL = os.environ.get("API_URL")
    API_KEY = os.environ.get("API_KEY")

    # Déterminer le type de recherche en fonction du paramètre is_series
    search_type = SERIES_CODE if is_series else MOVIE_CODE

    # Construire l'URL de la requête à l'API
    url = f"{API_URL}?apiKey={API_KEY}&search_value={title}&search_type={search_type}"
    response = requests.get(url)

    # Gérer les erreurs potentielles de la requête HTTP
    if response.status_code != 200:
        response.raise_for_status()

    for result in response.json().get("results", []):
        titles.append({
            'name': result["name"],
            'year': result["year"],
            'image': result["image_url"]
        })

    return titles
