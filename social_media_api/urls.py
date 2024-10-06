from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle the root URL
def welcome(request):
    return HttpResponse("Welcome to the Social Media API. Use /api/ to interact with the API.")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin panel access
    path('api/', include('social.urls')),  # Your API URLs from the 'social' app
    path('', welcome),  # This handles the root URL "/"
]
