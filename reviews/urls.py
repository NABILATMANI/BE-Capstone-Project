from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieReviewViewSet, UserViewSet

router = DefaultRouter()
router.register(r'reviews', MovieReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
