<<<<<<< HEAD
from django.shortcuts import render, redirect
from product.models import Pizza
from product.models import Burger
from product.models import Juice
from product.models import MenuItem, CartItem


=======
from django.shortcuts import render
from  product.models import Pizza
from  product.models import Burger
from  product.models import Juice
from . models import Login
>>>>>>> edf09a1596e948c896b4bae3a18788ab4bae42c0

def index(request):
   # dataform = LoginForm(request.POST)
    # dataform.save()
    return render(request, 'apps/index.html')  # {'if': dataform})


def about(request):
    return render(request, 'apps/about.html')


def add_casheir(request):
    return render(request, 'apps/add_casheir.html')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


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


def register(request):
    email = request.POST.get('Email')
    password = request.POST.get('password')
   
    data= Login(email=email,password=password)
    data.save()
    return render(request, 'apps/register.html')


<<<<<<< HEAD
def Signup(request):
    return render(request, 'apps/Signup.html')
=======

>>>>>>> edf09a1596e948c896b4bae3a18788ab4bae42c0


def menu(request):
    return render(request, 'apps/menu.html', {
        'piz': Pizza.objects.all().order_by('name').exclude(available=False),
        'bur': Burger.objects.all().order_by('name').exclude(available=False),
        'ju': Juice.objects.all().order_by('name').exclude(available=False),
    })


def add_to_cart(request, menu_item_id):
    menu_item = MenuItem.objects.get(id=menu_item_id)
    cart_item, created = CartItem.objects.get_or_create(
        menu_item=menu_item, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(cart_item.menu_item.price * cart_item.quantity for cart_item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)
    order.items.set(cart_items)
    cart_items.delete()
    return render(request, 'checkout.html', {'order': order})