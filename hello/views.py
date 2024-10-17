from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Alarm_Settings
from .serializer import AlarmSerializer
from .fuzzySystem import set_alarm_settings


class HelloWorldView(APIView):

    def get(self, request, format=None):
        return Response({'hello': 'world'})


@api_view(['POST'])
def set_alarm_values(request):
    data = request.data
    serializer = AlarmSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        responseData = set_alarm_settings(data)
        return Response(responseData, status= status.HTTP_200_OK)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)