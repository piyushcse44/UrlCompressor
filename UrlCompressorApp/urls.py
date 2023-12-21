from django.urls import path,include
from .views import compressor,compressed

urlpatterns = [
     path('compressor/',compressor,name="compressor"),
     path('compressed/<str:short_url>',compressed,name="compressed"),
   

]