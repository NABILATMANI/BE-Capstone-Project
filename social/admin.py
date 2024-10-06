from django.contrib import admin
from .models import User, Post, Follower

# Registering the models to make them available in the Django admin interface.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follower)
