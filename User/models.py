from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='user/profile_pic/default.png', upload_to='user/profile_pic/')
    name = models.CharField(max_length=200, null=False, blank=False, default="Anonymous")
    email = models.EmailField(max_length = 200,null=False,blank=False,default = "anonymus@gmail.com")

    def __str__(self):
        return self.email
