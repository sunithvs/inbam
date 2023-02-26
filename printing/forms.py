from django import forms

from .models import ObjectModel, Order


class ObjectModelForm(forms.ModelForm):
    class Meta:
        model = ObjectModel
        fields = ['file', ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["description", ]
