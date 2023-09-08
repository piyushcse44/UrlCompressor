from django.urls import path,include
from  .views import homepage,user_login,signup,profile,log_out

urlpatterns =[
    path('',homepage,name="homepage"),
    path('user_login/',user_login,name='user_login'),
    path('signup/',signup,name='signup'),
    path('logout/',log_out,name="logout"),
    path('profile/',profile,name='profile'),

    
]


