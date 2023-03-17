from rest_framework import serializers
from django.contrib.auth.models import User
from Admin.models import Contact, Category, Product, Contact
from Home.models import Cartlist, Checkout, Items

import smtplib
from email.mime.text import MIMEText
from socket import gaierror
from datetime import timedelta



class ProductDetailSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','product_name','description','price','stock','available','picture','offer', 'discount']
    
    def get_discount(self, obj):
        discount = obj.price - (obj.price*obj.offer/100)
        return discount

class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['product']

    def create(self, validated_data):
        user = self.context['request'].user 
        product = self.validated_data['product'] 
        if Cartlist.objects.filter(user=user):
            item = Items.objects.filter(cart__user=user,product=product).first()
            if item:
                item.quantity += 1
                item.save()
                return item
            else:
                item = Items.objects.create(cart=Cartlist.objects.get(user=user),**validated_data)
                item.save()
                return item          
        else:
            cart = Cartlist.objects.create(user=user)
            cart.save()
            item = Items.objects.create(cart=cart,**validated_data)
            item.save()
            return item
        
class CheckoutSerilaiser(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        exclude = ['user']

    def create(self, validated_data):
        user = self.context['request'].user 
        items = Items.objects.filter(cart__user=user)
        total = 0
        if items:
            for i in items:
                total  += (i.quantity * (i.product.price - (i.product.price * i.product.offer/100)))
            checkout = Checkout.objects.create(user=user,payment_amount=total,**validated_data)
            checkout.save()
            
            expect_date = checkout.created_at + timedelta(days=10)
            
            email_from = 'admin@gmail.com'
            email_to = 'jerin@gmail.com'
            email_subject = 'Checkout mail'
            email_body = f"""
            Bill Date : {checkout.created_at}\n
            Expect Date : {expect_date}\n
            Name : {checkout}\n
            Address : {checkout.address}\n
            Mobile Number : {checkout.mobile}\n
            Landmark : {checkout.landmark}\n
            State : {checkout.state}\n
            Country : {checkout.country}\n
            Pincode : {checkout.pincode}\n
            Payment Method : {checkout.get_payment_method_display()}\n
            Total amount : {total}\n\n\n
            Checkout sucessful.
            
            """
            message = MIMEText(email_body)
            message['From'] = email_from
            message['To'] = email_to
            message['Subject'] = email_subject
            smtp_server = 'smtp.mailtrap.io'
            smpt_port = 465
            smtp_username = 'c9afbb9b64a4fe'
            smtp_password = '99d9eb81e7a8ee'
            server = smtplib.SMTP(smtp_server, smpt_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(email_from, email_to, message.as_string())
            server.quit()
            print('Mail send successfully..')
           
            return checkout 
  
class ContactInformationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','user','address','mobile']

    def to_representation(self, instance):
        rep = super(ContactInformationSerialiser, self).to_representation(instance)
        rep['user'] = instance.user.id
        rep['first_name'] = instance.user.first_name
        rep['last_name'] = instance.user.last_name
        rep['email'] = instance.user.email
        return rep
    
class ListCatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

class ListProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','product_name','price','offer','discount']
    def get_discount(self, obj):
        discount = obj.price - (obj.price*obj.offer/100)
        return discount    