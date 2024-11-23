from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Coffee, Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm
from django import forms


def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
         category= Category.objects.get(name=foo)
         product=Product.objects.filter(category=category)
         return render(request, 'category.html', {'products':product, 'category':category})
    except:
        messages.success(request, ("That Category Doesn't Exist...."))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'products':product})

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

def register_user(request):
    if request.method == 'POST':  # Corrected method check
        form = SignUpForm(request.POST)  # Corrected attribute
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']  # Corrected typo
            password = form.cleaned_data['password1']  # Match Django's default UserCreationForm field

            # Log in the user after registration
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Automatically log in the new user
                messages.success(request, "You have registered successfully! Welcome!")
                return redirect('home')
        else:
            messages.error(request, "Oops! Something went wrong. Please try again.")
    else:
        form = SignUpForm()  # Instantiate the form for GET requests

    # Render the registration page with the form
    return render(request, 'register.html', {'form': form})
