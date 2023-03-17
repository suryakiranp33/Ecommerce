from django.contrib import admin
from Home import models


@admin.register(models.Cartlist)
class CartAdmin(admin.ModelAdmin):
    fields = ['user',]
    list_display = ['id','user_id']

@admin.register(models.Items)
class ItemsAdmin(admin.ModelAdmin):
    fields = ['cart','product','quantity',]
    list_display = ['id','cart_id','product_id','quantity',]

@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    fields = ['user','mobile', 'address','landmark','state','country', 'pincode', 'payment_amount','payment_method']
    list_display = ['id','user_id','mobile', 'address','landmark','state','country', 'pincode','payment_amount', 'payment_method','created_at']
