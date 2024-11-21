from django.shortcuts import render
from django.http import HttpResponse
from . models import Coffee, Product



def home(request):
    products = Product.objects.all()
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'products':products})
