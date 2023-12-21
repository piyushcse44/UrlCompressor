from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Profile
from UrlCompressorApp.models import ListShortUrls
from UrlCompressorApp import const



# Create your views here.
def user_login(request):   

    if request.user.is_authenticated:
        return redirect('user_profile')
    
    data ={}
    
    if request.method == "POST":
        username = request.POST.get("email",'-1')
        password = request.POST.get("password","-1")
        data['email'] = username
        try:
            user = User.objects.get(username = username)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return redirect('user_profile')
            else:
                data['login_error_msg'] = "UserName or Password is Incorrect"
        except User.DoesNotExist:
                data['login_error_msg'] = "User is Not registered"
            
    return render(request=request,template_name='sign-in.html',context=data)


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('user_profile')
        else:
            # Form is not valid, display errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request=request, template_name='sign-up.html', context={'form': form})

    
    

    

@login_required(login_url="user_login")
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    url_list = ListShortUrls.objects.filter(user = user)
    data ={
        "profile" : profile,
         "url_list" : url_list,
         'domin_name':const.domin_name
    }
    return render(request,'profile.html',data)