from rest_framework import serializers
from .models import Alarm_Settings

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm_Settings
        fields = '__all__'