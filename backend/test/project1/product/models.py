from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Pizza(models.Model):
 cat = [
     ('Pizza','Pizza') ,
     ('Burger','Burger'),
     ('Juice','Juice'),
   ]
   
 name = models.CharField(max_length=50)
 Characteristic  = models.TextField(null=True,blank=True) #null,blank means that this field is not required
 price = models.DecimalField(max_digits=5,decimal_places=1)
 image = models.ImageField(upload_to = 'photos/%y/%m/%d')
 available = models.BooleanField(default=True) #available or not 
 category = models.CharField(max_length=50,null=True , blank=True,choices=cat)
 datime=models.DateTimeField(default=datetime.now)


 def __str__ (self):  #(self) = call the class
    return self.name  #to be named by the the item name in the admin page
     



class Burger(models.Model):
   
   
 cat = [
     ('Pizza','Pizza') ,
     ('Burger','Burger'),
     ('Juice','Juice'),
   ]


 name = models.CharField(max_length=50)
 Characteristic  = models.TextField(null=True,blank=True) #null,blank means that this field is not required
 price = models.DecimalField(max_digits=5,decimal_places=1)
 image = models.ImageField(upload_to = 'photos/%y/%m/%d')
 available = models.BooleanField(default=True) #available or not 
 category = models.CharField(max_length=50,null=True , blank=True,choices=cat)
 datime=models.DateTimeField(default=datetime.now)


 
 def __str__ (self):  #(self) = call the class
    return self.name  #to be named by the the item name in the admin page
     
 
 
  
 

class Juice(models.Model):
   
 cat = [
     ('Pizza','Pizza') ,
     ('Burger','Burger'),
     ('Juice','Juice'),
   ]


 name = models.CharField(max_length=50)
 Characteristic  = models.TextField(null=True,blank=True) #null,blank means that this field is not required
 price = models.DecimalField(max_digits=5,decimal_places=1)
 image = models.ImageField(upload_to = 'photos/%y/%m/%d')
 available = models.BooleanField(default=True) #available or not  
 category = models.CharField(max_length=50,null=True , blank=True,choices=cat)
 datime=models.DateTimeField(default=datetime.now)
 
 def __str__ (self):  #(self) = call the class
    return self.name  #to be named by the the item name in the admin page

  
class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=6, decimal_places=2)
 
  def __str__ (self):  #(self) = call the class
       return self.name  #to be named by the the item name in the admin page

     

class CartItem(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
  def __str__ (self):  #(self) = call the class
       return self.name  #to be named by the the item name in the admin page

 

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  items = models.ManyToManyField(CartItem)
  total_price = models.DecimalField(max_digits=8, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__ (self):  #(self) = call the class
      return self.name  #to be named by the the item name in the admin page

  
     
 

    
