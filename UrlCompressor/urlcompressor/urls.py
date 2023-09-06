from django.urls import path,include
from  .views import homepage,welcome

urlpatterns =[
    path('',homepage,name="homepage"),
    path('welcome/',welcome,name='welcome'),
    
]


