"""ECOMMERCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from Login.views import RegisterView, LoginView,ProfileView, LogoutView, LogoutAllView

from Admin.views import AddContactView,ListContactView
from Admin.views import AddCategoryView, AddProductView, EditProductView,DeleteProductView

from Home.views import AddCartView, CheckoutView,ContactInformationView
from Home.views import ListCategoryView, ListProductView, ProductDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [


    path('', ProfileView.as_view()), 
    path('loginuser/', LoginView.as_view()), 
    path('registeruser/', RegisterView.as_view()),
    

    path('category-list/', ListCategoryView.as_view()),
    path('product-list/', ListProductView.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('add-to-cart/', AddCartView.as_view()),
    path('checkout/', CheckoutView.as_view()),
    path('contact-details/', ContactInformationView.as_view()),
    



    path('add-contact/', AddContactView.as_view()),
    path('list-contact/', ListContactView.as_view()),
    

    path('add-category/', AddCategoryView.as_view()),


    path('add-product/', AddProductView.as_view()),
    path('edit-product/<int:pk>/', EditProductView.as_view()),
    path('delete-product/<int:pk>/', DeleteProductView.as_view()),



    path('admin/', admin.site.urls),


    path('token-generate/', TokenObtainPairView.as_view(), name='token-generate'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/',TokenRefreshView.as_view(), name='token-refresh'),

    path('logout/',LogoutView.as_view()),
    path('logout-all/',LogoutAllView.as_view()),
]