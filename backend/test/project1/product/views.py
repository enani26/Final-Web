from django.shortcuts import render
from . models import Pizza
from . models import Burger
from . models import Juice
# Create your views here.
def Pizza(request):
    return render(request, 'apps/menu.html')

  
def register(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        data = Login(email=email, password=password)
        data.save()
    return render(request, 'apps/register.html')