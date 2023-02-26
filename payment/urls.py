from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("callback/", views.payment_handler, name="payment_handler"),
    # path("checkout.html/", views.CheckoutView.as_view(), name="checkout.html"),
]
