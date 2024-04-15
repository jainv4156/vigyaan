from django.shortcuts import render
from django.http import HttpResponse,response
from rest_framework.decorators import api_view
from .models import topicname,topictotoenvirementalist,envirementalistlist
from .serializer import topicnameserializer,topictotoenvirementalistserializer,envirementalistlistserializer
from rest_framework.response import Response

@api_view(['GET'])
def getcatagories(request):
    if request.method == 'GET':
        catagories = topicname.objects.all()
        serializer=topicnameserializer(catagories,many=True)
        return Response({'data':serializer.data})

@api_view(['POST'])
def getenvirementalist(request):
    if request.method == 'POST':
        topicnames=request.data['heading']
        print(topicnames)
        gettopic=topicname.objects.get(topicname=topicnames)
        envirementalists = envirementalistlist.objects.all().filter(topicname=gettopic)
        print(envirementalists)
        # for i in envirementalists:
        #     envirementalistdetail=envirementalistlist.objects.get(envirementalistid=i.envirementalist.envirementalistid)
        #     serializer1=envirementalistlistserializer(envirementalistdetail)
        #     context.append(serializer1.data)

        serializer=envirementalistlistserializer(envirementalists,many=True)
        return Response({'data':serializer.data})