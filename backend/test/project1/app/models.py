from django.db import models



class Login(models.Model):
    models.EmailField(default='marwan', max_length=254)
    password= models.CharField( max_length=50)
   

