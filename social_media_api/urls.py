from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view to handle the root URL
def welcome(request):
    return HttpResponse("<h1>Welcome to the Social Media API!</h1><p>Use <a href='/api/'>/api/</a> to interact with the API.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel access
    path('api/', include('social.urls')),  # Include app URLs
    path('', welcome),  # Root URL ("/")
]
