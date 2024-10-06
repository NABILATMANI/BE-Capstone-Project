from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view function to handle the root URL ("/")
def welcome(request):
    return HttpResponse("Welcome to the Social Media API! Visit /api/ for API documentation.")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel access
    path('api/', include('social.urls')),  # Includes the URLs from the social app
    path('', welcome),  # This handles the root URL "/"
]
