from django.db import models

class Login(models.Model):
    email=models.EmailField(max_length=256, default='')
    password=models.CharField(max_length=90, default='')



def __str__(self):
    return self.email    

