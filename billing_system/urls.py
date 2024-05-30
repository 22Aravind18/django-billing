"""
The root URL configuration. Maps URL paths to views. Typically includes URL configurations from various apps
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('billing.urls')),
]