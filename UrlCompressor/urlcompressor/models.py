from django.db import models
import uuid


class UrlCompressor(models.Model):
    id = models.UUIDField(default = uuid.uuid4,unique=True,primary_key=True,editable=False)
    OriginalUrl = models.CharField(max_length=250)
    CompressedUrl = models.CharField(max_length=250)
    TimeDate = models.DateTimeField(auto_created=False)

    def __str__(self):
        return self.OriginalUrl
    
    

# Create your models here.
