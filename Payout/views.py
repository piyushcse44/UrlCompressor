from django.shortcuts import render

# Create your views here.

def payout(request):
    return render(request=request,template_name='payout-rates.html')
