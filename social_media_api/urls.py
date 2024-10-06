from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view function to handle the root URL ("/")
def welcome(request):
    return HttpResponse("Welcome to the Social Media API! Use /api/ to interact with the API.")

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django admin interface
    path('api/', include('social.urls')),  # Include your app's URLs
    path('', welcome),  # This handles the root URL ("/")
]
