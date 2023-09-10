from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    return render(request,'home.html')



def user_login(request):

    if request.user.is_authenticated:
        return redirect('profile')
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            print(username)
            user = User.objects.get(username=username) 
        except:
            messages.error(request,'Username Does not Exist')
            return render(request,'user_login.html')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Username or password incorrect')
            return render(request,'user_login.html')

    return render(request,'user_login.html')

def log_out(request):
    logout(request)
    return redirect('user_login')

def signup(request):
    page = 'register'
    form = CustomUserCreationForm()  # Use your custom form here
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("enter")
            user = form.save(commit=False)
            user.save()
            return redirect('homepage')
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='user_login')
def profile(request):
    return render(request,'profile.html')
    


    

# Create your views here.
