from django.db import models

# Create your models here.

class Faq(models.Model):
    title = models.CharField(max_length = 50,null=False,blank=False,default = "")
    question = models.CharField(max_length = 200,null=False,blank=False,default = "")
    answer = models.TextField(null = False,blank = False,default ="")

    def __str__(self):
        return self.title

