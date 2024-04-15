from django.contrib import admin

# Register your models here
from .models import topicname,topictotoenvirementalist,envirementalistlist
admin.site.register(topicname)
admin.site.register(topictotoenvirementalist)
admin.site.register(envirementalistlist)
