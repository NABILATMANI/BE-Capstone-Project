from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Vue simple pour l'URL racine
def welcome(request):
    return HttpResponse("<h1>Bienvenue sur l'API des Réseaux Sociaux !</h1><p>Utilisez <a href='/api/'>/api/</a> pour interagir avec l'API.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Chemin pour l'administration
    path('api/', include('social.urls')),  # Chemin pour inclure les URLs de l'application 'social'
    path('', welcome),  # Chemin pour la racine ("/")
]
