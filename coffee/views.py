from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Coffee, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def home(request):
    products = Product.objects.all()
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'products':products})


def about (request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return render(request, "login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def logout_user (request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('login')
