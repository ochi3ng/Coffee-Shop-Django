from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_list, name='coffee_list'),
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
