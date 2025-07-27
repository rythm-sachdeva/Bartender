import django.forms as forms


class CocktailForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
      # Optional field for cocktail image