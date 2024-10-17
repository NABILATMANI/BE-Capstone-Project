from django.urls import path
from .views import MovieReviewListCreateView, MovieReviewDetailView

urlpatterns = [
    path('reviews/', MovieReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', MovieReviewDetailView.as_view(), name='review-detail'),
]