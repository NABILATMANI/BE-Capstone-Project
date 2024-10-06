from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view to handle the root URL
def welcome(request):
    return HttpResponse("Welcome to the Social Media API. Use /api/ to interact with the API.")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('api/', include('social.urls')),  # Include the URLs from your app
    
    # Root URL
    path('', welcome),  # Handle the root URL with a simple welcome message
]
