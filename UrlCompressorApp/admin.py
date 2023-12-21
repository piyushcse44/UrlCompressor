from django.contrib import admin
from .models import ListShortUrls,CurrentAvaliableUniqueKey,Reserved_pair

# Register your models here.
admin.site.register(ListShortUrls)
admin.site.register(CurrentAvaliableUniqueKey)
admin.site.register(Reserved_pair)

