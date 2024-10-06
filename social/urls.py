from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, FollowerViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register('followers', FollowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
