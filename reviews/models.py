from django.contrib.auth.models import User
from django.db import models

class MovieReview(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.rating} Stars"
