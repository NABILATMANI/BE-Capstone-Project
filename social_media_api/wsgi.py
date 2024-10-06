"""
WSGI config for social_media_api project.

This script is used to serve your application in production using WSGI, 
which is the Python standard for web servers and applications.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for the 'social_media_api' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

# Get the WSGI application for the project.
application = get_wsgi_application()
