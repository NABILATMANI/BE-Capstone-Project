from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, FollowerViewSet

# Définition du routeur pour la gestion des URLs REST
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'followers', FollowerViewSet)

# Les URLs générées par le routeur sont ajoutées au urlpatterns
urlpatterns = router.urls
