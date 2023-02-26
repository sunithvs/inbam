# dashboard/urls.py
# Compare this snippet from config/urls.py:
# """config URL Configuration
from django.urls import path

from .views import dashboard, edit_profile, pending_orders, completed_orders

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('orders/pending/', pending_orders, name='pending_orders'),
    path('orders/completed/', completed_orders, name='completed_orders'),
]


