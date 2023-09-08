from django.urls import path,include
from  .views import homepage,login,signup,profile,log_out

urlpatterns =[
    path('',homepage,name="homepage"),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',log_out,name="logout"),
    path('profile/',profile,name='profile'),

    
]


