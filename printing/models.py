from _decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from auth_login.models import User
from home.models import Address


def create_order_id():
    # create order id in the format ORD00001 , ORD00002 etc
    last_order = Order.objects.all().order_by('id').last()
    if not last_order:
        return 'ORD000001'
    order_id = last_order.id
    new_order_id = int(order_id) + 1
    new_order_id = 'ORD' + str(new_order_id).zfill(6)
    return new_order_id


def create_object_id():
    # create object id in the format OBJ00001 , OBJ00002 etc
    last_object = ObjectModel.objects.all().order_by('id').last()
    if not last_object:
        return 'OBJ00001'
    object_id = last_object.id
    new_object_id = int(object_id) + 1
    new_object_id = 'OBJ' + str(new_object_id).zfill(6)
    return new_object_id


class ObjectModel(models.Model):
    valid_extensions = ['stl', 'STL', 'Stl', 'sTL', 'stL', 'sTl', 'StL', 'STl']
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=create_object_id)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', )
    type = models.CharField(max_length=200, choices=(
        ('metal', 'Metal'),
        ("ornament", "Ornament"),
        ('plastic', 'Plastic'),
    ), default='metal')

    def __str__(self):
        return self.name

    #     validate file extension
    def clean(self):
        if not self.file.name.endswith(tuple(self.valid_extensions)):
            raise ValidationError(u'File not supported!')


# a model for an order of a 3d printing service oline
class Order(models.Model):
    user = models.ForeignKey('auth_login.User', on_delete=models.CASCADE)
    # the name of the order
    name = models.CharField(max_length=200, default=create_order_id)
    # the description of the order
    description = models.TextField(blank=True, null=True)
    # the date of the order
    date = models.DateTimeField(auto_now_add=True)
    # the price of the order
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))],
                                default=0.00)
    # the status of the order
    status = models.CharField(max_length=200, choices=(
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ), default='pending')
    model = models.ForeignKey(ObjectModel, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='order_delivery_address')
    type = models.CharField(max_length=200, choices=(
        ('metal', 'Metal'),
        ("ornament", "Ornament"),
        ('plastic', 'Plastic'),
    ), default='plastic')
    payment_status = models.CharField(max_length=200, choices=(
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ), default='pending')

    # the string representation of the order
    def __str__(self):
        return self.name
