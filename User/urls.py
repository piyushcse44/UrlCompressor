from django.urls import path,include
from .views import user_login,user_signup,user_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('social-auth/', include('social_django.urls', namespace='social')),
     path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
     path('login/',user_login,name="user_login"),
     path('sign-up/',user_signup,name="user_signup"),
     path('profile/',user_profile,name="user_profile"),

]