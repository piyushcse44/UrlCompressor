from django.shortcuts import render
from .models import Faq

# Create your views here.

def faq(request):
    data = {'data' : Faq.objects.all()}
    return render(request=request,template_name='faq.html',context=data)