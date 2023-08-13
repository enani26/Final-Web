from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from product.models import Burger, Juice, Pizza, Category  # Import Category enum
from .models import Loginn  # Import the Loginn model

# Your view functions here...




def index(request):
    return render(request, 'apps/index.html')

def about(request):
    return render(request, 'apps/about.html')

def add_casheir(request):
    return render(request, 'apps/add_casheir.html')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu_item.price *
                      item.quantity for item in cart_items)
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



def Signup(request):
    return render(request, 'apps/Signup.html')

def menu(request):
    return render(request, 'apps/menu.html', {
        'pizza': Pizza.objects.filter(category=Category.PIZZA, available=True).order_by('name'),
        'Burger': Burger.objects.filter(category=Category.BURGER, available=True).order_by('name'),
        'Juice': Juice.objects.filter(category=Category.JUICE, available=True).order_by('name'),
    })

# Your other view logic here



# ...

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = Loginn(email=email, password=password)
        data.save()
        return render(request, 'apps/register.html')
    return render(request, 'apps/register.html')