from django.db import models
from django.contrib.auth.models import User
from Admin.models import Product
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Cartlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.user.username

class Items(models.Model):
    cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.product)

class Checkout(models.Model):
    CHOICE = ((1,'Cash On Delivery'),(2,'Google Pay'),(3, 'Paytm'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = PhoneNumberField(blank=False)
    address = models.TextField()
    landmark = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = CountryField(multiple=False)
    pincode = models.CharField(max_length=100)
    payment_amount = models.FloatField(default=0)
    payment_method = models.IntegerField(choices=CHOICE)
    created_at = models.DateField(auto_now_add=True) 
    
    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.user.username