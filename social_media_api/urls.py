from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle the root URL
def welcome(request):
    return HttpResponse("<h1>Welcome to the Social Media API!</h1><p>Use /api/ to interact with the API.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('social.urls')),  # Include app URLs for 'social'
    path('', welcome),  # Root URL to display a simple welcome message
]
