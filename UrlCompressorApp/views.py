from django.shortcuts import render,redirect
from UrlCompressorApp import const
from django.http import JsonResponse

def compressor(request):
    data = {}
    data['custom_back_half_error'] = ''
    data['custom_url'] = const.domin_name

    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        custom_back_half = request.POST.get('custom_back_half')
        error_msg = const.short_url_input_validation(custom_back_half)
        if error_msg != const.success_msg:
            data['custom_back_half_error'] = error_msg
        else:
            if custom_back_half == "" or const.accept_user_short_url(request=request,long_url=long_url,short_url=custom_back_half) == custom_back_half:
                if custom_back_half == "": 
                    custom_back_half = const.generate_short_url(long_url=long_url,request=request)    
                return redirect('compressed',short_url = custom_back_half)
            else:
                data['custom_back_half_error'] = const.unavilable_error_msg
        data['long_url'] = long_url
        data['custom_back_half'] = custom_back_half


    return render(request, 'url-compressor.html', data)

def compressed(request,short_url):
    is_found,long_url = const.find_long_url(short_url=short_url)
    if is_found :
        data ={}
        data['long_url'] = long_url
        data['short_url'] = f"{const.domin_name.rstrip('/')}/{short_url.lstrip('/')}"
        return render(request,'compressed-url.html',data)
    else:
        status_code = 400
        return JsonResponse({'status_code': status_code, 'message': 'The page you are looking for is not available'}, status=status_code)


