from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle the root URL ("/") and return a basic HTML response
def welcome(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Welcome Page</title>
            </head>
            <body>
                <h1>Welcome to the Social Media API!</h1>
                <p>Use <a href="/api/">/api/</a> to interact with the API.</p>
            </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin panel access
    path('api/', include('social.urls')),  # Your API URLs from the 'social' app
    path('', welcome),  # This handles the root URL "/"
]
