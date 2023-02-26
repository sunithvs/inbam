from django import forms

from .models import ObjectModel


class ObjectModelForm(forms.ModelForm):
    class Meta:
        model = ObjectModel
        fields = ['file', ]
