from .models import ListShortUrls,CurrentAvaliableUniqueKey,Reserved_pair

#Domin name
domin_name = 'http://127.0.0.1:8000/redirect'
success_msg = "successed"

unavilable_error_msg = 'This Back Half name is already taken!'

base64_dict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31,
    'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39,
    'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47,
    'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55,
    '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '-': 63
}
base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+?"
base64_string = ''.join(base64_characters)




def str_to_base64(short_url):
    current_mult_value = 1
    unique_key = 0
    for val in short_url:
        unique_key += current_mult_value * base64_dict[val]
        current_mult_value*=64
    return unique_key

def base64_to_string(unique_key):
    short_url = ""
    while unique_key > 0 :
        short_url += base64_string[unique_key%64]
        unique_key//=64
    return short_url


def update_unique_key(current_avaliable_unique_key):
    try:
        first_reserved_value = Reserved_pair.objects.earliest('lower_limit')
        if first_reserved_value.lower_limit == current_avaliable_unique_key.unique_key+1 :
            current_avaliable_unique_key.unique_key = first_reserved_value.upper_limit+1
            first_reserved_value.delete()
        else:
            current_avaliable_unique_key.unique_key +=1
    except Reserved_pair.DoesNotExist:
        current_avaliable_unique_key.unique_key +=1

    current_avaliable_unique_key.save()


def find_long_url(short_url):
    try:
        list_short_url_obj = ListShortUrls.objects.get(short_url=short_url)
        long_url = list_short_url_obj.long_url
        return (True,long_url)
    except ListShortUrls.DoesNotExist:
        return (False,short_url)
        

def verify_short_url(short_url):

    unique_key = str_to_base64(short_url=short_url)
    current_avaliable_unique_key = CurrentAvaliableUniqueKey.objects.get()
   
    if current_avaliable_unique_key.unique_key > unique_key :
        return False
    
    if current_avaliable_unique_key.unique_key == unique_key :
        update_unique_key(current_avaliable_unique_key=current_avaliable_unique_key)
        return True
    
    range = Reserved_pair.objects.filter(lower_limit__lte=unique_key, upper_limit__gte=unique_key)

    if range.exists():
        return False
    
    else:
        try:
            right_portion = Reserved_pair.objects.get(lower_limit = unique_key+1)
            try:
                left_portion = Reserved_pair.objects.get(upper_limit = unique_key-1)
                lower_limit = left_portion.lower_limit
                upper_limit = right_portion.upper_limit
                right_portion.delete()
                left_portion.delete()
                Reserved_pair.objects.create(left_portion=lower_limit,right_portion=upper_limit)
            except:
                right_portion.lower_limit -=1
                right_portion.save()  
        except:
            try:
                left_portion = Reserved_pair.objects.get(upper_limit = unique_key-1)
                left_portion.upper_limit +=1
                left_portion.save()
            except:
                Reserved_pair.objects.create(lower_limit=unique_key,upper_limit=unique_key)

    return True



def generate_short_url(request,long_url):
    
    unique_key = CurrentAvaliableUniqueKey.objects.get()
    short_url = base64_to_string(unique_key.unique_key)
    update_unique_key(unique_key)
    ListShortUrls.objects.create(long_url = long_url,user = request.user,short_url = short_url)
    return short_url


def accept_user_short_url(request,long_url,short_url):

    if verify_short_url(short_url=short_url):
        ListShortUrls.objects.create(long_url=long_url,user = request.user,short_url=short_url)
        return short_url
    else:
        return unavilable_error_msg
        
        

def short_url_input_validation(short_url):
    if len(short_url) >=10:
        return "The length of back-half must be less than 10"
    for ch in short_url:
        if ch not in base64_dict:
            return "Pls Enter  Combination of 'a-z' 'A-z' '0-9' '-' only "
    return success_msg   
        

    