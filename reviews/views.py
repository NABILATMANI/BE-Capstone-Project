from rest_framework import generics, permissions
from .models import MovieReview
from .serializers import MovieReviewSerializer
from rest_framework.permissions import IsAuthenticated  # This is the missing import

# List and Create Reviews
class MovieReviewListCreateView(generics.ListCreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read for unauthenticated users, auth required for creating reviews

    def perform_create(self, serializer):
        # Automatically associate the review with the logged-in user
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete Individual Reviews
class MovieReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Only authenticated users can edit/delete

    def get_queryset(self):
        # Ensure users can only edit or delete their own reviews
        return MovieReview.objects.filter(user=self.request.user)
