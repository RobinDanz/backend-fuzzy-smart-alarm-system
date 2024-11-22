from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from hello.fuzzy_systems.preferred_wake_method import wake_sim_preferred_wake, preferred_wake_method
# from hello.fuzzy_systems.schedule_importance import wake_sim_schedule, schedule_importance
from .serializer import AlarmSerializer,StaticSettingsSerializer
from .fuzzySystem import set_alarm_settings
from hello.fuzzy_systems import sleep_quality
from hello.fuzzy_systems import fatigue_level


class HelloWorldView(APIView):

    def get(self, request, format=None):
        data_sleep_quality = {}
        data_sleep_quality['ambiant_noise'] = 0
        data_sleep_quality['bed_quality'] = 5
        data_sleep_quality['stress_level'] = 0

        data_fatigue_level = {}
        data_fatigue_level['last_night_sleep'] = 5
        data_fatigue_level['sleep_dept'] = 5

        fatigue_level.process_fatigue_level(data_fatigue_level)


        sleep_quality.process_sleep_quality(data_sleep_quality)


        return Response({'hello': 'world'})

    # def get(self, request, format=None):
    #     # Prepare input data for schedule_importance (meeting_time and urgent_tasks)
    #     data_schedule_importance = {}
    #     data_schedule_importance['meeting_time'] = 6  # Example value, you can change this
    #     data_schedule_importance['urgent_tasks'] = 5  # Example value, you can change this

    #     # Prepare input data for preferred_wake_method (sleep_quality and morning_energy)
    #     data_preferred_wake_method = {}
    #     data_preferred_wake_method['sleep_quality'] = 7  # Example value, you can change this
    #     data_preferred_wake_method['morning_energy'] = 8  # Example value, you can change this

    #     # Process the fuzzy logic for both variables
    #     schedule_importance.simulate_schedule_importance(data_schedule_importance)
    #     preferred_wake_method.simulate_wake_method(data_preferred_wake_method)

    #     # Return the processed response
    #     return Response({
    #         'schedule_importance_result': schedule_importance.simulate_schedule_importance(data_schedule_importance),
    #         'preferred_wake_method_result': preferred_wake_method.simulate_wake_method(data_preferred_wake_method)
    #     })


@api_view(['POST'])
def set_alarm_values(request):
    data = request.data
    serializer = AlarmSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        responseData = set_alarm_settings(data)
        return Response(responseData, status= status.HTTP_200_OK)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def set_static_settings(request):
    data = request.data
    serializer = StaticSettingsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        responseData = {'Static Settings Saved'}
        return Response(responseData, status= status.HTTP_200_OK)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)