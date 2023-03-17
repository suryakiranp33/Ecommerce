from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = PhoneNumberField(blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.user


class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.category_name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField()
    picture = models.ImageField(upload_to='product')
    offer = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name