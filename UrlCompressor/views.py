from django.shortcuts import render,redirect
from django.http import JsonResponse
from UrlCompressorApp.models import ListShortUrls
from UrlCompressorApp import const


def home(request):
    data ={}

    if request.method == 'POST':
        my_url = request.POST.get('url')
        data['long_url'] = my_url
        data['custom_back_half_error'] = ""


        return render(request=request,template_name='url-compressor.html',context=data)

    return render(request=request,template_name='home.html')


def short_to_long(request, short_url):
    is_found,long_url = const.find_long_url(short_url=short_url)
    if is_found :
        return redirect(long_url)
    else:
        status_code = 400
        return JsonResponse({'status_code': status_code, 'message': 'The page you are looking for is not available'}, status=status_code)


