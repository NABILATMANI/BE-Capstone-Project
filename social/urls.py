from django.urls import path
from .views import PostViewSet, UserViewSet, FollowerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'followers', FollowerViewSet)

urlpatterns = router.urls
