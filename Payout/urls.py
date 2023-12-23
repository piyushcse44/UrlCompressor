from django.urls import path
from .views import payout


urlpatterns = [
    path('',payout,name="payout"),

]