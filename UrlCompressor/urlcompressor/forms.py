from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Specify the model for the form (User in this case)
        fields = ('username', 'email', 'password1', 'password2')  # Specify the order of fields
       
        # Add more customization options as needed
