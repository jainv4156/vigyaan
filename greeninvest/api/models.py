from django.db import models

class topicname(models.Model):
    topicname = models.CharField(max_length=100)

class topictotoenvirementalist(models.Model):

    topicname = models.CharField(max_length=100)
    envirementalist = models.ForeignKey("api.envirementalistlist", on_delete=models.CASCADE)

class envirementalistlist(models.Model):
    topicname = models.ForeignKey("api.topicname", on_delete=models.CASCADE ,default=1)
    envirementalistid = models.AutoField(primary_key=True)
    envirementalistname = models.CharField(max_length=100)
    envirementalistwebsite=models.URLField()
    # envirementalistemail=models.EmailField()
    # websiteimage=models.ImageField(upload_to='images/')

    
