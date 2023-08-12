from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.TextChoices):
  PIZZA = 'Pizza'
  BURGER = 'Burger'
  JUICE = 'Juice'

class MenuItem(models.Model):
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.PIZZA)
    name = models.CharField(max_length=100)
    characteristic = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    available = models.BooleanField(default=True)
    datime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} - {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.created_at}"
