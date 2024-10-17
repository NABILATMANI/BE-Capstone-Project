from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MovieReview

admin.site.register(MovieReview)
