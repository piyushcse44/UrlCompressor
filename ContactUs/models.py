from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200,null=False,blank=False,default="No Name")
    email = models.EmailField(max_length=200,null=False,blank=False,default="NoName@gmail.com")
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-created_on']

    def __str__(self):
        return self.full_name     




