from django.shortcuts import render
from django.http import HttpResponse


data =[
    'Name',
    'Email',
    'Phn_no',
    'Topic',
    'Message'
]


def homepage(request):
    return render(request,'home.html',{'data': data})

def welcome(request):
    return HttpResponse(f'welcome')


    

# Create your views here.
