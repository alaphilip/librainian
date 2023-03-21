"""
WSGI config for ebookstore_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebookstore_project.settings')

# Get the WSGI application for the Django project
application = get_wsgi_application()
