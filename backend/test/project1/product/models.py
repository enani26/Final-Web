from django.db import models
from datetime import datetime

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

  

class user(models.Model):

 fname = models.CharField(max_length=50)
 lname = models.CharField(max_length=50)
 email=models.CharField(max_length=500)


 def __str__ (self):  #(self) = call the class
    return self.email  #to be named by the the item name in the admin page
     
     
 

    
