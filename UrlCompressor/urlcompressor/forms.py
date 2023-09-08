from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',"password"]
        labels = {
            'username' : 'UserName',
            'email' : 'Email',
            'password' : 'Password',
        }
       