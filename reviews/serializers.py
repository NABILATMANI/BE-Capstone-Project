from rest_framework import serializers
from .models import MovieReview

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']
