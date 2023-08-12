from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),

path('about.html',views.about,name='about'),

path('add_casheir.html',views.add_casheir,name='add_casheir'),

path('Cart.html', views.cart, name='cart'),

path('checkout.html',views.checkout,name='checkout'),

path('cashier.html',views.cashier,name='cashier'),

path('Cashierview.html',views.Cashierview,name='Cashierview'),

path('Contact.html',views.Contact,name='Contact'),

path('Login.html',views.Login,name='Login'),

path('Orders.html',views.Orders,name='Orders'),

path('register.html',views.register,name='register'),

path('menu.html',views.menu,name='menu'),


 path('menu/', views.menu, name='menu'),
    path('add-to-cart/<int:menu_item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),

]