import os
import sys

# Make sure your project path is added to the system path
path = '/home/nabilatmami/BE-Capstone-Project'
if path not in sys.path:
    sys.path.append(path)

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_media_api.settings'

# Load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
