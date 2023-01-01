from django.core.exceptions import ValidationError
from django.db import models


# to store the delivery address
class Address(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.address


# a model for an order of a 3d printing service oline
class Order(models.Model):
    valid_extensions = ['stl', 'STL', 'Stl', "obj"]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # the name of the order
    name = models.CharField(max_length=200)
    # the description of the order
    description = models.TextField()
    # the date of the order
    date = models.DateTimeField(auto_now_add=True)
    # the price of the order
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # the status of the order
    status = models.CharField(max_length=200, choices=(
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ), default='pending')

    # the file of the order
    file = models.FileField(upload_to='uploads/')
    delivery_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='order_delivery_address')

    # the string representation of the order
    def __str__(self):
        return self.name

    #     validate file extension
    def clean(self):
        if not self.file.name.endswith(tuple(self.valid_extensions)):
            raise ValidationError(u'File not supported!')

