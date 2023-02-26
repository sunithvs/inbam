from django import forms

from .models import ObjectModel


class ObjectModelForm(forms.ModelForm):
    class Meta:
        model = ObjectModel
        fields = ['name', 'file', 'type']

    def validate(self):
        if self.cleaned_data['type'] == 'type1' and self.cleaned_data['file'] is None:
            raise forms.ValidationError('File is required for type1')
        return self.cleaned_data
