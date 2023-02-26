# urls.py
from django.contrib import admin

from django.urls import path, include
from .views import upload, checkout

urlpatterns = [
    path("upload/", upload, name="upload"),
    path("checkout/<str:order>/", checkout, name="checkout"),
]
