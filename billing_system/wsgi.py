"""
Configuration for WSGI, which is the specification for handling web server requests.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'billing_system.settings')

application = get_wsgi_application()
