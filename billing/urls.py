from django.urls import path
from .views import billing_view

urlpatterns = [
    path('', billing_view, name='billing'),
]