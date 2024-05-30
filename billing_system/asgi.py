"""
Configuration for ASGI, which is the specification for handling async requests

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'billing_system.settings')

application = get_asgi_application()
