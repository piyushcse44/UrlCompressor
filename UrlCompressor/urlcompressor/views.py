from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm


def homepage(request):
    return render(request,'home.html')



def login(request):

    if request.user.is_authenticated:
        return redirect('profile')
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = user.objects.get(username=username) 
        except:
            messages.error(request,'Username Does not Exist')
            return render(request,'login.html')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home.html')
        else:
            messages.error(request,'Username or password incorrect')
            return render(request,'login.html')

    return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            print("lev 2")
            user = form.save(commit=False)
            user.save()
            return render(request,'login.html')  
     
    return render(request,'signup.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
    


    

# Create your views here.
