

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Loginn
from product.models import MenuItem, CartItem, Order, Category  # Import Category enum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User





def index(request):
    return render(request, 'apps/index.html')

def about(request):
    return render(request, 'apps/about.html')

def add_casheir(request):
    return render(request, 'apps/add_casheir.html')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def cashier(request):
    return render(request, 'apps/cashier.html')

def Cashierview(request):
    return render(request, 'apps/Cashierview.html')

def Contact(request):
    return render(request, 'apps/Contact.html')


def Orders(request):
    return render(request, 'apps/Orders.html')

def qc_cashier(request):
    return render(request, 'apps/quality_control_cashier.html')

def qc_users(request):
    return render(request, 'apps/quality_control_users.html')

def qc_view(request):
    return render(request, 'apps/quality_control_view.html')

def register(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        pw = request.POST.get('password')
        data = Loginn(email=em, password=pw)
        data.save()
        
        # You can add any additional fields and attributes to the User model here

    return render(request, 'apps/register.html')



@login_required
def menu(request):
    piz = MenuItem.objects.filter(category=Category.PIZZA, available=True).order_by('name')
    bur = MenuItem.objects.filter(category=Category.BURGER, available=True).order_by('name')
    ju = MenuItem.objects.filter(category=Category.JUICE, available=True).order_by('name')

    # Your other view logic here

    return render(request, 'menu.html', {'piz': piz, 'bur': bur, 'ju': ju})

@login_required
def add_to_cart(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    cart_item, created = CartItem.objects.get_or_create(
        menu_item=menu_item,
        user=request.user,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        for cart_item in cart_items:
            order.items.add(cart_item)
        cart_items.delete()
        return redirect('view_cart')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})





def index(request):
    return render(request, 'apps/index.html')

def about(request):
    return render(request, 'apps/about.html')

def add_casheir(request):
    return render(request, 'apps/add_casheir.html')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def cashier(request):
    return render(request, 'apps/cashier.html')

def Cashierview(request):
    return render(request, 'apps/Cashierview.html')

def Contact(request):
    return render(request, 'apps/Contact.html')

def Login(request):
    return render(request, 'apps/Login.html')

def Orders(request):
    return render(request, 'apps/Orders.html')

def qc_cashier(request):
    return render(request, 'apps/quality_control_cashier.html')

def qc_users(request):
    return render(request, 'apps/quality_control_users.html')

def qc_view(request):
    return render(request, 'apps/quality_control_view.html')


 



@login_required
def menu(request):
    piz = MenuItem.objects.filter(category=Category.PIZZA, available=True).order_by('name')
    bur = MenuItem.objects.filter(category=Category.BURGER, available=True).order_by('name')
    ju = MenuItem.objects.filter(category=Category.JUICE, available=True).order_by('name')

    return render(request, 'menu.html', {'piz': piz, 'bur': bur, 'ju': ju})

@login_required
def add_to_cart(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    cart_item, created = CartItem.objects.get_or_create(
        menu_item=menu_item,
        user=request.user,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_price)
        for cart_item in cart_items:
            order.items.add(cart_item)
        cart_items.delete()
        return redirect('view_cart')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})





