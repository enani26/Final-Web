from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('add_casheir.html', views.add_casheir, name='add_casheir'),
    path('cashier.html', views.cashier, name='cashier'),
    path('Cashierview.html', views.Cashierview, name='Cashierview'),
    path('Contact.html', views.Contact, name='Contact'),
    path('Orders.html', views.Orders, name='Orders'),
    path('register.html', views.register, name='register'),
    path('menu.html', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
]
