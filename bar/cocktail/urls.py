from django.contrib import admin
from django.urls import path
from .views import cocktail_list

urlpatterns = [
    path('', cocktail_list, name='cocktail_list')
]