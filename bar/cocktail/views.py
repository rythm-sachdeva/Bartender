from django.shortcuts import render

from .forms import CocktailForm
import requests
# Create your views here.


def cocktail_list(request):
    data = None
    error_message = None
    if(request.method == 'POST'):
        query = CocktailForm(request.POST)
        if query.is_valid():
            q = query.cleaned_data['name']
            api_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={q}"
            try:
                # Replace with your API URL
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    else:
        query = CocktailForm()
    
    context = {
        'form': query,
        'data': data,
        'error_message': error_message,
    }

    return render(request, 'cocktail/index.html', context)
