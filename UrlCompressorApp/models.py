from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListShortUrls(models.Model):
    long_url = models.TextField()
  #  unique_key = models.IntegerField(null=False,blank=False)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank = True)
    short_url = models.CharField(max_length =200,default="")
    created_on = models.DateField(auto_now_add = True)


    class Meta:
        indexes = [
 #           models.Index(fields=['uniqwue_key']),
           models.Index(fields=['user']),
           models.Index(fields=['short_url']),

        ]

    def __str__(self):
        return str(self.user)


class CurrentAvaliableUniqueKey(models.Model):
    unique_key = models.IntegerField(default=1)

    def __str__(self):
        return str(self.unique_key)
    
class Reserved_pair(models.Model):
    lower_limit = models.IntegerField()
    upper_limit = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['lower_limit'])

        ]

    def __str__(self):
        return str(self.lower_limit)
    
    









