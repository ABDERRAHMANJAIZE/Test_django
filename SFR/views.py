from django.http import HttpResponseServerError
from django.shortcuts import render

from .forms import SearchForm
from .utils import search_media


def search_view(request):
    """
    Traiter les données du formulaire pour rechercher des titres de médias si la méthode de requête est POST.
    Préremplir le formulaire avec les données de la dernière requête de recherche si la méthode de requête est GET.

    """
    titles = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # Valider les données du formulaire
        if form.is_valid():
            title = form.cleaned_data['title']
            is_series = form.cleaned_data['is_series']
            # Essayer d'effectuer la recherche et gérer les erreurs potentielles
            try:
                titles = search_media(title, is_series)
            except Exception as e:
                print(f"Une erreur s'est produite pendant la recherche : {str(e)}")
                return HttpResponseServerError("Une erreur interne du serveur s'est produite.")

            request.session['last_search_query_title'] = title
            request.session['last_search_query_type'] = is_series
    else:
        # Récupérer les informations de la dernière requête de recherche de la session (si disponible)
        title = request.session.get("last_search_query_title", "")
        is_series = request.session.get("last_search_query_type", False)
        # Initialiser le formulaire avec les données de la dernière requête de recherche
        form = SearchForm({'title': title, 'is_series': is_series})

    # Rendre la page de recherche avec le formulaire et les résultats de la recherche
    return render(request, 'search.html', {'form': form, 'results': titles})
