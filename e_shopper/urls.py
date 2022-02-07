"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *
from django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexpage),
    path('homepage/',homepage),
    path('signuppage/',signuppage),
    path('signinpage/',signinpage),
    path('signoutpage/',signoutpage),
    path('profilepage/',profilepage),
    path('updateprofile/',updateprofile),
    path('changepassword/',changepassword),
    path('delete/<int:id>/',delete,name="delete"),
    path('search/',search,name='search'),
    path('products/',products,name='products'),
    path('product_details/<int:id>/',product_details,name='product_details'),
    path('place_order/',place_order,name='place_order'),
    path('checkout/',checkout,name='checkout'),
    path('payment/',payment,name="payment"),
    path('contact/',contactus,name="contact"),
    path('about/',aboutus,name="about"),
    path('order/',orderlist,name="order"),
    path('wishlist/',wishlist,name='wishlist'),
    path('order_detail/<int:id>/',order_detail,name="order_detail"),

    
    path('add/<int:id>/', cart_add, name='cart_add'),
    path('item_clear/<int:id>/', item_clear, name='item_clear'),
    path('item_increment/<int:id>/',item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart_clear/',cart_clear, name='cart_clear'),
    path('cart_details/',cart_detail,name='cart_detail'),
]