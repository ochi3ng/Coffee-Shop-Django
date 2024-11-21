from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Coffee, Cart, CartItem

def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee/coffee_list.html', {'coffees': coffees})

@login_required
def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, coffee=coffee)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'cart_detail.html', {'items': items, 'total': total})
