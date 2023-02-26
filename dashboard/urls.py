# dashboard/urls.py
# Compare this snippet from config/urls.py:
# """config URL Configuration
from django.urls import path

from .views import dashboard, profile, pending_orders, completed_orders

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('orders/pending/', pending_orders, name='pending_orders'),
    path('orders/completed/', completed_orders, name='completed_orders'),
]


