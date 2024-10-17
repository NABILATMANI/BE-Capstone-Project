from django.db import models
from django.contrib.auth.models import User

class MovieReview(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie_title} - {self.rating} stars'
