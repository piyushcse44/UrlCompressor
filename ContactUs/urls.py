from django.urls import path,include
from .views import contact_us
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', contact_us, name='contact_us'),
        
]
