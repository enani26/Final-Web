from django.shortcuts import render
from  product.models import Pizza
from  product.models import Burger
from  product.models import Juice


def index(request):
    return render(request,'apps/index.html')
    
def about(request):
    return render(request,'apps/about.html')

def add_casheir(request):
    return render(request,'apps/add_casheir.html')

def cart(request):
    return render(request,'apps/Cart.html')

def cashier(request):
    return render(request,'apps/cashier.html')

def Cashierview(request):
    return render(request,'apps/Cashierview.html')

def Contact(request):
    return render(request,'apps/Contact.html')

def Login(request):
    return render(request,'apps/Login.html')

def Orders(request):
    return render(request,'apps/Orders.html')

def qc_cashier(request):
    return render(request,'apps/quality_control_cashier.html')

def qc_users(request):
    return render(request,'apps/quality_control_users.html')

def qc_view(request):
    return render(request,'apps/quality_control_view.html')

def register(request):
    return render(request,'apps/register.html')    

def Signup(request):
    return render(request,'apps/Signup.html')

def menu(request):
    return render(request,'apps/menu.html', {'piz':Pizza.objects.all().order_by('name').exclude(available=False),'bur':Burger.objects.all().order_by('name').exclude(available=False),'ju':Juice.objects.all().order_by('name').exclude(available=False)})


# Create your views here.
