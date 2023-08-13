from django.shortcuts import render
from . models import Pizza
from . models import Burger
from . models import Juice
# Create your views here.
def Pizza(request):
    return render(request, 'apps/menu.html')

  
  