from rest_framework import serializers
from .models import topicname,topictotoenvirementalist,envirementalistlist

class topicnameserializer(serializers.ModelSerializer):
    class Meta:
        model = topicname
        fields = '__all__'
class topictotoenvirementalistserializer(serializers.ModelSerializer):
    class Meta:
        model = topictotoenvirementalist
        fields = '__all__'
class envirementalistlistserializer(serializers.ModelSerializer):
    class Meta:
        model = envirementalistlist
        fields = '__all__'