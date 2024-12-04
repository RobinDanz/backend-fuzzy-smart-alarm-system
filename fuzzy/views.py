from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from fuzzy.fuzzy_systems import fatigue_level_fuzz, schedule_importance_fuzz, global_system, preferred_wake_method_fuzz, sleep_quality_fuzz
from fuzzy.serializers import AlarmSettingsSerializer

class FuzzyView(APIView):
    def get(self, request, format=None):
        data_sleep_quality = {}
        data_sleep_quality['ambient_noise'] = 0
        data_sleep_quality['bed_quality'] = 5
        data_sleep_quality['stress_level'] = 0

        data_fatigue_level = {}
        data_fatigue_level['last_night_sleep'] = 5
        data_fatigue_level['sleep_dept'] = 5

        fatigue_level_fuzz.process_fatigue_level(data_fatigue_level)
        sleep_quality_fuzz.process_sleep_quality(data_sleep_quality)

        # Prepare input data for schedule_importance (meeting_time and urgent_tasks)
        # data_schedule_importance = {}
        # data_schedule_importance['meeting_time'] = 200  # Example value, you can change this
        # data_schedule_importance['urgent_tasks'] = 7  # Example value, you can change this

        # Prepare input data for preferred_wake_method (sleep_quality and morning_energy)
        # data_preferred_wake_method = {}
        # data_preferred_wake_method['sleep_quality'] = 7  # Example value, you can change this
        # data_preferred_wake_method['morning_energy'] = 8  # Example value, you can change this

        # Process the fuzzy logic for both variables
        # schedule_importance_fuzz.process_schedule_importance(data_schedule_importance)
        # preferred_wake_method_fuzz.process_wake_method(data_preferred_wake_method)

        return Response({'hello': 'world'})
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AlarmSettingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            responseData = global_system.set_alarm_settings(serializer)
            return Response(responseData, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

from rest_framework import generics
from fuzzy.models import AlarmSettings

class AlarmSettingsList(generics.ListCreateAPIView):


    
    serializer_class = AlarmSettingsSerializer

    def get_queryset(self):
        queryset = AlarmSettings.objects.all()

        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(pk=user_id)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class AlarmSettingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlarmSettings.objects.all()
    serializer_class = AlarmSettingsSerializer