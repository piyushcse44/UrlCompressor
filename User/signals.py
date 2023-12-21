from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save,sender=User)
def profile_update(sender,instance,created,**kwargs):
    if created == True:
        email = instance.email
        if email == "":
            email = instance.username
        Profile.objects.create(
            user = instance,
            email = email,
        )


@receiver(post_delete,sender = Profile)
def delete_user_when_profile_deleted(sender,instance,**kwargs):
    user = instance.user
    user.delete()
 



