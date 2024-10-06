from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle the root URL ("/")
def welcome(request):
    return HttpResponse("Welcome to the Social Media API! Use /api/ to interact with the API.")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel access
    path('api/', include('social.urls')),  # Includes the URLs from the app
    path('', welcome),  # Handles the root URL "/"
]
