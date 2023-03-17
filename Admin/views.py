from django.shortcuts import render
from Admin.models import Contact, Category, Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import AddContactSerializer, ListContactSerializer
from .serializers import AddCatergorySerializer, AddProductSerializer, EditProductSerializer,DeleteSerializer




class AddProductView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

3
class EditProductView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = EditProductSerializer


class DeleteProductView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = DeleteSerializer



class AddContactView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contact.objects.all()
    serializer_class = AddContactSerializer

 
class ListContactView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Contact.objects.all()
    serializer_class = ListContactSerializer


class AddCategoryView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = AddCatergorySerializer    