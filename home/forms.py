# form of order model
from django import forms

from home.models import Order

#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'description', 'price', 'file', 'delivery_date', 'delivery_address']
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'file': forms.FileInput(attrs={'class': 'form-control'}),
#             'delivery_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
#             'delivery_address': forms.Select(attrs={'class': 'form-control'}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         file = cleaned_data.get('file')
#         if file:
#             if not file.name.endswith(tuple(Order.valid_extensions)):
#                 raise forms.ValidationError(u'File not supported!')
#         return cleaned_data

