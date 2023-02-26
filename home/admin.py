# register orders
from datetime import datetime

from django.contrib import admin, messages

from .models import  Address


# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('address', 'city', 'state', 'zip_code', 'country')
#     search_fields = ('address', 'city', 'state', 'zip_code', 'country')
#
