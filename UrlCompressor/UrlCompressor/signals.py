from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings



def Post_update_signup(sender,instance,created,**kwargs):
    email =[instance.email]
    send_mail(
        'Created account in UrlCompresser',
        'Welcome To UrlCompressor',
        settings.EMAIL_HOST_USER,
        email,
        fail_silently=False,
    )





post_save.connect(Post_update_signup,sender= User)    