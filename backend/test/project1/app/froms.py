from django import forms 
from .models import Login
class LoginForm(forms.modelform):
  class Meta:
    model = Login
    feilds = '__all__'
    
 