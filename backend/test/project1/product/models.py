from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.TextChoices):
  PIZZA = 'Pizza'
  BURGER = 'Burger'
  JUICE = 'Juice'

class Pizza(models.Model):
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.PIZZA)
    name = models.CharField(max_length=100)
    characteristic = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    available = models.BooleanField(default=True)
    datime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Burger(models.Model):
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.PIZZA)
    name = models.CharField(max_length=100)
    characteristic = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    available = models.BooleanField(default=True)
    datime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Juice(models.Model):
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.PIZZA)
    name = models.CharField(max_length=100)
    characteristic = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    available = models.BooleanField(default=True)
    datime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name




