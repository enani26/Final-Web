# app/models/loginn.py
from django.db import models

class Loginn(models.Model):
    email = models.EmailField(max_length=254, default='')
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.email
