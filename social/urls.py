from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, FollowerViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'followers', FollowerViewSet)

urlpatterns = router.urls
